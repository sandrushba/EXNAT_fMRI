#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on September 04, 2023, at 14:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'EXNAT-2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'age': '', 'handedness': 'r', 'gender': 'w', 'testing_mode': 'yes', 'meas_hearing': 'no', 'test_triggers': 'no'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\AC\\Desktop\\Merle\\EXNAT-2 Win7 Experiment EYELINK TIMING IMPROVED\uf025\\selfpaced_reading_nback_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "settings"
settingsClock = core.Clock()
# set screen resolution for eyetracker here:
SCN_W, SCN_H = (1280, 800)

### import packages:

# for setting the output encoding to UTF-8
import sys
# --> if you don't do this, German "Umlaute" can't be displayed correctly:
sys.stdout = open(sys.stdout.fileno(), mode = 'w', encoding = 'utf8', buffering = 1)
# print Python environment psychopy is currently using
print(sys.executable)

# for showing pictures
from psychopy import visual

# for playing sounds:
import psychtoolbox as ptb
from psychopy import prefs
prefs.hardware['audioLib'] = ['ptb'] # set 'ptb', 'pyo' or'pygame' as sound library here

# I use ptb here as a sound library because PTB is built to bring a number of advantages in 
# terms of latency.
# PsychoPy docs on PTB's advantages: "With the most aggressive low-latency settings you 
# can get a sound to play in “immediate” mode with typically in the region of 5ms lag and 
# maybe 1ms precision. That’s pretty good compared to the other options that have a lag of 
# 20ms upwards and several ms variability. BUT, on top of that, PTB allows you to preschedule 
# your sound to occur at a particular point in time (e.g. when the trigger is due to be 
# sent or when the screen is due to flip) and the PTB engine will then prepare all the buffers 
# ready to go and will also account for the known latencies in the card. With this method the 
# PTB engine is capable of sub-ms precision and even sub-ms lag!" 
# --> sounds good to me
# Psychopy uses "aggressive exclusive mode" as a default for the Latency Mode in PTB. 
# This means your study will take control of the audio device you’re using and prioritise our use 
# of the sound card over all others (e.g. other sound-playing apps like Spotify). 
# This makes the latencies as low as possible.
from psychopy import sound
from psychopy.sound import Sound
print(Sound) # should look roughly like this: <class 'psychopy.sound.SoundPtb'>
import soundfile as sf

import os

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

# Get functions from my custom scripts:
# import all texts
from EXNAT2_texts_MC_Qs import *
# import some additional functions I wrote for the experiment:
from EXNAT2_study_components import change_bg_colour
from nback_colour_generator import create_nback_stimlist, draw_without_replacement, get_targets, create_0back_stimlist

# load CSVs with tone sequences for prediction tendency task:
ordered_path = "Prediction Tendency Task/df_ordered_seqs.csv"
random_path = "Prediction Tendency Task/df_random_seqs.csv"
df_ordered_tone_seqs = pd.read_csv(ordered_path)
df_random_tone_seqs = pd.read_csv(random_path)
print("loaded CSVs with stimulus lists for prediction tendency task")

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


### Setup LSL Stream
#print("create trigger stream") 
# Create trigger stream:
#global out_marker
#info_marker_stream = StreamInfo('PsychoPyMarkers', 'Marker', 1, 0, 'string')
#out_marker = StreamOutlet(info_marker_stream)
#out_marker.push_sample(["TEST MARKER"])


# make mouse invisible during experiment
#mouse = io.devices.mouse
win.setMouseVisible(False)

# create 10 ms timer that we can use instead of core.wait()
my_timer = core.CountdownTimer(0.01)
### Stimulus settings

# measure frame rate (in Hz)
frame_rate = win.getActualFrameRate() # frame rate in Hz
print("measured frame rate:", frame_rate, "Hz")
# set flicker frequency (in Hz)
flicker_freq = frame_rate/4 # 60/4 = 15 Hz

# set colours you want to use for background:
#light_bg_col_hex = "#FDFBF0" # ivory instructions background
#dark_bg_col_hex  = "#505050" # dark grey background for stimuli
light_bg_col = [(x / 127.5) - 1 for x in (253, 251, 240)] # ivory instructions background (use RGB -1:1)
dark_bg_col  = [(x / 127.5) - 1 for x in (80, 80, 80)] # dark grey background for stimuli (use RGB -1:1)

# for timing test:
#dark_bg_col = [(x / 127.5) - 1 for x in (255, 255, 255)]

# make background light for a start - use rgb -1:1 colour codes
win.setColor(light_bg_col, colorSpace='rgb')

# set colours you want to use for the stimuli:
colours = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"]
print("Preparing experiment with n-back colours:", colours)
# for timing test:
#colours = ["#000000", "#F989A2", "#2AB7EF", "#88BA3F"]

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
all_main_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04", "text_05", "text_06", "text_07", "text_08", "text_09", "text_10"]
# shuffle text numbers
random.shuffle(all_main_texts_nrs_list)

# only get first 9 texts for the main blocks, the last one will be used for the vis task:
vis_task_text_nr = all_main_texts_nrs_list[-1]
all_main_texts_nrs_list = all_main_texts_nrs_list[0:-1]

# append "empty" text numbers to the list where we have blocks that are not main blocks.
all_texts_nrs_list = []
for t_idx, t in enumerate(all_main_texts_nrs_list):
    # if it's the first text, it's the reading BL main block.
    # Append 1 empty text number before text (for the reading BL training) 
    # and 4 after text (for click training, 2x single task training & 1x single task main)
    if t_idx == 0: 
        all_texts_nrs_list = all_texts_nrs_list + ["", t, "", "", "", ""]
    # the second text is the first n-back block. 
    # There are 3 "empty" blocks after it (2x single task training & 1x single task main)
    elif t_idx == 1: 
        all_texts_nrs_list = all_texts_nrs_list + [t, "", "", ""]
    # all following texts are main blocks and can be appended to all_texts_nrs_list
    elif t_idx > 1:
        all_texts_nrs_list.append(t)
        
print(all_texts_nrs_list)

### Set order of blocks 
print("set block order") 
# The first blocks should be:
# - reading baseline + training
# - click training
# - in random order: 1-back (2x single task training & 1x main & 1x dual task main) & 2-back (2x single task training & 1x main & 1x dual task main)
# - in random order: 2x reading BL main, 2x 1-back main, 2x 2-back main

# this always comes first in the experiment
Reading_BL = ["Reading_Baseline_training", "Reading_Baseline_main", "click_training"]

# then you get both n-back conditions with trainings (which of them is first is randomized)
oneback = ["1back_single_training1", "1back_single_training2", "1back_single_main", "1back_dual_main"]
twoback = ["2back_single_training1", "2back_single_training2", "2back_single_main", "2back_dual_main"]

# shuffle the order of the 2 lists
main_blocks1 = [oneback, twoback]
random.shuffle(main_blocks1)

# flatten nested list
main_blocks1 = flatten_list(main_blocks1)

# now shuffle order of the last 6 main blocks:
main_blocks2 = ["Reading_Baseline_main", "Reading_Baseline_main", "1back_dual_main", 
                "1back_dual_main", "2back_dual_main", "2back_dual_main"]
random.shuffle(main_blocks2)

# put them all together:
#global all_blocks 
all_blocks = Reading_BL + main_blocks1 + main_blocks2
print(all_blocks)
### Create n-back colour lists for all blocks

print("create n-back colour lists")
# The reading bl training text has 159 trials.

# The click training has 6 trials. 

# Then we also have 4 short training blocks à 20 trials each (5 targets)
# 4 * single training

# We have 2 single-task main blocks, 
# one for 1-back and 1 for 2-back à 60 trials each (10 targets):
# 2 * single main

# There are 9 dual-task main blocks à 300 stimuli each (50 targets)
# reading bl * 3
# 1-back * 3
# 2-back * 3

# --> all in all, 15 blocks

# So for every block, build a list with colour codes containing the right amount of targets.
# The function is defined in another script bc it's super long, 
# I import it at the beginning of this script.

# First, create list with length of all texts. The length of the blocks is 
# always in the same order, only the conditions change.
blocks_textlen = [159, 300, 6, # reading bl blocks + click training
                  20, 20, 60, 300, 20, 20, 60, 300, # main blocks 1 + trainings & single tasks
                  300, 300, 300, 300, 300, 300] # main blocks 2        
blocks_target_counts = [25, 50, 1, # reading bl blocks + click training
                        5, 5, 10, 50, 5, 5, 10, 50, # main blocks 1 + trainings & single tasks
                        50, 50, 50, 50, 50, 50]
# Now loop this list. Check which condition we have there and the create colour list for each text.
all_colour_lists = []
all_target_lists = []
for block_idx, block_length in enumerate(blocks_textlen):
    # get 1st letter of block name - that tells us the condition
    block_cond = all_blocks[block_idx][0]

    # for each condition, decide which n-back level we want to assign
    # For all no-n-back blocks, we use 1 (just for the colour list generation)
    #global curr_nback_level
    if block_cond == "R":
        curr_nback_level = 1
    elif block_cond == "c":
        curr_nback_level = 1
    elif block_cond == "1":
        curr_nback_level = 1
    else: curr_nback_level = 2

    # generate colour list for current block  
    #global curr_colours
    curr_colours = create_nback_stimlist(nback_level = curr_nback_level, 
                                         colour_codes = colours, 
                                         story = ["x"] * block_length, 
                                         target_abs_min = blocks_target_counts[block_idx], 
                                         target_abs_max = blocks_target_counts[block_idx], 
                                         zeroback_target = None)

    # get list of targets / non-targets
    curr_targets = get_targets(stim_list = curr_colours, 
                               nback_level = curr_nback_level)

    # add to bigger lists
    all_colour_lists.append(curr_colours)
    all_target_lists.append(curr_targets)

print("------ finished preparing stimuli! ------")


# ------------------------------------------

# init block counter for the whole experiment
exp_block_counter = 0

print("starting experiment now!")
empty_placeholder = visual.TextStim(win=win, name='empty_placeholder',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "eyetr_calibr"
eyetr_calibrClock = core.Clock()

# Initialize components for Routine "triggers"
triggersClock = core.Clock()

# Initialize components for Routine "sounds"
soundsClock = core.Clock()

# Initialize components for Routine "no_text_blocks"
no_text_blocksClock = core.Clock()

# Initialize components for Routine "text_blocks"
text_blocksClock = core.Clock()

# Initialize components for Routine "Q1"
Q1Clock = core.Clock()

# Initialize components for Routine "Q2"
Q2Clock = core.Clock()

# Initialize components for Routine "Q3"
Q3Clock = core.Clock()

# Initialize components for Routine "difficulty"
difficultyClock = core.Clock()

# Initialize components for Routine "warning"
warningClock = core.Clock()

# Initialize components for Routine "warning_1"
warning_1Clock = core.Clock()

# Initialize components for Routine "vistask_t"
vistask_tClock = core.Clock()

# Initialize components for Routine "vistask_m"
vistask_mClock = core.Clock()

# Initialize components for Routine "warning_1"
warning_1Clock = core.Clock()

# Initialize components for Routine "pred_tendency"
pred_tendencyClock = core.Clock()

# Initialize components for Routine "end"
endClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "settings"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
### Set up connection to EyeLink Eyetracker

# for connecting to Eyelink:
import pylink
import platform # ?
from PIL import Image # for host backdrop image
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy # ?
from string import ascii_letters, digits # ?

# set up EDF data file:
edf_name = expInfo['participant'] # make sure file name (without .edf) is <= 8 characters
if len(edf_name) >4:
    print("edf file name is too long - choose shorter participant code!")
# eyetracking data should be saved in folder "eyetracking_data", 
# located in the same folder as this script

# We download the EDF file with the data from the Eyelink Host PC (aka the Eyetracking PC) 
# at the end of this experiment and put it into this folder.


### Connect to the Eyelink Host PC

eyelink_IP = "100.1.1.1" # set IP address of host PC here
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
#vstr = el_tracker.getTrackerVersionString()
#eyelink_ver = int(vstr.split()[-1].split('.')[0]
# print version info:
#print("running experiment on %s, version %d" % (vstr, eyelink_ver))


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
el_tracker.sendCommand("calibration_type = HV9") # use 9 target dots for calibration/validation screen
# Set a gamepad button to accept calibration/drift check target
# You need a supported gamepad/button box that's connected to the Host PC
el_tracker.sendCommand("button_function 5 'accept_target_fixation'") # I think that's enter on our keyboard?

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


### -------------------- OLD:  --------------------  

### Drift check function:
# We need to correct for small changes or shifts that might occur
# in the eye tracking system's calibration over time. Those drifts can be caused 
# by slight movements of the eye tracking hardware or changes in the 
# environment that influence the hardware (e.g. temperature changes).
# Long story short, we have to correct for those drifts from time to time.

#def do_drift_check(): 
#    
#    # get connection to tracker
#    el_tracker = pylink.getEYELINK()
#    
#    # terminate the task if connection to tracker is lost/can't be found:
#    if not el_tracker.isConnected():
#        print("lost connection to Eyetracker, terminating experiment now!")
#        # quit PsychoPy 
#        core.quit()
#        sys.exit()
#
#    # if the connection can be found, try running drift correction:
#    try: 
#        el_tracker.doDriftCorrect(int(scn_width/2.0),
#                                  int(scn_height/2.0), 
#                                  1, 1)
#    except: pass # do nothing if drift correction didn't work

# keep track of which components have finished
settingsComponents = [empty_placeholder]
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
settingsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "settings"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = settingsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=settingsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *empty_placeholder* updates
    if empty_placeholder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        empty_placeholder.frameNStart = frameN  # exact frame index
        empty_placeholder.tStart = t  # local t and not account for scr refresh
        empty_placeholder.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(empty_placeholder, 'tStartRefresh')  # time at next scr refresh
        empty_placeholder.setAutoDraw(True)
    if empty_placeholder.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > empty_placeholder.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            empty_placeholder.tStop = t  # not accounting for scr refresh
            empty_placeholder.frameNStop = frameN  # exact frame index
            win.timeOnFlip(empty_placeholder, 'tStopRefresh')  # time at next scr refresh
            empty_placeholder.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in settingsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "settings"-------
for thisComponent in settingsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('empty_placeholder.started', empty_placeholder.tStartRefresh)
thisExp.addData('empty_placeholder.stopped', empty_placeholder.tStopRefresh)

# ------Prepare to start Routine "eyetr_calibr"-------
continueRoutine = True
# update component parameters for each repeat
### Calibration/Validation Setup

# show instruction for starting Calibration / Validation:
instr_calibr = visual.TextStim(win = win, text = "Eyetracker-Kalibrierung. Zum Starten bitte die Leertaste und dann Enter drücken!", pos = (0,0), color = "black", height = 0.5, wrapWidth = 1600)
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

# Beeps to play during calibration, validation and drift correction:
# parameters: target, good, error
#             target: sound to play when target moves
#             good: sound to play on successful operation
#             bad: sound to play on failure or interruption
# You can use "" for default sounds, "off" for no sounds, or a wav file for custom sounds.
# --> we use the default sounds:
genv.setCalibrationSounds("off", "off", "off")

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
eyetr_calibrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "eyetr_calibr"-------
while continueRoutine:
    # get current time
    t = eyetr_calibrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=eyetr_calibrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eyetr_calibrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "eyetr_calibr"-------
for thisComponent in eyetr_calibrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "eyetr_calibr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "triggers"-------
continueRoutine = True
# update component parameters for each repeat
### Prepare triggers

# pylsl for pushing triggers to lsl stream:
#from pylsl import StreamInlet, resolve_stream, StreamOutlet, StreamInfo

# for sending triggers the oldschool way by using serial ports:
from psychopy import parallel
#port = parallel.ParallelPort() # create port object
#port.setPortAddress(0xB010) # set address of port
port = parallel.setPortAddress(0xB010)# set address of port

time_after_trigger = 0.003 # wait for 3ms after a trigger before clearing the line with the 0 trigger

### List of Trigger Values
trigger_map = {
    'block_onset': 2,
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
    'ordered_onset': 56,
    'random_onset': 58,
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
    
    # send trigger to EEG:
    parallel.setData(trigger_value)
    #core.wait(0.01) # you need a break between the triggers: wait for 10 ms
    # turn off trigger
    #parallel.setData(0) 
    # I do this after each trigger "manually" because I don't want 
    # to wait for 10 ms while nothing is happening.
    
    # send trigger to Eyetracker:
    el_tracker.sendMessage(event_name)

# send test triggers to parallel port to check if they all work
for i in [num for num in range(2, 69) if num % 2 == 0]:
    # send trigger:
    parallel.setData(i)
    core.wait(time_after_trigger) # you need a break between the triggers: wait for a few ms
    # turn off trigger
    parallel.setData(0)
    
    # send trigger as string to Eyetracker:
    el_tracker.sendMessage(str(i))
    

core.wait(1) # wait 1 s

send_trigger(event_name = 'start_experiment')

# This is just for checking if the triggers we send 
# are in the correct spot in the data 
# (we can only check this roughly, but if there's a 
# trigger and we don't see any neural or pupil response #
# afterwards, there's definitely something off)

# Send 50 light flashes with 3 s in between


if expInfo["test_triggers"] == "yes": # check if we're in testing mode
    # turn bg dark:
    win.setColor(dark_bg_col, colorSpace='rgb')
    win.flip()
    
    # create empty stimulus 
    stim = visual.Rect(win = win,
                 width = 6, # width = 6 * 6° visual angle
                 height = 6, # height = 6° visual angle
                 # colorSpace = "hex",
                 pos = (0,0)) # center stimulus 
    stim.fillColor = "#FFFFFF" # make stimulus white
    
    my_trial_clock = core.Clock() # create trial clock
    
    for test_trial in range(1, 51): 
        print("sound & light flash test - trial", test_trial, "/ 50")
        
        stim.draw()
        win.flip()
        my_trial_clock.reset() # start trial clock
        
        # send EEG trigger:
        parallel.setData(68)

        # send Eyetracker trigger:
        el_tracker.sendMessage(str("test_trigger"))
        
        # turn off EEG trigger
        core.wait(0.01)
        parallel.setData(0)
        
        while my_trial_clock.getTime() < 0.1:
            stim.draw()
            win.flip()
        
        win.flip() # clear screen 
        core.wait(3) # wait for 3 s before starting next trial
        
    # turn bg colour light again
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    
continueRoutine = False # end routine
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
triggersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "triggers"-------
while continueRoutine:
    # get current time
    t = triggersClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=triggersClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "triggers"-------
for thisComponent in triggersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "triggers" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sounds"-------
continueRoutine = True
# update component parameters for each repeat
### Setup for playing sounds
#--> we need this for the prediction tendency task!
from sounds_custom import Sound
import sounddevice as sd 
sound_device = 34
import soundfile as sf

# settings for the sounds:
tone_volume = 1 # use full volume and make sure the system volume is
               # set to a value where the tones are played with 40dB
tones = [440, 587, 782, 1043]  # Pure tone frequencies in Hz
tone_duration = 0.1  # Duration of each pure tone in seconds (each lasted 100 ms)
tone_rate = 3  # Rate of pure tone presentation in Hz
audio_sample_freq = 44100 # 44100 Hz --> audio sampling rate at the lab (according to Frauke)
tones_iti = 1/3
tone_fade = 5e-3

sound_device = "Analog (7+8) (RME Fireface UC), Windows DirectSound" # 7+8 are the output channels

### HEARING THRESHOLD TEST

# We want to play the sounds with a volume of 40 dB above hearing threshold.

#import os
#import sounds_custom # sounds3 module from Sarah's cuecue study T2
#import sounddevice as sd
#print(sd.query_devices()) # print all sound devices we can access to check which one you need


if expInfo["meas_hearing"] == "yes":
    
    # prepare instructions
    instr_hearthres = visual.TextStim(win=win, text = "Messung der Hörschwelle. Zum Starten bitte die Leertaste drücken!", pos = (0,0), color = "black", height = 0.5, wrapWidth = 1600)

    message1 = visual.TextStim(win=win, text = "Laut nach leise.\n\nDrücken Sie bitte die Leertaste, wenn nichts mehr zu hören ist.", pos = (0,0), color = "black", height = 0.5, wrapWidth = 1600)
    message2 = visual.TextStim(win=win, text = "Leise nach laut.\n\nDrücken Sie bitte die Leertaste, sobald etwas zu hören ist.", pos = (0,0), color = "black", height = 0.5, wrapWidth = 1600)
    pause = visual.TextStim(win=win, text = "Kurze Pause!", pos = (0,0), color = "black", height = 0.5, wrapWidth = 1600)
    
    # create a sound file for the hearing threshold test
    curr_freq = 1043 # Hz - I use the highest frequency from the prediction tendency task here 
    
    # build a time array: you need the sound duration and the right sampling frequency for your device
    # 1 divided by the sampling rate = duration of a single sample in sec
    tone_sample_len = 1/audio_sample_freq
    
    # calculate the number of samples required for a 100 ms duration
    num_samples = int(audio_sample_freq * tone_duration)

    # build a time array
    t = np.arange(0, num_samples) / audio_sample_freq  # Adjust the time array
    
    # generate sine wave:
    sine_wave = np.sin(2 * np.pi * curr_freq * t)

    # apply cosine ramp:
    # check how many samples we have to use for the fade in/out:
    fade_samples = int(tone_fade * audio_sample_freq)

    # if there are enough, but not too many fade samples,
    # apply cosine ramp to signal
    if fade_samples > 0 and fade_samples < len(sine_wave):
      ramp = np.cos(np.linspace(0, np.pi / 2, fade_samples))
      sine_wave[:fade_samples] *= ramp[::-1]
      sine_wave[-fade_samples:] *= ramp

    # save sine_wave object as an audio file in .wav format
    sf.write("sine_wave.wav", sine_wave, audio_sample_freq)

    # create a Sound object that can be used by our custom Sound function
    sound = Sound(filename = "sine_wave.wav", 
                       device = sound_device, 
                       mul = 10)
                       

    # Functions for the staircases:
    
    # loud to soft:
    def staircase_down(start, step, limit):
        event.clearEvents() # clear all previous keypresses from buffer
        b = start
        while True:
            pressed_keys = event.getKeys()
            if 'escape' in pressed_keys:
                core.quit()
            if b < limit and not pressed_keys:
                sound = Sound("sine_wave.wav", sound_device, b)
                sound.play()
                b = b + step
            else:
                sound = Sound("sine_wave.wav", sound_device, b)
                #sound.play()
                sound.stop()
                print("detected threshold for current run:", b)
                return(b)
                
                
                
    #soft to loud, start at 10dB attenuation and go up to 100dB attenuation max.
    def staircase_up(start, step, limit):
        event.clearEvents() # clear all previous keypresses from buffer
        b = start
        while True:
            pressed_keys = event.getKeys()
            if 'escape' in pressed_keys:
                core.quit()
            if b > limit and not pressed_keys:
                sound = Sound("sine_wave.wav", sound_device, b)
                sound.play()
                b = b - step
            else:
                sound = Sound("sine_wave.wav", sound_device, b)
                #sound.play()
                sound.stop()
                print("detected threshold for current run:", b)
                return(b)

                
    # Start tests:
    values_down = []
    values_up = []
    values_av = []
    start_down = 10
    step = 3
    limit_down = 100
    limit_up = 0

    # show instruction
    while True:
        instr_hearthres.draw()
        win.flip()
        if event.getKeys(['space']):
            break

    # clear screen & wait a second
    win.flip()
    core.wait(1)

    #run test 5x:
    for t_idx in range(1,6):
        print("hearing ts trial:", t_idx)
        print("start down:", start_down)
        print("step:", step)
        print("limit down:", limit_down)
        print("limit up", limit_up)
        
        core.wait(0.5)
        # loud to soft:
        message1.setAutoDraw(True)
        win.flip()
        thres_down = staircase_down(start_down, step, limit_down)
        values_down.append(thres_down)
        message1.setAutoDraw(False)
        win.flip()
        core.wait(1)
        
        # soft to loud:
        start_up = thres_down + 15.0
        print("start_up", start_up)
        message2.setAutoDraw(True)
        win.flip()
        thres_up = staircase_up(start_up, step, limit_up)
        values_up.append(thres_up)
        message2.setAutoDraw(False)
        win.flip()
        core.wait(1)
        
        # get average of the 2 thresholds:
        thres_av = (thres_down + thres_up)/2.0
        print(thres_av)
        values_av.append(thres_av)
        
        # break:
        pause.setAutoDraw(True)
        win.flip()
        core.wait(3.0)
        pause.setAutoDraw(False)
        win.flip()
        print("-------------")
        
    # get mean attenuation we need for the experiment:
    av_attenuation = np.mean(values_av) 
    threshold = av_attenuation - 40 # - 40 dB to be 40dB above threshold
    print("average attenuation:", av_attenuation, " - threshold to use:", threshold)
    
# if we don't want to run the test, use default value for av_attenuation:
elif expInfo["meas_hearing"] == "no":
    av_attenuation = 50
    threshold = av_attenuation - 40 # - 40 dB to be 40dB above threshold
    print("default attenuation:", av_attenuation, " - threshold to use:", threshold)



### SOUNDCHECK: Can we hear the test sounds properly?

# show instructions
instr_test_sounds = visual.TextStim(win = win, text = "Soundcheck! Zum Starten bitte die Leertaste drücken!", pos = (0,0), color = "black", height = 0.5, wrapWidth = 1600)

while True: 
    instr_test_sounds.draw()
    win.flip()
    
    if event.getKeys(['space']):
        break

# loop tones and play them to test if everything works:
for test_freq in tones:

    # build a time array: you need the sound duration and the right sampling frequency for your device
    # 1 divided by the sampling rate = duration of a single sample in sec
    tone_sample_len = 1/audio_sample_freq
    
    # calculate the number of samples required for a 100 ms duration
    num_samples = int(audio_sample_freq * tone_duration)

    # build a time array
    t = np.arange(0, num_samples) / audio_sample_freq  # Adjust the time array
    
    # generate sine wave:
    sine_wave = np.sin(2 * np.pi * test_freq * t)

    # apply cosine ramp:
    # check how many samples we have to use for the fade in/out:
    fade_samples = int(tone_fade * audio_sample_freq)

    # if there are enough, but not too many fade samples,
    # apply cosine ramp to signal
    if fade_samples > 0 and fade_samples < len(sine_wave):
      ramp = np.cos(np.linspace(0, np.pi / 2, fade_samples))
      sine_wave[:fade_samples] *= ramp[::-1]
      sine_wave[-fade_samples:] *= ramp

    # save sine_wave object as an audio file in .wav format
    sf.write("sine_wave.wav", sine_wave, audio_sample_freq)

    # create a Sound object that can be used by our custom Sound function
    curr_sound = Sound(filename = "sine_wave.wav", 
                       device = sound_device, 
                       mul = threshold) # use threshold we determined before
    
    # create trial clock:
    my_trial_clock = core.Clock()
    
    # play each sound 3x
    for test_sound_run in range(1, 4):     
        # get current time:
        now = ptb.GetSecs()
        
        # send tone onset trigger
        send_trigger("freq_" + str(test_freq) + "_onset")
        my_trial_clock.reset() # start trial clock
        
        # play the sound immediately:
        curr_sound.play() # duration: 100 ms
        
        # send 0 trigger to EEG, wait, then send tone offset trigger
        parallel.setData(0)
        core.wait(time_after_trigger) # wait 3 ms
        send_trigger("freq_" + str(test_freq) + "_offset")
        core.wait(time_after_trigger) # wait 3 ms
        parallel.setData(0)
        
        # 1 3Hz cycle = 333.33 ms, so continue waiting until 333.33 ms have 
        # passed since starting the tone before playing the next tone
        #print("time passed since start of tone:", time_passed)
        core.wait(0.33333 - my_trial_clock.getTime())
        
continueRoutine = False # end routine
# keep track of which components have finished
soundsComponents = []
for thisComponent in soundsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
soundsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sounds"-------
while continueRoutine:
    # get current time
    t = soundsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=soundsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in soundsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sounds"-------
for thisComponent in soundsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "sounds" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=30.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "no_text_blocks"-------
    continueRoutine = True
    # update component parameters for each repeat
    #################################################
    #                Blocks w/o text                #
    #################################################
    # this routine is for all blocks where there are 
    # coloured rectangles instead of words
    
    # the non-text blocks all come in succession, there's just 1 main block in between them.
    # So use loop here that runs the non-text blocks 
    # until we have to display a main text block (in this case we exit the routine).
    while True:
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
        
        # clear buffer of all previously recorded key events:
        event.clearEvents()
        
        ### specify settings for the current block
    
        ### Prepare stimuli:
    
        # get block kind
        curr_block = all_blocks[exp_block_counter]
        print("start preparing block " + curr_block)
    
        # Check whether it's one of the non-text tasks.
        # If current block is a text block, skip this routine and go to the next.
        if curr_block not in ["click_training", "1back_single_training1", "1back_single_training2", 
                          "1back_single_main", "2back_single_training1", "2back_single_training2", "2back_single_main"]:
            print("skipping current routine")
            break
    
        # if it's one of the non-text blocks, though, prepare stimuli:
        else:
            print(curr_block + " is not a text block - preparing rect as stim now")
            
            # keep background ivory
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
            
            ### Show instructions
            # set instruction text
            instr_text = locals()["instr_" + curr_block]
            # create text box
            instr_text_stim = visual.TextStim(win, 
                                             text = instr_text, 
                                             height = 0.5, 
                                             pos = (0, 7),
                                             font = "Bookman Old Style",
                                             color = 'black')
            # create ImageStim object
            curr_instr_pic = visual.ImageStim(win, 
                                              size = (10, 4),
                                              pos = (0, -2),
                                              image = locals()["instr_pic_" + curr_block]) # set path to image here
    
            # display the text & image on screen
            if curr_block in ["1back_single_training2", "2back_single_training2"]:
                while True:
                    instr_text_stim.draw()
                    curr_instr_pic.draw()
                    win.flip()
                    # skip current block (aka the second training block))
                    if event.getKeys(['space']):
                        print("start next block - skip second training block")
                        skip_curr_block = True
                        break
                    # repeat training (aka run current block, which is the second training block)
                    elif event.getKeys(['w']):
                        print("repeat training block")
                        skip_curr_block = False
                        break
            # for regular blocks that can't be repeated:
            else: 
                while True:
                    instr_text_stim.draw()
                    curr_instr_pic.draw()
                    win.flip()
                    # start current block
                    if event.getKeys(['space']):
                        print("start current block")
                        skip_curr_block = False
                        break
                        
            # only run this if the current block shall not be skipped:
            if skip_curr_block == False:
                ### change background colour 
                # transition from white (RGB: 255, 255, 255)
                # to medium grey (RGB: 10, 10, 10)
                change_bg_colour(window = win, 
                                 start_rgb = light_bg_col, 
                                 end_rgb = dark_bg_col, 
                                 seconds = 2)
                # Wait for a brief period of time (800 ms) so bg is set
                core.wait(0.8)
                # keep background grey
                win.setColor(dark_bg_col, colorSpace='rgb')
                win.flip()
            
                # don't show questions
                skip_questions = True
                training_Qs = False
    
                # get n-back condition:
                curr_nback_cond = curr_block[0] # get first character of block name
                
                # if it is a 1 or a 2, set that as current n-back level:
                if curr_nback_cond in ['1', '2']:
                    curr_nback_cond == int(curr_nback_cond)
                # if it's neither 1 nor 2, it has to be a block without n-back,
                # so set curr_nback_cond to None
                else:
                    curr_nback_cond = None
                
                print("current n-back condition: " + str(curr_nback_cond))
    
                # get list with targets & list with colours
                curr_targets = all_target_lists[exp_block_counter]
                curr_colours = all_colour_lists[exp_block_counter]
                # for current text nr, get text whose name = current text nr
                curr_text = locals()[curr_text_nr]
    
    
                
                ### PUPIL SIZE BASELINE MEASUREMENT BLOCK
                
                start_block_instr = visual.TextStim(win = win, 
                                                text = "Der Block startet in 10 Sekunden. Bitte schauen Sie solange auf das Fixationskreuz.", 
                                                pos = (0,0), 
                                                color = "white", 
                                                height = 0.5, 
                                                wrapWidth = 1600)
                # CREATE CLOCK:
                my_block_clock = core.Clock()
                my_block_clock.reset() # start block clock
    
                while my_block_clock.getTime() < 3: 
                    start_block_instr.draw()
                    win.flip()
                    if event.getKeys(['space']):
                        break
                win.flip()
    
                # show fixation cross for 10 seconds
                fix_cross = visual.TextStim(win = win, 
                                         text = "+", 
                                         pos = (0,0), 
                                         color = "black", 
                                         height = 1, 
                                         wrapWidth = 1600)
                                         
                my_block_clock.reset() # start block clock
    
                while my_block_clock.getTime() < 10: 
                    fix_cross.draw()
                    win.flip()
                    if event.getKeys(['escape']):
                        break
                win.flip() # clear screen again
                
    
                ### Start block loop
                
                # prepare flicker
                # hint: flicker_freq and frame_rate are set in the settings 
                # code component at the beginning of the experiment.
                
                # create flicker phase variable - start at phase = 0
                flicker_phase = 0
                
                # CREATE CLOCKS: 
                my_block_clock = core.Clock()
                my_block_clock.reset() # start block clock
                start_time = my_block_clock.getTime() # get start time of block
                # also create trial clock
                my_trial_clock = core.Clock()
               
                # create empty stimulus 
                stim = visual.Rect(win = win,
                                   width = 3, # width = 3 * 1° visual angle (to make it look rectangle-ish)
                                   height = 1, # height = 1° visual angle (just like words)
                                  # colorSpace = "hex",
                                   pos = (0,0)) # center stimulus 
                
                stim.draw()
                win.flip()
    
                # clear buffer of all previously recorded key events:
                event.clearEvents()
    
                # send block onset trigger
                send_trigger(curr_block + "_onset")
                # wait for a few ms before sending 0 trigger
                core.wait(time_after_trigger) 
                parallel.setData(0)
                core.wait(0.1) #wait 100ms before starting first trial
    
                # loop colours in current text
                for trial_idx, curr_col in enumerate(curr_colours):
                    #print("current idx: " + str(trial_idx) + ", curr colour:" + curr_col)
                    
                    ### prepare & show current word:
                    my_trial_clock.reset() # start trial clock
                    onset_time = my_trial_clock.getTime()
                    
                    # if it's a block with an n-back task, prepare target list
                    if curr_nback_cond != None:
                        curr_target = curr_targets[trial_idx]
                        saw_target = False
                    
                    # get trial number (start counting from 1, so add 1)
                    curr_trial_nr = trial_idx + 1
                    
                    ### ISI: wait for 200 ms
                    
                    while my_trial_clock.getTime() < 0.2:
                        win.flip() # don't draw anything
                        core.wait(0.005) # wait 5 ms before next iteration
                    
                    # set current colour as colour of rectangle
                    stim.fillColor = curr_col
                    
                    # Flicker option 1: use sine-wave (gradient) flicker
                    #frame_time = my_block_clock.getTime() # get current time point (in sec)
                    #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
                    #opacity = (flicker_intensity + 1) / 2
        
                    # Flicker option 2: use square-wave (on-off) flicker
                    frame_time = my_block_clock.getTime()
                    time_passed = frame_time - start_time # subtract current time from block onset time
                    cycle_duration = 1 / flicker_freq
                    cycle_passed = time_passed % cycle_duration
                    
                    if cycle_passed < cycle_duration / 2:
                        opacity = 1
                    else: 
                        opacity = 0
                    
                    # set opacity
                    stim.opacity = opacity  
                    # draw stimulus on screen
                    stim.draw()
                    win.flip()
            
                    # show stimulus on screen & send trigger:
                    stim.draw() # draw stimulus on screen
                    # update the window to clear the screen and display 
                    # the stimulus, send trigger on flip
                    trig_off = False # haven't turned off trigger yet
                    win.callOnFlip(send_trigger, "trial_onset") 
                                    
                    # start trial clock for measuring RTs from stimulus onset
                    my_trial_clock.reset()
    
                    #onset_time = my_trial_clock.getTime()
                                           
                    ### wait for key response: 
                    # In blocks with n-back task, participants can press "c" to indicate they saw a target colour and "space" to go to the next word/stimulus.
                    # In blocks without n-back task, participants can only press "space" to go to the next stimulus.
                    #print("start tracking key responses")
                        
                    ### start recording responses
                    # start "endless" while loop that looks for responses
                    # in each iteration, draw word on screen
                    continue_trial = True
                    while continue_trial:       
                        # check if 3 ms have passed since trigger was sent,
                        # if yes, send 0 to parallel port
                        if trig_off == False and my_trial_clock.getTime() >= onset_time + time_after_trigger: # trigger onset + 3 ms
                            parallel.setData(0)
                            trig_off = True # remember you turned off the trigger
    
                        # Flicker option 1: use sine-wave (gradient) flicker
                        #frame_time = my_block_clock.getTime() # get current time point (in sec)
                        #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
                        #opacity = (flicker_intensity + 1) / 2
                    
                        # Flicker option 2: use square-wave (on-off) flicker
                        frame_time = my_block_clock.getTime()
                        time_passed = frame_time - start_time 
                        cycle_duration = 1 / flicker_freq
                        cycle_passed = time_passed % cycle_duration
                        
                        if cycle_passed < cycle_duration / 2:
                            opacity = 1
                        else: 
                            opacity = 0
                        
                        # set opacity
                        stim.opacity = opacity  
                        # draw stimulus on screen
                        stim.draw()
                        win.flip()
                        
                        # check for responses: 
                        keys = event.getKeys(['space', 'c', 'escape'])
                        
                        # check if there was a response. If there wasn't, we can go straight 
                        # to the next iteration which will hopefully save us some dropped 
                        # frames in the flicker.
                        for key in keys:
                            
                            # if participant pressed the space bar on their keyboard...
                            if key == 'space':
                                # get reaction time
                                curr_duration = my_trial_clock.getTime() * 1000
                                # send trigger for response:
                                send_trigger("response_continue")
                                # wait 3ms
                                core.wait(time_after_trigger)
                                parallel.setData(0)
                                
                                # break while loop to go to next trial
                                continue_trial = False
    
                            # if participant pressed button "c" for the first time and it's an n-back condition 
                            # where they're actually supposed to do that (aka not a reading baseline condition)...
                            elif key == 'c' and curr_nback_cond != None and saw_target == False:
                                # get reaction time
                                curr_nback_RT = my_trial_clock.getTime() * 1000
    
                                # send trigger for response:
                                send_trigger("response_target")
                                # wait 3ms
                                core.wait(time_after_trigger)
                                parallel.setData(0)
                                
                                # only get first target response, we don't care if they press the button more than once:
                                saw_target = True
    
                            # If esc is pressed, end the experiment:
                            elif key == 'escape':
                                et_abort_exp() # shut down eyetrigger and download incremental data
                                # make sure parallel port line is cleared
                                core.wait(time_after_trigger)
                                parallel.setData(0)
                                core.wait(0.5)
                                # end experiment
                                core.quit()
                        
                    ### end trial
                    #print("end trial")
                                       
                    # stop display of current word & send trial offset trigger
                    win.callOnFlip(send_trigger, "trial_offset")
                    core.wait(time_after_trigger)
                    parallel.setData(0)
         
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
                    thisExp.addData('target', curr_target)
                    thisExp.addData('nback_response', curr_nback_response)
                    thisExp.addData('nback_RT', curr_nback_RT) # in ms
                    thisExp.addData('duration', curr_duration) # in ms
                    thisExp.addData('trial_nr', curr_trial_nr)
                    thisExp.addData('block_nr', exp_block_counter)
                    thisExp.addData('block_name', curr_block)
                    thisExp.addData('block_kind', curr_nback_cond)
        
                    # start a new row in the csv
                    thisExp.nextEntry()
                    
                    ### IF TESTING MODE ENABLED: end loop after 4 trials
                    if expInfo['testing_mode'] == "yes":
                        if trial_idx == 3:
                            break
    
                print("finished presenting trials")
                
                # change background colour from grey (RGB: 10, 10, 10)
                # to ivory (RGB: 240, 223, 204)
                change_bg_colour(window = win, 
                                 start_rgb = dark_bg_col, 
                                 end_rgb = light_bg_col, 
                                 seconds = 2)
                # Wait for a brief period of time so bg is set
                core.wait(0.8)
                # keep background ivory
                win.setColor(light_bg_col, colorSpace='rgb')
                win.flip()
            
            ### End currrent block
            core.wait(time_after_trigger) # wait 3 ms
            # send block offset trigger
            send_trigger("block_offset")
            # wait for 3 ms before sending 0 trigger
            core.wait(time_after_trigger) 
            parallel.setData(0)
                
            # add 1 to the block counter to go load the next block
            exp_block_counter = exp_block_counter + 1
            print("Going to block " + str(exp_block_counter + 1) + "/17 now!")
    
    # go to next routine
    print("going to next routine")
    continueRoutine = False
    # keep track of which components have finished
    no_text_blocksComponents = []
    for thisComponent in no_text_blocksComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    no_text_blocksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "no_text_blocks"-------
    while continueRoutine:
        # get current time
        t = no_text_blocksClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=no_text_blocksClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in no_text_blocksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "no_text_blocks"-------
    for thisComponent in no_text_blocksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "no_text_blocks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "text_blocks"-------
    continueRoutine = True
    # update component parameters for each repeat
    #################################################
    #                Blocks with text               #
    #################################################
    # this routine is for all blocks with texts
    
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    
    # clear buffer of all previously recorded key events:
    event.clearEvents()
    
    ### specify settings for the current block
    
    ### Prepare stimuli:
    
    # get block kind
    curr_block = all_blocks[exp_block_counter]
    print("start preparing block " + curr_block)
    
    # Check whether it's some of the non-text tasks, 
    # the reading bl training or one of the dual-task main blocks.
    
    # If current block it's a non-text block, skip this routine.
    if curr_block in ["click_training", "1back_single_training1", "1back_single_training2", 
                      "1back_single_main", "2back_single_training1", "2back_single_training2", "2back_single_main"]:
        print("skipping current routine")
        # skip questions & end current routine
        skip_questions = True
        continueRoutine = False
        
    # if it's the reading bl training block, prepare training stimuli:
    elif curr_block == "Reading_Baseline_training":
        
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
        
        ### Show instructions
        # set instruction text
        instr_text = locals()["instr_" + curr_block]
        # create text box
        instr_text_stim = visual.TextStim(win, 
                                          text = instr_text, 
                                          height = 0.5, # font height: 5° visual angle
                                          font = "Bookman Old Style",
                                          pos = (0, 7), # move up a bit
                                          color = "black")
        # create ImageStim object
        curr_instr_pic = visual.ImageStim(win, 
                                          size = (10, 4),
                                          pos = (0, -2),
                                          image = locals()["instr_pic_" + curr_block]) # set path to image here
    
        # display the text on screen
        while True:
            # keep background ivory
            win.setColor(light_bg_col, colorSpace='rgb')
            instr_text_stim.draw()
            curr_instr_pic.draw()
            win.flip()
            # end showing screen if participant presses space
            if 'space' in event.getKeys():
                break 
                
        ### get training text
        curr_text = reading_bl_tr_text
        curr_text_nr = "reading_bl_training_text"
        curr_nback_cond = None
        curr_colours = all_colour_lists[0]
        # show training questions
        skip_questions = False
        training_Qs = True
        
        ### prepare flicker
        # hint: flicker_freq and frame_rate are set in the settings 
        # code component at the beginning of the experiment.
        
        # create flicker phase variable - start at phase = 0
        flicker_phase = 0
        # we also need the start time (let's set it as current time 
        # at this point in the script):
        start_time = core.getTime()
        
        
        ### change background colour 
        # transition from ivory 
        # to medium grey 
        change_bg_colour(window = win, 
                         start_rgb = light_bg_col,
                         end_rgb = dark_bg_col, 
                         seconds = 2)
        # Wait for a brief period of time so bg is set
        core.wait(0.8)
        # keep background grey
        win.setColor(dark_bg_col, colorSpace='rgb')
        win.flip()
    
    # if it's one of the "normal" main blocks, prepare main block stimuli:
    elif curr_block in ["Reading_Baseline_main", "1back_dual_main", "2back_dual_main"]:
    
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
        
        ### Show instructions
        # set instruction text
        instr_text = locals()["instr_" + curr_block]
        # create text box
        instr_text_stim = visual.TextStim(win, 
                                          text = instr_text, 
                                          height = 0.5, # font height: 5° visual angle
                                          font = "Bookman Old Style",
                                          pos = (0, 7),
                                          color = "black")
        
        # create ImageStim object
        curr_instr_pic = visual.ImageStim(win, 
                                          size = (10, 4),
                                          pos = (0, -2),
                                          image = locals()["instr_pic_" + curr_block]) # set path to image here
    
        # Display the text on screen
        while True:
            instr_text_stim.draw()
            curr_instr_pic.draw()
            win.flip()
            # end showing screen if participant presses space
            if 'space' in event.getKeys():
                break 
        
        ### change background colour 
        # transition from ivory to medium grey
        change_bg_colour(window = win, 
                         start_rgb = light_bg_col,
                         end_rgb = dark_bg_col, 
                         seconds = 2)
        # Wait for a brief period of time so bg is set
        core.wait(0.8)
        # keep background grey
        win.setColor(dark_bg_col, colorSpace='rgb')
        win.flip()
    
        # show main block questions
        skip_questions = False
        training_Qs = False
        
        # get text nr:
        curr_text_nr = all_texts_nrs_list[exp_block_counter]
        
        # get n-back condition:
        curr_nback_cond = curr_block[0] # get first character of block name
    
        # if it is a 1 or a 2, set that as current n-back level:
        if curr_nback_cond in ['1', '2']:
            curr_nback_cond == int(curr_nback_cond)
        # if it's neither 1 nor 2, it has to be a block without n-back,
        # so set curr_nback_cond to None
        else:
            curr_nback_cond = None
        
        print("current n-back condition: " + str(curr_nback_cond))
        
        # get list with targets & list with colours
        curr_targets = all_target_lists[exp_block_counter]
        curr_colours = all_colour_lists[exp_block_counter]
        # for current text nr, get text whose name = current text nr
        curr_text = locals()[curr_text_nr]
    
        
    ### Start block loop
    
    # if it's the first reading BL block, create arrays for saving response 
    # times & words - we need that later for the visual task
    if exp_block_counter == 1:
        vis_task_durations = []
        vis_task_words = []
    
    # create empty text stimulus 
    stim = visual.TextStim(win = win, 
                           text = " ", 
                           pos = (0,0), # center stimulus
                           font = "Times New Roman",
                           height = 1) # font height = 1° visual angle
    
    # create grey rectangle that masks the text if I set opacity to 1
    # --> changing the text opacity directly isn't working: https://discourse.psychopy.org/t/opacity-of-text-stimuli-is-not-updating/11152/7    
    stim_mask = visual.Rect(win = win,
                            width = 20, # width = 20° visual angle
                            height = 3, # height = 3° visual angle 
                            pos = (0,0), # center stimulus 
                            opacity = 0, # set opacity to 0 for a start
                            fillColor = dark_bg_col,
                            colorSpace = "rgb")
    
    stim.draw()
    stim_mask.draw()
    win.flip()
    
    # clear buffer of all previously recorded key events:
    event.clearEvents()
    
    # send block onset trigger
    send_trigger(curr_block + "_onset")
    # wait for 3 ms before sending 0 trigger
    core.wait(time_after_trigger) 
    parallel.setData(0)
    core.wait(0.1) #wait 100ms before starting first trial
    
    
    ### PUPIL SIZE BASELINE MEASUREMENT BLOCK
                
    start_block_instr = visual.TextStim(win = win, 
                                    text = "Der Block startet in 30 Sekunden. Bitte schauen Sie solange auf das Fixationskreuz.", 
                                    pos = (0,0), 
                                    color = "white", 
                                    height = 0.5, 
                                    wrapWidth = 1600)
    # CREATE CLOCK:
    my_block_clock = core.Clock()
    my_block_clock.reset() # start block clock
    
    while my_block_clock.getTime() < 3: 
        start_block_instr.draw()
        win.flip()
        if event.getKeys(['space']):
            break
    win.flip()
    
    # show fixation cross for 10 seconds
    fix_cross = visual.TextStim(win = win, 
                             text = "+", 
                             pos = (0,0), 
                             color = "black", 
                             height = 1, 
                             wrapWidth = 1600)
                             
    my_block_clock.reset() # start block clock
    
    while my_block_clock.getTime() < 10: 
        fix_cross.draw()
        win.flip()
        if event.getKeys(['escape']):
            break
    win.flip() # clear screen again
    
    
    ### prepare flicker
    # hint: flicker_freq and frame_rate are set in the settings 
    # code component at the beginning of the experiment.    
    # create flicker phase variable - start at phase = 0
    flicker_phase = 0
    # we also need the start time, this is recorded where we create the block clocks
    
    # CREATE CLOCKS: 
    my_block_clock.reset() # start block clock
    start_time = my_block_clock.getTime() # get start time of block
    # also create trial clock
    my_trial_clock = core.Clock()
    
    
    # loop words in current text
    for trial_idx, curr_word in enumerate(curr_text):
        #print("current idx: " + str(trial_idx) + ", curr word:" + curr_word)
        
        ### prepare & show current word:
        
        # get current colour
        curr_colour = curr_colours[trial_idx]
        
        # if it's a block with an n-back task, prepare target list as well
        if curr_nback_cond != None:
            curr_target = curr_targets[trial_idx]
            saw_target = False
        
        # get trial number (start counting from 1, so add 1)
        curr_trial_nr = trial_idx + 1
    
        # set current word & colour as content of text stimulus
        stim.color = curr_colour
        stim.text = curr_word
        
        
        # Flicker option 1: use sine-wave (gradient) flicker
        # --> doesn't seem to work, I don't see the words flicker when I play this
        # create current opacity value to continue flickering the word
        #frame_time = my_block_clock.getTime() # get current time point (in sec)
        #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
        #opacity = (flicker_intensity + 1) / 2
    
        # Flicker option 2: use square-wave (on-off) flicker
        frame_time = my_block_clock.getTime() # get current time point (in sec)
        time_passed = frame_time - start_time # calculate time passed since start
        cycle_duration = 1 / flicker_freq # calculate duration of one flicker cycle
        cycle_passed = time_passed % cycle_duration # calculate time passed in current flicker cycle
        if cycle_passed < cycle_duration / 2: # if in the first half of the cycle
            opacity = 1 # set opacity to 1
        else: # if in the second half of the cycle
            opacity = 0 # set opacity to 0
            
        stim_mask.opacity = opacity
        
        # show word on screen & send trigger:
        stim.draw() # draw word on screen
        stim_mask.draw() # draw mask on screen
        
        # update the window to clear the screen and display 
        # the stimulus, send word onset trigger on flip
        trig_off = False # haven't turned off trigger yet
        win.callOnFlip(send_trigger, "trial_onset") 
                    
        # start trial clock
        my_trial_clock.reset()
        onset_time = my_trial_clock.getTime()
        
        ### wait for 50 ms
        while my_trial_clock.getTime() < onset_time + 0.05:
            
            # if it's time to turn off trigger, do so:
            if my_trial_clock.getTime() <= onset_time + time_after_trigger and trig_off == False:
                parallel.setData(0)
                trig_off = True
            
            # draw the stimulus during the waiting period
    
            # Flicker option 1: use sine-wave (gradient) flicker
            #frame_time = my_block_clock.getTime() 
            #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
            #opacity = (flicker_intensity + 1) / 2
    
            # Flicker option 2: use square-wave (on-off) flicker
            frame_time = my_block_clock.getTime() 
            time_passed = frame_time - start_time 
            cycle_duration = 1 / flicker_freq
            cycle_passed = time_passed % cycle_duration
            if cycle_passed < cycle_duration / 2:
                opacity = 1
            else: 
                opacity = 0
            
            stim_mask.opacity = opacity
        
            stim.draw() # draw text
            stim_mask.draw() # draw mask
            win.flip()
                
        ### wait for key response: 
        # In blocks with n-back task, participants can press "c" to indicate they saw a target colour and "space" to go to the next word/stimulus.
        # In blocks without n-back task, participants can only press "space" to go to the next word/stimulus.
        #print("start tracking key responses")
            
        ### start recording responses
        # start "endless" while loop that looks for responses
        continue_trial = True
        while continue_trial:   
                    
            # in each iteration, draw word on screen
            # --> flicker again
    
            # Flicker option 1: use sine-wave (gradient) flicker
            #frame_time = my_block_clock.getTime() 
            #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
            #opacity = (flicker_intensity + 1) / 2
    
            # Flicker option 2: use square-wave (on-off) flicker
            frame_time = my_block_clock.getTime() 
            time_passed = frame_time - start_time 
            cycle_duration = 1 / flicker_freq
            cycle_passed = time_passed % cycle_duration
            if cycle_passed < cycle_duration / 2:
                opacity = 1
            else: 
                opacity = 0
                
            stim_mask.opacity = opacity
            
            stim.draw()
            stim_mask.draw()
            win.flip()
            
            # check for key responses:
            keys = event.getKeys(['space', 'c', 'escape'])
            
            # if we recorded a response, check which one. 
            # If not, we go  to the next "while" iteration, 
            # so I hope this saves us a few dropped frames in the flicker.
            for key in keys:
                
                # if participant pressed space bar on their keyboard...
                if key == 'space':
                    # get reaction time
                    curr_duration = my_trial_clock.getTime() * 1000
                    # send trigger for response:
                    send_trigger("response_continue")
                    # wait 3ms before closing trigger
                    core.wait(time_after_trigger)
                    parallel.setData(0)
                    # break while loop
                    continue_trial = False
    
                # if participant pressed button "c" for the first time and it's an n-back condition 
                # where they're actually supposed to do that (aka not a reading baseline condition)...
                elif key == 'c' and curr_nback_cond != None and saw_target == False:
                    # get reaction time
                    curr_nback_RT = my_trial_clock.getTime() * 1000    
                    # send trigger for response:
                    send_trigger("response_target")
                    # wait 3ms before closing trigger
                    core.wait(time_after_trigger)
                    parallel.setData(0)
                    
                    # only get first target response, we don't care if they press the button more than once:
                    saw_target = True
                    
                # If esc is pressed, end the experiment:
                elif key =='escape':
                    et_abort_exp() # shut down eyetrigger and download incremental data             
                    # close trigger & close experiment
                    core.wait(time_after_trigger)
                    parallel.setData(0)
                    core.wait(0.5)
                    core.quit()
            
        ### end trial
        print("end trial")
        # stop display of current word & send trial offset trigger
        win.callOnFlip(send_trigger, "trial_offset")
        core.wait(time_after_trigger)
        parallel.setData(0)
        
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
        thisExp.addData('target', curr_target)
        thisExp.addData('nback_response', curr_nback_response)
        thisExp.addData('nback_RT', curr_nback_RT) # in ms
        thisExp.addData('duration', curr_duration) # in ms
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('trial_nr', curr_trial_nr)
        thisExp.addData('block_nr', exp_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('block_kind', curr_nback_cond)
        # careful, make sure quotes in the strings are escaped using a 
        # quote (weird, I know) so it's properly saved in the CSV:
        thisExp.addData('word', escape_quotes(curr_word))
    
        # start a new row in the csv
        thisExp.nextEntry()
        
        # if it's a reading BL block, we need to 
        # also collect the RTs in an array for the visual task later
        if curr_block == "Reading_Baseline_main":
            vis_task_durations.append(curr_duration)
            vis_task_words.append(curr_word)
    
        ### IF TESTING MODE ENABLED: end loop after 4 trials
        if expInfo['testing_mode'] == "yes":
            if trial_idx == 3:
                break
    
    print("finished presenting trials")
    
    # Send end of block trigger:
    core.wait(time_after_trigger) # wait 3 ms
    # send block offset trigger
    send_trigger("block_offset")
    # wait for3 ms before sending 0 trigger
    core.wait(time_after_trigger) 
    parallel.setData(0)
            
    ### Prepare questions
    
    # change background colour from grey to ivory
    change_bg_colour(window = win, 
                     start_rgb = dark_bg_col, 
                     end_rgb = light_bg_col, 
                     seconds = 2)
    # Wait for a brief period of time so bg is set
    core.wait(0.5)
    
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
            
    # end current routine
    continueRoutine = False
    # keep track of which components have finished
    text_blocksComponents = []
    for thisComponent in text_blocksComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    text_blocksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "text_blocks"-------
    while continueRoutine:
        # get current time
        t = text_blocksClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=text_blocksClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in text_blocksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "text_blocks"-------
    for thisComponent in text_blocksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "text_blocks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q1"-------
    continueRoutine = True
    # update component parameters for each repeat
    ##########################################################
    #            Text Comprehension Questions - Q1           #
    ##########################################################
    
    ### Settings:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    
    # clear buffer of all previously recorded key events:
    event.clearEvents()
    
    # check which kind of block we have
    # if there was no text before, we can skip the questions
    if skip_questions:
        continueRoutine = False
    # if we have a training text, set training questions
    elif skip_questions == False and training_Qs:
        Q1 = reading_bl_tr_Q1
        Q1_answers = reading_bl_tr_Q1_ans
        Q1_corr = reading_bl_tr_Q1_corr
        
    # if we have a main text, set regular questions
    elif skip_questions == False and training_Qs == False:
        # load first question for current text & their respective answers
        Q1 = locals()[curr_text_nr + "_Q1"]
        Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
        Q1_corr = locals()[curr_text_nr + "_Q1_corr"]
    
    # Define text positions and formatting
    question_pos = (0, 3)
    answer_xpos = -7 # move questions a bit to the left 
    answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers
    
    # Create text stim for the question:
    question = visual.TextStim(win, 
                               text = Q1, 
                               pos = question_pos,
                               color = "black",
                               height = 0.5,
                               font = "Bookman Old Style",
                               anchorHoriz = 'center',
                               alignText = 'center', 
                               wrapWidth = 10)
    # create 1 text stim for each answer option:
    answers = [visual.TextStim(win, 
                               text = Q1_answers[i], 
                               pos = (answer_xpos, answer_ypos[i]), 
                               color = "black", # set all to black as a default
                               height = 0.5, 
                               font = "Bookman Old Style",
                               wrapWidth = 15,
                               anchorHoriz = 'left', 
                               alignText = 'center') for i in range(len(Q1_answers))]
    # set up instruction text
    instr_text = visual.TextStim(win, 
                                 text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                                 color = "grey",
                                 pos = (0, -10),
                                 wrapWidth = 20,
                                 height = 0.4,
                                 font = "Bookman Old Style")
    
    ### Show all on screen until I set .autoDraw = False
    question.autoDraw = True
    instr_text.autoDraw = True
    for answer in answers:
        answer.autoDraw = True
    win.flip()
    
    
    ### Record key responses:
    Q1_chosen_ans = None
    
    while True:        
        # if 1 was pressed...
        if event.getKeys(['1']):
            print('a')
            # save Q1 answer as a 
            Q1_chosen_ans = "a"
            # set font colour of the first answer (answer a) to 
            # green and the rest to black:
            answers[0].setColor("green")
            for answer in answers[1:]:
                answer.setColor("black")
                # draw updated stimulus:
                win.flip()
        # same procedure for all other answer options:
        if event.getKeys(['2']):
            print('b')
            Q1_chosen_ans = "b"
            # set font colour of the second answer (answer b) to 
            # green and the rest to black:
            answers[1].setColor("green")
            for answer in [answers[0]] + answers[2:]:
                answer.setColor("black")
                # draw updated stimulus:
                win.flip()
        if event.getKeys(['3']):
            print('c')
            Q1_chosen_ans = "c"
            # set font colour of the third answer (answer c) to 
            # green and the rest to black:
            answers[2].setColor("green")
            for answer in answers[:2] + answers[3:]:
                answer.setColor("black")
            # draw updated stimulus:
            win.flip()
        if event.getKeys(['4']):
            print('d')
            Q1_chosen_ans = "d"
            # set font colour of the fourth answer (answer d) to 
            # green and the rest to black:
            answers[3].setColor("green")
            for answer in answers[:-1]:
                answer.setColor("black")
            # draw updated stimulus 
            win.flip()
        # if participant pressed "space", check whether they chose an answer.
        # if yes, end this routine and go to next question, if not, wait for valid answer.
        elif event.getKeys(['space']) and Q1_chosen_ans != None:
            break
    
    # print chosen answer for Q1
    print("answer for Q1:" + str(Q1_chosen_ans))
    
    # check if answer was correct:
    if Q1_chosen_ans == Q1_corr: 
        print("answer correct!")
    else: 
        print("answer incorrect!")
        
    # save data:
    thisExp.addData('question', 'Q1')
    thisExp.addData('chosen_ans', Q1_chosen_ans)
    thisExp.addData('ans_correct', Q1_chosen_ans == Q1_corr)
    thisExp.addData('text_nr', curr_text_nr)
    thisExp.addData('block_nr', exp_block_counter)
    thisExp.addData('block_name', curr_block)
    thisExp.addData('block_kind', curr_nback_cond)
                    
    # start a new row in the csv
    thisExp.nextEntry()
    
    ### End Q1: Set .autoDraw = False to stop showing question & answers
    question.autoDraw = False
    instr_text.autoDraw = False
    for answer in answers:
        answer.autoDraw = False
    
    # end current routine
    continueRoutine = False
    # keep track of which components have finished
    Q1Components = []
    for thisComponent in Q1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Q1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Q1"-------
    while continueRoutine:
        # get current time
        t = Q1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Q1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q1"-------
    for thisComponent in Q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Q1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q2"-------
    continueRoutine = True
    # update component parameters for each repeat
    ##########################################################
    #            Text Comprehension Questions - Q2           #
    ##########################################################
    
    ### Settings:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    
    # clear buffer of all previously recorded key events:
    event.clearEvents()
    
    # check which kind of block we have
    # if there was no text before, we can skip the questions
    if skip_questions:
        continueRoutine = False
    # if we have a training text, set training questions
    elif skip_questions == False and training_Qs:
        Q2 = reading_bl_tr_Q2
        Q2_answers = reading_bl_tr_Q2_ans
        Q2_corr = reading_bl_tr_Q2_corr
        
    # if we have a main text, set regular questions
    elif skip_questions == False and training_Qs == False:
        # load first question for current text & their respective answers
        Q2 = locals()[curr_text_nr + "_Q2"]
        Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
        Q2_corr = locals()[curr_text_nr + "_Q2_corr"]
    
    # Define text positions and formatting
    question_pos = (0, 3)
    answer_xpos = -7 # move questions a bit to the left 
    answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers
    
    # Create text stim for the question:
    question = visual.TextStim(win, 
                               text = Q2, 
                               pos = question_pos,
                               color = "black",
                               height = 0.5,
                               font = "Bookman Old Style",
                               anchorHoriz = 'center',
                               alignText = 'center', 
                               wrapWidth = 10)
    # create 1 text stim for each answer option:
    answers = [visual.TextStim(win, 
                               text = Q2_answers[i], 
                               pos = (answer_xpos, answer_ypos[i]), 
                               color = "black", # set all to black as a default
                               height = 0.5, 
                               font = "Bookman Old Style",
                               wrapWidth = 15,
                               anchorHoriz = 'left', 
                               alignText = 'center') for i in range(len(Q1_answers))]
    # set up instruction text
    instr_text = visual.TextStim(win, 
                                 text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                                 color = "grey",
                                 pos = (0, -10),
                                 wrapWidth = 20,
                                 height = 0.4,
                                 font = "Bookman Old Style")
    ### Show all on screen until I set .autoDraw = False
    question.autoDraw = True
    instr_text.autoDraw = True
    for answer in answers:
        answer.autoDraw = True
    win.flip()
    
    
    ### Record key responses:
    Q2_chosen_ans = None
    
    while True:        
        # if 1 was pressed...
        if event.getKeys(['1']):
            print('a')
            # save Q2 answer as a 
            Q2_chosen_ans = "a"
            # set font colour of the first answer (answer a) to 
            # green and the rest to black:
            answers[0].setColor("green")
            for answer in answers[1:]:
                answer.setColor("black")
                # draw updated stimulus:
                win.flip()
        # same procedure for all other answer options:
        if event.getKeys(['2']):
            print('b')
            Q2_chosen_ans = "b"
            # set font colour of the second answer (answer b) to 
            # green and the rest to black:
            answers[1].setColor("green")
            for answer in [answers[0]] + answers[2:]:
                answer.setColor("black")
                # draw updated stimulus:
                win.flip()
        if event.getKeys(['3']):
            print('c')
            Q2_chosen_ans = "c"
            # set font colour of the third answer (answer c) to 
            # green and the rest to black:
            answers[2].setColor("green")
            for answer in answers[:2] + answers[3:]:
                answer.setColor("black")
            # draw updated stimulus:
            win.flip()
        if event.getKeys(['4']):
            print('d')
            Q2_chosen_ans = "d"
            # set font colour of the fourth answer (answer d) to 
            # green and the rest to black:
            answers[3].setColor("green")
            for answer in answers[:-1]:
                answer.setColor("black")
            # draw updated stimulus 
            win.flip()
        # if participant pressed "space", check whether they chose an answer.
        # if yes, end this routine and go to next question, if not, wait for valid answer.
        elif event.getKeys(['space']) and Q2_chosen_ans != None:
            break
    
    # print chosen answer for Q2
    print("answer for Q2:" + str(Q2_chosen_ans))
    
    # check if answer was correct:
    if Q2_chosen_ans == Q2_corr: 
        print("answer correct!")
    else: 
        print("answer incorrect!")
        
    # save data:
    thisExp.addData('question', 'Q2')
    thisExp.addData('chosen_ans', Q2_chosen_ans)
    thisExp.addData('ans_correct', Q2_chosen_ans == Q2_corr)
    thisExp.addData('text_nr', curr_text_nr)
    thisExp.addData('block_nr', exp_block_counter)
    thisExp.addData('block_name', curr_block)
    thisExp.addData('block_kind', curr_nback_cond)
                    
    # start a new row in the csv
    thisExp.nextEntry()
    
    ### End Q2: Set .autoDraw = False to stop showing question & answers
    question.autoDraw = False
    instr_text.autoDraw = False
    for answer in answers:
        answer.autoDraw = False
    
    # end current routine
    continueRoutine = False
    # keep track of which components have finished
    Q2Components = []
    for thisComponent in Q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Q2"-------
    while continueRoutine:
        # get current time
        t = Q2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Q2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q2"-------
    for thisComponent in Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q3"-------
    continueRoutine = True
    # update component parameters for each repeat
    ##########################################################
    #            Text Comprehension Questions - Q3           #
    ##########################################################
    
    ### Settings:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    
    # clear buffer of all previously recorded key events:
    event.clearEvents()
    
    # check which kind of block we have
    # if there was no text before, we can skip the questions
    if skip_questions:
        continueRoutine = False
    # if we have a training text, set training questions
    elif skip_questions == False and training_Qs:
        Q3 = reading_bl_tr_Q3
        Q3_answers = reading_bl_tr_Q3_ans
        Q3_corr = reading_bl_tr_Q3_corr
        
    # if we have a main text, set regular questions
    elif skip_questions == False and training_Qs == False:
        # load first question for current text & their respective answers
        Q3 = locals()[curr_text_nr + "_Q3"]
        Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
        Q3_corr = locals()[curr_text_nr + "_Q3_corr"]
    
    # Define text positions and formatting
    question_pos = (0, 3)
    answer_xpos = -7 # move questions a bit to the left 
    answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers
    
    # Create text stim for the question:
    question = visual.TextStim(win, 
                               text = Q3, 
                               pos = question_pos,
                               color = "black",
                               height = 0.5,
                               font = "Bookman Old Style",
                               anchorHoriz = 'center',
                               alignText = 'center', 
                               wrapWidth = 10)
    # create 1 text stim for each answer option:
    answers = [visual.TextStim(win, 
                               text = Q3_answers[i], 
                               pos = (answer_xpos, answer_ypos[i]), 
                               color = "black", # set all to black as a default
                               height = 0.5, 
                               font = "Bookman Old Style",
                               wrapWidth = 15,
                               anchorHoriz = 'left', 
                               alignText = 'center') for i in range(len(Q3_answers))]
    # set up instruction text
    instr_text = visual.TextStim(win, 
                                 text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                                 color = "grey",
                                 pos = (0, -10),
                                 wrapWidth = 20,
                                 height = 0.4,
                                 font = "Bookman Old Style")
                                 
    ### Show all on screen until I set .autoDraw = False
    question.autoDraw = True
    instr_text.autoDraw = True
    for answer in answers:
        answer.autoDraw = True
    win.flip()
    
    
    ### Record key responses:
    Q3_chosen_ans = None
    
    while True:        
        # if 1 was pressed...
        if event.getKeys(['1']):
            print('a')
            # save Q3 answer as a 
            Q3_chosen_ans = "a"
            # set font colour of the first answer (answer a) to 
            # green and the rest to black:
            answers[0].setColor("green")
            for answer in answers[1:]:
                answer.setColor("black")
                # draw updated stimulus:
                win.flip()
        # same procedure for all other answer options:
        if event.getKeys(['2']):
            print('b')
            Q3_chosen_ans = "b"
            # set font colour of the second answer (answer b) to 
            # green and the rest to black:
            answers[1].setColor("green")
            for answer in [answers[0]] + answers[2:]:
                answer.setColor("black")
                # draw updated stimulus:
                win.flip()
        if event.getKeys(['3']):
            print('c')
            Q3_chosen_ans = "c"
            # set font colour of the third answer (answer c) to 
            # green and the rest to black:
            answers[2].setColor("green")
            for answer in answers[:2] + answers[3:]:
                answer.setColor("black")
            # draw updated stimulus:
            win.flip()
        if event.getKeys(['4']):
            print('d')
            Q3_chosen_ans = "d"
            # set font colour of the fourth answer (answer d) to 
            # green and the rest to black:
            answers[3].setColor("green")
            for answer in answers[:-1]:
                answer.setColor("black")
            # draw updated stimulus 
            win.flip()
        # if participant pressed "space", check whether they chose an answer.
        # if yes, end this routine and go to next question, if not, wait for valid answer.
        elif event.getKeys(['space']) and Q3_chosen_ans != None:
            break
    
    # print chosen answer for Q3
    print("answer for Q3:" + str(Q3_chosen_ans))
    
    # check if answer was correct:
    if Q3_chosen_ans == Q3_corr: 
        print("answer correct!")
    else: 
        print("answer incorrect!")
        
    # save data:
    thisExp.addData('question', 'Q3')
    thisExp.addData('chosen_ans', Q3_chosen_ans)
    thisExp.addData('ans_correct', Q3_chosen_ans == Q3_corr)
    thisExp.addData('text_nr', curr_text_nr)
    thisExp.addData('block_nr', exp_block_counter)
    thisExp.addData('block_name', curr_block)
    thisExp.addData('block_kind', curr_nback_cond)
    
    # start a new row in the csv
    thisExp.nextEntry()
    
    ### End Q3: Set .autoDraw = False to stop showing question & answers
    question.autoDraw = False
    instr_text.autoDraw = False
    for answer in answers:
        answer.autoDraw = False
    
    # end current routine
    continueRoutine = False
    # keep track of which components have finished
    Q3Components = []
    for thisComponent in Q3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Q3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Q3"-------
    while continueRoutine:
        # get current time
        t = Q3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Q3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q3"-------
    for thisComponent in Q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Q3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "difficulty"-------
    continueRoutine = True
    # update component parameters for each repeat
    ##########################################################
    #                 Text Difficulty Rating                 #
    ##########################################################
    
    ### Settings:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    
    # check which kind of block we have
    # skip this routine if the current block wasn't Reading BL main
    if curr_block != "Reading_Baseline_main":
        continueRoutine = False
    else:
        
        # create a keyboard object to check if key is currently pressed 
        # (not really possible with event.getKey())
        kb = keyboard.Keyboard()
        
        # set question texts, item names and labels:
        items = ["Wie anstrengend war es für Sie, dem Text zu folgen?", "Wie schwierig fanden Sie den Text inhaltlich?", "Wie verständlich war der Text für Sie?", "Wie sehr mussten Sie sich beim Lesen konzentrieren?", "Wie einfach fanden Sie die Formulierungen im Text?", "Wie interessant fanden Sie den Text?"]
        item_names = ["subj_reading_effort1", "subj_text_difficulty", "subj_text_incomprehensibility1", "subj_reading_effort2", "subj_text_incomprehensibility2", "subj_interest_in_text"]
        item_labels = [["gar nicht anstrengend", "sehr anstrengend"], ["sehr leicht", "sehr schwierig"], ["sehr verständlich", "gar nicht verständlich"], ["gar nicht", "sehr stark"], ["sehr einfach","sehr schwierig"], ["sehr langweilig","sehr interessant"]]
        
        # loop items
        for item_idx, curr_item in enumerate(items):
            print("rating text difficulty – current item: " + item_names[item_idx])
                    
            # clear buffer of all previously recorded key events:
            event.clearEvents()
            
            # get matching labels & name of current item
            curr_item_labels = item_labels[item_idx]
            print("item labels: ", curr_item_labels)
            curr_item_name = item_names[item_idx]
            
            # set up slider
            slider = visual.Slider(win = win,
                                   pos = (0, 0), # position of the slider (centered on screen)
                                   size = (10, 0.5), # size of the scale
                                   labels = curr_item_labels, # labels for the ticks
                                   ticks = [0, 100], # make ticks at 0 and 100
                                   units = "deg", # unit = viewing angle degrees
                                   color = "black", 
                                   fillColor = "green", 
                                   borderColor = "black", 
                                   granularity = 1, # scale step size
                                   labelHeight = 0.5, # font size of the labels I guess?
                                   font = "Bookman Old Style")
            slider.markerPos = 50  # initial position of slider button
    
            # set up question text
            question_text = visual.TextStim(win, 
                                            text = curr_item,
                                            color = "black",
                                            pos = (0, 2),
                                            height = 0.6,
                                            font = "Bookman Old Style")
                                            
            # set up instruction text
            instr_text = visual.TextStim(win, 
                                         text = "(Bitte benutzen Sie die Pfeiltasten um den Punkt zu bewegen. Mit der Leertaste können Sie Ihre Bewertung bestätigen.)",
                                         color = "grey",
                                         pos = (0,-3), 
                                         height = 0.4,
                                         font = "Bookman Old Style")
            # show all on screen
            question_text.draw()
            instr_text.draw()
            slider.draw()
            win.flip()                              
            core.wait(0.1)
            
            # check for key responses
            print("set question & slider - awaiting key responses now!")
            moved_slider = False
            
            while True:
                # show stimuli on screen
                question_text.draw()
                instr_text.draw()
                slider.draw()
                win.flip()
    
                # check for key events
                keys = event.getKeys()
                # if there was a key response...
                if keys:
                    # get the last key that was pressed
                    key = keys[-1]
                    
                    # if esc was pressed, end the experiment:
                    if key == "escape":
                        print("quitting experiment")
                        core.quit()
    
                    # if left arrow key was pressed, move slider button 1 unit to the left
                    elif key == "left":
                        # move slider button
                        slider.markerPos -= 1
                        
                        # keep in mind that participant moved the slider button
                        moved_slider = True
                        
                        # update slider on screen
                        #win.flip() # clear screen before drawing question & slider again
                        core.wait(0.1)
                        question_text.draw()
                        instr_text.draw()
                        slider.draw()
                        win.flip()
                        print("moving slider button to the left")
    
                    # if right arrow key is pressed, move slider button 1 unit to the right
                    elif key == "right":
                        
                        # move slider button
                        slider.markerPos += 1
                        
                        # keep in mind that participant moved the slider button
                        moved_slider = True
                        
                        # update slider on screen
                        #win.flip() # clear screen before drawing question & slider again
                        core.wait(0.1)
                        question_text.draw()
                        instr_text.draw()
                        slider.draw()
                        win.flip()
                        print("moving slider button to the right")
    
                    # if space bar is pressed and participant moved slider, save rating and go to next item
                    elif key == "space" and moved_slider == True:
                        # get slider position aka rating
                        curr_rating = slider.markerPos
                        print("Participant rated " +  curr_item_name +  " as: ", curr_rating)
                        
                        # save data:
                        thisExp.addData('question', curr_item_name)
                        thisExp.addData('chosen_ans', curr_rating)
                        thisExp.addData('text_nr', curr_text_nr)                    
                        thisExp.addData('block_nr', exp_block_counter)
                        thisExp.addData('block_name', curr_block)
                        thisExp.addData('block_kind', curr_nback_cond)
                        # start a new row in the csv
                        thisExp.nextEntry()            
                        
                        # clear window for next item
                        win.flip()
                        # wait for 500 ms before drawing the next item on screen
                        core.wait(0.5)
                        break  # end the while loop
    
    # go to next block!
    exp_block_counter += 1
    print("Going to block " + str(exp_block_counter + 1) + "/17 now!")
    continueRoutine = False
    
    # If there are still blocks left, go to next one.
    # If not, end loop here:
    if exp_block_counter == 17:
        blocks.finished = True
    
    
    # keep track of which components have finished
    difficultyComponents = []
    for thisComponent in difficultyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    difficultyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "difficulty"-------
    while continueRoutine:
        # get current time
        t = difficultyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=difficultyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in difficultyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "difficulty"-------
    for thisComponent in difficultyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "difficulty" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "warning"-------
    continueRoutine = True
    # update component parameters for each repeat
    ### Eyetracker: Run drift correction
    # do_drift_check()
    # --> I think you only have to this once every hour or so, 
    # so doing this after each block would be too much. 
    # My experiment is only 1.5h long or so, so I guess it's 
    # not that important. 
    # More importantly: I think it stops the recording, which I don't want.
    
    
    ### Show warning sign if task changes
    
    # If task in last block (curr_block) is not the same as the next one, show warning.
    
    # To check this, we compare the first letter in the block names.
    # I won't show a warning if it switches from rectangles to words,
    # I think people will notice it's different.
    
    if exp_block_counter < 17: # if there are still blocks left
        if curr_block[0] != all_blocks[exp_block_counter][0]:
    
            # create ImageStim object
            curr_instr_pic = visual.ImageStim(win, 
                                          size = (10, 10),
                                          pos = (0, 0),
                                          image = warning_sign) # set path to image here
    
            # draw image on screen
            curr_instr_pic.draw()
            win.flip()
    
            # Wait for 4 seconds
            core.wait(4)
            win.flip()
    else: print("task in current block", curr_block, "is the same as in next block - skipping warning sign!")
    
    # go to next slide
    continueRoutine = False
    # keep track of which components have finished
    warningComponents = []
    for thisComponent in warningComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    warningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "warning"-------
    while continueRoutine:
        # get current time
        t = warningClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=warningClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in warningComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "warning"-------
    for thisComponent in warningComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "warning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 30.0 repeats of 'blocks'

# get names of stimulus parameters
if blocks.trialList in ([], [None], None):
    params = []
else:
    params = blocks.trialList[0].keys()
# save data for this loop
blocks.saveAsText(filename + 'blocks.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "warning_1"-------
continueRoutine = True
# update component parameters for each repeat
### Show warning sign if task changes

# If task in last block (curr_block) is not the same as the next one, show warning.

# create ImageStim object
curr_instr_pic = visual.ImageStim(win, 
                              size = (10, 10),
                              pos = (0, 0),
                              image = warning_sign) # set path to image here

# draw image on screen
curr_instr_pic.draw()
win.flip()

# Wait for 4 seconds
core.wait(4)
win.flip()

# go to next slide
continueRoutine = False
# keep track of which components have finished
warning_1Components = []
for thisComponent in warning_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
warning_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "warning_1"-------
while continueRoutine:
    # get current time
    t = warning_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=warning_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in warning_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "warning_1"-------
for thisComponent in warning_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "warning_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "vistask_t"-------
continueRoutine = True
# update component parameters for each repeat
##########################################################
#                 VISUAL TASK: TRAINING BLOCK            #
##########################################################

# In this task, we present a new text, but the text proceeds 
# automatically without the participant having to press the Space bar.
# To make sure the words are not presented too fast, 
# we compute the average reading speed per letter and compute "reading speeds" 
# for each word in the new text.

# In both the training & main block, there's no 1-back or 2-back, but we use a 0-back 
# task as a motoric "tapping task", so basically the participants always 
# have to press a certain button if the current word has a certain target colour.
# Target to non-target ratio: 50:250 (16.66% targets just as in the other blocks)
# The target colour is chosen at random from the 4 colours we use in the experiment.

# Put differently: We take the words & the measured reading times for each 
# word all BL main blocks and compute an average reading time / letter. 
# Then we show a new text, using the reading time / letter to generate 
# durations so the text can proceed automatically. 
# Every time a word is shown in a certain target colour (e.g. blue), 
# the participant has to press a button, but there's no real n-back in this block.
# Obviously, the participant will be told which colour is the target colour before each block.


# First things first: Compute average reading time / letter:

# I collected all RTs & words from the Reading_Baseline_main 
# blocks in vis_task_durations and vis_task_words.

# exclude all RTs where participant was way too fast (< 50 ms) or
# way too slow (> 2s), also remove the corresponding words from vis_task_words
print("vis_task_durations:", vis_task_durations)
print("vis_task_words:", vis_task_words)

filtered_durations = []
filtered_words = []
for duration, word in zip(vis_task_durations, vis_task_words):
    if 50 <= duration <= 2000:
        filtered_durations.append(duration)
        filtered_words.append(word)
print("filtered_durations:", filtered_durations)
print("filtered_words:", filtered_words)

# Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
letters_total = sum(len(word) for word in filtered_words)
print("letters_total:", letters_total)
# also get time it took in total to read them all:
reading_time_total = sum(filtered_durations) # in ms

# Now check how many words / min they read on average.
#reading_speed_wpm = words_total / (reading_time_total/60000)
#print("reading speed in words / min:" + str(reading_speed_wpm))

# Check average RT / letter
RT_per_letter = reading_time_total/letters_total
print(RT_per_letter)

# choose 1 target colour & generate 0-back colour list
target_colour = random.choice(colours)

# save this in the output csv:
thisExp.addData('vistask_RT_per_letter', RT_per_letter)
thisExp.addData('vistask_target', target_colour)
thisExp.addData('block_cond', 'None')
thisExp.addData('block_name', 'visual_task_training')

# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# ----------------------------------
 
### VISUAL TASK TRAINING

# Show instructions

# clear buffer of all previously recorded key events:
event.clearEvents()

# create text boxes
instr_text_stim1 = visual.TextStim(win, 
                                  text = locals()["instr_vis_task_1"], 
                                  height = 0.5, # font height: 5° visual angle
                                  font = "Bookman Old Style",
                                  pos = (0, 4), # move instructions up a bit
                                  color = "black")
instr_text_stim2 = visual.TextStim(win, 
                                  text = locals()["instr_vis_task_2"], 
                                  height = 0.5, # font height: 5° visual angle
                                  font = "Bookman Old Style",
                                  pos = (0, -5), # move instructions down a bit
                                  color = "black")
# create "empty" circle as stimulus
instr_colour_circle_stim = visual.Circle(win = win,
                                         radius = 1, # radius = 1° visual angle
                                         # colorSpace = "hex",
                                         pos = (0,0)) # move circle slightly down

# set current target colour as colour of circle:
instr_colour_circle_stim.fillColor = target_colour

# display the text & the circle on screen until Space is pressed
while True:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    instr_text_stim1.draw()
    instr_text_stim2.draw()
    instr_colour_circle_stim.draw()
    win.flip()
    # end screen if participant presses space
    if 'space' in event.getKeys():
        break 


### START VISUAL TASK TRAINING

# change background colour: 
# transition from ivory 
# to medium grey 
change_bg_colour(window = win, 
                 start_rgb = light_bg_col,
                 end_rgb = dark_bg_col, 
                 seconds = 2)
# Wait for a brief period of time so bg is set
core.wait(0.8)
# keep background grey
win.setColor(dark_bg_col, colorSpace='rgb')
win.flip()

# clear buffer of all previously recorded key events:
event.clearEvents()


# prepare stimuli:
curr_text_training = ['Einen', 'Augenblick', 'herrschte', 'totale', 'Stille.', 'Man', 'hörte', 'plötzlich', 'die', 'Wellen', 'rauschen', 'und', 'das', 'Radio', 'aus', 'dem', 'Salon', 'herüberjazzen,', 'man', 'vernahm', 'jeden', 'Schritt', 'vom', 'Promenadendeck', 'und', 'das', 'leise,', 'feine', 'Sausen', 'des', 'Winds,', 'der', 'durch', 'die', 'Fugen', 'der', 'Fenster', 'fuhr.', 'Keiner', 'von', 'uns', 'atmete,', 'es', 'war', 'zu', 'plötzlich', 'gekommen', 'und', 'wir', 'alle', 'noch', 'geradezu', 'erschrocken', 'über', 'das', 'Unwahrscheinliche,', 'dass', 'dieser', 'Unbekannte', 'dem', 'Weltmeister', 'in', 'einer', 'schon', 'halb', 'verlorenen', 'Partie', 'seinen', 'Willen', 'aufgezwungen', 'haben', 'sollte.', 'McConnor', 'lehnte', 'sich', 'mit', 'einem', 'Ruck', 'zurück,', 'der', 'zurückgehaltene', 'Atem', 'fuhr', 'ihm', 'hörbar', 'in', 'einem', 'beglückten', "\"Ah!\"", 'von', 'den', 'Lippen.', 'Ich', 'wiederum', 'beobachtete', 'Czentovic.', 'Schon', 'bei', 'den', 'letzten', 'Zügen', 'hatte', 'mir', 'geschienen,', 'als', 'ob', 'er', 'blässer', 'geworden', 'sei.', 'Aber', 'er','verstand', 'sich', 'gut', 'zusammenzuhalten.', 'Er', 'verharrte', 'in', 'seiner', 'scheinbar', 'gleichmütigen', 'Starre', 'und', 'fragte', 'nur', 'in', 'lässigster', 'Weise,', 'während', 'er', 'die', 'Figuren', 'mit', 'ruhiger', 'Hand', 'vom', 'Brette', 'schob:', "\"Wünschen", 'die', 'Herren', 'noch', 'eine', 'dritte', 'Partie?\"']

# compute RTs using patrticipant's average reading speed / letter
curr_durations_training = [len(word) * RT_per_letter for word in curr_text_training] # in ms
# print(curr_durations_training)

# generate random colour list:
curr_colours_training = create_0back_stimlist(target_colour = target_colour, nr_targets = 25, colour_codes = colours, nr_words = len(curr_text_training))

# save position of targets as True/False list:
curr_targets_training = [colour == target_colour for colour in curr_colours_training]



start_block_instr = visual.TextStim(win = win, 
                                text = "Der Block startet in 10 Sekunden. Bitte schauen Sie solange auf das Fixationskreuz.", 
                                pos = (0,0), 
                                color = "white", 
                                height = 0.5, 
                                wrapWidth = 1600)
# CREATE CLOCK:
my_block_clock = core.Clock()
my_block_clock.reset() # start block clock

while my_block_clock.getTime() < 3: 
    start_block_instr.draw()
    win.flip()
    if event.getKeys(['space']):
        break
win.flip()

# show fixation cross for 10 seconds
fix_cross = visual.TextStim(win = win, 
                         text = "+", 
                         pos = (0,0), 
                         color = "black", 
                         height = 1, 
                         wrapWidth = 1600)
                         
my_block_clock.reset() # start block clock

while my_block_clock.getTime() < 10: 
    fix_cross.draw()
    win.flip()
    if event.getKeys(['escape']):
        break
win.flip() # clear screen again



### prepare flicker
# hint: flicker_freq and frame_rate are set in the settings 
# code component at the beginning of the experiment.

# create flicker phase variable - start at phase = 0
flicker_phase = 0
# we also need the start time (let's set it as current time 
# at this point in the script):
#start_time = core.getTime()

# CREATE CLOCKS: 
my_block_clock = core.Clock()
my_block_clock.reset() # start block clock
start_time = my_block_clock.getTime() # get start time of block
# also create trial clock
my_trial_clock = core.Clock()

### start block loop

# create empty text stimulus 
stim = visual.TextStim(win = win, 
                       text = " ", 
                       pos = (0,0), # center stimulus
                       font = "Times New Roman",
                       height = 1) # font height = 1° visual angle

# create grey rectangle that masks the text if I set opacity to 1
# --> changing the text opacity directly isn't working: https://discourse.psychopy.org/t/opacity-of-text-stimuli-is-not-updating/11152/7    
stim_mask = visual.Rect(win = win,
                        width = 20, # width = 20° visual angle
                        height = 3, # height = 3° visual angle 
                        pos = (0,0), # center stimulus 
                        opacity = 0, # set opacity to 0 for a start
                        fillColor = dark_bg_col,
                        colorSpace = "rgb")

stim.draw()
stim_mask.draw()
win.flip()

# send block onset trigger
send_trigger("vis_task_training_onset")
core.wait(time_after_trigger)
parallel.setData(0)
core.wait(0.1) #wait 100ms before starting first trial

# loop words in current text
for trial_idx, curr_word in enumerate(curr_text_training):
    #print("current idx: " + str(trial_idx) + ", curr word:" + curr_word)
    
    ### prepare & show current word:
    
    # get current colour
    curr_colour = curr_colours_training[trial_idx]
    # check if it's a target
    curr_target = curr_targets_training[trial_idx]
    
    # get duration for current word
    curr_duration = curr_durations_training[trial_idx]
    
    # get trial number (start counting from 1, so add 1)
    curr_trial_nr = trial_idx + 1

    # set current word & colour as content of text stimulus
    stim.color = curr_colour
    stim.text = curr_word
    
    # Flicker option 1: use sine-wave (gradient) flicker
    # create current opacity value to continue flickering the word
    #frame_time = my_block_clock.getTime() # get current time point (in sec)
    #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
    #opacity = (flicker_intensity + 1) / 2

    # use square-wave (on-off) flicker
    frame_time = my_block_clock.getTime() # get current time point (in sec)
    time_passed = frame_time - start_time # calculate time passed since start
    cycle_duration = 1 / flicker_freq # calculate duration of one flicker cycle
    cycle_passed = time_passed % cycle_duration # calculate time passed in current flicker cycle
    if cycle_passed < cycle_duration / 2: # if in the first half of the cycle
        opacity = 1 # set opacity to 1
    else: # if in the second half of the cycle
        opacity = 0 # set opacity to 0
        
    stim_mask.opacity = opacity
    
    # show word on screen
    stim.draw() # draw word on screen
    stim_mask.draw() # draw mask on screen
    trig_off = False # haven't sent 0 to port yet
    win.callOnFlip(send_trigger, "trial_onset")

    # start trial clock
    my_trial_clock.reset()
    onset_time = core.getTime()

    ### wait for key response until curr_duration is over: 

    # create tracker for 0-back responses for the current trial:
    previous_response = False

    ### start recording responses
    # start while loop that looks for responses
    # --> end while loop only if duration for current word is over
    while my_trial_clock.getTime() < (onset_time + curr_duration):
        
        # if it's time to turn off trigger, do so:
        if my_trial_clock.getTime() <= onset_time + time_after_trigger and trig_off == False:
            parallel.setData(0)
            trig_off = True
            
        #print("curr time stamp:", core.getTime())
        # in each iteration, draw word on screen
        # --> flicker again

        # Flicker option 1: use sine-wave (gradient) flicker
        #frame_time = my_block_clock.getTime() 
        #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
        #opacity = (flicker_intensity + 1) / 2

        # Flicker option 2: use square-wave (on-off) flicker
        frame_time = my_block_clock.getTime() 
        time_passed = frame_time - start_time 
        cycle_duration = 1 / flicker_freq
        cycle_passed = time_passed % cycle_duration
        if cycle_passed < cycle_duration / 2:
            opacity = 1
        else: 
            opacity = 0
            
        stim_mask.opacity = opacity
        
        stim.draw()
        stim_mask.draw()
        win.flip()
        
        # check if there were responses:
        keys = event.getKeys(['c', 'escape'])
        
        # if there were, check responses:
        for key in keys:
            
            # if participant pressed button "c" and hasn't already responded in the current trial
            if key == 'c' and previous_response == False:
                # get reaction time
                # we measure reaction time from the onset of the current word, even if the target 
                # was the word before (or occurred even earlier). 
                # In such cases we can infer the actual reaction times from the df later.
                # Reason why I don't use the last target as an onset: Doesn't take into 
                # account that there might be false alarm responses.
                curr_nback_RT = my_trial_clock.getTime() * 1000 
               
                # send trigger to indicate n-back response
                send_trigger("response_target")
                core.wait(time_after_trigger) # wait 3 ms
                parallel.setData(0)
                
                previous_response = True
                
            # If esc is pressed, end the experiment:
            elif key == 'escape':
                et_abort_exp() # shut down eyetrigger and download incremental data
                # close parallel port
                core.wait(time_after_trigger)
                parallel.setData(0)
                core.wait(0.5)
                core.quit()
               
    
    ### end trial
    #print("end trial")
    # stop display of current word & send trial offset trigger
    win.callOnFlip(send_trigger, "trial_offset")
    core.wait(time_after_trigger)
    parallel.setData(0)
    
    # check whether response was hit, miss, false alarm or correct rejection
    # they saw a target and there was one: hit
    if previous_response and curr_target:
        curr_nback_response = "hit"
    # they didn't see a target but there was one: miss
    elif previous_response == False and curr_target:
        curr_nback_response = "miss"
        curr_nback_RT = None
    # they didn't see a target and there was none: correct rejection
    elif previous_response == False and curr_target == False:
        curr_nback_response = "correct rejection"
        curr_nback_RT = None
    # they saw a target but there was none: false alarm
    elif previous_response and curr_target == False:
        curr_nback_response = "false alarm"

    ### End of trial / current word display:
    
    ### save everything in output csv
    thisExp.addData('colour', curr_colour)
    thisExp.addData('target', curr_target)
    thisExp.addData('nback_response', curr_nback_response)
    thisExp.addData('nback_RT', curr_nback_RT) # in ms
    thisExp.addData('duration', curr_duration) # in ms
    thisExp.addData('text_nr', None)
    thisExp.addData('trial_nr', curr_trial_nr)
    thisExp.addData('block_cond', 'None')
    thisExp.addData('block_nr', exp_block_counter)
    thisExp.addData('block_name', 'visual_task_training')
    # careful, make sure to escape quotes in the string 
    # differently before saving in csv file:
    thisExp.addData('word', escape_quotes(curr_word))
    
    # start a new row in the csv
    thisExp.nextEntry()

    ### IF TESTING MODE ENABLED: end loop after 4 trials
    if expInfo['testing_mode'] == "yes":
        if trial_idx == 10:
            break
    
print("finished visual task training block")
# send block offset trigger
send_trigger("block_offset")
core.wait(time_after_trigger) # wait 10 ms
parallel.setData(0)
core.wait(0.1) # wait 100 ms

# change background colour from grey to ivory
change_bg_colour(window = win, 
                 start_rgb = dark_bg_col, 
                 end_rgb = light_bg_col, 
                 seconds = 2)
# Wait for a brief period of time so bg is set
core.wait(0.5)

# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

##########################################################
#            Text Comprehension Questions - Q1           #
##########################################################

### Settings:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# clear buffer of all previously recorded key events:
event.clearEvents()

# get current text nr:
curr_text_nr = vis_task_text_nr

# define first question for current text & their respective answers
Q1 = "Welche Geräusche hören die Figuren aus dem benachbarten Salon kommen?"
Q1_answers = ["1) Musik aus einem Radio", "2) einen lauten Streit", "3) Kinderlachen", "4) einen bellenden Hund"]
Q1_corr = "a"

# Define text positions and formatting
question_pos = (0, 3)
answer_xpos = -7 # move questions a bit to the left 
answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers

# Create text stim for the question:
question = visual.TextStim(win, 
                           text = Q1, 
                           pos = question_pos,
                           color = "black",
                           height = 0.5,
                           font = "Bookman Old Style",
                           anchorHoriz = 'center',
                           alignText = 'center', 
                           wrapWidth = 10)
# create 1 text stim for each answer option:
answers = [visual.TextStim(win, 
                           text = Q1_answers[i], 
                           pos = (answer_xpos, answer_ypos[i]), 
                           color = "black", # set all to black as a default
                           height = 0.5, 
                           font = "Bookman Old Style",
                           wrapWidth = 15,
                           anchorHoriz = 'left', 
                           alignText = 'center') for i in range(len(Q1_answers))]
# set up instruction text
instr_text = visual.TextStim(win, 
                             text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                             color = "grey",
                             pos = (0, -10),
                             wrapWidth = 20,
                             height = 0.4,
                             font = "Bookman Old Style")

### Show all on screen until I set .autoDraw = False
question.autoDraw = True
instr_text.autoDraw = True
for answer in answers:
    answer.autoDraw = True
win.flip()


### Record key responses:
Q1_chosen_ans = None

while True:        
    # if 1 was pressed...
    if event.getKeys(['1']):
        print('a')
        # save Q1 answer as a 
        Q1_chosen_ans = "a"
        # set font colour of the first answer (answer a) to 
        # green and the rest to black:
        answers[0].setColor("green")
        for answer in answers[1:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    # same procedure for all other answer options:
    if event.getKeys(['2']):
        print('b')
        Q1_chosen_ans = "b"
        # set font colour of the second answer (answer b) to 
        # green and the rest to black:
        answers[1].setColor("green")
        for answer in [answers[0]] + answers[2:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    if event.getKeys(['3']):
        print('c')
        Q1_chosen_ans = "c"
        # set font colour of the third answer (answer c) to 
        # green and the rest to black:
        answers[2].setColor("green")
        for answer in answers[:2] + answers[3:]:
            answer.setColor("black")
        # draw updated stimulus:
        win.flip()
    if event.getKeys(['4']):
        print('d')
        Q1_chosen_ans = "d"
        # set font colour of the fourth answer (answer d) to 
        # green and the rest to black:
        answers[3].setColor("green")
        for answer in answers[:-1]:
            answer.setColor("black")
        # draw updated stimulus 
        win.flip()
    # if participant pressed "space", check whether they chose an answer.
    # if yes, end this routine and go to next question, if not, wait for valid answer.
    elif event.getKeys(['space']) and Q1_chosen_ans != None:
        break

# print chosen answer for Q1
print("answer for Q1:" + str(Q1_chosen_ans))

# check if answer was correct:
if Q1_chosen_ans == Q1_corr: 
    print("answer correct!")
else: 
    print("answer incorrect!")
    
# save data:
thisExp.addData('question', 'Q1')
thisExp.addData('chosen_ans', Q1_chosen_ans)
thisExp.addData('ans_correct', Q1_chosen_ans == Q1_corr)
thisExp.addData('text_nr', "vis_task_training")
thisExp.addData('block_nr', exp_block_counter)
thisExp.addData('block_name', "visual_task_training")
thisExp.addData('block_kind', "visual_task_training")
                
# start a new row in the csv
thisExp.nextEntry()

### End Q1: Set .autoDraw = False to stop showing question & answers
question.autoDraw = False
instr_text.autoDraw = False
for answer in answers:
    answer.autoDraw = False

# end current routine
#continueRoutine = False
##########################################################
#            Text Comprehension Questions - Q2           #
##########################################################

### Settings:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# get current text nr:
curr_text_nr = vis_task_text_nr

# load second question for current text & their respective answers
Q2 = "Was tun die Figuren am Anfang des Textes?"
Q2_answers = ["1) jubeln", "2) Jive tanzen", "3) den Atem anhalten", "4) Dart spielen"]
Q2_corr = "c"

# Define text positions and formatting
question_pos = (0, 3)
answer_xpos = -7 # move questions a bit to the left 
answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers

# Create text stim for the question:
question = visual.TextStim(win, 
                           text = Q2, 
                           pos = question_pos,
                           color = "black",
                           height = 0.5,
                           font = "Bookman Old Style",
                           anchorHoriz = 'center',
                           alignText = 'center', 
                           wrapWidth = 10)
# create 1 text stim for each answer option:
answers = [visual.TextStim(win, 
                           text = Q2_answers[i], 
                           pos = (answer_xpos, answer_ypos[i]), 
                           color = "black", # set all to black as a default
                           height = 0.5, 
                           font = "Bookman Old Style",
                           wrapWidth = 15,
                           anchorHoriz = 'left', 
                           alignText = 'center') for i in range(len(Q1_answers))]
# set up instruction text
instr_text = visual.TextStim(win, 
                             text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                             color = "grey",
                             pos = (0, -10),
                             wrapWidth = 20,
                             height = 0.4,
                             font = "Bookman Old Style")
### Show all on screen until I set .autoDraw = False
question.autoDraw = True
instr_text.autoDraw = True
for answer in answers:
    answer.autoDraw = True
win.flip()


### Record key responses:
Q2_chosen_ans = None

while True:        
    # if 1 was pressed...
    if event.getKeys(['1']):
        print('a')
        # save Q2 answer as a 
        Q2_chosen_ans = "a"
        # set font colour of the first answer (answer a) to 
        # green and the rest to black:
        answers[0].setColor("green")
        for answer in answers[1:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    # same procedure for all other answer options:
    if event.getKeys(['2']):
        print('b')
        Q2_chosen_ans = "b"
        # set font colour of the second answer (answer b) to 
        # green and the rest to black:
        answers[1].setColor("green")
        for answer in [answers[0]] + answers[2:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    if event.getKeys(['3']):
        print('c')
        Q2_chosen_ans = "c"
        # set font colour of the third answer (answer c) to 
        # green and the rest to black:
        answers[2].setColor("green")
        for answer in answers[:2] + answers[3:]:
            answer.setColor("black")
        # draw updated stimulus:
        win.flip()
    if event.getKeys(['4']):
        print('d')
        Q2_chosen_ans = "d"
        # set font colour of the fourth answer (answer d) to 
        # green and the rest to black:
        answers[3].setColor("green")
        for answer in answers[:-1]:
            answer.setColor("black")
        # draw updated stimulus 
        win.flip()
    # if participant pressed "space", check whether they chose an answer.
    # if yes, end this routine and go to next question, if not, wait for valid answer.
    elif event.getKeys(['space']) and Q2_chosen_ans != None:
        break

# print chosen answer for Q2
print("answer for Q2:" + str(Q2_chosen_ans))

# check if answer was correct:
if Q2_chosen_ans == Q2_corr: 
    print("answer correct!")
else: 
    print("answer incorrect!")
    
# save data:
thisExp.addData('question', 'Q2')
thisExp.addData('chosen_ans', Q2_chosen_ans)
thisExp.addData('ans_correct', Q2_chosen_ans == Q2_corr)
thisExp.addData('text_nr', curr_text_nr)
thisExp.addData('block_nr', exp_block_counter)
thisExp.addData('block_name', "visual_task_training")
thisExp.addData('block_kind', "visual_task_training")
                
# start a new row in the csv
thisExp.nextEntry()

### End Q2: Set .autoDraw = False to stop showing question & answers
question.autoDraw = False
instr_text.autoDraw = False
for answer in answers:
    answer.autoDraw = False

# end current routine
#continueRoutine = False
##########################################################
#            Text Comprehension Questions - Q3           #
##########################################################

### Settings:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# clear buffer of all previously recorded key events:
event.clearEvents()

# get current text nr:
curr_text_nr = vis_task_text_nr

# set third question for current text & the respective answers
Q3 = "Was fragt Czentovic die umstehenden Herren?"
Q3_answers = ["1) ob sie noch eine Partie spielen wollen", "2) ob sie Interesse an einer Runde Skat haben", "3) ob sie Feuer haben", "4) ob er sie auf einen Drink einladen darf"]
Q3_corr = "a"

# Define text positions and formatting
question_pos = (0, 3)
answer_xpos = -7 # move questions a bit to the left 
answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers

# Create text stim for the question:
question = visual.TextStim(win, 
                           text = Q3, 
                           pos = question_pos,
                           color = "black",
                           height = 0.5,
                           font = "Bookman Old Style",
                           anchorHoriz = 'center',
                           alignText = 'center', 
                           wrapWidth = 10)
# create 1 text stim for each answer option:
answers = [visual.TextStim(win, 
                           text = Q3_answers[i], 
                           pos = (answer_xpos, answer_ypos[i]), 
                           color = "black", # set all to black as a default
                           height = 0.5, 
                           font = "Bookman Old Style",
                           wrapWidth = 15,
                           anchorHoriz = 'left', 
                           alignText = 'center') for i in range(len(Q3_answers))]
# set up instruction text
instr_text = visual.TextStim(win, 
                             text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                             color = "grey",
                             pos = (0, -10),
                             wrapWidth = 20,
                             height = 0.4,
                             font = "Bookman Old Style")
                             
### Show all on screen until I set .autoDraw = False
question.autoDraw = True
instr_text.autoDraw = True
for answer in answers:
    answer.autoDraw = True
win.flip()


### Record key responses:
Q3_chosen_ans = None

while True:        
    # if 1 was pressed...
    if event.getKeys(['1']):
        print('a')
        # save Q3 answer as a 
        Q3_chosen_ans = "a"
        # set font colour of the first answer (answer a) to 
        # green and the rest to black:
        answers[0].setColor("green")
        for answer in answers[1:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    # same procedure for all other answer options:
    if event.getKeys(['2']):
        print('b')
        Q3_chosen_ans = "b"
        # set font colour of the second answer (answer b) to 
        # green and the rest to black:
        answers[1].setColor("green")
        for answer in [answers[0]] + answers[2:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    if event.getKeys(['3']):
        print('c')
        Q3_chosen_ans = "c"
        # set font colour of the third answer (answer c) to 
        # green and the rest to black:
        answers[2].setColor("green")
        for answer in answers[:2] + answers[3:]:
            answer.setColor("black")
        # draw updated stimulus:
        win.flip()
    if event.getKeys(['4']):
        print('d')
        Q3_chosen_ans = "d"
        # set font colour of the fourth answer (answer d) to 
        # green and the rest to black:
        answers[3].setColor("green")
        for answer in answers[:-1]:
            answer.setColor("black")
        # draw updated stimulus 
        win.flip()
    # if participant pressed "space", check whether they chose an answer.
    # if yes, end this routine and go to next question, if not, wait for valid answer.
    elif event.getKeys(['space']) and Q3_chosen_ans != None:
        break

# print chosen answer for Q3
print("answer for Q3:" + str(Q3_chosen_ans))

# check if answer was correct:
if Q3_chosen_ans == Q3_corr: 
    print("answer correct!")
else: 
    print("answer incorrect!")
    
# save data:
thisExp.addData('question', 'Q3')
thisExp.addData('chosen_ans', Q3_chosen_ans)
thisExp.addData('ans_correct', Q3_chosen_ans == Q3_corr)
thisExp.addData('text_nr', curr_text_nr)
thisExp.addData('block_nr', exp_block_counter)
thisExp.addData('block_name', "visual_task_training")
thisExp.addData('block_kind', "visual_task_training")

# start a new row in the csv
thisExp.nextEntry()

### End Q3: Set .autoDraw = False to stop showing question & answers
question.autoDraw = False
instr_text.autoDraw = False
for answer in answers:
    answer.autoDraw = False

# end current routine
#continueRoutine = False
##########################################################
#                 Text Difficulty Rating                 #
##########################################################

### Settings:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# get current text nr:
curr_text_nr = vis_task_text_nr

# create a keyboard object to check if key is currently pressed 
# (not really possible with event.getKey())
kb = keyboard.Keyboard()

# set question texts, item names and labels:
items = ["Wie anstrengend war es für Sie, dem Text zu folgen?", "Wie schwierig fanden Sie den Text inhaltlich?", "Wie verständlich war der Text für Sie?", "Wie sehr mussten Sie sich beim Lesen konzentrieren?", "Wie einfach fanden Sie die Formulierungen im Text?", "Wie interessant fanden Sie den Text?"]
item_names = ["subj_reading_effort1", "subj_text_difficulty", "subj_text_incomprehensibility1", "subj_reading_effort2", "subj_text_incomprehensibility2", "subj_interest_in_text"]
item_labels = [["gar nicht anstrengend", "sehr anstrengend"], ["sehr leicht", "sehr schwierig"], ["sehr verständlich", "gar nicht verständlich"], ["gar nicht", "sehr stark"], ["sehr einfach","sehr schwierig"], ["sehr langweilig","sehr interessant"]]

# loop items
for item_idx, curr_item in enumerate(items):
    print("rating text difficulty – current item: " + item_names[item_idx])

    # clear buffer of all previously recorded key events:
    event.clearEvents()
    
    # get matching labels & name of current item
    curr_item_labels = item_labels[item_idx]
    print("item labels: ", curr_item_labels)
    curr_item_name = item_names[item_idx]
    
    # set up slider
    slider = visual.Slider(win = win,
                           pos = (0, 0), # position of the slider (centered on screen)
                           size = (10, 0.5), # size of the scale
                           labels = curr_item_labels, # labels for the ticks
                           ticks = [0, 100], # make ticks at 0 and 100
                           units = "deg", # unit = viewing angle degrees
                           color = "black", 
                           fillColor = "green", 
                           borderColor = "black", 
                           granularity = 1, # scale step size
                           labelHeight = 0.5, # font size of the labels I guess?
                           font = "Bookman Old Style")
    slider.markerPos = 50  # initial position of slider button

    # set up question text
    question_text = visual.TextStim(win, 
                                    text = curr_item,
                                    color = "black",
                                    pos = (0, 2),
                                    height = 0.6,
                                    font = "Bookman Old Style")
                                        
    # set up instruction text
    instr_text = visual.TextStim(win, 
                                 text = "(Bitte benutzen Sie die Pfeiltasten um den Punkt zu bewegen. Mit der Leertaste können Sie Ihre Bewertung bestätigen.)",
                                 color = "grey",
                                 pos = (0,-3), 
                                 height = 0.4,
                                 font = "Bookman Old Style")
    # show all on screen
    question_text.draw()
    instr_text.draw()
    slider.draw()
    win.flip()                              
    core.wait(0.1)
        
    # check for key responses
    print("set question & slider - awaiting key responses now!")
    moved_slider = False
        
    while True:
        # show stimuli on screen
        question_text.draw()
        instr_text.draw()
        slider.draw()
        win.flip()
        
        # check for key events
        keys = event.getKeys()
        # if there was a key response...
        if keys:
            # get the last key that was pressed
            key = keys[-1]
            
            # if esc was pressed, end the experiment:
            if key == "escape":
                print("quitting experiment")
                core.quit()

            # if left arrow key was pressed, move slider button 1 unit to the left
            elif key == "left":
                # move slider button
                slider.markerPos -= 1
                
                # keep in mind that participant moved the slider button
                moved_slider = True
                    
                # update slider on screen
                core.wait(0.1)
                question_text.draw()
                instr_text.draw()
                slider.draw()
                win.flip()

            # if right arrow key is pressed, move slider button 1 unit to the right
            elif key == "right":
                
                # move slider button
                slider.markerPos += 1
                
                # keep in mind that participant moved the slider button
                moved_slider = True
                
                # update slider on screen
                core.wait(0.1)
                question_text.draw()
                instr_text.draw()
                slider.draw()
                win.flip()
                print("moving slider button to the right")

            # if space bar is pressed and participant moved slider, save rating and go to next item
            elif key == "space" and moved_slider == True:
                # get slider position aka rating
                curr_rating = slider.markerPos
                print("Participant rated " +  curr_item_name +  " as: ", curr_rating)
                
                # save data:
                thisExp.addData('question', curr_item_name)
                thisExp.addData('chosen_ans', curr_rating)
                thisExp.addData('text_nr', curr_text_nr)                    
                thisExp.addData('block_nr', exp_block_counter)
                thisExp.addData('block_name', "visual_task_training")
                thisExp.addData('block_kind', "visual_task_training")
                # start a new row in the csv
                thisExp.nextEntry()            
                
                # clear window for next item
                win.flip()
                # wait for 500 ms before drawing the next item on screen
                core.wait(0.5)
                break  # end the while loop

# go to next block!
exp_block_counter += 1
continueRoutine = False
# keep track of which components have finished
vistask_tComponents = []
for thisComponent in vistask_tComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
vistask_tClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "vistask_t"-------
while continueRoutine:
    # get current time
    t = vistask_tClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=vistask_tClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in vistask_tComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "vistask_t"-------
for thisComponent in vistask_tComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "vistask_t" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "vistask_m"-------
continueRoutine = True
# update component parameters for each repeat
##########################################################
#                 VISUAL TASK: MAIN BLOCK                #
##########################################################

# clear buffer of all previously recorded key events:
event.clearEvents()


### Show instructions
# set instruction text
instr_text = "Instruktionen\n\n\nGut gemacht!\n\nNun folgt ein etwas längerer Hauptblock, die Aufgabe bleibt aber die Gleiche.\n\nBitte drücken Sie die Leertaste, um den Block zu starten."
# create text box
instr_text_stim = visual.TextStim(win, 
                                  text = instr_text, 
                                  height = 0.5, # font height: 5° visual angle
                                  font = "Bookman Old Style",
                                  pos = (0, 0),
                                  color = "black")

# display the instructions on screen
while True:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    instr_text_stim.draw()
    win.flip()
    # end screen if participant presses space
    if 'space' in event.getKeys():
        break 

 
### START VISUAL TASK BLOCK:

### change background colour 
# transition from ivory 
# to medium grey 
change_bg_colour(window = win, 
                 start_rgb = light_bg_col,
                 end_rgb = dark_bg_col, 
                 seconds = 2)
# Wait for a brief period of time so bg is set
core.wait(0.8)
# keep background grey
win.setColor(dark_bg_col, colorSpace='rgb')
win.flip()

# clear buffer of all previously recorded key events:
event.clearEvents()

### prepare stimuli

# get text for vis task main
curr_text_nr = vis_task_text_nr
curr_text = locals()[vis_task_text_nr]

# compute RTs using participant's average reading speed / letter
vis_task_durations = [len(word) * RT_per_letter for word in curr_text] # in ms
# print(vis_task_durations)

# choose 1 target colour & generate 0-back colour list
target_colour = random.choice(colours)
curr_colours = create_0back_stimlist(target_colour = target_colour, nr_targets = 50, colour_codes = colours, nr_words = 300)

# save position of targets as True/False list:
curr_targets = [colour == target_colour for colour in curr_colours]



start_block_instr = visual.TextStim(win = win, 
                                text = "Der Block startet in 10 Sekunden. Bitte schauen Sie solange auf das Fixationskreuz.", 
                                pos = (0,0), 
                                color = "white", 
                                height = 0.5, 
                                wrapWidth = 1600)
# CREATE CLOCK:
my_block_clock = core.Clock()
my_block_clock.reset() # start block clock

while my_block_clock.getTime() < 3: 
    start_block_instr.draw()
    win.flip()
    if event.getKeys(['space']):
        break
win.flip()

# show fixation cross for 10 seconds
fix_cross = visual.TextStim(win = win, 
                         text = "+", 
                         pos = (0,0), 
                         color = "black", 
                         height = 1, 
                         wrapWidth = 1600)
                         
my_block_clock.reset() # start block clock

while my_block_clock.getTime() < 10: 
    fix_cross.draw()
    win.flip()
    if event.getKeys(['escape']):
        break
win.flip() # clear screen again



### prepare flicker
# hint: flicker_freq and frame_rate are set in the settings 
# code component at the beginning of the experiment.

# create flicker phase variable - start at phase = 0
flicker_phase = 0
# we also need the start time (let's set it as current time 
# at this point in the script):
#start_time = core.getTime()

# CREATE CLOCKS: 
my_block_clock = core.Clock()
my_block_clock.reset() # start block clock
start_time = my_block_clock.getTime() # get start time of block
# also create trial clock
my_trial_clock = core.Clock()

### start block loop

# create empty text stimulus 
stim = visual.TextStim(win = win, 
                       text = " ", 
                       pos = (0,0), # center stimulus
                       font = "Times New Roman",
                       height = 1) # font height = 1° visual angle

# create grey rectangle that masks the text if I set opacity to 1
# --> changing the text opacity directly isn't working: https://discourse.psychopy.org/t/opacity-of-text-stimuli-is-not-updating/11152/7    
stim_mask = visual.Rect(win = win,
                        width = 20, # width = 20° visual angle
                        height = 3, # height = 3° visual angle 
                        pos = (0,0), # center stimulus 
                        opacity = 0, # set opacity to 0 for a start
                        fillColor = dark_bg_col,
                        colorSpace = "rgb")

stim.draw()
stim_mask.draw()
win.flip()

# send block onset trigger
send_trigger("vis_task_onset")
core.wait(time_after_trigger)
parallel.setData(0)
core.wait(0.1) # wait 100 ms

# loop words in current text
for trial_idx, curr_word in enumerate(curr_text):
    #print("current idx: " + str(trial_idx) + ", curr word:" + curr_word)
    
    ### prepare & show current word:
    
    # get current colour
    curr_colour = curr_colours[trial_idx]
    # check if it's a target
    curr_target = curr_targets[trial_idx]
    
    # get duration for current word
    curr_duration = vis_task_durations[trial_idx]
    
    # get trial number (start counting from 1, so add 1)
    curr_trial_nr = trial_idx + 1

    # set current word & colour as content of text stimulus
    stim.color = curr_colour
    stim.text = curr_word
    
    # Flicker option 1: use sine-wave (gradient) flicker
    # create current opacity value to continue flickering the word
    #frame_time = my_block_clock.getTime() # get current time point (in sec)
    #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
    #opacity = (flicker_intensity + 1) / 2

    # Flicker option 2: use square-wave (on-off) flicker
    frame_time = my_block_clock.getTime() # get current time point (in sec)
    time_passed = frame_time - start_time # calculate time passed since start
    cycle_duration = 1 / flicker_freq # calculate duration of one flicker cycle
    cycle_passed = time_passed % cycle_duration # calculate time passed in current flicker cycle
    if cycle_passed < cycle_duration / 2: # if in the first half of the cycle
        opacity = 1 # set opacity to 1
    else: # if in the second half of the cycle
        opacity = 0 # set opacity to 0
        
    stim_mask.opacity = opacity
    
    # show word on screen & send trial onset trigger
    stim.draw() # draw word on screen
    stim_mask.draw() # draw mask on screen
    trig_off = False # we haven't sent 0 to port yet   
    win.callOnFlip(send_trigger, "trial_onset")

    # start trial clock & record trial onset time
    my_trial_clock.reset()
    onset_time = my_trial_clock.getTime()

    ### wait for key response until curr_duration is over: 

    # create tracker for 0-back responses for the current trial:
    previous_response = False

    ### start recording responses
    # start while loop that looks for responses
    # --> end while loop only if duration for current word is over
    while my_trial_clock.getTime() < (onset_time + curr_duration):  

        # if it's time to turn off trigger, do so:
        if my_trial_clock.getTime() <= onset_time + time_after_trigger and trig_off == False:
            parallel.setData(0)
            trig_off = True  

        # in each iteration, draw word on screen
        # --> flicker again

        # Flicker option 1: use sine-wave (gradient) flicker
        #frame_time = my_block_clock.getTime() 
        #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
        #opacity = (flicker_intensity + 1) / 2

        # Flicker option 2: use square-wave (on-off) flicker
        frame_time = my_block_clock.getTime() 
        time_passed = frame_time - start_time 
        cycle_duration = 1 / flicker_freq
        cycle_passed = time_passed % cycle_duration
        if cycle_passed < cycle_duration / 2:
            opacity = 1
        else: 
            opacity = 0
            
        stim_mask.opacity = opacity
        
        stim.draw()
        stim_mask.draw()
        win.flip()
        
        # check for key presses
        keys = event.getKeys(['c', 'escape'])
        
        # if there are any key presses recorded:
        if len(keys) > 0:
            
            # if participant pressed button "c" and hasn't already responded in the current trial
            if event.getKeys(['c']) and previous_response == False:
                # get reaction time
                # we measure reaction time from the onset of the current word, even if the target 
                # was the word before (or occurred even earlier). 
                # In such cases we can infer the actual reaction times from the df later.
                # Reason why I don't use the last target as an onset: Doesn't take into 
                # account that there might be false alarm responses.
                curr_nback_RT = my_trial_clock.getTime() * 1000
                
                # send trigger to indicate n-back response
                send_trigger("response_target")
                core.wait(time_after_trigger) # wait 10 ms
                parallel.setData(0)
                
                # only get first target response, we don't care if they press the button more than once in this trial:
                previous_response = True
                #print("detected C key press -- 0-back RT: " + str(curr_nback_RT) + " ms") # * 1000 to convert s to ms
            
            # If esc is pressed, end the experiment:
            elif event.getKeys(['escape']):
                et_abort_exp() # shut down eyetrigger and download incremental data
                # close parallel port
                core.wait(time_after_trigger)
                parallel.setData(0)
                core.wait(0.5)
                core.quit()
        
    ### end trial
    #print("end trial")
    # stop display of current word & send trial offset trigger
    win.callOnFlip(send_trigger, "trial_offset")
    core.wait(time_after_trigger)
    parallel.setData(0)
    
    # check whether response was hit, miss, false alarm or correct rejection
    # they saw a target and there was one: hit
    if previous_response and curr_target:
        curr_nback_response = "hit"
    # they didn't see a target but there was one: miss
    elif previous_response == False and curr_target:
        curr_nback_response = "miss"
        curr_nback_RT = None
    # they didn't see a target and there was none: correct rejection
    elif previous_response == False and curr_target == False:
        curr_nback_response = "correct rejection"
        curr_nback_RT = None
    # they saw a target but there was none: false alarm
    elif previous_response and curr_target == False:
        curr_nback_response = "false alarm"

    ### End of trial / current word display:
    
    ### save everything in output csv
    thisExp.addData('colour', curr_colour)
    thisExp.addData('target', curr_target)
    thisExp.addData('nback_response', curr_nback_response)
    thisExp.addData('nback_RT', curr_nback_RT) # in ms
    thisExp.addData('duration', curr_duration) # in ms
    thisExp.addData('text_nr', curr_text_nr)
    thisExp.addData('trial_nr', curr_trial_nr)
    thisExp.addData('block_cond', 'None')
    thisExp.addData('block_nr', exp_block_counter)
    thisExp.addData('block_name', 'visual_task')
    # careful, make sure quotes in the strings are escaped using a 
    # quote (weird, I know) so it's properly saved in the CSV:
    thisExp.addData('word', escape_quotes(curr_word))
    
    # start a new row in the csv
    thisExp.nextEntry()

    ### IF TESTING MODE ENABLED: end loop after 4 trials
    if expInfo['testing_mode'] == "yes":
        if trial_idx == 3:
            break
            
print("finished visual task block")

# send trigger to indicate block offset
send_trigger("block_offset")
core.wait(time_after_trigger) # wait 3 ms
parallel.setData(0)
core.wait(0.1) # wait 100 ms           

# change background colour from grey to ivory
change_bg_colour(window = win, 
                 start_rgb = dark_bg_col, 
                 end_rgb = light_bg_col, 
                 seconds = 2)
# Wait for a brief period of time so bg is set
core.wait(0.5)

# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()
       
### START VISUAL TASK BLOCK

# clear buffer of all previously recorded key events:
event.clearEvents()


### Show instructions
# set instruction text
instr_text = "Instruktionen\n\n\nGut gemacht!\n\nNun folgt ein etwas längerer Hauptblock, die Aufgabe bleibt aber die Gleiche.\n\nBitte drücken Sie die Leertaste, um den Block zu starten."
# create text box
instr_text_stim = visual.TextStim(win, 
                                  text = instr_text, 
                                  height = 0.5, # font height: 5° visual angle
                                  font = "Bookman Old Style",
                                  pos = (0, 0),
                                  color = "black")

# display the instructions on screen
while True:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    instr_text_stim.draw()
    win.flip()
    # end screen if participant presses space
    if 'space' in event.getKeys():
        break 

 
### START VISUAL TASK BLOCK:

### change background colour 
# transition from ivory 
# to medium grey 
change_bg_colour(window = win, 
                 start_rgb = light_bg_col,
                 end_rgb = dark_bg_col, 
                 seconds = 2)
# Wait for a brief period of time so bg is set
core.wait(0.8)
# keep background grey
win.setColor(dark_bg_col, colorSpace='rgb')
win.flip()

# clear buffer of all previously recorded key events:
event.clearEvents()

### prepare stimuli

# get text for vis task main
curr_text_nr = vis_task_text_nr
curr_text = locals()[vis_task_text_nr]

# compute RTs using participant's average reading speed / letter
vis_task_durations = [len(word) * RT_per_letter for word in curr_text] # in ms
# print(vis_task_durations)

# use the same target_colour as in the training & generate 0-back colour list
print("target colour for vis task main:", target_colour)
curr_colours = create_0back_stimlist(target_colour = target_colour, nr_targets = 50, colour_codes = colours, nr_words = 300)

# save position of targets as True/False list:
curr_targets = [colour == target_colour for colour in curr_colours]


### prepare flicker
# hint: flicker_freq and frame_rate are set in the settings 
# code component at the beginning of the experiment.

# create flicker phase variable - start at phase = 0
flicker_phase = 0
# we also need the start time (let's set it as current time 
# at this point in the script):
#start_time = core.getTime()

# CREATE CLOCKS: 
my_block_clock = core.Clock()
my_block_clock.reset() # start block clock
start_time = my_block_clock.getTime() # get start time of block
# also create trial clock
my_trial_clock = core.Clock()

### start block loop

# create empty text stimulus 
stim = visual.TextStim(win = win, 
                       text = " ", 
                       pos = (0,0), # center stimulus
                       font = "Times New Roman",
                       height = 1) # font height = 1° visual angle

# create grey rectangle that masks the text if I set opacity to 1
# --> changing the text opacity directly isn't working: https://discourse.psychopy.org/t/opacity-of-text-stimuli-is-not-updating/11152/7    
stim_mask = visual.Rect(win = win,
                        width = 20, # width = 20° visual angle
                        height = 3, # height = 3° visual angle 
                        pos = (0,0), # center stimulus 
                        opacity = 0, # set opacity to 0 for a start
                        fillColor = dark_bg_col,
                        colorSpace = "rgb")

stim.draw()
stim_mask.draw()
win.flip()

# send block onset trigger
send_trigger("vis_task_onset")
core.wait(time_after_trigger)
parallel.setData(0)
core.wait(0.1) # wait 100 ms

# loop words in current text
for trial_idx, curr_word in enumerate(curr_text):
    #print("current idx: " + str(trial_idx) + ", curr word:" + curr_word)
    
    ### prepare & show current word:
    
    # get current colour
    curr_colour = curr_colours[trial_idx]
    # check if it's a target
    curr_target = curr_targets[trial_idx]
    
    # get duration for current word
    curr_duration = vis_task_durations[trial_idx]
    
    # get trial number (start counting from 1, so add 1)
    curr_trial_nr = trial_idx + 1

    # set current word & colour as content of text stimulus
    stim.color = curr_colour
    stim.text = curr_word
    
    # Flicker option 1: use sine-wave (gradient) flicker
    # create current opacity value to continue flickering the word
    #frame_time = my_block_clock.getTime() # get current time point (in sec)
    #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
    #opacity = (flicker_intensity + 1) / 2

    # Flicker option 2: use square-wave (on-off) flicker
    frame_time = my_block_clock.getTime() # get current time point (in sec)
    time_passed = frame_time - start_time # calculate time passed since start
    cycle_duration = 1 / flicker_freq # calculate duration of one flicker cycle
    cycle_passed = time_passed % cycle_duration # calculate time passed in current flicker cycle
    if cycle_passed < cycle_duration / 2: # if in the first half of the cycle
        opacity = 1 # set opacity to 1
    else: # if in the second half of the cycle
        opacity = 0 # set opacity to 0
        
    stim_mask.opacity = opacity
    
    # show word on screen & send trial onset trigger
    stim.draw() # draw word on screen
    stim_mask.draw() # draw mask on screen
    trig_off = False # we haven't sent 0 to port yet   
    win.callOnFlip(send_trigger, "trial_onset")

    # start trial clock & record trial onset time
    my_trial_clock.reset()
    onset_time = my_trial_clock.getTime()

    ### wait for key response until curr_duration is over: 

    # create tracker for 0-back responses for the current trial:
    previous_response = False

    ### start recording responses
    # start while loop that looks for responses
    # --> end while loop only if duration for current word is over
    while my_trial_clock.getTime() < (onset_time + curr_duration):  

        # if it's time to turn off trigger, do so:
        if my_trial_clock.getTime() <= onset_time + time_after_trigger and trig_off == False:
            parallel.setData(0)
            trig_off = True  

        # in each iteration, draw word on screen
        # --> flicker again

        # Flicker option 1: use sine-wave (gradient) flicker
        #frame_time = my_block_clock.getTime() 
        #flicker_intensity = np.sin(2 * np.pi * flicker_freq * (frame_time - start_time) + flicker_phase)
        #opacity = (flicker_intensity + 1) / 2

        # Flicker option 2: use square-wave (on-off) flicker
        frame_time = my_block_clock.getTime() 
        time_passed = frame_time - start_time 
        cycle_duration = 1 / flicker_freq
        cycle_passed = time_passed % cycle_duration
        if cycle_passed < cycle_duration / 2:
            opacity = 1
        else: 
            opacity = 0
            
        stim_mask.opacity = opacity
        
        stim.draw()
        stim_mask.draw()
        win.flip()
        
        # check for key presses
        keys = event.getKeys(['c', 'escape'])
        
        # if there are any key presses recorded:
        for key in keys:
            
            # if participant pressed button "c" and hasn't already responded in the current trial
            if key == 'c' and previous_response == False:
                # get reaction time
                # we measure reaction time from the onset of the current word, even if the target 
                # was the word before (or occurred even earlier). 
                # In such cases we can infer the actual reaction times from the df later.
                # Reason why I don't use the last target as an onset: Doesn't take into 
                # account that there might be false alarm responses.
                curr_nback_RT = my_trial_clock.getTime() * 1000 # in ms
                
                # send trigger to indicate n-back response
                send_trigger("response_target")
                core.wait(time_after_trigger) # wait 10 ms
                parallel.setData(0)
                
                # only get first target response, we don't care if they press the button more than once in this trial:
                previous_response = True
                #print("detected C key press -- 0-back RT: " + str(curr_nback_RT) + " ms") # * 1000 to convert s to ms
            
            # If esc is pressed, end the experiment:
            elif key == 'escape':
                et_abort_exp() # shut down eyetrigger and download incremental data
                # close parallel port
                core.wait(time_after_trigger)
                parallel.setData(0)
                core.wait(0.5)
                core.quit()
        
    ### end trial
    #print("end trial")
    # stop display of current word & send trial offset trigger
    win.callOnFlip(send_trigger, "trial_offset")
    core.wait(time_after_trigger)
    parallel.setData(0)
    
    # check whether response was hit, miss, false alarm or correct rejection
    # they saw a target and there was one: hit
    if previous_response and curr_target:
        curr_nback_response = "hit"
    # they didn't see a target but there was one: miss
    elif previous_response == False and curr_target:
        curr_nback_response = "miss"
        curr_nback_RT = None
    # they didn't see a target and there was none: correct rejection
    elif previous_response == False and curr_target == False:
        curr_nback_response = "correct rejection"
        curr_nback_RT = None
    # they saw a target but there was none: false alarm
    elif previous_response and curr_target == False:
        curr_nback_response = "false alarm"

    ### End of trial / current word display:
    
    ### save everything in output csv
    thisExp.addData('colour', curr_colour)
    thisExp.addData('target', curr_target)
    thisExp.addData('nback_response', curr_nback_response)
    thisExp.addData('nback_RT', curr_nback_RT) # in ms
    thisExp.addData('duration', curr_duration) # in ms
    thisExp.addData('text_nr', curr_text_nr)
    thisExp.addData('trial_nr', curr_trial_nr)
    thisExp.addData('block_cond', 'None')
    thisExp.addData('block_nr', exp_block_counter)
    thisExp.addData('block_name', 'visual_task')
    # careful, make sure quotes in the strings are escaped using a 
    # quote (weird, I know) so it's properly saved in the CSV:
    thisExp.addData('word', escape_quotes(curr_word))
    
    # start a new row in the csv
    thisExp.nextEntry()

    ### IF TESTING MODE ENABLED: end loop after 4 trials
    if expInfo['testing_mode'] == "yes":
        if trial_idx == 3:
            break
            
print("finished visual task block")

# send trigger to indicate block offset
send_trigger("block_offset")
core.wait(time_after_trigger) # wait 3 ms
parallel.setData(0)
core.wait(0.1) # wait 100 ms           

# change background colour from grey to ivory
change_bg_colour(window = win, 
                 start_rgb = dark_bg_col, 
                 end_rgb = light_bg_col, 
                 seconds = 2)
# Wait for a brief period of time so bg is set
core.wait(0.5)

# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()
        
# end routine
#continueRoutine = False




##########################################################
#            Text Comprehension Questions - Q1           #
##########################################################

### Settings:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# clear buffer of all previously recorded key events:
event.clearEvents()

# get current text nr:
curr_text_nr = vis_task_text_nr

# load first question for current text & their respective answers
Q1 = locals()[curr_text_nr + "_Q1"]
Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
Q1_corr = locals()[curr_text_nr + "_Q1_corr"]

# Define text positions and formatting
question_pos = (0, 3)
answer_xpos = -7 # move questions a bit to the left 
answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers

# Create text stim for the question:
question = visual.TextStim(win, 
                           text = Q1, 
                           pos = question_pos,
                           color = "black",
                           height = 0.5,
                           font = "Bookman Old Style",
                           anchorHoriz = 'center',
                           alignText = 'center', 
                           wrapWidth = 10)
# create 1 text stim for each answer option:
answers = [visual.TextStim(win, 
                           text = Q1_answers[i], 
                           pos = (answer_xpos, answer_ypos[i]), 
                           color = "black", # set all to black as a default
                           height = 0.5, 
                           font = "Bookman Old Style",
                           wrapWidth = 15,
                           anchorHoriz = 'left', 
                           alignText = 'center') for i in range(len(Q1_answers))]
# set up instruction text
instr_text = visual.TextStim(win, 
                             text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                             color = "grey",
                             pos = (0, -10),
                             wrapWidth = 20,
                             height = 0.4,
                             font = "Bookman Old Style")

### Show all on screen until I set .autoDraw = False
question.autoDraw = True
instr_text.autoDraw = True
for answer in answers:
    answer.autoDraw = True
win.flip()


### Record key responses:
Q1_chosen_ans = None

while True:        
    # if 1 was pressed...
    if event.getKeys(['1']):
        print('a')
        # save Q1 answer as a 
        Q1_chosen_ans = "a"
        # set font colour of the first answer (answer a) to 
        # green and the rest to black:
        answers[0].setColor("green")
        for answer in answers[1:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    # same procedure for all other answer options:
    if event.getKeys(['2']):
        print('b')
        Q1_chosen_ans = "b"
        # set font colour of the second answer (answer b) to 
        # green and the rest to black:
        answers[1].setColor("green")
        for answer in [answers[0]] + answers[2:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    if event.getKeys(['3']):
        print('c')
        Q1_chosen_ans = "c"
        # set font colour of the third answer (answer c) to 
        # green and the rest to black:
        answers[2].setColor("green")
        for answer in answers[:2] + answers[3:]:
            answer.setColor("black")
        # draw updated stimulus:
        win.flip()
    if event.getKeys(['4']):
        print('d')
        Q1_chosen_ans = "d"
        # set font colour of the fourth answer (answer d) to 
        # green and the rest to black:
        answers[3].setColor("green")
        for answer in answers[:-1]:
            answer.setColor("black")
        # draw updated stimulus 
        win.flip()
    # if participant pressed "space", check whether they chose an answer.
    # if yes, end this routine and go to next question, if not, wait for valid answer.
    elif event.getKeys(['space']) and Q1_chosen_ans != None:
        break

# print chosen answer for Q1
print("answer for Q1:" + str(Q1_chosen_ans))

# check if answer was correct:
if Q1_chosen_ans == Q1_corr: 
    print("answer correct!")
else: 
    print("answer incorrect!")
    
# save data:
thisExp.addData('question', 'Q1')
thisExp.addData('chosen_ans', Q1_chosen_ans)
thisExp.addData('ans_correct', Q1_chosen_ans == Q1_corr)
thisExp.addData('text_nr', curr_text_nr)
thisExp.addData('block_nr', exp_block_counter)
thisExp.addData('block_name', "visual_task_main")
thisExp.addData('block_kind', "visual_task_main")
                
# start a new row in the csv
thisExp.nextEntry()

### End Q1: Set .autoDraw = False to stop showing question & answers
question.autoDraw = False
instr_text.autoDraw = False
for answer in answers:
    answer.autoDraw = False

# end current routine
#continueRoutine = False
##########################################################
#            Text Comprehension Questions - Q2           #
##########################################################

### Settings:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# get current text nr:
curr_text_nr = vis_task_text_nr

# load second question for current text & their respective answers
Q2 = locals()[curr_text_nr + "_Q2"]
Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
Q2_corr = locals()[curr_text_nr + "_Q2_corr"]

# Define text positions and formatting
question_pos = (0, 3)
answer_xpos = -7 # move questions a bit to the left 
answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers

# Create text stim for the question:
question = visual.TextStim(win, 
                           text = Q2, 
                           pos = question_pos,
                           color = "black",
                           height = 0.5,
                           font = "Bookman Old Style",
                           anchorHoriz = 'center',
                           alignText = 'center', 
                           wrapWidth = 10)
# create 1 text stim for each answer option:
answers = [visual.TextStim(win, 
                           text = Q2_answers[i], 
                           pos = (answer_xpos, answer_ypos[i]), 
                           color = "black", # set all to black as a default
                           height = 0.5, 
                           font = "Bookman Old Style",
                           wrapWidth = 15,
                           anchorHoriz = 'left', 
                           alignText = 'center') for i in range(len(Q1_answers))]
# set up instruction text
instr_text = visual.TextStim(win, 
                             text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                             color = "grey",
                             pos = (0, -10),
                             wrapWidth = 20,
                             height = 0.4,
                             font = "Bookman Old Style")
### Show all on screen until I set .autoDraw = False
question.autoDraw = True
instr_text.autoDraw = True
for answer in answers:
    answer.autoDraw = True
win.flip()


### Record key responses:
Q2_chosen_ans = None

while True:        
    # if 1 was pressed...
    if event.getKeys(['1']):
        print('a')
        # save Q2 answer as a 
        Q2_chosen_ans = "a"
        # set font colour of the first answer (answer a) to 
        # green and the rest to black:
        answers[0].setColor("green")
        for answer in answers[1:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    # same procedure for all other answer options:
    if event.getKeys(['2']):
        print('b')
        Q2_chosen_ans = "b"
        # set font colour of the second answer (answer b) to 
        # green and the rest to black:
        answers[1].setColor("green")
        for answer in [answers[0]] + answers[2:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    if event.getKeys(['3']):
        print('c')
        Q2_chosen_ans = "c"
        # set font colour of the third answer (answer c) to 
        # green and the rest to black:
        answers[2].setColor("green")
        for answer in answers[:2] + answers[3:]:
            answer.setColor("black")
        # draw updated stimulus:
        win.flip()
    if event.getKeys(['4']):
        print('d')
        Q2_chosen_ans = "d"
        # set font colour of the fourth answer (answer d) to 
        # green and the rest to black:
        answers[3].setColor("green")
        for answer in answers[:-1]:
            answer.setColor("black")
        # draw updated stimulus 
        win.flip()
    # if participant pressed "space", check whether they chose an answer.
    # if yes, end this routine and go to next question, if not, wait for valid answer.
    elif event.getKeys(['space']) and Q2_chosen_ans != None:
        break

# print chosen answer for Q2
print("answer for Q2:" + str(Q2_chosen_ans))

# check if answer was correct:
if Q2_chosen_ans == Q2_corr: 
    print("answer correct!")
else: 
    print("answer incorrect!")
    
# save data:
thisExp.addData('question', 'Q2')
thisExp.addData('chosen_ans', Q2_chosen_ans)
thisExp.addData('ans_correct', Q2_chosen_ans == Q2_corr)
thisExp.addData('text_nr', curr_text_nr)
thisExp.addData('block_nr', exp_block_counter)
thisExp.addData('block_name', "visual_task_main")
thisExp.addData('block_kind', "visual_task_main")
                
# start a new row in the csv
thisExp.nextEntry()

### End Q2: Set .autoDraw = False to stop showing question & answers
question.autoDraw = False
instr_text.autoDraw = False
for answer in answers:
    answer.autoDraw = False

# end current routine
#continueRoutine = False
##########################################################
#            Text Comprehension Questions - Q3           #
##########################################################

### Settings:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# clear buffer of all previously recorded key events:
event.clearEvents()

# get current text nr:
curr_text_nr = vis_task_text_nr

# load third question for current text & their respective answers
Q3 = locals()[curr_text_nr + "_Q3"]
Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
Q3_corr = locals()[curr_text_nr + "_Q3_corr"]

# Define text positions and formatting
question_pos = (0, 3)
answer_xpos = -7 # move questions a bit to the left 
answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers

# Create text stim for the question:
question = visual.TextStim(win, 
                           text = Q3, 
                           pos = question_pos,
                           color = "black",
                           height = 0.5,
                           font = "Bookman Old Style",
                           anchorHoriz = 'center',
                           alignText = 'center', 
                           wrapWidth = 10)
# create 1 text stim for each answer option:
answers = [visual.TextStim(win, 
                           text = Q3_answers[i], 
                           pos = (answer_xpos, answer_ypos[i]), 
                           color = "black", # set all to black as a default
                           height = 0.5, 
                           font = "Bookman Old Style",
                           wrapWidth = 15,
                           anchorHoriz = 'left', 
                           alignText = 'center') for i in range(len(Q3_answers))]
# set up instruction text
instr_text = visual.TextStim(win, 
                             text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                             color = "grey",
                             pos = (0, -10),
                             wrapWidth = 20,
                             height = 0.4,
                             font = "Bookman Old Style")
                             
### Show all on screen until I set .autoDraw = False
question.autoDraw = True
instr_text.autoDraw = True
for answer in answers:
    answer.autoDraw = True
win.flip()


### Record key responses:
Q3_chosen_ans = None

while True:        
    # if 1 was pressed...
    if event.getKeys(['1']):
        print('a')
        # save Q3 answer as a 
        Q3_chosen_ans = "a"
        # set font colour of the first answer (answer a) to 
        # green and the rest to black:
        answers[0].setColor("green")
        for answer in answers[1:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    # same procedure for all other answer options:
    if event.getKeys(['2']):
        print('b')
        Q3_chosen_ans = "b"
        # set font colour of the second answer (answer b) to 
        # green and the rest to black:
        answers[1].setColor("green")
        for answer in [answers[0]] + answers[2:]:
            answer.setColor("black")
            # draw updated stimulus:
            win.flip()
    if event.getKeys(['3']):
        print('c')
        Q3_chosen_ans = "c"
        # set font colour of the third answer (answer c) to 
        # green and the rest to black:
        answers[2].setColor("green")
        for answer in answers[:2] + answers[3:]:
            answer.setColor("black")
        # draw updated stimulus:
        win.flip()
    if event.getKeys(['4']):
        print('d')
        Q3_chosen_ans = "d"
        # set font colour of the fourth answer (answer d) to 
        # green and the rest to black:
        answers[3].setColor("green")
        for answer in answers[:-1]:
            answer.setColor("black")
        # draw updated stimulus 
        win.flip()
    # if participant pressed "space", check whether they chose an answer.
    # if yes, end this routine and go to next question, if not, wait for valid answer.
    elif event.getKeys(['space']) and Q3_chosen_ans != None:
        break

# print chosen answer for Q3
print("answer for Q3:" + str(Q3_chosen_ans))

# check if answer was correct:
if Q3_chosen_ans == Q3_corr: 
    print("answer correct!")
else: 
    print("answer incorrect!")
    
# save data:
thisExp.addData('question', 'Q3')
thisExp.addData('chosen_ans', Q3_chosen_ans)
thisExp.addData('ans_correct', Q3_chosen_ans == Q3_corr)
thisExp.addData('text_nr', curr_text_nr)
thisExp.addData('block_nr', exp_block_counter)
thisExp.addData('block_name', "visual_task_main")
thisExp.addData('block_kind', "visual_task_main")

# start a new row in the csv
thisExp.nextEntry()

### End Q3: Set .autoDraw = False to stop showing question & answers
question.autoDraw = False
instr_text.autoDraw = False
for answer in answers:
    answer.autoDraw = False

# end current routine
#continueRoutine = False
##########################################################
#                 Text Difficulty Rating                 #
##########################################################

### Settings:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# get current text nr:
curr_text_nr = vis_task_text_nr

# create a keyboard object to check if key is currently pressed 
# (not really possible with event.getKey())
kb = keyboard.Keyboard()

# set question texts, item names and labels:
items = ["Wie anstrengend war es für Sie, dem Text zu folgen?", "Wie schwierig fanden Sie den Text inhaltlich?", "Wie verständlich war der Text für Sie?", "Wie sehr mussten Sie sich beim Lesen konzentrieren?", "Wie einfach fanden Sie die Formulierungen im Text?", "Wie interessant fanden Sie den Text?"]
item_names = ["subj_reading_effort1", "subj_text_difficulty", "subj_text_incomprehensibility1", "subj_reading_effort2", "subj_text_incomprehensibility2", "subj_interest_in_text"]
item_labels = [["gar nicht anstrengend", "sehr anstrengend"], ["sehr leicht", "sehr schwierig"], ["sehr verständlich", "gar nicht verständlich"], ["gar nicht", "sehr stark"], ["sehr einfach","sehr schwierig"], ["sehr langweilig","sehr interessant"]]

# loop items
for item_idx, curr_item in enumerate(items):
    print("rating text difficulty – current item: " + item_names[item_idx])

    # clear buffer of all previously recorded key events:
    event.clearEvents()
    
    # get matching labels & name of current item
    curr_item_labels = item_labels[item_idx]
    print("item labels: ", curr_item_labels)
    curr_item_name = item_names[item_idx]
    
    # set up slider
    slider = visual.Slider(win = win,
                           pos = (0, 0), # position of the slider (centered on screen)
                           size = (10, 0.5), # size of the scale
                           labels = curr_item_labels, # labels for the ticks
                           ticks = [0, 100], # make ticks at 0 and 100
                           units = "deg", # unit = viewing angle degrees
                           color = "black", 
                           fillColor = "green", 
                           borderColor = "black", 
                           granularity = 1, # scale step size
                           labelHeight = 0.5, # font size of the labels I guess?
                           font = "Bookman Old Style")
    slider.markerPos = 50  # initial position of slider button

    # set up question text
    question_text = visual.TextStim(win, 
                                    text = curr_item,
                                    color = "black",
                                    pos = (0, 2),
                                    height = 0.6,
                                    font = "Bookman Old Style")
                                        
    # set up instruction text
    instr_text = visual.TextStim(win, 
                                 text = "(Bitte benutzen Sie die Pfeiltasten um den Punkt zu bewegen. Mit der Leertaste können Sie Ihre Bewertung bestätigen.)",
                                 color = "grey",
                                 pos = (0,-3), 
                                 height = 0.4,
                                 font = "Bookman Old Style")
    # show all on screen
    question_text.draw()
    instr_text.draw()
    slider.draw()
    win.flip()                              
    core.wait(0.1)
        
    # check for key responses
    print("set question & slider - awaiting key responses now!")
    moved_slider = False
        
    while True:
        # show stimuli on screen
        question_text.draw()
        instr_text.draw()
        slider.draw()
        win.flip()
        
        # check for key events
        keys = event.getKeys()
        # if there was a key response...
        if keys:
            # get the last key that was pressed
            key = keys[-1]
            
            # if esc was pressed, end the experiment:
            if key == "escape":
                print("quitting experiment")
                core.quit()

            # if left arrow key was pressed, move slider button 1 unit to the left
            elif key == "left":
                # move slider button
                slider.markerPos -= 1
                
                # keep in mind that participant moved the slider button
                moved_slider = True
                    
                # update slider on screen
                core.wait(0.1)
                question_text.draw()
                instr_text.draw()
                slider.draw()
                win.flip()

            # if right arrow key is pressed, move slider button 1 unit to the right
            elif key == "right":
                
                # move slider button
                slider.markerPos += 1
                
                # keep in mind that participant moved the slider button
                moved_slider = True
                
                # update slider on screen
                core.wait(0.1)
                question_text.draw()
                instr_text.draw()
                slider.draw()
                win.flip()
                print("moving slider button to the right")

            # if space bar is pressed and participant moved slider, save rating and go to next item
            elif key == "space" and moved_slider == True:
                # get slider position aka rating
                curr_rating = slider.markerPos
                print("Participant rated " +  curr_item_name +  " as: ", curr_rating)
                
                # save data:
                thisExp.addData('question', curr_item_name)
                thisExp.addData('chosen_ans', curr_rating)
                thisExp.addData('text_nr', curr_text_nr)                    
                thisExp.addData('block_nr', exp_block_counter)
                thisExp.addData('block_name', "visual_task_main")
                thisExp.addData('block_kind', "visual_task_main")
                # start a new row in the csv
                thisExp.nextEntry()            
                
                # clear window for next item
                win.flip()
                # wait for 500 ms before drawing the next item on screen
                core.wait(0.5)
                break  # end the while loop

# go to next block!
exp_block_counter += 1
continueRoutine = False
# keep track of which components have finished
vistask_mComponents = []
for thisComponent in vistask_mComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
vistask_mClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "vistask_m"-------
while continueRoutine:
    # get current time
    t = vistask_mClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=vistask_mClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in vistask_mComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "vistask_m"-------
for thisComponent in vistask_mComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "vistask_m" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "warning_1"-------
continueRoutine = True
# update component parameters for each repeat
### Show warning sign if task changes

# If task in last block (curr_block) is not the same as the next one, show warning.

# create ImageStim object
curr_instr_pic = visual.ImageStim(win, 
                              size = (10, 10),
                              pos = (0, 0),
                              image = warning_sign) # set path to image here

# draw image on screen
curr_instr_pic.draw()
win.flip()

# Wait for 4 seconds
core.wait(4)
win.flip()

# go to next slide
continueRoutine = False
# keep track of which components have finished
warning_1Components = []
for thisComponent in warning_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
warning_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "warning_1"-------
while continueRoutine:
    # get current time
    t = warning_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=warning_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in warning_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "warning_1"-------
for thisComponent in warning_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "warning_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pred_tendency"-------
continueRoutine = True
# update component parameters for each repeat
# TO DO: add block & trial clocks

### Settings for Prediction Tendency Task:

# For testing this in google colab or so:
# import numpy as np
# from matplotlib import pyplot as plt

# pick the right channels here: 
# 7+8 are the in-ear headphone channels, so 5+6 (#34 as used in Sarah's CueCue) 
# could be the loudspeakers?
sound_device = "Analog (7+8) (RME Fireface UC), Windows DirectSound" # 7+8 are the output channels

# for the sounds:
tone_volume = 1 # use full volume and make sure the system volume is
                # set to a value where the tones are played with 40dB
tones = [440, 587, 782, 1043]  # Pure tone frequencies in Hz
#tone_duration = 0.1  # Duration of each pure tone in seconds (each lasted 100 ms)
tone_rate = 3  # Rate of pure tone presentation in Hz
audio_sample_freq = 44100 # 44100 Hz --> audio sampling rate at the lab (according to Frauke)
tones_iti = 1/3
tone_fade = 5e-3


# for the paradigm:
block_trials = 1500  # Number of trials per entropy condition
trigger_ordered = 1
trigger_random = 2


# -------------------------------------------

### Prediction Tendency Task:

### Prepare sound objects for all 4 tones:
tones_objects = {}
for tone_idx, curr_freq in enumerate(tones):
    print("preparing sound object for tone", curr_freq, "- tone index:", tone_idx)
    
    # how many samples do we need for a tone duration of 100 ms?
    num_samples = int(audio_sample_freq * tone_duration)
    
    # build a time array: 
    # build an array of length num_samples and divide it by the audio sampling frequency:
    t = np.arange(0, num_samples) / audio_sample_freq
    
    # OLD: 
    # build a time array: you need the sound duration and the right sampling frequency for your device
    # 1 divided by the sampling rate = duration of a single sample in sec
    #tone_sample_len = 1/audio_sample_freq
    #t = np.arange(0, tone_duration, tone_sample_len)
    
    # generate sine wave:
    sine_wave = np.sin(2*np.pi*curr_freq*t)

    # plot the sine wave
    #plt.plot(t, sine_wave)
    #plt.xlabel('Time (s)')
    #plt.ylabel('Amplitude')
    #plt.show()

    # Apply cosine ramp to "smoothen" the edges of the sound a bit 
    # (I'm not an audio expert as you can tell)
    # We basically gradually turn up the sound, play it for a while,
    # and then decrease the volume again so it doesn't make annoying 
    # clicking noises when it's played.

    # apply cosine ramp:
    # check how many samples we have to use for the fade in/out:
    fade_samples = int(tone_fade * audio_sample_freq)

    # if there are enough, but not too many fade samples,
    # apply cosine ramp to signal
    if fade_samples > 0 and fade_samples < len(sine_wave):
      ramp = np.cos(np.linspace(0, np.pi / 2, fade_samples))
      sine_wave[:fade_samples] *= ramp[::-1]
      sine_wave[-fade_samples:] *= ramp

    # plot the modified sine wave again
    #plt.plot(t, sine_wave)
    #plt.xlabel('Time (s)')
    #plt.ylabel('Amplitude')
    #plt.show()

    print("----------------------")

    # save the sine wave to a temporary audio file
    curr_sound_filename = "sine_wave" + str(curr_freq) + ".wav"
    sf.write(curr_sound_filename, sine_wave, audio_sample_freq)

    # Create a Sound instance using the temporary audio file
    sound = Sound(filename = curr_sound_filename, # the sound file (in .wav format)
                  device   = sound_device, # portaudio device used for playback
                  mul = threshold) # volume multiplier - use threshold we determined earlier in the hearing threshold test or default = 50 attentuation - 40 dB
    
    # OLD:
    # generate sound object for the sound file we built
    #sound = Sound(value = sine_wave,
    #              secs = tone_duration, # duration of sound in seconds
    #              sampleRate = audio_sample_freq,
    #              name = f"tone{tone_idx + 1}", # create a name for the sound for logging
    #              hamming = False, # don't apply filter, we did this before
    #              volume = tone_volume,
    #              loops = 0) # don't repeat sound, play only once
    
    # add the sound to the dict
    tones_objects[f"tone_{curr_freq}"] = sound

print("finished preparing sound objects for prediction tendency task")

# now you can access & play each sound by its name, like this:
#curr_tone = tones_objects["tone_440"]
#curr_tone.play()


# Get the trial sequences for both entropy conditions 
# (both for 1500 tones aka trials)

# randomly choose 2 sequences, 1 ordered & 1 random sequence: 
ordered_row = df_ordered_tone_seqs.sample(n = 1)
random_row = df_random_tone_seqs.sample(n = 1)
# access the values in the random rows, exclude the first value (it's the index of the row): 
ordered_sequence = ordered_row.values[0][1:]
random_sequence = random_row.values[0][1:]

# break them into chunks of about 500 trials 
# (aka 3 blocks per condition aka 6 blocks in total)
# We have 1505 trials in each condition, so 2 of the  blocks will have 505 trials.
ordered_sub1 = ordered_sequence[:500] # 0 - 499
ordered_sub2 = ordered_sequence[500:1000] # 500 - 999
ordered_sub3 = ordered_sequence[1000:] # 1000 - end

random_sub1 = random_sequence[:500] # 0 - 499
random_sub2 = random_sequence[500:1000] # 500 - 999
random_sub3 = random_sequence[1000:] # 1000 - end

# build trigger names for each condition ("random" and "ordered")
ordered_trig1 = ["ordered"]*len(ordered_sub1)
ordered_trig2 = ["ordered"]*len(ordered_sub2)
ordered_trig3 = ["ordered"]*len(ordered_sub3)
random_trig1 = ["random"]*len(random_sub1)
random_trig2 = ["random"]*len(random_sub2)
random_trig3 = ["random"]*len(random_sub3)

# put the smaller lists into a list & shuffle them
task_order_stimuli = [ordered_sub1, ordered_sub2, ordered_sub3, random_sub1, random_sub2, random_sub3]
task_order_trigger = [ordered_trig1, ordered_trig2, ordered_trig3, random_trig1, random_trig2, random_trig3]

# shuffle both in the exact same way using the same seed:
pred_tend_seed = random.randint(1, 100)
random.seed(pred_tend_seed)

random.shuffle(task_order_stimuli)
random.shuffle(task_order_trigger)

# 3010 trials are quite a lot without a break, so include one after the first 3 blocks:
# find out after how many trials the 3rd block ends:
break_idx = len(task_order_stimuli[0]) + len(task_order_stimuli[1]) + len(task_order_stimuli[2])
#print(break_idx) # if we reach this index, include a small break


# flatten the lists so they're not nested anymore:
task_order_stimuli = np.concatenate(task_order_stimuli).ravel().tolist()
task_order_trigger = flatten_list(task_order_trigger)


# choose which of the conditions to play first:
choice = random.choice(["ordered", "random"])


### START PLAYING TASK

# set instruction text
instr_text = "Im folgenden Block wird Ihnen eine längere Tonsequenz vorgespielt (Dauer ca. 8 min).\n\nSie können nebenbei den Film auf dem Laptop schauen, hören Sie aber bitte trotzdem den Tönen zu. \n\n\nDrücken Sie die Leertaste, wenn Sie beginnen möchten."

# create text box
instr_text_stim = visual.TextStim(win, 
                                  text = instr_text, 
                                  height = 0.5, 
                                  pos = (0, 0),
                                  font = "Bookman Old Style",
                                  color = 'black')

# display the text on screen & wait for keypress:
while True:
    instr_text_stim.draw()
    win.flip()
    
    # if space bar is pressed, start second block:
    if event.getKeys(['space']):
        # remove words from screen
        win.flip()
        break # break while loop

# send block onset trigger
#send_trigger("prediction_tendency_task_onset")
#core.wait(time_after_trigger) # wait 3 ms
#parallel.setData(0)
#core.wait(0.1) # wait 100 ms

# CREATE TRIAL CLOCK:
my_trial_clock = core.Clock()

# loop over list first_sequence with all frequencies:
for tone_idx, curr_freq in enumerate(task_order_stimuli):
      
    ### BREAK:
    # if we reached the first trial after the 3rd block, include break:
    if tone_idx == break_idx:
               
        # set instruction text
        instr_text = "Sie können nun eine kurze Pause machen. Drücken Sie die Leertaste, wenn Sie den nächsten Block starten möchten. Bitte hören Sie auch im nächsten Block wieder nur zu."

        # create text box
        instr_text_stim = visual.TextStim(win, 
                                          text = instr_text, 
                                          height = 0.5, 
                                          pos = (0, 0),
                                          font = "Bookman Old Style",
                                          color = 'black')
                                          
        # display the text on screen & wait for keypress:
        while True:
            instr_text_stim.draw()
            win.flip()
            
            # if space bar is pressed, start second block:
            if event.getKeys(['space']):
                # remove words from screen
                win.flip()
                break # break while loop

        print("starting second prediction tendency task block")
        fixation_cross.setAutoDraw(True) # start drawing fixation cross on screen again
        ptb.WaitSecs(0.5) # wait 500 ms before playing the first tone of the next sequence


    ### Block onset/offset triggers
    # check which condition it is currently:
    # if it's the first trial of the task, there were no earlier trials, so 
    # set last_trial_cond as current condition, send block onset trigger and move on.
    if tone_idx == 0:
        last_trial_cond = str(task_order_trigger[tone_idx])
        #print("vis task - starting block of condition" + str(task_order_trigger[tone_idx]) + "now")
        # current block's onset trigger
        send_trigger(str(task_order_trigger[tone_idx]) + "_onset")
        core.wait(time_after_trigger) # wait 3 ms
        parallel.setData(0)
        core.wait(time_after_trigger) # wait 3 ms
      
    # if it's not, check if the condition of the last trial is the same as the current one.
    # If yes, don't do anything, if not, send block offset trigger for the block before, 
    # send block onset trigger for the new one and 
    # update last_trial_cond to current (new) condition.
    elif tone_idx > 0 and last_trial_cond != str(task_order_trigger[tone_idx]):
      #print("vis task - starting block of condition" + str(task_order_trigger[tone_idx]) + "now")
      # old block's offset trigger:
      send_trigger("block_offset")
      core.wait(time_after_trigger) # wait 3 ms
      parallel.setData(0)
      core.wait(time_after_trigger) # wait 3 ms
      
      # current block's onset trigger
      send_trigger(str(task_order_trigger[tone_idx]) + "_onset")
      core.wait(time_after_trigger) # wait 3 ms
      parallel.setData(0)
      core.wait(time_after_trigger) # wait 3 ms
      
      # set new condition as last_trial_cond:
      last_trial_cond = str(task_order_trigger[tone_idx])
    
    
    ### RUN TRIAL:
    # get sound object for current frequency tone
    curr_tone = tones_objects[f"tone_{curr_freq}"]
    
    # send tone onset trigger
    send_trigger("freq_" + str(curr_freq) + "_onset")
    my_trial_clock.reset() # start trial clock
    
    # play sound for 100 ms
    # OLD: curr_tone.play(when = now)  # play the sound immediately
    curr_tone.play()
    
    # send 0 trigger to EEG
    parallel.setData(0)
    
    # wait a bit & send tone offset trigger:
    core.wait(time_after_trigger) # wait 3 ms    
    send_trigger("freq_" + str(curr_freq) + "_offset")
    core.wait(time_after_trigger) # wait again
    parallel.setData(0)
    
    ### save information on current trial in output csv
    # (even if we don't record any behavioral data here)
    thisExp.addData('trial_nr', tone_idx)
    thisExp.addData('block_nr', exp_block_counter)
    thisExp.addData('block_name', "prediction_tendency_task")
    thisExp.addData('block_kind', task_order_trigger[tone_idx])
    thisExp.addData('frequency', curr_freq)
    
    # start a new row in the csv
    thisExp.nextEntry()
        
    # end this loop after 10 tones if testing mode is activated
    if expInfo['testing_mode'] == "yes":
        if tone_idx == 30:
            break
            
    # 1 3Hz cycle = 333.33 ms, so continue waiting until 333.33 ms have 
    # passed since starting the tone before playing the next tone
    core.wait(0.33333 - my_trial_clock.getTime())
    
    #print("------ next tone ------ ")

win.flip() # clear window (although it should be cleared)


# Send end of block trigger:
#core.wait(time_after_trigger) # wait 3 ms
# send block offset trigger
#send_trigger("block_offset")
# wait for 3 ms before sending 0 trigger
#core.wait(time_after_trigger) 
#parallel.setData(0)

# If everything's finished, go to next routine
print(" --- ENDING PREDICTION TENDENCY TASK NOW --- ")
continueRoutine = False


# keep track of which components have finished
pred_tendencyComponents = []
for thisComponent in pred_tendencyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pred_tendencyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pred_tendency"-------
while continueRoutine:
    # get current time
    t = pred_tendencyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pred_tendencyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pred_tendencyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pred_tendency"-------
for thisComponent in pred_tendencyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pred_tendency" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
### END OF EXPERIMENT:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

### Show message
# set text
instr_text = "Geschafft, das Experiment ist zu Ende!\n\nBitte sagen Sie der Versuchsleitung Bescheid.\n\n\n(Bitte Leertaste drücken um Daten zu sichern!)" 

# create text box
instr_text_stim = visual.TextStim(win, 
                                  text = instr_text, 
                                  height = 0.5, # font height: 5° visual angle
                                  font = "Bookman Old Style",
                                  pos = (0, 0),
                                  color = "black")

# display the text on screen until Space is pressed
while True:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    instr_text_stim.draw()
    win.flip()
    # end screen if participant presses space
    if 'space' in event.getKeys():
        
        # send end of experiment trigger:
        core.wait(0.01) # wait 10 ms
        # send trigger
        send_trigger("end_experiment")
        # wait for 10 ms before sending 0 trigger
        core.wait(0.01) 
        parallel.setData(0)
        
        
        ### STOP EYETRACKER:
        
        # wait 500 ms to catch final events before stopping
        pylink.pumpDelay(500)

        # stop recording:
        eyelink.stopRecording()
        
        # put eyetracker into Offline Mode:
        eyelink.setOfflineMode()
        
        # clear eyetracking host PC screen and wait for 500 ms
        el_tracker.sendCommand('clear_screen 0')
        pylink.msecDelay(500)
        
        # close data file:
        el_tracker.closeDataFile()
        
        # print file transfer message:
        print("EDF data is transferring from Eyetracking PC")
        
        # download the EDF data from the Host PC to a local data folder:
        local_edf = os.path.join(expInfo['participant'] + "EL" + ".EDF")
        el_tracker.receiveDataFile(edf_file, local_edf)
        
        # Wait 2s to ensure data isn't lost:
        core.wait(2)  
        
        # close eyetracker:
        el_tracker.close()
        
        # Wait again:
        core.wait(2) 
        
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
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
