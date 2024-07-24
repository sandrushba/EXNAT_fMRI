#################################################
#          Blocks w/o text – self-paced         #
#################################################
# this routine is for all blocks where there are
# coloured rectangles instead of words

# Use loop here that runs the non-text blocks
# until we have to display a main text block (in this case we exit the routine).

while True:
    event. Mouse(visible=False)
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()

    # clear buffer of all previously recorded key events:
    event.clearEvents()

    ### specify settings for the current block

    ### Prepare stimuli:

    # get block kind
    curr_block = all_blocks[exp_block_counter]

    # Check whether it's one of the non-text tasks.
    # If current block is a text block, skip this routine and go to the next.
    if curr_block not in ["click_training", "0back_single_training", "1back_single_training1", "1back_single_training2",
                          "1back_single_main", "2back_single_training1", "2back_single_training2", "2back_single_main"]:
        print(f"this is block {curr_block}")
        print(f"\tskipping self-paced n-back routine")
        break

    # if it's one of the non-text blocks, though, prepare stimuli:
    else:
        print(f"this is block {curr_block}")
        print(f"\tstart preparing block {curr_block}")
        # print("\t" + curr_block + " is not a text block - preparing rect as stim now")

        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        win.flip()

        ### Show instructions
        # set instruction text
        if curr_block == "0back_single_training":
            # create text boxes
            instr_text_stim1 = visual.TextStim(win,
                                               text=locals()["instr_0back_single_training1"],
                                               height=0.025,  # font height relative to height of screen
                                               pos=(0, 0.30),  # move instructions up a bit
                                               color="black")
            instr_text_stim2 = visual.TextStim(win,
                                               text=locals()["instr_0back_single_training2"],
                                               height=0.025,  # font height: 5° visual angle
                                               pos=(0, -0.35),  # move instructions down a bit
                                               color="black")
            # create "empty" circle as stimulus
            instr_colour_circle_stim = visual.Circle(win=win,
                                                     radius=0.065,
                                                     pos=(0, 0.1))  # move circle slightly down

            # set current target colour as colour of circle:
            instr_colour_circle_stim.fillColor = target_colours_list[0]

            # create ImageStim object
            curr_instr_pic = visual.ImageStim(win,
                                              size=(0.55, 0.25),
                                              pos=(0, -0.15),
                                              image=locals()["instr_pic_0back"])  # set path to image here

        else:
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

        # display the text & image on screen
        if curr_block == "0back_single_training":
            # show instructions on screen
            instr_text_stim1.draw()
            instr_text_stim2.draw()
            instr_colour_circle_stim.draw()
            curr_instr_pic.draw()
            win.flip()
            core.wait(3)  # wait for 3s before starting response window

            # display the text & the circle on screen until Space is pressed
            while True:
                instr_text_stim1.draw()
                instr_text_stim2.draw()
                instr_colour_circle_stim.draw()
                curr_instr_pic.draw()
                win.flip()
                # end screen if participant presses space
                if event.getKeys(['space']):
                    print("\t\tstart current block")
                    skip_curr_block = False
                    break

        elif curr_block in ["1back_single_training2", "2back_single_training2"]:
            # draw instructions on screen
            instr_text_stim.draw()
            curr_instr_pic.draw()
            win.flip()
            core.wait(3)  # wait for 3 s before starting response window

            while True:
                instr_text_stim.draw()
                curr_instr_pic.draw()
                win.flip()
                # skip current block (aka the second training block))
                if event.getKeys(['space']):
                    print("\t\tstart next block - skip second training block")
                    skip_curr_block = True
                    break
                # repeat training (aka run current block, which is the second training block)
                elif event.getKeys(['w']):
                    print("\t\trepeat training block")
                    skip_curr_block = False
                    break

        # for regular blocks that can't be repeated:
        else:
            while True:
                instr_text_stim.draw()
                curr_instr_pic.draw()
                win.flip()
                # start current block
                if event.getKeys(['space']):
                    print("\t\tstart current block")
                    skip_curr_block = False
                    break

        # only run this if the current block shall not be skipped:
        if skip_curr_block == False:
            ### change background colour
            win.setColor(dark_bg_col, colorSpace='rgb')
            win.flip()

            # don't show questions
            skip_questions = True
            training_Qs = False

            # get n-back condition:
            curr_nback_cond = curr_block[0]  # get first character of block name

            # if it is a 0, 1 or 2, set that as current n-back level:
            if curr_nback_cond in ['0', '1', '2']:
                curr_nback_cond == int(curr_nback_cond)
            # if it's neither 0, 1 nor 2, it has to be a block without n-back,
            # so set curr_nback_cond to None
            else:
                curr_nback_cond = None

            print(f"\tcurrent n-back condition: {curr_nback_cond}")

            # get list with targets & list with colours
            curr_targets = all_target_lists[exp_block_counter]
            curr_colours = all_colour_lists[exp_block_counter]

            ### Start block loop
            # depending on condition, create arrays for saving response
            # times - we need that later for the paced task of the 1- and 2-back single blocks
            if curr_block == "1back_single_main":
                oneback_single_paced_durations = []
            elif curr_block == "2back_single_main":
                twoback_single_paced_durations = []

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

                # onset_time = my_trial_clock.getTime()

                ### wait for key response:
                # In blocks with n-back task, participants can press "c" to indicate they saw a target colour and "space" to go to the next word/stimulus.
                # In blocks without n-back task, participants can only press "space" to go to the next stimulus.
                # print("start tracking key responses")

                ### start recording responses
                # start "endless" while loop that looks for responses
                # in each iteration, draw word on screen
                continue_trial = True
                while continue_trial:

                    # draw stimulus on screen
                    stim.draw()
                    win.flip()

                    # check for responses:
                    keys = event.getKeys(['space', 'c', 'escape'])

                    # check if there was a response. If there wasn't, we can go straight
                    # to the next iteration which will hopefully save us some dropped
                    # frames in the flicker.
                    for key in keys:

                        # if participant pressed the space bar on their keyboard...
                        if key == 'space':
                            # get reaction time
                            curr_duration = my_trial_clock.getTime() * 1000
                            # send trigger for response:
                            # send_trigger("response_continue")

                            # break while loop to go to next trial
                            continue_trial = False

                        # if participant pressed button "c" for the first time and it's an n-back condition
                        # where they're actually supposed to do that (aka not a reading baseline condition)...
                        elif key == 'c' and curr_nback_cond != None and saw_target == False:
                            # get reaction time
                            curr_nback_RT = my_trial_clock.getTime() * 1000

                            # send trigger for response:
                            # send_trigger("response_target")

                            # only get first target response, we don't care if they press the button more than once:
                            saw_target = True

                        # If esc is pressed, end the experiment:
                        elif key == 'escape':
                            # et_abort_exp()  # shut down eyetrigger and download incremental data
                            # make sure parallel port line is cleared
                            # core.wait(time_after_trigger)
                            # parallel.setData(0)
                            core.wait(0.5)
                            # end experiment
                            core.quit()

                    # Check for timeout - if more than 1.5 or 2 seconds have passed, move to the next trial
                    if my_trial_clock.getTime() - trial_start_time >= 1.5 and curr_block in [
                        "Oback_single_training", "1back_single_training1", "1back_single_training2", "1back_single_main"]:
                        curr_duration = 1500
                        continue_trial = False
                    elif my_trial_clock.getTime() - trial_start_time >= 2 and curr_block in [
                        "2back_single_training1", "2back_single_training2", "2back_single_main"]:
                        curr_duration = 2000
                        continue_trial = False

                ### end trial
                # print("end trial")

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
                thisExp.addData('duration', curr_duration)  # in ms
                thisExp.addData('trial_nr', curr_trial_nr)
                thisExp.addData('block_nr', exp_block_counter)
                thisExp.addData('block_name', curr_block)
                thisExp.addData('block_kind', curr_nback_cond)

                # start a new row in the csv
                thisExp.nextEntry()

                # depending on condition, save response times and words in previously created arrays
                # we need that later for the paced reading tasks
                if curr_block == "1back_single_main":
                    oneback_single_paced_durations.append(curr_duration)
                elif curr_block == "2back_single_main":
                    twoback_single_paced_durations.append(curr_duration)

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