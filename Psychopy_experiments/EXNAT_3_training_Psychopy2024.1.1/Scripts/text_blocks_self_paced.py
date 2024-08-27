#################################################
#           Blocks with text – self-paced       #
#################################################
# this routine is for all blocks with texts that are self-paced

# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# clear buffer of all previously recorded key events:
event.clearEvents()

### specify settings for the current block

### Prepare stimuli:

# get block kind
curr_block = all_blocks[exp_block_counter]
# print("start preparing block " + curr_block)

# Check whether it's a block that isn't self-paced
# If yes, skip this routine
if curr_block in ["click_training", "0back_single_training", "1back_single_training1", "1back_single_training2",
                  "1back_single_main", "2back_single_training1", "2back_single_training2", "2back_single_main",
                  "Reading_Baseline_main_no_click", "0back_dual_main_no_click", "1back_dual_main_no_click", "2back_dual_main_no_click",
                  "Reading_Baseline_training_no_click", "1back_single_main_no_click", "2back_single_main_no_click"]:
    print(f"this is block {curr_block}")
    print("\tskipping self-paced text routine")
    # skip questions & end current routine
    skip_questions = True
    continueRoutine = False
    # break

# if it's the reading bl training block, prepare training stimuli:
elif curr_block == "Reading_Baseline_training_click":
    print(f"this is block {curr_block}")
    print(f"start preparing block {curr_block}")

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
                                      size=(0.6, 0.3),
                                      pos=(0, -0.2),
                                      image=locals()["instr_pic_" + curr_block])  # set path to image here

    # show instructions on screen
    win.setColor(light_bg_col, colorSpace='rgb')
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

    ### get training text
    curr_text = reading_bl_tr_text
    curr_text_nr = "reading_bl_training_text"
    curr_nback_cond = None
    curr_colours = all_colour_lists[0]
    # show training questions
    skip_questions = False
    training_Qs = True

    # we also need the start time (let's set it as current time
    # at this point in the script):
    start_time = core.getTime()

    ### change background colour
    win.setColor(dark_bg_col, colorSpace='rgb')
    win.flip()

    print(f"\tcurrent text: {curr_text_nr}")

# if it's one of the "normal" main blocks, prepare main block stimuli:
elif curr_block in ["Reading_Baseline_main_click", "0back_dual_main_click", "1back_dual_main_click", "2back_dual_main_click"]:
    print(f"this is block {curr_block}")
    print(f"start preparing block {curr_block}")

    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()

    ### Show instructions
    # set instruction text
    if curr_block == "0back_dual_main_click":
        # create text boxes
        instr_text_stim1 = visual.TextStim(win,
                                           text=locals()["instr_0back_dual_main_click1"],
                                           height=0.025,  # font height relative to height of screen
                                           pos=(0, 0.3),  # move instructions up a bit
                                           color="black")
        instr_text_stim2 = visual.TextStim(win,
                                           text=locals()["instr_0back_dual_main_click2"],
                                           height=0.025,  # font height: 5° visual angle
                                           pos=(0, -0.35),  # move instructions down a bit
                                           color="black")
        # create "empty" circle as stimulus
        instr_colour_circle_stim = visual.Circle(win=win,
                                                 radius=0.065,
                                                 pos=(0, 0.1))  # move circle slightly down

        # set current target colour as colour of circle:
        instr_colour_circle_stim.fillColor = target_colours_list[1]

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
        if curr_block == "Reading_Baseline_main_click":
            # create ImageStim object
            curr_instr_pic = visual.ImageStim(win,
                                              size=(0.6, 0.3),
                                              pos=(0, -0.2),
                                              image=locals()["instr_pic_" + curr_block])  # set path to image here
        else:
            # create ImageStim object
            curr_instr_pic = visual.ImageStim(win,
                                              size=(0.8, 0.3),
                                              pos=(0, -0.2),
                                              image=locals()["instr_pic_" + curr_block])  # set path to image here

    # show instructions
    if curr_block == "0back_dual_main_click":
        win.setColor(light_bg_col, colorSpace='rgb')
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
                break

    else:
        win.setColor(light_bg_col, colorSpace='rgb')
        instr_text_stim.draw()
        curr_instr_pic.draw()
        win.flip()
        core.wait(3)  # wait for 3s before starting response window

        # Display the text on screen
        while True:
            instr_text_stim.draw()
            curr_instr_pic.draw()
            win.flip()
            # end showing screen if participant presses space
            if 'space' in event.getKeys():
                break

    ### change background colour
    win.setColor(dark_bg_col, colorSpace='rgb')
    win.flip()

    # show main block questions
    skip_questions = False
    training_Qs = False

    # get text nr:
    curr_text_nr = all_texts_nrs_list[exp_block_counter]

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
    print(f"\tcurrent text: {curr_text_nr}")

    # get list with targets & list with colours
    curr_targets = all_target_lists[exp_block_counter]
    curr_colours = all_colour_lists[exp_block_counter]
    # for current text nr, get text whose name = current text nr
    curr_text = locals()[curr_text_nr]

### Start block loop
if curr_block in ["Reading_Baseline_training_click", "Reading_Baseline_main_click", "0back_dual_main_click", "1back_dual_main_click", "2back_dual_main_click"]:
    # depending on condition, create arrays for saving response
    # times & words - we need that later for the paced reading tasks
    if curr_block == "Reading_Baseline_main_click":
        BL_paced_durations = []
        BL_paced_words = []
    elif curr_block == "0back_dual_main_click":
        zeroback_paced_durations = []
        zeroback_paced_words = []
    elif curr_block == "1back_dual_main_click":
        oneback_paced_durations = []
        oneback_paced_words = []
    elif curr_block == "2back_dual_main_click":
        twoback_paced_durations = []
        twoback_paced_words = []

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

        # get trial number (start counting from 1, so add 1)
        curr_trial_nr = trial_idx + 1

        # set current word & colour as content of text stimulus
        stim.color = curr_colour
        stim.text = curr_word

        # show word on screen
        stim.draw()  # draw word on screen

        # start trial clock
        my_trial_clock.reset()
        onset_time = my_trial_clock.getTime()

        ### wait for 50 ms
        while my_trial_clock.getTime() < onset_time + 0.05:

            # draw the stimulus during the waiting period
            stim.draw()  # draw text
            win.flip()

        ### wait for key response:
        # In blocks with n-back task, participants can press "c" to indicate they saw a target colour and "space" to go to the next word/stimulus.
        # In blocks without n-back task, participants can only press "space" to go to the next word/stimulus.
        # print("start tracking key responses")

        ### start recording responses
        # start "endless" while loop that looks for responses
        continue_trial = True
        trial_start_time = my_trial_clock.getTime()  # Record the start time of the trial
        while continue_trial:

            # in each iteration, draw word on screen
            stim.draw()
            win.flip()

            # check for key responses:
            keys = event.getKeys(['space', 'c', 'escape'])

            # if we recorded a response, check which one.
            # If not, we go  to the next "while" iteration,
            # so I hope this saves us a few dropped frames in the flicker.
            for key in keys:

                # if participant pressed space bar on their keyboard...
                if key == 'space':
                    # get reaction time
                    curr_duration = my_trial_clock.getTime() * 1000
                    # send trigger for response:
                    # send_trigger("response_continue")
                    # break while loop
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
                    # close trigger & close experiment
                    # core.wait(time_after_trigger)
                    # parallel.setData(0)
                    core.wait(0.5)
                    core.quit()

            # Check for timeout - if more than 1.5, 2 or 2.5 seconds have passed, move to the next trial
            if my_trial_clock.getTime() - trial_start_time >= 1.5 and curr_block in ["Reading_Baseline_training_click", "Reading_Baseline_main_click",
                                                                                     "0back_dual_main_click"]:
                curr_duration = 1500
                continue_trial = False
            elif my_trial_clock.getTime() - trial_start_time >= 2 and curr_block == "1back_dual_main_click":
                curr_duration = 2000
                continue_trial = False
            elif my_trial_clock.getTime() - trial_start_time >= 2.5 and curr_block == "2back_dual_main_click":
                curr_duration = 2500
                continue_trial = False

        ### end trial
        # print("\tend self-paced trial")
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
        if curr_block == "0back_dual_main_click":
            thisExp.addData('curr_0back_target', target_colours_list[1])
        thisExp.addData('nback_response', curr_nback_response)
        thisExp.addData('nback_RT', curr_nback_RT)  # in ms
        thisExp.addData('duration', curr_duration)  # in ms
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('trial_nr', curr_trial_nr)
        thisExp.addData('block_nr', exp_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('block_kind', curr_nback_cond)
        # careful, make sure quotes in the strings are escaped using a
        # quote (weird, I know) so it's properly saved in the CSV:
        thisExp.addData('word', escape_quotes(curr_word))

        # start a new row in the csv
        thisExp.nextEntry()

        # depending on condition, save response times and words in previously created arrays
        # we need that later for the paced reading tasks
        if curr_block == "Reading_Baseline_main_click":
            BL_paced_durations.append(curr_duration)
            BL_paced_words.append(curr_word)
        elif curr_block == "0back_dual_main_click":
            zeroback_paced_durations.append(curr_duration)
            zeroback_paced_words.append(curr_word)
        elif curr_block == "1back_dual_main_click":
            oneback_paced_durations.append(curr_duration)
            oneback_paced_words.append(curr_word)
        elif curr_block == "2back_dual_main_click":
            twoback_paced_durations.append(curr_duration)
            twoback_paced_words.append(curr_word)

        ### IF TESTING MODE ENABLED: end loop after 4 trials
        if expInfo['testing_mode'] == "yes":
            if trial_idx == 3:
                break

    print("finished presenting trials")

    if 11 <= exp_block_counter < 12:
        # Calculate and print out RTs per letter for each condition. This is needed to have these times if the training experiment breaks or fails or needs to be stopped
        filtered_durations_BL = []
        filtered_words_BL = []
        for duration, word in zip(BL_paced_durations, BL_paced_words):
            if 50 <= duration <= 1500:
                filtered_durations_BL.append(duration)
                filtered_words_BL.append(word)
        # print("\tfiltered_durations_BL:", filtered_durations_BL)
        # print("\tfiltered_words_BL:", filtered_words_BL)

        # Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
        letters_total_BL = sum(len(word) for word in filtered_words_BL)
        # print("\tletters_total_BL:", letters_total_BL)
        # also get time it took in total to read them all:
        reading_time_total_BL = sum(filtered_durations_BL)  # in ms

        # Now check how many words / min they read on average.
        # reading_speed_wpm = words_total / (reading_time_total/60000)
        # print("reading speed in words / min:" + str(reading_speed_wpm))

        # Check average RT / letter
        RT_per_letter_baseline = reading_time_total_BL / letters_total_BL
        print("\tRT_per_letter_baseline:", round(RT_per_letter_baseline))

        # save this in the output csv:
        thisExp.addData('RT_per_letter_baseline', round(RT_per_letter_baseline))

        # elif curr_block in ["0back_dual_main_no_click"]:

        filtered_durations_0back = []
        filtered_words_0back = []
        for duration, word in zip(zeroback_paced_durations, zeroback_paced_words):
            if 50 <= duration <= 1500:
                filtered_durations_0back.append(duration)
                filtered_words_0back.append(word)
        # print("\tfiltered_durations_BL:", filtered_durations_BL)
        # print("\tfiltered_words_BL:", filtered_words_BL)

        # Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
        letters_total_0back = sum(len(word) for word in filtered_words_0back)
        # print("\tletters_total_0back:", letters_total_0back)
        # also get time it took in total to read them all:
        reading_time_total_0back = sum(filtered_durations_0back)  # in ms

        # Now check how many words / min they read on average.
        # reading_speed_wpm = words_total / (reading_time_total/60000)
        # print("reading speed in words / min:" + str(reading_speed_wpm))

        # Check average RT / letter
        RT_per_letter_0back = reading_time_total_0back / letters_total_0back
        print("\tRT_per_letter_0back:", round(RT_per_letter_0back))

        # save this in the output csv:
        thisExp.addData('RT_per_letter_0back', round(RT_per_letter_0back))

        # elif curr_block in ["1back_dual_main_no_click"]:

        filtered_durations_1bck = []
        filtered_words_1bck = []
        for duration, word in zip(oneback_paced_durations, oneback_paced_words):
            if 50 <= duration <= 2000:
                filtered_durations_1bck.append(duration)
                filtered_words_1bck.append(word)
        # print("\tfiltered_durations_1bck:", filtered_durations_1bck)
        # print("\tfiltered_words_1bck:", filtered_words_1bck)

        # Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
        letters_total_1bck = sum(len(word) for word in filtered_words_1bck)
        # print("\tletters_total_1bck:", letters_total_1bck)
        # also get time it took in total to read them all:
        reading_time_total_1bck = sum(filtered_durations_1bck)  # in ms

        # Now check how many words / min they read on average.
        # reading_speed_wpm = words_total / (reading_time_total/60000)
        # print("reading speed in words / min:" + str(reading_speed_wpm))

        # Check average RT / letter
        RT_per_letter_1bck = reading_time_total_1bck / letters_total_1bck
        print("\tRT_per_letter_1bck:", round(RT_per_letter_1bck))

        # save this in the output csv:
        thisExp.addData('RT_per_letter_1bck', round(RT_per_letter_1bck))

        # elif curr_block in ["2back_dual_main_no_click"]:

        filtered_durations_2bck = []
        filtered_words_2bck = []
        for duration, word in zip(twoback_paced_durations, twoback_paced_words):
            if 50 <= duration <= 2500:
                filtered_durations_2bck.append(duration)
                filtered_words_2bck.append(word)
        # print("\tfiltered_durations_2bck:", filtered_durations_2bck)
        # print("\tfiltered_words_2bck:", filtered_words_2bck)

        # Now get number of letters (not words, I want to know how fast they read 1 letter on average!):
        letters_total_2bck = sum(len(word) for word in filtered_words_2bck)
        # print("\tletters_total_2bck:", letters_total_2bck)
        # also get time it took in total to read them all:
        reading_time_total_2bck = sum(filtered_durations_2bck)  # in ms

        # Now check how many words / min they read on average.
        # reading_speed_wpm = words_total / (reading_time_total/60000)
        # print("reading speed in words / min:" + str(reading_speed_wpm))

        # Check average RT / letter
        RT_per_letter_2bck = reading_time_total_2bck / letters_total_2bck
        print("\tRT_per_letter_2bck:", round(RT_per_letter_2bck))

        # save this in the output csv:
        thisExp.addData('RT_per_letter_2bck', round(RT_per_letter_2bck))

        # if curr_block == "1back_single_main_no_click":

        filtered_durations_oneback_single = []
        for duration in oneback_single_paced_durations:
            if 50 <= duration <= 1500:
                filtered_durations_oneback_single.append(duration)
        # count n of trials:
        oneback_single_trials = len(filtered_durations_oneback_single)
        # get time it took in total:
        oneback_single_time_total = sum(filtered_durations_oneback_single)  # in ms

        # Check average RT / rectangle
        RT_per_rectangle_oneback_single = oneback_single_time_total / oneback_single_trials
        print("\taverage RT per rectangle in ms for single 1back:", round(RT_per_rectangle_oneback_single))

        # save this in the output csv:
        thisExp.addData('RT_per_rect_1back_single', round(RT_per_rectangle_oneback_single))

        # elif curr_block == "2back_single_main_no_click":

        filtered_durations_twoback_single = []
        for duration in twoback_single_paced_durations:
            if 50 <= duration <= 2000:
                filtered_durations_twoback_single.append(duration)
        # count n of trials:
        twoback_single_trials = len(filtered_durations_twoback_single)
        # get time it took in total:
        twoback_single_time_total = sum(filtered_durations_twoback_single)  # in ms

        # Check average RT / rectangle
        RT_per_rectangle_twoback_single = twoback_single_time_total / twoback_single_trials
        print("\taverage RT per rectangle in ms for single 2back:", round(RT_per_rectangle_twoback_single))

        # save this in the output csv:
        thisExp.addData('RT_per_rect_2back_single', round(RT_per_rectangle_twoback_single))

    # end current routine
    continueRoutine = False