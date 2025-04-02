#!/bin/bash

# This script runs MRIQC on the given participants. The mriqc_config.sh file contains the data path variables.

source MRIQC_config.sh

# Initialize an empty array
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

# Total number of datasets
total_datasets=${#subject_array[@]}

# How many to process in parallel
group_size=5

for (( i=0; i<total_datasets; i+=group_size )); do
  for (( j=0; j<group_size; j++ )); do
    # Calculate dataset index
    index=$((i+j))
    
    # Break the inner loop if the index exceeds the total datasets
    if [ $index -ge $total_datasets ]; then
      break
    fi
    
    # Get the subject ID from the array
    subject_id=${subject_array[$index]}
    
    # Skip OA01
    if [ "$subject_id" == "OA01" ]; then
      echo "Skipping OA01..."
      continue
    fi
    
    # Check if the output directory already exists
    if [ -d "$output_dir/sub-$subject_id" ]; then
      echo "Output directory for $subject_id already exists. Skipping..."
      continue
    fi
    
    # Process the dataset in the background
    echo "Processing dataset $subject_id in background..."
    # Use subject_id in the singularity run command
    singularity run -B /data/pt_02956/,/data/p_02956/EXNAT_3_Data /data/pt_02956/mriqc-24.0.2.simg --fd_thres 0.7 --no-sub "$data_path" "$output_dir/sub-$subject_id" -w "$working_dir/$subject_id" participant --participant-label "$subject_id" &

  done
  
  # Wait for all background processes to finish before moving to the next group
  wait
  echo "Completed processing group of datasets up to subject ID $subject_id."
done

echo "All datasets processed."
