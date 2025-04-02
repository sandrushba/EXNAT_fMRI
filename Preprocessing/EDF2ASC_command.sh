#!/bin/bash

# Path to subjects directory
data_path="/data/p_02956/EXNAT_3_Data/derivatives/fmriprep-stats/subjects"

subject_array=()

# Add participant directories to the array
for dir in $data_path/sub-{YA,MA,OA}{01..35}; do
  if [ -d "$dir" ]; then
    # Extract the subject label (remove path prefix)
    subject_label=$(basename $dir)
    # Remove 'sub-' prefix from the subject label
    subject_label=${subject_label#sub-}
    subject_array+=($subject_label)
  fi
done

# To print the entire array
echo ${subject_array[@]}

# Loop over subject_array
for subject_label in ${subject_array[@]}
do
  subject_dir="$data_path/sub-$subject_label"
  # Check for eyetracker directory in subject directory
  if [ -d "$subject_dir/eyetracker" ]; then
    # Check for any .edf files in eyetracker directory
    for edf_file in "$subject_dir/eyetracker"/*.EDF
    do
      # Determine name of .asc file
      asc_file="${edf_file%.EDF}.asc"
      # Check if file exists
      if [ -f "$edf_file" ]; then
      	  # Check if corresponding .asc file does not exist
      	  if [ ! -f "$asc_file" ]; then
          	echo "Converting $edf_file..."
          	# Call EDF2ASC on the .edf file 
         	edf2asc -input "$edf_file"
 	  else
 	  	echo "Skipping $edf_file because $asc_file already exists..."
  	  fi
      fi
    done
  fi
done

