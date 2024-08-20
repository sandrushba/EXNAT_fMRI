### PUPIL SIZE BASELINE MEASUREMENT BLOCK
print(f"trigger count: {trigger_count}")
start_block_instr = visual.TextStim(win=win,
                                    text="Das Experiment startet in 10 Sekunden. Bitte schauen Sie solange auf das Fixationskreuz.",
                                    pos=(0, 0),
                                    color="white",
                                    height=0.03,
                                    wrapWidth=1)
# CREATE CLOCK:
my_block_clock = core.Clock()
my_block_clock.reset()  # start block clock

while my_block_clock.getTime() < 3:
    start_block_instr.draw()
    win.flip()
    if event.getKeys(['space']):
        break
win.flip()

# show fixation cross for 10 seconds
fix_cross = visual.TextStim(win=win,
                            text="+",
                            pos=(0, 0),
                            color="black",
                            height=0.2,
                            wrapWidth=1)

my_block_clock.reset()  # start block clock

while my_block_clock.getTime() < 10:
    fix_cross.draw()
    win.flip()
    if event.getKeys(['escape']):
        break
win.flip()  # clear screen again