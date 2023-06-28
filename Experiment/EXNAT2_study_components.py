#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Study Components to use in EXNAT-2

Author: Merle Schuckart (merle.schuckart@uni-luebeck.de)
Version: March 2023

"""

from psychopy import visual, event, core
import numpy as np
# make sure to pip install hmmlearn first:
from hmmlearn import hmm

""" 1) Function to turn background from colour 1 to colour 2 (both defined in RGB -1:1 as list) over the course of x seconds """
def change_bg_colour(window, start_rgb, end_rgb, seconds = 2):

    # create a rectangle with the same size as the window
    rect = visual.Rect(window, width = window.size[0], height = window.size[1])

    # gradually change the background colour over x seconds
    num_steps = seconds * 60
    for i in range(num_steps):
        # calculate the current RGB values
        curr_r = start_rgb[0] + (i/num_steps) * (end_rgb[0] - start_rgb[0])
        curr_g = start_rgb[1] + (i/num_steps) * (end_rgb[1] - start_rgb[1])
        curr_b = start_rgb[2] + (i/num_steps) * (end_rgb[2] - start_rgb[2])

        # set the rectangle fill color to the current color
        rect.setFillColor([curr_r, curr_g, curr_b])

        # draw the rectangle on screen
        rect.draw()
        window.flip()

        # wait for a few ms
        core.wait(1/60)

    # set end color
    window.setColor(end_rgb, colorSpace = 'rgb')
    window.flip()

    # wait a few ms to ensure the final bg colour is fully set
    core.wait(0.5)
    print("finished changing bg")



""" Function to generate sequence of 1500 tones with
    certain transition probabilities """
def generate_trial_sequence(entropy_level):

    # check how many tones we have - this determines
    # how big our matrices with the transition probabilities
    # need to be:
    n_features = len(tones)

    # create emission matrix: We want to emit
    # the given state with 100% probability
    # (feels a bit odd to explicitly specify that,
    # but we need it for the HMM function later)
    emission_matrix = np.eye(n_features)
    #print(emission_matrix)


    if entropy_level == "ordered":
        # create a matrix with transition probabilities
        # for the ordered condition:
        transition_matrix = [[0.25, 0.75, 0., 0.],
                             [0., 0.25, 0.75, 0.],
                             [0., 0., 0.25, 0.75],
                             [0.75, 0., 0., 0.25]]
        #print("ordered transition probabilities matrix:", transition_matrix)

    elif entropy_level == "random":
        # create a matrix with transition probabilities
        # for the random condition:
        transition_matrix = [[0.25, 0.25, 0.25, 0.25],
                             [0.25, 0.25, 0.25, 0.25],
                             [0.25, 0.25, 0.25, 0.25],
                             [0.25, 0.25, 0.25, 0.25]]
        #print("random transition probabilities matrix:", transition_matrix)




    # Create an HMM model
    model = hmm.MultinomialHMM(n_components = n_features,
                               n_trials = 1,
                               verbose = False)

    model.startprob_ = np.ones(n_features) / n_features  # Set equal initial probabilities
    model.transmat_ = transition_matrix
    model.emissionprob_ = emission_matrix

    # Generate a sequence of pure tones
    sequence, _ = model.sample(n_samples = 1500, random_state = None)

    pure_tones_sequence = []

    for sublist in sequence:
      #print(sublist)
      index = np.where(sublist != 0)[0][0]  # Get the index of the non-zero element
      #print(index)
      pure_tone = tones[index]  # Retrieve the corresponding pure tone
      pure_tones_sequence.append(pure_tone)

    #print(sequence)

    # TO DO: 
    # The transition probabilities don't match exactly the probabilities I specified in my transition matrix.
    # Idea: Polish it a bit manually, so I get exactly 0%, 25% and 75% transition probabilities in the 
    # output? Or is this not a problem?

    return(pure_tones_sequence)

# Generate the trial sequences for both entropy conditions
#ordered_sequence = generate_trial_sequence("ordered")
#random_sequence = generate_trial_sequence("random")
#print(ordered_sequence)


