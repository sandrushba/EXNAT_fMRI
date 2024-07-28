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