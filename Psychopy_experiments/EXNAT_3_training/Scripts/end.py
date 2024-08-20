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
        print(f"This is how participant performed during the paced version:")
        print(f"\t0-back dual blocks:")
        print(f"\t\thits: {zeroback_n_hits}")
        print(f"\t\tmisses: {zeroback_n_misses}")
        print(f"\t\tfalse alarms: {zeroback_n_false_alarms}")
        print(f"\t\tcorrect rejections: {zeroback_n_correct_rejections}")
        print(f"\t\tcorrect answers to questions: {zeroback_correct_answers}")
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
        print(f"\tRT_per_letter_baseline: {RT_per_letter_baseline}")
        print(f"\tRT_per_letter_0back: {RT_per_letter_0back}")
        print(f"\tRT_per_letter_1back: {RT_per_letter_1bck}")
        print(f"\tRT_per_letter_2back: {RT_per_letter_2bck}")
        # end experiment
        break