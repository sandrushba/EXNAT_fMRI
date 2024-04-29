#################################################
#            Blocks with text – paced           #
#################################################
# this routine is for all blocks with texts that are paced, i.e., visually presented without space bar

#---------- Calculate duration of words based on previous block ----------
# We collected RTs & words from the self-paced block of each condition
# for the training, we only use data from the reading BL since there is no separate training for 1- and 2-back

# we calculate letter duration based on condition since participants need more time for n-back tasks than for baseline reading
# BL reading blocks are based on duration during self-paced BL reading
# 1- and 2-back blocks are based on their respective self-paced version

# get block kind
curr_block = all_blocks[exp_block_counter]

if curr_block in ["Reading_Baseline_main_no_click", "Reading_Baseline_training_no_click"]:

    # exclude all RTs where participant was way too fast (< 50 ms) or
    # way too slow (> 2s), also remove the corresponding words from vis_task_words
    print("\tBL_paced_durations:", BL_paced_durations)
    print("\tBL_paced_words:", BL_paced_words)

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
    print("\tletters_total_BL:", letters_total_BL)
    # also get time it took in total to read them all:
    reading_time_total_BL = sum(filtered_durations_BL)  # in ms

    # Now check how many words / min they read on average.
    # reading_speed_wpm = words_total / (reading_time_total/60000)
    # print("reading speed in words / min:" + str(reading_speed_wpm))

    # Check average RT / letter
    RT_per_letter_baseline = reading_time_total_BL / letters_total_BL
    print("\taverage RT per letter in ms:", RT_per_letter_baseline)

    # save this in the output csv:
    thisExp.addData('RT_per_letter_baseline', RT_per_letter_baseline)

elif curr_block in ["1back_dual_main_no_click"]:

    # exclude all RTs where participant was way too fast (< 50 ms) or
    # way too slow (> 2s), also remove the corresponding words from vis_task_words
    print("\t1back_paced_durations:", oneback_paced_durations)
    print("\t1back_paced_words:", oneback_paced_words)

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
    print("\tletters_total_1bck:", letters_total_1bck)
    # also get time it took in total to read them all:
    reading_time_total_1bck = sum(filtered_durations_1bck)  # in ms

    # Now check how many words / min they read on average.
    # reading_speed_wpm = words_total / (reading_time_total/60000)
    # print("reading speed in words / min:" + str(reading_speed_wpm))

    # Check average RT / letter
    RT_per_letter_1bck = reading_time_total_1bck / letters_total_1bck
    print("\taverage RT per letter in ms:", RT_per_letter_1bck)

    # save this in the output csv:
    thisExp.addData('RT_per_letter_1bck', RT_per_letter_1bck)

elif curr_block in ["2back_dual_main_no_click"]:

    # exclude all RTs where participant was way too fast (< 50 ms) or
    # way too slow (> 2.5s), also remove the corresponding words from vis_task_words
    print("\t2back_paced_durations:", twoback_paced_durations)
    print("\t2back_paced_words:", twoback_paced_words)

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
    print("\tletters_total_2bck:", letters_total_2bck)
    # also get time it took in total to read them all:
    reading_time_total_2bck = sum(filtered_durations_2bck)  # in ms

    # Now check how many words / min they read on average.
    # reading_speed_wpm = words_total / (reading_time_total/60000)
    # print("reading speed in words / min:" + str(reading_speed_wpm))

    # Check average RT / letter
    RT_per_letter_2bck = reading_time_total_2bck / letters_total_2bck
    print("\taverage RT per letter in ms:", RT_per_letter_2bck)

    # save this in the output csv:
    thisExp.addData('RT_per_letter_2bck', RT_per_letter_2bck)

# keep background ivory
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()

# ----------------------------------

# clear buffer of all previously recorded key events:
event.clearEvents()

### specify settings for the current block

### Prepare stimuli:

# get block kind
curr_block = all_blocks[exp_block_counter]
# print("start preparing block " + curr_block)

# Check whether it's a block that is self-paced
# Also, if current block is a non-text block, skip this routine.
if curr_block in ["click_training", "1back_single_training1", "1back_single_training2",
                  "2back_single_training1", "2back_single_training2",
                  "Reading_Baseline_main_click", "1back_dual_main_click", "2back_dual_main_click", "Reading_Baseline_training_click"]:
    print(f"this is block {curr_block}")
    print("\tskipping paced routine")
    # skip questions & end current routine
    skip_questions_paced = True
    continueRoutine = False
    # break

# if it's the paced reading training block, prepare training stimuli:
elif curr_block == "Reading_Baseline_training_no_click":
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
                                      pos=(0, 0),  # move up a bit
                                      color="black")

    # show instructions on screen
    win.setColor(light_bg_col, colorSpace='rgb')
    instr_text_stim.draw()
    win.flip()
    core.wait(3)  # wait for 3s before starting response window

    # display the text on screen
    while True:
        # keep background ivory
        win.setColor(light_bg_col, colorSpace='rgb')
        instr_text_stim.draw()
        win.flip()
        # end showing screen if participant presses space
        if 'space' in event.getKeys():
            break

    # clear buffer of all previously recorded key events:
    event.clearEvents()

    ### get training text
    curr_text_training = reading_bl_tr_text_no_click
    curr_text_nr = "Reading_Baseline_training_no_click"
    curr_text = curr_text_training
    curr_nback_cond = None
    # show training questions
    skip_questions_paced = False
    training_Qs_paced = True

    # get list with targets & list with colours
    curr_targets = all_target_lists[exp_block_counter]
    curr_colours = all_colour_lists[exp_block_counter]

    # compute RTs using participant's average reading speed / letter – old, based on linear increase of RTs,
    # feels very unnatural however
    # curr_durations = [len(word) * RT_per_letter_baseline for word in curr_text]  # in ms

    # compute RTs using participant's average reading speed / letter
    # we define a minimum and a maximum duration for each word
    # the minimum is based on 5 x RT per letter in the respective condition
    # the max duration is based on a time-out of 1.5 s in the reading baseline condition
    minimum_duration = 5 * RT_per_letter_baseline
    maximum_duration = 1500
    curr_durations = []
    for word in curr_text:
        # this is an absolute value based on estimates of how long you need to feel comfortable reading a word on
        # screen in a paced task
        # duration = RT_per_letter_baseline * math.log((len(word))) + 300
        # more flexible solution:
        duration = RT_per_letter_baseline * math.log((len(word))) + 4 * RT_per_letter_baseline
        if duration < maximum_duration:
            curr_durations.append(max(duration, minimum_duration))
        else:
            curr_durations.append(maximum_duration)

    print(f"\tdurations for paced task training block: {curr_durations}")

    # we also need the start time (let's set it as current time
    # at this point in the script):
    start_time = core.getTime()

    ### change background colour
    win.setColor(dark_bg_col, colorSpace='rgb')
    win.flip()

# if it's one of the "normal" main blocks, prepare main block stimuli:
elif curr_block in ["Reading_Baseline_main_no_click", "1back_dual_main_no_click", "2back_dual_main_no_click"]:
    print(f"start preparing block {curr_block}")

    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()

    ### Show instructions
    # only add image, if it's a 1- or 2-back block where participants have to press "c"
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
        core.wait(3)  # wait for 3s before starting response window

        # Display the text on screen
        while True:
            instr_text_stim.draw()
            win.flip()
            # end showing screen if participant presses space
            if 'space' in event.getKeys():
                break

        # get text nr:
        curr_text_nr = all_texts_nrs_list[exp_block_counter]
        curr_text = locals()[curr_text_nr]

        # compute RTs using participant's average reading speed / letter – old, based on linear increase of RTs,
        # feels very unnatural however
        # curr_durations = [len(word) * RT_per_letter_baseline for word in curr_text]  # in ms

        # compute RTs using participant's average reading speed / letter
        # we define a minimum and a maximum duration for each word
        # the minimum is based on 5 x RT per letter in the respective condition
        # the max duration is based on a time-out of 1.5 s in the reading baseline condition
        minimum_duration = 5 * RT_per_letter_baseline
        maximum_duration = 1500
        curr_durations = []
        for word in curr_text:
            # this is an absolute value based on estimates of how long you need to feel comfortable reading a word on
            # screen in a paced task
            # duration = RT_per_letter_baseline * math.log((len(word))) + 300
            # more flexible solution:
            duration = RT_per_letter_baseline * math.log((len(word))) + 4 * RT_per_letter_baseline
            if duration < maximum_duration:
                curr_durations.append(max(duration, minimum_duration))
            else:
                curr_durations.append(maximum_duration)

        print(f"\tdurations for paced baseline block: {curr_durations}")

        ### change background colour
        win.setColor(dark_bg_col, colorSpace='rgb')
        win.flip()

    elif curr_block in ["1back_dual_main_no_click", "2back_dual_main_no_click"]:

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

        # get text nr:
        curr_text_nr = all_texts_nrs_list[exp_block_counter]
        curr_text = locals()[curr_text_nr]
        # compute RTs using participant's average reading speed / letter
        if curr_block == "1back_dual_main_no_click":
            # curr_durations = [len(word) * RT_per_letter_1bck for word in curr_text]  # in ms

            # compute RTs using participant's average reading speed / letter
            # we define a minimum and a maximum duration for each word
            # the minimum is based on 5 x RT per letter in the respective condition
            # the max duration is based on a time-out of 2 s in the 1-back condition
            minimum_duration = 5 * RT_per_letter_1bck
            maximum_duration = 2000
            curr_durations = []
            for word in curr_text:
                # this is an absolute value based on estimates of how long you need to feel comfortable reading a
                # word on screen in a paced task
                # duration = RT_per_letter_baseline * math.log((len(word))) + 300 more
                # more flexible solution:
                duration = RT_per_letter_1bck * math.log((len(word))) + 4 * RT_per_letter_1bck
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
            minimum_duration = 5 * RT_per_letter_2bck
            maximum_duration = 2000
            curr_durations = []
            for word in curr_text:
                # this is an absolute value based on estimates of how long you need to feel comfortable reading a word on
                # screen in a paced task
                # duration = RT_per_letter_baseline * math.log((len(word))) + 300
                # more flexible solution:
                duration = RT_per_letter_2bck * math.log((len(word))) + 4 * RT_per_letter_2bck
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

        print(f"\tdurations for paced n-back block: {curr_durations}")

        ### change background colour
        win.setColor(dark_bg_col, colorSpace='rgb')
        win.flip()

    # show main block questions
    skip_questions_paced = False
    training_Qs_paced = False

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
    print(f"\tcurrent text: {curr_text_nr}")

    # get list with targets & list with colours
    curr_targets = all_target_lists[exp_block_counter]
    curr_colours = all_colour_lists[exp_block_counter]
    # for current text nr, get text whose name = current text nr
    # curr_text = locals()[curr_text_nr]

### Start block loop
if curr_block in ["Reading_Baseline_training_no_click", "Reading_Baseline_main_no_click", "1back_dual_main_no_click",
                  "2back_dual_main_no_click"]:

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
        thisExp.addData('block_nr', exp_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('block_kind', curr_nback_cond)
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

    # Send end of block trigger:
    # core.wait(time_after_trigger)  # wait 3 ms
    # send block offset trigger
    # send_trigger("block_offset")

# end current routine
# continueRoutine = False