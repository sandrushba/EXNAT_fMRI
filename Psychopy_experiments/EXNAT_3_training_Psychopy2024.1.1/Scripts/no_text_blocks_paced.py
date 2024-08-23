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
    # if curr_block == "1back_single_main_no_click":
    #
    #     # exclude all RTs where participant was way too fast (< 50 ms) or
    #     # too slow (> 1.5 s)
    #     # print("\toneback_single_paced_durations:", oneback_single_paced_durations)
    #
    #     filtered_durations_oneback_single = []
    #     for duration in oneback_single_paced_durations:
    #         if 50 <= duration <= 1500:
    #             filtered_durations_oneback_single.append(duration)
    #     # count n of trials:
    #     oneback_single_trials = len(filtered_durations_oneback_single)
    #     # get time it took in total:
    #     oneback_single_time_total = sum(filtered_durations_oneback_single)  # in ms
    #
    #
    #     # Check average RT / rectangle
    #     RT_per_rectangle_oneback_single = oneback_single_time_total / oneback_single_trials
    #     print("\taverage RT per rectangle in ms for single 1back:", RT_per_rectangle_oneback_single)
    #
    #     # save this in the output csv:
    #     thisExp.addData('RT_per_rect_1back_single', RT_per_rectangle_oneback_single)
    #
    # elif curr_block == "2back_single_main_no_click":
    #
    #     # exclude all RTs where participant was way too fast (< 50 ms) or
    #     # too slow (> 2.0 s)
    #     # print("\ttwoback_single_paced_durations:", twoback_single_paced_durations)
    #
    #     filtered_durations_twoback_single = []
    #     for duration in twoback_single_paced_durations:
    #         if 50 <= duration <= 2000:
    #             filtered_durations_twoback_single.append(duration)
    #     # count n of trials:
    #     twoback_single_trials = len(filtered_durations_twoback_single)
    #     # get time it took in total:
    #     twoback_single_time_total = sum(filtered_durations_twoback_single)  # in ms
    #
    #     # Check average RT / rectangle
    #     RT_per_rectangle_twoback_single = twoback_single_time_total / twoback_single_trials
    #     print("\taverage RT per rectangle in ms for single 2back:", RT_per_rectangle_twoback_single)
    #
    #     # save this in the output csv:
    #     thisExp.addData('RT_per_rect_2back_single', RT_per_rectangle_twoback_single)


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
            # ser.timeout = remaining_time
            if remaining_time > 0:
                ser.timeout = remaining_time
            else:
                ser.timeout = 0

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