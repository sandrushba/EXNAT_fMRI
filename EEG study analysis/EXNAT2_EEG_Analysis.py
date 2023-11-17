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

from mne.io import read_raw_eyelink

import re # for regular expressions

# for plotting
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap #  for plotting bridging between electrodes


# ----------------------------------------------------- # 

# set path to data file here:
curr_data_path = "/Users/merleschuckart/Github/PhD/EXNAT/EEG_study_EXNAT2/EEG study analysis/Data/"
#curr_data_path = "/Users/merle/Github/PhD/EXNAT/EEG_study_EXNAT2/EEG study analysis/Data/"

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
    
    # Print information about the Raw object: Now you can check if all looks 
    # as intended or if channels are missing for example.
    #print(raw.info)
    #print(raw.ch_names)
    
    
    
    """ Set Montage (aka Sensor Locations) """
    
    montage = mne.channels.make_standard_montage("standard_1020") # use 10_20 system as montage
    raw.set_montage(montage, verbose = False)
    
    # plot montage:
    raw.plot_sensors(show_names=True)
    
    
    # TO DO: Set sensor location using data from this fancy digitizing device
    

    
    """ Set triggers """
    
    # print annotations we can construct events from:
    #print(set(raw.annotations.description))
    
    # There are 2 things that might be a bit weird here:
    # 1. There is an additional trigger I did not set in the experiment called 'New Segment/'. 
    #    I think it's created by the BrainVision Recorder everytime you start a recording, so you know where a new recording startet if you record multiple blocks.
    #    We recorded everything in one go, so there should be only 1 of those triggers if I'm correct. 
    # 2. There might be some annotations missing if we skipped the prediction tendency task, but this is fine.
    # 3. Currently the labels of the triggers are not very informative, so I'll have to change the labels.


    """ Delete 'New Segment/' Trigger """
    
    # So first, check how often the weird additional trigger occurs and delete it from the annotations.
    new_segment_count = sum(1 for trigger in raw.annotations.description if 'New Segment/' in trigger)
    # just a sanity check to see if my code works properly: For trial onsets, we should have way more triggers:
    #new_segment_count = sum(1 for trigger in raw.annotations.description if 'Stimulus/S  8' in trigger)
    #print(new_segment_count)
    # As you can see, the trigger occurs only once, so I'm probably right and we can exclude it. 
    annotations = [trigger for trigger in raw.annotations.description if 'New Segment/' not in trigger]
    #Check if it's gone:
    #print('New Segment/' in annotations)
    
    # build a new annotations object without the weird 'New Segment/' trigger
    new_annotations = mne.Annotations(onset = raw.annotations.onset[raw.annotations.description != 'New Segment/'],
                                      duration = raw.annotations.duration[raw.annotations.description != 'New Segment/'],
                                      description = annotations)

    # assign new annotations object to the raw object
    raw.set_annotations(new_annotations)
    
    # check if the weird trigger is still there:
    #print(set(raw.annotations.description))
    # Doesn't seem to be the case so let's hope I did everything correctly.
    
    
    """ Change Trigger Labels """
    
    # Now change the labels of the remaining annotations. 
    # The trigger map from the experiment looks like this:    
    # trigger_map = {'block_onset': 2,
    #                'response_target': 4,
    #                'response_continue': 6,
    #                'trial_onset': 8,
    #                'click_training_onset': 10,
    #                'Reading_Baseline_training_onset': 12,
    #                'Reading_Baseline_main_onset': 14,
    #                '1back_single_training1_onset': 16,
    #                '1back_single_training2_onset': 18,
    #                '1back_single_main_onset': 20,
    #                '1back_dual_main_onset': 22,
    #                '2back_single_training1_onset': 24,
    #                '2back_single_training2_onset': 26,
    #                '2back_single_main_onset': 28,
    #                '2back_dual_main_onset': 30,
    #                'prediction_tendency_task_onset': 32,
    #                'visual_task_main_onset': 34,
    #                'visual_task_training_onset': 36,
    #                'block_offset': 38,
    #                'freq_440_onset': 40,
    #                'freq_440_offset': 42,
    #                'freq_587_onset': 44,
    #                'freq_587_offset': 46,
    #                'freq_782_onset': 48,
    #                'freq_782_offset': 50,
    #                'freq_1043_onset': 52,
    #                'freq_1043_offset': 54,
    #                'ordered': 56,
    #                'random': 58,
    #                'start_experiment': 60,
    #                'end_experiment': 62,
    #                'trial_offset': 64}
    
    # Unfortunately, we can only use trigger labels up to a certain length, 
    # so we have to shorten them a bit:
    trigger_map = {'block_on': 2,
                   'resp_target': 4,
                   'resp_continue': 6,
                   'trial_on': 8,
                   'click_t_on': 10,
                   'BL_t_on': 12,
                   'BL_m_on': 14,
                   '1back_t1_on': 16,
                   '1back_t2_on': 18,
                   '1back_s_m_on': 20,
                   '1back_d_m_on': 22,
                   '2back_t1_on': 24,
                   '2back_t2_on': 26,
                   '2back_s_m_on': 28,
                   '2back_d_m_on': 30,
                   'pt_task_on': 32,
                   'vtask_main_on': 34,
                   'vtask_t_on': 36,
                   'block_off': 38,
                   '440_on': 40,
                   '440_off': 42,
                   '587_on': 44,
                   '587_off': 46,
                   '782_on': 48,
                   '782_off': 50,
                   '1043_on': 52,
                   '1043_off': 54,
                   'ordered': 56,
                   'random': 58,
                   'start_exp': 60,
                   'end_exp': 62,
                   'trial_off': 64}
    
    
    # loop annotations in raw object:
    for old_annotation in set(raw.annotations.description):
        #print(old_annotation)
        
        # use regex to extract the number of the trigger & convert it to int:
        trigger_value = int(re.findall(r'\d+', old_annotation)[0])
        #print(trigger_value)
        
        # find correct trigger label for the trigger value we extracted:
        trigger_label = list(trigger_map.keys())[list(trigger_map.values()).index(trigger_value)] 
        #print(trigger_label)
        
        # change label in the annotations:
        raw.annotations.description[raw.annotations.description == old_annotation] = trigger_label

    # print annotations again to check if it worked:
    #print(set(raw.annotations.description))

    """ Get Eyetracking Data: Read in ascii Dataset as MNE Raw Object"""
    eyelink_raw = read_raw_eyelink(curr_data_path + "part_" + curr_id + "/" + curr_id + ".asc", 
                                   create_annotations = ["blinks", "messages"], # mark blinks in the stream & add trigger messages
                                   preload = True,
                                   apply_offsets = True) # adjust onset time of the mne.Annotations created from exp. messages (= triggers)

    # Check out info to see if everything looks fine:
    eyelink_raw.info

    # plot raw eyetracking data from pupil size channel of right eye 
    # to see if everything's there and the triggers were recorded properly:
    pupil_channel_idx = mne.pick_channels(eyelink_raw.ch_names, ["pupil_right"])
    #eyelink_raw.plot(scalings = dict(eyegaze = 1e3), order = pupil_channel_idx)
    
    
    """ Add Extracking Channels to EEG raw object """
    
    
    
    
    
    
    
    """ Choose Reference """
    # Apply reference (use common average for now because for some reason I didn't record my ref channel)
    raw.set_eeg_reference(ref_channels = 'average')
    
    
    """ Look at Raw Data """
    # Filter & downsample the data for plotting (this is not applied to the actual data)
    #raw_resampled = raw.copy().resample(sfreq = 250)
    #raw_resampled.plot(n_channels = 63, duration = 1, scalings = 'auto', highpass = 2, lowpass = 12, filtorder = 4)
    
    
    
    """ Check If We Have EEG Electrodes That Formed Bridges Due to Too Much Gel """
    
    # If we find some, there's not a lot we can do, but maybe we can exlude them as bad channels 
    # or interpolating them.
    
    # first check electrical distance metrics to estimate electrode bridging
    # "The electrical distance is just the variance of signals subtracted pairwise. 
    # Channels with activity that mirror another channel nearly exactly will have 
    # very low electrical distance." - https://mne.tools/stable/auto_examples/preprocessing/eeg_bridging.html
    
    # It's sufficient to use about 3 min of data to detect bridging, but we need a segment from the end of the 
    # recording where the gel is already set.
    
    raw_bridges = raw.copy()
    #montage = mne.channels.make_standard_montage("standard_1020") # use 10_20 system as montage
    #raw_bridges.set_montage(montage, verbose=False)
    
    ed_data = mne.preprocessing.compute_bridged_electrodes(raw)

    # plot potential bridges in red on topoplot:
    bridged_idx, ed_matrix = ed_data
        
    #mne.viz.plot_bridged_electrodes(raw_bridges.info,
    #                                bridged_idx,
    #                                ed_matrix,
    #                                title = "Bridged Electrodes of Participant " + curr_id,
    #                                topomap_args = dict(vlim = (None, 5)),
    #                                )
    
    
    """ Interpolate Bridged Electrodes or Exclude Data of Current Participant """
    
    # if there are bridges, but not too many (let's say 3, 
    # that would be 6 affected electrodes at most), interpolate them: 
    if len(bridged_idx) > 0 and len(bridged_idx) < 3:
        print("interpolating " + str(len(bridged_idx)) + " bridged electrodes!" )
        raw_interpolated_bridges = mne.preprocessing.interpolate_bridged_electrodes(raw_bridges.copy(), 
                                                                                    bridged_idx = bridged_idx)
        # overwrite raw object with data with fixed channels
        raw = raw_interpolated_bridges.copy()
    
    # if there are more than 3 bridges, exclude participant from further analysis and go to next one:
    elif len(bridged_idx) > 3:
        print("Detected " + str(len(bridged_idx)) +  " electrode bridges for current participant! Excluding dataset from the analysis!")
        next
        
    # if there are no bridges, just keep the df as is
    elif len(bridged_idx) == 0:
        print("no electrode bridging detected here :-)" )        
    
        
    
    
    """ ICA """
    
    # apply high-pass filter to get rid of slow drifts
    raw = raw.filter(l_freq = 1.0, h_freq = None)

    # --> get rid of ICs that represent motor artifacts like head & eye movements or blinks.

    # Initialize ICA with a desired number of components
    # How many components should I use here?!
    ica = mne.preprocessing.ICA(n_components = 20,
                                random_state = 42, # set seed
                                method = "fastica")
    
    # Fit ICA to the raw data
    ica.fit(raw)
    # make computer remind you to check the ICA output:
    os.system('say "queen go check your screen"')


    # Exclude ICA components manually:
        
    # 1. inspect topoplots: Where do we have weird frontal activity?
    # 2. inspect signal of all components and check where blinks or eye movements are visible.
    # 3. inspect power spectrum: Where do we have a weird skewed spectrum, 50 Hz peaks or no (!) alpha? --> probably artifacts

    excl_components = [] # collect indices of all components that should be excluded here
    
    # 1. Plot the ICA components as topoplots
    ica.plot_components()
    # ask user to set the components that should be excluded:
    user_input_excl_components = input("Which components should be excluded? Please provide the corresponding indices separated by commas: ")
    print("You told me to exclude the following components:" + user_input_excl_components)
    # append chosen components to list of components we want to exclude:
    excl_components = excl_components + list(map(int, user_input_excl_components.split(', ')))
    
    
    # 2. Plot the time series of the components
    ica.plot_sources(raw, show_scrollbars = True)
    # ask user to set the components that should be excluded:
    user_input_excl_components = input("Which components should be excluded? Please provide the corresponding indices separated by commas: ")
    print("You told me to exclude the following components:" + user_input_excl_components)
    # append chosen components to list of components we want to exclude:
    excl_components = excl_components + list(map(int, user_input_excl_components.split(', ')))
    
    
    # 3. Plot power spectrum of components
    user_input_excl_components = []
    # Get the power spectrum of the first five ICA components
    ica_sources = ica.get_sources(raw)  # extract ICA sources from raw data
    ica_sources_data = ica_sources.get_data()  # get NumPy array of ICA sources
    freqs, psds = mne.time_frequency.psd_array_welch(ica_sources_data, raw.info['sfreq'], fmin=1, fmax=80, n_fft=2048, window='hamming')
    # Plot the power spectrum of all ICA components
    for i in range(np.shape(ica_sources_data)[0]):
        fig, ax = plt.subplots()
        ax.plot(psds, freqs[i])  # transpose psds[i] to match the shape of freqs
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Power')
        ax.set_title('ICA component {}'.format(i))
        # Show plot
        plt.show() 
         # ask user to set the components that should be excluded:
        user_input_excl_curr_component = input("Exclude this component? (y/n)")
        if user_input_excl_curr_component == "y":
            user_input_excl_components = user_input_excl_components + [i]
    
    print("You told me to exclude the following components: " + ', '.join(map(str, user_input_excl_components)))
    # append chosen components to list of components we want to exclude:
    excl_components = excl_components + user_input_excl_components




    # Exclude ICA components automatically if they have a high correlation with EOG events:

    # Find & exclude ICA components that match EOG events from frontopolar electrodes.
    
    # set channels here that we can use to detect 
    # electrooculogram (EOG) events aka blinks & eye movements
    eog_channels = ["Fp1", "Fp2"] # we don't really have face electrodes, but I guess Fp1 & Fp2 works too
        
    #
    eog_indices, eog_scores = ica.find_bads_eog(raw, 
                                                ch_name = eog_channels, 
                                                reject_by_annotation = False,
                                                measure = "correlation",
                                                threshold = .8)
        
    # The eog indices tell how much each ICA component 
    # correlates with activity in the EOG channels.
    # If the correlation is > .8 for some component, we exclude it.
        
        
    # if we found some matches, visualise eog indices and exclude matching ICA components
    if len(eog_indices) > 0:
            
        # visualise EOG indices (aka correlations of each ICA component with EOG activity)     
        plt.figure(figsize = (12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(eog_indices, marker = 'o', linestyle = '-', color = 'red')
        plt.title('EOG Indices')
        plt.xlabel('Index of ICA Component')
        plt.ylabel('Correlation with EOG activity')
        plt.grid(True)
        
        print("automatically identified " + len(eog_indices) + " components for exclusion.")
    
        # exclude all ICs that match the EOG artifacts from back transformation:
        excl_components = excl_components + eog_indices



    
    # Exclude Components:
    # remove all duplicated component indices from list of components that should be excluded:
    print("excluding the following components from data: " + ', '.join(map(str, excl_components)))
    excl_components = list(set(excl_components))
    ica.exclude = excl_components  # Remove components 1, 3, and 5
    # remove components from the EEG data
    ica.apply(raw)

    
    """ Filtering """
    # --> 5 - 15 Hz for word onset ERPs?
    
    # plot PSD before filtering:
    #raw.plot_psd(fmax = 50, average = True, spatial_colors = False)
    
    # Visualise filter parameters
    filter_params = mne.filter.create_filter(data = raw.get_data(),
                                             sfreq = raw.info["sfreq"],
                                             l_freq = 2,
                                             h_freq = 30,
                                             phase = 'zero', 
                                             fir_window ='hamming',
                                             verbose = None)
    
    #mne.viz.plot_filter(filter_params, raw.info["sfreq"])

    # Apply filter:
    raw = raw.filter(l_freq = 2,
                     h_freq = 30,
                     phase = 'zero', 
                     fir_window ='hamming',
                     verbose = None)


    # plot PSD after filtering
    #raw.plot_psd(fmax = 50, average = True, spatial_colors = False)









        
        
    
    """ 4.4 Select relevant channels """
    #eeg_channel_picks = 
    #raw.pick_channels(eeg_channel_picks)    
        
     
        
    """ Epoching """
    
    """ --> cut data into blocks """
    
    # Create Events from Annotations
    events, event_id = mne.events_from_annotations(raw, event_id = trigger_map)
    #print(event_id)
    #print(events) 
    
    # define onset triggers for all blocks you want to get
    onset_triggers = ['BL_m_on', '1back_d_m_on', '2back_d_m_on']
    
    # get the corresponding values from the trigger_map
    onset_trigger_values = [trigger_map[trigger] for trigger in onset_triggers]
    
    # Find indices where the last value corresponds to the value of one of the onset triggers
    onset_indices = np.where(np.isin(events[:, -1], onset_trigger_values))[0]


    # Now this is where it gets tricky: 
    # For each onset trigger, I want to get the next offset trigger in the data.
    
    # So first, we'll get ALL offset triggers, also the offset triggers for the blocks we're not interested in:
    offset_indices = np.where(np.isin(events[:, -1], trigger_map["block_off"]))[0]

    # Next, we'll get their indices, then we'll merge the onset and offset indices, sort them in ascending order 
    # and we can extract the index following each onset index as the corresponding offset-index:
    
    all_indices = np.sort(np.concatenate((onset_indices, offset_indices)))

    # create a dict for saving onset + offset indices
    onset_to_offset_dict = {}
    
    # loop onset indices:
    for onset_index in onset_indices:
        
        # get the index after the current onset index in "all_indices"
        next_index = all_indices[all_indices > onset_index][0]
        
        # check if the next index is from an offset trigger
        if events[next_index, -1] == trigger_map["block_off"]:
            
            # put both the on- and the offset trigger in the dict
            onset_to_offset_dict[onset_index] = next_index
    
    #print(onset_to_offset_dict)

    # Worked! Now we can cut the data into smaller segments, ranging from 
    # each onset to the corresponding offset trigger.


    # empty dict for storing the segmented data:
    main_blocks_segments = []
    main_block_names = []
    # loop dict with onset and offset pairs:
    for onset_index, offset_index in onset_to_offset_dict.items():
        print("onset index:" + str(onset_index) + ", offset index: " + str(offset_index))

        # get the time points corresponding to the onset and offset indices
        onset_time = events[onset_index, 0] / raw.info["sfreq"]
        offset_time = events[offset_index, 0] / raw.info["sfreq"]
    
        # cut the raw data into a segment from onset to offset
        segment = raw.copy().crop(tmin = onset_time, tmax = offset_time)
    
        # find out which block this belongs to:
        onset_annotation_value = events[onset_index, -1]
        block_name = next((key for key, value in trigger_map.items() if value == onset_annotation_value), None)
    
        # Append the segment to the list of segments
        main_blocks_segments.append(segment)
        # append block name to the list of segment names
        main_block_names.append(block_name)


    # Sanity check: 
    # Check number of trials in one of the segments to see if we did everything correctly.
    
    # loop blocks
    for i in range(0, len(main_block_names)):

        # get segment
        segment_to_plot = main_blocks_segments[i]

        # count the number of 'trial_on' triggers
        count_trials = sum(1 for trigger in segment_to_plot.annotations.description if 'trial_on' in trigger)

        print("number of trials in block " + main_block_names[i] + ": " + str(count_trials))
    
        # Plot the data
        #segment_to_plot.plot()

    # Works! :-)
    
    
    """ --> cut blocks into trials """
    # window: - 1000 to 2000 ms around stimulus onset
    
    
    # loop blocks again & cut epochs:
    epochs_list = []     
    for curr_segment, curr_block_name, curr_block_idx in zip(main_blocks_segments, main_block_names, range(0, len(main_block_names))):
        
        # use "trial_on" as stimulus onset trigger:
        events = mne.pick_events(segment, include = [trigger_map["trial_on"]])
        
        
        """ Cut Epochs & Apply Baseline Correction """
        # Concerning the BL Correction:
        # --> does it make sense to use a baseline period before stimulus onset, 
        # bc this is basically during the presentation of another stimulus or possibly 
        # even more than one?
        
        # From Ditman, T., Holcomb, P. J., & Kuperberg, G. R. (2007). 
        # An investigation of concurrent ERP and self-paced reading methodologies. 
        # Psychophysiology, 44(6), 927–935. doi:10.1111/j.1469-8986.2007.00593.x     
        # "[...] using the 100ms that preceded word onset as a baseline."
        # If they did it, I can do this, too. 
        
        curr_events = pass
    
    
        """ create events from annotations """
        # use regex to look for strings beginning with t (I only need the trial starts)
        # Also, round strings instead of truncating them so we get unique time values
        curr_events, curr_event_ids = mne.events_from_annotations(curr_segment, {"trial_onset": 8})    



        epochs = mne.Epochs(curr_segment, 
                            events = curr_events,
                            event_id = trigger_map['trial_on'], 
                            tmin = -1, 
                            tmax = 2, 
                            detrend = 1, # 1 = linear detrend --> performed before BL correction
                            baseline = (-100, 0), 
                            preload = True)
        
        
        """ Downsample Data """
        # Important: We need to do this after epoching so triggers are not jittered
        # --> https://gist.github.com/larsoner/01642cb3789992fbca59
        
        # downsample the data a bit so it's easier to work with:
        epochs.resample(sfreq = 250)
        print(epochs.info)
    
    
        """ Add Metadata for Each Epoch """
        
        # loop epochs
        for i, epoch in enumerate(epochs):
            
            epoch.info['trial_nr'] = i # trial nr
            epoch.info['block_nr'] = curr_block_idx # block nr
            
            # assign block name
            epoch.info['block_name'] = curr_block_name
            
            # extract a few information from the block name:
                
            # if we have a BL block, it can only be a single-task:
            if curr_block_name[0] == "B":
                epoch.info['cognitive_load'] = "BL"
                epoch.info['task_kind'] = "single_task"
            
            # if we have a 1-back block, check if it's single or dual task:
            elif curr_block_name[0] == "1":
                epoch.info['cognitive_load'] = "1back"
                if curr_block_name[6] == "d":
                    epoch.info['task_kind'] = "dual_task"
                else: epoch.info['task_kind'] = "single_task"
                
            # if we have a 2-back block, check if it's single or dual task:
            elif curr_block_name[0] == "2":
                epoch.info['cognitive_load'] = "2back"
                if curr_block_name[6] == "d":
                    epoch.info['task_kind'] = "dual_task"
                else: epoch.info['task_kind'] = "single_task"
                
          
            # add information on the stimulus material:    
            epoch.info['word'] = None
            
            epoch.info['surprisal_1'] = None
            epoch.info['surprisal_4'] = None
            epoch.info['surprisal_12'] = None
            epoch.info['surprisal_60'] = None
            
            epoch.info['word_length'] = None
            epoch.info['reaction'] = None
            epoch.info['word_freq'] = None

            

        # If epochs object is ready, append to list for all epochs:
        epochs_list.append(epochs)
    
    
    
    
    
    
    
    # Define epochs parameters
event_id = {'Auditory/Left': 1, 'Auditory/Right': 2}
tmin, tmax = -0.2, 0.5
baseline = (None, 0)
reject_criteria = dict(mag=4000e-15,     # 4000 fT
                       grad=4000e-13,    # 4000 fT/cm
                       eeg=150e-6,       # 150 µV
                       eog=150e-6)       # 150 µV

# Create epochs
epochs = mne.Epochs(raw, events, event_id, tmin, tmax, baseline=baseline, reject=reject_criteria, preload=True)

# Plot individual trials for manual inspection and rejection
epochs.plot(n_epochs=5, n_channels=30, title='Manual Trial Inspection', scalings=dict(eeg=50e-6), reject_by_annotation=False)

# After plotting, you can manually reject trials by clicking on them in the plot
# and then pressing the 'D' key (to mark as bad) or 'G' key (to mark as good).

# To get the list of rejected epochs
rejected_epochs = epochs.drop_log

# To get the cleaned epochs (epochs without rejected trials)
clean_epochs = epochs.copy().drop(reject='manually')


    
    
    """ Exclude noisy trials """
    
    
 
    
    """ Compute Word Onset ERPs """
    
    












""" Find events """

# print annotations we can construct events from:
print(set(eyelink_raw.annotations.description))
# --> I want "trial_offset" because the screen gradually changes 
# from grey to white there, so maybe I can see a pupillary light reflex.


(events_from_annot, event_dict) = mne.events_from_annotations(eyelink_raw, 
                                                              event_id = trigger_map)
#print(event_dict)
#print(events_from_annot[30:80]) 

eyelink_raw.plot(start=5, duration=5, order = pupil_channel_idx)




















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








