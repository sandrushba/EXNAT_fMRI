#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on Mon 26 Aug 2024 12:37:42 PM CEST
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.1.3')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'EXNAT_3_fMRI_Psychopy2023.1.3'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'testing_mode': 'no',
    'RT_per_rectangle_oneback_single': '',
    'RT_per_rectangle_twoback_single': '',
    'RT_per_letter_baseline': '',
    'RT_per_letter_oneback_dual': '',
    'RT_per_letter_twoback_dual': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'Data/Psychopy/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/data/tu_martin_cloud/EXNAT/EXNAT_fMRI/Psychopy_experiments/EXNAT_3_fMRI_Psychopy2023.1.3/EXNAT_3_fMRI_Psychopy2023.1.3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 1024], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.sr_research.eyelink.EyeTracker'] = {
    'name': 'tracker',
    'model_name': 'EYELINK 1000 DESKTOP',
    'simulation_mode': False,
    'network_settings': '100.1.1.1',
    'default_native_data_file_name': 'EXPFILE',
    'runtime_settings': {
        'sampling_rate': 1000.0,
        'track_eyes': 'RIGHT_EYE',
        'sample_filtering': {
            'sample_filtering': 'FILTER_LEVEL_2',
            'elLiveFiltering': 'FILTER_LEVEL_OFF',
        },
        'vog_settings': {
            'pupil_measure_types': 'PUPIL_AREA',
            'tracking_mode': 'PUPIL_CR_TRACKING',
            'pupil_center_algorithm': 'ELLIPSE_FIT',
        }
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='EXNAT_3_fMRI_Psychopy2023.1.3', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "settings" ---
# Run 'Begin Experiment' code from functions
# set screen resolution for eyetracker here:
SCN_W, SCN_H = (1280, 800)

### import packages:

# for setting the output encoding to UTF-8
# import sys
# --> if you don't do this, German "Umlaute" can't be displayed correctly:
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
# print Python environment psychopy is currently using
print(sys.executable)

# for showing pictures
from psychopy import visual
# for getting current date & time:
import datetime
# numpy for being able to calculate
import numpy as np
# for random number generator:
import random
# for saving data in csv / working with pd data frames:
import pandas as pd
# additional timing package (I know we have core.wait, but I also want this one)
import time
# for calculations
import math

# Get functions from my custom scripts:
# import all texts and instructions
from EXNAT3_texts_MC_Qs import (instr_pic_path, welcome_text, instr_Reading_Baseline_main_no_click, instr_Reading_pseudotext_no_click, \
    instr_1back_single_main_no_click, instr_pic_1back_single_main_no_click, instr_1back_dual_main_no_click, \
    instr_pic_1back_dual_main_no_click, instr_2back_single_main_no_click, instr_pic_2back_single_main_no_click, instr_2back_dual_main_no_click, \
    instr_pic_2back_dual_main_no_click, warning_sign, text_01, text_01_Q1, text_01_Q1_ans, text_01_Q1_corr, \
    text_01_Q2, text_01_Q2_ans, text_01_Q2_corr, text_01_Q3, text_01_Q3_ans, text_01_Q3_corr, text_02, text_02_Q1, \
    text_02_Q1_ans, text_02_Q1_corr, text_02_Q2, text_02_Q2_ans, text_02_Q2_corr, text_02_Q3, text_02_Q3_ans, \
    text_02_Q3_corr, text_03, text_03_Q1, text_03_Q1_ans, text_03_Q1_corr, text_03_Q2, text_03_Q2_ans, text_03_Q2_corr, \
    text_03_Q3, text_03_Q3_ans, text_03_Q3_corr, text_04, text_04_Q1, text_04_Q1_ans, text_04_Q1_corr, text_04_Q2, \
    text_04_Q2_ans, text_04_Q2_corr, text_04_Q3, text_04_Q3_ans, text_04_Q3_corr, text_05, text_05_Q1, text_05_Q1_ans, \
    text_05_Q1_corr, text_05_Q2, text_05_Q2_ans, text_05_Q2_corr, text_05_Q3, text_05_Q3_ans, text_05_Q3_corr, text_06, \
    text_06_Q1, text_06_Q1_ans, text_06_Q1_corr, text_06_Q2, text_06_Q2_ans, text_06_Q2_corr, text_06_Q3, \
    text_06_Q3_ans, text_06_Q3_corr, text_07, text_07_Q1, text_07_Q1_ans, text_07_Q1_corr, text_07_Q2, text_07_Q2_ans, \
    text_07_Q2_corr, text_07_Q3, text_07_Q3_ans, text_07_Q3_corr, text_08, text_08_Q1, text_08_Q1_ans, text_08_Q1_corr, \
    text_08_Q2, text_08_Q2_ans, text_08_Q2_corr, text_08_Q3, text_08_Q3_ans, text_08_Q3_corr, text_09, text_09_Q1, \
    text_09_Q1_ans, text_09_Q1_corr, text_09_Q2, text_09_Q2_ans, text_09_Q2_corr, text_09_Q3, text_09_Q3_ans, \
    text_09_Q3_corr, text_10, text_10_Q1, text_10_Q1_ans, text_10_Q1_corr, text_10_Q2, text_10_Q2_ans, text_10_Q2_corr, \
    text_10_Q3, text_10_Q3_ans, text_10_Q3_corr, pseudo_text_01, pseudo_text_02, pseudo_text_03, pseudo_text_04, pseudo_text_05, \
    pseudo_text_06, pseudo_text_07, pseudo_text_08, pseudo_text_09)

# import some additional functions I wrote for the experiment:
# from EXNAT3_study_components import change_bg_colour
from nback_colour_generator import create_nback_stimlist, draw_without_replacement, get_targets, create_0back_stimlist


# build little function to flatten nested lists:
def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list


# If I try to save strings containing escaped quotes in a csv file,
# the format gets completely messed up. So we need to escape all
# weird characters like quotes and backslashes with quotes (as odd as it sounds).
def escape_quotes(string):
    # escape quotes with quotes instead of backslashes
    return string.replace('"', '""')

### fMRI set-up ####
# Define a list to store all trigger times and a counter for the number of triggers
all_trigger_times = []
trigger_count = 0

# Start global clock
globalClock = core.Clock()

def wait_for_first_trigger(instr_text, number_of_triggers):
    """
    Wait for the first scanner trigger while displaying instructions on the screen.

    Parameters:
    - instr_text: The instruction text to display.
    """
    trigger_count = number_of_triggers  # Declare trigger_count as global to modify it

    print("Waiting for the first scanner trigger...")

    # Define the instruction text stimulus
    instr_text_stim = visual.TextStim(
        win,
        text=instr_text,
        height=0.04,  # font height relative to height of screen
        pos=(0, 0.08),  # move up a bit
        color="black"
    )

    while True:
        # Display the instructions
        win.setColor(light_bg_col, colorSpace='rgb')
        instr_text_stim.draw()
        win.flip()

        # Check for the first trigger key '5'
        keys = event.getKeys(keyList=['5'])
        if keys:
            first_trigger_time = globalClock.getTime()
            trigger_count += 1
            thisExp.addData('TriggerCount', trigger_count)
            thisExp.addData('TriggerTime', first_trigger_time)
            # Start a new row in the csv
            # thisExp.nextEntry()
            print(f"First trigger received at {first_trigger_time}")
            
            # Wait for an additional 2 seconds
            core.wait(2)
            
            return first_trigger_time, trigger_count


def log_trigger(instr_text, instr_pic, number_of_triggers):
    """
    Wait for the first scanner trigger while displaying instructions on the screen.

    Parameters:
    - instr_text: The instruction text to display.
    """
    trigger_count = number_of_triggers

    print("Waiting for the first scanner trigger...")

    # create text box
    instr_text_stim = visual.TextStim(win,
                                      text=instr_text,
                                      height=0.03,  # font height relative to height of screen
                                      pos=(0, 0.2),  # move up a bit
                                      color="black",
                                      wrapWidth=1)
    # create ImageStim object
    curr_instr_pic = visual.ImageStim(win,
                                      size=(0.9, 0.3),
                                      pos=(0, -0.2),
                                      image=instr_pic)  # set path to image here

    first_trigger_time = None
    while True:
        # Display the instructions
        win.setColor(light_bg_col, colorSpace='rgb')
        instr_text_stim.draw()
        curr_instr_pic.draw()
        win.flip()

        # Check for the first trigger key '5'
        keys = event.getKeys(keyList=['5'])
        if keys:
            first_trigger_time = globalClock.getTime()
            trigger_count += 1
            thisExp.addData('TriggerCount', trigger_count)
            thisExp.addData('TriggerTime', first_trigger_time)
            # Start a new row in the csv
            # thisExp.nextEntry()
            print(f"First trigger received at {first_trigger_time}")
            # break

            # Wait for an additional 8.75 seconds
            core.wait(8.75)

            return first_trigger_time, trigger_count
# Run 'Begin Experiment' code from stimuli
### Stimulus settings

# set colours you want to use for background:
# light_bg_col_hex = "#FDFBF0" # ivory instructions background
# dark_bg_col_hex  = "#505050" # dark grey background for stimuli
#light_bg_col = [(x / 127.5) - 1 for x in (253, 251, 240)]
light_bg_col = [(x / 127.5) - 1 for x in (186, 186, 186)] # ivory instructions background (use RGB -1:1)
dark_bg_col = [(x / 127.5) - 1 for x in (80, 80, 80)]  # dark grey background for stimuli (use RGB -1:1)

# make background light for a start - use rgb -1:1 colour codes
win.setColor(light_bg_col, colorSpace='rgb')

# set colours you want to use for the stimuli:
colours = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"]
print("Preparing experiment with n-back colours:", colours)

#  #D292F3 = weird lilac with a 2000s vibe
#  #F989A2 = Barbie pink
#  #2AB7EF = Twitter blue
#  #88BA3F = medium grass green
# (#D8A244 = dark curry-ish yellow --> excluded!)

#   All colours have a luminance of 70 and a chroma of 74.

#   The colours are selected for distinguishability (is that a word?!)
#   for people with "normal" colour vision as well as for
#   people with protanomaly (red olour vision deficiency (CVD)),
#   deuteranomaly (green CVD) and
#   tritanomaly (blue CVD).

#   People with a "true" colour blindness
#   (i.e. protanopia, deuteranopia, tritanopia)
#   shouldn't participate in this study. */


# ----------------------------------------------
### Shuffle order of texts
print("shuffle texts")
# collect the text IDs in lists so I know which text was shown
all_main_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04", "text_05", "text_06", "text_07", "text_08",
                           "text_09", "text_10"]
all_pseudotexts_nrs_list = ["pseudo_text_01", "pseudo_text_02", "pseudo_text_03", "pseudo_text_04", "pseudo_text_05",
                            "pseudo_text_06", "pseudo_text_07", "pseudo_text_08", "pseudo_text_09"]
# shuffle text numbers
random.shuffle(all_main_texts_nrs_list)
random.shuffle(all_pseudotexts_nrs_list)

# only get first 5 texts for the main blocks
all_main_texts_nrs_list = all_main_texts_nrs_list[0:5]

# only get first text for pseudotext
all_pseudotexts_nrs_list = all_pseudotexts_nrs_list[0:1]

# append "empty" text numbers to the list where we have blocks that are not main blocks.
all_texts_nrs_list = []

# Loop through the range of the length of texts since it's the longer list
for t_idx in range(len(all_main_texts_nrs_list)):
    # if it's the first text, it's the reading BL main block.
    if t_idx == 0:
        # Append 1 text for baseline reading
        all_texts_nrs_list.append(all_main_texts_nrs_list[t_idx])
        # Then append 1 text for pseudotext plus 4 empty blocks for n-back single task
        all_texts_nrs_list.extend([all_pseudotexts_nrs_list[0], "", "", "", ""])
    elif t_idx >= 1:
        # Then 4 reading blocks for dual task
        all_texts_nrs_list.append(all_main_texts_nrs_list[t_idx])

# This will result in a list following your described logic
print(all_texts_nrs_list)

### Set order of blocks
print("set block order for runs")

# RUN 1
# always starts with single reading (BL + PS)
single_reading = ["Reading_Baseline_main_no_click", "Reading_pseudotext_no_click"]

run1_blocks = single_reading
print("Blocks for run1:", run1_blocks)

# RUN 2
# then you get both single n-back conditions
nback1 = ["1back_single_main_no_click", "2back_single_main_no_click"]
random.shuffle(nback1)

nback2 = ["1back_single_main_no_click", "2back_single_main_no_click"]
random.shuffle(nback2)

run2_blocks = nback1 + nback2
print("Blocks for run2:", run2_blocks)

# RUNS 3, 4, 5 & 6
# one dual-task block per run, order randomized
dual_blocks = ["1back_dual_main_no_click", "2back_dual_main_no_click", "1back_dual_main_no_click", "2back_dual_main_no_click"]

random.shuffle(dual_blocks)

run3_blocks = dual_blocks[0]
run4_blocks = dual_blocks[1]
run5_blocks = dual_blocks[2]
run6_blocks = dual_blocks[3]

print("Blocks for run3:", run3_blocks)
print("Blocks for run4:", run4_blocks)
print("Blocks for run5:", run5_blocks)
print("Blocks for run6:", run6_blocks)

### Create n-back colour lists for all blocks

print("create n-back colour lists")
# There are 10 blocks in total
# For run 1, 6 blocks (2 text blocks + 4 single n-back)
# Run 2 and 3 each have 2 dual-task blocks with 300 stimuli each (50 targets)

# So for every block, build a list with colour codes containing the right amount of targets.
# The function is defined in another script bc it's super long,
# I import it at the beginning of this script.

# RUN 1
blocks_textlen = [300, 100] # reading blocks
blocks_target_counts = [25, 25]  # reading blocks

# Now loop this list. Check which condition we have there and then create colour list for each text.
run1_colour_lists = []
run1_target_lists = []
for block_idx, block_length in enumerate(blocks_textlen):
    # get 1st letter of block name - that tells us the condition
    block_cond = run1_blocks[block_idx][0]

    # for each condition, decide which n-back level we want to assign
    # For all no-n-back blocks, we use 1 (just for the colour list generation)
    # global curr_nback_level
    if block_cond == "R":
        curr_nback_level = 1
    elif block_cond == "1":
        curr_nback_level = 1
    else:
        curr_nback_level = 2

    # generate colour list for current block
    # global curr_colours
    curr_colours = create_nback_stimlist(nback_level=curr_nback_level,
                                         colour_codes=colours,
                                         story=["x"] * block_length,
                                         target_abs_min=blocks_target_counts[block_idx],
                                         target_abs_max=blocks_target_counts[block_idx],
                                         zeroback_target=None)

    # get list of targets / non-targets
    curr_targets = get_targets(stim_list=curr_colours,
                               nback_level=curr_nback_level)

    # add to bigger lists
    run1_colour_lists.append(curr_colours)
    run1_target_lists.append(curr_targets)

# RUN 2
blocks_textlen = [60, 60, 60, 60]  # single n-back blocks
blocks_target_counts = [10, 10, 10, 10]

# Now loop this list. Check which condition we have there and then create colour list for each text.
run2_colour_lists = []
run2_target_lists = []
for block_idx, block_length in enumerate(blocks_textlen):
    # get 1st letter of block name - that tells us the condition
    block_cond = run2_blocks[block_idx][0]
    #print(f"block cond: {block_cond}")

    # for each condition, decide which n-back level we want to assign
    # For all no-n-back blocks, we use 1 (just for the colour list generation)
    # global curr_nback_level
    if block_cond == "R":
        curr_nback_level = 1
    elif block_cond == "1":
        curr_nback_level = 1
    elif block_cond == "2":
        curr_nback_level = 2
    #print(f"curr nback: {curr_nback_level}")

    # generate colour list for current block
    # global curr_colours
    curr_colours = create_nback_stimlist(nback_level=curr_nback_level,
                                         colour_codes=colours,
                                         story=["x"] * block_length,
                                         target_abs_min=blocks_target_counts[block_idx],
                                         target_abs_max=blocks_target_counts[block_idx],
                                         zeroback_target=None)

    # get list of targets / non-targets
    curr_targets = get_targets(stim_list=curr_colours,
                               nback_level=curr_nback_level)

    # add to bigger lists
    run2_colour_lists.append(curr_colours)
    run2_target_lists.append(curr_targets)

# RUNS 3, 4, 5 & 6
blocks_textlen = [300, 300, 300, 300] # dual-task blocks
blocks_target_counts = [50, 50, 50, 50]  # dual-task blocks

# Now loop this list. Check which condition we have there and then create colour list for each text.
dual_blocks = run3_blocks, run4_blocks, run5_blocks, run6_blocks
run3_4_5_6_colour_lists = []
run3_4_5_6_target_lists = []
for block_idx, block_length in enumerate(blocks_textlen):
    # get 1st letter of block name - that tells us the condition
    block_cond = dual_blocks[block_idx][0]

    # for each condition, decide which n-back level we want to assign
    # For all no-n-back blocks, we use 1 (just for the colour list generation)
    # global curr_nback_level
    if block_cond == "R":
        curr_nback_level = 1
    elif block_cond == "1":
        curr_nback_level = 1
    elif block_cond == "2":
        curr_nback_level = 2
    #print(f"curr nback: {curr_nback_level}")

    # generate colour list for current block
    # global curr_colours
    curr_colours = create_nback_stimlist(nback_level=curr_nback_level,
                                         colour_codes=colours,
                                         story=["x"] * block_length,
                                         target_abs_min=blocks_target_counts[block_idx],
                                         target_abs_max=blocks_target_counts[block_idx],
                                         zeroback_target=None)

    # get list of targets / non-targets
    curr_targets = get_targets(stim_list=curr_colours,
                               nback_level=curr_nback_level)

    # add to bigger lists
    run3_4_5_6_colour_lists.append(curr_colours)
    run3_4_5_6_target_lists.append(curr_targets)

run3_colour_lists = run3_4_5_6_colour_lists[0]
run4_colour_lists = run3_4_5_6_colour_lists[1]
run5_colour_lists = run3_4_5_6_colour_lists[2]
run6_colour_lists = run3_4_5_6_colour_lists[3]

run3_target_lists = run3_4_5_6_target_lists[0]
run4_target_lists = run3_4_5_6_target_lists[1]
run5_target_lists = run3_4_5_6_target_lists[2]
run6_target_lists = run3_4_5_6_target_lists[3]

print("------ finished preparing stimuli! ------")

# ------------------------------------------

# init block counter for the whole experiment and for each run
exp_block_counter = 0
# init block counter for run1 (two blocks in total)
run1_block_counter = 0
# init block counter for run2 (four blocks in total)
run2_block_counter = 0
# init block counter for run3 (one block in total)
run3_block_counter = 0
# init block counter for run4 (one block in total)
run4_block_counter = 0
# init block counter for run5 (one block in total)
run5_block_counter = 0
# init block counter for run6 (one block in total)
run6_block_counter = 0

print("starting experiment now!")

# --- Initialize components for Routine "eyetr_calibr" ---

# --- Initialize components for Routine "triggers" ---

# --- Initialize components for Routine "pupil_measurement" ---

# --- Initialize components for Routine "wait_for_scanner" ---

# --- Initialize components for Routine "single_reading" ---

# --- Initialize components for Routine "run_finished" ---

# --- Initialize components for Routine "single_nback" ---

# --- Initialize components for Routine "run_finished" ---

# --- Initialize components for Routine "dual_task_block" ---

# --- Initialize components for Routine "end" ---

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "settings" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from setup_eyelink
### Set up connection to EyeLink Eyetracker

# for connecting to Eyelink:
import pylink
import platform  # ?
from PIL import Image  # for host backdrop image
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy  # ?
from string import ascii_letters, digits  # ?

# set up EDF data file:
edf_name = expInfo['participant']  # make sure file name (without .edf) is <= 8 characters
#if len(edf_name) > 4:
#    print("edf file name is too long - choose shorter participant code!")
# eyetracking data should be saved in folder "eyetracking_data",
# located in the same folder as this script

# We download the EDF file with the data from the Eyelink Host PC (aka the Eyetracking PC)
# at the end of this experiment and put it into this folder.


### Connect to the Eyelink Host PC

eyelink_IP = "100.1.1.1"  # set IP address of host PC here
el_tracker = pylink.EyeLink(eyelink_IP)

### Open an EDF file on the Host PC:
edf_file = edf_name + ".EDF"
el_tracker.openDataFile(edf_file)

# Modify EDF file (this is optional):
# If the text starts with "RECORDED BY", it will be available in the DataViewer's Inspector window
# if you click on the EDF session node in the top panel and look for the "Recorded By:" field
# in the bottom panel of the inspector.
preamble_text = "RECORDED BY %s" % os.path.basename(__file__)
el_tracker.sendCommand("add_file_preamble_text '%s'" % preamble_text)

### Configure the Eyetracker:
# put the tracker in offline mode before we change the tracking parameters:
el_tracker.setOfflineMode()

# Get software version: 1-EyeLink I, 2-EyeLink II, 3/4-EyeLink 1000, 5-EyeLink 1000 Plus, 6-Portable DUO
# vstr = el_tracker.getTrackerVersionString()
# eyelink_ver = int(vstr.split()[-1].split('.')[0]
# print version info:
# print("running experiment on %s, version %d" % (vstr, eyelink_ver))


### Data control:

# Which events do you want to save in the EDF file?
# --> include everything by default!
file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
# Which events should be made available over the link?
# --> include everything by default!
link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
# What sample data should be saved in the EDF data file and made available over the link?
# --> include the "HTARGET" flag to save head target sticker data for supported eye trackers with version > 3
eyelink_ver = 5
if eyelink_ver > 3:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,HTARGET,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT'
else:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'

# Optional tracking parameters:
# Sample rate: 250, 500, 1000 or 2000 (depending on tracker)
el_tracker.sendCommand("sample_rate = 1000")
# choose a calibration type: H3, HV3, HV5, HV13 (HV = Horizontal/Vertical)
el_tracker.sendCommand("calibration_type = HV9")  # use 9 target dots for calibration/validation screen
# Set a gamepad button to accept calibration/drift check target
# You need a supported gamepad/button box that's connected to the Host PC
el_tracker.sendCommand("button_function 5 'accept_target_fixation'")  # I think that's enter on our keyboard?

### Set screen resolution:

# get the native screen resolution used by PsychoPy
scn_width, scn_height = win.size

# pass the display pixel coordinates (left, top, right, bottom) to the tracker
el_coords = "screen_pixel_coords = 0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendCommand(el_coords)

# write a DISPLAY_COORDS message to the EDF file
# Data Viewer needs this piece of info for proper visualisation,
# see "Protocol for Eyelink Data to Viewer Integration" in DataViewer user manual
dv_coords = "DISPLAY_COORDS 0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendMessage(dv_coords)


def et_abort_exp():
    """Ends recording """
    el_tracker = pylink.getEYELINK()

    # Stop recording
    if el_tracker.isRecording():
        # add 100 ms to catch final trial events
        pylink.pumpDelay(100)
        el_tracker.stopRecording()

    # put eyetracker into Offline Mode:
    el_tracker.setOfflineMode()

    # clear eyetracking host PC screen and wait for 500 ms
    el_tracker.sendCommand('clear_screen 0')
    pylink.msecDelay(500)

    # close data file:
    el_tracker.closeDataFile()

    # print file transfer message:
    print("EDF data is transferring from Eyetracking PC")

    # download the EDF data from the Host PC to a local data folder:
    el_tracker.receiveDataFile(edf_file, edf_file)

    # Wait 2s to ensure data isn't lost:
    core.wait(2)

    # close eyetracker:
    el_tracker.close()

    # Wait again:
    core.wait(2) 
# keep track of which components have finished
settingsComponents = []
for thisComponent in settingsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "settings" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in settingsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "settings" ---
for thisComponent in settingsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "settings" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "eyetr_calibr" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from calib_setup
### Calibration/Validation Setup

# show instruction for starting Calibration / Validation:
instr_calibr = visual.TextStim(win = win, text = "Eyetracker-Kalibrierung. Zum Starten bitte die Leertaste und dann Enter drücken!", pos = (0,0), color = "black", height = 0.05, wrapWidth = 1)
while True:
    instr_calibr.draw()
    win.flip()
    if event.getKeys(['space']):
        break
win.flip() # clear screen

### Configure Graphics ENVironment (= genv) for the tracker calibration:
genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)
print("version number of EyelinkCoreGraphics library:" + str(genv))

# set colours for the calibratio target
foreground_color = (-1, -1, -1) # black
background_color = tuple(win.color)
genv.setCalibrationColors(foreground_color, background_color)

# set up the calibration target

# The target could be: "circle" (default), "picture", "movie" clip, or a rotating "spiral"
# To change the type of calibration target, set TargetType like so:
# genv.setTargetType("picture")
# genv.setPictureTarget(os.path.join("images", "fixTarget.bmp"))

# We use the default circle here.

# Configure the size of the target in pixels:
# (this is only possible for "circle" and "spiral")
genv.setTargetSize(24)

# request pylink to use the PsychoPy window genv we created above for calibration:
pylink.openGraphicsEx(genv)

# --> Remember we set el_tracker.setOfflineMode()?
#     We didn't set it back to online mode, but the tracker
#     should now switch to online mode automatically as we start the recording.

### Calibrate the Tracker:
el_tracker.doTrackerSetup()
# This will open a window where the calibration is run.
# After the calibration you'll be asked to run the validation.

### Start Recording
el_tracker.startRecording(1, # sample_to_file = yes
                          1, # events_to_file = yes
                          1, # sample_over_link = yes
                          1) # event_over_link = yes

# wait for 500 ms before starting experiment:
pylink.pumpDelay(500)
# keep track of which components have finished
eyetr_calibrComponents = []
for thisComponent in eyetr_calibrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "eyetr_calibr" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eyetr_calibrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "eyetr_calibr" ---
for thisComponent in eyetr_calibrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "eyetr_calibr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "triggers" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from set_triggers
### Prepare triggers

time_after_trigger = 0.003  # wait for 3ms after a trigger before clearing the line with the 0 trigger

### List of Trigger Values
trigger_map = {
    'block_onset': 2,
    'response_target': 4,
    #'response_continue': 6,
    'trial_onset': 8,
    #'click_training_onset': 10,
    'Reading_pseudotext_no_click_onset': 12,
    'Reading_Baseline_main_no_click_onset': 14,
    #'1back_single_training1_onset': 16,
    #'1back_single_training2_onset': 18,
    '1back_single_main_no_click_onset': 20,
    '1back_dual_main_no_click_onset': 22,
    #'2back_single_training1_onset': 24,
    #'2back_single_training2_onset': 26,
    '2back_single_main_no_click_onset': 28,
    '2back_dual_main_no_click_onset': 30,
    #'prediction_tendency_task_onset': 32,
    #'visual_task_main_onset': 34,
    #'visual_task_training_onset': 36,
    'block_offset': 38,
    #'freq_440_onset': 40,
    #'freq_440_offset': 42,
    #'freq_587_onset': 44,
    #'freq_587_offset': 46,
    #'freq_782_onset': 48,
    #'freq_782_offset': 50,
    #'freq_1043_onset': 52,
    #'freq_1043_offset': 54,
    #'ordered_onset': 56,
    #'random_onset': 58,
    'start_experiment': 60,
    'end_experiment': 62,
    'trial_offset': 64,
    'eyetracking_baseline': 66,
    'test_trigger': 68
}

# Function to send trigger value by specifying event name
def send_trigger(event_name):
    # get corresponding trigger value:
    trigger_value = trigger_map[event_name]

    # send trigger to Eyetracker:
    el_tracker.sendMessage(event_name)

send_trigger(event_name='start_experiment')
# keep track of which components have finished
triggersComponents = []
for thisComponent in triggersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "triggers" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "triggers" ---
for thisComponent in triggersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "triggers" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "pupil_measurement" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from pupil_measure
### PUPIL SIZE BASELINE MEASUREMENT BLOCK
print(f"trigger count: {trigger_count}")
start_block_instr = visual.TextStim(win=win,
                                    text="Das Experiment startet in 10 Sekunden. Bitte schauen Sie solange auf das Fixationskreuz.",
                                    pos=(0, 0),
                                    color="black",
                                    height=0.03,
                                    wrapWidth=1)
# CREATE CLOCK:
my_block_clock = core.Clock()
my_block_clock.reset()  # start block clock

while my_block_clock.getTime() < 3:
    start_block_instr.draw()
    win.flip()
    if event.getKeys(['space']):
        break
win.flip()

# show fixation cross for 10 seconds
fix_cross = visual.TextStim(win=win,
                            text="+",
                            pos=(0, 0),
                            color="black",
                            height=0.2,
                            wrapWidth=1)

my_block_clock.reset()  # start block clock

while my_block_clock.getTime() < 10:
    fix_cross.draw()
    win.flip()
    if event.getKeys(['escape']):
        break
win.flip()  # clear screen again
# keep track of which components have finished
pupil_measurementComponents = []
for thisComponent in pupil_measurementComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pupil_measurement" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pupil_measurementComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pupil_measurement" ---
for thisComponent in pupil_measurementComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pupil_measurement" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "wait_for_scanner" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from scanner_wait
#################################################
#              Welcome to experiment            #
#################################################
# this routine waits for the scanner trigger and then starts the experiment
print(f"trigger count: {trigger_count}")
# clear buffer of all previously recorded key events:
event.clearEvents()

# Reset global clock
# globalClock = core.Clock()
# globalClock.reset()

### Show instructions
# set instruction text
instr_text = locals()["welcome_text"]

# Wait for the first trigger
first_trigger_time, trigger_count = wait_for_first_trigger(instr_text, trigger_count)
# keep track of which components have finished
wait_for_scannerComponents = []
for thisComponent in wait_for_scannerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "wait_for_scanner" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_scannerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "wait_for_scanner" ---
for thisComponent in wait_for_scannerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "wait_for_scanner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_run1_single_reading = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_run1_single_reading')
thisExp.addLoop(loop_run1_single_reading)  # add the loop to the experiment
thisLoop_run1_single_reading = loop_run1_single_reading.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_run1_single_reading.rgb)
if thisLoop_run1_single_reading != None:
    for paramName in thisLoop_run1_single_reading:
        exec('{} = thisLoop_run1_single_reading[paramName]'.format(paramName))

for thisLoop_run1_single_reading in loop_run1_single_reading:
    currentLoop = loop_run1_single_reading
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_run1_single_reading.rgb)
    if thisLoop_run1_single_reading != None:
        for paramName in thisLoop_run1_single_reading:
            exec('{} = thisLoop_run1_single_reading[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "single_reading" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from single_reading_blocks
    #################################################
    #        Blocks with text – reading only        #
    #################################################
    # this routine is for all blocks with texts that are paced, i.e., visually presented without space bar
    # this is for reading only texts
    
    # make mouse invisible during experiment
    # mouse = io.devices.mouse
    win.setMouseVisible(False)
    
    if 0 <= exp_block_counter <= 1:
        # We collected RTs & words from the self-paced block of each condition
        RT_per_letter_baseline = int(expInfo['RT_per_letter_baseline'])
        print("Using RT_per_letter_baseline for this block:", RT_per_letter_baseline)
    
        # get block kind
        curr_block = run1_blocks[run1_block_counter]
    
        # ----------------------------------
    
        # clear buffer of all previously recorded key events:
        event.clearEvents()
    
        ### specify settings for the current block
        ### Prepare stimuli:
    
        if curr_block in ["Reading_Baseline_main_no_click", "Reading_pseudotext_no_click"]:
            print(f"Start preparing block {curr_block}")
    
            # light background
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
    
            ### Show instructions
            if curr_block == "Reading_Baseline_main_no_click":
    
                # set instruction text
                instr_text = locals()["instr_" + curr_block]
                # create text box
                instr_text_stim = visual.TextStim(win,
                                                  text=instr_text,
                                                  height=0.03,  # font height relative to height of screen
                                                  pos=(0, 0.08),  # move up a bit
                                                  color="black")
    
                # show instructions on screen
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim.draw()
                win.flip()
                core.wait(8.75)  # wait for 8.75 s
                # If esc is pressed, end the experiment:
                if 'escape' in event.getKeys():
                    et_abort_exp()  # shut down eyetrigger and download incremental data
                    # close trigger & close experiment
                    core.wait(0.5)
                    core.quit()
    
                # get text nr:
                curr_text_nr = all_texts_nrs_list[exp_block_counter]
                curr_text = locals()[curr_text_nr]
    
                # compute RTs using participant's average reading speed / letter
                # we define a minimum and a maximum duration for each word
                # the minimum is based on 5 x RT per letter in the respective condition
                # the max duration is based on a time-out of 1.5 s in the reading baseline condition
                minimum_duration = 5 * RT_per_letter_baseline
                maximum_duration = 1500
                curr_durations = []
                for word in curr_text:
                    duration = RT_per_letter_baseline * math.log((len(word))) + 4 * RT_per_letter_baseline
                    if duration < maximum_duration:
                        curr_durations.append(max(duration, minimum_duration))
                    else:
                        curr_durations.append(maximum_duration)
    
                # print(f"\tdurations for paced baseline block: {curr_durations}")
    
                ### change background colour
                win.setColor(dark_bg_col, colorSpace='rgb')
                win.flip()
    
                # show main block questions
                skip_questions_paced = False
    
            elif curr_block == "Reading_pseudotext_no_click":
    
                # set instruction text
                instr_text = locals()["instr_" + curr_block]
                # create text box
                instr_text_stim = visual.TextStim(win,
                                                  text=instr_text,
                                                  height=0.03,  # font height relative to height of screen
                                                  pos=(0, 0.08),  # move up a bit
                                                  color="black",
                                                  wrapWidth=1.5)
    
                # show instructions on screen
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim.draw()
                win.flip()
                core.wait(8.75)  # wait for 8.75 s
                # If esc is pressed, end the experiment:
                if 'escape' in event.getKeys():
                    et_abort_exp()  # shut down eyetrigger and download incremental data
                    # close trigger & close experiment
                    core.wait(0.5)
                    core.quit()
    
                # get text nr:
                curr_text_nr = all_texts_nrs_list[exp_block_counter]
                curr_text = locals()[curr_text_nr]
    
                # compute RTs using participant's average reading speed / letter
                # we define a minimum and a maximum duration for each word
                # the minimum is based on 5 x RT per letter in the respective condition
                # the max duration is based on a time-out of 1.5 s in the reading baseline condition
                minimum_duration = 5 * RT_per_letter_baseline
                maximum_duration = 1500
                curr_durations = []
                for word in curr_text:
                    duration = RT_per_letter_baseline * math.log((len(word))) + 4 * RT_per_letter_baseline
                    if duration < maximum_duration:
                        curr_durations.append(max(duration, minimum_duration))
                    else:
                        curr_durations.append(maximum_duration)
    
                # print(f"\tdurations for paced baseline block: {curr_durations}")
    
                ### change background colour
                win.setColor(dark_bg_col, colorSpace='rgb')
                win.flip()
    
                # show main block questions
                skip_questions_paced = True
    
            # Define n-back level
            curr_nback_cond = None
    
            print(f"\tcurrent n-back condition: {curr_nback_cond}")
            print(f"\tcurrent text: {curr_text_nr}")
            print(f"\texp block counter: {exp_block_counter}")
    
            # get list with targets & list with colours
            curr_targets = run1_target_lists[run1_block_counter]
            curr_colours = run1_colour_lists[run1_block_counter]
    
        ### Start block loop
        if curr_block in ["Reading_Baseline_main_no_click", "Reading_pseudotext_no_click"]:
    
            # create empty text stimulus
            stim = visual.TextStim(win=win,
                                   text=" ",
                                   pos=(0, 0),  # center stimulus
                                   font="Times New Roman",
                                   height=0.07)
    
            stim.draw()
            win.flip()
    
            # clear buffer of all previously recorded key events:
            event.clearEvents()
            defaultKeyboard.clearEvents()
    
            # CREATE CLOCKS:
            my_block_clock = core.Clock()
            my_block_clock.reset()  # start block clock
            start_time = my_block_clock.getTime()  # get start time of block
            # also create trial clock
            my_trial_clock = core.Clock()
    
            # send block onset trigger
            send_trigger(curr_block + "_onset")
    
            # loop words in current text
            for trial_idx, curr_word in enumerate(curr_text):
                # print("current idx: " + str(trial_idx) + ", curr word:" + curr_word)
    
                # Log trigger information before or after other trial-specific logging
                # trigger_count = log_trigger(trigger_count)
    
                ### prepare & show current word:
                # get current colour
                curr_colour = curr_colours[trial_idx]
    
                # get duration for current word
                curr_duration = curr_durations[trial_idx] / 1000  # convert ms to seconds
                # print("duration for current word (in s):", curr_duration)
    
                # get trial number (start counting from 1, so add 1)
                curr_trial_nr = trial_idx + 1
    
                # set current word & colour as content of text stimulus
                stim.color = curr_colour
                stim.text = curr_word
    
                # show word on screen
                stim.draw()  # draw word on screen
                # update the window to clear the screen and display
                # the stimulus, send trigger on flip
                win.callOnFlip(send_trigger, "trial_onset")
    
                # start trial clock & record trial onset time
                my_trial_clock.reset()
                onset_time = my_trial_clock.getTime()
                global_onset_time = globalClock.getTime()
                onset_time_rel2trigger = global_onset_time - first_trigger_time
    
                ### start recording responses
                # start while loop that looks for responses
                # --> end while loop only if duration for current word is over
                while my_trial_clock.getTime() < (onset_time + curr_duration):
    
                    stim.draw()
                    win.flip()
    
                    # check for key responses:
                    keys = event.getKeys(['1', 'escape'])
    
                    # if there were, check responses:
                    for key in keys:
    
                        # if participant pressed button "c" for the first time and it's an n-back condition
                        # where they're actually supposed to do that (aka not a reading baseline condition)...
                        if key == '1' and curr_nback_cond != None and saw_target == False:
                            # get reaction time
                            curr_nback_RT = my_trial_clock.getTime() * 1000
                            # send trigger for response:
                            send_trigger("response_target")
                            # only get first target response, we don't care if they press the button more than once:
                            saw_target = True
    
                        # If esc is pressed, end the experiment:
                        elif key == 'escape':
                            et_abort_exp()  # shut down eyetrigger and download incremental data
                            # close trigger & close experiment
                            # core.wait(time_after_trigger)
                            # parallel.setData(0)
                            core.wait(0.5)
                            core.quit()
    
                ### end trial
                # print("\tend paced trial")
                # stop display of current word & send trial offset trigger
                win.callOnFlip(send_trigger, "trial_offset")
    
                # check whether response was hit, miss, false alarm or correct rejection
                # they saw a target and there was one: hit
                if curr_nback_cond != None:
                    if saw_target and curr_target:
                        curr_nback_response = "hit"
                    # they didn't see a target but there was one: miss
                    elif saw_target == False and curr_target:
                        curr_nback_response = "miss"
                        curr_nback_RT = None
                    # they didn't see a target and there was none: correct rejection
                    elif saw_target == False and curr_target == False:
                        curr_nback_response = "correct rejection"
                        curr_nback_RT = None
                    # they saw a target but there was none: false alarm
                    elif saw_target and curr_target == False:
                        curr_nback_response = "false alarm"
                # if it wasn't an n-back task block:
                else:
                    curr_target = None
                    curr_nback_response = None
                    curr_nback_RT = None
    
                ### save everything in output csv
                thisExp.addData('colour', curr_colour)
                thisExp.addData('global_onset_time', global_onset_time)
                thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
                thisExp.addData('target', curr_target)
                thisExp.addData('nback_response', curr_nback_response)
                thisExp.addData('nback_RT', curr_nback_RT)  # in ms
                thisExp.addData('duration', curr_duration * 1000)  # in ms
                thisExp.addData('text_nr', curr_text_nr)
                thisExp.addData('trial_nr', curr_trial_nr)
                thisExp.addData('block_nr_exp', exp_block_counter+1)
                thisExp.addData('run_nr', '1')
                thisExp.addData('block_nr_run', run1_block_counter+1)
                thisExp.addData('block_name', curr_block)
                thisExp.addData('n-back_level', curr_nback_cond)
                # careful, make sure quotes in the strings are escaped using a
                # quote (weird, I know) so it's properly saved in the CSV:
                thisExp.addData('word', escape_quotes(curr_word))
    
                # start a new row in the csv
                thisExp.nextEntry()
    
                ### IF TESTING MODE ENABLED: end loop after 4 trials
                if expInfo['testing_mode'] == "yes":
                    if trial_idx == 3:
                        break
    
            print("finished presenting trials")
    
            # send block offset trigger
            send_trigger("block_offset")
    
            if curr_block == "Reading_pseudotext_no_click":
                # show main block questions
                skip_questions_paced = True
    
                # go to next run
                exp_block_counter += 1
                run1_block_counter += 1
                print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
                continueRoutine = False
    
                # If there are still blocks left, go to next one.
                # If not, end loop here:
                if run1_block_counter == 2:
                    print(f"Finished block {run1_block_counter}/2 in run 1, moving on to next run!")
                    loop_run1_single_reading.finished = True
    # Run 'Begin Routine' code from questions
    ##########################################################
    #              Text Comprehension Questions              #
    ##########################################################
    
    def setup_question(question_text, answers_text):
        question = visual.TextStim(win, text=question_text, pos=(0, 0.2), color="black", height=0.03, anchorHoriz='center', alignText='center', wrapWidth=1)
        answers = [visual.TextStim(win, text=ans, pos=(0, 0.1 - i * 0.08), color="black", height=0.03, wrapWidth=1, anchorHoriz='center', alignText='center') for i, ans in enumerate(answers_text)]
        return question, answers
    
    def display_question_and_get_response(question, answers, correct_answer):
        defaultKeyboard.clearEvents()
        
        # Set-up time to write into logfile
        question_time = globalClock.getTime()
        onset_time_rel2trigger = question_time - first_trigger_time
    
        question.autoDraw = True
        for answer in answers:
            answer.autoDraw = True
        instr_text.autoDraw = True
    
        countdown_timer = visual.TextStim(win, text='', pos=(0, -0.25), color="grey", height=0.02, anchorHoriz='center', alignText='center', wrapWidth=1)
    
        chosen_ans = "NA"
        is_correct = "NA"
        button_pressed = "NA"
        response_received = False
    
        # Start a clock to track response time
        response_clock = core.Clock()
    
        # Countdown from 10 seconds
        while response_clock.getTime() < 10:
            remaining_time = 10 - int(response_clock.getTime())
            countdown_timer.text = f"Zeit: {remaining_time}"
            countdown_timer.draw()
            win.flip()
    
            keys = defaultKeyboard.getKeys(['1', '2', '3', '4'], waitRelease=False)
            if keys:
                key_name = keys[0].name  # Get the name of the first key pressed
                button_pressed = key_name
    
                # Now, use the key_name to determine the action
                if key_name == '1':
                    index = 0  # Corresponds to the first choice
                elif key_name == '2':
                    index = 1  # Corresponds to the second choice
                elif key_name == '3':
                    index = 2  # Corresponds to the third choice
                elif key_name == '4':
                    index = 3  # Corresponds to the fourth choice
                else:
                    index = None  # Just in case, not really needed if you're sure about the input keys
    
                # Proceed with your logic based on the index
                if index is not None:
                    chosen_ans = chr(97 + index)  # Convert index to letter ('a', 'b', 'c', 'd')
                    is_correct = chosen_ans == correct_answer  # Assuming correct_answer is defined ('a', 'b', 'c', or 'd')
                    for i, answer in enumerate(answers):
                        answer.setColor("green" if i == index else "black")
                    win.flip()
                    core.wait(0.5)  # Ensure the color change is visible
                    response_received = True
                    break
    
        # Hide the countdown timer after it finishes
        countdown_timer.text = ''
        countdown_timer.draw()
        win.flip()
    
        # If no response is received within 10 seconds, return "NA"
        if not response_received:
            chosen_ans = "NA"
            is_correct = "NA"
            button_pressed = "NA"
    
        return question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed
    
    def reset_answers(answers):
        for answer in answers:
            answer.setColor("black")
        question.autoDraw = False
        instr_text.autoDraw = False
        for answer in answers:
            answer.autoDraw = False
    
    # Set up instructions
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    instr_text = visual.TextStim(win, text="(Bitte benutzen Sie die Tasten 1, 2, 3 und 4, um die richtige Antwort auszuwählen.)", color="grey", pos=(0, -0.3), wrapWidth=2, height=0.018)
    event.clearEvents()
    
    # Assuming skip_questions_paced and other variables are defined
    if not skip_questions_paced:
        # Setup for Q1
        Q1_text = locals()[curr_text_nr + "_Q1"]
        Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
        Q1_correct = locals()[curr_text_nr + "_Q1_corr"]
    
        question, answers = setup_question(Q1_text, Q1_answers)
        question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q1_correct)
        print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)
    
        # save data:
        thisExp.addData('global_onset_time', question_time)
        thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
        thisExp.addData('question', 'Q1')
        thisExp.addData('button_pressed', button_pressed)
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q1_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter+1)
        thisExp.addData('run_nr', '1')
        thisExp.addData('block_nr_run', run1_block_counter+1)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)
    
        # start a new row in the csv
        thisExp.nextEntry()
    
        # Setup for Q2
        Q2_text = locals()[curr_text_nr + "_Q2"]
        Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
        Q2_correct = locals()[curr_text_nr + "_Q2_corr"]
    
        question, answers = setup_question(Q2_text, Q2_answers)
        question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q2_correct)
        print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)
    
        # save data:
        thisExp.addData('global_onset_time', question_time)
        thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
        thisExp.addData('question', 'Q2')
        thisExp.addData('button_pressed', button_pressed)
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q2_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter+1)
        thisExp.addData('run_nr', "1")
        thisExp.addData('block_nr_run', run1_block_counter+1)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)
    
        # start a new row in the csv
        thisExp.nextEntry()
    
        # Setup for Q3
        Q3_text = locals()[curr_text_nr + "_Q3"]
        Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
        Q3_correct = locals()[curr_text_nr + "_Q3_corr"]
    
        question, answers = setup_question(Q3_text, Q3_answers)
        question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q3_correct)
        print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)
    
        # save data:
        thisExp.addData('global_onset_time', question_time)
        thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
        thisExp.addData('question', 'Q3')
        thisExp.addData('button_pressed', button_pressed)
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q3_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter+1)
        thisExp.addData('run_nr', "1")
        thisExp.addData('block_nr_run', run1_block_counter+1)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)
    
        # start a new row in the csv
        thisExp.nextEntry()
    
        # go to next block!
        exp_block_counter += 1
        run1_block_counter += 1
        print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
        print(f"Going to block {run1_block_counter + 1}/2 in run 1 now!")
        continueRoutine = False
    
        # If there are still blocks left, go to next one.
        # If not, end loop here:
        if run1_block_counter == 2:
            loop_run1_single_reading.finished = True
    # keep track of which components have finished
    single_readingComponents = []
    for thisComponent in single_readingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "single_reading" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in single_readingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "single_reading" ---
    for thisComponent in single_readingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "single_reading" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'loop_run1_single_reading'


# --- Prepare to start Routine "run_finished" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from finished_run
#################################################
#                  Finished run                 #
#################################################

# light background
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

if exp_block_counter == 2 or exp_block_counter == 6:

    # reset (local) trigger counter since new run starts from 0
    trigger_count = 0

    run_finished_text = "Diese Runde des Experiments ist nun zu Ende. Bitte bleiben Sie ruhig liegen, es geht gleich weiter."
    # set text
    instr_text = run_finished_text
    # create text box
    instr_text_stim = visual.TextStim(win,
                                      text=instr_text,
                                      height=0.04,
                                      pos=(0, 0),
                                      color="black")

    # display the text on screen until Space is pressed
    while True:
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        instr_text_stim.draw()
        win.flip()
        # end screen if participant presses space
        if 'return' in event.getKeys():
            print("\tMoving on to next run!")
            break
        # If esc is pressed, end the experiment:
        elif 'escape' in event.getKeys():
            et_abort_exp()  # shut down eyetrigger and download incremental data
            # close trigger & close experiment
            core.wait(0.5)
            core.quit()
            break
# keep track of which components have finished
run_finishedComponents = []
for thisComponent in run_finishedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "run_finished" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in run_finishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "run_finished" ---
for thisComponent in run_finishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "run_finished" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_run2_single_nback = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_run2_single_nback')
thisExp.addLoop(loop_run2_single_nback)  # add the loop to the experiment
thisLoop_run2_single_nback = loop_run2_single_nback.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_run2_single_nback.rgb)
if thisLoop_run2_single_nback != None:
    for paramName in thisLoop_run2_single_nback:
        exec('{} = thisLoop_run2_single_nback[paramName]'.format(paramName))

for thisLoop_run2_single_nback in loop_run2_single_nback:
    currentLoop = loop_run2_single_nback
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_run2_single_nback.rgb)
    if thisLoop_run2_single_nback != None:
        for paramName in thisLoop_run2_single_nback:
            exec('{} = thisLoop_run2_single_nback[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "single_nback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from blocks_single_nback
    # ################################################
    #         Blocks w/o text – single n-back        #
    # ################################################
    # this routine is for all blocks where there are coloured rectangles
    # instead of words and participants are presented with a paced version, i.e., rectangles are presented based on their
    # reaction times in the training before scanning
    
    if 2 <= exp_block_counter <= 5:
    
        event. Mouse(visible=False)
    
        # clear buffer of all previously recorded key events:
        event.clearEvents()
    
        ### Prepare stimuli:
    
        RT_per_rectangle_oneback_single = int(expInfo['RT_per_rectangle_oneback_single'])
        RT_per_rectangle_twoback_single = int(expInfo['RT_per_rectangle_twoback_single'])
    
        # get block kind
        curr_block = run2_blocks[run2_block_counter]
    
        if curr_block in ["1back_single_main_no_click", "2back_single_main_no_click"]:
            print(f"Start preparing block {curr_block}")
            if curr_block == "1back_single_main_no_click":
                print("Using RT_per_rectangle_oneback for this block:", RT_per_rectangle_oneback_single)
    
            elif curr_block == "2back_single_main_no_click":
                print("Using RT_per_rectangle_twoback for this block:", RT_per_rectangle_twoback_single)
    
            # light background
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
    
            ### Show instructions
            # if it's the first block of this run, wait for the first scanner trigger before moving on
            if exp_block_counter == 2:
    
                # set instruction text
                instr_text = locals()["instr_" + curr_block]
                instr_pic = locals()["instr_pic_" + curr_block]
    
                first_trigger_time, trigger_count = log_trigger(instr_text, instr_pic, trigger_count)
    
            else:
                # set instruction text
                instr_text = locals()["instr_" + curr_block]
                # create text box
                instr_text_stim = visual.TextStim(win,
                                                  text=instr_text,
                                                  height=0.03,  # font height relative to height of screen
                                                  pos=(0, 0.2),  # move up a bit
                                                  color="black",
                                                  wrapWidth=1)
                # instr_text_stim = visual.TextBox2(win,
                #                                   text=instr_text,
                #                                   letterHeight=0.03,  # font height relative to height of screen
                #                                   pos=(0, 0.2),  # move up a bit
                #                                   color="black")
                #                                   #wrapwidth = 1.5)
                # create ImageStim object
                curr_instr_pic = visual.ImageStim(win,
                                                  size=(0.8, 0.3),
                                                  pos=(0, -0.2),
                                                  image=locals()["instr_pic_" + curr_block])  # set path to image here
    
                # show instructions on screen
                instr_text_stim.draw()
                curr_instr_pic.draw()
                win.flip()
                core.wait(8.75)  # wait for 3s before starting response window
                # If esc is pressed, end the experiment:
                if 'escape' in event.getKeys():
                    et_abort_exp()  # shut down eyetrigger and download incremental data
                    # close trigger & close experiment
                    core.wait(0.5)
                    core.quit()
    
            ### change background colour
            win.setColor(dark_bg_col, colorSpace='rgb')
            win.flip()
    
            # get n-back condition:
            curr_nback_cond = curr_block[0]  # get first character of block name
    
            # if it is a 1 or a 2, set that as current n-back level:
            if curr_nback_cond in ['1', '2']:
                curr_nback_cond == int(curr_nback_cond)
            # if it's neither 1 nor 2, it has to be a block without n-back,
            # so set curr_nback_cond to None
            else:
                curr_nback_cond = None
    
            print(f"\tcurrent n-back condition: {curr_nback_cond}")
    
            # get list with targets & list with colours
            curr_targets = run2_target_lists[run2_block_counter]
            curr_colours = run2_colour_lists[run2_block_counter]
    
            # determine duration per rectangle for this block
            # we use average time per rectangle as duration here and add an increment over the duration of the block
            if curr_block == "1back_single_main_no_click":
                curr_durations = []
                for rect in curr_targets:
                    curr_durations.append(RT_per_rectangle_oneback_single)
    
                # Latency factor of an incremental increase (increment per trial = 3 ms) added over duration of entire
                # block assuming that participants get tired over the course of the block and thus need a bit more time:
                increment_per_trial = 3
                maximum_duration = 1500  # 1.5 seconds for 1back
                for i in range(len(curr_durations)):
                    # Calculate incremental increase for current trial
                    increment = (i + 1) * increment_per_trial
                    # Add incremental increase to current trial's duration
                    incremented_duration = curr_durations[i] + increment
                    # Ensure the duration does not exceed the maximum duration
                    curr_durations[i] = min(incremented_duration, maximum_duration)
    
            elif curr_block == "2back_single_main_no_click":
                curr_durations = []
                for rect in curr_targets:
                    curr_durations.append(RT_per_rectangle_twoback_single)
    
                # Latency factor of an incremental increase (increment per trial = 3 ms) added over duration of entire
                # block assuming that participants get tired over the course of the block and thus need a bit more time:
                increment_per_trial = 3
                maximum_duration = 2000  # 2 seconds for 2back
                for i in range(len(curr_durations)):
                    # Calculate incremental increase for current trial
                    increment = (i + 1) * increment_per_trial
                    # Add incremental increase to current trial's duration
                    incremented_duration = curr_durations[i] + increment
                    # Ensure the duration does not exceed the maximum duration
                    curr_durations[i] = min(incremented_duration, maximum_duration)
    
            ### Start block loop
    
            # CREATE CLOCKS:
            my_block_clock = core.Clock()
            my_block_clock.reset()  # start block clock
            start_time = my_block_clock.getTime()  # get start time of block
            # also create trial clock
            my_trial_clock = core.Clock()
    
            # create empty stimulus
            stim = visual.Rect(win=win,
                               width=0.4,  # width = 3 * 1° visual angle (to make it look rectangle-ish)
                               height=0.15,  # height = 1° visual angle (just like words)
                               # colorSpace = "hex",
                               pos=(0, 0))  # center stimulus
    
            stim.draw()
            win.flip()
    
            # clear buffer of all previously recorded key events:
            event.clearEvents()
            defaultKeyboard.clearEvents()
    
            # send block onset trigger
            send_trigger(curr_block + "_onset")
    
            # loop colours in current text
            for trial_idx, curr_col in enumerate(curr_colours):
                # print("current idx: " + str(trial_idx) + ", curr colour:" + curr_col)
    
                ### prepare & show current trial:
                my_trial_clock.reset()  # start trial clock
                onset_time = my_trial_clock.getTime()
    
                # if it's a block with an n-back task, prepare target list
                if curr_nback_cond != None:
                    curr_target = curr_targets[trial_idx]
                    saw_target = False
    
                # get duration for current trial
                curr_duration = curr_durations[trial_idx] / 1000  # convert ms to seconds
    
                # get trial number (start counting from 1, so add 1)
                curr_trial_nr = trial_idx + 1
    
                ### ISI: wait for 200 ms
                while my_trial_clock.getTime() < 0.2:
                    win.flip()  # don't draw anything
                    core.wait(0.005)  # wait 5 ms before next iteration
    
                # set current colour as colour of rectangle
                stim.fillColor = curr_col
    
                # draw stimulus on screen
                stim.draw()
                win.flip()
    
                # show stimulus on screen & send trigger:
                stim.draw()  # draw stimulus on screen
                # update the window to clear the screen and display
                # the stimulus, send trigger on flip
                win.callOnFlip(send_trigger, "trial_onset")
    
                # start trial clock for measuring RTs from stimulus onset
                my_trial_clock.reset()
                onset_time = my_trial_clock.getTime()
                global_onset_time = globalClock.getTime()
                onset_time_rel2trigger = global_onset_time - first_trigger_time
    
                ### start recording responses
                # start "endless" while loop that looks for responses
                # --> end while loop only if duration for current word is over
                while my_trial_clock.getTime() < (onset_time + curr_duration):
    
                    # draw stimulus on screen
                    stim.draw()
                    win.flip()
    
                    # check for responses:
                    keys = event.getKeys(['1', 'escape'])
                    button_pressed = "NA"
    
                    # check if there was a response. If there wasn't, we can go straight
                    # to the next iteration
                    for key in keys:
    
                        # if participant pressed button "1" for the first time and it's an n-back condition
                        if key == '1' and curr_nback_cond != None and saw_target == False:
                            # get reaction time
                            curr_nback_RT = my_trial_clock.getTime() * 1000
                            # send trigger for response:
                            send_trigger("response_target")
                            # only get first target response, we don't care if they press the button more than once:
                            saw_target = True
    
                        # If esc is pressed, end the experiment:
                        elif key == 'escape':
                            et_abort_exp()  # shut down eyetrigger and download incremental data
                            # close trigger & close experiment
                            # core.wait(time_after_trigger)
                            # parallel.setData(0)
                            core.wait(0.5)
                            core.quit()
    
                ### end trial
                # print("end paced rect trial")
    
                # stop display of current word & send trial offset trigger
                win.callOnFlip(send_trigger, "trial_offset")
    
                # check whether response was hit, miss, false alarm or correct rejection
                # they saw a target and there was one: hit
                if curr_nback_cond != None:
                    if saw_target and curr_target:
                        curr_nback_response = "hit"
                        button_pressed = key
                    # they didn't see a target but there was one: miss
                    elif saw_target == False and curr_target:
                        curr_nback_response = "miss"
                        curr_nback_RT = None
                    # they didn't see a target and there was none: correct rejection
                    elif saw_target == False and curr_target == False:
                        curr_nback_response = "correct rejection"
                        curr_nback_RT = None
                    # they saw a target but there was none: false alarm
                    elif saw_target and curr_target == False:
                        curr_nback_response = "false alarm"
                        button_pressed = key
                # if it wasn't an n-back task block:
                else:
                    curr_target = None
                    curr_nback_response = None
                    curr_nback_RT = None
    
                ### save everything in output csv
                thisExp.addData('colour', curr_col)
                thisExp.addData('global_onset_time', global_onset_time)
                thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
                thisExp.addData('target', curr_target)
                thisExp.addData('button_pressed', button_pressed)
                thisExp.addData('nback_response', curr_nback_response)
                thisExp.addData('nback_RT', curr_nback_RT)  # in ms
                thisExp.addData('duration', curr_duration * 1000)  # in ms
                thisExp.addData('trial_nr', curr_trial_nr)
                thisExp.addData('block_nr_exp', exp_block_counter+1)
                thisExp.addData('run_nr', '2')
                thisExp.addData('block_nr_run', run2_block_counter+1)
                thisExp.addData('block_name', curr_block)
                thisExp.addData('n-back_level', curr_nback_cond)
    
                # start a new row in the csv
                thisExp.nextEntry()
    
                ### IF TESTING MODE ENABLED: end loop after 4 trials
                if expInfo['testing_mode'] == "yes":
                    if trial_idx == 3:
                        break
    
            print("\t\tfinished presenting trials")
    
            # send block offset trigger
            send_trigger("block_offset")
    
            # add 1 to the block counter to go load the next block
            exp_block_counter += 1
            run2_block_counter += 1
            print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
            continueRoutine = False
    
            # If there are still blocks left, go to next one.
            # If not, end loop here:
            if run2_block_counter == 4:
                print(f"Finished block {run2_block_counter}/4 in run 2, moving on to next run!")
                loop_run2_single_nback.finished = True
    # keep track of which components have finished
    single_nbackComponents = []
    for thisComponent in single_nbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "single_nback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in single_nbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "single_nback" ---
    for thisComponent in single_nbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "single_nback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'loop_run2_single_nback'


# --- Prepare to start Routine "run_finished" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from finished_run
#################################################
#                  Finished run                 #
#################################################

# light background
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

if exp_block_counter == 2 or exp_block_counter == 6:

    # reset (local) trigger counter since new run starts from 0
    trigger_count = 0

    run_finished_text = "Diese Runde des Experiments ist nun zu Ende. Bitte bleiben Sie ruhig liegen, es geht gleich weiter."
    # set text
    instr_text = run_finished_text
    # create text box
    instr_text_stim = visual.TextStim(win,
                                      text=instr_text,
                                      height=0.04,
                                      pos=(0, 0),
                                      color="black")

    # display the text on screen until Space is pressed
    while True:
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        instr_text_stim.draw()
        win.flip()
        # end screen if participant presses space
        if 'return' in event.getKeys():
            print("\tMoving on to next run!")
            break
        # If esc is pressed, end the experiment:
        elif 'escape' in event.getKeys():
            et_abort_exp()  # shut down eyetrigger and download incremental data
            # close trigger & close experiment
            core.wait(0.5)
            core.quit()
            break
# keep track of which components have finished
run_finishedComponents = []
for thisComponent in run_finishedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "run_finished" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in run_finishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "run_finished" ---
for thisComponent in run_finishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "run_finished" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_dual_task_blocks = data.TrialHandler(nReps=8.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_dual_task_blocks')
thisExp.addLoop(loop_dual_task_blocks)  # add the loop to the experiment
thisLoop_dual_task_block = loop_dual_task_blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_dual_task_block.rgb)
if thisLoop_dual_task_block != None:
    for paramName in thisLoop_dual_task_block:
        exec('{} = thisLoop_dual_task_block[paramName]'.format(paramName))

for thisLoop_dual_task_block in loop_dual_task_blocks:
    currentLoop = loop_dual_task_blocks
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_dual_task_block.rgb)
    if thisLoop_dual_task_block != None:
        for paramName in thisLoop_dual_task_block:
            exec('{} = thisLoop_dual_task_block[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "dual_task_block" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from blocks_dual_task
    def setup_instructions_and_stimuli(block_config, curr_instr, curr_instr_pic):
        """
        Setup and display instructions and stimuli based on the block configuration.
        """
        RT_per_letter = block_config['RT_per_letter']
        print(f"Start preparing block {block_config['name']}")
        print(f"\tUsing RT_per_letter for this block: {RT_per_letter}")
    
        # set light background
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
    
        # set instruction text
        # instr_text = curr_instr
        # instr_pic = curr_instr_pic
        # create text box
        instr_text_stim = visual.TextStim(win,
                                          text=curr_instr,
                                          height=0.03,  # font height relative to height of screen
                                          pos=(0, 0.2),  # move up a bit
                                          color="black")
    
        # create ImageStim object
        instr_pic = visual.ImageStim(win,
                                     size=(0.85, 0.25),
                                     pos=(0, -0.2),
                                     image=curr_instr_pic)
    
        # show instructions on screen
        if 6 <= exp_block_counter <= 9:
            # instr_text = locals()["instr_" + curr_block]
            # instr_pic = locals()["instr_pic_" + curr_block]
    
            first_trigger_time = log_trigger(curr_instr, curr_instr_pic, trigger_count)
    
            return first_trigger_time
        else:
            win.setColor(light_bg_col, colorSpace='rgb')
            instr_text_stim.draw()
            instr_pic.draw()
            win.flip()
            core.wait(8.75)  # wait for 3s before starting
            # If esc is pressed, end the experiment:
            if 'escape' in event.getKeys():
                et_abort_exp()  # shut down eyetrigger and download incremental data
                # close trigger & close experiment
                core.wait(0.5)
                core.quit()
    
    
    def calculate_durations(text, block_config):
        """
        Calculate word display durations based on the block configuration.
        """
        # compute RTs using participant's average reading speed / letter
        # we define a minimum and a maximum duration for each word
        # the minimum is based on 5 x RT per letter in the respective condition
        # the max duration is based on each condition
        RT_per_letter = block_config['RT_per_letter']
        minimum_duration = 5 * RT_per_letter
    
        if block_config['name'][0] == '1':
            maximum_duration = 2000  # 2 seconds
        elif block_config['name'][0] == '2':
            maximum_duration = 2500  # 2.5 seconds
    
        curr_durations = []
        for i, word in enumerate(curr_text):
            base_duration = RT_per_letter * math.log(len(word)) + 4 * RT_per_letter
            incremented_duration = base_duration + 3 * (i + 1)  # Increment increases with trial number
            if incremented_duration < maximum_duration:
                curr_durations.append(max(incremented_duration, minimum_duration))
            else:
                curr_durations.append(maximum_duration)
    
        return curr_durations
    
    
    def process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                      curr_instr_pic):
        """
        Process each block based on its configuration.
        """
        first_trigger_time, trigger_count = setup_instructions_and_stimuli(block_config, curr_instr, curr_instr_pic)
        curr_durations = calculate_durations(curr_text, block_config)
    
        ### change background colour
        win.setColor(dark_bg_col, colorSpace='rgb')
        win.flip()
    
        # show main block questions
        skip_questions_paced = False
    
        # get n-back condition:
        curr_nback_cond = curr_block[0]  # get first character of block name
    
        # if it is a 1 or a 2, set that as current n-back level:
        if curr_nback_cond in ['1', '2']:
            curr_nback_cond == int(curr_nback_cond)
        # if it's neither 1 nor 2, it has to be a block without n-back,
        # so set curr_nback_cond to None
        else:
            curr_nback_cond = None
    
        print(f"\tCurrent n-back condition: {curr_nback_cond}")
        print(f"\tCurrent text: {curr_text_nr}")
    
        # create empty text stimulus
        stim = visual.TextStim(win=win,
                               text=" ",
                               pos=(0, 0),  # center stimulus
                               font="Times New Roman",
                               height=0.07)
    
        stim.draw()
        win.flip()
    
        # clear buffer of all previously recorded key events:
        event.clearEvents()
        defaultKeyboard.clearEvents()
    
        # CREATE CLOCKS:
        my_block_clock = core.Clock()
        my_block_clock.reset()  # start block clock
        start_time = my_block_clock.getTime()  # get start time of block
        # also create trial clock
        my_trial_clock = core.Clock()
    
        # send block onset trigger
        send_trigger(curr_block + "_onset")
    
        # loop words in current text
        for trial_idx, curr_word in enumerate(curr_text):
            # print("current idx: " + str(trial_idx) + ", curr word:" + curr_word)
    
            ### prepare & show current word:
    
            # get current colour
            curr_colour = curr_colours[trial_idx]
    
            # if it's a block with an n-back task, prepare target list as well
            if curr_nback_cond != None:
                curr_target = curr_targets[trial_idx]
                saw_target = False
    
            # get duration for current word
            curr_duration = curr_durations[trial_idx] / 1000  # convert ms to seconds
            # print("duration for current word (in s):", curr_duration)
    
            # get trial number (start counting from 1, so add 1)
            curr_trial_nr = trial_idx + 1
    
            # set current word & colour as content of text stimulus
            stim.color = curr_colour
            stim.text = curr_word
    
            # show word on screen
            stim.draw()  # draw word on screen
            # update the window to clear the screen and display
            # the stimulus, send trigger on flip
            win.callOnFlip(send_trigger, "trial_onset")
    
            # start trial clock & record trial onset time
            my_trial_clock.reset()
            global_onset_time = globalClock.getTime()
            onset_time_rel2trigger = global_onset_time - first_trigger_time
    
            ### wait for key response:
            # In blocks with n-back task, participants can press "c" to indicate they saw a target colour.
    
            ### start recording responses
            # start while loop that looks for responses
            # --> end while loop only if duration for current word is over
            while my_trial_clock.getTime() < (onset_time + curr_duration):
    
                stim.draw()
                win.flip()
    
                # check for key responses:
                keys = event.getKeys(['1', 'escape'])
                button_pressed = "NA"
    
                # if there were, check responses:
                for key in keys:
    
                    # if participant pressed button "1" for the first time and it's an n-back condition
                    # where they're actually supposed to do that (aka not a reading baseline condition)...
                    if key == '1' and curr_nback_cond != None and saw_target == False:
                        # get reaction time
                        curr_nback_RT = my_trial_clock.getTime() * 1000
                        # send trigger for response:
                        send_trigger("response_target")
                        # only get first target response, we don't care if they press the button more than once:
                        saw_target = True
    
                    # If esc is pressed, end the experiment:
                    elif key == 'escape':
                        et_abort_exp()  # shut down eyetrigger and download incremental data
                        # close trigger & close experiment
                        # core.wait(time_after_trigger)
                        # parallel.setData(0)
                        core.wait(0.5)
                        core.quit()
    
            ### end trial
            # print("\tend paced trial")
            # stop display of current word & send trial offset trigger
            win.callOnFlip(send_trigger, "trial_offset")
    
            # check whether response was hit, miss, false alarm or correct rejection
            # they saw a target and there was one: hit
            if curr_nback_cond != None:
                if saw_target and curr_target:
                    curr_nback_response = "hit"
                    button_pressed = key
                # they didn't see a target but there was one: miss
                elif saw_target == False and curr_target:
                    curr_nback_response = "miss"
                    curr_nback_RT = None
                # they didn't see a target and there was none: correct rejection
                elif saw_target == False and curr_target == False:
                    curr_nback_response = "correct rejection"
                    curr_nback_RT = None
                # they saw a target but there was none: false alarm
                elif saw_target and curr_target == False:
                    curr_nback_response = "false alarm"
                    button_pressed = key
            # if it wasn't an n-back task block:
            else:
                curr_target = None
                curr_nback_response = None
                curr_nback_RT = None
    
            ### save everything in output csv
            thisExp.addData('colour', curr_colour)
            thisExp.addData('global_onset_time', global_onset_time)
            thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
            thisExp.addData('target', curr_target)
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('nback_response', curr_nback_response)
            thisExp.addData('nback_RT', curr_nback_RT)  # in ms
            thisExp.addData('duration', curr_duration * 1000)  # in ms
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('trial_nr', curr_trial_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('run_nr', run_nr)
            thisExp.addData('block_nr_run', block_nr_run)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
            # careful, make sure quotes in the strings are escaped using a
            # quote (weird, I know) so it's properly saved in the CSV:
            thisExp.addData('word', escape_quotes(curr_word))
    
            # start a new row in the csv
            thisExp.nextEntry()
    
            ### IF TESTING MODE ENABLED: end loop after 4 trials
            if expInfo['testing_mode'] == "yes":
                if trial_idx == 9:
                    break
    
        print("finished presenting trials")
    
        # send block offset trigger
        send_trigger("block_offset")
    
    # Block configurations
    block_configs = {
        "1back_dual_main_no_click": {
            "name": "1back_dual_main_no_click",
            "RT_per_letter": int(expInfo['RT_per_letter_oneback_dual']),
            # Add other block-specific configurations or parameters here
        },
        "2back_dual_main_no_click": {
            "name": "2back_dual_main_no_click",
            "RT_per_letter": int(expInfo['RT_per_letter_twoback_dual']),
            # Add other block-specific configurations or parameters here
        }
    }
    
    if exp_block_counter == 6:
        run_nr = 3
        block_nr_run = run3_block_counter + 1
        curr_block = run3_blocks
        curr_targets = run3_target_lists
        curr_colours = run3_colour_lists
        block_config = block_configs.get(curr_block)
    
        if block_config:
            curr_text_nr = all_texts_nrs_list[exp_block_counter]
            curr_text = locals()[curr_text_nr]  # Assuming this retrieves the text for the current block
            curr_instr = locals()["instr_" + block_config['name']]
            curr_instr_pic = locals()["instr_pic_" + block_config['name']]  # set path to image here
    
            # show main block questions
            skip_questions_paced = False
            process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                          curr_instr_pic)
            # continueRoutine = False
        else:
            print("Error: Block configuration not found.")
    
    elif exp_block_counter == 7:
        run_nr = 4
        block_nr_run = run4_block_counter + 1
        curr_block = run4_blocks
        curr_targets = run4_target_lists
        curr_colours = run4_colour_lists
        block_config = block_configs.get(curr_block)
    
        if block_config:
            curr_text_nr = all_texts_nrs_list[exp_block_counter]
            curr_text = locals()[curr_text_nr]  # Assuming this retrieves the text for the current block
            curr_instr = locals()["instr_" + block_config['name']]
            curr_instr_pic = locals()["instr_pic_" + block_config['name']]  # set path to image here
    
            skip_questions_paced = False
            process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                          curr_instr_pic)
            # continueRoutine = False
        else:
            print("Error: Block configuration not found.")
    
    elif exp_block_counter == 8:
        run_nr = 5
        block_nr_run = run5_block_counter + 1
        curr_block = run5_blocks
        curr_targets = run5_target_lists
        curr_colours = run5_colour_lists
        block_config = block_configs.get(curr_block)
    
        if block_config:
            curr_text_nr = all_texts_nrs_list[exp_block_counter]
            curr_text = locals()[curr_text_nr]  # Assuming this retrieves the text for the current block
            curr_instr = locals()["instr_" + block_config['name']]
            curr_instr_pic = locals()["instr_pic_" + block_config['name']]  # set path to image here
    
            skip_questions_paced = False
            process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                          curr_instr_pic)
            # continueRoutine = False
        else:
            print("Error: Block configuration not found.")
    
    elif exp_block_counter == 9:
        run_nr = 6
        block_nr_run = run6_block_counter + 1
        curr_block = run6_blocks
        curr_targets = run6_target_lists
        curr_colours = run6_colour_lists
        block_config = block_configs.get(curr_block)
    
        if block_config:
            curr_text_nr = all_texts_nrs_list[exp_block_counter]
            curr_text = locals()[curr_text_nr]  # Assuming this retrieves the text for the current block
            curr_instr = locals()["instr_" + block_config['name']]
            curr_instr_pic = locals()["instr_pic_" + block_config['name']]  # set path to image here
    
            skip_questions_paced = False
            process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                          curr_instr_pic)
            # continueRoutine = False
        else:
            print("Error: Block configuration not found.")
    # Run 'Begin Routine' code from questions_dual_task
    ##########################################################
    #              Text Comprehension Questions              #
    ##########################################################
    
    def setup_question(question_text, answers_text):
        question = visual.TextStim(win, text=question_text, pos=(0, 0.2), color="black", height=0.03, anchorHoriz='center', alignText='center', wrapWidth=1)
        answers = [visual.TextStim(win, text=ans, pos=(0, 0.1 - i * 0.08), color="black", height=0.03, wrapWidth=1, anchorHoriz='center', alignText='center') for i, ans in enumerate(answers_text)]
        return question, answers
    
    from psychopy import visual, core, event
    from psychopy.hardware import keyboard
    
    def display_question_and_get_response(question, answers, correct_answer):
        defaultKeyboard.clearEvents()
        
        # Set-up time to write into logfile
        question_time = globalClock.getTime()
        onset_time_rel2trigger = question_time - first_trigger_time
    
        question.autoDraw = True
        for answer in answers:
            answer.autoDraw = True
        instr_text.autoDraw = True
    
        countdown_timer = visual.TextStim(win, text='', pos=(0, -0.25), color="grey", height=0.02, anchorHoriz='center', alignText='center', wrapWidth=1)
    
        # defaultKeyboard = keyboard.Keyboard()
        chosen_ans = "NA"
        is_correct = "NA"
        button_pressed = "NA"
        response_received = False
    
        # Start a clock to track response time
        response_clock = core.Clock()
    
        # Countdown from 10 seconds
        while response_clock.getTime() < 10:
            remaining_time = 10 - int(response_clock.getTime())
            countdown_timer.text = f"Zeit: {remaining_time}"
            countdown_timer.draw()
            win.flip()
    
            keys = defaultKeyboard.getKeys(['1', '2', '3', '4'], waitRelease=False)
            if keys:
                key_name = keys[0].name  # Get the name of the first key pressed
                button_pressed = key_name
    
                # Now, use the key_name to determine the action
                if key_name == '1':
                    index = 0  # Corresponds to the first choice
                elif key_name == '2':
                    index = 1  # Corresponds to the second choice
                elif key_name == '3':
                    index = 2  # Corresponds to the third choice
                elif key_name == '4':
                    index = 3  # Corresponds to the fourth choice
                else:
                    index = None  # Just in case, not really needed if you're sure about the input keys
    
                # Proceed with your logic based on the index
                if index is not None:
                    chosen_ans = chr(97 + index)  # Convert index to letter ('a', 'b', 'c', 'd')
                    is_correct = chosen_ans == correct_answer  # Assuming correct_answer is defined ('a', 'b', 'c', or 'd')
                    for i, answer in enumerate(answers):
                        answer.setColor("green" if i == index else "black")
                    win.flip()
                    core.wait(0.5)  # Ensure the color change is visible
                    response_received = True
                    break
    
        # Hide the countdown timer after it finishes
        countdown_timer.text = ''
        countdown_timer.draw()
        win.flip()
    
        # If no response is received within 10 seconds, return "NA"
        if not response_received:
            chosen_ans = "NA"
            is_correct = "NA"
            button_pressed = "NA"
    
        return question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed
    
    def reset_answers(answers):
        for answer in answers:
            answer.setColor("black")
        question.autoDraw = False
        instr_text.autoDraw = False
        for answer in answers:
            answer.autoDraw = False
    
    # Set up instructions
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    instr_text = visual.TextStim(win, text="(Bitte benutzen Sie die Tasten 1, 2, 3 und 4, um die richtige Antwort auszuwählen.)", color="grey", pos=(0, -0.3), wrapWidth=2, height=0.018)
    event.clearEvents()
    
    # Assuming skip_questions_paced and other variables are defined
    if not skip_questions_paced:
        # Setup for Q1
        Q1_text = locals()[curr_text_nr + "_Q1"]
        Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
        Q1_correct = locals()[curr_text_nr + "_Q1_corr"]
    
        question, answers = setup_question(Q1_text, Q1_answers)
        question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q1_correct)
        print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)
    
        # save data:
        thisExp.addData('global_onset_time', question_time)
        thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
        thisExp.addData('question', 'Q1')
        thisExp.addData('button_pressed', button_pressed)
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q1_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter+1)
        thisExp.addData('run_nr', '1')
        thisExp.addData('block_nr_run', run1_block_counter+1)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)
    
        # start a new row in the csv
        thisExp.nextEntry()
    
        # Setup for Q2
        Q2_text = locals()[curr_text_nr + "_Q2"]
        Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
        Q2_correct = locals()[curr_text_nr + "_Q2_corr"]
    
        question, answers = setup_question(Q2_text, Q2_answers)
        question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q2_correct)
        print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)
    
        # save data:
        thisExp.addData('global_onset_time', question_time)
        thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
        thisExp.addData('question', 'Q2')
        thisExp.addData('button_pressed', button_pressed)
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q2_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter+1)
        thisExp.addData('run_nr', "1")
        thisExp.addData('block_nr_run', run1_block_counter+1)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)
    
        # start a new row in the csv
        thisExp.nextEntry()
    
        # Setup for Q3
        Q3_text = locals()[curr_text_nr + "_Q3"]
        Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
        Q3_correct = locals()[curr_text_nr + "_Q3_corr"]
    
        question, answers = setup_question(Q3_text, Q3_answers)
        question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q3_correct)
        print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)
    
        # save data:
        thisExp.addData('global_onset_time', question_time)
        thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
        thisExp.addData('question', 'Q3')
        thisExp.addData('button_pressed', button_pressed)
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q3_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter+1)
        thisExp.addData('run_nr', "1")
        thisExp.addData('block_nr_run', run1_block_counter+1)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)
        
        # start a new row in the csv
        thisExp.nextEntry()
    
        exp_block_counter += 1
        # run3_block_counter += 1
        print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
        continueRoutine = False
    
        print(f"Finished this dual task run, moving on to next run!")
        # loop_dual_task_blocks.finished = True
    
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
    
        # Show run finished screen in between runs
        if 6 <= exp_block_counter <= 9:
            run_finished_text = "Diese Runde des Experiments ist nun zu Ende. Bitte bleiben Sie ruhig liegen, es geht gleich weiter."
            # set text
            instr_text = run_finished_text
            # create text box
            instr_text_stim = visual.TextStim(win,
                                              text=instr_text,
                                              height=0.05,
                                              pos=(0, 0),
                                              color="black")
    
            # display the text on screen until Return is pressed
            while True:
                # keep background ivory
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim.draw()
                win.flip()
                # end screen if participant presses space
                if 'return' in event.getKeys():
                    print("moving on to next run!")
                    break
                # If esc is pressed, end the experiment:
                elif 'escape' in event.getKeys():
                    et_abort_exp()  # shut down eyetrigger and download incremental data
                    # close trigger & close experiment
                    core.wait(0.5)
                    core.quit()
                    break
    
        # If there are still blocks left, go to next one.
        # If not, end loop here:
        elif exp_block_counter == 10:
            print(f"Finished run 4, finishing experiment!")
            loop_dual_task_blocks.finished = True
    # keep track of which components have finished
    dual_task_blockComponents = []
    for thisComponent in dual_task_blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "dual_task_block" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dual_task_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "dual_task_block" ---
    for thisComponent in dual_task_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "dual_task_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'loop_dual_task_blocks'


# --- Prepare to start Routine "end" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from end_2
### END OF EXPERIMENT:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

### Show message
# set text
instr_text = "Hervorragend!\n\n\nVielen Dank,\ndas Experiment ist nun zu Ende!"

# create text box
instr_text_stim = visual.TextStim(win,
                                  text = instr_text,
                                  height = 0.05,
                                  pos = (0, 0),
                                  color = "black")

# display the text on screen until Space is pressed
while True:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    instr_text_stim.draw()
    win.flip()
    # end screen if participant presses space
    if 'return' in event.getKeys():
        et_abort_exp()  # shut down eyetrigger and download incremental data
        core.wait(0.5)
        # send trigger
        send_trigger("end_experiment")
        print("ending experiment now!")
        # end experiment
        break
# keep track of which components have finished
endComponents = []
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='comma')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
