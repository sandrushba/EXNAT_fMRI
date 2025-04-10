import os
from atlasreader import create_output
from nilearn.glm import threshold_stats_img

def find_contrasts(curr_stats_dir):
    unique_contrasts = set()

    # Iterate over all files in the directory
    for filename in os.listdir(curr_stats_dir):
        # Split the filename at the first underscore
        prefix = filename.split('_', 1)[0]
        # Add the prefix to the set
        unique_contrasts.add(prefix)

    return unique_contrasts

def create_output_from_atlas(stats_map, outdir, voxel_thresh, atlases):
    create_output(stats_map,
              cluster_extent=10,
              direction="pos",
              voxel_thresh=voxel_thresh,
              atlas=atlases,
              min_distance=8,
              outdir=outdir)

    print("Finished creating output from atlas")

def main():
    # Configuration
    stats_dir = "/data/p_02956/EXNAT_3_Data/derivatives/fmriprep-stats/group_statistics"
    atlases = ["aal", "harvard_oxford", "juelich"]

    curr_stats = "SingleBlocks" # change this according to the dir you want result tables for
    curr_stat_dir = os.path.join(stats_dir, curr_stats)

    contrasts = find_contrasts(curr_stat_dir)

    # now loop over list of contrasts and generate output files in a dedicated directory
    for contrast in contrasts:
        curr_dir = os.path.join(curr_stat_dir, contrast)
        if not os.path.exists(curr_dir):
            os.makedirs(curr_dir)

        for filename in os.listdir(curr_stat_dir):
            # Check if the file contains both the specific string and "z_map", and ends with "nii.gz"
            if filename.startswith(contrast) and "z_map" in filename and filename.endswith("nii.gz"):
                curr_stats_img = filename
                print(f"Processing stat image: {filename}")
                break

        curr_stats_img = os.path.join(curr_stat_dir, curr_stats_img)

        # determine a specific threshold to apply with the atlasreader tool
        img, threshold = threshold_stats_img(
            stat_img=curr_stats_img,
            alpha=0.05,
            height_control="fdr",
            two_sided=False,
            cluster_threshold=10)

        # now clculate clusters and output tables with atlasreader
        create_output_from_atlas(curr_stats_img, curr_dir, threshold, atlases)

if __name__ == "__main__":
    main()