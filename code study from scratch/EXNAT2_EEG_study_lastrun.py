#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Mar 20 17:07:55 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
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
expName = 'EXNAT2_EEG_study'  # from the Builder filename that created this script
expInfo = {'participant': '', 'age': '', 'gender': 'w', 'handedness': 'r'}
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
    originPath='/Users/merleschuckart/Github/PhD/EXNAT/EEG_study_EXNAT2/code study from scratch/EXNAT2_EEG_study_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
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

# Initialize components for Routine "trial"
trialClock = core.Clock()

#############################################
#                 SETTINGS                  #
#############################################

# Import packages: 
print("import packages")

# --> you might have to pip install some of the packages first

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

# Set working directory:
# get the absolute path of the current file
#current_file = os.path.abspath(os.getcwd())

# get the directory containing the current file
#current_dir = os.path.dirname(current_file)

# set the working directory to the directory containing the current file
#os.chdir(current_dir)

#os.chdir("/Users/merleschuckart/Github/PhD/EXNAT/EEG_study_EXNAT2/code study from scratch")

# I defined a function for generating colour lists in another script, so import that one, too.
# Also import function for counting n-back targets in stimulus list
from nback_colour_generator import create_nback_stimlist, get_targets

# build little function to flatten nested lists:
def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

######## Setup LSL Stream ################################
print("create trigger stream") 
# Create trigger stream:
#global out_marker
#info_marker_stream = StreamInfo('PsychoPyMarkers', 'Marker', 1, 0, 'string')
#out_marker = StreamOutlet(info_marker_stream)
#out_marker.push_sample(["TEST MARKER"])

######## Setup CSV #######################################
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
print("get user input (demographics") 
# what do we want to know?
#exp_info = {'Geschlecht': 'w', 'Alter': '', 'Versuchspersonen-Code': '', 'Händigkeit': 'r'}
# create dialogue box with text fields
#dlg = gui.DlgFromDict(exp_info) # show small window for user input

# Check whether user clicked okay or cancel in the dialogue box.
# If they clicked cancel, print message and abort experiment
#if not dlg.OK:
#    print("User pressed 'Cancel'!")
#    core.quit()

# If everything's fine though, proceed: Push information to LSL.
# In this new LSL stream called "Demographics", we have 7 channels, each channel containing a string (
# = our demographical data and a few additional information on the dataset)
#demogr_info = pylsl.StreamInfo('Demographics', 'DemographicsData', 7, 0, pylsl.cf_string)
#demogr_outlet = pylsl.StreamOutlet(demogr_info)
#demogr_data = ['Participant ID: ' + exp_info['Versuchspersonen-Code'] , 
#               'Age: ' + exp_info['Alter'], 
#               'Gender: ' + exp_info['Geschlecht'], 
#               'Handedness: ' + exp_info['Handedness'], 
#               'Native Language: German',
#               'Vision: corrected or corrected to normal',
#               'Date & time of recording' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")]
#demogr_outlet.push_sample(demogr_data)




############# Experiment Settings ##############################

###### set up window for experiment ############################
print("set up window for experiment") 
#global win
#out_marker.push_sample(["start"])
#win = visual.Window(size     = (800,600), # set window size
#                    fullscr  = False, # make window full screen for better timing and less distractions
#                    allowGUI = True, # False = draw window w/o frame or closing buttons
#                    monitor  = 'testMonitor', 
#                    units    = 'norm',
#                    color    = [1,1,1]) # make the background white for a start
        
############# set response keys ################################
print("set response keys") 
# make sure there are no key events defined so we start with a clean slate
event.globalKeys.clear()

# to go from word to word, I use the Space bar
# to indicate that an n-back target was detected & 
# the key C for right-handed people 
# (we don't test left-handed people in the EEG study)

# add new global event keys "c" and "Space"
# "c" calls the function target_response and Space calls the 
# function next_word (both defined at the end of the script)
#target_key = "c"
#event.globalKeys.add(key = target_key, func = target_response)
        
#continue_key = "Space"
#event.globalKeys.add(key = continue_key, func = next_word)


############# Set Colours ############################
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


############# Set texts ###################################
print("set texts") 
# Prepare lists with words & additional information on the blocks
# hint: escape " characters like this \"

# Giant Squid
#global text_01
text_01 = ["Beim", "Anblick", "der", "Tiere", "wird", "klar,", "warum", "die", "Seeleute", "vergangener", "Jahrhunderte", "Angst", "vor", "Seeungeheuern", "hatten.", "Meterlange", "Fangarme,", "spitze", "Mäuler", "und", "riesige", "Augen", "verleihen", "den", "großen", "Kalmaren", "ein", "furchterregendes", "Aussehen.", "Vor", "der", "Küste", "Chiles", "sind", "sie", "aktuell", "in", "Massen", "zu", "sehen.", "Hunderte", "von", "riesigen", "Tintenfischen", "schwimmen", "in", "den", "flachen", "Gewässern", "und", "fressen", "dort", "die", "Fische.", "Normalerweise", "sind", "die", "großen", "Kalmare", "nur", "schwer", "zu", "beobachten.", "Sie", "leben", "eigentlich", "im", "offenen", "Meer.", "Nur", "nachts", "kommen", "sie", "an", "die", "Oberfläche,", "um", "kleine", "Fische", "zu", "jagen.", "Seit", "zwei", "Wochen", "aber", "sind", "sie", "auch", "bei", "Tageslicht", "vor", "der", "Küste", "zu", "sehen.", "Zunächst", "wurden", "mehr", "als", "200", "Kalmare", "vor", "einer", "Insel", "vor", "Chile", "gesichtet.", "Später", "wurden", "dann", "weitere", "Kalmare", "an", "anderen", "Orten", "entlang", "der", "Küste", "Chiles", "beobachtet.", "Vor", "allem", "für", "die", "Fischer", "ist", "das", "ärgerlich.", "Die", "Kalmare", "fressen", "Hechte,", "Sardinen", "und", "Sardellen.", "Und", "sie", "haben", "großen", "Hunger -", "schlechte", "Karten", "für", "die", "kleineren", "Fische.", "Die", "Kalmare", "selbst", "haben", "hingegen", "Glück:", "Sie", "gelten", "zwar", "in", "manchen", "Ländern", "als", "Delikatesse,", "werden", "in", "Chile", "jedoch", "nicht", "gegessen.", "Meeresbiologen", "standen", "wegen", "des", "plötzlichen", "Erscheinens", "der", "Kalmare", "zunächst", "vor", "einem", "großen", "Rätsel.", "Nun", "ist", "jedoch", "klar,", "weshalb", "die", "Kalmare", "plötzlich", "auftauchten.", "Im", "Februar", "erwärmte", "sich", "das", "Meer", "verglichen", "mit", "den", "Temperaturen", "in", "den", "Vorjahren", "ungewöhnlich", "stark.", "Es", "sammelten", "sich", "viele", "kleine", "Fische", "vor", "der", "Küste.", "Die", "Kalmare", "wurden", "dadurch", "magisch", "angezogen.", "Die", "kleinen", "Fische", "bedeuten", "für", "sie", "reiche", "Beute.", "Für", "Forscher", "ist", "das", "ein", "besonderer", "Glücksfall.", "Normalerweise", "sind", "die", "großen", "Kalmare", "so", "schwer", "vor", "die", "Kamera", "zu", "bekommen,", "dass", "Forscher", "teilweise", "auf", "seltsame", "Ideen", "kommen.", "Ein", "Biologe", "aus", "Neuseeland", "etwa", "will", "versuchen,", "den", "legendären", "Riesenkalmar", "mit", "Sexualhormonen", "vor", "die", "Linse", "zu", "locken.", "Der", "Riesenkalmar", "ist", "mit", "bis", "zu", "20", "Metern", "Länge", "und", "einer", "halben", "Tonne", "Gewicht", "das", "größte", "wirbellose", "Tier", "der", "Welt.", "Bisher", "wurde", "er", "aber", "noch", "nie", "innerhalb", "seines", "natürlichen", "Lebensraums", "gefilmt."]

text_01_Q1 = "Wieso tauchten 2004 vor der Küste Chiles auf einmal hunderte Kalmare auf?"
text_01_Q1_ans = ["sie wurden nicht mehr befischt, weshalb ihr Bestand innerhalb einer Saison quasi explodierte", "vor Chile gab es im Sommer zuvor ein großes Haisterben, weshalb sie kaum noch natürliche Fressfeinde hatten", "sie folgten kleinen Beutefischen vor die Küste", "sie wurden von Meeresbiologen vor der Küste Perus ausgewildert und migrierten dann nach Süden"]
text_01_Q1_corr = ["a", "b", "TRUE_c", "d"]

text_01_Q2 = "Wie möchte der Biologe die Kalmare zu seiner Kamera locken?"
text_01_Q2_ans = ["mit niederfrequenten Tönen", "mit Heringen", "mit Wärmestrahlern", "mit Sexualhormonen"]
text_01_Q2_corr = ["a", "b", "c", "TRUE_d"]

text_01_Q3 = "Wie groß sind die Kalmare?"
text_01_Q3_ans = ["20 m", "15 m", "10 m", "5 m"]
text_01_Q3_corr = ["TRUE_a", "b", "c", "d"]

# Hemingway / The old man and the sea
#global text_02
text_02 = ["Zwanzig", "Jahre", "verbrachte", "Ernest", "Hemingway", "auf", "Kuba.", "Die", "meiste", "Zeit", "davon", "lebte", "er", "in", "Vigía,", "seinem", "legendären", "Haus", "vor", "den", "Toren", "Havannas.", "Seit", "seinem", "Tod", "Anfang", "der", "1960er", "lagern", "in", "Vigía", "etwa", "3000", "Manuskripte", "des", "Autors.", "In", "den", "vergangenen", "Jahren", "sind", "sie", "nach", "und", "nach", "digitalisiert", "worden.", "Nun", "will", "man", "sie", "zunächst", "in", "Kuba", "zeigen,", "bevor", "sie", "dann", "der", "Bibliothek", "von", "Boston", "übergeben", "werden.", "Die", "Leiterin", "des", "Archivs", "in", "Vigía", "sagte", "am", "Montag", "im", "kubanischen", "Fernsehen,", "es", "handele", "sich", "um", "bisher", "unveröffentlichte", "Stücke.", "Die", "Digitalisierung", "war", "zwischen", "den", "USA", "und", "Kuba", "bereits", "2002", "vereinbart", "worden.", "Damals", "berichtete", "die", "\"New", "York", "Times\",", "unter", "den", "Dokumenten", "befänden", "sich", "Texte,", "die", "auf", "lose", "Blätter", "und", "Buchrücken", "gekritzelt", "worden", "seien.", "Dies", "seien", "vor", "allem", "Briefe,", "Entwürfe", "und", "Aufzeichnungen", "zu", "Hemingways", "großen", "Romanen.", "Der", "Biograf", "Hemingways", "nannte", "den", "gesamten", "Nachlass", "eine", "\"Computertomografie", "von", "Hemingways", "Gehirn\".", "In", "Kuba", "schrieb", "Hemingway", "unter", "anderem", "seine", "berühmte", "Novelle", "\"Der", "alte", "Mann", "und", "das", "Meer\".", "Die", "Novelle", "handelt", "vom", "Kampf", "eines", "alten", "Fischers", "mit", "einem", "riesigen", "Schwertfisch.", "Zwei", "Tage", "und", "zwei", "Nächte", "ringt", "der", "Fischer", "mit", "dem", "Schwertfisch,", "bis", "er", "ihn", "schließlich", "am", "dritten", "Tag", "überwältigen", "kann.", "Da", "der", "Fisch", "zu", "groß", "ist,", "um", "ihn", "ins", "Boot", "zu", "ziehen,", "bindet", "er", "ihn", "von", "außen", "ans", "Boot.", "Das", "Blut", "des", "Schwertfisches", "lockt", "auf", "der", "Heimfahrt", "jedoch", "Haie", "an.", "Die", "Haie", "fressen", "nach", "und", "nach", "Teile", "des", "Schwertfischs,", "sodass", "dem", "Fischer", "nur", "das", "Skelett", "bleibt,", "als", "er", "wieder", "in", "den", "Heimathafen", "zurückkehrt.", "Die", "Figur", "des", "Fischers", "ist", "vermutlich", "angelehnt", "an", "den", "Fischer", "Gregorio", "Fuentes,", "der", "sich", "auf", "Kuba", "um", "Hemingways", "Boot", "kümmerte.", "Für", "sein", "Werk", "wurde", "Hemingway", "mit", "dem", "Literaturnobelpreis", "ausgezeichnet.", "Die", "Nobelpreis-Medaille", "schenkte", "er", "aus", "Verbundenheit", "zu", "Kuba", "der", "Wallfahrtskirche", "der", "barmherzigen", "Jungfrau", "von", "Cobre.", "Sie", "ist", "die", "Schutzpatronin", "Kubas.", "Die", "Medaille", "ist", "auch", "heute", "noch", "in", "der", "Kirche", "zu", "sehen."]

text_02_Q1 = "Wem schenkte Hemingway seine Nobelpreis-Medaille?"
text_02_Q1_ans = ["seiner Frau Mary Welsh Hemingway", "seiner Lieblingsbar “Sloppy Joe’s” in Key West, Florida", "einer Wallfahrtskirche zu Ehren der Schutzpatronin von Kuba", "dem Fischer Gregorio Fuentes"]
text_02_Q1_corr = ["a", "b", "TRUE_c", "d"]

text_02_Q2 = "Wie heißt Hemingways Wohnhaus auf Kuba?"
text_02_Q2_ans = ["Vigia", "Baluarte", "Almeneas", "Fortaleza"]
text_02_Q2_corr = ["TRUE_a", "b", "c", "d"]

text_02_Q3 = "Als was bezeichnet der Hemingway-Biograf Andrew Scott Berg den Nachlass Hemingways?"
text_02_Q3_ans = ["als ein Röntgenbild von Hemingways Seele", "als ein MRT von Hemingways Geist", "als eine Computertomografie von Hemingways Gehirn", "als ein Ultraschall von Hemingways Herz"]
text_02_Q3_corr = ["a", "b", "TRUE_c", "d"]

# Einstein
text_03 = ["Sie", "besuchte", "ihn", "oft", "in", "seinem", "Haus", "und", "bekam", "Briefe", "und", "Gedichte", "von", "ihm.", "Manchmal", "durfte", "sie", "ihm", "sogar", "die", "Haare", "schneiden.", "Johanna", "Fantova", "galt", "als", "letzte", "Freundin", "von", "Albert", "Einstein.", "Die", "beiden", "trafen", "sich", "regelmäßig,", "telefonierten", "viel", "und", "gingen", "miteinander", "segeln.", "Nun", "wurde", "bekannt,", "was", "offenbar", "nicht", "einmal", "Einstein", "wusste:", "Johanna", "Fantova", "fertigte", "Notizen", "über", "den", "Inhalt", "ihrer", "Gespräche", "an.", "In", "ihren", "Aufzeichnungen", "zeigt", "sie", "ihn", "nicht", "als", "den", "großen", "Mann,", "der", "zu", "Lebzeiten", "zur", "Legende", "wurde,", "sondern", "als", "Einstein,", "den", "Menschenfreund.", "Die", "Nachwelt", "dürfte", "ihr", "dankbar", "sein.", "Ohne", "die", "Notizen", "wüssten", "wir", "heute", "nichts", "von", "Bibo,", "dem", "traurigen", "Papagei.", "Auch", "eine", "ganze", "Reihe", "kluger", "und", "lustiger", "Zitate", "von", "Einstein", "wären", "verloren", "gegangen.", "Es", "ist", "bisher", "das", "einzige", "bekannte", "Tagebuch", "von", "einer", "Person,", "die", "während", "seiner", "letzten", "Jahre", "eng", "mit", "Einstein", "befreundet", "war.", "Die", "22", "Jahre", "jüngere", "Johanna", "Fantova", "stammte", "wie", "Einstein", "aus", "Europa.", "Die", "Eltern", "ihres", "Ehemannes", "Otto", "Fanta", "empfingen", "vor", "dem", "Krieg", "viele", "berühmte", "Gäste", "in", "ihrem", "Salon.", "Neben", "Einstein", "zählte", "dazu", "auch", "Franz", "Kafka.", "Johanna", "Fantova", "war", "für", "Einstein", "daher", "ein", "Teil", "der", "alten", "Welt.", "Sie", "war", "eine", "Verbindung", "zu", "Dingen,", "die", "er", "vermisste.", "In", "Fantovas", "Manuskript", "erscheint", "Einstein", "als", "komischer", "Eigenbrötler.", "Zugleich", "beschreibt", "sie", "ihn", "aber", "auch", "als", "Menschenfreund,", "der", "vielen", "seiner", "Freunde", "bei", "persönlichen", "Problemen", "half.", "Und", "doch", "fühlte", "sich", "Einstein", "nie", "wirklich", "mit", "seinen", "Mitmenschen", "verbunden.", "Angesichts", "seiner", "eigenen", "gescheiterten", "Beziehungen", "betrachtete", "er", "die", "Beziehungen", "seiner", "Freunde", "mit", "spöttischer", "Distanz:", "\"Ich", "war", "bei", "einem", "Nachbarn.", "Es", "besteht", "die", "Gefahr,", "dass", "sein", "Sohn", "heiratet.\"", "Rührend", "kümmerte", "er", "sich", "dagegen", "um", "sein", "Haustier,", "einen", "deprimierten", "Papagei", "namens", "Bibo.", "\"Der", "Papagei", "ist", "noch", "ganz", "verschüchtert.", "Er", "kam", "mit", "der", "Post.\"", "Einstein", "schritt", "sofort", "zur", "Tat.", "Der", "Erfolg", "blieb", "jedoch", "leider", "aus:", "\"Der", "Papagei", "ist", "traurig.", "Ich", "versuche", "ihn", "aufzuheitern,", "aber", "er", "versteht", "leider", "meine", "Witze", "nicht.\""]

text_03_Q1 = "Wie hieß der Ehemann von Einsteins Freundin Johanna?"
text_03_Q1_ans = ["Hans Spreit", "Franz Kolar", "Kurt Lift", "Otto Fanta"]
text_03_Q1_corr = ["a", "b", "c", "TRUE_d"]

text_03_Q2 = "Welches Haustier hatte Einstein?"
text_03_Q2_ans = ["einen verschüchterten Papagei", "einen lethargischen Kater", "eine depressive Schildkröte", "einen taubstummen Kanarienvogel"]
text_03_Q2_corr = ["TRUE_a", "b", "c", "d"]

text_03_Q3 = "Wen luden die Eltern von Johannas Ehemann neben Einstein noch in ihren Salon ein?"
text_03_Q3_ans = ["Franz Kafka", "Robert Oppenheimer", "Theodor W. Adorno", "Werner Heisenberg"]
text_03_Q3_corr = ["TRUE_a", "b", "c", "d"]

# Batman's Joker
text_04 = ["Jerry", "Robinson", "war", "erst", "17,", "als", "er", "die", "wichtigste", "Entscheidung", "seines", "Lebens", "traf -", "und", "möglicherweise", "seinen", "größten", "Fehler", "beging.", "Statt", "wie", "geplant", "aufs", "College", "zu", "gehen,", "ließ", "er", "sich", "von", "einem", "Mann", "namens", "Bob", "Kane", "als", "Zeichner", "engagieren.", "Kane", "hatte", "gerade", "die", "Zeichnungen", "für", "ein", "Comicheft", "abgeliefert,", "in", "dem", "er", "eine", "völlig", "neue", "Figur", "auftreten", "ließ,", "genannt", "\"Batman\".", "Jetzt", "machte", "er", "Urlaub", "in", "den", "Poconos,", "einem", "Ausflugsgebiet", "in", "Pennsylvania.", "Der", "untergewichtige", "Jerry", "Robinson", "war", "auf", "einer", "Kur", "dort,", "um", "Gewicht", "zuzulegen.", "Um", "Bob", "Kane", "von", "seinem", "Talent", "als", "Zeichner", "zu", "überzeugen,", "fertigte", "Jerry", "Robinson", "für", "ihn", "ein", "paar", "Zeichnungen", "an.", "Da", "er", "kein", "Papier", "zur", "Hand", "hatte,", "zeichnete", "er", "kurzerhand", "auf", "seiner", "Jacke.", "Beeindruckt", "stellte", "Kane", "den", "Jungen", "an.", "Bereits", "ab", "der", "dritten", "Ausgabe", "der", "Batman-Comics", "war", "er", "der", "Hauptzeichner", "der", "Serie.", "Seine", "Zeichnungen", "fertigte", "er", "vor", "allem", "nachts", "an.", "Tagsüber", "studierte", "er", "Journalistik", "in", "New", "York.", "Neben", "dem", "Zeichnen", "tat", "er", "sich", "auch", "bei", "der", "Entwicklung", "der", "Figuren", "hervor.", "Von", "ihm", "stammten", "die", "Entwürfe", "für", "Batmans", "Butler", "Alfred", "und", "Batmans", "Helfer,", "den", "jungen", "Robin.", "Fast", "zeitgleich", "hatte", "der", "Joker,", "Batmans", "Erzfeind,", "seinen", "ersten", "Auftritt", "in", "einem", "weiteren", "Heft.", "Robinson", "behauptete", "später,", "die", "Idee", "zur", "Figur", "des", "Jokers", "sei", "von", "ihm", "ausgegangen.", "Inspiriert", "wurde", "er", "dabei", "durch", "ein", "Kartenspiel,", "das", "seine", "Kollegen", "immer", "zur", "Hand", "hatten.", "Laut", "Bob", "Kane", "beruht", "der", "Entwurf", "des", "Schurken", "dagegen", "auf", "einer", "Szene", "aus", "einem", "Stummfilm.", "\"Robinson", "hatte", "nichts", "damit", "zu", "tun\",", "war", "sein", "drastisches", "Urteil.", "Hier", "rächte", "es", "sich,", "dass", "Jerry", "Robinson", "lediglich", "als", "Assistent", "engagiert", "war,", "auch", "wenn", "er", "der", "Hauptzeichner", "war.", "Kane", "dagegen", "hatte", "sich", "alle", "Rechte", "an", "den", "Figuren", "zugesichert.", "Nicht", "zuletzt", "deshalb", "begann", "Jerry", "Robinson", "ab", "1940", "nicht", "mehr", "für", "Kane,", "sondern", "für", "den", "Comic-Verlag", "direkt", "zu", "arbeiten.", "In", "dessen", "Studio", "saß", "er", "zeitweise", "neben", "\"Superman\"-Miterfinder", "Joe", "Shuster", "am", "Zeichentisch."]

text_04_Q1 = "Warum war Jerry Robinson 1939 in den Poconos?"
text_04_Q1_ans = ["er wollte einen Alkohol-Entzug machen", "er wollte sich von einer Lungenentzündung erholen", "er wollte abnehmen", "er wollte zunehmen"]
text_04_Q1_corr = ["a", "b", "c", "TRUE_d"]

text_04_Q2 = "Was studierte Jerry Robinson neben seiner Tätigkeit als Comiczeichner?"
text_04_Q2_ans = ["Journalistik", "Grafikdesign", "Kunstgeschichte", "Modedesign"]
text_04_Q2_corr = ["TRUE_a", "b", "c", "d"]

text_04_Q3 = "Die Idee zu welcher Figur stammt angeblich von Jerrry Robinson?"
text_04_Q3_ans = ["Catwoman", "Bane", "der Joker", "Harley Quinn"]
text_04_Q3_corr = ["a", "b", "TRUE_c", "d"]

# tiny chameleons
#global text_05
text_05 = ["Die", "Korallenriffe", "und", "die", "sandigen", "Buchten", "sind", "perfekt", "für", "jede", "Urlaubsbroschüre.", "Insgesamt", "ist", "die", "Inselgruppe", "namens", "Nosy", "Hara", "vor", "Madagaskar", "aber", "doch", "recht", "karg.", "In", "dieser", "eher", "lebensfeindlichen", "Umgebung", "haben", "Biologen", "nun", "eine", "neue", "Tierart", "entdeckt:", "Das", "winzige", "Chamäleon", "Brookesia", "micra.", "Von", "der", "Schnauze", "bis", "zum", "Schwanzende", "misst", "es", "weniger", "als", "drei", "Zentimeter.", "Farblich", "machen", "die", "braunen", "Tierchen", "wenig", "her.", "Doch", "ihre", "winzige", "Körpergröße", "fasziniert", "die", "Forscher.", "\"Das", "ist", "nichts,", "wo", "man", "viele", "Untersuchungen", "machen", "muss.", "Man", "erkennt", "auch", "so,", "dass", "das", "etwas", "Neues", "ist\",", "sagt", "Miguel", "Vences.", "Der", "Zoologe", "berichtet", "in", "einem", "Fachartikel", "gleich", "von", "vier", "neuen", "Arten", "von", "Mini-Chamäleons.", "Laut", "den", "Forschern", "weiß", "man", "von", "den", "Tieren", "jedoch", "kaum", "mehr,", "als", "dass", "es", "sie", "gibt.", "Zu", "ihrer", "Lebensweise", "ist", "nur", "sehr", "wenig", "bekannt.", "Tagsüber", "leben", "die", "kleinen", "Chamäleons", "am", "Boden.", "Wenn", "möglich", "verbergen", "sie", "sich", "dabei", "unter", "einer", "Schicht", "Laub.", "Nachts", "geht", "es", "dann", "auf", "niedrig", "gelegene", "Äste", "zum", "Schlafen.", "Direkte", "Fressfeinde", "haben", "die", "Tierchen", "allerdings", "wohl", "eher", "nicht.", "Zu", "ihrem", "Glück,", "so", "die", "Forscher.", "Auf", "solchen", "kleinen", "Inseln", "kann", "die", "Konkurrenz", "zwischen", "den", "Tierarten", "schnell", "sehr", "groß", "werden.", "Auch", "die", "anderen", "neuen", "Chamäleon-Arten", "besiedeln", "nur", "kleine", "Gebiete", "auf", "Madagaskar.", "Durch", "die", "Zerstörung", "ihres", "Lebensraums", "sind", "sie", "jedoch", "besonders", "bedroht.", "Rund", "40", "Prozent", "der", "Reptilien-Arten", "auf", "Madagaskar", "gelten", "mittlerweile", "als", "gefährdet.", "Die", "Forscher", "befürchten,", "dass", "auch", "Brookesia", "tristis,", "eine", "weitere", "neu", "entdeckte", "Art,", "einer", "ungewissen", "Zukunft", "entgegen", "sieht.", "Zwar", "ist", "der", "Lebensraum", "des", "Chamäleons", "vor", "wenigen", "Jahren", "unter", "Schutz", "gestellt", "worden,", "doch", "die", "Abholzung", "des", "Gebiets", "hat", "seitdem", "leider", "sogar", "noch", "zugenommen.", "Mit", "der", "Wahl", "der", "Namen", "der", "neu", "entdeckten", "Chamäleon-Arten", "wollen", "sie", "auf", "die", "große", "Gefahr", "hinweisen,", "die", "den", "Chamäleons", "droht.", "Die", "Botschaft", "hinter", "den", "Namen", "Brookesia", "desperata", "und", "Brookesia", "tristis", "versteht", "man", "auch", "ohne", "Latein", "zu", "können:", "Desperata", "heißt", "verzweifelt", "und", "tristis", "so", "viel", "wie", "traurig."]

text_05_Q1 = "Wo liegt die kleine Inselgruppe, auf der die Chamäleons entdeckt wurden?"
text_05_Q1_ans = ["vor Sri Lanka", "vor Thailand", "vor Madagaskar", "vor Java"]
text_05_Q1_corr = ["a", "b", "TRUE_c", "d"]

text_05_Q2 = "Was haben die lateinischen Namen der neuentdeckten Chamäleons gemeinsam?"
text_05_Q2_ans = ["Miguel Vences hat jede Chamäleon-Art nach je einem Forscher aus seinem Team benannt.", "Ihre Namen beinhalten alle das lateinische Wort \"minima\" für \"klein\".", "Ihre Namen beinhalten alle ein negativ konnotiertes Adjektiv wie \"desperata\" oder \"tristis\".", "Alle Chamäleon-Arten wurden nach berühmten Tierschutz-Aktivist*innen benannt."]
text_05_Q2_corr = ["a", "b", "TRUE_c", "d"]

text_05_Q3 = "Wo verstecken sich die Chamäleons tagsüber?"
text_05_Q3_ans = ["unter Mangroven-Wurzeln", "unter Laub auf dem Boden", "unter Steinen und in Felsnischen", "unter morschen Baumstämmen"]
text_05_Q3_corr = ["a", "TRUE_b", "c", "d"]

# Mauritius
#global text_06
text_06 = ["In", "den", "siebziger", "Jahren", "war", "Mauritius", "eine", "kleine", "Insel", "mitten", "im", "Indischen", "Ozean,", "die", "im", "Ausland", "niemand", "kannte.", "Heute", "ist", "sie", "dagegen", "weltweit", "als", "paradiesisches", "Urlaubsziel", "bekannt.", "Doch", "schon", "lange", "bevor", "die", "ersten", "Touristen", "kamen,", "war", "Mauritius", "in", "einigen", "Teilen", "der", "Welt", "sehr", "bekannt.", "Die", "Portugiesen", "waren", "die", "Ersten,", "die", "die", "Insel", "entdeckten.", "Sie", "nannten", "sie", "\"Schwaneninsel\",", "ließen", "sich", "aber", "nicht", "auf", "ihr", "nieder.", "Erst", "fast", "hundert", "Jahre", "später", "kamen", "die", "Holländer.", "Sie", "gaben", "der", "Insel", "zu", "Ehren", "des", "holländischen", "Prinzen", "Moritz", "den", "Namen", "\"Mauritius\".", "Den", "Namen", "Mauritius", "hat", "sie", "bis", "heute", "behalten.", "Die", "Holländer", "begannen,", "an", "der", "Küste", "Felder", "anzulegen.", "Sie", "brachten", "Zuckerrohr,", "Wild", "und", "Affen", "mit", "auf", "die", "Insel.", "Sie", "bauten", "Häuser", "und", "Festungen", "und", "holzten", "die", "dichten", "Wälder", "aus", "Ebenholz", "ab.", "Zu", "dieser", "Zeit", "lebten", "auf", "Mauritius", "noch", "viele", "Dodos.", "Die", "flugunfähigen", "Vögel", "hatten", "keine", "natürlichen", "Feinde", "auf", "der", "Insel", "und", "waren", "daher", "zu", "ihrem", "eigenen", "Unglück", "sehr", "zahm.", "Für", "die", "Holländer", "machte", "sie", "das", "zur", "perfekten", "Jagdbeute.", "Der", "Dodo", "wurde", "so", "stark", "bejagt,", "dass", "er", "schon", "einige", "Jahrzehnte", "nach", "Ankunft", "der", "Holländer", "vollständig", "ausgerottet", "war.", "Heute", "ist", "er", "das", "Nationalsymbol", "von", "Mauritius.", "Als", "kein", "Holz", "mehr", "zu", "holen", "und", "die", "Natur", "schwer", "geschädigt", "war,", "verließen", "die", "Holländer", "Mauritius.", "Um", "die", "Kontrolle", "der", "Insel", "brach", "ein", "erbitterter", "Krieg", "zwischen", "Briten", "und", "Franzosen", "aus.", "Aber", "wer", "lebt", "heute", "dort?", "Die", "Bevölkerung", "von", "Mauritius", "ist", "das", "Ergebnis", "einer", "Vermischung", "verschiedener", "Kulturen", "und", "Religionen.", "Viele", "der", "Menschen", "kamen", "nicht", "freiwillig.", "Die", "Holländer", "brachten", "afrikanische", "Sklaven", "mit", "auf", "die", "Insel.", "Aus", "Indien", "kamen", "Arbeiter", "für", "die", "Zuckerrohr-Plantagen", "und", "Handwerker,", "die", "beim", "Bau", "von", "Brücken", "und", "Straßen", "halfen.", "Zeitgleich", "mit", "den", "Indern", "kamen", "auch", "muslimische", "und", "chinesische", "Händler", "nach", "Mauritius. ", "Die", "Nachfahren", "von", "Indern,", "Franzosen,", "Chinesen,", "Arabern", "und", "afrikanischen", "Sklaven", "bilden", "heute", "auf", "Mauritius", "eine", "der", "wenigen", "echten", "multikulturellen", "Gesellschaften", "der", "Welt."]

text_06_Q1 = "Woher stammten die Seefahrer, die den Dodo ausrotteten?"
text_06_Q1_ans = ["Holland", "England", "Spanien", "Portugal"]
text_06_Q1_corr = ["TRUE_a", "b", "c", "d"]

text_06_Q2 = "Aus welchem Holz bestanden die Wälder der Insel?"
text_06_Q2_ans = ["Mangoholz", "Teakholz", "Ebenholz", "Mahagoni"]
text_06_Q2_corr = ["a", "b", "TRUE_c", "d"]

text_06_Q3 = "Wie lautete der erste Name der Insel, um die es im Text geht?"
text_06_Q3_ans = ["Schwaneninsel", "Kolibri-Insel", "Tukan-Insel", "Papageieninsel"]
text_06_Q3_corr = ["TRUE_a", "b", "c", "d"]

# Angkor Wat
#global text_07
text_07 = ["Wer", "Angkor", "sagt,", "meint", "in", "der", "Regel", "Angkor", "Wat.", "Die", "berühmte", "Tempelanlage", "wurde", "vermutlich", "vor", "knapp", "900", "Jahren", "in", "den", "Dschungel", "Kambodschas", "gebaut.", "Seit", "mehr", "als", "hundert", "Jahren", "hat", "sich", "die", "Wissenschaft", "auf", "die", "riesigen", "Tempelanlagen", "und", "ihre", "Inschriften", "konzentriert.", "Für", "die", "Lebensweise", "der", "Bewohner", "der", "Region", "hat", "sich", "hingegen", "kaum", "jemand", "interessiert.", "Das", "Team", "um", "den", "Forscher", "Damian", "Evans", "hat", "nun", "erstmals", "eine", "Karte", "von", "Angkor", "Wat", "erstellt.", "Die", "Karte", "zeigt,", "dass", "Angkor", "Wat", "eine", "richtige", "Stadt", "war,", "nicht", "nur", "eine", "kleine", "Tempelanlage.", "Die", "Forscher", "gehen", "davon", "aus,", "dass", "Ihre", "Größe", "sogar", "New", "York", "übertroffen", "haben", "könnte.", "Damit", "ist", "\"Groß-Angkor\"", "die", "mit", "Abstand", "größte", "vorindustrielle", "Siedlung", "der", "Welt.", "Selbst", "die", "riesigen", "Städte", "der", "Maya", "erscheinen", "dagegen", "winzig.", "Die", "Forscher", "fanden", "außerdem", "heraus,", "dass", "Angkor", "eine", "hydraulische", "Stadt", "war.", "Dank", "eines", "komplizierten", "Bewässerungssystems", "konnten", "die", "mehr", "als", "eine", "Million", "Bewohner", "versorgt", "werden.", "Durch", "das", "riesige", "Netz", "aus", "Flüssen,", "Kanälen", "und", "Stauseen", "hat", "die", "mittelalterliche", "Stadt", "mehrmals", "im", "Jahr", "Reis", "ernten", "können.", "Das", "verschaffte", "den", "Bewohnern", "nicht", "nur", "volle", "Teller,", "sondern", "auch", "einen", "enormen", "Reichtum.", "Die", "Stadt", "umgab", "ein", "riesiges", "Geflecht", "aus", "Äckern,", "Häusern", "und", "Seen,", "das", "sich", "über", "mindestens", "tausend", "Quadratkilometer", "erstreckte.", "Auf", "dieser", "Fläche", "gibt", "es", "kaum", "einen", "Fleck,", "der", "nicht", "genutzt", "worden", "ist.", "Das", "Bewässerungsnetz", "war", "sogar", "dazu", "geeignet,", "den", "Reisanbau", "zu", "stärken.", "Für", "den", "Anbau", "von", "Reis", "braucht", "man", "jedoch", "extrem", "viel", "Wasser", "und", "riesige", "Flächen.", "Um", "die", "Felder", "und", "die", "künstlichen", "Seen,", "Flüsse", "und", "Kanäle", "anzulegen,", "mussten", "große", "Waldflächen", "gerodet", "werden.", "Mit", "der", "Zeit", "führte", "das", "wahrscheinlich", "zu", "riesigen", "Problemen", "wie", "Erdrutschen.", "Das", "gesamte", "System", "dürfte", "daher", "auch", "sehr", "empfindlich", "auf", "Naturkatastrophen", "reagiert", "haben.", "Insbesondere", "im", "Norden", "der", "Stadt", "fand", "man", "Spuren", "von", "hektischen", "Anpassungen", "und", "Deichbrüchen.", "Genaueres", "weiß", "man", "aber", "nicht.", "Die", "neue", "Karte", "der", "Stadt", "verrät", "aber", "zumindest,", "wo", "man", "nach", "Antworten", "suchen", "sollte."]

text_07_Q1 = "Wie groß war die Stadt Angkor Wat?"
text_07_Q1_ans = ["größer als New York", "größer als Tokyo", "größer als Delhi", "größer als São Paulo"]
text_07_Q1_corr = ["TRUE_a", "b", "c", "d"]

text_07_Q2 = "Wovon ernährten sich die Bewohner*innen Angkor Wats vornehmlich?"
text_07_Q2_ans = ["Hirse", "Linsen", "Reis", "Mais"]
text_07_Q2_corr = ["a", "b", "TRUE_c", "d"]

text_07_Q3 = "Warum ist Angkor Wat vermutlich untergegangen?"
text_07_Q3_ans = ["durch Massaker im Rahmen der Kolonialisierung Südostasiens", "durch eine Hungersnot", "durch die Pest", "durch Umweltzerstörung"]
text_07_Q3_corr = ["a", "b", "c", "TRUE_d"]

# Petra
#global text_08
text_08 = ["Ein", "solcher", "Anblick", "lässt", "selbst", "Indiana", "Jones", "Kinnlade", "herunterklappen:", "Nach", "einem", "spektakulären", "Ritt", "durch", "eine", "teils", "nur", "zwei", "Meter", "schmale", "Schlucht", "erhebt", "sich", "vor", "dem", "Filmhelden", "eine", "riesige", "Fassade.", "Die", "Szene", "aus", "dem", "Kinofilm", "machte", "die", "antike", "Felsenstadt", "Petra", "endgültig", "weltberühmt.", "Die", "prachtvolle", "Fassade", "ist", "eine", "der", "schönsten", "Bauten", "in", "der", "Felsenstadt", "mitten", "in", "der", "Wüste", "Jordaniens.", "Die", "Metropole", "war", "einst", "die", "Hauptstadt", "der", "Nabatäer.", "Zwei", "Jahrhunderte", "beherrschten", "die", "Nabatäer", "große", "Teile", "des", "Handels", "im", "Nahen", "Osten.", "So", "reich", "und", "mächtig", "wurde", "das", "Wüstenvolk,", "dass", "es", "sogar", "die", "Römer", "herausforderte.", "Doch", "wie", "ihre", "riesige", "Hauptstadt", "mitten", "in", "der", "Wüste", "funktioniert", "hat,", "weiß", "niemand", "genau.", "Sicher", "ist,", "dass", "die", "Stadt", "in", "atemberaubend", "kurzer", "Zeit", "entstand.", "Als", "die", "Nabatäer", "ins", "heutige", "Jordanien", "vordrangen,", "war", "die", "Region", "die", "reinste", "Goldgrube.", "Bei", "Petra", "kreuzten", "sich", "mehrere", "Handelswege,", "darunter", "die", "uralte", "Weihrauchstraße.", "Binnen", "weniger", "Jahrzehnte", "entstanden", "hunderte", "Höhlen", "mit", "prunkvollen", "Fassaden", "und", "teils", "gewaltigen", "Räumen.", "Von", "der", "eigentlichen", "Stadt", "ist", "heute", "nichts", "geblieben", "außer", "Steinhaufen", "und", "Mauerreste.", "Bis", "in", "die", "siebziger", "Jahre", "glaubte", "man", "daher,", "Petra", "sei", "eine", "Stadt", "für", "die", "Toten", "und", "die", "Götter", "gewesen,", "und", "die", "Menschen", "hätten", "woanders", "gewohnt.", "Aber", "Petra", "war", "eine", "ganz", "normale", "Stadt,", "nur", "an", "einem", "unmöglichen", "Ort.", "Die", "seltenen", "Regenfälle", "nutzten", "die", "Nabatäer", "mit", "einem", "genialen", "Bewässerungssystem.", "Überall", "in", "der", "Stadt", "waren", "Wasserbecken", "in", "den", "Fels", "geschlagen.", "Viele", "Kilometer", "Wasserleitungen", "leiteten", "das", "Wasser", "zuerst", "in", "die", "Speicher", "und", "von", "dort", "aus", "zu", "den", "Bewohnern.", "Die", "vielen", "Leitungen,", "die", "den", "Regen", "einst", "von", "den", "wertvollen", "Fassaden", "fernhielten,", "wurden", "von", "den", "Nabatäern", "dauernd", "instand", "gehalten.", "Doch", "wenn", "es", "jetzt", "regnet,", "strömt", "das", "Wasser", "unkontrolliert", "die", "Fassaden", "herab.", "Für", "den", "Sandstein", "ist", "das", "eine", "Katastrophe.", "Versuche", "zur", "Rettung", "der", "Fassaden", "gab", "es,", "doch", "wirklich", "erfolgreich", "war", "bislang", "leider", "keiner.", "Die", "antike", "Felsenstadt", "wird", "daher", "wohl", "eines", "Tages", "wieder", "zu", "Sand", "zerfallen."]

text_08_Q1 = "An welcher antiken Handelsroute lag die in Fels gehauene Wüstenstadt Petra?"
text_08_Q1_ans = ["an der Safranstraße", "an der Weihrauchstraße", "an der Seidenstraße", "an der Kaschmirstraße"]
text_08_Q1_corr = ["a", "TRUE_b", "c", "d"]

text_08_Q2 = "Wie heißt das Wüstenvolk, um das es im Artikel geht?"
text_08_Q2_ans = ["Nabatäer", "Tuareg", "Beduinen", "Garamanten"]
text_08_Q2_corr = ["TRUE_a", "b", "c", "d"]

text_08_Q3 = "Was könnte dazu führen, dass Petra schon bald völlig zerstört sein könnte?"
text_08_Q3_ans = ["Massentourismus", "Sandstürme","Grabräuberei","Überschwemmungen"]
text_08_Q3_corr = ["a", "b", "c", "TRUE_d"]

# Shakespeare / Hamlet
#global text_09
text_09 = ["William", "Shakespeare", "war", "etwa", "fünf", "Jahre", "alt,", "als", "gar", "nicht", "weit", "entfernt", "von", "seinem", "Heimatdorf", "die", "nur", "zweijährige", "Jane", "Shaxspere", "ums", "Leben", "kam.", "Das", "kleine", "Mädchen", "wollte", "Ringelblumen", "pflücken,", "die", "am", "Ufer", "eines", "Mühlteichs", "wuchsen.", "Beim", "Blumenpflücken", "rutschte", "Jane", "aus,", "fiel", "ins", "Wasser", "und", "ertrank.", "William", "Shakespeare,", "der", "etwa", "20", "Kilometer", "entfernt", "im", "Dorf", "Stratford-upon-Avon", "aufwuchs,", "sollte", "später", "zum", "größten", "Dramatiker", "aller", "Zeiten", "heranwachsen.", "Forscher", "der", "Universität", "von", "Oxford", "vermuten", "nun", "einen", "Zusammenhang", "dieses", "Unfalls", "mit", "Shakespeares", "Stück", "\"Hamlet\".", "Eine", "Nebenhandlung", "des", "Stücks", "erzählt", "die", "Geschichte", "der", "fiktiven", "Edeldame", "Ophelia,", "der", "Tochter", "eines", "Kämmerers.", "Ophelia", "wächst", "am", "dänischen", "Königshof", "auf,", "wo", "sie", "die", "Geliebte", "des", "Prinzen", "Hamlet", "wird.", "Ihre", "Beziehung", "wird", "von", "ihrem", "Vater", "und", "ihrem", "Bruder", "jedoch", "missbilligt.", "Sie", "bezweifeln,", "dass", "Hamlet", "die", "ehrliche", "Absicht", "hat,", "Ophelia", "zu", "heiraten.", "Als", "Hamlet", "aus", "Versehen", "Ophelias", "Vater", "tötet,", "verzweifelt", "sie", "und", "erleidet", "ein", "ähnliches", "Schicksal", "wie", "die", "kleine", "Jane.", "Beim", "Blumenpflücken", "an", "einem", "Bachufer", "verliert", "sie", "das", "Gleichgewicht", "und", "fällt", "in", "den", "Bach.", "Ihr", "Kleid", "saugt", "sich", "mit", "Wasser", "voll", "und", "zieht", "sie", "wie", "ein", "Gewicht", "nach", "unten.", "Ob", "ihr", "Tod", "ein", "Unfall", "ist", "oder", "sie", "sich", "mit", "Absicht", "nicht", "aus", "dem", "Wasser", "rettet,", "wird", "im", "Stück", "offengelassen.", "Die", "erstaunliche", "Verbindung", "zwischen", "realen", "Ereignissen", "und", "Shakespeares", "\"Hamlet\"", "fiel", "Historikern", "auf,", "als", "sie", "alte", "medizinische", "Akten", "untersuchten.", "Die", "Ähnlichkeit", "der", "Nachnamen", "könnte", "sogar", "darauf", "hinweisen,", "dass", "William", "und", "Jane", "Verwandte", "gewesen", "sein", "könnten.", "Feste", "Schreibweisen", "von", "Namen", "gab", "es", "zu", "Shakespeares", "Zeiten", "nicht.", "Für", "eine", "der", "Forscherinnen", "aus", "Oxford", "ist", "dieses", "Detail", "aber", "nicht", "entscheidend:", "\"Selbst", "wenn", "sie", "nicht", "verwandt", "gewesen", "sind,", "hat", "sich", "die", "Geschichte", "durch", "die", "Ähnlichkeit", "der", "Namen", "vielleicht", "in", "Shakespeares", "Kopf", "verankert.\"", "Neben", "historischen", "Grundlagen", "seien", "Shakespeares", "Stücke", "auch", "von", "Klatsch", "und", "Tratsch-Geschichten", "beeinflusst", "worden.", "Dazu", "könnte", "auch", "die", "Geschichte", "über", "den", "Tod", "von", "Jane", "Shaxspere", "gezählt", "haben."]

text_09_Q1 = "Im Artikel wird beschrieben, dass ein Unfall in einem Nachbarort Shakespeare zu einem seiner bekanntesten Stücke inspiriert haben könnte. Um welches Stück handelt es sich?"
text_09_Q1_ans = ["Othello", "King Lear", "Hamlet","Macbeth"]
text_09_Q1_corr = ["a", "b", "TRUE_c", "d"]

text_09_Q2 = "Wie hieß das Mädchen, um das es im Artikel geht?"
text_09_Q2_ans = ["Rosalind Shaxspere", "Ann Shaxspere", "Viola Shaxspere", "Jane Shaxspere"]
text_09_Q2_corr = ["a", "b", "c", "TRUE_d"]

text_09_Q3 = "Wie alt war Shakespeare, als das Unglück passierte?"
text_09_Q3_ans = ["ca. 5 Jahre", "ca. 10 Jahre", "ca. 15 Jahre", "ca. 20 Jahre"]
text_09_Q3_corr = ["a", "b", "c", "d"]


############# shuffle order of texts ####################################
print("shuffle texts") 

# collect the text IDs in lists so I know which text was shown 
all_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04", "text_05", "text_06", "text_07", "text_08", "text_09"]

# shuffle text numbers
random.shuffle(all_texts_nrs_list)

############# Set order of blocks ############################################
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

######## Create n-back colour lists for all blocks ##############################
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


#--------------------------------------------------------------


#############################################
#              ADDITIONAL FUN               #
#    (FUN as in fun, not functions obvi)    #
#############################################


### Function for showing 3 MC questions (each with 4 answer options) on screen.

# The participant can select the correct answers using their mouse
# and they can confirm their selection by pressing the space bar on their keyboard.
# The selected answer option is shown in green and a selection can be changed 
# if the participant selected the wrong option by accident.

def multiple_choice(window, questions, answer_options, ans_correct):
    print("start preparing MC questions")
    # create TextStims for each question & its answer options:
    q_stims = []
    a_stims = []
    # do the following for each of the 3 questions:
    for i in range(3):
        print("start preparing Q" + str(i))
        # create a TextStim for the current question
        q_stim = visual.TextStim(win, text = questions[i], pos = (0, 6))
        q_stims.append(q_stim)
        
        # do the same for the answer options:
        print("start preparing answer options for Q" + str(i))
        a_stim1 = visual.TextStim(win, text = "1) " + answer_options[i][0], pos = (-6, 2))
        a_stim2 = visual.TextStim(win, text = "2) " + answer_options[i][1], pos = (-6, 1))
        a_stim3 = visual.TextStim(win, text = "3) " + answer_options[i][2], pos = (-6, 0))
        a_stim4 = visual.TextStim(win, text = "4) " + answer_options[i][3], pos = (-6, -1))
        a_stims.append([a_stim1, a_stim2, a_stim3, a_stim4])
    
    # create another TextStim for the instruction
    # I want to tell my participants that they can confirm their selection by pressing Space
    print("prepare instruction")
    instr_stim = visual.TextStim(window, 
                                 text = "Bitte drücken Sie die Leertaste um fortzufahren", 
                                 pos = (-10, 10))

    # Track participant's answers - so far they haven't 
    # selected anything so start with some default values
    selected_answers = [-1, -1, -1]
    answer_colors = ['black','black','black']
    
    # small helper function: change answer font colour if it's selected
    def update_answer_colors(q_num):
        print("change answer if it's selected")
        for i in range(4):
            if i == selected_answers[q_num]:
                print("answer selected, show it in green")
                a_stims[q_num][i].color = (0.44, 0.54, 0.37) # Dark sage green
            else:
                a_stims[q_num][i].color = answer_colors[q_num]
    
    # small helper function: check participant's answers and display feedback
    def check_answers():
        print("check participant's answers")
        feedback_stims = []
        for i in range(3):
            # If no answer is selected, show text "please answer all questions"
            if selected_answers[i] == -1:
                print("no ans given")
                feedback_stim = visual.TextStim(win, 
                                                text = "Bitte beantworten Sie alle Fragen.", 
                                                pos = (0, -6))
                feedback_stims.append(feedback_stim)
                continue
            # if answer was correct, show "correct!"
            if ans_correct[i][selected_answers[i]]:
                print("correct ans")
                feedback_stim = visual.TextStim(win, 
                                                text = "Richtig!", 
                                                pos = (0, -6))
            # if answer was not correct, show "wrong answer"
            else:
                print("wrong ans")
                feedback_stim = visual.TextStim(win, 
                                                text = "Falsch.", 
                                                pos = (0, -6))
            feedback_stims.append(feedback_stim)
            
        # loop feedback stimuli and draw on screen
        for stim in feedback_stims:
            print("draw feedback")
            stim.draw()

        window.flip()
        # Check if participant pressed "Space"
        event.waitKeys(keyList=['space'])
    
    # main loop for displaying questions
    for i in range(3):
        # Draw question and answer option stims
        q_stims[i].draw()
        for stim in a_stims[i]:
            print("draw questions + answers on screen")
            stim.draw()
        instr_stim.draw()
        print("show questions + answers on screen")
        window.flip()
        
        # Handle participant's response
        print("wait for responses")
        keys = event.waitKeys(keyList = ['1','2','3','4','space'], 
                              clearEvents = True)
                              
        # do this until you find a response
        while True:
            # if participant selected option 1, save as "a"
            if '1' in keys:
                print("selected option a")
                selected_answers[i] = "a"
                break
            # if participant selected option 2, save as "d"
            elif '2' in keys:
                print("selected option b")
                selected_answers[i] = "b"
                break
            # if participant selected option 3, save as "c"
            elif '3' in keys:
                selected_answers[i] = "c"
                print("selected option c")
                break
            # if participant selected option 4, save as "d"
            elif '4' in keys:
                print("selected option d")
                selected_answers[i] = "d"
                break
            # if participant pressed space, check whether 
            # their answers are valid / correct
            elif 'space' in keys:
                print("submitted answers - checking answers now")
                check_answers()
                break

# Define the questions and answer options
#questions = ["What is the name of the orphanage where Reynie lived before being recruited to the Secret Benedict Society?", 
#             "What is the name of the founder of the society?", 
#             "What is the name of the test the children had to pass in order to join the society?"]
#answer_options = [["St. Michael's Orphanage", "St. Joseph's Orphanage", "St. John's Orphanage", "St. Jude's Orphanage"], 
#                  ["Nicholas Benedict", "William Benedict", "Thomas Benedict", "Edward Benedict"], 
#                  ["The Test of Intelligence", "The Test of Knowledge", "The Test of Perseverance", "The Test of Resourcefulness"]]
#ans_correct = [[True, False, False, False], 
#               [True, False, False, False], 
#               [False, False, False, True]]


# Present the questions and record the participant's answers
#selected_answers = multiple_choice(win, questions, answer_options, ans_correct)

# Print the participant's answers
#print("Participant's answers:", selected_answers)


curr_mc_question = visual.Slider(win = win,
                                 size = (3,5), pos = (0, -4),
                                 units = None, 
                                 labels = ["a", "b", "c", "d"], 
                                 ticks = (1,2,3,4),
                                 granularity = 1,
                                 style = ("radio",),
                                 color = "black", 
                                 font = "Arial", 
                                 flip = False)

curr_mc_question.draw()
win.flip()



### Function to turn background from colour 1 to colour 2 (both defined in HEX) 
#   over the course of x seconds
def change_bg_colour(window, start_rgb, end_rgb, seconds=2):
    # Convert normal RGB values to 0-1 scale
    start_rgb = [c/255 for c in start_rgb]
    end_rgb = [c/255 for c in end_rgb]
    
    # Create a rectangle with the same size as the window
    rect = visual.Rect(window, width=window.size[0], height=window.size[1])
    
    # Gradually change the background colour over "seconds" seconds
    num_steps = seconds * 60
    for i in range(num_steps):
        # Calculate the current RGB values
        curr_r = start_rgb[0] + (i/num_steps) * (end_rgb[0] - start_rgb[0])
        curr_g = start_rgb[1] + (i/num_steps) * (end_rgb[1] - start_rgb[1])
        curr_b = start_rgb[2] + (i/num_steps) * (end_rgb[2] - start_rgb[2])
        
        # Set the rectangle fill color to the current color
        rect.setFillColor([curr_r, curr_g, curr_b])
        
        # Draw the rectangle on the window
        rect.draw()
        
        # Flip the window to update the display
        window.flip()
        
        # Wait for a few ms before updating the background colour again
        core.wait(1/60)
    
    # Set end color as final bg colour
    window.color = end_rgb
    
    # Add an extra delay to ensure the final bg colour is fully set
    core.wait(0.5)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
#############################################
#             START EXPERIMENT              #
#############################################
print("starting experiment now")
# create block counter
block_counter = 0

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


# keep track of which components have finished
trialComponents = []
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
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
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
