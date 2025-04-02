import pandas as pd
import os
import argparse
import json
import re

def find_directory(db_id, source_dir):
    return (os.path.join(source_dir, entry) for entry in os.listdir(source_dir)
            if os.path.isdir(os.path.join(source_dir, entry)) and str(db_id) in entry)



def remove_bids_sub_from_intendedFor_in_directory(directory_path, pattern):
    # Compile the regex pattern to match the exact pattern followed by a slash
    regex = re.compile(pattern + r'/')

    # Loop over all files in the specified directory
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                json_file_path = os.path.join(root, file)

                # Read the JSON file
                with open(json_file_path, 'r') as file:
                    data = json.load(file)

                # Remove the specified pattern from each entry in the intendedFor list
                if "IntendedFor" in data:
                    data["IntendedFor"] = [regex.sub('', entry) for entry in data["IntendedFor"]]

                # Write the updated data back to the JSON file
                with open(json_file_path, 'w') as file:
                    json.dump(data, file, indent=4)

# Subject format
sub_format = "sub-{0}"

# Source directories
source_dir = "/data/p_02956/EXNAT_3_Data/sourcedata/"
nifti_dir = "/data/p_02956/EXNAT_3_Data/rawdata"
analysis_dir = "/data/p_02956/Analysis/"

# Initialize parser
parser = argparse.ArgumentParser(
    description="Write the study IDs of the participants to be converted as argument using -p")

# Adding optional argument
parser.add_argument("-p", "--Participant", nargs="+", help="Provide participant number",
                    required=True)

# Read arguments from command line
args = parser.parse_args()

# define subjects to process
participants = args.Participant
print("Participants: %s" % participants)

# define folder with participants table, which contains both study ID and DB ID to match dicom files coming from the MRI
data_table = os.path.join(analysis_dir, "EXNAT_3_Participants.xlsx")
study_data = pd.read_excel(data_table)

for participant in participants:
    # determine DB ID based on study ID
    db_ids = study_data.loc[study_data['Subject'] == participant, 'DB-ID']
    db_id = next(iter(db_ids.items()))

    sub_dirs = list(find_directory(db_id[1], source_dir))
    print(f"Directories found for DB-ID {db_id[1]}: {sub_dirs}")
    if not sub_dirs:  # if the list is empty
        print(f"No directory found for DB-ID {db_id[1]}")
    else:
        sub_dir = sub_dirs[0]  # take the first directory found
        print(f"Working with directory: {sub_dir}")
        os.listdir(sub_dir)  # run os.listdir on the first directory found

    # arguments for dcm2bids command
    config_file = os.path.join(analysis_dir, "Preprocessing/EXNAT_3_dcm2bids_config.json")
    # dcm_dir = os.path.join(sub_dir, "DICOM")
    dcm_dir = os.path.join(sub_dir)
    target_dir = nifti_dir

    cmd = "dcm2bids -d {0} -p {1} -c {2} -o {3} --auto_extract_entities --force_dcm2bids".format(dcm_dir, participant, config_file, target_dir)
    os.system(cmd)

    # dcm2bids writes some strings in front of func directory in the IntendedFor field that we need to remove,
    # otherwise fMRIPrep won't recognize the fieldmaps
    fmap_dir = os.path.join(nifti_dir, sub_format.format(participant), "fmap")
    pattern = r"bids::sub-[A-Z]{2}\d{2}"
    remove_bids_sub_from_intendedFor_in_directory(fmap_dir, pattern)