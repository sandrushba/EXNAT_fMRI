def setup_instructions_and_stimuli(block_config, curr_instr, curr_instr_pic):
    """
    Setup and display instructions and stimuli based on the block configuration.
    """
    RT_per_letter = block_config['RT_per_letter']
    print(f"Start preparing block {block_config['name']}")
    print(f"\tUsing RT_per_letter for this block: {RT_per_letter}")

    # set light background
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()

    # set instruction text
    # instr_text = curr_instr
    # instr_pic = curr_instr_pic
    # create text box
    instr_text_stim = visual.TextStim(win,
                                      text=curr_instr,
                                      height=0.03,  # font height relative to height of screen
                                      pos=(0, 0.2),  # move up a bit
                                      color="black")

    # create ImageStim object
    instr_pic = visual.ImageStim(win,
                                 size=(0.85, 0.25),
                                 pos=(0, -0.2),
                                 image=curr_instr_pic)

    # show instructions on screen
    if 6 <= exp_block_counter <= 9:
        # instr_text = locals()["instr_" + curr_block]
        # instr_pic = locals()["instr_pic_" + curr_block]

        first_trigger_time = log_trigger(curr_instr, curr_instr_pic, trigger_count)

        return first_trigger_time
    else:
        win.setColor(light_bg_col, colorSpace='rgb')
        instr_text_stim.draw()
        instr_pic.draw()
        win.flip()
        core.wait(8.75)  # wait for 3s before starting
        # If esc is pressed, end the experiment:
        if 'escape' in event.getKeys():
            et_abort_exp()  # shut down eyetrigger and download incremental data
            # close trigger & close experiment
            core.wait(0.5)
            core.quit()


def calculate_durations(text, block_config):
    """
    Calculate word display durations based on the block configuration.
    """
    # compute RTs using participant's average reading speed / letter
    # we define a minimum and a maximum duration for each word
    # the minimum is based on 5 x RT per letter in the respective condition
    # the max duration is based on each condition
    RT_per_letter = block_config['RT_per_letter']
    minimum_duration = 5 * RT_per_letter

    if block_config['name'][0] == '1':
        maximum_duration = 2000  # 2 seconds
    elif block_config['name'][0] == '2':
        maximum_duration = 2500  # 2.5 seconds

    curr_durations = []
    for i, word in enumerate(curr_text):
        base_duration = RT_per_letter * math.log(len(word)) + 4 * RT_per_letter
        incremented_duration = base_duration + 3 * (i + 1)  # Increment increases with trial number
        if incremented_duration < maximum_duration:
            curr_durations.append(max(incremented_duration, minimum_duration))
        else:
            curr_durations.append(maximum_duration)

    return curr_durations


def process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                  curr_instr_pic):
    """
    Process each block based on its configuration.
    """
    first_trigger_time, trigger_count = setup_instructions_and_stimuli(block_config, curr_instr, curr_instr_pic)
    curr_durations = calculate_durations(curr_text, block_config)

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
    defaultKeyboard.clearEvents()

    # CREATE CLOCKS:
    my_block_clock = core.Clock()
    my_block_clock.reset()  # start block clock
    start_time = my_block_clock.getTime()  # get start time of block
    # also create trial clock
    my_trial_clock = core.Clock()

    # send block onset trigger
    send_trigger(curr_block + "_onset")

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
        # update the window to clear the screen and display
        # the stimulus, send trigger on flip
        win.callOnFlip(send_trigger, "trial_onset")

        # start trial clock & record trial onset time
        my_trial_clock.reset()
        global_onset_time = globalClock.getTime()
        onset_time_rel2trigger = global_onset_time - first_trigger_time

        ### wait for key response:
        # In blocks with n-back task, participants can press "c" to indicate they saw a target colour.

        ### start recording responses
        # start while loop that looks for responses
        # --> end while loop only if duration for current word is over
        while my_trial_clock.getTime() < (onset_time + curr_duration):

            stim.draw()
            win.flip()

            # check for key responses:
            keys = event.getKeys(['1', 'escape'])
            button_pressed = "NA"

            # if there were, check responses:
            for key in keys:

                # if participant pressed button "1" for the first time and it's an n-back condition
                # where they're actually supposed to do that (aka not a reading baseline condition)...
                if key == '1' and curr_nback_cond != None and saw_target == False:
                    # get reaction time
                    curr_nback_RT = my_trial_clock.getTime() * 1000
                    # send trigger for response:
                    send_trigger("response_target")
                    # only get first target response, we don't care if they press the button more than once:
                    saw_target = True

                # If esc is pressed, end the experiment:
                elif key == 'escape':
                    et_abort_exp()  # shut down eyetrigger and download incremental data
                    # close trigger & close experiment
                    # core.wait(time_after_trigger)
                    # parallel.setData(0)
                    core.wait(0.5)
                    core.quit()

        ### end trial
        # print("\tend paced trial")
        # stop display of current word & send trial offset trigger
        win.callOnFlip(send_trigger, "trial_offset")

        # check whether response was hit, miss, false alarm or correct rejection
        # they saw a target and there was one: hit
        if curr_nback_cond != None:
            if saw_target and curr_target:
                curr_nback_response = "hit"
                button_pressed = key
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
                button_pressed = key
        # if it wasn't an n-back task block:
        else:
            curr_target = None
            curr_nback_response = None
            curr_nback_RT = None

        ### save everything in output csv
        thisExp.addData('colour', curr_colour)
        thisExp.addData('global_onset_time', global_onset_time)
        thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
        thisExp.addData('target', curr_target)
        thisExp.addData('button_pressed', button_pressed)
        thisExp.addData('nback_response', curr_nback_response)
        thisExp.addData('nback_RT', curr_nback_RT)  # in ms
        thisExp.addData('duration', curr_duration * 1000)  # in ms
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('trial_nr', curr_trial_nr)
        thisExp.addData('block_nr_exp', exp_block_counter + 1)
        thisExp.addData('run_nr', run_nr)
        thisExp.addData('block_nr_run', block_nr_run)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)
        # careful, make sure quotes in the strings are escaped using a
        # quote (weird, I know) so it's properly saved in the CSV:
        thisExp.addData('word', escape_quotes(curr_word))

        # start a new row in the csv
        thisExp.nextEntry()

        ### IF TESTING MODE ENABLED: end loop after 4 trials
        if expInfo['testing_mode'] == "yes":
            if trial_idx == 9:
                break

    print("finished presenting trials")

    # send block offset trigger
    send_trigger("block_offset")

# Block configurations
block_configs = {
    "1back_dual_main_no_click": {
        "name": "1back_dual_main_no_click",
        "RT_per_letter": int(expInfo['RT_per_letter_oneback_dual']),
        # Add other block-specific configurations or parameters here
    },
    "2back_dual_main_no_click": {
        "name": "2back_dual_main_no_click",
        "RT_per_letter": int(expInfo['RT_per_letter_twoback_dual']),
        # Add other block-specific configurations or parameters here
    }
}

if exp_block_counter == 6:
    run_nr = 3
    block_nr_run = run3_block_counter + 1
    curr_block = run3_blocks
    curr_targets = run3_target_lists
    curr_colours = run3_colour_lists
    block_config = block_configs.get(curr_block)

    if block_config:
        curr_text_nr = all_texts_nrs_list[exp_block_counter]
        curr_text = locals()[curr_text_nr]  # Assuming this retrieves the text for the current block
        curr_instr = locals()["instr_" + block_config['name']]
        curr_instr_pic = locals()["instr_pic_" + block_config['name']]  # set path to image here

        # show main block questions
        skip_questions_paced = False
        process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                      curr_instr_pic)
        # continueRoutine = False
    else:
        print("Error: Block configuration not found.")

elif exp_block_counter == 7:
    run_nr = 4
    block_nr_run = run4_block_counter + 1
    curr_block = run4_blocks
    curr_targets = run4_target_lists
    curr_colours = run4_colour_lists
    block_config = block_configs.get(curr_block)

    if block_config:
        curr_text_nr = all_texts_nrs_list[exp_block_counter]
        curr_text = locals()[curr_text_nr]  # Assuming this retrieves the text for the current block
        curr_instr = locals()["instr_" + block_config['name']]
        curr_instr_pic = locals()["instr_pic_" + block_config['name']]  # set path to image here

        skip_questions_paced = False
        process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                      curr_instr_pic)
        # continueRoutine = False
    else:
        print("Error: Block configuration not found.")

elif exp_block_counter == 8:
    run_nr = 5
    block_nr_run = run5_block_counter + 1
    curr_block = run5_blocks
    curr_targets = run5_target_lists
    curr_colours = run5_colour_lists
    block_config = block_configs.get(curr_block)

    if block_config:
        curr_text_nr = all_texts_nrs_list[exp_block_counter]
        curr_text = locals()[curr_text_nr]  # Assuming this retrieves the text for the current block
        curr_instr = locals()["instr_" + block_config['name']]
        curr_instr_pic = locals()["instr_pic_" + block_config['name']]  # set path to image here

        skip_questions_paced = False
        process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                      curr_instr_pic)
        # continueRoutine = False
    else:
        print("Error: Block configuration not found.")

elif exp_block_counter == 9:
    run_nr = 6
    block_nr_run = run6_block_counter + 1
    curr_block = run6_blocks
    curr_targets = run6_target_lists
    curr_colours = run6_colour_lists
    block_config = block_configs.get(curr_block)

    if block_config:
        curr_text_nr = all_texts_nrs_list[exp_block_counter]
        curr_text = locals()[curr_text_nr]  # Assuming this retrieves the text for the current block
        curr_instr = locals()["instr_" + block_config['name']]
        curr_instr_pic = locals()["instr_pic_" + block_config['name']]  # set path to image here

        skip_questions_paced = False
        process_block(block_config, curr_text, run_nr, block_nr_run, curr_block, curr_targets, curr_colours, curr_instr,
                      curr_instr_pic)
        # continueRoutine = False
    else:
        print("Error: Block configuration not found.")