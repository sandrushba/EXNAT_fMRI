#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Merle Schuckart
Psychopy Version: v2021.2.3
Script Version: March 2023

"""

#############################################
#                 SETTINGS                  #
#############################################

# Import packages: 
print("import packages")

# --> you might have to pip install some of the packages first


from psychopy import visual, gui, core, event, data, logging
from psychopy.hardware import keyboard

# for setting the output encoding to UTF-8
# --> if you don't do this, German "Umlaute" can't be displayed correctly
import sys
sys.stdout = open(sys.stdout.fileno(), mode = 'w', encoding = 'utf8', buffering = 1)
# os for getting/setting working directory:
import os
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

### Set working directory:
# set the working directory to the directory containing the current file
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)


### Import custom packages
# I defined a function for generating colour lists in another script, so import that one, too.
# Also import function for counting n-back targets in stimulus list
from nback_colour_generator import create_nback_stimlist, get_targets

# import other study components I wrote as functions:
from EXNAT2_study_components import multiple_choice, change_bg_colour

# import texts & questions:
from EXNAT2_texts_MC_Qs import *


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

### Setup CSV
print("create columns for csv") 
# Create columns for all information we'd like to save

# col 0: ID
ID = []
# col 1: age
age = []
# col 3: gender
gender = []
# col 4: handedness
handedness = []
# col 5: sender
sender = []
# col 6: block_kind
block_kind = []
# col 7: text_nr
text_nr = []
# col 8: duration
duration = []
# col 9: word
word = []
# col 10: colour
colour = []
# col 11: target
target = []
# col 12: nback_response
nback_response = []
# col 13: nback_RT
nback_RT = []
# col 14: trial_nr
trial_nr = []
# col 15: block_nr
block_nr = []
# col 16: Q1
Q1 = []
# col 17: Q2
Q2 = []
# col 18: Q3
Q3 = []
# col 19: subj_reading_effort1
subj_reading_effort1 = []
# col 20: subj_reading_effort2
subj_reading_effort2 = []
# col 21: subj_text_difficulty
subj_text_difficulty = []
# col 22: subj_text_incomprehensibility1
subj_text_incomprehensibility1 = []
# col 23: subj_text_incomprehensibility2
subj_text_incomprehensibility2 = []
# col 24: subj_interest_in_text
subj_interest_in_text = []

########## Demographics - Get user input ####################

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'EXNAT2_EEG_study' 

# get information from user (participant)
print("get user input (demographics") 
expInfo = {'Versuchspersonen-Code': '', 
           'Alter': '', 
           'Geschlecht': 'w', 
           'Händigkeit': 'r'}
dlg = gui.DlgFromDict(dictionary = expInfo, sortKeys = False, title = expName)
# if participant clicked "cancel", end experiment
if dlg.OK == False:
    core.quit()

# If everything's fine, proceed: Push information to LSL.
# In this new LSL stream called "Demographics", we have 7 channels, each channel containing a string (
# = our demographical data and a few additional information on the dataset)
#demogr_info = pylsl.StreamInfo('Demographics', 'DemographicsData', 7, 0, pylsl.cf_string)
#demogr_outlet = pylsl.StreamOutlet(demogr_info)
#demogr_data = ['Participant ID: ' + exp_info['Versuchspersonen-Code'] , 
#               'Age: ' + exp_info['Alter'], 
#               'Gender: ' + exp_info['Geschlecht'], 
#               'Handedness: ' + exp_info['Händigkeit'], 
#               'Native Language: German',
#               'Vision: corrected or corrected to normal',
#               'Date & time of recording' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")]
#demogr_outlet.push_sample(demogr_data)


# add time stamp, exp name and psychopy version
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Versuchspersonen-Code'], expName, expInfo['date'])

### Other setup stuff:
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/merleschuckart/Github/PhD/EXNAT/EEG_study_EXNAT2/code study from scratch/EXNAT2_EEG_study.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
    
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame



############# Experiment Settings ##############################

###### set up window for experiment ############################
print("set up window for experiment") 
#global win
#out_marker.push_sample(["start"])

# Setup the Window
win = visual.Window(size=[1500, 1000], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
    
# store frame rate of monitor if we can measure it
# --> if frame rate can't be measured, set to 60 Hz as default
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
#ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()


### Set response keys 
print("set response keys") 
# make sure there are no key events defined so we start with a clean slate
event.globalKeys.clear()


### Set Colours 
print("set colours") 
#global colours 
colours = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"]
#  #D292F3 = weird lilac with a 2000s vibe
#  #F989A2 = bubblegum pink
#  #2AB7EF = Twitter blue
#  #88BA3F = medium grass green
# (#D8A244 = dark curry-ish yellow --> excluded!)

# All colours have a luminance of 70 and a chroma of 74.

# The colours are selected for distinguishability (is that a word?!) 
# for people with "normal" colour vision as well as for 
# people with protanomaly (red olour vision deficiency (CVD)), 
# deuteranomaly (green CVD) and tritanomaly (blue CVD).
        
# People with a "true" colour blindness 
# (i.e. protanopia, deuteranopia, tritanopia)
# shouldn't participate in this study.


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


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#############################################
#             START EXPERIMENT              #
#############################################
print("starting experiment now")
# create block counter
block_counter = 0










# create a window to display the form
win = visual.Window(size=(800, 600), fullscr=False)

# define the questions and answer options
questions = [
    {'question': 'What is the capital of France?', 'options': ['Madrid', 'Paris', 'Berlin', 'Rome'], 'answer': 1},
    {'question': 'What is the largest planet in our solar system?', 'options': ['Jupiter', 'Venus', 'Mars', 'Mercury'], 'answer': 0},
    {'question': 'Who is the author of "To Kill a Mockingbird"?', 'options': ['Harper Lee', 'John Steinbeck', 'Ernest Hemingway', 'F. Scott Fitzgerald'], 'answer': 0},
    {'question': 'What is the tallest mammal in the world?', 'options': ['Elephant', 'Giraffe', 'Hippopotamus', 'Rhino'], 'answer': 1}
]

# shuffle the order of the questions and answer options
random.shuffle(questions)
for q in questions:
    random.shuffle(q['options'])

# create the form
form = visual.Form(win = win,
                   items = [visual.TextStim(win, text = q['question'], pos = (0, 0.5)) for q in questions] + 
                           [visual.RadioButtons(win, choices = q['options'], pos = (0, i*0.25-0.5)) for i, q in enumerate(questions)] + 
                           [visual.ButtonStim(win, text = 'Auswahl bestätigen', pos = (0, -0.9))])

# display the form and collect user responses
while True:
    form.draw()
    win.flip()

    if form.items[-1].pressed:
        break

# check the answers and display the user's score
score = 0
for i, q in enumerate(questions):
    if form.items[i+1].getRating() == q['answer']:
        score += 1

visual.TextStim(win, text=f'Sie haben {score}/{len(questions)} Fragen korrekt beantwortet!', pos=(0, 0)).draw()
win.flip()

# wait for a key press to exit
event.waitKeys()
win.close()











#####################################################
#                READING BL TRAINING                #
#####################################################

# set background colour to white
win.color = 'white' 
win.flip()

# define TextStim object and add heading for instructions as text

instr_text = visual.TextStim(win, 
                             text = "", 
                             pos = (0, 0), 
                             color = 'black', 
                             height = 1)

# Add instruction text to the same TextStim object
instr_text.text += "Hi, this is the instruction for the reading BL training.\n\n" \
                   "Please press space to go to the next word.\n\n" \
                   "There will be 3 MC questions after the block, so make sure to read the text carefully.\n\n" \
                   "Please press Space to start the block!\n\n"

# show the instructions on screen
instr_text.draw()
win.flip()

# show text until participant pressed Space to start block:
event.waitKeys(keyList=["space"])


#### Start block: 

# count trials
trial_counter = 0

# change background colour from white (RGB: 255, 255, 255)
# to medium grey (RGB: 128, 128, 128)
change_bg_colour(window = win, 
                 start_rgb = (255, 255, 255), 
                 end_rgb = (10, 10, 10), 
                 seconds = 2)
# Wait for a brief period of time so bg is set
core.wait(0.1)

# prepare text:
# the training text is the first paragraph of the novel "Die Schachnovelle" by Stefan Zweig
curr_text = ["Auf", "dem", "großen", "Passagierdampfer,", "der", "um", "Mitternacht", "von", "New", "York", "nach", "Buenos", "Aires", "abgehen", "sollte,", "herrschte", "die", "übliche", "Geschäftigkeit", "und", "Bewegung", "der", "letzten", "Stunde.", "Gäste", "vom", "Land", "drängten", "durcheinander,", "um", "ihren", "Freunden", "das", "Geleit", "zu", "geben,", "Telegraphenboys", "mit", "schiefen", "Mützen", "schossen", "Namen", "ausrufend", "durch", "die", "Gesellschaftsräume,", "Koffer", "und", "Blumen", "wurden", "geschleppt,", "Kinder", "liefen", "neugierig", "treppauf", "und", "treppab,", "während", "das", "Orchester", "unerschütterlich", "zur", "Deckshow", "spielte.", "Ich", "stand", "im", "Gespräch", "mit", "einem", "Bekannten", "etwas", "abseits", "von", "diesem", "Getümmel", "auf", "dem", "Promenadendeck,", "als", "neben", "uns", "zwei-", "oder", "dreimal", "Blitzlicht", "scharf", "aufsprühte", "-", "anscheinend", "war", "irgendein", "Prominenter", "knapp", "vor", "der", "Abfahrt", "noch", "rasch", "von", "Reportern", "interviewt", "und", "photographiert", "worden.", "Mein", "Freund", "blickte", "hin", "und", "lächelte.", "\"Sie", "haben", "da", "einen", "raren", "Vogel", "an", "Bord,", "den", "Czentovic.\"", "Und", "da", "ich", "offenbar", "ein", "ziemlich", "verständnisloses", "Gesicht", "zu", "dieser", "Mitteilung", "machte,", "fügte", "er", "erklärend", "bei:", "\"Mirko", "Czentovic,", "der", "Weltschachmeister.", "Er", "hat", "ganz", "Amerika", "von", "Ost", "nach", "West", "mit", "Turnierspielen", "abgeklappert", "und", "fährt", "jetzt", "zu", "neuen", "Triumphen", "nach", "Argentinien.\""]
curr_text_nr = "training_text"

# prepare questions:
curr_Q1 = "Wo befinden sich die Personen im Text?"
curr_Q1_ans = ["auf einem Schiff","in einem Flugzeug", "in einem Zug", "in einem Bus"]
curr_Q1_corr = ["TRUE_a", "b", "c", "d"]

curr_Q2 = "Wohin geht ihre Reise?"
curr_Q2_ans = ["Caracas (Venezuela)","Lima (Peru)", "Buenos Aires (Argentinien)", "Manaus (Brasilien)"]
curr_Q2_corr = ["a", "b", "TRUE_c", "d"]

curr_Q3 = "Einer der Reisenden hat einen ungewöhnlichen Beruf. Welchen?"
curr_Q3_ans = ["Schachspieler","Dressurreiter", "Trickbetrüger", "Diamantenhändler"]
curr_Q3_corr = ["TRUE_a", "b", "c", "d"]

# prepare colours
curr_colours = all_colour_lists[block_counter]

# prepare targets
# (no targets here because we don't have an n-back)
curr_targets = [False] * len(curr_text) 

# get n-back condition:
curr_nback_cond = all_blocks[block_counter][0]
if curr_nback_cond != 1 and curr_nback_cond != 2:
    curr_nback_cond == None
else:
    curr_nback_cond = int(curr_nback_cond)
    
print("current nback condition: " + str(curr_nback_cond))


# Present trials
# - loop words & their indices
# - show each word on screen for 50 ms (about 3 frames)
# - after 50 ms, record key presses
# - record RT & go to next iteration (aka word) if "space" is pressed,
#   only record RT and wait for "space" to be pressed if "c" is pressed.
print("starting block " + all_blocks[block_counter])

for word_idx, word in enumerate(text_02):

    ### settings

    # create empty text stimulus
    stim = visual.TextStim(win = win, 
                           text = '', 
                           pos = (0,0), # center stimulus 
                           height = 2) # font height = 2° visual angle

    # reading BL block, so no trial is a target trial:
    curr_target = False
    
    # get colour for current trial & set as font colour
    curr_colour = curr_colours[trial_counter]
    print(curr_colour)
    print(word)
    stim.color = curr_colour
    
    # set current word
    stim.text = word # set word in text stimulus
    
    ### show word on screen
    stim.draw() # draw word on screen
    win.flip() # update the window to clear the screen and display the word

    ### send word onset trigger to LSL stream
    marker_text = "block_" + all_blocks[block_counter] + "_trial_" + str(trial_counter) + "_" + word + "_" + curr_colour + "_" + str(curr_target)
    #out_marker.push_sample(["WORD_ONSET_" + marker_text])
    
    ### record trial onset time
    onset_time = core.getTime()
    print(onset_time)
    # wait for 50 ms
    #while core.getTime() < onset_time + 0.05:
    #    core.wait(0.003) # wait for 3 ms
    #    # draw the stimulus during the waiting period
    #    stim.draw()
    #    win.flip()
    #    print(core.getTime())
        
    ### start recording responses
    # start "endless" while loop that looks for responses
    while True:
        # in each iteration, draw word on screen
        stim.draw()
        win.flip()
        # if participant presses space bar on their keyboard...
        if event.getKeys(['space']):
            # get reaction time
            curr_duration = onset_time - core.getTime()
            ### send trigger to LSL stream to indicate participant wants to go to next word
            marker_text = "block_" + all_blocks[block_counter] + "_trial_" + str(trial_counter) + "_" + word + "_" + curr_colour + "_" + str(curr_target)
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
            marker_text = "block_" + all_blocks[block_counter] + "_trial_" + str(trial_counter) + "_" + word + "_" + curr_colour + "_" + str(curr_target)
            #out_marker.push_sample(["NBACK_REACTION_" + marker_text])
            print("detected C key press -- n-back RT: " + str(curr_nback_RT))
        # If esc is pressed, end the experiment:
        elif event.getKeys(['escape']):
            core.quit()

    ### end trial
    print("end trial")
    # increase trial counter
    trial_counter += 1
    
    # stop display of current word
    #stim.setAutoDraw(False)  
    win.flip()

    ### send word offset trigger to LSL stream
    marker_text = "block_" + all_blocks[block_counter] + "_trial_" + str(trial_counter) + "_" + word + "_" + curr_colour + "_" + str(curr_target)
    #out_marker.push_sample(["WORD_OFFSET_" + marker_text])
    
    
print("finished presenting trials")

### Show Questions

# change background colour from grey (RGB: 10, 10, 10)
# to white (RGB: 255, 255, 255)
change_bg_colour(window = win, 
                 start_rgb = (10, 10, 10), 
                 end_rgb = (255, 255, 255), 
                 seconds = 2)
# Wait for a brief period of time so bg is set
core.wait(0.1)


print("showing MC questions now")









print("finished showing MC questions")
# go to next block 
block_counter += 1
print("finished block")






#####################################################
#                  READING BL MAIN                  #
#####################################################

# reset trial counter
trial_counter = 0

# Prepare questions for Reading BL main:
# get number of current text, then get 
# corresponding text, questions and answers
#curr_text_nr = all_texts_nrs_list[block_counter]

#curr_text = locals()[curr_text_nr]
#curr_Q1 = locals()[curr_text_nr + "_Q1"]
#curr_Q2 = locals()[curr_text_nr + "_Q2"]
#curr_Q3 = locals()[curr_text_nr + "_Q3"]
#curr_Q1_ans  = locals()[curr_text_nr + "_Q1_ans"]
#curr_Q2_ans  = locals()[curr_text_nr + "_Q2_ans"]
#curr_Q3_ans  = locals()[curr_text_nr + "_Q3_ans"]
#curr_Q1_corr = locals()[curr_text_nr + "_Q1_corr"]
#curr_Q2_corr = locals()[curr_text_nr + "_Q2_corr"]
#curr_Q3_corr = locals()[curr_text_nr + "_Q3_corr"]

# get colours
#curr_colours = pass
# no targets because there's no no-back here:
#curr_targets = [False] * len(curr_text)


#####################################################
#                  END EXPERIMENT                   #
#####################################################


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
