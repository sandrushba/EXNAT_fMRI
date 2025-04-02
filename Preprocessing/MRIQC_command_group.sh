#!/bin/bash

# This script runs MRIQC on the given participants. The mriqc_config.sh file contains the data path variables.

source MRIQC_config.sh

singularity run -B /data/pt_02956/EXNAT_3_Data,/data/p_02956/EXNAT_3_Data /data/pt_02956/mriqc-24.0.2.simg "$data_path" "$output_dir" -w "$working_dir" group --fd_thres 0.7 --no-sub
