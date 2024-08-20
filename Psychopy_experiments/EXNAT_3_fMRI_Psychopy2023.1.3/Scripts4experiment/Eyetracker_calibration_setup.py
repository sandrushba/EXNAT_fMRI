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