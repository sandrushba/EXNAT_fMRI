#!/bin/bash

# This script runs fmriprep on the given participants. The fmriprep_config.sh file contains the data path variables.

source fmriprep_config.sh
export SINGULARITYENV_TEMPLATEFLOW_HOME="/data/u_martin_software/templateflow"
export TEMPLATEFLOW_HOME="/data/u_martin_software/templateflow"

for p in OA29; do
(singularity run -B /data/pt_02956/,/data/p_02956/EXNAT_3_Data /data/pt_02956/fmriprep-24.1.0.simg \
"$data_path" "$output_dir/"sub-"$p" --fs-license-file /data/pt_02956/license.txt -w "$working_dir/"sub-"$p" \
participant --fd-spike-threshold 0.7 --participant-label "$p" --output-spaces MNI152NLin6Asym:res-2 MNI152NLin2009cAsym:res-2 --me-t2s-fit-method curvefit \
--me-output-echos --notrack --skip-bids-validation --no-submm-recon > /data/p_02956/Analysis/fmriprep_lastParticipants.txt )&
done
wait
echo "All participants are in the pipeline"
