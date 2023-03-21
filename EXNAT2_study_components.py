#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Study Components to use in EXNAT-2

Author: Merle Schuckart (merle.schuckart@uni-luebeck.de)
Version: March 2023

"""

from psychopy import visual, event, core


""" 1) Function for showing 3 MC questions (each with 4 answer options) on screen """

# The participant can select the correct answers using their mouse
# and they can confirm their selection by pressing the space bar on their keyboard.
# The selected answer option is shown in green and a selection can be changed 
# if the participant selected the wrong option by accident.

def multiple_choice(window, questions, answer_options, ans_correct):
    print("start preparing MC questions")
    # create TextStims for each question & its answer options:
    q_stims = []
    a_stims = []
    # do the following for each of the 3 questions:
    for i in range(3):
        print("start preparing Q" + str(i))
        # create a TextStim for the current question
        q_stim = visual.TextStim(win, text = questions[i], pos = (0, 6))
        q_stims.append(q_stim)
        
        # do the same for the answer options:
        print("start preparing answer options for Q" + str(i))
        a_stim1 = visual.TextStim(win, text = "1) " + answer_options[i][0], pos = (-6, 2))
        a_stim2 = visual.TextStim(win, text = "2) " + answer_options[i][1], pos = (-6, 1))
        a_stim3 = visual.TextStim(win, text = "3) " + answer_options[i][2], pos = (-6, 0))
        a_stim4 = visual.TextStim(win, text = "4) " + answer_options[i][3], pos = (-6, -1))
        a_stims.append([a_stim1, a_stim2, a_stim3, a_stim4])
    
    # create another TextStim for the instruction
    # I want to tell my participants that they can confirm their selection by pressing Space
    print("prepare instruction")
    instr_stim = visual.TextStim(window, 
                                 text = "Bitte drücken Sie die Leertaste um fortzufahren", 
                                 pos = (-10, 10))

    # Track participant's answers - so far they haven't 
    # selected anything so start with some default values
    selected_answers = [-1, -1, -1]
    answer_colors = ['black','black','black']
    
    # small helper function: change answer font colour if it's selected
    def update_answer_colors(q_num):
        print("change answer if it's selected")
        for i in range(4):
            if i == selected_answers[q_num]:
                print("answer selected, show it in green")
                a_stims[q_num][i].color = (0.44, 0.54, 0.37) # Dark sage green
            else:
                a_stims[q_num][i].color = answer_colors[q_num]
    
    # small helper function: check participant's answers and display feedback
    def check_answers():
        print("check participant's answers")
        feedback_stims = []
        for i in range(3):
            # If no answer is selected, show text "please answer all questions"
            if selected_answers[i] == -1:
                print("no ans given")
                feedback_stim = visual.TextStim(win, 
                                                text = "Bitte beantworten Sie alle Fragen.", 
                                                pos = (0, -6))
                feedback_stims.append(feedback_stim)
                continue
            # if answer was correct, show "correct!"
            if ans_correct[i][selected_answers[i]]:
                print("correct ans")
                feedback_stim = visual.TextStim(win, 
                                                text = "Richtig!", 
                                                pos = (0, -6))
            # if answer was not correct, show "wrong answer"
            else:
                print("wrong ans")
                feedback_stim = visual.TextStim(win, 
                                                text = "Falsch.", 
                                                pos = (0, -6))
            feedback_stims.append(feedback_stim)
            
        # loop feedback stimuli and draw on screen
        for stim in feedback_stims:
            print("draw feedback")
            stim.draw()

        window.flip()
        # Check if participant pressed "Space"
        event.waitKeys(keyList=['space'])
    
    # main loop for displaying questions
    for i in range(3):
        # Draw question and answer option stims
        q_stims[i].draw()
        for stim in a_stims[i]:
            print("draw questions + answers on screen")
            stim.draw()
        instr_stim.draw()
        print("show questions + answers on screen")
        window.flip()
        
        # Handle participant's response
        print("wait for responses")
        keys = event.waitKeys(keyList = ['1','2','3','4','space'], 
                              clearEvents = True)
                              
        # do this until you find a response
        while True:
            # if participant selected option 1, save as "a"
            if '1' in keys:
                print("selected option a")
                selected_answers[i] = "a"
                break
            # if participant selected option 2, save as "d"
            elif '2' in keys:
                print("selected option b")
                selected_answers[i] = "b"
                break
            # if participant selected option 3, save as "c"
            elif '3' in keys:
                selected_answers[i] = "c"
                print("selected option c")
                break
            # if participant selected option 4, save as "d"
            elif '4' in keys:
                print("selected option d")
                selected_answers[i] = "d"
                break
            # if participant pressed space, check whether 
            # their answers are valid / correct
            elif 'space' in keys:
                print("submitted answers - checking answers now")
                check_answers()
                break

# Define the questions and answer options
#questions = ["What is the name of the orphanage where Reynie lived before being recruited to the Secret Benedict Society?", 
#             "What is the name of the founder of the society?", 
#             "What is the name of the test the children had to pass in order to join the society?"]
#answer_options = [["St. Michael's Orphanage", "St. Joseph's Orphanage", "St. John's Orphanage", "St. Jude's Orphanage"], 
#                  ["Nicholas Benedict", "William Benedict", "Thomas Benedict", "Edward Benedict"], 
#                  ["The Test of Intelligence", "The Test of Knowledge", "The Test of Perseverance", "The Test of Resourcefulness"]]
#ans_correct = [[True, False, False, False], 
#               [True, False, False, False], 
#               [False, False, False, True]]


# Present the questions and record the participant's answers
#selected_answers = multiple_choice(win, questions, answer_options, ans_correct)

# Print the participant's answers
#print("Participant's answers:", selected_answers)



""" 2) Function to turn background from colour 1 to colour 2 (both defined in HEX) over the course of x seconds """
def change_bg_colour(window, start_rgb, end_rgb, seconds=2):
    # Convert normal RGB values to 0-1 scale
    start_rgb = [c/255 for c in start_rgb]
    end_rgb = [c/255 for c in end_rgb]
    
    # Create a rectangle with the same size as the window
    rect = visual.Rect(window, width=window.size[0], height=window.size[1])
    
    # Gradually change the background colour over "seconds" seconds
    num_steps = seconds * 60
    for i in range(num_steps):
        # Calculate the current RGB values
        curr_r = start_rgb[0] + (i/num_steps) * (end_rgb[0] - start_rgb[0])
        curr_g = start_rgb[1] + (i/num_steps) * (end_rgb[1] - start_rgb[1])
        curr_b = start_rgb[2] + (i/num_steps) * (end_rgb[2] - start_rgb[2])
        
        # Set the rectangle fill color to the current color
        rect.setFillColor([curr_r, curr_g, curr_b])
        
        # Draw the rectangle on the window
        rect.draw()
        
        # Flip the window to update the display
        window.flip()
        
        # Wait for a few ms before updating the background colour again
        core.wait(1/60)
    
    # Set end color as final bg colour
    window.color = end_rgb
    
    # Add an extra delay to ensure the final bg colour is fully set
    core.wait(0.5)