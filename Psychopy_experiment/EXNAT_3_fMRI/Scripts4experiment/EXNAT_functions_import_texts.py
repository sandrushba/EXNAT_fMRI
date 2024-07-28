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
            first_trigger_time = globalClock.getTime(format='float')
            trigger_count += 1
            thisExp.addData('TriggerCount', trigger_count)
            thisExp.addData('TriggerTime', first_trigger_time)
            # Start a new row in the csv
            # thisExp.nextEntry()
            print(f"First trigger received at {first_trigger_time}")
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
                                      wrapWidth=1.5)
    # create ImageStim object
    curr_instr_pic = visual.ImageStim(win,
                                      size=(0.8, 0.3),
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
            first_trigger_time = globalClock.getTime(format='float')
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