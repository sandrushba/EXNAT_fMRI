# ################################################
#         Blocks w/o text – single n-back        #
# ################################################
# this routine is for all blocks where there are coloured rectangles
# instead of words and participants are presented with a paced version, i.e., rectangles are presented based on their
# reaction times in the training before scanning

if 2 <= exp_block_counter <= 5:

    event. Mouse(visible=False)

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
            instr_text_stim = visual.TextStim(win,
                                              text=instr_text,
                                              height=0.03,  # font height relative to height of screen
                                              pos=(0, 0.2),  # move up a bit
                                              color="black",
                                              wrapwidth=1.5)
            # instr_text_stim = visual.TextBox2(win,
            #                                   text=instr_text,
            #                                   letterHeight=0.03,  # font height relative to height of screen
            #                                   pos=(0, 0.2),  # move up a bit
            #                                   color="black")
            #                                   #wrapwidth = 1.5)
            # create ImageStim object
            curr_instr_pic = visual.ImageStim(win,
                                              size=(0.8, 0.3),
                                              pos=(0, -0.2),
                                              image=locals()["instr_pic_" + curr_block])  # set path to image here

            # show instructions on screen
            instr_text_stim.draw()
            curr_instr_pic.draw()
            win.flip()
            core.wait(8.75)  # wait for 3s before starting response window

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
                keys = event.getKeys(['1', 'escape'])

                # check if there was a response. If there wasn't, we can go straight
                # to the next iteration which will hopefully save us some dropped
                # frames in the flicker.
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
            thisExp.addData('block_nr_exp', exp_block_counter+1)
            thisExp.addData('run_nr', '2')
            thisExp.addData('block_nr_run', run2_block_counter+1)
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