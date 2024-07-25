#################################################
#        Blocks with text – reading only        #
#################################################
# this routine is for all blocks with texts that are paced, i.e., visually presented without space bar

if 0 <= exp_block_counter <= 1:
    # We collected RTs & words from the self-paced block of each condition
    RT_per_letter_baseline = int(expInfo['RT_per_letter_baseline'])
    print("Using RT_per_letter_baseline for this block:", RT_per_letter_baseline)

    # get block kind
    curr_block = run1_blocks[run1_block_counter]

    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()

    # ----------------------------------

    # clear buffer of all previously recorded key events:
    event.clearEvents()

    ### specify settings for the current block
    ### Prepare stimuli:

    if curr_block in ["Reading_Baseline_main_no_click", "Reading_pseudotext_no_click"]:
        print(f"Start preparing block {curr_block}")

        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()

        ### Show instructions
        if curr_block == "Reading_Baseline_main_no_click":

            # set instruction text
            instr_text = locals()["instr_" + curr_block]
            # create text box
            instr_text_stim = visual.TextStim(win,
                                              text=instr_text,
                                              height=0.025,  # font height relative to height of screen
                                              pos=(0, 0),  # move up a bit
                                              color="black")

            # show instructions on screen
            win.setColor(light_bg_col, colorSpace='rgb')
            instr_text_stim.draw()
            win.flip()
            core.wait(1)  # wait for 3s before starting response window

            # get text nr:
            curr_text_nr = all_texts_nrs_list[exp_block_counter]
            curr_text = locals()[curr_text_nr]

            # compute RTs using participant's average reading speed / letter
            # we define a minimum and a maximum duration for each word
            # the minimum is based on 5 x RT per letter in the respective condition
            # the max duration is based on a time-out of 1.5 s in the reading baseline condition
            minimum_duration = 5 * RT_per_letter_baseline
            maximum_duration = 1500
            curr_durations = []
            for word in curr_text:
                duration = RT_per_letter_baseline * math.log((len(word))) + 4 * RT_per_letter_baseline
                if duration < maximum_duration:
                    curr_durations.append(max(duration, minimum_duration))
                else:
                    curr_durations.append(maximum_duration)

            # print(f"\tdurations for paced baseline block: {curr_durations}")

            ### change background colour
            win.setColor(dark_bg_col, colorSpace='rgb')
            win.flip()

            # show main block questions
            skip_questions_paced = False

        elif curr_block == "Reading_pseudotext_no_click":

            # set instruction text
            instr_text = locals()["instr_" + curr_block]
            # create text box
            instr_text_stim = visual.TextStim(win,
                                              text=instr_text,
                                              height=0.025,  # font height relative to height of screen
                                              pos=(0, 0),  # move up a bit
                                              color="black")

            # show instructions on screen
            win.setColor(light_bg_col, colorSpace='rgb')
            instr_text_stim.draw()
            win.flip()
            core.wait(1)  # wait for 3s before starting response window

            # get text nr:
            curr_text_nr = all_texts_nrs_list[exp_block_counter]
            curr_text = locals()[curr_text_nr]

            # compute RTs using participant's average reading speed / letter
            # we define a minimum and a maximum duration for each word
            # the minimum is based on 5 x RT per letter in the respective condition
            # the max duration is based on a time-out of 1.5 s in the reading baseline condition
            minimum_duration = 5 * RT_per_letter_baseline
            maximum_duration = 1500
            curr_durations = []
            for word in curr_text:
                duration = RT_per_letter_baseline * math.log((len(word))) + 4 * RT_per_letter_baseline
                if duration < maximum_duration:
                    curr_durations.append(max(duration, minimum_duration))
                else:
                    curr_durations.append(maximum_duration)

            # print(f"\tdurations for paced baseline block: {curr_durations}")

            ### change background colour
            win.setColor(dark_bg_col, colorSpace='rgb')
            win.flip()

            # show main block questions
            skip_questions_paced = True

        # Define n-back level
        curr_nback_cond = None

        print(f"\tcurrent n-back condition: {curr_nback_cond}")
        print(f"\tcurrent text: {curr_text_nr}")
        print(f"\texp block counter: {exp_block_counter}")

        # get list with targets & list with colours
        curr_targets = run1_target_lists[run1_block_counter]
        curr_colours = run1_colour_lists[run1_block_counter]

    ### Start block loop
    if curr_block in ["Reading_Baseline_main_no_click", "Reading_pseudotext_no_click"]:

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
            thisExp.addData('run_nr', 'run1')
            thisExp.addData('block_nr_run', run1_block_counter)
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

        if curr_block == "Reading_pseudotext_no_click":
            # show main block questions
            skip_questions_paced = True

            # go to next run
            exp_block_counter += 1
            run1_block_counter += 1
            print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
            continueRoutine = False

            # If there are still blocks left, go to next one.
            # If not, end loop here:
            if run1_block_counter == 2:
                print(f"Finished block {run1_block_counter}/2 in run 1, moving on to next run!")
                loop_run1_single_reading.finished = True

        # Send end of block trigger:
        # core.wait(time_after_trigger)  # wait 3 ms
        # send block offset trigger
        # send_trigger("block_offset")