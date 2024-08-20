### END OF EXPERIMENT:
# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

### Show message
# set text
instr_text = "Hervorragend!\n\n\nVielen Dank,\ndas Experiment ist nun zu Ende!"

# create text box
instr_text_stim = visual.TextStim(win,
                                  text = instr_text,
                                  height = 0.05,
                                  pos = (0, 0),
                                  color = "black")

# display the text on screen until Space is pressed
while True:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    instr_text_stim.draw()
    win.flip()
    # end screen if participant presses space
    if 'return' in event.getKeys():
        et_abort_exp()  # shut down eyetrigger and download incremental data
        core.wait(0.5)
        # send trigger
        send_trigger("end_experiment")
        print("ending experiment now!")
        # end experiment
        break