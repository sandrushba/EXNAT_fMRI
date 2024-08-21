#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.0),
    on Wed Aug 21 22:44:31 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2024.1.0')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.0'
expName = 'EXNAT_3_training'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'testing_mode': 'yes',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_loggingLevel = logging.getLevel('error')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'Analysis/Data_EXNAT_3_training/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/sandramartin/ownCloud/EXNAT/EXNAT_fMRI/Psychopy_experiments/EXNAT_3_training/EXNAT_3_training_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1080], fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Settings" ---
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
    # math package for log function
    import math
    
    # Button box set-up
    # Import serial for button box
    import serial
    # Initialize serial connection
    #ser = serial.Serial('/dev/ttyUSB0', 19200)
    
    
    # Get functions from my custom scripts:
    # import all texts
    from EXNAT3_training_texts_MC_Qs import instr_pic_path, instr_Reading_Baseline_training_click, \
        instr_pic_Reading_Baseline_training_click, instr_Reading_pseudotext_no_click, instr_Reading_Baseline_main_click, \
        instr_pic_Reading_Baseline_main_click, instr_Reading_Baseline_main_no_click, instr_click_training, \
        instr_pic_click_training, instr_0back_single_training1, instr_0back_single_training2, instr_pic_0back, instr_0back_dual_main_click1, instr_0back_dual_main_click2, instr_0back_dual_main_no_click1, instr_0back_dual_main_no_click2, instr_1back_single_training1, instr_pic_1back_single_training1, \
        instr_pic_0back_dual_no_click, instr_1back_single_training2, instr_pic_1back_single_training2, instr_1back_single_main, \
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
    # Run 'Begin Experiment' code from stimuli
    ### Stimulus settings
    import random
    
    # measure frame rate (in Hz)
    # frame_rate = win.getActualFrameRate() # frame rate in Hz
    # print("measured frame rate:", frame_rate, "Hz")
    # set flicker frequency (in Hz)
    # flicker_freq = frame_rate/4 # 60/4 = 15 Hz
    
    # set colours you want to use for background:
    # light_bg_col_hex = "#FDFBF0" # ivory instructions background
    # dark_bg_col_hex  = "#505050" # dark grey background for stimuli
    light_bg_col = [(x / 127.5) - 1 for x in (253, 251, 240)]  # ivory instructions background (use RGB -1:1)
    dark_bg_col = [(x / 127.5) - 1 for x in (80, 80, 80)]  # dark grey background for stimuli (use RGB -1:1)
    
    # for timing test:
    # dark_bg_col = [(x / 127.5) - 1 for x in (255, 255, 255)]
    
    # make background light for a start - use rgb -1:1 colour codes
    win.setColor(light_bg_col, colorSpace='rgb')
    
    # set colours you want to use for the stimuli:
    colours = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"]
    print("Preparing experiment with n-back colours:", colours)
    # for timing test:
    # colours = ["#000000", "#F989A2", "#2AB7EF", "#88BA3F"]
    
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
    all_main_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04", "text_05", "text_06", "text_07", "text_08"]
    # shuffle text numbers
    random.shuffle(all_main_texts_nrs_list)
    
    # only get first 9 texts for the main blocks, the last one will be used for the vis task:
    # vis_task_text_nr = all_main_texts_nrs_list[-1]
    # all_main_texts_nrs_list = all_main_texts_nrs_list[0:-1]
    
    # append "empty" text numbers to the list where we have blocks that are not main blocks.
    all_texts_nrs_list = []
    
    for t_idx, t in enumerate(all_main_texts_nrs_list):
        # if it's the first text, it's the reading BL main block.
        if t_idx == 0:
            all_texts_nrs_list = all_texts_nrs_list + ["", t, ""]
        elif t_idx == 1:
            all_texts_nrs_list = all_texts_nrs_list + [t, "", "", ""]
        # one text for 0back dual block with click, one text for 0-back no click
        elif t_idx == 2:
            all_texts_nrs_list = all_texts_nrs_list + [t, "", "", ""]
        # append one text for self-paced dual block 0-back,
        # then two empty blocks for n-back training, then two blocks for single n-back blocks (self-paced and paced)
        elif t_idx == 3:
            all_texts_nrs_list = all_texts_nrs_list + [t, ""]
        # one text for paced dual block, then again four empty blocks for other n-back condition
        elif t_idx == 4:
            all_texts_nrs_list = all_texts_nrs_list + [t]
        elif t_idx == 5:
            all_texts_nrs_list = all_texts_nrs_list + [t, ""]
        elif t_idx == 6:
            all_texts_nrs_list = all_texts_nrs_list + [t, ""]
        elif t_idx > 6:
            [t]
        # then finally append rest of texts (two texts)
    
            all_texts_nrs_list.append(t)
    
    print(all_texts_nrs_list)
    
    ### Set order of blocks
    # Currently 20 blocks in total
    print("set block order")
    
    # this always comes first in the experiment
    blocks_click = ["Reading_Baseline_training_click", "Reading_Baseline_main_click", "0back_single_training",
                    "0back_dual_main_click", "1back_single_training1", "1back_single_training2", "1back_single_main",
                    "1back_dual_main_click", "2back_single_training1", "2back_single_training2", "2back_single_main",
                    "2back_dual_main_click"]
    reading_no_click = ["Reading_Baseline_training_no_click", "Reading_Baseline_main_no_click", "0back_dual_main_no_click"]
    
    # then you get both n-back conditions with trainings (which of them is first is randomized)
    oneback = ["1back_single_main_no_click", "1back_dual_main_no_click"]
    twoback = ["2back_single_main_no_click", "2back_dual_main_no_click"]
    
    # shuffle the order of the 2 lists
    blocks_no_click = [oneback, twoback]
    random.shuffle(blocks_no_click)
    
    # flatten nested list
    main_blocks = flatten_list(blocks_no_click)
    
    pseudo_block = ["Reading_pseudotext_no_click"]
    
    # put them all together:
    # global all_blocks
    all_blocks = blocks_click + reading_no_click + blocks_no_click + pseudo_block
    all_blocks = flatten_list(all_blocks)
    print(all_blocks)
    
    ### Create n-back colour lists for all blocks
    
    print("create n-back colour lists")
    # The reading bl training text has 55 trials.
    # the reading bl main has 91 words
    # reading training no click has 58 words
    # then main reading bl no click with 91 words
    # then 0-back short training with 20 trials
    # then 0-back dual self-paced and paced block with 91 trials and 15 targets each
    
    # Then we have 2 short training blocks à 20 trials each (5 targets) for n-back
    # then two single n-back blocks with 90 trials each (15 targets)
    # then two dual blocks with 91 trials each (15 targets)
    # then again two short training blocks, two single n-back blocks with 90 trials each (15 targets), and two dual blocks with 91 trials (15 targets)
    # and finally, one pseudotext block
    
    # --> all in all, 20 blocks
    
    # So for every block, build a list with colour codes containing the right amount of targets.
    # The function is defined in another script bc it's super long,
    # I import it at the beginning of this script.
    
    # First, create list with length of all texts. The length of the blocks is
    # always in the same order, only the conditions change.
    
    blocks_click = ["Reading_Baseline_training_click", "Reading_Baseline_main_click", "0back_single_training",
                    "0back_dual_main_click", "1back_single_training1", "1back_single_training2", "1back_single_main",
                    "1back_dual_main_click", "2back_single_training1", "2back_single_training2", "2back_single_main",
                    "2back_dual_main_click"]
    reading_no_click = ["Reading_Baseline_training_no_click", "Reading_Baseline_main_no_click", "0back_dual_main_no_click"]
    
    # then you get both n-back conditions with trainings (which of them is first is randomized)
    oneback = ["1back_single_main_no_click", "1back_dual_main_no_click"]
    twoback = ["2back_single_main_no_click", "2back_dual_main_no_click"]
    
    blocks_textlen = [60, 91, 20, 91,
                      20, 20, 90, 91,
                      20, 20, 90, 91,
                      60, 91, 91, 90, 91, 90, 91,
                      100]
    blocks_target_counts = [15, 15, 5, 15,
                            5, 5, 15, 15,
                            5, 5, 15, 15,
                            15, 15, 15, 15,
                            15, 15, 15, 15]
    # Now loop this list. Check which condition we have there and the create colour list for each text.
    all_colour_lists = []
    all_target_lists = []
    target_colours_list = []
    # target_colour = np.random.choice(colours)
    for block_idx, block_length in enumerate(blocks_textlen):
        # get 1st letter of block name - that tells us the condition
        block_cond = all_blocks[block_idx][0]
    
        # for each condition, decide which n-back level we want to assign
        # For all no-n-back blocks, we use 1 (just for the colour list generation)
        # global curr_nback_level
        if block_cond == "R":
            curr_nback_level = 1
        elif block_cond == "0":
            curr_nback_level = 0
        elif block_cond == "1":
            curr_nback_level = 1
        else:
            curr_nback_level = 2
    
        # generate colour list for current block
        if curr_nback_level == 0:
            # generate random colour list for 0-back:
            # Filter out the colours that have already been used as target colours
            available_colours = [colour for colour in colours if colour not in target_colours_list]
    
            # Shuffle the available colours to randomize the selection
            random.shuffle(available_colours)
    
            # Select the first colour from the shuffled available colours as the target colour
            target_colour = available_colours[0]
    
            print("curr target colour:", target_colour)
            curr_colours = create_0back_stimlist(target_colour=target_colour,
                                                 nr_targets=blocks_target_counts[block_idx],
                                                 colour_codes=colours,
                                                 nr_words=blocks_textlen[block_idx])
            # Get list of targets / non-targets
            curr_targets = [colour == target_colour for colour in curr_colours]
    
            # Add the selected target colour to the list of target colours
            target_colours_list.append(target_colour)
    
        elif curr_nback_level in [1, 2]:
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
        all_colour_lists.append(curr_colours)
        all_target_lists.append(curr_targets)
    
    print("------ finished preparing stimuli! ------")
    
    # ------------------------------------------
    
    # init block counter for the whole experiment
    exp_block_counter = 0
    
    print("starting experiment now!")
    
    # --- Initialize components for Routine "demographics" ---
    win.allowStencil = True
    demographic_form = visual.Form(win=win, name='demographic_form',
        items='demographics_form.csv',
        textHeight=0.03,
        font='Open Sans',
        randomize=False,
        style='custom...',
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=[1.0000, 1.0000, 1.0000], itemColor=[-1.0000, -1.0000, -1.0000], 
        responseColor=[-1.0000, -1.0000, -1.0000], markerColor=[0.9608, 0.8431, 0.6863], colorSpace='rgb', 
        size=(1.3, 0.9),
        pos=(0, 0),
        itemPadding=0.03,
        depth=0
    )
    demographic_button = visual.ButtonStim(win, 
        text='Weiter', font='Open Sans',
        pos=(0.3, -0.35),
        letterHeight=0.06,
        size=(0.3, 0.12), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='demographic_button',
        depth=-1
    )
    demographic_button.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "education" ---
    win.allowStencil = True
    edu_form = visual.Form(win=win, name='edu_form',
        items='education_form.csv',
        textHeight=0.03,
        font='Open Sans',
        randomize=False,
        style='custom...',
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=[1.0000, 1.0000, 1.0000], itemColor=[-1.0000, -1.0000, -1.0000], 
        responseColor=[-1.0000, -1.0000, -1.0000], markerColor=[0.9608, 0.8431, 0.6863], colorSpace='rgb', 
        size=(1.3, 0.9),
        pos=(0, 0),
        itemPadding=0.03,
        depth=0
    )
    edu_button = visual.ButtonStim(win, 
        text='Weiter', font='Open Sans',
        pos=(0.3, -0.35),
        letterHeight=0.06,
        size=(0.3, 0.12), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='edu_button',
        depth=-1
    )
    edu_button.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "welcome_Ishihara" ---
    instructions = visual.TextStim(win=win, name='instructions',
        text='Farbsehtest\n\nIm Folgenden werden Ihnen nun einige Bilder gezeigt, auf denen jeweils eine Zahl zu sehen ist.\n\nBitte geben Sie unter jedem Bild an, welche Zahl Sie sehen. ',
        font='Open Sans',
        pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instr_button = visual.ButtonStim(win, 
        text='Weiter', font='Open Sans',
        pos=(0.3, -0.35),
        letterHeight=0.035,
        size=(0.3, 0.12), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='instr_button',
        depth=-1
    )
    instr_button.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "Ishihara" ---
    ishihara_1 = visual.ImageStim(
        win=win,
        name='ishihara_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    ishihara_number = visual.TextBox2(
         win, text=None, placeholder=None, font='Open Sans',
         pos=(0, -0.3),     letterHeight=0.025,
         size=(0.15, 0.1), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='hidden',
         fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='ishihara_number',
         depth=-1, autoLog=True,
    )
    ishihara_button = visual.ButtonStim(win, 
        text='Weiter', font='Open Sans',
        pos=(0.3, -0.35),
        letterHeight=0.035,
        size=(0.3, 0.12), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ishihara_button',
        depth=-2
    )
    ishihara_button.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "feedback" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "no_text_blocks_self_paced" ---
    
    # --- Initialize components for Routine "text_blocks_self_paced" ---
    
    # --- Initialize components for Routine "text_blocks_paced" ---
    
    # --- Initialize components for Routine "no_text_blocks_paced" ---
    
    # --- Initialize components for Routine "pseudotext" ---
    
    # --- Initialize components for Routine "end" ---
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Settings" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Settings.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    SettingsComponents = []
    for thisComponent in SettingsComponents:
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
    
    # --- Run Routine "Settings" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SettingsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Settings" ---
    for thisComponent in SettingsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Settings.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "Settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "demographics" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('demographics.started', globalClock.getTime(format='float'))
    # reset demographic_button to account for continued clicks & clear times on/off
    demographic_button.reset()
    # keep track of which components have finished
    demographicsComponents = [demographic_form, demographic_button]
    for thisComponent in demographicsComponents:
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
    
    # --- Run Routine "demographics" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *demographic_form* updates
        
        # if demographic_form is starting this frame...
        if demographic_form.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            demographic_form.frameNStart = frameN  # exact frame index
            demographic_form.tStart = t  # local t and not account for scr refresh
            demographic_form.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demographic_form, 'tStartRefresh')  # time at next scr refresh
            # update status
            demographic_form.status = STARTED
            demographic_form.setAutoDraw(True)
        
        # if demographic_form is active this frame...
        if demographic_form.status == STARTED:
            # update params
            pass
        # *demographic_button* updates
        
        # if demographic_button is starting this frame...
        if demographic_button.status == NOT_STARTED and demographic_form.complete==True:
            # keep track of start time/frame for later
            demographic_button.frameNStart = frameN  # exact frame index
            demographic_button.tStart = t  # local t and not account for scr refresh
            demographic_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demographic_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            demographic_button.status = STARTED
            demographic_button.setAutoDraw(True)
        
        # if demographic_button is active this frame...
        if demographic_button.status == STARTED:
            # update params
            pass
            # check whether demographic_button has been pressed
            if demographic_button.isClicked:
                if not demographic_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    demographic_button.timesOn.append(demographic_button.buttonClock.getTime())
                    demographic_button.timesOff.append(demographic_button.buttonClock.getTime())
                elif len(demographic_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    demographic_button.timesOff[-1] = demographic_button.buttonClock.getTime()
                if not demographic_button.wasClicked:
                    # end routine when demographic_button is clicked
                    continueRoutine = False
                if not demographic_button.wasClicked:
                    # run callback code when demographic_button is clicked
                    pass
        # take note of whether demographic_button was clicked, so that next frame we know if clicks are new
        demographic_button.wasClicked = demographic_button.isClicked and demographic_button.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in demographicsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "demographics" ---
    for thisComponent in demographicsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('demographics.stopped', globalClock.getTime(format='float'))
    demographic_form.addDataToExp(thisExp, 'rows')
    demographic_form.autodraw = False
    thisExp.nextEntry()
    # the Routine "demographics" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "education" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('education.started', globalClock.getTime(format='float'))
    # reset edu_button to account for continued clicks & clear times on/off
    edu_button.reset()
    # keep track of which components have finished
    educationComponents = [edu_form, edu_button]
    for thisComponent in educationComponents:
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
    
    # --- Run Routine "education" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *edu_form* updates
        
        # if edu_form is starting this frame...
        if edu_form.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            edu_form.frameNStart = frameN  # exact frame index
            edu_form.tStart = t  # local t and not account for scr refresh
            edu_form.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(edu_form, 'tStartRefresh')  # time at next scr refresh
            # update status
            edu_form.status = STARTED
            edu_form.setAutoDraw(True)
        
        # if edu_form is active this frame...
        if edu_form.status == STARTED:
            # update params
            pass
        # *edu_button* updates
        
        # if edu_button is starting this frame...
        if edu_button.status == NOT_STARTED and edu_form.complete:
            # keep track of start time/frame for later
            edu_button.frameNStart = frameN  # exact frame index
            edu_button.tStart = t  # local t and not account for scr refresh
            edu_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(edu_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            edu_button.status = STARTED
            edu_button.setAutoDraw(True)
        
        # if edu_button is active this frame...
        if edu_button.status == STARTED:
            # update params
            pass
            # check whether edu_button has been pressed
            if edu_button.isClicked:
                if not edu_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    edu_button.timesOn.append(edu_button.buttonClock.getTime())
                    edu_button.timesOff.append(edu_button.buttonClock.getTime())
                elif len(edu_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    edu_button.timesOff[-1] = edu_button.buttonClock.getTime()
                if not edu_button.wasClicked:
                    # end routine when edu_button is clicked
                    continueRoutine = False
                if not edu_button.wasClicked:
                    # run callback code when edu_button is clicked
                    pass
        # take note of whether edu_button was clicked, so that next frame we know if clicks are new
        edu_button.wasClicked = edu_button.isClicked and edu_button.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in educationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "education" ---
    for thisComponent in educationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('education.stopped', globalClock.getTime(format='float'))
    edu_form.addDataToExp(thisExp, 'rows')
    edu_form.autodraw = False
    thisExp.nextEntry()
    # the Routine "education" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "welcome_Ishihara" ---
    continueRoutine = True
    # update component parameters for each repeat
    # reset instr_button to account for continued clicks & clear times on/off
    instr_button.reset()
    # keep track of which components have finished
    welcome_IshiharaComponents = [instructions, instr_button]
    for thisComponent in welcome_IshiharaComponents:
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
    
    # --- Run Routine "welcome_Ishihara" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions* updates
        
        # if instructions is starting this frame...
        if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions.frameNStart = frameN  # exact frame index
            instructions.tStart = t  # local t and not account for scr refresh
            instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructions.status = STARTED
            instructions.setAutoDraw(True)
        
        # if instructions is active this frame...
        if instructions.status == STARTED:
            # update params
            pass
        # *instr_button* updates
        
        # if instr_button is starting this frame...
        if instr_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instr_button.frameNStart = frameN  # exact frame index
            instr_button.tStart = t  # local t and not account for scr refresh
            instr_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_button.status = STARTED
            instr_button.setAutoDraw(True)
        
        # if instr_button is active this frame...
        if instr_button.status == STARTED:
            # update params
            pass
            # check whether instr_button has been pressed
            if instr_button.isClicked:
                if not instr_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    instr_button.timesOn.append(instr_button.buttonClock.getTime())
                    instr_button.timesOff.append(instr_button.buttonClock.getTime())
                elif len(instr_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    instr_button.timesOff[-1] = instr_button.buttonClock.getTime()
                if not instr_button.wasClicked:
                    # end routine when instr_button is clicked
                    continueRoutine = False
                if not instr_button.wasClicked:
                    # run callback code when instr_button is clicked
                    pass
        # take note of whether instr_button was clicked, so that next frame we know if clicks are new
        instr_button.wasClicked = instr_button.isClicked and instr_button.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome_IshiharaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome_Ishihara" ---
    for thisComponent in welcome_IshiharaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    # the Routine "welcome_Ishihara" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ishihara_pics = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ishihara_loop.csv'),
        seed=None, name='ishihara_pics')
    thisExp.addLoop(ishihara_pics)  # add the loop to the experiment
    thisIshihara_pic = ishihara_pics.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIshihara_pic.rgb)
    if thisIshihara_pic != None:
        for paramName in thisIshihara_pic:
            globals()[paramName] = thisIshihara_pic[paramName]
    
    for thisIshihara_pic in ishihara_pics:
        currentLoop = ishihara_pics
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisIshihara_pic.rgb)
        if thisIshihara_pic != None:
            for paramName in thisIshihara_pic:
                globals()[paramName] = thisIshihara_pic[paramName]
        
        # --- Prepare to start Routine "Ishihara" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Ishihara.started', globalClock.getTime(format='float'))
        ishihara_1.setImage(DisplayImage)
        ishihara_number.reset()
        ishihara_number.setText('')
        # reset ishihara_button to account for continued clicks & clear times on/off
        ishihara_button.reset()
        # keep track of which components have finished
        IshiharaComponents = [ishihara_1, ishihara_number, ishihara_button]
        for thisComponent in IshiharaComponents:
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
        
        # --- Run Routine "Ishihara" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ishihara_1* updates
            
            # if ishihara_1 is starting this frame...
            if ishihara_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ishihara_1.frameNStart = frameN  # exact frame index
                ishihara_1.tStart = t  # local t and not account for scr refresh
                ishihara_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ishihara_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                ishihara_1.status = STARTED
                ishihara_1.setAutoDraw(True)
            
            # if ishihara_1 is active this frame...
            if ishihara_1.status == STARTED:
                # update params
                pass
            
            # *ishihara_number* updates
            
            # if ishihara_number is starting this frame...
            if ishihara_number.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ishihara_number.frameNStart = frameN  # exact frame index
                ishihara_number.tStart = t  # local t and not account for scr refresh
                ishihara_number.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ishihara_number, 'tStartRefresh')  # time at next scr refresh
                # update status
                ishihara_number.status = STARTED
                ishihara_number.setAutoDraw(True)
            
            # if ishihara_number is active this frame...
            if ishihara_number.status == STARTED:
                # update params
                pass
            # *ishihara_button* updates
            
            # if ishihara_button is starting this frame...
            if ishihara_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                ishihara_button.frameNStart = frameN  # exact frame index
                ishihara_button.tStart = t  # local t and not account for scr refresh
                ishihara_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ishihara_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                ishihara_button.status = STARTED
                ishihara_button.setAutoDraw(True)
            
            # if ishihara_button is active this frame...
            if ishihara_button.status == STARTED:
                # update params
                pass
                # check whether ishihara_button has been pressed
                if ishihara_button.isClicked:
                    if not ishihara_button.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        ishihara_button.timesOn.append(ishihara_button.buttonClock.getTime())
                        ishihara_button.timesOff.append(ishihara_button.buttonClock.getTime())
                    elif len(ishihara_button.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        ishihara_button.timesOff[-1] = ishihara_button.buttonClock.getTime()
                    if not ishihara_button.wasClicked:
                        # end routine when ishihara_button is clicked
                        continueRoutine = False
                    if not ishihara_button.wasClicked:
                        # run callback code when ishihara_button is clicked
                        pass
            # take note of whether ishihara_button was clicked, so that next frame we know if clicks are new
            ishihara_button.wasClicked = ishihara_button.isClicked and ishihara_button.status == STARTED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in IshiharaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Ishihara" ---
        for thisComponent in IshiharaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Ishihara.stopped', globalClock.getTime(format='float'))
        ishihara_pics.addData('ishihara_number.text',ishihara_number.text)
        # the Routine "Ishihara" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if ishihara_number.text == str(corrAns):
            thisFeedback = "Korrekt"
        else:
            thisFeedback = "Falsch"
        feedback_text.setText(thisFeedback)
        # keep track of which components have finished
        feedbackComponents = [feedback_text]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            
            # if feedback_text is starting this frame...
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedback_text.status = STARTED
                feedback_text.setAutoDraw(True)
            
            # if feedback_text is active this frame...
            if feedback_text.status == STARTED:
                # update params
                pass
            
            # if feedback_text is stopping this frame...
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text.frameNStop = frameN  # exact frame index
                    # update status
                    feedback_text.status = FINISHED
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'ishihara_pics'
    
    
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
            globals()[paramName] = thisBlock[paramName]
    
    for thisBlock in blocks:
        currentLoop = blocks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                globals()[paramName] = thisBlock[paramName]
        
        # --- Prepare to start Routine "no_text_blocks_self_paced" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('no_text_blocks_self_paced.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from no_text_and_training_2
        #################################################
        #          Blocks w/o text – self-paced         #
        #################################################
        # this routine is for all blocks where there are
        # coloured rectangles instead of words
        
        # Use loop here that runs the non-text blocks
        # until we have to display a main text block (in this case we exit the routine).
        
        while True:
            event. Mouse(visible=False)
            # keep background ivory
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
        
            # clear buffer of all previously recorded key events:
            event.clearEvents()
        
            ### specify settings for the current block
        
            ### Prepare stimuli:
        
            # get block kind
            curr_block = all_blocks[exp_block_counter]
        
            # Check whether it's one of the non-text tasks.
            # If current block is a text block, skip this routine and go to the next.
            if curr_block not in ["click_training", "0back_single_training", "1back_single_training1", "1back_single_training2",
                                  "1back_single_main", "2back_single_training1", "2back_single_training2", "2back_single_main"]:
                print(f"this is block {curr_block}")
                print(f"\tskipping self-paced n-back routine")
                break
        
            # if it's one of the non-text blocks, though, prepare stimuli:
            else:
                print(f"this is block {curr_block}")
                print(f"\tstart preparing block {curr_block}")
                # print("\t" + curr_block + " is not a text block - preparing rect as stim now")
        
                # keep background ivory
                win.setColor(light_bg_col, colorSpace='rgb')
                win.flip()
        
                ### Show instructions
                # set instruction text
                if curr_block == "0back_single_training":
                    # create text boxes
                    instr_text_stim1 = visual.TextStim(win,
                                                       text=locals()["instr_0back_single_training1"],
                                                       height=0.025,  # font height relative to height of screen
                                                       pos=(0, 0.30),  # move instructions up a bit
                                                       color="black")
                    instr_text_stim2 = visual.TextStim(win,
                                                       text=locals()["instr_0back_single_training2"],
                                                       height=0.025,  # font height: 5° visual angle
                                                       pos=(0, -0.35),  # move instructions down a bit
                                                       color="black")
                    # create "empty" circle as stimulus
                    instr_colour_circle_stim = visual.Circle(win=win,
                                                             radius=0.065,
                                                             pos=(0, 0.075))  # move circle slightly down
        
                    # set current target colour as colour of circle:
                    instr_colour_circle_stim.fillColor = target_colours_list[0]
        
                    # create ImageStim object
                    curr_instr_pic = visual.ImageStim(win,
                                                      size=(0.55, 0.25),
                                                      pos=(0, -0.15),
                                                      image=locals()["instr_pic_0back"])  # set path to image here
        
                else:
                    instr_text = locals()["instr_" + curr_block]
                    # create text box
                    instr_text_stim = visual.TextStim(win,
                                                      text=instr_text,
                                                      height=0.025,  # font height relative to height of screen
                                                      pos=(0, 0.2),  # move up a bit
                                                      color="black")
                    # create ImageStim object
                    curr_instr_pic = visual.ImageStim(win,
                                                      size=(0.8, 0.3),
                                                      pos=(0, -0.2),
                                                      image=locals()["instr_pic_" + curr_block])  # set path to image here
        
                # display the text & image on screen
                if curr_block == "0back_single_training":
                    # show instructions on screen
                    instr_text_stim1.draw()
                    instr_text_stim2.draw()
                    instr_colour_circle_stim.draw()
                    curr_instr_pic.draw()
                    win.flip()
                    core.wait(3)  # wait for 3s before starting response window
        
                    # display the text & the circle on screen until Space is pressed
                    while True:
                        instr_text_stim1.draw()
                        instr_text_stim2.draw()
                        instr_colour_circle_stim.draw()
                        curr_instr_pic.draw()
                        win.flip()
                        # end screen if participant presses space
                        if event.getKeys(['space']):
                            print("\t\tstart current block")
                            skip_curr_block = False
                            break
        
                elif curr_block in ["1back_single_training2", "2back_single_training2"]:
                    # draw instructions on screen
                    instr_text_stim.draw()
                    curr_instr_pic.draw()
                    win.flip()
                    core.wait(3)  # wait for 3 s before starting response window
        
                    while True:
                        instr_text_stim.draw()
                        curr_instr_pic.draw()
                        win.flip()
                        # skip current block (aka the second training block))
                        if event.getKeys(['space']):
                            print("\t\tstart next block - skip second training block")
                            skip_curr_block = True
                            break
                        # repeat training (aka run current block, which is the second training block)
                        elif event.getKeys(['w']):
                            print("\t\trepeat training block")
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
                            print("\t\tstart current block")
                            skip_curr_block = False
                            break
        
                # only run this if the current block shall not be skipped:
                if skip_curr_block == False:
                    ### change background colour
                    win.setColor(dark_bg_col, colorSpace='rgb')
                    win.flip()
        
                    # don't show questions
                    skip_questions = True
                    training_Qs = False
        
                    # get n-back condition:
                    curr_nback_cond = curr_block[0]  # get first character of block name
        
                    # if it is a 0, 1 or 2, set that as current n-back level:
                    if curr_nback_cond in ['0', '1', '2']:
                        curr_nback_cond == int(curr_nback_cond)
                    # if it's neither 0, 1 nor 2, it has to be a block without n-back,
                    # so set curr_nback_cond to None
                    else:
                        curr_nback_cond = None
        
                    print(f"\tcurrent n-back condition: {curr_nback_cond}")
        
                    # get list with targets & list with colours
                    curr_targets = all_target_lists[exp_block_counter]
                    curr_colours = all_colour_lists[exp_block_counter]
        
                    ### Start block loop
                    # depending on condition, create arrays for saving response
                    # times - we need that later for the paced task of the 1- and 2-back single blocks
                    if curr_block == "1back_single_main":
                        oneback_single_paced_durations = []
                    elif curr_block == "2back_single_main":
                        twoback_single_paced_durations = []
        
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
                        # the stimulus
        
                        # start trial clock for measuring RTs from stimulus onset
                        my_trial_clock.reset()
        
                        # onset_time = my_trial_clock.getTime()
        
                        ### wait for key response:
                        # In blocks with n-back task, participants can press "c" to indicate they saw a target colour and "space" to go to the next word/stimulus.
                        # In blocks without n-back task, participants can only press "space" to go to the next stimulus.
                        # print("start tracking key responses")
        
                        ### start recording responses
                        # start "endless" while loop that looks for responses
                        # in each iteration, draw word on screen
                        continue_trial = True
                        while continue_trial:
        
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
                                    # send_trigger("response_continue")
        
                                    # break while loop to go to next trial
                                    continue_trial = False
        
                                # if participant pressed button "c" for the first time and it's an n-back condition
                                # where they're actually supposed to do that (aka not a reading baseline condition)...
                                elif key == 'c' and curr_nback_cond != None and saw_target == False:
                                    # get reaction time
                                    curr_nback_RT = my_trial_clock.getTime() * 1000
        
                                    # send trigger for response:
                                    # send_trigger("response_target")
        
                                    # only get first target response, we don't care if they press the button more than once:
                                    saw_target = True
        
                                # If esc is pressed, end the experiment:
                                elif key == 'escape':
                                    # et_abort_exp()  # shut down eyetrigger and download incremental data
                                    # make sure parallel port line is cleared
                                    # core.wait(time_after_trigger)
                                    # parallel.setData(0)
                                    core.wait(0.5)
                                    # end experiment
                                    core.quit()
        
                            # Check for timeout - if more than 1.5 or 2 seconds have passed, move to the next trial
                            if my_trial_clock.getTime() - trial_start_time >= 1.5 and curr_block in [
                                "0back_single_training", "1back_single_training1", "1back_single_training2", "1back_single_main"]:
                                curr_duration = 1500
                                continue_trial = False
                            elif my_trial_clock.getTime() - trial_start_time >= 2 and curr_block in [
                                "2back_single_training1", "2back_single_training2", "2back_single_main"]:
                                curr_duration = 2000
                                continue_trial = False
        
                        ### end trial
                        # print("end trial")
        
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
                        thisExp.addData('colour', curr_col)
                        thisExp.addData('target', curr_target)
                        if curr_block == "0back_single_training":
                            thisExp.addData('curr_0back_target', target_colours_list[0])
                        thisExp.addData('nback_response', curr_nback_response)
                        thisExp.addData('nback_RT', curr_nback_RT)  # in ms
                        thisExp.addData('duration', curr_duration)  # in ms
                        thisExp.addData('trial_nr', curr_trial_nr)
                        thisExp.addData('block_nr', exp_block_counter)
                        thisExp.addData('block_name', curr_block)
                        thisExp.addData('block_kind', curr_nback_cond)
        
                        # start a new row in the csv
                        thisExp.nextEntry()
        
                        # depending on condition, save response times and words in previously created arrays
                        # we need that later for the paced reading tasks
                        if curr_block == "1back_single_main":
                            oneback_single_paced_durations.append(curr_duration)
                        elif curr_block == "2back_single_main":
                            twoback_single_paced_durations.append(curr_duration)
        
                        ### IF TESTING MODE ENABLED: end loop after 4 trials
                        if expInfo['testing_mode'] == "yes":
                            if trial_idx == 3:
                                break
        
                    print("\t\tfinished presenting trials")
        
                    # change background colour from grey (RGB: 10, 10, 10)
                    # to ivory (RGB: 240, 223, 204)
                    win.setColor(light_bg_col, colorSpace='rgb')
                    win.flip()
        
                # add 1 to the block counter to go load the next block
                exp_block_counter = exp_block_counter + 1
                print(f"\tGoing to block {exp_block_counter + 1}/20 now!")
        
        # go to next routine
        # print("going to next routine")
        continueRoutine = False
        # keep track of which components have finished
        no_text_blocks_self_pacedComponents = []
        for thisComponent in no_text_blocks_self_pacedComponents:
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
        
        # --- Run Routine "no_text_blocks_self_paced" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in no_text_blocks_self_pacedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "no_text_blocks_self_paced" ---
        for thisComponent in no_text_blocks_self_pacedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('no_text_blocks_self_paced.stopped', globalClock.getTime(format='float'))
        # the Routine "no_text_blocks_self_paced" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "text_blocks_self_paced" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('text_blocks_self_paced.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from text_blocks
        #################################################
        #           Blocks with text – self-paced       #
        #################################################
        # this routine is for all blocks with texts that are self-paced
        
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
        
        # clear buffer of all previously recorded key events:
        event.clearEvents()
        
        ### specify settings for the current block
        
        ### Prepare stimuli:
        
        # get block kind
        curr_block = all_blocks[exp_block_counter]
        # print("start preparing block " + curr_block)
        
        # Check whether it's a block that isn't self-paced
        # If yes, skip this routine
        if curr_block in ["click_training", "0back_single_training", "1back_single_training1", "1back_single_training2",
                          "1back_single_main", "2back_single_training1", "2back_single_training2", "2back_single_main",
                          "Reading_Baseline_main_no_click", "0back_dual_main_no_click", "1back_dual_main_no_click", "2back_dual_main_no_click",
                          "Reading_Baseline_training_no_click", "1back_single_main_no_click", "2back_single_main_no_click"]:
            print(f"this is block {curr_block}")
            print("\tskipping self-paced text routine")
            # skip questions & end current routine
            skip_questions = True
            continueRoutine = False
            # break
        
        # if it's the reading bl training block, prepare training stimuli:
        elif curr_block == "Reading_Baseline_training_click":
            print(f"this is block {curr_block}")
            print(f"start preparing block {curr_block}")
        
            # keep background ivory
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
        
            ### Show instructions
            # set instruction text
            instr_text = locals()["instr_" + curr_block]
            # create text box
            instr_text_stim = visual.TextStim(win,
                                              text=instr_text,
                                              height=0.025,  # font height relative to height of screen
                                              pos=(0, 0.2),  # move up a bit
                                              color="black")
            # create ImageStim object
            curr_instr_pic = visual.ImageStim(win,
                                              size=(0.6, 0.3),
                                              pos=(0, -0.2),
                                              image=locals()["instr_pic_" + curr_block])  # set path to image here
        
            # show instructions on screen
            win.setColor(light_bg_col, colorSpace='rgb')
            instr_text_stim.draw()
            curr_instr_pic.draw()
            win.flip()
            core.wait(3)  # wait for 3s before starting response window
        
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
        
            # we also need the start time (let's set it as current time
            # at this point in the script):
            start_time = core.getTime()
        
            ### change background colour
            win.setColor(dark_bg_col, colorSpace='rgb')
            win.flip()
        
            print(f"\tcurrent text: {curr_text_nr}")
        
        # if it's one of the "normal" main blocks, prepare main block stimuli:
        elif curr_block in ["Reading_Baseline_main_click", "0back_dual_main_click", "1back_dual_main_click", "2back_dual_main_click"]:
            print(f"this is block {curr_block}")
            print(f"start preparing block {curr_block}")
        
            # keep background ivory
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
        
            ### Show instructions
            # set instruction text
            if curr_block == "0back_dual_main_click":
                # create text boxes
                instr_text_stim1 = visual.TextStim(win,
                                                   text=locals()["instr_0back_dual_main_click1"],
                                                   height=0.025,  # font height relative to height of screen
                                                   pos=(0, 0.3),  # move instructions up a bit
                                                   color="black")
                instr_text_stim2 = visual.TextStim(win,
                                                   text=locals()["instr_0back_dual_main_click2"],
                                                   height=0.025,  # font height: 5° visual angle
                                                   pos=(0, -0.35),  # move instructions down a bit
                                                   color="black")
                # create "empty" circle as stimulus
                instr_colour_circle_stim = visual.Circle(win=win,
                                                         radius=0.065,
                                                         pos=(0, 0.1))  # move circle slightly down
        
                # set current target colour as colour of circle:
                instr_colour_circle_stim.fillColor = target_colours_list[1]
        
                # create ImageStim object
                curr_instr_pic = visual.ImageStim(win,
                                                  size=(0.55, 0.25),
                                                  pos=(0, -0.15),
                                                  image=locals()["instr_pic_0back"])  # set path to image here
        
            else:
                instr_text = locals()["instr_" + curr_block]
                # create text box
                instr_text_stim = visual.TextStim(win,
                                                  text=instr_text,
                                                  height=0.025,  # font height relative to height of screen
                                                  pos=(0, 0.2),  # move up a bit
                                                  color="black")
                if curr_block == "Reading_Baseline_main_click":
                    # create ImageStim object
                    curr_instr_pic = visual.ImageStim(win,
                                                      size=(0.6, 0.3),
                                                      pos=(0, -0.2),
                                                      image=locals()["instr_pic_" + curr_block])  # set path to image here
                else:
                    # create ImageStim object
                    curr_instr_pic = visual.ImageStim(win,
                                                      size=(0.8, 0.3),
                                                      pos=(0, -0.2),
                                                      image=locals()["instr_pic_" + curr_block])  # set path to image here
        
            # show instructions
            if curr_block == "0back_dual_main_click":
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim1.draw()
                instr_text_stim2.draw()
                instr_colour_circle_stim.draw()
                curr_instr_pic.draw()
                win.flip()
                core.wait(3)  # wait for 3s before starting response window
        
                # display the text & the circle on screen until Space is pressed
                while True:
                    instr_text_stim1.draw()
                    instr_text_stim2.draw()
                    instr_colour_circle_stim.draw()
                    curr_instr_pic.draw()
                    win.flip()
                    # end screen if participant presses space
                    if event.getKeys(['space']):
                        break
        
            else:
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim.draw()
                curr_instr_pic.draw()
                win.flip()
                core.wait(3)  # wait for 3s before starting response window
        
                # Display the text on screen
                while True:
                    instr_text_stim.draw()
                    curr_instr_pic.draw()
                    win.flip()
                    # end showing screen if participant presses space
                    if 'space' in event.getKeys():
                        break
        
            ### change background colour
            win.setColor(dark_bg_col, colorSpace='rgb')
            win.flip()
        
            # show main block questions
            skip_questions = False
            training_Qs = False
        
            # get text nr:
            curr_text_nr = all_texts_nrs_list[exp_block_counter]
        
            # get n-back condition:
            curr_nback_cond = curr_block[0]  # get first character of block name
        
            # if it is a 0, 1 or 2, set that as current n-back level:
            if curr_nback_cond in ['0', '1', '2']:
                curr_nback_cond == int(curr_nback_cond)
            # if it's neither 0, 1 nor 2, it has to be a block without n-back,
            # so set curr_nback_cond to None
            else:
                curr_nback_cond = None
        
            print(f"\tcurrent n-back condition: {curr_nback_cond}")
            print(f"\tcurrent text: {curr_text_nr}")
        
            # get list with targets & list with colours
            curr_targets = all_target_lists[exp_block_counter]
            curr_colours = all_colour_lists[exp_block_counter]
            # for current text nr, get text whose name = current text nr
            curr_text = locals()[curr_text_nr]
        
        ### Start block loop
        if curr_block in ["Reading_Baseline_training_click", "Reading_Baseline_main_click", "0back_dual_main_click", "1back_dual_main_click", "2back_dual_main_click"]:
            # depending on condition, create arrays for saving response
            # times & words - we need that later for the paced reading tasks
            if curr_block == "Reading_Baseline_main_click":
                BL_paced_durations = []
                BL_paced_words = []
            elif curr_block == "0back_dual_main_click":
                zeroback_paced_durations = []
                zeroback_paced_words = []
            elif curr_block == "1back_dual_main_click":
                oneback_paced_durations = []
                oneback_paced_words = []
            elif curr_block == "2back_dual_main_click":
                twoback_paced_durations = []
                twoback_paced_words = []
        
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
        
            # CREATE CLOCKS:
            my_block_clock = core.Clock()
            my_block_clock.reset()  # start block clock
            start_time = my_block_clock.getTime()  # get start time of block
            # also create trial clock
            my_trial_clock = core.Clock()
        
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
        
                # get trial number (start counting from 1, so add 1)
                curr_trial_nr = trial_idx + 1
        
                # set current word & colour as content of text stimulus
                stim.color = curr_colour
                stim.text = curr_word
        
                # show word on screen
                stim.draw()  # draw word on screen
        
                # start trial clock
                my_trial_clock.reset()
                onset_time = my_trial_clock.getTime()
        
                ### wait for 50 ms
                while my_trial_clock.getTime() < onset_time + 0.05:
        
                    # draw the stimulus during the waiting period
                    stim.draw()  # draw text
                    win.flip()
        
                ### wait for key response:
                # In blocks with n-back task, participants can press "c" to indicate they saw a target colour and "space" to go to the next word/stimulus.
                # In blocks without n-back task, participants can only press "space" to go to the next word/stimulus.
                # print("start tracking key responses")
        
                ### start recording responses
                # start "endless" while loop that looks for responses
                continue_trial = True
                trial_start_time = my_trial_clock.getTime()  # Record the start time of the trial
                while continue_trial:
        
                    # in each iteration, draw word on screen
                    stim.draw()
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
                            # send_trigger("response_continue")
                            # break while loop
                            continue_trial = False
        
                        # if participant pressed button "c" for the first time and it's an n-back condition
                        # where they're actually supposed to do that (aka not a reading baseline condition)...
                        elif key == 'c' and curr_nback_cond != None and saw_target == False:
                            # get reaction time
                            curr_nback_RT = my_trial_clock.getTime() * 1000
                            # send trigger for response:
                            # send_trigger("response_target")
                            # only get first target response, we don't care if they press the button more than once:
                            saw_target = True
        
                        # If esc is pressed, end the experiment:
                        elif key == 'escape':
                            # et_abort_exp()  # shut down eyetrigger and download incremental data
                            # close trigger & close experiment
                            # core.wait(time_after_trigger)
                            # parallel.setData(0)
                            core.wait(0.5)
                            core.quit()
        
                    # Check for timeout - if more than 1.5, 2 or 2.5 seconds have passed, move to the next trial
                    if my_trial_clock.getTime() - trial_start_time >= 1.5 and curr_block in ["Reading_Baseline_training_click", "Reading_Baseline_main_click",
                                                                                             "0back_dual_main_click"]:
                        curr_duration = 1500
                        continue_trial = False
                    elif my_trial_clock.getTime() - trial_start_time >= 2 and curr_block == "1back_dual_main_click":
                        curr_duration = 2000
                        continue_trial = False
                    elif my_trial_clock.getTime() - trial_start_time >= 2.5 and curr_block == "2back_dual_main_click":
                        curr_duration = 2500
                        continue_trial = False
        
                ### end trial
                # print("\tend self-paced trial")
                # stop display of current word & send trial offset trigger
                # win.callOnFlip(send_trigger, "trial_offset")
        
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
                if curr_block == "0back_dual_main_click":
                    thisExp.addData('curr_0back_target', target_colours_list[1])
                thisExp.addData('nback_response', curr_nback_response)
                thisExp.addData('nback_RT', curr_nback_RT)  # in ms
                thisExp.addData('duration', curr_duration)  # in ms
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
        
                # depending on condition, save response times and words in previously created arrays
                # we need that later for the paced reading tasks
                if curr_block == "Reading_Baseline_main_click":
                    BL_paced_durations.append(curr_duration)
                    BL_paced_words.append(curr_word)
                elif curr_block == "0back_dual_main_click":
                    zeroback_paced_durations.append(curr_duration)
                    zeroback_paced_words.append(curr_word)
                elif curr_block == "1back_dual_main_click":
                    oneback_paced_durations.append(curr_duration)
                    oneback_paced_words.append(curr_word)
                elif curr_block == "2back_dual_main_click":
                    twoback_paced_durations.append(curr_duration)
                    twoback_paced_words.append(curr_word)
        
                ### IF TESTING MODE ENABLED: end loop after 4 trials
                if expInfo['testing_mode'] == "yes":
                    if trial_idx == 3:
                        break
        
            print("finished presenting trials")
        
            # Send end of block trigger:
            # core.wait(time_after_trigger)  # wait 3 ms
            # send block offset trigger
            # send_trigger("block_offset")
        
            # end current routine
            continueRoutine = False
        # Run 'Begin Routine' code from questions_self_paced
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
        
            return question_time, chosen_ans, is_correct, button_pressed
        
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
        if not skip_questions and training_Qs:
            # Setup for Q1
            Q1_text = reading_bl_tr_Q1
            Q1_answers = reading_bl_tr_Q1_ans
            Q1_correct = reading_bl_tr_Q1_corr
        
            question, answers = setup_question(Q1_text, Q1_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q1_correct)
            print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q1')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q1_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter+1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # Setup for Q2
            Q2_text = reading_bl_tr_Q2
            Q2_answers = reading_bl_tr_Q2_ans
            Q2_correct = reading_bl_tr_Q2_corr
        
            question, answers = setup_question(Q2_text, Q2_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q2_correct)
            print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q2')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q2_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter+1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # Setup for Q3
            Q3_text = reading_bl_tr_Q3
            Q3_answers = reading_bl_tr_Q3_ans
            Q3_correct = reading_bl_tr_Q3_corr
        
            question, answers = setup_question(Q3_text, Q3_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q3_correct)
            print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q3')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q3_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter+1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # go to next block!
            exp_block_counter += 1
            print(f"Going to block {exp_block_counter + 1}/20 now!")
            continueRoutine = False
        
            # If there are still blocks left, go to next one.
            # If not, end loop here:
            if exp_block_counter == 20:
                blocks.finished = True
                
        elif not skip_questions and not training_Qs:
            # Setup for Q1
            Q1_text = locals()[curr_text_nr + "_Q1"]
            Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
            Q1_correct = locals()[curr_text_nr + "_Q1_corr"]
        
            question, answers = setup_question(Q1_text, Q1_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q1_correct)
            print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q1')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q1_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter+1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # Setup for Q2
            Q2_text = locals()[curr_text_nr + "_Q2"]
            Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
            Q2_correct = locals()[curr_text_nr + "_Q2_corr"]
        
            question, answers = setup_question(Q2_text, Q2_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q2_correct)
            print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q2')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q2_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter+1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # Setup for Q3
            Q3_text = locals()[curr_text_nr + "_Q3"]
            Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
            Q3_correct = locals()[curr_text_nr + "_Q3_corr"]
        
            question, answers = setup_question(Q3_text, Q3_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q3_correct)
            print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q3')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q3_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter+1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # go to next block!
            exp_block_counter += 1
            print(f"Going to block {exp_block_counter + 1}/20 now!")
            continueRoutine = False
        
            # If there are still blocks left, go to next one.
            # If not, end loop here:
            if exp_block_counter == 20:
                blocks.finished = True
        # keep track of which components have finished
        text_blocks_self_pacedComponents = []
        for thisComponent in text_blocks_self_pacedComponents:
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
        
        # --- Run Routine "text_blocks_self_paced" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in text_blocks_self_pacedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "text_blocks_self_paced" ---
        for thisComponent in text_blocks_self_pacedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('text_blocks_self_paced.stopped', globalClock.getTime(format='float'))
        # the Routine "text_blocks_self_paced" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "text_blocks_paced" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('text_blocks_paced.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from paced_blocks
        #################################################
        #            Blocks with text – paced           #
        #################################################
        # this routine is for all blocks with texts that are paced, i.e., visually presented without space bar
        
        #---------- Calculate duration of words based on previous block ----------
        # We collected RTs & words from the self-paced block of each condition
        # for the training, we only use data from the reading BL since there is no separate training for 1- and 2-back
        
        # we calculate letter duration based on condition since participants need more time for n-back tasks than for baseline reading
        # BL reading blocks are based on duration during self-paced BL reading
        # 1- and 2-back blocks are based on their respective self-paced version
        
        # get block kind
        curr_block = all_blocks[exp_block_counter]
        
        if curr_block in ["Reading_Baseline_main_no_click", "Reading_Baseline_training_no_click"]:
        
            # exclude all RTs where participant was way too fast (< 50 ms) or
            # too slow (> 2s)
            #print("\tBL_paced_durations:", BL_paced_durations)
            #print("\tBL_paced_words:", BL_paced_words)
        
            filtered_durations_BL = []
            filtered_words_BL = []
            for duration, word in zip(BL_paced_durations, BL_paced_words):
                if 50 <= duration <= 1500:
                    filtered_durations_BL.append(duration)
                    filtered_words_BL.append(word)
            # print("\tfiltered_durations_BL:", filtered_durations_BL)
            # print("\tfiltered_words_BL:", filtered_words_BL)
        
            # Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
            letters_total_BL = sum(len(word) for word in filtered_words_BL)
            # print("\tletters_total_BL:", letters_total_BL)
            # also get time it took in total to read them all:
            reading_time_total_BL = sum(filtered_durations_BL)  # in ms
        
            # Now check how many words / min they read on average.
            # reading_speed_wpm = words_total / (reading_time_total/60000)
            # print("reading speed in words / min:" + str(reading_speed_wpm))
        
            # Check average RT / letter
            RT_per_letter_baseline = reading_time_total_BL / letters_total_BL
            print("\taverage RT per letter in ms:", RT_per_letter_baseline)
        
            # save this in the output csv:
            thisExp.addData('RT_per_letter_baseline', RT_per_letter_baseline)
        
        elif curr_block in ["0back_dual_main_no_click"]:
        
            # exclude all RTs where participant was way too fast (< 50 ms) or
            # too slow (> 2s)
            # print("\t0back_paced_durations:", zeroback_paced_durations)
            # print("\t0back_paced_words:", zeroback_paced_words)
        
            filtered_durations_0back = []
            filtered_words_0back = []
            for duration, word in zip(zeroback_paced_durations, zeroback_paced_words):
                if 50 <= duration <= 1500:
                    filtered_durations_0back.append(duration)
                    filtered_words_0back.append(word)
            # print("\tfiltered_durations_BL:", filtered_durations_BL)
            # print("\tfiltered_words_BL:", filtered_words_BL)
        
            # Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
            letters_total_0back = sum(len(word) for word in filtered_words_0back)
            # print("\tletters_total_0back:", letters_total_0back)
            # also get time it took in total to read them all:
            reading_time_total_0back = sum(filtered_durations_0back)  # in ms
        
            # Now check how many words / min they read on average.
            # reading_speed_wpm = words_total / (reading_time_total/60000)
            # print("reading speed in words / min:" + str(reading_speed_wpm))
        
            # Check average RT / letter
            RT_per_letter_0back = reading_time_total_0back / letters_total_0back
            print("\taverage RT per letter in ms 0-back:", RT_per_letter_0back)
        
            # save this in the output csv:
            thisExp.addData('RT_per_letter_0back', RT_per_letter_0back)
        
        elif curr_block in ["1back_dual_main_no_click"]:
        
            # exclude all RTs where participant was way too fast (< 50 ms) or
            # way too slow (> 2s), also remove the corresponding words from vis_task_words
            # print("\t1back_paced_durations:", oneback_paced_durations)
            # print("\t1back_paced_words:", oneback_paced_words)
        
            filtered_durations_1bck = []
            filtered_words_1bck = []
            for duration, word in zip(oneback_paced_durations, oneback_paced_words):
                if 50 <= duration <= 2000:
                    filtered_durations_1bck.append(duration)
                    filtered_words_1bck.append(word)
            # print("\tfiltered_durations_1bck:", filtered_durations_1bck)
            # print("\tfiltered_words_1bck:", filtered_words_1bck)
        
            # Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
            letters_total_1bck = sum(len(word) for word in filtered_words_1bck)
            # print("\tletters_total_1bck:", letters_total_1bck)
            # also get time it took in total to read them all:
            reading_time_total_1bck = sum(filtered_durations_1bck)  # in ms
        
            # Now check how many words / min they read on average.
            # reading_speed_wpm = words_total / (reading_time_total/60000)
            # print("reading speed in words / min:" + str(reading_speed_wpm))
        
            # Check average RT / letter
            RT_per_letter_1bck = reading_time_total_1bck / letters_total_1bck
            print("\taverage RT per letter in ms:", RT_per_letter_1bck)
        
            # save this in the output csv:
            thisExp.addData('RT_per_letter_1bck', RT_per_letter_1bck)
        
        elif curr_block in ["2back_dual_main_no_click"]:
        
            # exclude all RTs where participant was way too fast (< 50 ms) or
            # way too slow (> 2s), also remove the corresponding words from vis_task_words
            # print("\t2back_paced_durations:", twoback_paced_durations)
            # print("\t2back_paced_words:", twoback_paced_words)
        
            filtered_durations_2bck = []
            filtered_words_2bck = []
            for duration, word in zip(twoback_paced_durations, twoback_paced_words):
                if 50 <= duration <= 2500:
                    filtered_durations_2bck.append(duration)
                    filtered_words_2bck.append(word)
            # print("\tfiltered_durations_2bck:", filtered_durations_2bck)
            # print("\tfiltered_words_2bck:", filtered_words_2bck)
        
            # Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
            letters_total_2bck = sum(len(word) for word in filtered_words_2bck)
            # print("\tletters_total_2bck:", letters_total_2bck)
            # also get time it took in total to read them all:
            reading_time_total_2bck = sum(filtered_durations_2bck)  # in ms
        
            # Now check how many words / min they read on average.
            # reading_speed_wpm = words_total / (reading_time_total/60000)
            # print("reading speed in words / min:" + str(reading_speed_wpm))
        
            # Check average RT / letter
            RT_per_letter_2bck = reading_time_total_2bck / letters_total_2bck
            print("\taverage RT per letter in ms:", RT_per_letter_2bck)
        
            # save this in the output csv:
            thisExp.addData('RT_per_letter_2bck', RT_per_letter_2bck)
        
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
        
        # ----------------------------------
        
        # clear buffer of all previously recorded key events:
        event.clearEvents()
        
        ### Prepare stimuli:
        
        # Check whether it's a block that is self-paced
        # Also, if current block is a non-text block, skip this routine.
        if curr_block in ["click_training", "1back_single_training1", "1back_single_training2",
                          "2back_single_training1", "2back_single_training2",
                          "Reading_Baseline_main_click", "1back_dual_main_click", "2back_dual_main_click", "Reading_Baseline_training_click",
                          "1back_single_main_no_click", "2back_single_main_no_click", "0back_single_training", "0back_dual_main_click"]:
            print(f"this is block {curr_block}")
            print("\tskipping paced text routine")
            # skip questions & end current routine
            skip_questions_paced = True
            continueRoutine = False
            # break
        
        # if it's the paced reading training block, prepare training stimuli:
        elif curr_block == "Reading_Baseline_training_no_click":
            print(f"start preparing block {curr_block}")
        
            # keep background ivory
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
        
            ### Show instructions
            # set instruction text
            instr_text = locals()["instr_" + curr_block]
            # create text box
            instr_text_stim = visual.TextStim(win,
                                              text=instr_text,
                                              height=0.025,  # font height relative to height of screen
                                              pos=(0, 0),  # move up a bit
                                              color="black")
        
            # show instructions on screen
            win.setColor(light_bg_col, colorSpace='rgb')
            instr_text_stim.draw()
            win.flip()
            core.wait(3)  # wait for 3s before starting response window
        
            # display the text on screen
            while True:
                # keep background ivory
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim.draw()
                win.flip()
                # end showing screen if participant presses space
                if 'space' in event.getKeys():
                    break
        
            # clear buffer of all previously recorded key events:
            event.clearEvents()
        
            ### get training text
            curr_text_training = reading_bl_tr_text_no_click
            curr_text_nr = "Reading_Baseline_training_no_click"
            curr_text = curr_text_training
            curr_nback_cond = None
            # show training questions
            skip_questions_paced = False
            training_Qs_paced = True
        
            # get list with targets & list with colours
            curr_targets = all_target_lists[exp_block_counter]
            curr_colours = all_colour_lists[exp_block_counter]
        
            # compute RTs using participant's average reading speed / letter – old, based on linear increase of RTs,
            # feels very unnatural however
            # curr_durations = [len(word) * RT_per_letter_baseline for word in curr_text]  # in ms
        
            # compute RTs using participant's average reading speed / letter
            # we define a minimum and a maximum duration for each word
            # the minimum is based on 5 x RT per letter in the respective condition
            # the max duration is based on a time-out of 1.5 s in the reading baseline condition
            minimum_duration = 5 * RT_per_letter_baseline
            maximum_duration = 1500
            curr_durations = []
            for word in curr_text:
                # this is an absolute value based on estimates of how long you need to feel comfortable reading a word on
                # screen in a paced task
                # duration = RT_per_letter_baseline * math.log((len(word))) + 300
                # more flexible solution:
                duration = RT_per_letter_baseline * math.log((len(word))) + 4 * RT_per_letter_baseline
                if duration < maximum_duration:
                    curr_durations.append(max(duration, minimum_duration))
                else:
                    curr_durations.append(maximum_duration)
        
            # print(f"\tdurations for paced task training block: {curr_durations}")
        
            # we also need the start time (let's set it as current time
            # at this point in the script):
            start_time = core.getTime()
        
            ### change background colour
            win.setColor(dark_bg_col, colorSpace='rgb')
            win.flip()
        
        # if it's one of the "normal" main blocks, prepare main block stimuli:
        elif curr_block in ["Reading_Baseline_main_no_click", "0back_dual_main_no_click",
                            "1back_dual_main_no_click", "2back_dual_main_no_click"]:
            print(f"start preparing block {curr_block}")
        
            # keep background ivory
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
        
            ### Show instructions
            # only add image, if it's a 0-, 1- or 2-back block where participants have to press "c"
            if curr_block == "Reading_Baseline_main_no_click":
        
                # set instruction text
                instr_text = locals()["instr_" + curr_block]
                # create text box
                instr_text_stim = visual.TextStim(win,
                                                  text=instr_text,
                                                  height=0.025,  # font height relative to height of screen
                                                  pos=(0, 0),  # move up a bit
                                                  color="black")
        
                # show instructions on screen
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim.draw()
                win.flip()
                core.wait(3)  # wait for 3s before starting response window
        
                # Display the text on screen
                while True:
                    instr_text_stim.draw()
                    win.flip()
                    # end showing screen if participant presses space
                    if 'space' in event.getKeys():
                        break
        
                # get text nr:
                curr_text_nr = all_texts_nrs_list[exp_block_counter]
                curr_text = locals()[curr_text_nr]
        
                # compute RTs using participant's average reading speed / letter – old, based on linear increase of RTs,
                # feels very unnatural however
                # curr_durations = [len(word) * RT_per_letter_baseline for word in curr_text]  # in ms
        
                # compute RTs using participant's average reading speed / letter
                # we define a minimum and a maximum duration for each word
                # the minimum is based on 5 x RT per letter in the respective condition
                # the max duration is based on a time-out of 1.5 s in the reading baseline condition
                minimum_duration = 5 * RT_per_letter_baseline
                maximum_duration = 1500
                curr_durations = []
                for word in curr_text:
                    # this is an absolute value based on estimates of how long you need to feel comfortable reading a word on
                    # screen in a paced task
                    # duration = RT_per_letter_baseline * math.log((len(word))) + 300
                    # more flexible solution:
                    duration = RT_per_letter_baseline * math.log((len(word))) + 4 * RT_per_letter_baseline
                    if duration < maximum_duration:
                        curr_durations.append(max(duration, minimum_duration))
                    else:
                        curr_durations.append(maximum_duration)
        
                # print(f"\tdurations for paced baseline block: {curr_durations}")
        
                ### change background colour
                win.setColor(dark_bg_col, colorSpace='rgb')
                win.flip()
        
            elif curr_block == "0back_dual_main_no_click":
                # create text boxes
                instr_text_stim1 = visual.TextStim(win,
                                                   text=locals()["instr_0back_dual_main_no_click1"],
                                                   height=0.025,
                                                   pos=(0, 0.3),  # move instructions up a bit
                                                   color="black")
                instr_text_stim2 = visual.TextStim(win,
                                                   text=locals()["instr_0back_dual_main_no_click2"],
                                                   height=0.025,
                                                   pos=(0, -0.35),  # move instructions down a bit
                                                   color="black")
                # create "empty" circle as stimulus
                instr_colour_circle_stim = visual.Circle(win=win,
                                                         radius=0.065,
                                                         pos=(0, 0.075))  # move circle slightly down
        
                # set current target colour as colour of circle:
                instr_colour_circle_stim.fillColor = target_colours_list[2]
        
                # create ImageStim object
                curr_instr_pic = visual.ImageStim(win,
                                                  size=(0.55, 0.25),
                                                  pos=(0, -0.15),
                                                  image=locals()["instr_pic_0back_dual_no_click"])  # set path to image here
        
                # show instructions
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim1.draw()
                instr_text_stim2.draw()
                instr_colour_circle_stim.draw()
                curr_instr_pic.draw()
                win.flip()
                core.wait(3)  # wait for 3s before starting response window
        
                # display the text & the circle on screen until Space is pressed
                while True:
                    instr_text_stim1.draw()
                    instr_text_stim2.draw()
                    instr_colour_circle_stim.draw()
                    curr_instr_pic.draw()
                    win.flip()
                    # end screen if participant presses space
                    if event.getKeys(['space']):
                        break
        
                # get text nr:
                curr_text_nr = all_texts_nrs_list[exp_block_counter]
                curr_text = locals()[curr_text_nr]
        
                # compute RTs using participant's average reading speed / letter
                # we define a minimum and a maximum duration for each word
                # the minimum is based on 5 x RT per letter in the respective condition
                # the max duration is based on a time-out of 1.5 s in the 0-back condition
                minimum_duration = 5 * RT_per_letter_0back
                maximum_duration = 1500
                curr_durations = []
                for word in curr_text:
                    # this is an absolute value based on estimates of how long you need to feel comfortable reading a
                    # word on screen in a paced task
                    # duration = RT_per_letter_baseline * math.log((len(word))) + 300 more
                    # more flexible solution:
                    duration = RT_per_letter_0back * math.log((len(word))) + 4 * RT_per_letter_0back
                    if duration < maximum_duration:
                        curr_durations.append(max(duration, minimum_duration))
                    else:
                        curr_durations.append(maximum_duration)
        
                # Latency factor of an incremental increase (increment per trial = 3 ms) added over duration of entire
                # block assuming that participants get tired of the course of a 300 words block and thus need a bit more
                # time:
                # Increment of 3 ms per trial
                increment_per_trial = 3
                for i in range(len(curr_durations)):
                    # Calculate incremental increase for current trial
                    increment = i * increment_per_trial
                    # Add incremental increase to current trial's duration
                    curr_durations[i] += increment
        
                ### change background colour
                win.setColor(dark_bg_col, colorSpace='rgb')
                win.flip()
        
            elif curr_block in ["1back_dual_main_no_click", "2back_dual_main_no_click"]:
        
                # set instruction text
                instr_text = locals()["instr_" + curr_block]
                # create text box
                instr_text_stim = visual.TextStim(win,
                                                  text=instr_text,
                                                  height=0.025,  # font height relative to height of screen
                                                  pos=(0, 0.2),  # move up a bit
                                                  color="black")
                # create ImageStim object
                curr_instr_pic = visual.ImageStim(win,
                                                  size=(0.8, 0.3),
                                                  pos=(0, -0.2),
                                                  image=locals()["instr_pic_" + curr_block])  # set path to image here
        
                # show instructions on screen
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim.draw()
                curr_instr_pic.draw()
                win.flip()
                core.wait(3)  # wait for 3s before starting response window
        
                # Display the text on screen
                while True:
                    instr_text_stim.draw()
                    curr_instr_pic.draw()
                    win.flip()
                    # end showing screen if participant presses space
                    if 'space' in event.getKeys():
                        break
        
                # get text nr:
                curr_text_nr = all_texts_nrs_list[exp_block_counter]
                curr_text = locals()[curr_text_nr]
                # compute RTs using participant's average reading speed / letter
                if curr_block == "1back_dual_main_no_click":
                    # curr_durations = [len(word) * RT_per_letter_1bck for word in curr_text]  # in ms
        
                    # compute RTs using participant's average reading speed / letter
                    # we define a minimum and a maximum duration for each word
                    # the minimum is based on 5 x RT per letter in the respective condition
                    # the max duration is based on a time-out of 2 s in the 1-back condition
                    minimum_duration = 5 * RT_per_letter_1bck
                    maximum_duration = 2000
                    curr_durations = []
                    for word in curr_text:
                        # this is an absolute value based on estimates of how long you need to feel comfortable reading a
                        # word on screen in a paced task
                        # duration = RT_per_letter_baseline * math.log((len(word))) + 300 more
                        # more flexible solution:
                        duration = RT_per_letter_1bck * math.log((len(word))) + 4 * RT_per_letter_1bck
                        if duration < maximum_duration:
                            curr_durations.append(max(duration, minimum_duration))
                        else:
                            curr_durations.append(maximum_duration)
        
                    # Latency factor of an incremental increase (increment per trial = 3 ms) added over duration of entire
                    # block assuming that participants get tired of the course of a 300 words block and thus need a bit more
                    # time:
                    # Increment of 3 ms per trial
                    increment_per_trial = 3
                    for i in range(len(curr_durations)):
                        # Calculate incremental increase for current trial
                        increment = i * increment_per_trial
                        # Add incremental increase to current trial's duration
                        curr_durations[i] += increment
        
                elif curr_block == "2back_dual_main_no_click":
                    minimum_duration = 5 * RT_per_letter_2bck
                    maximum_duration = 2000
                    curr_durations = []
                    for word in curr_text:
                        # this is an absolute value based on estimates of how long you need to feel comfortable reading a word on
                        # screen in a paced task
                        # duration = RT_per_letter_baseline * math.log((len(word))) + 300
                        # more flexible solution:
                        duration = RT_per_letter_2bck * math.log((len(word))) + 4 * RT_per_letter_2bck
                        if duration < maximum_duration:
                            curr_durations.append(max(duration, minimum_duration))
                        else:
                            curr_durations.append(maximum_duration)
        
                    # Add increment of 3 ms per trial
                    increment_per_trial = 3
                    for i in range(len(curr_durations)):
                        # Calculate incremental increase for current trial
                        increment = i * increment_per_trial
                        # Add incremental increase to current trial's duration
                        curr_durations[i] += increment
        
                # print(f"\tdurations for paced n-back block: {curr_durations}")
        
                ### change background colour
                win.setColor(dark_bg_col, colorSpace='rgb')
                win.flip()
        
            # show main block questions
            skip_questions_paced = False
            training_Qs_paced = False
        
            # get n-back condition:
            curr_nback_cond = curr_block[0]  # get first character of block name
        
            # if it is a 0, 1 or 2, set that as current n-back level:
            if curr_nback_cond in ['0', '1', '2']:
                curr_nback_cond == int(curr_nback_cond)
            # if it's neither 1 nor 2, it has to be a block without n-back,
            # so set curr_nback_cond to None
            else:
                curr_nback_cond = None
        
            print(f"\tcurrent n-back condition: {curr_nback_cond}")
            print(f"\tcurrent text: {curr_text_nr}")
        
            # get list with targets & list with colours
            curr_targets = all_target_lists[exp_block_counter]
            curr_colours = all_colour_lists[exp_block_counter]
            # for current text nr, get text whose name = current text nr
            # curr_text = locals()[curr_text_nr]
        
        ### Start block loop
        if curr_block in ["Reading_Baseline_training_no_click", "Reading_Baseline_main_no_click", "0back_dual_main_no_click",
                          "1back_dual_main_no_click", "2back_dual_main_no_click"]:
        
            if curr_block == "0back_dual_main_no_click":
                zeroback_n_hits = 0
                zeroback_n_misses = 0
                zeroback_n_false_alarms = 0
                zeroback_n_correct_rejections = 0
            elif curr_block == "1back_dual_main_no_click":
                oneback_n_hits = 0
                oneback_n_misses = 0
                oneback_n_false_alarms = 0
                oneback_n_correct_rejections = 0
            elif curr_block == "2back_dual_main_no_click":
                twoback_n_hits = 0
                twoback_n_misses = 0
                twoback_n_false_alarms = 0
                twoback_n_correct_rejections = 0
        
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
        
            # clear the input buffer before starting the trial
            ser.flushInput()
            button_pressed = None
        
            # CREATE CLOCKS:
            my_block_clock = core.Clock()
            my_block_clock.reset()  # start block clock
            start_time = my_block_clock.getTime()  # get start time of block
            # also create trial clock
            my_trial_clock = core.Clock()
        
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
        
                # start trial clock & record trial onset time
                my_trial_clock.reset()
                onset_time = my_trial_clock.getTime()
        
                ### wait for key response:
                # In blocks with n-back task, participants can press button 1 on the button box to indicate they saw a target colour.
        
                ### start recording responses
                # start while loop that looks for responses
                # --> end while loop only if duration for current word is over
                while my_trial_clock.getTime() < (onset_time + curr_duration):
        
                    stim.draw()
                    win.flip()
        
                    # check for key responses:
                    keys = event.getKeys(['escape'])
                    if 'escape' in keys:
                        core.wait(0.5)
                        core.quit()
        
                    # Calculate remaining time for the stimulus
                    remaining_time = (onset_time + curr_duration) - my_trial_clock.getTime()
                    ser.timeout = remaining_time
        
                    # Check for button box responses
                    response = ser.read()
                    if response:
                        button_pressed = response.hex()
                        if button_pressed == '01' and curr_nback_cond is not None and not saw_target:
                            # Get reaction time
                            curr_nback_RT = my_trial_clock.getTime() * 1000
                            # Send trigger for response:
                            # send_trigger("response_target")
                            # Only get first target response, we don't care if they press the button more than once:
                            saw_target = True
        
                    # # if there were, check responses:
                    # for resp in response:
                    #
                    #     # if participant pressed button "c" for the first time and it's an n-back condition
                    #     # where they're actually supposed to do that (aka not a reading baseline condition)...
                    #     if resp == 'c' and curr_nback_cond != None and saw_target == False:
                    #         # get reaction time
                    #         curr_nback_RT = my_trial_clock.getTime() * 1000
                    #         # send trigger for response:
                    #         # send_trigger("response_target")
                    #         # only get first target response, we don't care if they press the button more than once:
                    #         saw_target = True
                    #
                    #     # If esc is pressed, end the experiment:
                    #     elif key == 'escape':
                    #         # et_abort_exp()  # shut down eyetrigger and download incremental data
                    #         # close trigger & close experiment
                    #         # core.wait(time_after_trigger)
                    #         # parallel.setData(0)
                    #         core.wait(0.5)
                    #         core.quit()
        
                ### end trial
                # print("\tend paced trial")
                # stop display of current word & send trial offset trigger
                # win.callOnFlip(send_trigger, "trial_offset")
        
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
                if curr_block == "0back_dual_main_no_click":
                    thisExp.addData('curr_0back_target', target_colours_list[2])
                thisExp.addData('button_pressed', button_pressed)
                thisExp.addData('nback_response', curr_nback_response)
                thisExp.addData('nback_RT', curr_nback_RT)  # in ms
                thisExp.addData('duration', curr_duration * 1000)  # in ms
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
        
                if curr_block == "0back_dual_main_no_click":
                    if curr_nback_response == "hit":
                        zeroback_n_hits += 1
                    elif curr_nback_response == "miss":
                        zeroback_n_misses += 1
                    elif curr_nback_response == "false alarm":
                        zeroback_n_false_alarms += 1
                    elif curr_nback_response == "correct rejection":
                        zeroback_n_correct_rejections += 1
                elif curr_block == "1back_dual_main_no_click":
                    if curr_nback_response == "hit":
                        oneback_n_hits += 1
                    elif curr_nback_response == "miss":
                        oneback_n_misses += 1
                    elif curr_nback_response == "false alarm":
                        oneback_n_false_alarms += 1
                    elif curr_nback_response == "correct rejection":
                        oneback_n_correct_rejections += 1
                elif curr_block == "2back_dual_main_no_click":
                    if curr_nback_response == "hit":
                        twoback_n_hits += 1
                    elif curr_nback_response == "miss":
                        twoback_n_misses += 1
                    elif curr_nback_response == "false alarm":
                        twoback_n_false_alarms += 1
                    elif curr_nback_response == "correct rejection":
                        twoback_n_correct_rejections += 1
        
                ### IF TESTING MODE ENABLED: end loop after 4 trials
                if expInfo['testing_mode'] == "yes":
                    if trial_idx == 3:
                        break
        
            print("finished presenting trials")
        # Run 'Begin Routine' code from questions_paced
        ##########################################################
        #              Text Comprehension Questions              #
        ##########################################################
        
        def setup_question(question_text, answers_text):
            question = visual.TextStim(win, text=question_text, pos=(0, 0.2), color="black", height=0.03, anchorHoriz='center',
                                       alignText='center', wrapWidth=1)
            answers = [visual.TextStim(win, text=ans, pos=(0, 0.1 - i * 0.08), color="black", height=0.03, wrapWidth=1,
                                       anchorHoriz='center', alignText='center') for i, ans in enumerate(answers_text)]
            return question, answers
        
        
        def display_question_and_get_response(question, answers, correct_answer):
            defaultKeyboard.clearEvents()
        
            # Set-up time to write into logfile
            question_time = globalClock.getTime()
        
            question.autoDraw = True
            for answer in answers:
                answer.autoDraw = True
            instr_text.autoDraw = True
        
            countdown_timer = visual.TextStim(win, text='', pos=(0, -0.25), color="grey", height=0.02, anchorHoriz='center',
                                              alignText='center', wrapWidth=1)
        
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
        
                if ser.in_waiting > 0:
                    response = ser.read()
                    button_pressed = response.hex()
        
                    if button_pressed == '01':
                        index = 0  # Corresponds to the first choice
                    elif button_pressed == '02':
                        index = 1  # Corresponds to the second choice
                    elif button_pressed == '03':
                        index = 2  # Corresponds to the third choice
                    elif button_pressed == '04':
                        index = 3  # Corresponds to the fourth choice
                    else:
                        index = None  # Just in case, not really needed if you're sure about the input keys
        
                # keys = defaultKeyboard.getKeys(['1', '2', '3', '4'], waitRelease=False)
                # if keys:
                #     key_name = keys[0].name  # Get the name of the first key pressed
                #     button_pressed = key_name
                #
                #     # Now, use the key_name to determine the action
                #     if key_name == '1':
                #         index = 0  # Corresponds to the first choice
                #     elif key_name == '2':
                #         index = 1  # Corresponds to the second choice
                #     elif key_name == '3':
                #         index = 2  # Corresponds to the third choice
                #     elif key_name == '4':
                #         index = 3  # Corresponds to the fourth choice
                #     else:
                #         index = None  # Just in case, not really needed if you're sure about the input keys
        
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
        
            return question_time, chosen_ans, is_correct, button_pressed
        
        
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
        instr_text = visual.TextStim(win,
                                     text="(Bitte benutzen Sie die Tasten 1, 2, 3 und 4, um die richtige Antwort auszuwählen.)",
                                     color="grey", pos=(0, -0.3), wrapWidth=2, height=0.018)
        event.clearEvents()
        
        # Assuming skip_questions_paced and other variables are defined
        if not skip_questions_paced and training_Qs_paced:
            # Setup for Q1
            Q1_text = reading_bl_tr_no_click_Q1
            Q1_answers = reading_bl_tr_no_click_Q1_ans
            Q1_correct = reading_bl_tr_no_click_Q1_corr
        
            question, answers = setup_question(Q1_text, Q1_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers,
                                                                                                      Q1_correct)
            print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q1')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q1_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # Setup for Q2
            Q2_text = reading_bl_tr_no_click_Q2
            Q2_answers = reading_bl_tr_no_click_Q2_ans
            Q2_correct = reading_bl_tr_no_click_Q2_corr
        
            question, answers = setup_question(Q2_text, Q2_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers,
                                                                                                      Q2_correct)
            print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q2')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q2_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # Setup for Q3
            Q3_text = reading_bl_tr_no_click_Q3
            Q3_answers = reading_bl_tr_no_click_Q3_ans
            Q3_correct = reading_bl_tr_no_click_Q3_corr
        
            question, answers = setup_question(Q3_text, Q3_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers,
                                                                                                      Q3_correct)
            print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q3')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q3_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # go to next block!
            exp_block_counter += 1
            print(f"Going to block {exp_block_counter + 1}/20 now!")
            continueRoutine = False
        
            # If there are still blocks left, go to next one.
            # If not, end loop here:
            if exp_block_counter == 20:
                blocks.finished = True
        
        elif not skip_questions_paced and not training_Qs_paced:
            # Save n of correct questions in variables for output at the end of the training
            if curr_block == "0back_dual_main_no_click":
                zeroback_correct_answers = 0
            elif curr_block == "1back_dual_main_no_click":
                oneback_correct_answers = 0
            elif curr_block == "2back_dual_main_no_click":
                twoback_correct_answers = 0
        
            # Setup for Q1
            Q1_text = locals()[curr_text_nr + "_Q1"]
            Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
            Q1_correct = locals()[curr_text_nr + "_Q1_corr"]
        
            question, answers = setup_question(Q1_text, Q1_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers,
                                                                                                      Q1_correct)
            print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
            if curr_block == "0back_dual_main_no_click" and is_correct:
                zeroback_correct_answers += 1
            elif curr_block == "1back_dual_main_no_click" and is_correct:
                oneback_correct_answers += 1
            elif curr_block == "2back_dual_main_no_click" and is_correct:
                twoback_correct_answers += 1
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q1')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q1_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # Setup for Q2
            Q2_text = locals()[curr_text_nr + "_Q2"]
            Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
            Q2_correct = locals()[curr_text_nr + "_Q2_corr"]
        
            question, answers = setup_question(Q2_text, Q2_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers,
                                                                                                      Q2_correct)
            print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
            if curr_block == "0back_dual_main_no_click" and is_correct:
                zeroback_correct_answers += 1
            elif curr_block == "1back_dual_main_no_click" and is_correct:
                oneback_correct_answers += 1
            elif curr_block == "2back_dual_main_no_click" and is_correct:
                twoback_correct_answers += 1
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q2')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q2_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # Setup for Q3
            Q3_text = locals()[curr_text_nr + "_Q3"]
            Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
            Q3_correct = locals()[curr_text_nr + "_Q3_corr"]
        
            question, answers = setup_question(Q3_text, Q3_answers)
            question_time, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers,
                                                                                                      Q3_correct)
            print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
            if curr_block == "0back_dual_main_no_click" and is_correct:
                zeroback_correct_answers += 1
            elif curr_block == "1back_dual_main_no_click" and is_correct:
                oneback_correct_answers += 1
            elif curr_block == "2back_dual_main_no_click" and is_correct:
                twoback_correct_answers += 1
            reset_answers(answers)
        
            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('question', 'Q3')
            thisExp.addData('button_pressed', button_pressed)
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q3_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)
        
            # start a new row in the csv
            thisExp.nextEntry()
        
            # go to next block!
            exp_block_counter += 1
            print(f"Going to block {exp_block_counter + 1}/20 now!")
            continueRoutine = False
        
            # If there are still blocks left, go to next one.
            # If not, end loop here:
            if exp_block_counter == 20:
                blocks.finished = True
        # keep track of which components have finished
        text_blocks_pacedComponents = []
        for thisComponent in text_blocks_pacedComponents:
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
        
        # --- Run Routine "text_blocks_paced" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in text_blocks_pacedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "text_blocks_paced" ---
        for thisComponent in text_blocks_pacedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('text_blocks_paced.stopped', globalClock.getTime(format='float'))
        # the Routine "text_blocks_paced" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "no_text_blocks_paced" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('no_text_blocks_paced.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from no_text_no_click
        #################################################
        #            Blocks w/o text – paced            #
        #################################################
        # this routine is for all blocks where there are
        # coloured rectangles instead of words and participants are presented with a paced version, i.e., rectangles are presented based on their reaction times in a
        
        # Use loop here that runs the non-text blocks
        # until we have to display a main text block (in this case we exit the routine).
        
        event. Mouse(visible=False)
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
        
        # clear buffer of all previously recorded key events:
        event.clearEvents()
        
        ### Prepare stimuli:
        
        # get block kind
        curr_block = all_blocks[exp_block_counter]
        # print("start preparing block " + curr_block)
        
        # Check whether it's one of the non-text tasks.
        # If current block is a text block, skip this routine and go to the next.
        if curr_block not in ["1back_single_main_no_click", "2back_single_main_no_click"]:
            print(f"this is block {curr_block}")
            print("\tskipping paced non-text routine")
            # skip questions & end current routine
            # skip_questions = True
            continueRoutine = False
            # break
        
        else:
            print(f"\tstart preparing block {curr_block}")
            if curr_block == "1back_single_main_no_click":
        
                # exclude all RTs where participant was way too fast (< 50 ms) or
                # too slow (> 1.5 s)
                # print("\toneback_single_paced_durations:", oneback_single_paced_durations)
        
                filtered_durations_oneback_single = []
                for duration in oneback_single_paced_durations:
                    if 50 <= duration <= 1500:
                        filtered_durations_oneback_single.append(duration)
                # count n of trials:
                oneback_single_trials = len(filtered_durations_oneback_single)
                # get time it took in total:
                oneback_single_time_total = sum(filtered_durations_oneback_single)  # in ms
        
        
                # Check average RT / rectangle
                RT_per_rectangle_oneback_single = oneback_single_time_total / oneback_single_trials
                print("\taverage RT per rectangle in ms for single 1back:", RT_per_rectangle_oneback_single)
        
                # save this in the output csv:
                thisExp.addData('RT_per_rect_1back_single', RT_per_rectangle_oneback_single)
        
            elif curr_block == "2back_single_main_no_click":
        
                # exclude all RTs where participant was way too fast (< 50 ms) or
                # too slow (> 2.0 s)
                # print("\ttwoback_single_paced_durations:", twoback_single_paced_durations)
        
                filtered_durations_twoback_single = []
                for duration in twoback_single_paced_durations:
                    if 50 <= duration <= 2000:
                        filtered_durations_twoback_single.append(duration)
                # count n of trials:
                twoback_single_trials = len(filtered_durations_twoback_single)
                # get time it took in total:
                twoback_single_time_total = sum(filtered_durations_twoback_single)  # in ms
        
                # Check average RT / rectangle
                RT_per_rectangle_twoback_single = twoback_single_time_total / twoback_single_trials
                print("\taverage RT per rectangle in ms for single 2back:", RT_per_rectangle_twoback_single)
        
                # save this in the output csv:
                thisExp.addData('RT_per_rect_2back_single', RT_per_rectangle_twoback_single)
        
        
            # keep background ivory
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
        
            ### Show instructions
            # set instruction text
            instr_text = locals()["instr_" + curr_block]
            # create text box
            instr_text_stim = visual.TextStim(win,
                                              text=instr_text,
                                              height=0.025,  # font height relative to height of screen
                                              pos=(0, 0.2),  # move up a bit
                                              color="black")
            # create ImageStim object
            curr_instr_pic = visual.ImageStim(win,
                                              size=(0.8, 0.3),
                                              pos=(0, -0.2),
                                              image=locals()["instr_pic_" + curr_block])  # set path to image here
        
            # show instructions on screen
            instr_text_stim.draw()
            curr_instr_pic.draw()
            win.flip()
            core.wait(3)  # wait for 3s before starting response window
        
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
        
            ### change background colour
            win.setColor(dark_bg_col, colorSpace='rgb')
            win.flip()
        
            # don't show questions
            skip_questions = True
            training_Qs = False
        
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
            curr_targets = all_target_lists[exp_block_counter]
            curr_colours = all_colour_lists[exp_block_counter]
        
            # determine duration per rectangle for this block
            # we use average time per rectangle as duration here and add an increment over the duration of the block
            if curr_block == "1back_single_main_no_click":
                curr_durations = []
                for rect in curr_targets:
                    curr_durations.append(RT_per_rectangle_oneback_single)
        
                # Latency factor of an incremental increase (increment per trial = 3 ms) added over duration of entire
                # block assuming that participants get tired of the course of the block and thus need a bit more
                # time:
                # Increment of 3 ms per trial
                increment_per_trial = 3
                for i in range(len(curr_durations)):
                    # Calculate incremental increase for current trial
                    increment = i * increment_per_trial
                    # Add incremental increase to current trial's duration
                    curr_durations[i] += increment
        
            elif curr_block == "2back_single_main_no_click":
                curr_durations = []
                for rect in curr_targets:
                    curr_durations.append(RT_per_rectangle_twoback_single)
        
                # Latency factor of an incremental increase (increment per trial = 3 ms) added over duration of entire
                # block assuming that participants get tired of the course of the block and thus need a bit more
                # time:
                # Increment of 3 ms per trial
                increment_per_trial = 3
                for i in range(len(curr_durations)):
                    # Calculate incremental increase for current trial
                    increment = i * increment_per_trial
                    # Add incremental increase to current trial's duration
                    curr_durations[i] += increment
        
            ### Start block loop
        
            if curr_block == "1back_single_main_no_click":
                oneback_single_n_hits = 0
                oneback_single_n_misses = 0
                oneback_single_n_false_alarms = 0
                oneback_single_n_correct_rejections = 0
            elif curr_block == "2back_single_main_no_click":
                twoback_single_n_hits = 0
                twoback_single_n_misses = 0
                twoback_single_n_false_alarms = 0
                twoback_single_n_correct_rejections = 0
        
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
        
            # loop colours in current text
            for trial_idx, curr_col in enumerate(curr_colours):
                # print("current idx: " + str(trial_idx) + ", curr colour:" + curr_col)
        
                # clear buffer of all previously recorded key events:
                event.clearEvents()
        
                # clear the input buffer before starting the trial
                ser.flushInput()
                button_pressed = None
        
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
                # the stimulus
        
                # start trial clock for measuring RTs from stimulus onset
                my_trial_clock.reset()
                onset_time = my_trial_clock.getTime()
        
                ### start recording responses
                # start while loop that looks for responses
                # --> end while loop only if duration for current word is over
                while my_trial_clock.getTime() < (onset_time + curr_duration):
        
                    stim.draw()
                    win.flip()
        
                    # check for key responses:
                    keys = event.getKeys(['escape'])
                    if 'escape' in keys:
                        core.wait(0.5)
                        core.quit()
        
                    # Calculate remaining time for the stimulus
                    remaining_time = (onset_time + curr_duration) - my_trial_clock.getTime()
                    ser.timeout = remaining_time
        
                    # Check for button box responses
                    response = ser.read()
                    if response:
                        button_pressed = response.hex()
                        if button_pressed == '01' and curr_nback_cond is not None and not saw_target:
                            # Get reaction time
                            curr_nback_RT = my_trial_clock.getTime() * 1000
                            # Send trigger for response:
                            # send_trigger("response_target")
                            # Only get first target response, we don't care if they press the button more than once:
                            saw_target = True
        
                ### end trial
                # print("end paced rect trial")
        
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
                thisExp.addData('colour', curr_col)
                thisExp.addData('target', curr_target)
                thisExp.addData('button_pressed', button_pressed)
                thisExp.addData('nback_response', curr_nback_response)
                thisExp.addData('nback_RT', curr_nback_RT)  # in ms
                thisExp.addData('duration', curr_duration)  # in ms
                thisExp.addData('trial_nr', curr_trial_nr)
                thisExp.addData('block_nr', exp_block_counter)
                thisExp.addData('block_name', curr_block)
                thisExp.addData('block_kind', curr_nback_cond)
        
                # start a new row in the csv
                thisExp.nextEntry()
        
                if curr_block == "1back_single_main_no_click":
                    if curr_nback_response == "hit":
                        oneback_single_n_hits += 1
                    elif curr_nback_response == "miss":
                        oneback_single_n_misses += 1
                    elif curr_nback_response == "false alarm":
                        oneback_single_n_false_alarms += 1
                    elif curr_nback_response == "correct rejection":
                        oneback_single_n_correct_rejections += 1
                elif curr_block == "2back_single_main_no_click":
                    if curr_nback_response == "hit":
                        twoback_single_n_hits += 1
                    elif curr_nback_response == "miss":
                        twoback_single_n_misses += 1
                    elif curr_nback_response == "false alarm":
                        twoback_single_n_false_alarms += 1
                    elif curr_nback_response == "correct rejection":
                        twoback_single_n_correct_rejections += 1
        
                ### IF TESTING MODE ENABLED: end loop after 4 trials
                if expInfo['testing_mode'] == "yes":
                    if trial_idx == 3:
                        break
        
            print("\t\tfinished presenting trials")
        
            # change background colour from grey (RGB: 10, 10, 10)
            # to ivory (RGB: 240, 223, 204)
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
        
            # add 1 to the block counter to go load the next block
            exp_block_counter = exp_block_counter + 1
            print(f"\tGoing to block {exp_block_counter + 1}/20 now!")
        
            # go to next routine
            # print("going to next routine")
            continueRoutine = False
        # keep track of which components have finished
        no_text_blocks_pacedComponents = []
        for thisComponent in no_text_blocks_pacedComponents:
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
        
        # --- Run Routine "no_text_blocks_paced" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in no_text_blocks_pacedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "no_text_blocks_paced" ---
        for thisComponent in no_text_blocks_pacedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('no_text_blocks_paced.stopped', globalClock.getTime(format='float'))
        # the Routine "no_text_blocks_paced" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pseudotext" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('pseudotext.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from pseudotext_paced_block
        #################################################
        #            Blocks with text – paced           #
        #################################################
        # this routine is for all blocks with texts that are paced, i.e., visually presented without space bar
        
        #---------- Calculate duration of words based on previous block ----------
        # We collected RTs & words from the self-paced block of each condition
        # for the training, we only use data from the reading BL since there is no separate training for 1- and 2-back
        
        # we calculate letter duration based on condition since participants need more time for n-back tasks than for baseline reading
        # BL reading blocks are based on duration during self-paced BL reading
        # 1- and 2-back blocks are based on their respective self-paced version
        
        # get block kind
        curr_block = all_blocks[exp_block_counter]
        
        if curr_block == "Reading_pseudotext_no_click":
        
            # exclude all RTs where participant was way too fast (< 50 ms) or
            # way too slow (> 2s), also remove the corresponding words from vis_task_words
            # print("\tBL_paced_durations:", BL_paced_durations)
            # print("\tBL_paced_words:", BL_paced_words)
        
            filtered_durations_BL = []
            filtered_words_BL = []
            for duration, word in zip(BL_paced_durations, BL_paced_words):
                if 50 <= duration <= 1500:
                    filtered_durations_BL.append(duration)
                    filtered_words_BL.append(word)
            # print("\tfiltered_durations_BL:", filtered_durations_BL)
            # print("\tfiltered_words_BL:", filtered_words_BL)
        
            # Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
            letters_total_BL = sum(len(word) for word in filtered_words_BL)
            # print("\tletters_total_BL:", letters_total_BL)
            # also get time it took in total to read them all:
            reading_time_total_BL = sum(filtered_durations_BL)  # in ms
        
            # Now check how many words / min they read on average.
            # reading_speed_wpm = words_total / (reading_time_total/60000)
            # print("reading speed in words / min:" + str(reading_speed_wpm))
        
            # Check average RT / letter
            RT_per_letter_baseline = reading_time_total_BL / letters_total_BL
            print("\taverage RT per letter in ms:", RT_per_letter_baseline)
        
            # save this in the output csv:
            thisExp.addData('RT_per_letter_baseline', RT_per_letter_baseline)
        
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
        
        # ----------------------------------
        
        # clear buffer of all previously recorded key events:
        event.clearEvents()
        
        ### specify settings for the current block
        
        ### Prepare stimuli:
        
        # get block kind
        curr_block = all_blocks[exp_block_counter]
        # print("start preparing block " + curr_block)
        
        # if it's the paced reading training block, prepare training stimuli:
        if curr_block == "Reading_pseudotext_no_click":
            print(f"start preparing block {curr_block}")
        
            # keep background ivory
            win.setColor(light_bg_col, colorSpace='rgb')
            win.flip()
        
            ### Show instructions
            # set instruction text
            instr_text = locals()["instr_" + curr_block]
            # create text box
            instr_text_stim = visual.TextStim(win,
                                              text=instr_text,
                                              height=0.025,  # font height relative to height of screen
                                              pos=(0, 0),  # move up a bit
                                              color="black")
        
            # show instructions on screen
            win.setColor(light_bg_col, colorSpace='rgb')
            instr_text_stim.draw()
            win.flip()
            core.wait(3)  # wait for 3s before starting response window
        
            # display the text on screen
            while True:
                # keep background ivory
                win.setColor(light_bg_col, colorSpace='rgb')
                instr_text_stim.draw()
                win.flip()
                # end showing screen if participant presses space
                if 'space' in event.getKeys():
                    break
        
            # clear buffer of all previously recorded key events:
            event.clearEvents()
        
            ### get training text
            curr_text_training = reading_ps_text_no_click
            curr_text_nr = "Reading_pseudotext_no_click"
            curr_text = curr_text_training
            curr_nback_cond = None
            # show training questions
            skip_questions_paced = True
            training_Qs_paced = False
        
            # get list with targets & list with colours
            curr_targets = all_target_lists[exp_block_counter]
            curr_colours = all_colour_lists[exp_block_counter]
        
            # compute RTs using participant's average reading speed / letter – old, based on linear increase of RTs,
            # feels very unnatural however
            # curr_durations = [len(word) * RT_per_letter_baseline for word in curr_text]  # in ms
        
            # compute RTs using participant's average reading speed / letter
            # we define a minimum and a maximum duration for each word
            # the minimum is based on 5 x RT per letter in the respective condition
            # the max duration is based on a time-out of 1.5 s in the reading baseline condition
            minimum_duration = 5 * RT_per_letter_baseline
            maximum_duration = 1500
            curr_durations = []
            for word in curr_text:
                # this is an absolute value based on estimates of how long you need to feel comfortable reading a word on
                # screen in a paced task
                # duration = RT_per_letter_baseline * math.log((len(word))) + 300
                # more flexible solution:
                duration = RT_per_letter_baseline * math.log((len(word))) + 4 * RT_per_letter_baseline
                if duration < maximum_duration:
                    curr_durations.append(max(duration, minimum_duration))
                else:
                    curr_durations.append(maximum_duration)
        
            # print(f"\tdurations for paced task training block: {curr_durations}")
        
            # we also need the start time (let's set it as current time
            # at this point in the script):
            start_time = core.getTime()
        
            ### change background colour
            win.setColor(dark_bg_col, colorSpace='rgb')
            win.flip()
        
        ### Start block loop
        if curr_block == "Reading_pseudotext_no_click":
        
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
        
            # CREATE CLOCKS:
            my_block_clock = core.Clock()
            my_block_clock.reset()  # start block clock
            start_time = my_block_clock.getTime()  # get start time of block
            # also create trial clock
            my_trial_clock = core.Clock()
        
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
        
                # start trial clock & record trial onset time
                my_trial_clock.reset()
                onset_time = my_trial_clock.getTime()
        
                ### wait for key response:
                # In blocks with n-back task, participants can press "c" to indicate they saw a target colour.
        
                ### start recording responses
                # start while loop that looks for responses
                # --> end while loop only if duration for current word is over
                while my_trial_clock.getTime() < (onset_time + curr_duration):
        
                    stim.draw()
                    win.flip()
        
                    # check for key responses:
                    keys = event.getKeys(['c', 'escape'])
        
                    # if there were, check responses:
                    for key in keys:
        
                        # if participant pressed button "c" for the first time and it's an n-back condition
                        # where they're actually supposed to do that (aka not a reading baseline condition)...
                        if key == 'c' and curr_nback_cond != None and saw_target == False:
                            # get reaction time
                            curr_nback_RT = my_trial_clock.getTime() * 1000
                            # send trigger for response:
                            # send_trigger("response_target")
                            # only get first target response, we don't care if they press the button more than once:
                            saw_target = True
        
                        # If esc is pressed, end the experiment:
                        elif key == 'escape':
                            # et_abort_exp()  # shut down eyetrigger and download incremental data
                            # close trigger & close experiment
                            # core.wait(time_after_trigger)
                            # parallel.setData(0)
                            core.wait(0.5)
                            core.quit()
        
                ### end trial
                # print("\tend paced pseudoword trial")
                # stop display of current word & send trial offset trigger
                # win.callOnFlip(send_trigger, "trial_offset")
        
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
                thisExp.addData('nback_RT', curr_nback_RT)  # in ms
                thisExp.addData('duration', curr_duration * 1000)  # in ms
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
        
                ### IF TESTING MODE ENABLED: end loop after 4 trials
                if expInfo['testing_mode'] == "yes":
                    if trial_idx == 3:
                        break
        
            print("finished presenting trials")
        
            # go to next block!
            exp_block_counter += 1
            print(f"Going to block {exp_block_counter + 1}/20 now!")
            continueRoutine = False
        
            # If there are still blocks left, go to next one.
            # If not, end loop here:
            if exp_block_counter == 20:
                blocks.finished = True
        
            # Send end of block trigger:
            # core.wait(time_after_trigger)  # wait 3 ms
            # send block offset trigger
            # send_trigger("block_offset")
        
        # end current routine
        # continueRoutine = False
        # keep track of which components have finished
        pseudotextComponents = []
        for thisComponent in pseudotextComponents:
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
        
        # --- Run Routine "pseudotext" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pseudotextComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pseudotext" ---
        for thisComponent in pseudotextComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('pseudotext.stopped', globalClock.getTime(format='float'))
        # the Routine "pseudotext" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 30.0 repeats of 'blocks'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from end
    ### END OF EXPERIMENT:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    
    ### Show message
    # set text
    instr_text = "Vielen Dank,\ndas Training ist nun zu Ende!\n\n\nIm MRT folgen nun erneut die Blöcke ohne die 'Weiter'-Taste.\nSie drücken also dann nur eine Taste in den Blöcken mit 1- oder 2-Zurück.\n\nViel Spaß!"
    
    # create text box
    instr_text_stim = visual.TextStim(win,
                                      text = instr_text,
                                      height = 0.03,
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
            print(f"Ending experiment now!")
            print(f"This is how the participant performed during the paced version:")
            print(f"\t0-back dual blocks:")
            print(f"\t\thits: {zeroback_n_hits}")
            print(f"\t\tmisses: {zeroback_n_misses}")
            print(f"\t\tfalse alarms: {zeroback_n_false_alarms}")
            print(f"\t\tcorrect rejections: {zeroback_n_correct_rejections}")
            print(f"\t\tcorrect answers to questions: {zeroback_correct_answers}")
            print(f"\t1-back single blocks:")
            print(f"\t\thits: {oneback_single_n_hits}")
            print(f"\t\tmisses: {oneback_single_n_misses}")
            print(f"\t\tfalse alarms: {oneback_single_n_false_alarms}")
            print(f"\t\tcorrect rejections: {oneback_single_n_correct_rejections}")
            print(f"\t2-back single blocks:")
            print(f"\t\thits: {twoback_single_n_hits}")
            print(f"\t\tmisses: {twoback_single_n_misses}")
            print(f"\t\tfalse alarms: {twoback_single_n_false_alarms}")
            print(f"\t\tcorrect rejections: {twoback_single_n_correct_rejections}")
            print(f"\t1-back dual blocks:")
            print(f"\t\thits: {oneback_n_hits}")
            print(f"\t\tmisses: {oneback_n_misses}")
            print(f"\t\tfalse alarms: {oneback_n_false_alarms}")
            print(f"\t\tcorrect rejections: {oneback_n_correct_rejections}")
            print(f"\t\tcorrect answers to questions: {oneback_correct_answers}")
            print(f"\t2-back dual blocks:")
            print(f"\t\thits: {twoback_n_hits}")
            print(f"\t\tmisses: {twoback_n_misses}")
            print(f"\t\tfalse alarms: {twoback_n_false_alarms}")
            print(f"\t\tcorrect rejections: {twoback_n_correct_rejections}")
            print(f"\t\tcorrect answers to questions: {twoback_correct_answers}")
            print(f"These are the RTs for the fMRI experiment:")
            print(f"RT_per_rect_1back_single: {RT_per_rectangle_oneback_single}")
            print(f"RT_per_rect_2back_single: {RT_per_rectangle_twoback_single}")
            print(f"\tRT_per_letter_baseline: {RT_per_letter_baseline}")
            print(f"\tRT_per_letter_0back: {RT_per_letter_0back}")
            print(f"\tRT_per_letter_1back: {RT_per_letter_1bck}")
            print(f"\tRT_per_letter_2back: {RT_per_letter_2bck}")
            
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
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
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
    thisExp.addData('end.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='tab')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
