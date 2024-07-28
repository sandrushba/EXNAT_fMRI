#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.0),
    on Sun Jul 28 10:04:38 2024
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
expName = 'EXNAT_3_fMRI'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': 'sub-',
    'session': '001',
    'testing_mode': 'yes',
    'RT_per_rectangle_oneback_single': '90',
    'RT_per_rectangle_twoback_single': '90',
    'RT_per_letter_baseline': '90',
    'RT_per_letter_oneback_dual': '90',
    'RT_per_letter_twoback_dual': '90',
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
_loggingLevel = logging.getLevel('warning')
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
    filename = u'Analysis/Data_EXNAT_3_fMRI/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)

    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/sandramartin/ownCloud/EXNAT/EXNAT_fMRI/Psychopy_experiment/EXNAT_3_fMRI/EXNAT_3_fMRI.py',
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
    logFile = logging.LogFile(filename + '.log', level=_loggingLevel)

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
            size=[1470, 956], fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0, 0, 0]
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
    # for calculations
    import math

    # Get functions from my custom scripts:
    # import all texts and instructions
    from EXNAT3_texts_MC_Qs import (instr_pic_path, welcome_text, instr_Reading_Baseline_main_no_click,
                                    instr_Reading_pseudotext_no_click, \
                                    instr_1back_single_main_no_click, instr_pic_1back_single_main_no_click,
                                    instr_1back_dual_main_no_click, \
                                    instr_pic_1back_dual_main_no_click, instr_2back_single_main_no_click,
                                    instr_pic_2back_single_main_no_click, instr_2back_dual_main_no_click, \
                                    instr_pic_2back_dual_main_no_click, warning_sign, text_01, text_01_Q1,
                                    text_01_Q1_ans, text_01_Q1_corr, \
                                    text_01_Q2, text_01_Q2_ans, text_01_Q2_corr, text_01_Q3, text_01_Q3_ans,
                                    text_01_Q3_corr, text_02, text_02_Q1, \
                                    text_02_Q1_ans, text_02_Q1_corr, text_02_Q2, text_02_Q2_ans, text_02_Q2_corr,
                                    text_02_Q3, text_02_Q3_ans, \
                                    text_02_Q3_corr, text_03, text_03_Q1, text_03_Q1_ans, text_03_Q1_corr, text_03_Q2,
                                    text_03_Q2_ans, text_03_Q2_corr, \
                                    text_03_Q3, text_03_Q3_ans, text_03_Q3_corr, text_04, text_04_Q1, text_04_Q1_ans,
                                    text_04_Q1_corr, text_04_Q2, \
                                    text_04_Q2_ans, text_04_Q2_corr, text_04_Q3, text_04_Q3_ans, text_04_Q3_corr,
                                    text_05, text_05_Q1, text_05_Q1_ans, \
                                    text_05_Q1_corr, text_05_Q2, text_05_Q2_ans, text_05_Q2_corr, text_05_Q3,
                                    text_05_Q3_ans, text_05_Q3_corr, text_06, \
                                    text_06_Q1, text_06_Q1_ans, text_06_Q1_corr, text_06_Q2, text_06_Q2_ans,
                                    text_06_Q2_corr, text_06_Q3, \
                                    text_06_Q3_ans, text_06_Q3_corr, text_07, text_07_Q1, text_07_Q1_ans,
                                    text_07_Q1_corr, text_07_Q2, text_07_Q2_ans, \
                                    text_07_Q2_corr, text_07_Q3, text_07_Q3_ans, text_07_Q3_corr, text_08, text_08_Q1,
                                    text_08_Q1_ans, text_08_Q1_corr, \
                                    text_08_Q2, text_08_Q2_ans, text_08_Q2_corr, text_08_Q3, text_08_Q3_ans,
                                    text_08_Q3_corr, text_09, text_09_Q1, \
                                    text_09_Q1_ans, text_09_Q1_corr, text_09_Q2, text_09_Q2_ans, text_09_Q2_corr,
                                    text_09_Q3, text_09_Q3_ans, \
                                    text_09_Q3_corr, text_10, text_10_Q1, text_10_Q1_ans, text_10_Q1_corr, text_10_Q2,
                                    text_10_Q2_ans, text_10_Q2_corr, \
                                    text_10_Q3, text_10_Q3_ans, text_10_Q3_corr, pseudo_text_01, pseudo_text_02,
                                    pseudo_text_03, pseudo_text_04, pseudo_text_05, \
                                    pseudo_text_06, pseudo_text_07, pseudo_text_08, pseudo_text_09)

    # import some additional functions I wrote for the experiment:
    # from EXNAT3_study_components import change_bg_colour
    from nback_colour_generator import create_nback_stimlist, draw_without_replacement, get_targets, \
        create_0back_stimlist

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

                # Wait for an additional 2 seconds
                core.wait(2)

                return first_trigger_time, trigger_count

    # Run 'Begin Experiment' code from stimuli
    ### Stimulus settings

    # set colours you want to use for background:
    # light_bg_col_hex = "#FDFBF0" # ivory instructions background
    # dark_bg_col_hex  = "#505050" # dark grey background for stimuli
    # light_bg_col = [(x / 127.5) - 1 for x in (253, 251, 240)] 
    light_bg_col = [(x / 127.5) - 1 for x in (186, 186, 186)]  # ivory instructions background (use RGB -1:1)
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
    all_pseudotexts_nrs_list = ["pseudo_text_01", "pseudo_text_02", "pseudo_text_03", "pseudo_text_04",
                                "pseudo_text_05",
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
    dual_blocks = ["1back_dual_main_no_click", "2back_dual_main_no_click", "1back_dual_main_no_click",
                   "2back_dual_main_no_click"]

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
    # First, create list with length of all texts. The length of the blocks is
    # always in the same order, only the conditions change.
    blocks_textlen = [300, 100]  # reading blocks
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
    blocks_textlen = [90, 90, 90, 90]  # single n-back blocks
    blocks_target_counts = [15, 15, 15, 15]

    # Now loop this list. Check which condition we have there and then create colour list for each text.
    run2_colour_lists = []
    run2_target_lists = []
    for block_idx, block_length in enumerate(blocks_textlen):
        # get 1st letter of block name - that tells us the condition
        block_cond = run2_blocks[block_idx][0]

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
        run2_colour_lists.append(curr_colours)
        run2_target_lists.append(curr_targets)

    # RUNS 3, 4, 5 & 6
    blocks_textlen = [300, 300, 300, 300]  # dual-task blocks
    blocks_target_counts = [50, 50, 50, 50]  # dual-task blocks

    # Now loop this list. Check which condition we have there and then create colour list for each text.
    dual_blocks = run3_blocks + run4_blocks + run5_blocks + run6_blocks
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

    # --- Initialize components for Routine "wait_for_scanner" ---

    # --- Initialize components for Routine "single_reading" ---

    # --- Initialize components for Routine "run_finished" ---

    # --- Initialize components for Routine "single_nback" ---

    # --- Initialize components for Routine "run_finished" ---

    # --- Initialize components for Routine "dual_task_block" ---

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

    # --- Prepare to start Routine "wait_for_scanner" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('wait_for_scanner.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from wait_for_scanner
    #################################################
    #              Welcome to experiment            #
    #################################################
    # this routine waits for the scanner trigger and then starts the experiment

    # clear buffer of all previously recorded key events:
    event.clearEvents()

    # Begin trigger_count, start from 0
    trigger_count_run1 = 0

    # Reset global clock
    # globalClock = core.Clock()
    # globalClock.reset()

    # def wait_for_first_trigger(instr_text, number_of_triggers):
    #     """
    #     Wait for the first scanner trigger while displaying instructions on the screen.
    # 
    #     Parameters:
    #     - instr_text: The instruction text to display.
    #     """
    #     trigger_count = number_of_triggers  # Declare trigger_count as global to modify it
    # 
    #     print("Waiting for the first scanner trigger...")
    # 
    #     # Define the instruction text stimulus
    #     instr_text_stim = visual.TextStim(
    #         win,
    #         text=instr_text,
    #         height=0.04,  # font height relative to height of screen
    #         pos=(0, 0.08),  # move up a bit
    #         color="black"
    #     )
    # 
    #     while True:
    #         # Display the instructions
    #         win.setColor(light_bg_col, colorSpace='rgb')
    #         instr_text_stim.draw()
    #         win.flip()
    # 
    #         # Check for the first trigger key '5'
    #         keys = event.getKeys(keyList=['5'])
    #         if keys:
    #             first_trigger_time = globalClock.getTime()
    #             trigger_count += 1
    #             thisExp.addData('TriggerCountRun1', trigger_count)
    #             thisExp.addData('TriggerTime', first_trigger_time)
    #             thisExp.addData('run_nr', "run1")
    #             # Start a new row in the csv
    #             # thisExp.nextEntry()
    #             print(f"First trigger received at {first_trigger_time}")
    #             return first_trigger_time, trigger_count

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
    thisExp.addData('wait_for_scanner.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "wait_for_scanner" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    loop_run1_single_reading = data.TrialHandler(nReps=5.0, method='sequential',
                                                 extraInfo=expInfo, originPath=-1,
                                                 trialList=[None],
                                                 seed=None, name='loop_run1_single_reading')
    thisExp.addLoop(loop_run1_single_reading)  # add the loop to the experiment
    thisLoop_run1_single_reading = loop_run1_single_reading.trialList[
        0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_run1_single_reading.rgb)
    if thisLoop_run1_single_reading != None:
        for paramName in thisLoop_run1_single_reading:
            globals()[paramName] = thisLoop_run1_single_reading[paramName]

    for thisLoop_run1_single_reading in loop_run1_single_reading:
        currentLoop = loop_run1_single_reading
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp,
                win=win,
                timers=[routineTimer],
                playbackComponents=[]
            )
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_run1_single_reading.rgb)
        if thisLoop_run1_single_reading != None:
            for paramName in thisLoop_run1_single_reading:
                globals()[paramName] = thisLoop_run1_single_reading[paramName]

        # --- Prepare to start Routine "single_reading" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('single_reading.started', globalClock.getTime(format='float'))
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
                    core.wait(2)  # wait for 2 s

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
                    core.wait(2)  # wait for 2 s

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

                # CREATE CLOCKS:
                my_block_clock = core.Clock()
                my_block_clock.reset()  # start block clock
                start_time = my_block_clock.getTime()  # get start time of block
                # also create trial clock
                my_trial_clock = core.Clock()

                # loop words in current text
                for trial_idx, curr_word in enumerate(curr_text):
                    # print("current idx: " + str(trial_idx) + ", curr word:" + curr_word)

                    print(f"trigger count: {trigger_count}")
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
                    print("\tend paced trial")
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
                    thisExp.addData('global_onset_time', global_onset_time)
                    thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
                    thisExp.addData('target', curr_target)
                    thisExp.addData('nback_response', curr_nback_response)
                    thisExp.addData('nback_RT', curr_nback_RT)  # in ms
                    thisExp.addData('duration', curr_duration * 1000)  # in ms
                    thisExp.addData('text_nr', curr_text_nr)
                    thisExp.addData('trial_nr', curr_trial_nr)
                    thisExp.addData('block_nr_exp', exp_block_counter + 1)
                    thisExp.addData('run_nr', '1')
                    thisExp.addData('block_nr_run', run1_block_counter + 1)
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

                # Send end of block trigger:
                # core.wait(time_after_trigger)  # wait 3 ms
                # send block offset trigger
                # send_trigger("block_offset")

        # Run 'Begin Routine' code from questions
        ##########################################################
        #              Text Comprehension Questions              #
        ##########################################################

        def setup_question(question_text, answers_text):
            question = visual.TextStim(win, text=question_text, pos=(0, 0.2), color="black", height=0.03,
                                       anchorHoriz='center', alignText='center', wrapWidth=1)
            answers = [
                visual.TextStim(win, text=ans, pos=(-0.75, 0.1 - i * 0.05), color="black", height=0.03, wrapWidth=1.5,
                                anchorHoriz='left', alignText='center') for i, ans in enumerate(answers_text)]
            return question, answers

        def display_question(question, answers):

            # set-up time to write into logfile
            # my_trial_clock = core.Clock()
            # my_trial_clock.reset()
            question_time = globalClock.getTime()
            onset_time_rel2trigger = question_time - first_trigger_time

            question.autoDraw = True
            for answer in answers:
                answer.autoDraw = True
            instr_text.autoDraw = True
            win.flip()
            return question_time, onset_time_rel2trigger

        def get_response(answers, correct_answer):
            while True:
                keys = defaultKeyboard.getKeys(['1', '2', '3', '4'])
                if keys:
                    key_name = keys[0].name  # Get the name of the first key pressed

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
                        break
            return chosen_ans, is_correct

        def reset_answers(answers):
            for answer in answers:
                answer.setColor("black")
            question.autoDraw = False
            instr_text.autoDraw = False
            for answer in answers:
                answer.autoDraw = False

        # Example usage:
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
        instr_text = visual.TextStim(win,
                                     text="(Bitte benutzen Sie die Tasten 1, 2, 3 und 4, um die richtige Antwort auszuwählen.)",
                                     color="grey", pos=(0, -0.3), wrapWidth=2, height=0.018)
        event.clearEvents()

        # Assuming skip_questions_paced and other variables are defined
        if not skip_questions_paced:
            # Setup for Q1
            Q1_text = locals()[curr_text_nr + "_Q1"]
            Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
            Q1_correct = locals()[curr_text_nr + "_Q1_corr"]

            question, answers = setup_question(Q1_text, Q1_answers)
            question_time, onset_time_rel2trigger = display_question(question, answers)
            chosen_ans, is_correct = get_response(answers, Q1_correct)
            print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)

            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
            thisExp.addData('question', 'Q1')
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q1_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('run_nr', '1')
            thisExp.addData('block_nr_run', run1_block_counter + 1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)

            # start a new row in the csv
            thisExp.nextEntry()

            # Setup for Q2
            Q2_text = locals()[curr_text_nr + "_Q2"]
            Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
            Q2_correct = locals()[curr_text_nr + "_Q2_corr"]

            question, answers = setup_question(Q2_text, Q2_answers)
            question_time, onset_time_rel2trigger = display_question(question, answers)
            chosen_ans, is_correct = get_response(answers, Q2_correct)
            print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)

            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
            thisExp.addData('question', 'Q2')
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q2_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('run_nr', "1")
            thisExp.addData('block_nr_run', run1_block_counter + 1)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)

            # start a new row in the csv
            thisExp.nextEntry()

            # Setup for Q3
            Q3_text = locals()[curr_text_nr + "_Q3"]
            Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
            Q3_correct = locals()[curr_text_nr + "_Q3_corr"]

            question, answers = setup_question(Q3_text, Q3_answers)
            question_time, onset_time_rel2trigger = display_question(question, answers)
            chosen_ans, is_correct = get_response(answers, Q3_correct)
            print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)

            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
            thisExp.addData('question', 'Q3')
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q3_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('run_nr', "1")
            thisExp.addData('block_nr_run', run1_block_counter + 1)
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
        thisExp.addData('single_reading.stopped', globalClock.getTime(format='float'))
        # the Routine "single_reading" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'loop_run1_single_reading'

    # --- Prepare to start Routine "run_finished" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('run_finished.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from run_finished
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
                                          height=0.05,
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
    thisExp.addData('run_finished.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "run_finished" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    loop_run2_single_nback = data.TrialHandler(nReps=10.0, method='sequential',
                                               extraInfo=expInfo, originPath=-1,
                                               trialList=[None],
                                               seed=None, name='loop_run2_single_nback')
    thisExp.addLoop(loop_run2_single_nback)  # add the loop to the experiment
    thisLoop_run2_single_nback = loop_run2_single_nback.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_run2_single_nback.rgb)
    if thisLoop_run2_single_nback != None:
        for paramName in thisLoop_run2_single_nback:
            globals()[paramName] = thisLoop_run2_single_nback[paramName]

    for thisLoop_run2_single_nback in loop_run2_single_nback:
        currentLoop = loop_run2_single_nback
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp,
                win=win,
                timers=[routineTimer],
                playbackComponents=[]
            )
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_run2_single_nback.rgb)
        if thisLoop_run2_single_nback != None:
            for paramName in thisLoop_run2_single_nback:
                globals()[paramName] = thisLoop_run2_single_nback[paramName]

        # --- Prepare to start Routine "single_nback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('single_nback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from single_nback_blocks
        # ################################################
        #         Blocks w/o text – single n-back        #
        # ################################################
        # this routine is for all blocks where there are coloured rectangles
        # instead of words and participants are presented with a paced version, i.e., rectangles are presented based on their
        # reaction times in the training before scanning

        if 2 <= exp_block_counter <= 5:

            event.Mouse(visible=False)

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
                    instr_text_stim = visual.TextBox2(win,
                                                      text="Bitte drücken Sie so schnell wie möglich mit dem Zeigefinger, wenn die Farbe des " \
                                 "aktuellen Rechtecks mit der des <b>vorherigen Rechtecks (1 zurück)</b> übereinstimmt.",
                                                      letterHeight=0.03,  # font height relative to height of screen
                                                      pos=(0, 0.2),  # move up a bit
                                                      color="black")
                                                      #wrapwidth=1.5)
                    # create ImageStim object
                    curr_instr_pic = visual.ImageStim(win,
                                                      size=(0.8, 0.3),
                                                      pos=(0, -0.2),
                                                      image=locals()[
                                                          "instr_pic_" + curr_block])  # set path to image here

                    # show instructions on screen
                    instr_text_stim.draw()
                    curr_instr_pic.draw()
                    win.flip()
                    core.wait(2)  # wait for 3s before starting response window

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
                        keys = event.getKeys(['c', 'escape'])

                        # check if there was a response. If there wasn't, we can go straight
                        # to the next iteration which will hopefully save us some dropped
                        # frames in the flicker.
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
                    print("end paced rect trial")

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
                    thisExp.addData('global_onset_time', global_onset_time)
                    thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
                    thisExp.addData('target', curr_target)
                    thisExp.addData('nback_response', curr_nback_response)
                    thisExp.addData('nback_RT', curr_nback_RT)  # in ms
                    thisExp.addData('duration', curr_duration)  # in ms
                    thisExp.addData('trial_nr', curr_trial_nr)
                    thisExp.addData('block_nr_exp', exp_block_counter + 1)
                    thisExp.addData('run_nr', '2')
                    thisExp.addData('block_nr_run', run2_block_counter + 1)
                    thisExp.addData('block_name', curr_block)
                    thisExp.addData('n-back_level', curr_nback_cond)

                    # start a new row in the csv
                    thisExp.nextEntry()

                    ### IF TESTING MODE ENABLED: end loop after 4 trials
                    if expInfo['testing_mode'] == "yes":
                        if trial_idx == 3:
                            break

                print("\t\tfinished presenting trials")

                # change background colour from grey (RGB: 10, 10, 10)
                # to ivory (RGB: 240, 223, 204)
                # win.setColor(light_bg_col, colorSpace='rgb')
                # win.flip()

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
        thisExp.addData('single_nback.stopped', globalClock.getTime(format='float'))
        # the Routine "single_nback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 10.0 repeats of 'loop_run2_single_nback'

    # --- Prepare to start Routine "run_finished" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('run_finished.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from run_finished
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
                                          height=0.05,
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
    thisExp.addData('run_finished.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "run_finished" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    loop_dual_task_blocks = data.TrialHandler(nReps=5.0, method='sequential',
                                              extraInfo=expInfo, originPath=-1,
                                              trialList=[None],
                                              seed=None, name='loop_dual_task_blocks')
    thisExp.addLoop(loop_dual_task_blocks)  # add the loop to the experiment
    thisLoop_dual_task_block = loop_dual_task_blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_dual_task_block.rgb)
    if thisLoop_dual_task_block != None:
        for paramName in thisLoop_dual_task_block:
            globals()[paramName] = thisLoop_dual_task_block[paramName]

    for thisLoop_dual_task_block in loop_dual_task_blocks:
        currentLoop = loop_dual_task_blocks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp,
                win=win,
                timers=[routineTimer],
                playbackComponents=[]
            )
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_dual_task_block.rgb)
        if thisLoop_dual_task_block != None:
            for paramName in thisLoop_dual_task_block:
                globals()[paramName] = thisLoop_dual_task_block[paramName]

        # --- Prepare to start Routine "dual_task_block" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('dual_task_block.started', globalClock.getTime(format='float'))

        # Run 'Begin Routine' code from dual_task_new
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
                core.wait(2)  # wait for 3s before starting

        def calculate_durations(text, block_config):
            """
            Calculate word display durations based on the block configuration.
            """
            RT_per_letter = block_config['RT_per_letter']
            minimum_duration = 5 * RT_per_letter
            if block_config['name'][0] == '1':
                maximum_duration = 2000  # 2 seconds
            elif block_config['name'][0] == '2':
                maximum_duration = 2500  # 2.5 seconds
            increment_per_trial = 3
            curr_durations = []

            for i, word in enumerate(text):
                duration = RT_per_letter * math.log(len(word)) + 4 * RT_per_letter
                adjusted_duration = max(min(duration, maximum_duration), minimum_duration)
                adjusted_duration += i * increment_per_trial  # Adjust for incremental increase
                curr_durations.append(adjusted_duration)

            return curr_durations

        def process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours,
                          curr_instr, curr_instr_pic):
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
                print("\tend paced trial")
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
                thisExp.addData('global_onset_time', onset_time)
                thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
                thisExp.addData('target', curr_target)
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
                    if trial_idx == 3:
                        break

            print("finished presenting trials")

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
                process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours,
                              curr_instr, curr_instr_pic)
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
                process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours,
                              curr_instr, curr_instr_pic)
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
                process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours,
                              curr_instr, curr_instr_pic)
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
                process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours,
                              curr_instr, curr_instr_pic)
                # continueRoutine = False
            else:
                print("Error: Block configuration not found.")

        # Run 'Begin Routine' code from questions_dual_task_new
        ##########################################################
        #              Text Comprehension Questions              #
        ##########################################################

        def setup_question(question_text, answers_text):
            question = visual.TextStim(win,
                                       text=question_text,
                                       pos=(0, 0.2),
                                       color="black",
                                       height=0.03,
                                       anchorHoriz='center',
                                       alignText='center',
                                       wrapWidth=1)
            answers = [visual.TextStim(win,
                                       text=ans,
                                       pos=(-0.75, 0.1 - i * 0.05),
                                       color="black",
                                       height=0.03,
                                       wrapWidth=1.5,
                                       anchorHoriz='left',
                                       alignText='center') for i, ans in enumerate(answers_text)]
            return question, answers

        def display_question(question, answers):

            # specify time of question for logfile
            question_time = globalClock.getTime()
            onset_time_rel2trigger = question_time - first_trigger_time

            question.autoDraw = True
            for answer in answers:
                answer.autoDraw = True
            instr_text.autoDraw = True
            win.flip()
            return question_time, onset_time_rel2trigger

        def get_response(answers, correct_answer):
            while True:
                keys = defaultKeyboard.getKeys(['1', '2', '3', '4'])
                if keys:
                    key_name = keys[0].name  # Get the name of the first key pressed

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
                        break
            return chosen_ans, is_correct

        def reset_answers(answers):
            for answer in answers:
                answer.setColor("black")
            question.autoDraw = False
            instr_text.autoDraw = False
            for answer in answers:
                answer.autoDraw = False

        # Start displaying questions
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()
        instr_text = visual.TextStim(win,
                                     text="(Bitte benutzen Sie die Tasten 1, 2, 3 und 4, um die richtige Antwort auszuwählen.)",
                                     color="grey", pos=(0, -0.3), wrapWidth=2, height=0.018)
        event.clearEvents()

        # Assuming skip_questions_paced and other variables are defined
        if not skip_questions_paced:
            # Setup for Q1
            Q1_text = locals()[curr_text_nr + "_Q1"]
            Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
            Q1_correct = locals()[curr_text_nr + "_Q1_corr"]

            question, answers = setup_question(Q1_text, Q1_answers)
            question_time, onset_time_rel2trigger = display_question(question, answers)
            chosen_ans, is_correct = get_response(answers, Q1_correct)
            print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)

            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
            thisExp.addData('question', 'Q1')
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q1_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('run_nr', run_nr)
            thisExp.addData('block_nr_run', block_nr_run)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)

            # start a new row in the csv
            thisExp.nextEntry()

            # Setup for Q2
            Q2_text = locals()[curr_text_nr + "_Q2"]
            Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
            Q2_correct = locals()[curr_text_nr + "_Q2_corr"]

            question, answers = setup_question(Q2_text, Q2_answers)
            question_time, onset_time_rel2trigger = display_question(question, answers)
            chosen_ans, is_correct = get_response(answers, Q2_correct)
            print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)

            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
            thisExp.addData('question', 'Q2')
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q2_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('run_nr', run_nr)
            thisExp.addData('block_nr_run', block_nr_run)
            thisExp.addData('block_name', curr_block)
            thisExp.addData('n-back_level', curr_nback_cond)

            # start a new row in the csv
            thisExp.nextEntry()

            # Setup for Q3
            Q3_text = locals()[curr_text_nr + "_Q3"]
            Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
            Q3_correct = locals()[curr_text_nr + "_Q3_corr"]

            question, answers = setup_question(Q3_text, Q3_answers)
            question_time, onset_time_rel2trigger = display_question(question, answers)
            chosen_ans, is_correct = get_response(answers, Q3_correct)
            print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
            reset_answers(answers)

            # save data:
            thisExp.addData('global_onset_time', question_time)
            thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
            thisExp.addData('question', 'Q3')
            thisExp.addData('chosen_ans', chosen_ans)
            thisExp.addData('ans_correct', chosen_ans == Q3_correct)
            thisExp.addData('text_nr', curr_text_nr)
            thisExp.addData('block_nr_exp', exp_block_counter + 1)
            thisExp.addData('run_nr', run_nr)
            thisExp.addData('block_nr_run', block_nr_run)
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
        thisExp.addData('dual_task_block.stopped', globalClock.getTime(format='float'))
        # the Routine "dual_task_block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'loop_dual_task_blocks'

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
    instr_text = "Hervorragend!\n\n\nVielen Dank,\ndas Experiment ist nun zu Ende!"

    # create text box
    instr_text_stim = visual.TextStim(win,
                                      text=instr_text,
                                      height=0.05,
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