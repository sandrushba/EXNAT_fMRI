import os
import glob
import pandas as pd
from nilearn import plotting, datasets, surface
from nilearn.glm.second_level import SecondLevelModel
from nilearn.glm import threshold_stats_img

def list_subject_folders(stats_dir):
    """
    List all subfolders in the stats directory starting with 'sub-YA'.
    """
    return [name for name in os.listdir(os.path.join(stats_dir))
            if os.path.isdir(os.path.join(stats_dir, name)) and name.startswith('sub-YA')]

def find_con_img(stats_dir, sub_ID, run):
    first_level_path = os.path.join(stats_dir, "subjects", sub_ID, "1st_level_SingleBlocks", sub_ID)

    img = glob.glob(os.path.join(first_level_path, "*" + run + "*stat-effect*.nii.gz"))

    new_data = pd.DataFrame({
        "subject_label": sub_ID,
        "effects_map_path": img
    })

    new_data['map_name'] = new_data["effects_map_path"].str.extract(r"contrast-(\w+)_stat")

    return new_data

def main():
    # Configuration
    stats_dir = "/data/p_02956/EXNAT_3_Data/derivatives/fmriprep-stats"
    runs = ["Reading", "back_single"]

    # For plotting
    template_img = datasets.load_mni152_template(resolution=2)

    # List all subject folders
    subject_folders = list_subject_folders(os.path.join(stats_dir, "subjects"))

    # Loop over runs and find contrast images
    for run in runs:
        print(f"This is run: {run}")

        # Initiate df for second level input
        contrasts_df = pd.DataFrame()

        # Process each subject
        for sub_ID in subject_folders:
            print(f"This is subject: {sub_ID}")

            con_img = find_con_img(stats_dir, sub_ID, run)

            contrasts_df = pd.concat([contrasts_df, con_img], ignore_index=True)

        dfs = {map_name: group_df for map_name, group_df in contrasts_df.groupby('map_name')}

        for df_name, current_df in dfs.items():
            if df_name == "effectsOfInterest":
                continue
            print(f"Processing contrast {df_name}")
            second_level_model = SecondLevelModel(verbose=1)
            second_level_model.fit(current_df)

            z_map = second_level_model.compute_contrast(
                output_type="z_score",
                second_level_stat_type="t",
                first_level_contrast=df_name
            )

            thresholded_img, threshold = threshold_stats_img( # this also writes out a one-sided thresholded image
                stat_img=z_map,
                alpha=0.05,
                height_control="fdr",
                two_sided=False,
                cluster_threshold=10)

            output_path = os.path.join(stats_dir, "group_statistics", "SingleBlocks")
            # Save thresholded image
            thresholded_img.to_filename(f"{output_path}/{df_name}_thresholded.nii.gz")
            # Also save non-thresholded image
            z_map.to_filename(f"{output_path}/{df_name}_z_map.nii.gz")

            # Plot image
            plotting.plot_stat_map(thresholded_img, display_mode="ortho")
            plotting.show()

            # plot interactive in browser
            view = plotting.view_img(z_map, threshold=threshold)
            view.save_as_html(os.path.join(output_path, df_name + "_thresholded_volume.html"))

            # Plot on surface
            view = plotting.view_img_on_surf(
                stat_map_img=thresholded_img,
                surf_mesh="fsaverage",
                darkness=1,
                bg_on_data=True,
                threshold=threshold,
                cmap="spring",
                vmin=threshold,
                symmetric_cmap=False,
                title=df_name)
            #view.open_in_browser()
            view.save_as_html(os.path.join(output_path, df_name + "_thresholded_surface.html"))

            # fsaverage = datasets.fetch_surf_fsaverage()
            # mesh = surface.load_surf_mesh(fsaverage.pial_left)
            # map = surface.vol_to_surf(z_map, mesh)
            # fig = plotting.plot_surf_stat_map(mesh, map, hemi='left',
            #                                   view='lateral', colorbar=True,
            #                                   threshold=threshold,
            #                                   bg_map=fsaverage.sulc_left,
            #                                   engine='plotly')
            # fig.show()

if __name__ == "__main__":
    main()