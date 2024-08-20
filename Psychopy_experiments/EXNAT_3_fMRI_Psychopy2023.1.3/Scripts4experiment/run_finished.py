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
                                      height=0.04,
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