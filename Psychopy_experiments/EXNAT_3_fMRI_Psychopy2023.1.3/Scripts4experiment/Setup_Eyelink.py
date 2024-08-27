### Set up connection to EyeLink Eyetracker

# for connecting to Eyelink:
import pylink
import platform  # ?
from PIL import Image  # for host backdrop image
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy  # ?
from string import ascii_letters, digits  # ?

# set up EDF data file:
edf_name = expInfo['participant']  # make sure file name (without .edf) is <= 8 characters
if len(edf_name) > 4:
    print("edf file name is too long - choose shorter participant code!")
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
#Sets automatic calibration pacing.  \c 1000 is a good value for most subjects, \c 1500 for slow
# subjects and when interocular data is required.
el_tracker.sendCommand("automatic_calibration_pacing=%d"%(1000))

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