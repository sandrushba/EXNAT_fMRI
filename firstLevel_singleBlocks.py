import os
import glob
import numpy as np
import pandas as pd
import nibabel as nib
from pathlib import Path
from nilearn import image
from nilearn.glm.first_level import make_first_level_design_matrix, FirstLevelModel
from nilearn.interfaces.fmriprep import load_confounds
from nilearn.interfaces.bids import save_glm_to_bids
from nilearn import plotting, datasets


def list_subject_folders(preproc_dir):
    """
    List all subfolders in the preprocessing directory starting with 'sub-YA'.
    """
    return [name for name in os.listdir(preproc_dir)
            if os.path.isdir(os.path.join(preproc_dir, name)) and name.startswith('sub-YA')]

def find_func_nifti(directory_path, run):
    """
    Find a NIfTI file in the specified directory that contains all search strings
    and ends with '_space-MNI152NLin2009cAsym_res-2_desc-preproc_bold.nii.gz'.
    """
    # Adjust search strings for multiple conditions
    if run == 'back_single':
        search_strings = ['back', 'single']
    else:
        search_strings = [run]

    for file_name in os.listdir(directory_path):
        if all(s in file_name for s in search_strings) and file_name.endswith('_space-MNI152NLin2009cAsym_res-2_desc-preproc_bold.nii.gz'):
            return os.path.join(directory_path, file_name)
    return None

def load_logfile(stats_dir, sub_ID, run):
    # Read logfile
    logfile = glob.glob(os.path.join(stats_dir, sub_ID, 'behavior/fMRI_exp/', '*.csv'))
    logfile_data = pd.read_csv(logfile[0])

    # Drop unnecessary columns
    trigger_count_index = logfile_data.columns.get_loc("TriggerCount")
    logfile_data = logfile_data.drop(columns=logfile_data.columns[:trigger_count_index])
    logfile_data = logfile_data.drop(columns=["expName", "frameRate", "psychopyVersion"])

    return logfile_data

def make_design_matrix(stats_dir, sub_ID, run):
    # Load the logfile
    logfile_data = load_logfile(stats_dir, sub_ID, run)

    # Adjust search strings for multiple conditions
    if run == 'back_single':
        search_strings = ['back', 'single']
    else:
        search_strings = [run]

    # Determine the start time of the first trial
    first_trial_df = logfile_data[
        logfile_data["block_name"].apply(lambda x: isinstance(x, str) and all(s in x for s in search_strings)) &
        (logfile_data["trial_nr"] == 1)
    ]

    # Now calculate durations of each block
    if run == "Reading":
        # Filter for trials with "pseudo" in the block name and trial number 100
        pseudo_trials = logfile_data[
            logfile_data["block_name"].apply(
                lambda x: isinstance(x, str) and "pseudo" in x and all(s in x for s in search_strings)) &
            (logfile_data["trial_nr"] == 100)
            ]

        # Filter for trials without "pseudo" in the block name and trial number 300
        reading_trials = logfile_data[
            logfile_data["block_name"].apply(
                lambda x: isinstance(x, str) and "pseudo" not in x and all(s in x for s in search_strings)) &
            (logfile_data["trial_nr"] == 300)
            ]

        # Combine both DataFrames
        last_trial_df = pd.concat([reading_trials, pseudo_trials])
    elif run == "back_single":
        last_trial_df = logfile_data[
            logfile_data["block_name"].apply(lambda x: isinstance(x, str) and all(s in x for s in search_strings)) &
            (logfile_data["trial_nr"] == 60)
        ]

    # Merge both into one df to calculate durations
    merged_df = pd.merge(first_trial_df, last_trial_df, on="block_nr_exp", suffixes=("_first", "_last"))

    # Calculate durations
    merged_df["duration"] = merged_df["onset_time_rel2trigger_last"] - merged_df["onset_time_rel2trigger_first"]

    # Add onsets, durations, and condition to our events df
    events_df = merged_df[["onset_time_rel2trigger_first", "duration", "block_name_first"]]

    # Rename columns
    events_df = events_df.rename(columns={
        "onset_time_rel2trigger_first": "onset",
    })

    # Create shorter version of block names
    events_df["trial_type"] = events_df["block_name_first"].apply(lambda x: '_'.join(x.split('_')[:2]))

    # Drop the old column
    events_df = events_df.drop(columns=["block_name_first"])

    # Write df to csv file
    output_dir = os.path.join(stats_dir, sub_ID, "1st_level_SingleBlocks")
    write_results_to_csv(events_df, output_dir, sub_ID, run)

    return events_df

def write_results_to_csv(events_df, output_dir, sub_ID, run):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_path = os.path.join(output_dir, f"{sub_ID}_{run}_design_matrix.csv")

    events_df.to_csv(file_path, index=False)
    print(f"Design matrix for {run} written to {file_path}")

def load_design_matrix(stats_dir, sub_ID, run):
    file_path = os.path.join(stats_dir, sub_ID, "1st_level_SingleBlocks", f"{sub_ID}_{run}_design_matrix.csv")

    events = pd.read_csv(file_path)

    return events

def load_add_regressors(stats_dir, sub_ID, run):
    file_path = os.path.join(stats_dir, sub_ID, "1st_level_SingleBlocks", f"{sub_ID}_{run}.csv")

    add_regressors = pd.read_csv(file_path)

    return add_regressors

def calculate_n_volumes(stats_dir, func_dir, sub_ID, run, tr):
    # Adjust search strings for multiple conditions
    if run == 'back_single':
        search_strings = ['back', 'single']
    else:
        search_strings = [run]

    # Find the functional NIfTI file
    func_file = find_func_nifti(func_dir, run)

    if func_file:
        # Read and smooth NIfTI image
        img = image.load_img(func_file)

        # Get the number of volumes
        num_volumes = img.shape[-1]

        # Calculate the time for each volume
        volume_times = [i * tr for i in range(num_volumes)]

        # We need to check if the volume is longer than the actual experiment, meaning the scanner was running longer
        # than intended and we might need to cut some volumes at the end
        logfile_data = load_logfile(stats_dir, sub_ID, run)

        # Check for end of trials in this run (= onset + duration)
        # Now calculate durations of each block
        if run == "Reading":
            # Filter for trials with "pseudo" in the block name and trial number 100
            pseudo_trials = logfile_data[
                logfile_data["block_name"].apply(
                    lambda x: isinstance(x, str) and "pseudo" in x and all(s in x for s in search_strings)) &
                (logfile_data["trial_nr"] == 100)
                ]

            # Filter for trials without "pseudo" in the block name and trial number 300
            reading_trials = logfile_data[
                logfile_data["block_name"].apply(
                    lambda x: isinstance(x, str) and "pseudo" not in x and all(s in x for s in search_strings)) &
                (logfile_data["trial_nr"] == 300)
                ]

            # Combine both DataFrames
            last_trial_df = pd.concat([reading_trials, pseudo_trials])
        elif run == "back_single":
            last_trial_df = logfile_data[
                logfile_data["block_name"].apply(lambda x: isinstance(x, str) and all(s in x for s in search_strings)) &
                (logfile_data["trial_nr"] == 60)
                ]

        last_trial_time = last_trial_df.iloc[-1]["onset_time_rel2trigger"] + last_trial_df.iloc[-1]["duration"]/1000

        # Now find the index of the volume that was recorded next after end of the experiment in this run
        index = None
        for i in range(len(volume_times)):
            if volume_times[i] > last_trial_time:
                index = i
                break
            else:
                index = len(volume_times)

        # Check if the index corresponds to the overall length of the functional scan
        if len(volume_times) == index:
            return volume_times, img
        elif len(volume_times) > index:
            # We need to shorten the functional scan
            shorter_func_image = shorten_func_scans(func_dir, run, index)

            # Read and smooth NIfTI image
            img = image.load_img(shorter_func_image)

            # Get the number of volumes
            num_volumes = img.shape[-1]

            # Calculate the time for each volume
            volume_times = [i * tr for i in range(num_volumes)]

            return volume_times, img

def shorten_func_scans(func_dir, run, index):
    # Find the functional NIfTI file
    func_file = find_func_nifti(func_dir, run)

    if func_file:
        img = nib.load(func_file)

        # Get the data array from the image
        data = img.get_fdata()

        # Shorten the data by slicing from the start to the specified index
        shortened_data = data[..., :index]

        # Create a new NIfTI image with the shortened data
        shortened_img = nib.Nifti1Image(shortened_data, img.affine, img.header)

        # Save the shortened image to a new file
        path = Path(func_file)
        if path.suffix == '.gz' and path.with_suffix('').suffix == '.nii':
            shortened_file_path = path.with_name(path.stem[:-4] + "_shortened.nii.gz")
        else:
            shortened_file_path = path.with_name(path.stem + "_shortened" + path.suffix)

        # Save the shortened image to the new file
        nib.save(shortened_img, shortened_file_path)

        return shortened_file_path

def make_instructions_regressor(stats_dir, sub_ID, run):
    logfile_data = load_logfile(stats_dir, sub_ID, run)

    # Define the number of blocks for each task
    block_counts = {
        'Reading': 2,
        'back_single': 4
    }

    # Adjust search strings for multiple conditions
    if run == 'back_single':
        search_strings = ['back', 'single']
    else:
        search_strings = [run]

    # Find the onset_time_rel2trigger for the first trial which also gives the duration of the first instructions
    first_trial_df = logfile_data[
        logfile_data["block_name"].apply(lambda x: isinstance(x, str) and all(s in x for s in search_strings)) &
        (logfile_data["TriggerCount"] == 1)
        ]

    instructions_df = pd.DataFrame()
    instructions_df["onset"] = [0]
    instructions_df["duration"] = first_trial_df.iloc[0]["onset_time_rel2trigger"]
    instructions_df["trial_type"] = "instructions"

    # Loop over each block within the task
    for block_nr in range(1, block_counts[run] + 1):
        # Determine trial numbers based on block type and block number
        if run == 'Reading':
            trial_end_nr = 300 if block_nr == 1 else 100
        else:
            trial_end_nr = 60

        # Get end times for each run
        run_end = logfile_data[
            (logfile_data["block_name"].apply(
                lambda x: isinstance(x, str) and all(s in x for s in search_strings))) &
            (logfile_data["block_nr_run"] == block_nr) &
            (logfile_data["trial_nr"] == trial_end_nr)
            ]

        if not run_end.empty:
            run_end_time = run_end.iloc[0]["onset_time_rel2trigger"] + run_end.iloc[0]["duration"]/1000

            # Identify volumes during the break for other blocks
            if block_nr < block_counts[run]:  # Only check for breaks if not the last block
                next_block_start = logfile_data[
                    (logfile_data["block_name"].apply(lambda x: isinstance(x, str) and all(
                        s in x for s in search_strings))) &
                    (logfile_data["block_nr_run"] == block_nr + 1) &
                    (logfile_data["trial_nr"] == 1)
                    ]
                if not next_block_start.empty:
                    next_block_start_time = next_block_start.iloc[0]["onset_time_rel2trigger"]
                    last_question_end_time = next_block_start_time - 8.75

                    if run == 'Reading' and last_question_end_time < next_block_start_time:
                        new_row = {
                            "onset": last_question_end_time,
                            "duration": next_block_start_time - last_question_end_time,
                            "trial_type": "instructions"
                        }

                        # Append the new row to the DataFrame
                        instructions_df = instructions_df._append(new_row, ignore_index=True)

                    elif run != 'Reading' and run_end_time < next_block_start_time:
                        new_row = {
                            "onset": run_end_time,
                            "duration": next_block_start_time - run_end_time,
                            "trial_type": "instructions"
                        }

                        # Append the new row to the DataFrame
                        instructions_df = instructions_df._append(new_row, ignore_index=True)

    return instructions_df

def make_questions_regressor(stats_dir, sub_ID, run):
    logfile_data = load_logfile(stats_dir, sub_ID, run)

    # Define the number of blocks for each task
    block_counts = {
        'Reading': 2,
    }

    search_strings = [run]

    # Loop over each block within the task
    for block_nr in range(1, block_counts[run] + 1):

        # Identify questions after the first run
        if block_nr == 1:
            questions = logfile_data[
                logfile_data["question"].apply(lambda x: isinstance(x, str) and x.startswith('Q')) &
                (logfile_data["block_name"].apply(
                    lambda x: isinstance(x, str) and all(s in x for s in search_strings)))
                ]
            if not questions.empty:
                first_question_time = questions.iloc[0]["onset_time_rel2trigger"]
                next_block_start = logfile_data[
                    (logfile_data["block_name"].apply(
                        lambda x: isinstance(x, str) and all(s in x for s in search_strings))) &
                    (logfile_data["block_nr_run"] == 2) &
                    (logfile_data["trial_nr"] == 1)
                    ].iloc[0]["onset_time_rel2trigger"]
                last_question_end_time = next_block_start - 8.75

                questions_df = pd.DataFrame()
                questions_df["onset"] = [first_question_time]
                questions_df["duration"] = [last_question_end_time - first_question_time]
                questions_df["trial_type"] = "questions"

                return questions_df

def choose_confounds(func_dir, run, strategy, n_vols):

    file_path = find_func_nifti(func_dir, run)

    confounds, sample_mask = load_confounds(file_path, strategy=strategy, motion="basic", scrub=0, fd_threshold=0.7, std_dvars_threshold=3)

    # Check if length of confounds matches length of functional scan
    if confounds.shape[0] == n_vols:
        return confounds, sample_mask
    # if not, shorten confounds and sample mask to match length
    elif confounds.shape[0] > n_vols:
        confounds = confounds.iloc[:n_vols]

        return confounds, sample_mask

def make_gm_mask(preproc_dir, sub_ID):
    gm_img = glob.glob(os.path.join(preproc_dir, sub_ID, sub_ID, "anat", "*_space-MNI152NLin2009cAsym_res-2_label-GM_probseg.nii.gz"))

    # Threshold the probabilistic GM mask
    binary_gm_mask = image.binarize_img(gm_img, threshold=0.05, copy_header=True)

    return binary_gm_mask

def make_contrasts(design_matrix, run):
    contrast_matrix = np.eye(design_matrix.shape[1])
    basic_contrasts = {
        column: contrast_matrix[i]
        for i, column in enumerate(design_matrix.columns)
    }

    if run == "Reading":
        contrasts_matrix = {
            "Text vs Pseudotext": basic_contrasts["Reading_Baseline"] - basic_contrasts["Reading_pseudotext"],
            "Pseudotext vs Text": -basic_contrasts["Reading_Baseline"]
                              + basic_contrasts["Reading_pseudotext"],
            "effects_of_interest": np.vstack(
                (basic_contrasts["Reading_Baseline"], basic_contrasts["Reading_pseudotext"])
            )
        }
    elif run == "back_single":
        contrasts_matrix = {
            "1back vs 2back": basic_contrasts["1back_single"] - basic_contrasts["2back_single"],
            "2back vs 1back": -basic_contrasts["1back_single"]
                              + basic_contrasts["2back_single"],
            "effects_of_interest": np.vstack(
                (basic_contrasts["1back_single"], basic_contrasts["2back_single"])
            ),
        }

    return contrasts_matrix

def main():
    # Configuration
    preproc_dir = '/data/p_02956/EXNAT_3_Data/derivatives/fmriprep-preproc/'
    stats_dir = '/data/p_02956/EXNAT_3_Data/derivatives/fmriprep-stats/subjects'
    tr = 1.75
    runs = ['Reading', 'back_single']

    # The hemodynamic response function
    hrf_model = "spm + derivative"
    # We use a discrete cosine transform to model signal drifts. Use cosine together with high pass filter (
    # https://neurostars.org/t/first-level-glm-using-nilearn-high-pass-filtering-cosine-drift-model-and-cosine-xx
    # -regressors-in-the-design-matrix/19469)
    drift_model = None
    # The cutoff for the drift model is 0.01 Hz.
    high_pass = None

    # Define strategy for confound selection
    # We use 6 motion regressors, cosine regressors from fMRIPrep, and individual regressors for excessive motion
    strategy = ["motion", "high_pass", "scrub"]

    # For plotting
    template_img = datasets.load_mni152_template(resolution=2)

    # List all subject folders
    subject_folders = list_subject_folders(preproc_dir)

    # Process each subject
    for sub_ID in subject_folders:
        print(f"This is subject: {sub_ID}")

        design_matrices = [] # list of design matrices for 1st-level (one per run)
        func_imgs = [] # list of functional runs for 1st-level
        sample_masks = [] # list of sample images for motion scrubbing per run
        contrasts = []

        # Load a subject-specific GM mask, threshold and binarize it
        gm_mask_binary = make_gm_mask(preproc_dir, sub_ID)

        for run in runs:
            print(f"This is run: {run}")
            make_design_matrix(stats_dir, sub_ID, run)

            # Now load file for design matrix
            events = load_design_matrix(stats_dir, sub_ID, run)

            # Load additional regressors for instructions and questions if there were questions
            if run == "Reading":
                questions_df = make_questions_regressor(stats_dir, sub_ID, run)
                instructions_df = make_instructions_regressor(stats_dir, sub_ID, run)

                # Bind with events df
                events = pd.concat([events, questions_df, instructions_df], ignore_index=True)

            elif run == "back_single":
                instructions_df = make_instructions_regressor(stats_dir, sub_ID, run)

                # Bind with events df
                events = pd.concat([events, instructions_df], ignore_index=True)

            # Now load functional file to specify times of volumes
            func_dir = os.path.join(preproc_dir, sub_ID, sub_ID, 'func')

            vol_times, img = calculate_n_volumes(stats_dir, func_dir, sub_ID, run, tr)
            vol_times = np.array(vol_times)

            # Append functional image to list
            func_imgs.append(img)

            print(f"Functional file loaded for Subject: {sub_ID}, Block: {run}, Number of volumes: {len(vol_times)}")

            # Load confounds and choose which confounds we add to our first level
            confounds, sample_mask = choose_confounds(func_dir, run, strategy, len(vol_times))

            # Now build design matrix
            design_matrix = make_first_level_design_matrix(
                vol_times,
                events,
                hrf_model=hrf_model,
                drift_model=drift_model,
                high_pass=high_pass,
                add_regs=confounds,
                oversampling=50
            )

            # put the design matrices in a list
            design_matrices.append(design_matrix)

            plotting.plot_design_matrix(design_matrix)
            plotting.show()

            # If we want to use the additional motion scrubbing provided through the sample mask coming out of our
            # confound definition, we need to align the length of the sample mask with the actual number of scans in
            # our functional image Filter indices to remove those that exceed the number of scans
            num_scans = img.shape[3] # count number of scans
            if sample_mask is None:
                # Create a default mask covering all scans if none exists
                sample_mask_corrected = np.arange(num_scans)
            else:
                filtered_indices = sample_mask[sample_mask < num_scans] # check for alignment
                sample_mask_corrected = filtered_indices
            sample_masks.append(sample_mask_corrected) # append to list of sample masks

            contrast_dict = make_contrasts(design_matrix, run)
            contrasts.append(contrast_dict)

            print(f"Fitting a GLM for run: {run}")
            fmri_glm = FirstLevelModel(t_r=tr,
                                       slice_time_ref=0.5,  # fMRIPrep sets the middle slice as reference during slice
                                       # time correction to account for this
                                       smoothing_fwhm=5,
                                       subject_label=sub_ID,
                                       drift_model=None,  # no additional drift because we're already using cosine
                                       # regressors from fmriprep
                                       hrf_model=hrf_model,
                                       mask_img=gm_mask_binary,
                                       minimize_memory=False) # so we also get residuals and r2
            # Fit GLM
            fmri_glm = fmri_glm.fit(run_imgs=img,
                                    design_matrices=design_matrix,
                                    sample_masks=sample_mask_corrected)

            # Save model output together with contrast images in stats directory
            output_dir = os.path.join(stats_dir, sub_ID, "1st_level_SingleBlocks")
            save_glm_to_bids(model=fmri_glm,
                             contrasts=contrast_dict,
                             out_dir=output_dir,
                             prefix=sub_ID+"_"+run,
                             plot_type="glass")

        print(f"Now fitting a GLM for both runs!")
        fmri_glm = FirstLevelModel(t_r=tr,
                                   slice_time_ref=0.5, # fMRIPrep sets the middle slice as reference during slice
                                   # time correction to account for this
                                   smoothing_fwhm=5,
                                   subject_label=sub_ID,
                                   drift_model=None, # no additional drift because we're already using cosine
                                   # regressors from fmriprep
                                   hrf_model=hrf_model,
                                   mask_img=gm_mask_binary,
                                   minimize_memory=False)

        fmri_glm = fmri_glm.fit(run_imgs=func_imgs,
                                design_matrices=design_matrices,
                                sample_masks=sample_masks)

        Reading_Nback = [
            np.array([[1, 0, 1] + (len(design_matrices[0].columns)-3)*[0]]),
            np.array([[-1, 0, -1] + (len(design_matrices[1].columns)-3)*[0]]),
        ]
        Nback_Reading = [
            np.array([[-1, 0, -1] + (len(design_matrices[0].columns)-3) * [0]]),
            np.array([[1, 0, 1] + (len(design_matrices[1].columns)-3) * [0]]),
        ]

        ReadingVsNback = fmri_glm.compute_contrast(
            Reading_Nback,
            stat_type="t",
            output_type="all",
        )

        NbackVsReading = fmri_glm.compute_contrast(
            Nback_Reading,
            stat_type="t",
            output_type="all",
        )

        output_dir = os.path.join(stats_dir, sub_ID, "1st_level_SingleBlocks", sub_ID)

        for name, nifti_img in NbackVsReading.items():
            filepath = f"{output_dir}/{sub_ID}_both_runs_contrast-NbackVsReading_{name}.nii.gz"
            nib.save(nifti_img, filepath)

        for name, nifti_img in ReadingVsNback.items():
            filepath = f"{output_dir}/{sub_ID}_both_runs_contrast-ReadingVsNback_{name}.nii.gz"
            nib.save(nifti_img, filepath)

if __name__ == "__main__":
    main()