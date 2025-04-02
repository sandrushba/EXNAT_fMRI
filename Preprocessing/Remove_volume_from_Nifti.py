import nibabel as nib
import argparse
import os


def process_nifti_file(participant_number, task_name, echo_number, run_number=None):
    # Set data folder
    dir = "/data/p_02956/EXNAT_3_Data/rawdata"
    sub_dir = dir + "/sub-" + participant_number + "/func/"

    # Construct the filename with optional run number
    if run_number is not None:
        filename = f"sub-{participant_number}_task-{task_name}_run-{run_number:02}_echo-{echo_number}_bold.nii.gz"
    else:
        filename = f"sub-{participant_number}_task-{task_name}_echo-{echo_number}_bold.nii.gz"

    # Load the NIfTI file
    img = nib.load(os.path.join(sub_dir, filename))

    # Get the data from the image
    data = img.get_fdata()

    # Remove the last volume
    new_data = data[..., :-1]

    # Create a new NIfTI image
    new_img = nib.Nifti1Image(new_data, img.affine, img.header)

    # Save the new image with the same filename
    nib.save(new_img, os.path.join(sub_dir, filename))
    print(f"Processed and saved: {filename}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process NIfTI files by removing the last volume.")
    parser.add_argument("-p", "--participant", type=str, required=True, help="Participant number (e.g., OA19)")
    parser.add_argument("-t", "--task", type=str, required=True, help="Task name (e.g., singleNback)")
    parser.add_argument("-e", "--echo", type=int, nargs='+', required=True, help="Echo numbers (e.g., 1 2 3)")
    parser.add_argument("-r", "--run", type=int, help="Run number with leading zero (optional, e.g., 01)")

    # Parse arguments
    args = parser.parse_args()

    # Process the NIfTI files for each echo number
    for echo_number in args.echo:
        process_nifti_file(args.participant, args.task, echo_number, args.run)

if __name__ == "__main__":
    main()