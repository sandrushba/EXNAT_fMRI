#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Study Components to use in EXNAT-2

Author: Merle Schuckart (merle.schuckart@uni-luebeck.de)
Version: March 2023

"""

from psychopy import visual, event, core
import numpy as np

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
