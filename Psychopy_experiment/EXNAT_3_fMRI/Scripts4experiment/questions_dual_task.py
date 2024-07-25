##########################################################
#              Text Comprehension Questions              #
##########################################################

def setup_question(question_text, answers_text):
    question = visual.TextStim(win, text=question_text, pos=(0, 0.2), color="black", height=0.025, anchorHoriz='center', alignText='center', wrapWidth=1)
    answers = [visual.TextStim(win, text=ans, pos=(-0.75, 0.1 - i * 0.05), color="black", height=0.025, wrapWidth=1.5, anchorHoriz='left', alignText='center') for i, ans in enumerate(answers_text)]
    return question, answers

def display_question(question, answers):
    question.autoDraw = True
    for answer in answers:
        answer.autoDraw = True
    instr_text.autoDraw = True
    win.flip()

def get_response(answers, correct_answer):
    while True:
        keys = defaultKeyboard.getKeys(['1', '2', '3', '4'])
        if keys:
            key_name = keys[0].name  # Get the name of the first key pressed

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
                break
    return chosen_ans, is_correct

def reset_answers(answers):
    for answer in answers:
        answer.setColor("black")
    question.autoDraw = False
    instr_text.autoDraw = False
    for answer in answers:
        answer.autoDraw = False

# Example usage:
win.setColor(light_bg_col, colorSpace='rgb')
win.flip()
instr_text = visual.TextStim(win, text="(Bitte benutzen Sie die Tasten 1, 2, 3 und 4, um die richtige Antwort auszuwählen.)", color="grey", pos=(0, -0.3), wrapWidth=2, height=0.018)
event.clearEvents()

# Assuming skip_questions_paced and other variables are defined
if not skip_questions_paced:
    # this is run 3:
    if 6 <= exp_block_counter <= 7:
        # Setup for Q1
        Q1_text = locals()[curr_text_nr + "_Q1"]
        Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
        Q1_correct = locals()[curr_text_nr + "_Q1_corr"]

        question, answers = setup_question(Q1_text, Q1_answers)
        display_question(question, answers)
        chosen_ans, is_correct = get_response(answers, Q1_correct)
        print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)

        # save data:
        thisExp.addData('question', 'Q1')
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q1_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter)
        thisExp.addData('run_nr', 'run3')
        thisExp.addData('block_nr_run', run3_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)

        # start a new row in the csv
        thisExp.nextEntry()

        # Setup for Q2
        Q2_text = locals()[curr_text_nr + "_Q2"]
        Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
        Q2_correct = locals()[curr_text_nr + "_Q2_corr"]

        question, answers = setup_question(Q2_text, Q2_answers)
        display_question(question, answers)
        chosen_ans, is_correct = get_response(answers, Q2_correct)
        print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)

        # save data:
        thisExp.addData('question', 'Q2')
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q2_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter)
        thisExp.addData('run_nr', 'run3')
        thisExp.addData('block_nr_run', run3_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)

        # start a new row in the csv
        thisExp.nextEntry()

        # Setup for Q3
        Q3_text = locals()[curr_text_nr + "_Q3"]
        Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
        Q3_correct = locals()[curr_text_nr + "_Q3_corr"]

        question, answers = setup_question(Q3_text, Q3_answers)
        display_question(question, answers)
        chosen_ans, is_correct = get_response(answers, Q3_correct)
        print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)

        # save data:
        thisExp.addData('question', 'Q3')
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q3_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter)
        thisExp.addData('run_nr', 'run3')
        thisExp.addData('block_nr_run', run3_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)

        # start a new row in the csv
        thisExp.nextEntry()

        exp_block_counter += 1
        run3_block_counter += 1
        print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
        continueRoutine = False

        # If there are still blocks left, go to next one.
        # If not, end loop here:
        if run3_block_counter == 2:
            print(f"Finished block {run3_block_counter}/2 in run 3, moving on to next run!")
            # loop_dual_task_blocks.finished = True

    # this is run 4:
    elif 8 <= exp_block_counter <= 9:

        # Setup for Q1
        Q1_text = locals()[curr_text_nr + "_Q1"]
        Q1_answers = locals()[curr_text_nr + "_Q1_ans"]
        Q1_correct = locals()[curr_text_nr + "_Q1_corr"]

        question, answers = setup_question(Q1_text, Q1_answers)
        display_question(question, answers)
        chosen_ans, is_correct = get_response(answers, Q1_correct)
        print(f"Chosen answer for Q1: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)

        # save data:
        thisExp.addData('question', 'Q1')
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q1_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter)
        thisExp.addData('run_nr', 'run3')
        thisExp.addData('block_nr_run', run4_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)

        # start a new row in the csv
        thisExp.nextEntry()

        # Setup for Q2
        Q2_text = locals()[curr_text_nr + "_Q2"]
        Q2_answers = locals()[curr_text_nr + "_Q2_ans"]
        Q2_correct = locals()[curr_text_nr + "_Q2_corr"]

        question, answers = setup_question(Q2_text, Q2_answers)
        display_question(question, answers)
        chosen_ans, is_correct = get_response(answers, Q2_correct)
        print(f"Chosen answer for Q2: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)

        # save data:
        thisExp.addData('question', 'Q2')
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q2_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter)
        thisExp.addData('run_nr', 'run3')
        thisExp.addData('block_nr_run', run4_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)

        # start a new row in the csv
        thisExp.nextEntry()

        # Setup for Q3
        Q3_text = locals()[curr_text_nr + "_Q3"]
        Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
        Q3_correct = locals()[curr_text_nr + "_Q3_corr"]

        question, answers = setup_question(Q3_text, Q3_answers)
        display_question(question, answers)
        chosen_ans, is_correct = get_response(answers, Q3_correct)
        print(f"Chosen answer for Q3: {chosen_ans}, Correct: {is_correct}")
        reset_answers(answers)

        # save data:
        thisExp.addData('question', 'Q3')
        thisExp.addData('chosen_ans', chosen_ans)
        thisExp.addData('ans_correct', chosen_ans == Q3_correct)
        thisExp.addData('text_nr', curr_text_nr)
        thisExp.addData('block_nr_exp', exp_block_counter)
        thisExp.addData('run_nr', 'run3')
        thisExp.addData('block_nr_run', run4_block_counter)
        thisExp.addData('block_name', curr_block)
        thisExp.addData('n-back_level', curr_nback_cond)

        # start a new row in the csv
        thisExp.nextEntry()

        # add 1 to the block counter to go load the next block
        exp_block_counter += 1
        run4_block_counter += 1
        print(f"Going to block {exp_block_counter + 1}/10 in the experiment now!")
        continueRoutine = False

        # If there are still blocks left, go to next one.
        # If not, end loop here:
        if run4_block_counter == 2:
            print(f"Finished block {run4_block_counter}/2 in run 4, moving on to next run!")
            loop_dual_task_blocks.finished = True