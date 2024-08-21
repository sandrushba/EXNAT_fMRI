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
# math package for log function
import math

# Button box set-up
# Import serial for button box
import serial
# Initialize serial connection
ser = serial.Serial('/dev/ttyUSB0', 19200)


# Get functions from my custom scripts:
# import all texts
from EXNAT3_training_texts_MC_Qs import instr_pic_path, instr_Reading_Baseline_training_click, \
    instr_pic_Reading_Baseline_training_click, instr_Reading_pseudotext_no_click, instr_Reading_Baseline_main_click, \
    instr_pic_Reading_Baseline_main_click, instr_Reading_Baseline_main_no_click, instr_click_training, \
    instr_pic_click_training, instr_0back_single_training1, instr_0back_single_training2, instr_pic_0back, instr_0back_dual_main_click1, instr_0back_dual_main_click2, instr_0back_dual_main_no_click1, instr_0back_dual_main_no_click2, instr_1back_single_training1, instr_pic_1back_single_training1, \
    instr_1back_single_training2, instr_pic_1back_single_training2, instr_1back_single_main, \
    instr_pic_1back_single_main, instr_1back_single_main_no_click, instr_pic_1back_single_main_no_click, instr_1back_dual_main_click, instr_pic_1back_dual_main_click, \
    instr_1back_dual_main_no_click, instr_2back_single_training1, instr_pic_2back_single_training1, \
    instr_2back_single_training2, instr_pic_2back_single_training2, instr_2back_single_main, \
    instr_pic_2back_single_main, instr_2back_single_main_no_click, instr_pic_2back_single_main_no_click, instr_2back_dual_main_click, instr_pic_2back_dual_main_click, \
    instr_2back_dual_main_no_click, instr_Reading_Baseline_training_no_click, instr_pic_1back_dual_main_no_click, \
    instr_pic_2back_dual_main_no_click, warning_sign, reading_bl_tr_text, reading_bl_tr_Q1, reading_bl_tr_Q1_ans, \
    reading_bl_tr_Q1_corr, reading_bl_tr_Q2, reading_bl_tr_Q2_ans, reading_bl_tr_Q2_corr, reading_bl_tr_Q3, \
    reading_bl_tr_Q3_ans, reading_bl_tr_Q3_corr, reading_bl_tr_text_no_click, reading_bl_tr_no_click_Q1, \
    reading_bl_tr_no_click_Q1_ans, reading_bl_tr_no_click_Q1_corr, reading_bl_tr_no_click_Q2, \
    reading_bl_tr_no_click_Q2_ans, reading_bl_tr_no_click_Q2_corr, reading_bl_tr_no_click_Q3, \
    reading_bl_tr_no_click_Q3_ans, reading_bl_tr_no_click_Q3_corr, text_01, text_01_Q1, text_01_Q1_ans, text_01_Q1_corr, \
    text_01_Q2, text_01_Q2_ans, text_01_Q2_corr, text_01_Q3, text_01_Q3_ans, text_01_Q3_corr, text_02, text_02_Q1, \
    text_02_Q1_ans, text_02_Q1_corr, text_02_Q2, text_02_Q2_ans, text_02_Q2_corr, text_02_Q3, text_02_Q3_ans, \
    text_02_Q3_corr, text_03, text_03_Q1, text_03_Q1_ans, text_03_Q1_corr, text_03_Q2, text_03_Q2_ans, text_03_Q2_corr, \
    text_03_Q3, text_03_Q3_ans, text_03_Q3_corr, text_04, text_04_Q1, text_04_Q1_ans, text_04_Q1_corr, text_04_Q2, \
    text_04_Q2_ans, text_04_Q2_corr, text_04_Q3, text_04_Q3_ans, text_04_Q3_corr, text_05, text_05_Q1, text_05_Q1_ans, \
    text_05_Q1_corr, text_05_Q2, text_05_Q2_ans, text_05_Q2_corr, text_05_Q3, text_05_Q3_ans, text_05_Q3_corr, text_06, \
    text_06_Q1, text_06_Q1_ans, text_06_Q1_corr, text_06_Q2, text_06_Q2_ans, text_06_Q2_corr, text_06_Q3, \
    text_06_Q3_ans, text_06_Q3_corr, text_07, \
    text_07_Q1, text_07_Q1_ans, text_07_Q1_corr, text_07_Q2, text_07_Q2_ans, text_07_Q2_corr, text_07_Q3, \
    text_07_Q3_ans, text_07_Q3_corr, text_08, \
    text_08_Q1, text_08_Q1_ans, text_08_Q1_corr, text_08_Q2, text_08_Q2_ans, text_08_Q2_corr, text_08_Q3, \
    text_08_Q3_ans, text_08_Q3_corr, reading_ps_text_no_click

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


# make mouse invisible during experiment
# mouse = io.devices.mouse
# win.setMouseVisible(False)
# mouse = event.Mouse(visible = False) 
# mouse.setExclusive(True) # this disables mouse during entire experiment
win.mouseVisible = False

# create 10 ms timer that we can use instead of core.wait()
my_timer = core.CountdownTimer(0.01)