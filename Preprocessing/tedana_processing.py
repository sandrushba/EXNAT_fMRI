import os
import argparse
from tedana.workflows import tedana_workflow

# Set up argument parser
parser = argparse.ArgumentParser(description='Process participant data with tedana.')
parser.add_argument('-p', '--participants', nargs='+', required=True,
                    help='Space-separated list of participant IDs to process')

args = parser.parse_args()

# Specify base path where participant folders are located
base_path = '/data/p_02956/EXNAT_3_Data/derivatives/fmriprep-preproc'
participants = args.participants

# Define the list of tasks
tasks_single_run = ['singleNback', 'singleReading']  # Tasks with a single run
task_multiple_runs = 'dualTask'  # Task with multiple runs

# Define the list of runs
runs = ['01', '02', '03', '04']  # Runs for task_multiple_runs

# TEDANA needs the echo times for processing
tes = [13.4, 34.9, 56.4]  # Replace these echo times with your actual echo times

# Process each participant
for participant_id in participants:
    participant_dir = os.path.join(base_path, f'sub-{participant_id}', f'sub-{participant_id}', 'func')

    # Tasks with a single run
    for task in tasks_single_run:

        # Prepare file paths
        fp_e1 = os.path.join(participant_dir, f'sub-{participant_id}_task-{task}_echo-1_desc-preproc_bold.nii.gz')
        fp_e2 = os.path.join(participant_dir, f'sub-{participant_id}_task-{task}_echo-2_desc-preproc_bold.nii.gz')
        fp_e3 = os.path.join(participant_dir, f'sub-{participant_id}_task-{task}_echo-3_desc-preproc_bold.nii.gz')

        data = [fp_e1, fp_e2, fp_e3]

        # Specify output directory
        out_dir = os.path.join('/data/p_02956/EXNAT_3_Data/derivatives/tedana', participant_id, task)

        # Ensure output directory exists
        os.makedirs(out_dir, exist_ok=True)

        # Run tedana
        tedana_workflow(data, tes, out_dir=out_dir)

    # Task with multiple runs
    for run in runs:

        # Prepare file paths
        fp_e1 = os.path.join(participant_dir, f'sub-{participant_id}_task-{task_multiple_runs}_run-{run}_echo-1_desc-preproc_bold.nii.gz')
        fp_e2 = os.path.join(participant_dir, f'sub-{participant_id}_task-{task_multiple_runs}_run-{run}_echo-2_desc-preproc_bold.nii.gz')
        fp_e3 = os.path.join(participant_dir, f'sub-{participant_id}_task-{task_multiple_runs}_run-{run}_echo-3_desc-preproc_bold.nii.gz')

        data = [fp_e1, fp_e2, fp_e3]

        # Specify output directory
        out_dir = os.path.join('/data/p_02956/EXNAT_3_Data/derivatives/tedana', participant_id, task_multiple_runs, run)

        # Ensure output directory exists
        os.makedirs(out_dir, exist_ok=True)

        # Run tedana
        tedana_workflow(data, tes, out_dir=out_dir)
