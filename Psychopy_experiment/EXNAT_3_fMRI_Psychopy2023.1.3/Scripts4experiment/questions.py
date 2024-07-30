##########################################################
#              Text Comprehension Questions              #
##########################################################

def setup_question(question_text, answers_text):
    question = visual.TextStim(win, text=question_text, pos=(0, 0.2), color="black", height=0.03, anchorHoriz='center', alignText='center', wrapWidth=1)
    answers = [visual.TextStim(win, text=ans, pos=(0, 0.1 - i * 0.08), color="black", height=0.03, wrapWidth=1, anchorHoriz='center', alignText='center') for i, ans in enumerate(answers_text)]
    return question, answers

from psychopy import visual, core, event
from psychopy.hardware import keyboard

def display_question_and_get_response(question, answers, correct_answer):
    defaultKeyboard.clearEvents()

    # Set-up time to write into logfile
    question_time = globalClock.getTime()
    onset_time_rel2trigger = question_time - first_trigger_time

    question.autoDraw = True
    for answer in answers:
        answer.autoDraw = True
    instr_text.autoDraw = True

    countdown_timer = visual.TextStim(win, text='', pos=(0, -0.25), color="grey", height=0.02, anchorHoriz='center', alignText='center', wrapWidth=1)

    # defaultKeyboard = keyboard.Keyboard()
    chosen_ans = "NA"
    is_correct = "NA"
    button_pressed = "NA"
    response_received = False

    # Start a clock to track response time
    response_clock = core.Clock()

    # Countdown from 10 seconds
    while response_clock.getTime() < 10:
        remaining_time = 10 - int(response_clock.getTime())
        countdown_timer.text = f"Zeit: {remaining_time}"
        countdown_timer.draw()
        win.flip()

        keys = defaultKeyboard.getKeys(['1', '2', '3', '4'], waitRelease=False)
        if keys:
            key_name = keys[0].name  # Get the name of the first key pressed
            button_pressed = key_name

            # Now, use the key_name to determine the action
            if key_name == '1':
                index = 0  # Corresponds to the first choice
            elif key_name == '2':
                index = 1  # Corresponds to the second choice
            elif key_name == '3':
                index = 2  # Corresponds to the third choice
            elif key_name == '4':
                index = 3  # Corresponds to the fourth choice
            else:
                index = None  # Just in case, not really needed if you're sure about the input keys

            # Proceed with your logic based on the index
            if index is not None:
                chosen_ans = chr(97 + index)  # Convert index to letter ('a', 'b', 'c', 'd')
                is_correct = chosen_ans == correct_answer  # Assuming correct_answer is defined ('a', 'b', 'c', or 'd')
                for i, answer in enumerate(answers):
                    answer.setColor("green" if i == index else "black")
                win.flip()
                core.wait(0.5)  # Ensure the color change is visible
                response_received = True
                break

    # Hide the countdown timer after it finishes
    countdown_timer.text = ''
    countdown_timer.draw()
    win.flip()

    # If no response is received within 10 seconds, return "NA"
    if not response_received:
        chosen_ans = "NA"
        is_correct = "NA"
        button_pressed = "NA"

    return question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed

def reset_answers(answers):
    for answer in answers:
        answer.setColor("black")
    question.autoDraw = False
    instr_text.autoDraw = False
    for answer in answers:
        answer.autoDraw = False

# Set up instructions
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()
instr_text = visual.TextStim(win, text="(Bitte benutzen Sie die Tasten 1, 2, 3 und 4, um die richtige Antwort auszuwählen.)", color="grey", pos=(0, -0.3), wrapWidth=2, height=0.018)
event.clearEvents()

# Assuming skip_questions_paced and other variables are defined
if not skip_questions_paced:
    # Setup for Q1
    Q1_text = locals()[curr_text_nr + "_Q1"]
    Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
    Q1_correct = locals()[curr_text_nr + "_Q1_corr"]

    question, answers = setup_question(Q1_text, Q1_answers)
    question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q1_correct)
    print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
    reset_answers(answers)

    # save data:
    thisExp.addData('global_onset_time', question_time)
    thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
    thisExp.addData('question', 'Q1')
    thisExp.addData('button_pressed', button_pressed)
    thisExp.addData('chosen_ans', chosen_ans)
    thisExp.addData('ans_correct', chosen_ans == Q1_correct)
    thisExp.addData('text_nr', curr_text_nr)
    thisExp.addData('block_nr_exp', exp_block_counter+1)
    thisExp.addData('run_nr', '1')
    thisExp.addData('block_nr_run', run1_block_counter+1)
    thisExp.addData('block_name', curr_block)
    thisExp.addData('n-back_level', curr_nback_cond)

    # start a new row in the csv
    thisExp.nextEntry()

    # Setup for Q2
    Q2_text = locals()[curr_text_nr + "_Q2"]
    Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
    Q2_correct = locals()[curr_text_nr + "_Q2_corr"]

    question, answers = setup_question(Q2_text, Q2_answers)
    question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q2_correct)
    print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
    reset_answers(answers)

    # save data:
    thisExp.addData('global_onset_time', question_time)
    thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
    thisExp.addData('question', 'Q2')
    thisExp.addData('button_pressed', button_pressed)
    thisExp.addData('chosen_ans', chosen_ans)
    thisExp.addData('ans_correct', chosen_ans == Q2_correct)
    thisExp.addData('text_nr', curr_text_nr)
    thisExp.addData('block_nr_exp', exp_block_counter+1)
    thisExp.addData('run_nr', "1")
    thisExp.addData('block_nr_run', run1_block_counter+1)
    thisExp.addData('block_name', curr_block)
    thisExp.addData('n-back_level', curr_nback_cond)

    # start a new row in the csv
    thisExp.nextEntry()

    # Setup for Q3
    Q3_text = locals()[curr_text_nr + "_Q3"]
    Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
    Q3_correct = locals()[curr_text_nr + "_Q3_corr"]

    question, answers = setup_question(Q3_text, Q3_answers)
    question_time, onset_time_rel2trigger, chosen_ans, is_correct, button_pressed = display_question_and_get_response(question, answers, Q3_correct)
    print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
    reset_answers(answers)

    # save data:
    thisExp.addData('global_onset_time', question_time)
    thisExp.addData('onset_time_rel2trigger', onset_time_rel2trigger)
    thisExp.addData('question', 'Q3')
    thisExp.addData('button_pressed', button_pressed)
    thisExp.addData('chosen_ans', chosen_ans)
    thisExp.addData('ans_correct', chosen_ans == Q3_correct)
    thisExp.addData('text_nr', curr_text_nr)
    thisExp.addData('block_nr_exp', exp_block_counter+1)
    thisExp.addData('run_nr', "1")
    thisExp.addData('block_nr_run', run1_block_counter+1)
    thisExp.addData('block_name', curr_block)
    thisExp.addData('n-back_level', curr_nback_cond)

    # start a new row in the csv
    thisExp.nextEntry()

    # go to next block!
    exp_block_counter += 1
    run1_block_counter += 1
    print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
    print(f"Going to block {run1_block_counter + 1}/2 in run 1 now!")
    continueRoutine = False

    # If there are still blocks left, go to next one.
    # If not, end loop here:
    if run1_block_counter == 2:
        loop_run1_single_reading.finished = True