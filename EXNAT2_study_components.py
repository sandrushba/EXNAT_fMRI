#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Study Components to use in EXNAT-2

Author: Merle Schuckart (merle.schuckart@uni-luebeck.de)
Version: March 2023

"""

from psychopy import visual, event, core


""" 1) Function to turn background from colour 1 to colour 2 (both defined in HEX) over the course of x seconds """
def change_bg_colour(window, start_rgb, end_rgb, seconds = 2):
    # Convert normal RGB values to 0-1 scale
    start_rgb = [c/255 for c in start_rgb]
    end_rgb = [c/255 for c in end_rgb]

    # Create a rectangle with the same size as the window
    rect = visual.Rect(window, width = window.size[0], height = window.size[1])

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

