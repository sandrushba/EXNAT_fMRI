import pandas as pd
import os
import argparse

def find_directory(db_id, source_dir):
    return (os.path.join(source_dir, entry) for entry in os.listdir(source_dir)
            if os.path.isdir(os.path.join(source_dir, entry)) and db_id in entry)

# Subject format
sub_format = "sub-{0}"

# Source directories
source_dir = "/data/p_02956/EXNAT_3_Data/sourcedata/"
nifti_dir = "/data/p_02956/EXNAT_3_Data/rawdata"
analysis_dir = "/data/tu_martin_cloud/EXNAT/EXNAT_fMRI/Analysis"

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

    # now search for subject folder in source_dir
    sub_dir = find_directory(db_id[1], source_dir)
    for sd in sub_dir:
        sub_dir = sd
        print(sd)

    os.listdir(sub_dir)

    # arguments for dcm2bids command
    config_file = os.path.join(analysis_dir, "EXNAT_3_dcm2bids_config.json")
    dcm_dir = os.path.join(sub_dir, "DICOM")
    target_dir = nifti_dir

    cmd = "dcm2bids -d {0} -p {1} -c {2} -o {3} --auto_extract_entities".format(dcm_dir, participant, config_file, target_dir)
    os.system(cmd)