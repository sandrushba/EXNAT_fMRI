#################################################
#         Blocks with text – dual task          #
#################################################
# this routine is for all blocks with texts that are paced, i.e., visually presented without space bar

if exp_block_counter == 6:
    # We collected RTs & words from the self-paced block of each condition
    RT_per_letter_oneback_dual = int(expInfo['RT_per_letter_oneback_dual'])
    RT_per_letter_twoback_dual = int(expInfo['RT_per_letter_twoback_dual'])

    # get block kind
    curr_block = run3_blocks[run3_block_counter]

    # clear buffer of all previously recorded key events:
    event.clearEvents()

    if curr_block in ["1back_dual_main_no_click", "2back_dual_main_no_click"]:
        print(f"Start preparing block {curr_block}")
        if curr_block == "1back_dual_main_no_click":
            print("\tUsing RT_per_letter_oneback_dual for this block:", RT_per_letter_oneback_dual)

        elif curr_block == "2back_dual_main_no_click":
            print("\tUsing RT_per_letter_twoback_dual for this block:", RT_per_letter_twoback_dual)

    ### Prepare stimuli:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()

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
                                      size=(0.8, 0.2),
                                      pos=(0, -0.2),
                                      image=locals()["instr_pic_" + curr_block])  # set path to image here

    # show instructions on screen
    win.setColor(light_bg_col, colorSpace='rgb')
    instr_text_stim.draw()
    curr_instr_pic.draw()
    win.flip()
    core.wait(3)  # wait for 3s before starting response window

    # Display the text on screen
    # while True:
    #     instr_text_stim.draw()
    #     curr_instr_pic.draw()
    #     win.flip()
    #     # end showing screen if participant presses space
    #     if 'space' in event.getKeys():
    #         break

    # get text nr:
    curr_text_nr = all_texts_nrs_list[exp_block_counter]
    curr_text = locals()[curr_text_nr]
    # compute RTs using participant's average reading speed / letter
    if curr_block == "1back_dual_main_no_click":
        # compute RTs using participant's average reading speed / letter
        # we define a minimum and a maximum duration for each word
        # the minimum is based on 5 x RT per letter in the respective condition
        # the max duration is based on a time-out of 2 s in the 1-back condition
        minimum_duration = 5 * RT_per_letter_oneback_dual
        maximum_duration = 2000
        curr_durations = []
        for word in curr_text:
            duration = RT_per_letter_oneback_dual * math.log((len(word))) + 4 * RT_per_letter_oneback_dual
            if duration < maximum_duration:
                curr_durations.append(max(duration, minimum_duration))
            else:
                curr_durations.append(maximum_duration)

        # Latency factor of an incremental increase (increment per trial = 3 ms) added over duration of entire
        # block assuming that participants get tired of the course of a 300 words block and thus need a bit more
        # time:
        # Increment of 3 ms per trial
        increment_per_trial = 3
        for i in range(len(curr_durations)):
            # Calculate incremental increase for current trial
            increment = i * increment_per_trial
            # Add incremental increase to current trial's duration
            curr_durations[i] += increment

    elif curr_block == "2back_dual_main_no_click":
        minimum_duration = 5 * RT_per_letter_twoback_dual
        maximum_duration = 2500
        curr_durations = []
        for word in curr_text:
            # this is an absolute value based on estimates of how long you need to feel comfortable reading a word on
            # screen in a paced task
            # duration = RT_per_letter_baseline * math.log((len(word))) + 300
            # more flexible solution:
            duration = RT_per_letter_twoback_dual * math.log((len(word))) + 4 * RT_per_letter_twoback_dual
            if duration < maximum_duration:
                curr_durations.append(max(duration, minimum_duration))
            else:
                curr_durations.append(maximum_duration)

        # Add increment of 3 ms per trial
        increment_per_trial = 3
        for i in range(len(curr_durations)):
            # Calculate incremental increase for current trial
            increment = i * increment_per_trial
            # Add incremental increase to current trial's duration
            curr_durations[i] += increment

    # print(f"\tdurations for paced n-back block: {curr_durations}")

    ### change background colour
    win.setColor(dark_bg_col, colorSpace='rgb')
    win.flip()

    # show main block questions
    skip_questions_paced = False

    # get n-back condition:
    curr_nback_cond = curr_block[0]  # get first character of block name

    # if it is a 1 or a 2, set that as current n-back level:
    if curr_nback_cond in ['1', '2']:
        curr_nback_cond == int(curr_nback_cond)
    # if it's neither 1 nor 2, it has to be a block without n-back,
    # so set curr_nback_cond to None
    else:
        curr_nback_cond = None

    print(f"\tCurrent n-back condition: {curr_nback_cond}")
    print(f"\tCurrent text: {curr_text_nr}")

    # get list with targets & list with colours
    curr_targets = run3_target_lists[run3_block_counter]
    curr_colours = run3_colour_lists[run3_block_counter]

    # create empty text stimulus
    stim = visual.TextStim(win=win,
                           text=" ",
                           pos=(0, 0),  # center stimulus
                           font="Times New Roman",
                           height=0.07)

    stim.draw()
    win.flip()

    # clear buffer of all previously recorded key events:
    event.clearEvents()

    # CREATE CLOCKS:
    my_block_clock = core.Clock()
    my_block_clock.reset()  # start block clock
    start_time = my_block_clock.getTime()  # get start time of block
    # also create trial clock
    my_trial_clock = core.Clock()

    # loop words in current text
    for trial_idx, curr_word in enumerate(curr_text):
        # print("current idx: " + str(trial_idx) + ", curr word:" + curr_word)

        ### prepare & show current word:

        # get current colour
        curr_colour = curr_colours[trial_idx]

        # if it's a block with an n-back task, prepare target list as well
        if curr_nback_cond != None:
            curr_target = curr_targets[trial_idx]
            saw_target = False

        # get duration for current word
        curr_duration = curr_durations[trial_idx] / 1000  # convert ms to seconds
        # print("duration for current word (in s):", curr_duration)

        # get trial number (start counting from 1, so add 1)
        curr_trial_nr = trial_idx + 1

        # set current word & colour as content of text stimulus
        stim.color = curr_colour
        stim.text = curr_word

        # show word on screen
        stim.draw()  # draw word on screen

        # start trial clock & record trial onset time
        my_trial_clock.reset()
        onset_time = my_trial_clock.getTime()

        ### wait for key response:
        # In blocks with n-back task, participants can press "c" to indicate they saw a target colour.

        ### start recording responses
        # start while loop that looks for responses
        # --> end while loop only if duration for current word is over
        while my_trial_clock.getTime() < (onset_time + curr_duration):

            stim.draw()
            win.flip()

            # check for key responses:
            keys = event.getKeys(['c', 'escape'])

            # if there were, check responses:
            for key in keys:

                # if participant pressed button "c" for the first time and it's an n-back condition
                # where they're actually supposed to do that (aka not a reading baseline condition)...
                if key == 'c' and curr_nback_cond != None and saw_target == False:
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
        print("\tend paced trial")
        # stop display of current word & send trial offset trigger
        # win.callOnFlip(send_trigger, "trial_offset")

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
        thisExp.addData('colour', curr_colour)
        thisExp.addData('target', curr_target)
        thisExp.addData('nback_response', curr_nback_response)
        thisExp.addData('nback_RT', curr_nback_RT)  # in ms
        thisExp.addData('duration', curr_duration * 1000)  # in ms
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('trial_nr', curr_trial_nr)
        thisExp.addData('block_nr_exp', exp_block_counter)
        thisExp.addData('run_nr', 'run3')
        thisExp.addData('block_nr_run', run3_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)
        # careful, make sure quotes in the strings are escaped using a
        # quote (weird, I know) so it's properly saved in the CSV:
        thisExp.addData('word', escape_quotes(curr_word))

        # start a new row in the csv
        thisExp.nextEntry()

        ### IF TESTING MODE ENABLED: end loop after 4 trials
        if expInfo['testing_mode'] == "yes":
            if trial_idx == 3:
                break

    print("finished presenting trials")

    # add 1 to the block counter to go load the next block
    # exp_block_counter += 1
    # run3_block_counter += 1
    # print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
    # continueRoutine = False
    #
    # # If there are still blocks left, go to next one.
    # # If not, end loop here:
    # if run3_block_counter == 2:
    #     print(f"Finished block {run3_block_counter}/2 in run 3, moving on to next run!")
    #     # loop_dual_task_blocks.finished = True

    # Send end of block trigger:
    # core.wait(time_after_trigger)  # wait 3 ms
    # send block offset trigger
    # send_trigger("block_offset")

elif 8 <= exp_block_counter <= 9:
    # We collected RTs & words from the self-paced block of each condition
    RT_per_letter_oneback_dual = int(expInfo['RT_per_letter_oneback_dual'])
    RT_per_letter_twoback_dual = int(expInfo['RT_per_letter_twoback_dual'])

    # get block kind
    curr_block = run4_blocks[run4_block_counter]

    # clear buffer of all previously recorded key events:
    event.clearEvents()

    if curr_block in ["1back_dual_main_no_click", "2back_dual_main_no_click"]:
        print(f"Start preparing block {curr_block}")
        if curr_block == "1back_dual_main_no_click":
            print("\tUsing RT_per_letter_oneback_dual for this block:", RT_per_letter_oneback_dual)

        elif curr_block == "2back_dual_main_no_click":
            print("\tUsing RT_per_letter_twoback_dual for this block:", RT_per_letter_twoback_dual)

    ### Prepare stimuli:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()

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
                                      size=(0.8, 0.2),
                                      pos=(0, -0.2),
                                      image=locals()["instr_pic_" + curr_block])  # set path to image here

    # show instructions on screen
    win.setColor(light_bg_col, colorSpace='rgb')
    instr_text_stim.draw()
    curr_instr_pic.draw()
    win.flip()
    core.wait(3)  # wait for 3s before starting response window

    # Display the text on screen
    # while True:
    #     instr_text_stim.draw()
    #     curr_instr_pic.draw()
    #     win.flip()
    #     # end showing screen if participant presses space
    #     if 'space' in event.getKeys():
    #         break

    # get text nr:
    curr_text_nr = all_texts_nrs_list[exp_block_counter]
    curr_text = locals()[curr_text_nr]
    # compute RTs using participant's average reading speed / letter
    if curr_block == "1back_dual_main_no_click":
        # compute RTs using participant's average reading speed / letter
        # we define a minimum and a maximum duration for each word
        # the minimum is based on 5 x RT per letter in the respective condition
        # the max duration is based on a time-out of 2 s in the 1-back condition
        minimum_duration = 5 * RT_per_letter_oneback_dual
        maximum_duration = 2000
        curr_durations = []
        for word in curr_text:
            duration = RT_per_letter_oneback_dual * math.log((len(word))) + 4 * RT_per_letter_oneback_dual
            if duration < maximum_duration:
                curr_durations.append(max(duration, minimum_duration))
            else:
                curr_durations.append(maximum_duration)

        # Latency factor of an incremental increase (increment per trial = 3 ms) added over duration of entire
        # block assuming that participants get tired of the course of a 300 words block and thus need a bit more
        # time:
        # Increment of 3 ms per trial
        increment_per_trial = 3
        for i in range(len(curr_durations)):
            # Calculate incremental increase for current trial
            increment = i * increment_per_trial
            # Add incremental increase to current trial's duration
            curr_durations[i] += increment

    elif curr_block == "2back_dual_main_no_click":
        minimum_duration = 5 * RT_per_letter_twoback_dual
        maximum_duration = 2000
        curr_durations = []
        for word in curr_text:
            # this is an absolute value based on estimates of how long you need to feel comfortable reading a word on
            # screen in a paced task
            # duration = RT_per_letter_baseline * math.log((len(word))) + 300
            # more flexible solution:
            duration = RT_per_letter_twoback_dual * math.log((len(word))) + 4 * RT_per_letter_twoback_dual
            if duration < maximum_duration:
                curr_durations.append(max(duration, minimum_duration))
            else:
                curr_durations.append(maximum_duration)

        # Add increment of 3 ms per trial
        increment_per_trial = 3
        for i in range(len(curr_durations)):
            # Calculate incremental increase for current trial
            increment = i * increment_per_trial
            # Add incremental increase to current trial's duration
            curr_durations[i] += increment

    # print(f"\tdurations for paced n-back block: {curr_durations}")

    ### change background colour
    win.setColor(dark_bg_col, colorSpace='rgb')
    win.flip()

    # show main block questions
    skip_questions_paced = False

    # get n-back condition:
    curr_nback_cond = curr_block[0]  # get first character of block name

    # if it is a 1 or a 2, set that as current n-back level:
    if curr_nback_cond in ['1', '2']:
        curr_nback_cond == int(curr_nback_cond)
    # if it's neither 1 nor 2, it has to be a block without n-back,
    # so set curr_nback_cond to None
    else:
        curr_nback_cond = None

    print(f"\tCurrent n-back condition: {curr_nback_cond}")
    print(f"\tCurrent text: {curr_text_nr}")

    # get list with targets & list with colours
    curr_targets = run4_target_lists[run4_block_counter]
    curr_colours = run4_colour_lists[run4_block_counter]

    # create empty text stimulus
    stim = visual.TextStim(win=win,
                           text=" ",
                           pos=(0, 0),  # center stimulus
                           font="Times New Roman",
                           height=0.07)

    stim.draw()
    win.flip()

    # clear buffer of all previously recorded key events:
    event.clearEvents()

    # CREATE CLOCKS:
    my_block_clock = core.Clock()
    my_block_clock.reset()  # start block clock
    start_time = my_block_clock.getTime()  # get start time of block
    # also create trial clock
    my_trial_clock = core.Clock()

    # loop words in current text
    for trial_idx, curr_word in enumerate(curr_text):
        # print("current idx: " + str(trial_idx) + ", curr word:" + curr_word)

        ### prepare & show current word:

        # get current colour
        curr_colour = curr_colours[trial_idx]

        # if it's a block with an n-back task, prepare target list as well
        if curr_nback_cond != None:
            curr_target = curr_targets[trial_idx]
            saw_target = False

        # get duration for current word
        curr_duration = curr_durations[trial_idx] / 1000  # convert ms to seconds
        # print("duration for current word (in s):", curr_duration)

        # get trial number (start counting from 1, so add 1)
        curr_trial_nr = trial_idx + 1

        # set current word & colour as content of text stimulus
        stim.color = curr_colour
        stim.text = curr_word

        # show word on screen
        stim.draw()  # draw word on screen

        # start trial clock & record trial onset time
        my_trial_clock.reset()
        onset_time = my_trial_clock.getTime()

        ### wait for key response:
        # In blocks with n-back task, participants can press "c" to indicate they saw a target colour.

        ### start recording responses
        # start while loop that looks for responses
        # --> end while loop only if duration for current word is over
        while my_trial_clock.getTime() < (onset_time + curr_duration):

            stim.draw()
            win.flip()

            # check for key responses:
            keys = event.getKeys(['c', 'escape'])

            # if there were, check responses:
            for key in keys:

                # if participant pressed button "c" for the first time and it's an n-back condition
                # where they're actually supposed to do that (aka not a reading baseline condition)...
                if key == 'c' and curr_nback_cond != None and saw_target == False:
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
        print("\tend paced trial")
        # stop display of current word & send trial offset trigger
        # win.callOnFlip(send_trigger, "trial_offset")

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
        thisExp.addData('colour', curr_colour)
        thisExp.addData('target', curr_target)
        thisExp.addData('nback_response', curr_nback_response)
        thisExp.addData('nback_RT', curr_nback_RT)  # in ms
        thisExp.addData('duration', curr_duration * 1000)  # in ms
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('trial_nr', curr_trial_nr)
        thisExp.addData('block_nr_exp', exp_block_counter)
        thisExp.addData('run_nr', 'run4')
        thisExp.addData('block_nr_run', run4_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)
        # careful, make sure quotes in the strings are escaped using a
        # quote (weird, I know) so it's properly saved in the CSV:
        thisExp.addData('word', escape_quotes(curr_word))

        # start a new row in the csv
        thisExp.nextEntry()

        ### IF TESTING MODE ENABLED: end loop after 4 trials
        if expInfo['testing_mode'] == "yes":
            if trial_idx == 3:
                break

    print("finished presenting trials")

    # # add 1 to the block counter to go load the next block
    # exp_block_counter += 1
    # run4_block_counter += 1
    # print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
    # continueRoutine = False
    #
    # # If there are still blocks left, go to next one.
    # # If not, end loop here:
    # if run4_block_counter == 2:
    #     print(f"Finished block {run4_block_counter}/2 in run 4, moving on to next run!")
    #     loop_dual_task_blocks.finished = True

    # Send end of block trigger:
    # core.wait(time_after_trigger)  # wait 3 ms
    # send block offset trigger
    # send_trigger("block_offset")