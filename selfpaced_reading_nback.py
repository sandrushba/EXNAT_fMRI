#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue Mar 21 09:21:32 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
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
expInfo = {'participant': '', 'session': '001'}
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
    originPath='/Users/merleschuckart/Github/PhD/EXNAT/EEG_study_EXNAT2/selfpaced_reading_nback.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1500, 1000], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "settings_2"
settings_2Clock = core.Clock()
### import packages:

# for setting the output encoding to UTF-8
import sys
# --> if you don't do this, German "Umlaute" can't be displayed correctly:
sys.stdout = open(sys.stdout.fileno(), mode = 'w', encoding = 'utf8', buffering = 1)

# for getting current date & time:
import datetime
# numpy for being able to calculate
import numpy as np
# for random number generator:
import random
# for saving data in csv:
import pandas as pd
# additional timing package (I know we have core.wait, but I also want this one)
import time
# pylsl for pushing triggers to lsl stream:
# from pylsl import StreamInlet, resolve_stream, StreamOutlet, StreamInfo
# for connecting to serial ports:
# import serial


# from my custom scripts...
# import all texts
from EXNAT2_texts_MC_Qs import *
# import some additional functions I wrote for the experiment:
from EXNAT2_study_components import change_bg_colour
from nback_colour_generator import create_nback_stimlist, draw_without_replacement, get_targets

# build little function to flatten nested lists:
def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list
    

### Setup LSL Stream
print("create trigger stream") 
# Create trigger stream:
#global out_marker
#info_marker_stream = StreamInfo('PsychoPyMarkers', 'Marker', 1, 0, 'string')
#out_marker = StreamOutlet(info_marker_stream)
#out_marker.push_sample(["TEST MARKER"])

### Stimulus settings

# set colours you want to use here:
# important: I set the colours "manually" in the trainings, 
# so change them there, too, if you change them here.

colours = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"]
print("Preparing experiment with n-back colours:", colours)

#  #D292F3 = weird lilac with a 2000s vibe
#  #F989A2 = bubblegum pink
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
all_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04", "text_05", "text_06", "text_07", "text_08", "text_09"]
# shuffle text numbers
random.shuffle(all_texts_nrs_list)


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
                  20, 60, 60, 300, 20, 60, 60, 300, # main blocks 1 + trainings & single tasks
                  300, 300, 300, 300, 300, 300] # main blocks 2        
blocks_target_counts = [25, 50, 1, # reading bl blocks + click training
                        5, 10, 10, 50, 5, 10, 10, 50, # main blocks 1 + trainings & single tasks
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

# init trial counter for the whole experiment
exp_trial_counter = 0

# init block counter for the whole experiment
exp_block_counter = 0


################################################

### Prepare information for first trial

#curr_colour = all_colour_lists[exp_block_counter][exp_trial_counter]
#print(curr_colour)
#curr_block_kind = all_block_kinds[exp_block_counter][exp_trial_counter]
#print(curr_block_kind)
#curr_target = all_targets[exp_block_counter][exp_trial_counter]
#print(curr_target)
#curr_text_nr = all_texts_nrs_list[exp_block_counter]
#print(curr_text_nr)
#curr_word = all_texts_list[exp_block_counter][exp_trial_counter]
#print(curr_word)

""" IMPORTANT: """
# Don't forget to set trial counter back to 0 after each main block!
# Don't forget to add 1 to trial_counter after each trial and to block_counter after each block!

print("starting experiment now!")
empty_placeholder = visual.TextStim(win=win, name='empty_placeholder',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instr"
instrClock = core.Clock()
instr_1_1 = visual.TextStim(win=win, name='instr_1_1',
    text='Cheerio cowboy, this is the beginning of a block!',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instr_1_2 = visual.TextStim(win=win, name='instr_1_2',
    text='Please press „Space“ to start the block!',
    font='Open Sans',
    pos=(0, -2), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
resp_1 = keyboard.Keyboard()

# Initialize components for Routine "word"
wordClock = core.Clock()

# Initialize components for Routine "Qs"
QsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Hi, this is a question.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=("a", "b", "c", "d"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)

# Initialize components for Routine "text_rating"
text_ratingClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "settings_2"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
settings_2Components = [empty_placeholder]
for thisComponent in settings_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
settings_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "settings_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = settings_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=settings_2Clock)
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
    for thisComponent in settings_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "settings_2"-------
for thisComponent in settings_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('empty_placeholder.started', empty_placeholder.tStartRefresh)
thisExp.addData('empty_placeholder.stopped', empty_placeholder.tStopRefresh)

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=17.0, method='sequential', 
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
    
    # ------Prepare to start Routine "instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    # set instructions for current block
    resp_1.keys = []
    resp_1.rt = []
    _resp_1_allKeys = []
    # keep track of which components have finished
    instrComponents = [instr_1_1, instr_1_2, resp_1]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_1_1* updates
        if instr_1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_1_1.frameNStart = frameN  # exact frame index
            instr_1_1.tStart = t  # local t and not account for scr refresh
            instr_1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_1_1, 'tStartRefresh')  # time at next scr refresh
            instr_1_1.setAutoDraw(True)
        
        # *instr_1_2* updates
        if instr_1_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            instr_1_2.frameNStart = frameN  # exact frame index
            instr_1_2.tStart = t  # local t and not account for scr refresh
            instr_1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_1_2, 'tStartRefresh')  # time at next scr refresh
            instr_1_2.setAutoDraw(True)
        
        # *resp_1* updates
        waitOnFlip = False
        if resp_1.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            resp_1.frameNStart = frameN  # exact frame index
            resp_1.tStart = t  # local t and not account for scr refresh
            resp_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_1, 'tStartRefresh')  # time at next scr refresh
            resp_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_1.status == STARTED and not waitOnFlip:
            theseKeys = resp_1.getKeys(keyList=['space'], waitRelease=False)
            _resp_1_allKeys.extend(theseKeys)
            if len(_resp_1_allKeys):
                resp_1.keys = _resp_1_allKeys[-1].name  # just the last key pressed
                resp_1.rt = _resp_1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('instr_1_1.started', instr_1_1.tStartRefresh)
    blocks.addData('instr_1_1.stopped', instr_1_1.tStopRefresh)
    blocks.addData('instr_1_2.started', instr_1_2.tStartRefresh)
    blocks.addData('instr_1_2.stopped', instr_1_2.tStopRefresh)
    # check responses
    if resp_1.keys in ['', [], None]:  # No response was made
        resp_1.keys = None
    blocks.addData('resp_1.keys',resp_1.keys)
    if resp_1.keys != None:  # we had a response
        blocks.addData('resp_1.rt', resp_1.rt)
    blocks.addData('resp_1.started', resp_1.tStartRefresh)
    blocks.addData('resp_1.stopped', resp_1.tStopRefresh)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "word"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    #################################################
    #                 Start Block                   #
    #################################################
    
    ### specify settings for the current block
    
    
    ### change background colour 
    # transition from white (RGB: 255, 255, 255)
    # to medium grey (RGB: 128, 128, 128)
    change_bg_colour(window = win, 
                     start_rgb = (255, 255, 255), 
                     end_rgb = (10, 10, 10), 
                     seconds = 2)
    # Wait for a brief period of time so bg is set
    core.wait(0.5)
    
    ### prepare stimuli:
    # get text nr & block kind
    curr_block = all_blocks[exp_block_counter][exp_trial_counter]
    curr_text_nr = all_texts_nrs_list[exp_block_counter]
    
    # get n-back condition:
    curr_nback_cond = curr_block[0] # get first character of block name
    # if it's neither 1 nor 2, it has to be a block without n-back,
    # so set curr_nback_cond to None.
    if curr_nback_cond != 1 and curr_nback_cond != 2:
        curr_nback_cond == None
    # if it is a 1 or a 2, though, set that as current n-back level:
    else:
        curr_nback_cond = int(curr_nback_cond)    
    
    # get list with targets & list with colours
    curr_targets = all_target_lists[exp_block_counter]
    curr_colours = all_colour_lists[exp_block_counter]
    
    # for current text nr, get text whose name = current text nr
    curr_text = locals()[curr_text_nr]
    
    
    
    # start block loop
    print("starting block")
    
    # create empty text stimulus
    stim = visual.TextStim(win = win, 
                           text = '', 
                           pos = (0,0), # center stimulus 
                           height = 2) # font height = 2° visual angle
    
    # loop words in current text
    for trial_idx, curr_word in enumerate(curr_text):
        print("current word: " + curr_word)
        
        # get current colour
        curr_colour = curr_colours[trial_idx]
        curr_target = curr_targets[trial_idx]
        
        # get trial number (start counting from 1, so add 1)
        curr_trial_nr = trial_idx + 1
    
        # show important information in console
        print("word:", curr_word, ", colour: ", curr_colour, " , target: ", str(curr_target), "trial nr: ", str(curr_trial_nr)) 
        
        ### set current word & colour as content of text stimulus
        stim.color = curr_colour
        stim.text = curr_word
        
        ### show word on screen
        stim.draw() # draw word on screen
        win.flip() # update the window to clear the screen and display the word
    
        # send word onset trigger to LSL stream
        marker_text = "block_" + curr_block + "_trial_" + str(curr_trial_nr) + "_" + curr_word + "_" + curr_colour + "_" + str(curr_target)
        #out_marker.push_sample(["WORD_ONSET_" + marker_text])
        
        ### record trial onset time
        onset_time = core.getTime()
        print(onset_time)
        
        
        ### wait for 50 ms
        #while core.getTime() < onset_time + 0.05:
        #    core.wait(0.003) # wait for 3 ms
        #    # draw the stimulus during the waiting period
        #    stim.draw()
        #    win.flip()
        #    print(core.getTime())
    
    
        ### wait for key response: 
        # In blocks with n-back task, participants can press "c" to indicate they saw a target colour and "space" to go to the next word/stimulus.
        # In blocks without n-back task, participants can only press "space" to go to the next word/stimulus.
        
        ### start recording responses
        # start "endless" while loop that looks for responses
        while True:
            
            # in each iteration, draw word on screen
            stim.draw()
            win.flip()
    
            # if participant presses space bar on their keyboard...
            if event.getKeys(['space']):
                # get reaction time
                curr_duration = core.getTime() - onset_time
                ### send trigger to LSL stream to indicate participant wants to go to next word
                marker_text = "block_" + curr_block + "_trial_" + str(curr_trial_nr) + "_" + curr_word + "_" + curr_colour + "_" + str(curr_target)
                #out_marker.push_sample(["REACTION_NEXT_WORD_" + marker_text])
                print("detected space key press -- RT: " + str(curr_duration))
                # break while loop
                break
    
            # if participant pressed button "c" and it's an n-back condition 
            # where they're actually supposed to do that (aka not a reading baseline condition)...
            elif event.getKeys(['c']) and curr_nback_cond != None:
                # get reaction time
                curr_nback_RT = onset_time - core.getTime()
                ### send trigger to LSL stream to indicate n-back response
                marker_text = "block_" + curr_block + "_trial_" + str(curr_trial_nr) + "_" + curr_word + "_" + curr_colour + "_" + str(curr_target)
                #out_marker.push_sample(["NBACK_REACTION_" + marker_text])
                print("detected C key press -- n-back RT: " + str(curr_nback_RT))
            # If esc is pressed, end the experiment:
            elif event.getKeys(['escape']):
                core.quit()
        
        ### end trial
        print("end trial")
        # stop display of current word
        #stim.setAutoDraw(False)  
        win.flip()
        
        # break loop after a few trials (for testing)
        if trial_idx == 3:
            break
        
        ### send word offset trigger to LSL stream
        marker_text = "block_" + curr_block + "_trial_" + str(curr_trial_nr) + "_" + curr_word + "_" + curr_colour + "_" + str(curr_target)
        #out_marker.push_sample(["WORD_OFFSET_" + marker_text])
        
    print("finished presenting trials")
    
    ### Prepare questions
    
    # change background colour from grey (RGB: 10, 10, 10)
    # to white (RGB: 255, 255, 255)
    change_bg_colour(window = win, 
                     start_rgb = (10, 10, 10), 
                     end_rgb = (255, 255, 255), 
                     seconds = 2)
    # Wait for a brief period of time so bg is set
    core.wait(0.1)
    
    # load questions & their respective answers for next screen
    
    # keep track of which components have finished
    wordComponents = []
    for thisComponent in wordComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "word"-------
    while continueRoutine:
        # get current time
        t = wordClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wordClock)
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
        for thisComponent in wordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "word"-------
    for thisComponent in wordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ### send word offset trigger
    
    #pass
    
    #--------------------------------
    
    ### save data for this trial
    
    # get reaction time for this slide
    curr_duration = resp_continue.rt
    curr_target_RT = resp_target.rt
    
    # save everything in output
    exp.addData('word', curr_word)
    exp.addData('colour', curr_colour)
    exp.addData('target', curr_target)
    exp.addData('block_kind', curr_block_kind)
    exp.addData('duration', curr_duration)
    
    # end of trial - move to next line in data output
    #exp.nextEntry()
    
    #--------------------------------
    
    ### prepare next trial
    
    # add 1 to trial counter
    exp_trial_counter = exp_trial_counter + 1
    
    # if there are still words left, prepare stimuli / information for next trial
    if exp_trial_counter > 300:
        curr_colour = all_colour_lists[exp_block_counter][exp_trial_counter]
        curr_block_kind = all_block_kinds[exp_block_counter][exp_trial_counter]
        curr_target = all_targets[exp_block_counter][exp_trial_counter]
        curr_text_nr = all_texts_nrs_list[exp_block_counter]
        curr_word = all_texts_list[exp_block_counter][exp_trial_counter]
    
    
    # the Routine "word" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Qs"-------
    continueRoutine = True
    # update component parameters for each repeat
    # prepare questions
    slider.reset()
    # keep track of which components have finished
    QsComponents = [text, slider]
    for thisComponent in QsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    QsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Qs"-------
    while continueRoutine:
        # get current time
        t = QsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=QsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in QsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Qs"-------
    for thisComponent in QsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('text.started', text.tStartRefresh)
    blocks.addData('text.stopped', text.tStopRefresh)
    blocks.addData('slider.response', slider.getRating())
    blocks.addData('slider.rt', slider.getRT())
    blocks.addData('slider.started', slider.tStartRefresh)
    blocks.addData('slider.stopped', slider.tStopRefresh)
    # the Routine "Qs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "text_rating"-------
    continueRoutine = True
    # update component parameters for each repeat
    # end of the block, so we have to add 1 to the block counter
    # save info on block first
    curr_block_kind = all_block_kinds[exp_block_counter][exp_trial_counter]
    curr_text_nr = all_texts_nrs_list[exp_block_counter]
    
    # now change block counter
    exp_block_counter = exp_block_counter + 1
    # and set trial counter back to 0
    exp_trial_counter = 0
    
    ################################################
    
    # skip this component if the block was not a reading baseline block
    if curr_block != "reading_baseline":
        continueRoutine: False
    # keep track of which components have finished
    text_ratingComponents = []
    for thisComponent in text_ratingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    text_ratingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "text_rating"-------
    while continueRoutine:
        # get current time
        t = text_ratingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=text_ratingClock)
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
        for thisComponent in text_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "text_rating"-------
    for thisComponent in text_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "text_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 17.0 repeats of 'blocks'


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
