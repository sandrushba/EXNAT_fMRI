#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

EXNAT-2 EEG DATA ANALYSIS PIPELINE

Author: Merle Schuckart
Version: November, 2023


"""


# ----------------------------------------------------- # 

""" General information / random stuff that's maybe good to know: """

# This is how the EEG data were recorded in the lab:
# sampling rate: 1000 Hz
# nr of channels: 64
# reference electrode: TP9
# filter: DC-280 Hz

# We used the BrainVision Recorder for recording the EEG.

# For each participant, we get 3 files from the EEG, one .eeg file (containing the raw eeg data), 
# one .vhdr file (containing metadata and configuration information for the EEG recording, 
# such as the sampling rate, number of channels, electrode locations, ...), and
# one .vmrk file (containining triggers). 

# So for participant 001, it would look like this:
# "part_001/EXNAT_part001_1.eeg",
# "part_001/EXNAT_part001_1.vhdr",
# "part_001/EXNAT_part001_1.vmrk"


# Please make sure to pip install MNE python 
# (or updating your version if it's older) 
# before running this script.


# ----------------------------------------------------- # 

""" Import Packages """

# for setting paths:
import os
#os.chdir('/Volumes/MERLE 1/EXNAT-2/EEG_study_EXNAT2/EXNAT-2 Win7 Experiment EYELINK/Analysis/')

import sys

import numpy as np

# for dataframes
import pandas as pd

# import MNE
# --> make sure it's pip installed 
!pip install mne
import mne

# for plotting
import matplotlib.pyplot as plt

# ----------------------------------------------------- # 

# set path to data file here:
#curr_data_path = "/Users/merleschuckart/Github/PhD/EXNAT/EEG_study_EXNAT2/EEG study analysis/Data/"
curr_data_path = "/Users/merle/Github/PhD/EXNAT/EEG_study_EXNAT2/EEG study analysis/Data/"

# get list of files in data directory: 
file_list = os.listdir(curr_data_path)

# Only get files that don't end with some file suffix like .py or .DS_Store, 
# those are the folders for each participant.
file_list = [item for item in file_list if ".py" not in item and ".DS_Store" not in item]


# ----------------------------------------------------- # 


# loop folders & read in data for each participant.

for curr_file in file_list: 
    
    # get ID of current participant
    curr_id = curr_file.replace("part_", "")
    print("reading in data for participant with ID", curr_id)
    

    """ create MNE raw object with raw EEG data + triggers + metadata """
    
    # read in the 3 EEG-related datasets
    curr_vhdr_file = curr_data_path + "part_" + curr_id + "/EXNAT_part" + curr_id + "_1.vhdr"
        
    # read in .eeg file with EEG data EEG data using MNE
    raw = mne.io.read_raw_brainvision(curr_vhdr_file, preload = True)
    
    
    """ Set triggers """

    # convert annotations to events 
    # --> use trigger map from experiment here!
    trigger_map = {'block_onset': 2,
                   'response_target': 4,
                   'response_continue': 6,
                   'trial_onset': 8,
                   'click_training_onset': 10,
                   'Reading_Baseline_training_onset': 12,
                   'Reading_Baseline_main_onset': 14,
                   '1back_single_training1_onset': 16,
                   '1back_single_training2_onset': 18,
                   '1back_single_main_onset': 20,
                   '1back_dual_main_onset': 22,
                   '2back_single_training1_onset': 24,
                   '2back_single_training2_onset': 26,
                   '2back_single_main_onset': 28,
                   '2back_dual_main_onset': 30,
                   'prediction_tendency_task_onset': 32,
                   'visual_task_main_onset': 34,
                   'visual_task_training_onset': 36,
                   'block_offset': 38,
                   'freq_440_onset': 40,
                   'freq_440_offset': 42,
                   'freq_587_onset': 44,
                   'freq_587_offset': 46,
                   'freq_782_onset': 48,
                   'freq_782_offset': 50,
                   'freq_1043_onset': 52,
                   'freq_1043_offset': 54,
                   'ordered': 56,
                   'random': 58,
                   'start_experiment': 60,
                   'end_experiment': 62,
                   'trial_offset': 64}

    events, event_id = mne.events_from_annotations(raw, event_id = trigger_map)
        
    
# print annotations we can construct events from:
print(set(eyelink_raw.annotations.description))
# --> I want "trial_offset" because the screen gradually changes 
# from grey to white there, so maybe I can see a pupillary light reflex.

# convert annotations to events 
# --> use trigger map from experiment here!
trigger_map = {'block_onset': 2,
               'response_target': 4,
               'response_continue': 6,
               'trial_onset': 8,
               'click_training_onset': 10,
               'Reading_Baseline_training_onset': 12,
               'Reading_Baseline_main_onset': 14,
               '1back_single_training1_onset': 16,
               '1back_single_training2_onset': 18,
               '1back_single_main_onset': 20,
               '1back_dual_main_onset': 22,
               '2back_single_training1_onset': 24,
               '2back_single_training2_onset': 26,
               '2back_single_main_onset': 28,
               '2back_dual_main_onset': 30,
               'prediction_tendency_task_onset': 32,
               'visual_task_main_onset': 34,
               'visual_task_training_onset': 36,
               'block_offset': 38,
               'freq_440_onset': 40,
               'freq_440_offset': 42,
               'freq_587_onset': 44,
               'freq_587_offset': 46,
               'freq_782_onset': 48,
               'freq_782_offset': 50,
               'freq_1043_onset': 52,
               'freq_1043_offset': 54,
               'ordered': 56,
               'random': 58,
               'start_experiment': 60,
               'end_experiment': 62,
               'trial_offset': 64}

(events_from_annot, event_dict) = mne.events_from_annotations(eyelink_raw, 
                                                              event_id = trigger_map)
#print(event_dict)
#print(events_from_annot[30:80]) 
    
    
    
    
    # Apply events to the raw data
    
    
    
    
    # Apply reference:
    raw.set_eeg_reference(ref_channels = 'average', projection = True)
    
    # Print information about the Raw object: Now you can check if all looks 
    # as intended or if channels are missing for example.
    #print(raw.info)
    #print(raw.ch_names)
    
    
    # downsample the data a bit so it's easier to work with:
    raw.resample(sfreq = 250)    
        
    
    
    
# Assuming your original event_id mapping looks like this
original_event_id = {'Stimulus/S4': 1, 'Stimulus/S5': 2, 'Stimulus/S6': 3}

# Create a new event_id mapping with meaningful names
new_event_id = {'word_onset': 1, 'another_event_name': 2, 'yet_another_event': 3}

# Remap the triggers using the new event_id mapping
events, _ = mne.events_from_annotations(raw, event_id=original_event_id)

# Update the event codes in the events array
events[:, 2] = [new_event_id[event] for event in mne.pick_events(events)[0]]

# Print the updated event_id mapping (although RawBrainVision doesn't have this attribute)
print(new_event_id)
    
    
    
    unique_events = set(mne.find_events(raw)[:, 2])
    
    
    
    
    
    
    
    # also check how the data look:
        
    # Plot the raw EEG data
    raw.plot(n_channels = 3, duration = 3, scalings = 'auto', highpass=2, lowpass=12, filtorder=4)
    
    # Plot the events on top of the raw data
    raw.plot_events(events, event_id = event_id, color ='blue', event_color={1: 'r', 2: 'g', 3: 'b'})

    
    """ Filtering """
    # --> 5 - 15 Hz for word onset ERPs?
    
        
        
    """ Epoching """
    
    # --> cut into blocks
    
    # --> cut blocks into trials around word onset triggers (use -2 to 2 around trigger)
    
    
    """ Word Onset ERPs """
    
    
    
    
    
    
    


 
# From Frauke's paper:
# "Data were then low-pass filtered at 4 Hz (Butterworth, fourth-order filter) ..."



# make copy of raw object for filtered data
filtered_raw = eyelink_raw.copy()

# set filter parameters:
filter_params = mne.filter.create_filter(eyelink_raw.get_data(), 
                                         eyelink_raw.info["sfreq"], 
                                         l_freq = 4, 
                                         h_freq = None,
                                         filter_length = "auto",
                                         iir_params = None, method="iir") # set these two to None and "iir" to create 4th order Butterworth filter
                                         
# visualize filter:
mne.viz.plot_filter(filter_params, eyelink_raw.info["sfreq"], flim=(0.01, 5))

# apply filter to the 2 pupil data channels:
channels_to_filter = ["pupil_right", "residual_pupil_size"]






# "...and segmented into trials ranging from –2 to 8 s relative to noise onset. 
# Trials were excluded if .40% of data points within a trial had to be interpolated. 
# The full dataset of a participant was excluded from analysis if .50% of trials
# were excluded in any of the conditions (N = 1).

# Pupil size data were downsampled to 50 Hz. For each trial, the mean
# pupil size was calculated in the 2 to 1.1 s time window before noise
# onset and was subtracted from the data at each time point (baseline correction). 
# This baseline time window was chosen to avoid contamination
# by visual stimulation (presented from 1 s onward). The 1.1 s
# time point was chosen to avoid potential smearing back of visual
# onset responses into the baseline period. Pupil size was averaged
# across trials, separately for each condition. We averaged data both
# within the main time window of interest used in the EEG analysis
# (3–4 s) as well as within a later time window from 5 to 6 s. The later
# time window for the pupil size analysis was chosen to account for
# the sluggishness of changes in pupil size (Knapen et al., 2016; Winn
# et al., 2018; Montefusco-Siegmund et al., 2022).











""" Find events """

# print annotations we can construct events from:
print(set(eyelink_raw.annotations.description))
# --> I want "trial_offset" because the screen gradually changes 
# from grey to white there, so maybe I can see a pupillary light reflex.

# convert annotations to events 
# --> use trigger map from experiment here!
trigger_map = {'block_onset': 2,
               'response_target': 4,
               'response_continue': 6,
               'trial_onset': 8,
               'click_training_onset': 10,
               'Reading_Baseline_training_onset': 12,
               'Reading_Baseline_main_onset': 14,
               '1back_single_training1_onset': 16,
               '1back_single_training2_onset': 18,
               '1back_single_main_onset': 20,
               '1back_dual_main_onset': 22,
               '2back_single_training1_onset': 24,
               '2back_single_training2_onset': 26,
               '2back_single_main_onset': 28,
               '2back_dual_main_onset': 30,
               'prediction_tendency_task_onset': 32,
               'visual_task_main_onset': 34,
               'visual_task_training_onset': 36,
               'block_offset': 38,
               'freq_440_onset': 40,
               'freq_440_offset': 42,
               'freq_587_onset': 44,
               'freq_587_offset': 46,
               'freq_782_onset': 48,
               'freq_782_offset': 50,
               'freq_1043_onset': 52,
               'freq_1043_offset': 54,
               'ordered': 56,
               'random': 58,
               'start_experiment': 60,
               'end_experiment': 62,
               'trial_offset': 64}

(events_from_annot, event_dict) = mne.events_from_annotations(eyelink_raw, 
                                                              event_id = trigger_map)
#print(event_dict)
#print(events_from_annot[30:80]) 

eyelink_raw.plot(start=5, duration=5, order = pupil_channel_idx)

# Plot 
epochs = mne.Epochs(
    eyelink_raw,
    events = events_from_annot,
    event_id = event_dict,
    tmin = -0.3,
    tmax = 3,
    preload = True,
    event_repeated = "merge" # merge all events that are the same
)


epochs[:8].plot(events=et_events, event_id=event_dict, order=pupil_channel_idx)

# plot evoked responses to the light flash:
epochs.average().plot(picks=["pupil_right"])











# FOR LATER:

""" Align EEG & Eyetracking Data """
# Convert event onsets from samples to seconds
et_flash_times = et_events[:, 0] / raw_et.info["sfreq"]
eeg_flash_times = eeg_events[:, 0] / raw_eeg.info["sfreq"]
# Align the data
mne.preprocessing.realign_raw(
    raw_et, raw_eeg, et_flash_times, eeg_flash_times, verbose="error"
)
# Add EEG channels to the eye-tracking raw object
raw_et.add_channels([raw_eeg], force_update_info=True)

# Define a few channel groups of interest and plot the data
frontal = ["E19", "E11", "E4", "E12", "E5"]
occipital = ["E61", "E62", "E78", "E67", "E72", "E77"]
pupil = ["pupil_right"]
picks_idx = mne.pick_channels(
    raw_et.ch_names, frontal + occipital + pupil, ordered=True
)
raw_et.plot(events=et_events, event_id=event_dict, event_color="g", order=picks_idx)








