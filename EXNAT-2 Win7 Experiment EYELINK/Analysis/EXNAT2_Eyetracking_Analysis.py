#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

EXNAT-2 PUPILLOMETRY DATA ANALYSIS PIPELINE

Author: Merle Schuckart
Version: August 16, 2023


"""


# ----------------------------------------------------- # 

""" General information / random stuff that's maybe good to know: """
    
    
# The sampling frequency of the Eyetracker is 1000 Hz. 
# We used an EyeLink eyetracker here and only recorded the right eye.


# For some reason, all Eyelink EDFs are not saved as 
# regular EDFs but in a weird Eyelink format. So they have to 
# be converted to .asc format using Eyelink's EDFConverter app.
# Make sure you did that for all files you want to analyse here.    


# Please make sure to pip install MNE python 
# (or updating your version if it's older) 
# before running this script.


# ----------------------------------------------------- # 

""" Import Packages """

# for setting paths:
import os
os.chdir('/Users/merle/Github/PhD/EXNAT/EEG_study_EXNAT2/EXNAT-2 Win7 Experiment EYELINK/Analysis/')


import numpy as np

# for dataframes
import pandas as pd

# import MNE
# --> make sure it's pip installed 
import mne
from mne.io import read_raw_eyelink # doesn't work for some reason
from mne.preprocessing.eyetracking import read_eyelink_calibration

# for linear regression
from sklearn.linear_model import LinearRegression

# for imputing NaN values 
from sklearn.impute import SimpleImputer

# for plotting
import matplotlib.pyplot as plt

# ----------------------------------------------------- # 

# set path to data here:
curr_data_path = "/Users/merle/Github/PhD/EXNAT/EEG_study_EXNAT2/EXNAT-2 Win7 Experiment EYELINK/Analysis/data_eyelink_asc/test.asc"


# ----------------------------------------------------- # 

""" Read in ascii Dataset as MNE Raw Object"""
eyelink_raw = read_raw_eyelink(curr_data_path, 
                               create_annotations=["blinks", "messages"], # mark blinks in the stream & add trigger messages
                               preload=True,
                               apply_offsets = False) # adjust onset time of the mne.Annotations created from exp. messages (= triggers)

# Check out info to see if everything looks fine:
eyelink_raw.info

# plot all channels:
eyelink_raw.plot(scalings = dict(eyegaze = 1e3))

""" Check quality of calibration: """
cals = read_eyelink_calibration(curr_data_path)
print(f"number of calibrations: {len(cals)}")
first_cal = cals[0]  # let's access the first (and only in this case) calibration
print(first_cal)
# plot calibrations to check quality:
# first_cal.plot()


""" Preprocessing: Interpolate missing data in blink periods """

# plot raw eyetracking data from pupil size channel of right eye 
# to see if everything's there and the triggers were recorded properly:
pupil_channel_idx = mne.pick_channels(eyelink_raw.ch_names, ["pupil_right"])
#eyelink_raw.plot(scalings = dict(eyegaze = 1e3), order = pupil_channel_idx)

# There are blinks in our data, so sometimes pupil dilation = 0. 
# We don't want to throw away data here, so interpolate the missing bits.
# We'll use 0.05 = 50 ms before and 0.2 = 200 ms after the blink as the interpolation 
# window, so that the noisy data surrounding the blink is also interpolated
#mne.preprocessing.eyetracking.interpolate_blinks(eyelink_raw, 
#                                                 buffer = (0.05, 0.2), 
#                                                 interpolate_gaze = True) # also interpolate gaze coordinates although eye movements can occur during blinks which makes the gaze data less suitable for interpolation

# plot again: 
#eyelink_raw.plot(scalings = dict(eyegaze = 1e3))



""" Preprocessing: Control for potential influence of eye movements on pupil size """

# From Frauke's paper: https://doi.org/10.1523/JNEUROSCI.2181-22.2023

# "To control for the potential influence of eye
# movement-related changes, the x-coordinates and y-coordinates
# were regressed out of the pupil data (multiple linear regression; Fink
# et al., 2021), and the resultant residual pupil size time course was
# used for all further analyses."

# I'll do the same here:
# 1. get eye movement data (recorded as x and y coordinates)
# 3. run multiple linear regression using x and y coordinates as predictors
# 4. calculate residual pupil size and use that for further analysis


# prepare predictor variables (x- and y-coordinates)
# --> find the channel names by running this: eyelink_raw.ch_names
x_coords = eyelink_raw.get_data(picks="xpos_right")
y_coords = eyelink_raw.get_data(picks="ypos_right")
pupil_size = eyelink_raw.get_data(picks="pupil_right")

# reshape data for regression (make them column vectors)
x_coords = x_coords.reshape(-1, 1)
y_coords = y_coords.reshape(-1, 1)
pupil_data = pupil_size.reshape(-1, 1)


# get rid of NaN values by imputing them 
# (mean imputation --> replace missing values using the mean along each column)
imputer = SimpleImputer(strategy="mean")
x_coords_imputed = imputer.fit_transform(x_coords)
y_coords_imputed = imputer.fit_transform(y_coords)
pupil_data_imputed = imputer.fit_transform(pupil_data)


# fit regression model
reg_model = LinearRegression()
reg_model.fit(np.hstack((x_coords_imputed, y_coords_imputed)), pupil_data_imputed)

# calculate residual pupil size
# from stackoverflow: "residual is simply the difference between the actual value and predictions". Makes sense. 
predicted_pupil_size = reg_model.predict(np.hstack((x_coords_imputed, y_coords_imputed)))
residual_pupil_size = pupil_data - predicted_pupil_size

# add to raw object as new channel
new_channel_data = residual_pupil_size.T

# create info for channel:
new_channel_info = mne.create_info(
    ch_names=["residual_pupil_size"],
    sfreq=eyelink_raw.info["sfreq"],
    ch_types=["pupil"],
)
new_channel_info["line_freq"] = eyelink_raw.info["line_freq"]
new_channel_info["subject_info"] = eyelink_raw.info["subject_info"]
with new_channel_info._unlock():
    new_channel_info["lowpass"] = eyelink_raw.info["lowpass"]
    new_channel_info["highpass"] = eyelink_raw.info["highpass"]
    
# put together to raw object
new_channel_raw = mne.io.RawArray(
    data = new_channel_data,
    info = new_channel_info,
    first_samp = eyelink_raw.first_samp,
)

# concatenate raw objects
eyelink_raw.add_channels([new_channel_raw])

# plot the new data and compare with original pupil size data:
eyelink_raw.plot(scalings = dict(eyegaze = 1e3), order = mne.pick_channels(eyelink_raw.ch_names, ["pupil_right", "residual_pupil_size"]))


""" Preprocessing: Filter data """
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

raw_highpass = eyelink_raw.copy().filter(l_freq = 4, 
h_freq = None,
filter_length = "auto",
iir_params = None, method="iir")

# plot filtered data:
raw_highpass.plot(start=5, duration=5, order = mne.pick_channels(eyelink_raw.ch_names, ["pupil_right", "residual_pupil_size"]))


""" Preprocessing: Downsampling to 50 Hz """
# --> maybe make the resolution a bit higher because the experiment is quite fast-paced?

# downsample data to 50 Hz:
raw_downsampled = raw_highpass.copy().resample(sfreq=100)
 
# plot again:
raw_downsampled.plot(start=5, duration=5, order = mne.pick_channels(eyelink_raw.ch_names, ["pupil_right", "residual_pupil_size"]))



""" Epoching """ 
# segment into trials around stim onset
# --> make sure to differentiate between blocks!


# Divide data into blocks
# --> cut original data into smaller raw objects 

# set names and values of block onset triggers and the consistent block offset trigger
all_block_onset_triggers = {'block_onset': 2,
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
                            'ordered': 56,
                            'random': 58}

all_block_offset_triggers = {'block_offset': 38}

# find events of the block on- and offsets using the annotations
# --> if a trigger occurs more than once, we get several events
onset_events, block_onset_triggers = mne.events_from_annotations(raw_downsampled, event_id = all_block_onset_triggers)
offset_events, block_offset_triggers = mne.events_from_annotations(raw_downsampled, event_id = all_block_offset_triggers)

# run this to check all events + triggers in the dataset: 
#events, triggers =  mne.events_from_annotations(raw_downsampled)

# Exclude incremental blocks:
# if we stopped the experiment within a block and there's 1 offset trigger 
# missing, don't use the incremental block:
if len(offset_events) < len(onset_events):
    print("offset trigger is missing - removing incremental block!")
    # remove last onset event & trigger from lists of events
    onset_events = onset_events[:-1]
    # --> doesn't matter if trigger is still in the trigger dict


# empty list to collect block datasets
epochs_list = []

# loop block onset trigger
for onset_row_idx, onset_row in enumerate(onset_events):
    
    # get trigger value and corresponding description string:
    onset_trigger_val = onset_row[2]
    
    print("creating epoch for current block with trigger value", onset_trigger_val, "at index", onset_row_idx)   

    # Find the corresponding block offset event
    offset_row = offset_events[onset_row_idx]

    # get time stamps for block on- and offset and convert from 10 ms to sec:
    block_onset_timestamp = onset_row[0]/100
    block_offset_timestamp = (offset_row[0]/100) + 1 # add 1 s to see the offset trigger in the plot
    
    # Why do I divide by 100 here?
    # In my test dataset, I get time stamps that look like this: 19609 (for the last trigger time stamp in my case)
    # When I check the time stamps from the original data, the last time stamp is 196.47, which makes sense if it's seconds because 
    # I recorded for about 3.5 minutes. So to get my weird trigger time steps in the same range, 
    # I have to divide them by 100. So they are not in ms, but in 10ms. 
    # You can check the time stamps from the original data like this:
    #data_first_timestamp = raw_downsampled.times[0]
    #data_last_timestamp = raw_downsampled.times[-1]
    
    
    # copy raw object, then crop to the specified time range
    curr_block_raw = raw_downsampled.copy().crop(tmin = block_onset_timestamp,
                                                 tmax = block_offset_timestamp)

    
    # plot it!
    # curr_block_raw.plot(order = mne.pick_channels(eyelink_raw.ch_names, ["pupil_right", "residual_pupil_size"]))

    # Now that we have the block, create epochs around the stim onsets:
    

    # find stim_onset events (look for all possible trial onset events)
    stim_onset_events = {'trial_onset': 8,
                         'freq_440_onset': 40,
                         'freq_587_onset': 44,
                         'freq_782_onset': 48,
                         'freq_1043_onset': 52}
        
    stim_onset_events = mne.events_from_annotations(curr_block_raw, 
                                                    event_id = stim_onset_events)
    
    # Create epochs for the current block
    curr_block_epochs = mne.Epochs(curr_block_raw, 
                                   stim_onset_events[0], 
                                   event_id = 8,  # 'trial_onset': 8
                                   tmin = 0.1, # use 100 ms pre stim 
                                   tmax = 1, # use 1 s post stim
                                   baseline = None, 
                                   preload = True,
                                   reject_by_annotation = True) # exclude all epochs that overlap with segments marked as "bad" --> blinks or breaks
    
    # plot the epochs:
    #curr_block_epochs.plot(order = mne.pick_channels(eyelink_raw.ch_names, ["pupil_right", "residual_pupil_size"]))
    
    # This is how you'd plot the average epoch / ERP
    # average_epoch = curr_block_epochs.average()
    # average_epoch.plot(picks = ['residual_pupil_size'])
    
    
    """Preprocessing: Baseline Correction"""
    # subtract mean pupil size from prestimulus time window (0.9 s) and subtract from data at each time point (baseline correction)
    
    # Pupil size was averaged across trials, separately for each condition. 
    # We averaged data both within the main time window of interest used in 
    # the EEG analysis (3–4 s) as well as within a later time window from 5 to 6 s. 
    # The later time window for the pupil size analysis was chosen to account for
    # the sluggishness of changes in pupil size (Knapen et al., 2016; Winn
    # et al., 2018; Montefusco-Siegmund et al., 2022).
    
    

    # Loop epochs, get corresponding word and save word, surprisal scores as annotations?
    
    
    
curr_block_epochs






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
#epochs = mne.Epochs(
#    eyelink_raw,
#    events = events_from_annot,
#    event_id = event_dict,
#    tmin = -0.3,
#    tmax = 3,
#    preload = True,
#    event_repeated = "merge" # merge all events that are the same
#)


#epochs[:8].plot(events=et_events, event_id=event_dict, order=pupil_channel_idx)

# plot evoked responses to the light flash:
#epochs.average().plot(picks=["pupil_right"])











# FOR LATER:

""" Align EEG & Eyetracking Data """
# Convert event onsets from samples to seconds
#et_flash_times = et_events[:, 0] / raw_et.info["sfreq"]
#eeg_flash_times = eeg_events[:, 0] / raw_eeg.info["sfreq"]
# Align the data
#mne.preprocessing.realign_raw(
#    raw_et, raw_eeg, et_flash_times, eeg_flash_times, verbose="error"
#)
# Add EEG channels to the eye-tracking raw object
#raw_et.add_channels([raw_eeg], force_update_info=True)

# Define a few channel groups of interest and plot the data
#frontal = ["E19", "E11", "E4", "E12", "E5"]
#occipital = ["E61", "E62", "E78", "E67", "E72", "E77"]
#pupil = ["pupil_right"]
#picks_idx = mne.pick_channels(
#    raw_et.ch_names, frontal + occipital + pupil, ordered=True
#)
#raw_et.plot(events=et_events, event_id=event_dict, event_color="g", order=picks_idx)








