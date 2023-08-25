# Analysis of the Timing Test Data for the Flicker Pilot Study

# EXNAT-2 Flicker Pilot
# Author: Merle Schuckart
# Version: 24. August 2023

# Timings were measured using a PsychoPy 2021.2.3 study on a Win7 Laptop ("Martin") with 60 Hz Display 
# (or the Win7 lab Stim PC with 60 Hz monitor from the CBBM lab) and a BBTKv2 timing measurement kit connected 
# to a Dell Laptop with Win10 ("Michelangelo") with the corresponding BBTK software.

# ---------------------------------------------------------

# read in csv with timing data (this is for test 1)
timing_data <-  read.csv("/Users/merleschuckart/Desktop/Flicker Timing Test/Merle_timing_test_blocks_TEST1.csv")
# have a look at the data structure:
head(timing_data)

# get rid of weird first row:
timing_data <- timing_data[-1, ]

# convert comma to dot for decimal
timing_data$Active.mS <- as.numeric(gsub(",", ".", timing_data$Active.mS))  

# Get durations from on-onset to on-onset
pair <- 0
curr_sum <- 0
intervals <- c()
for (row_idx in 1:length(timing_data$Active.mS)){
  #print(row_idx)
  
  # get current duration:
  curr_duration = timing_data[row_idx, ]$Active.mS
  
  # add duration to curr_sum
  curr_sum <- curr_sum + curr_duration
  
  # add 1 to pair counter
  pair <-  pair + 1
  
  # if we summed up enough values, save curr_sum in intervals vector:
  if (pair == 2){
    intervals <- c(intervals, curr_sum)
    # reset curr_sum & pair counter
    curr_sum <- 0 
    pair <- 0
  }
  
}

# convert from ms to s
intervals <- intervals / 1000

# calculate the frequency (1 / average time interval) for flicker
flicker_frequency <- 1 / mean(intervals)

cat("Mean flicker frequency:", flicker_frequency, "Hz")


# Merle talks to herself in R comments:

# Test 1: 12 Hz with a sampling rate of 17.3 Hz on a 60 Hz screen. 
# That's quite low, so if people are not annoyed by that, they probably 
# won't be annoyed by higher frequencies either. 
# Problem: I don't want a flicker in the alpha range. 
# I think we can only show flickers of 60/x where x is an int. So basically 
# with our current display, I can choose between 12, 15, 20 and 30 Hz, 
# which is all not amazing. See:
#60/2
#60/3
#60/4
#60/5

# If I set it to 59Hz though, I could get different frequencies, e.g. this rather nice 19.667 Hz:
# 59/3


# Test 2: Try using the 59 Hz setting on the Stim PC. 
# --> It didn't work, for some reason I get a weird 10 Hz flicker with 500ms breaks in between so that it 
# looks like a fast 10 Hz flicker and a slow 2 Hz flicker combined. 
# I found out that even if I set the monitor to 59 Hz, it's using the 60Hz setting internally. 
# https://support.microsoft.com/en-us/topic/screen-refresh-rate-in-windows-does-not-apply-the-user-selected-settings-on-monitors-tvs-that-report-specific-tv-compatible-timings-0a7a6a38-6c6a-2aec-debc-5183a76b9e1d
# I hate Windows so much. 

# ANYWAY. Test 3: Try 50/3 = 16.66 Hz. It can't possibly also change 50 Hz to 60 Hz internally, right? RIGHT?! 
# After spending a bit of time in windows self help forums because my change to a 50Hz refresh rate is always changed back to 60Hz: 
# Apparently the 50Hz option was also intended for use with TV screens, so same problem as with the 59Hz option I guess?
# (At this point I feel like screaming into a pillow. It's not even the first hardware problem with my windows setup. 
# Will this Windows madness ever end? Probably not. Will I ever finish my PhD? I doubt it.)

# Btw: Is it a problem that sometimes samples are skipped?

# Test 4: I'll try using a 60/4 = 15Hz setting. 
# Pretty? No. Its harmonics are 30, 45, 60 and 75 Hz. But what else can I do?!
1/mean(c(42.25+17.75, 123+17, 42.25+17.5, 123+17, 42.25+17.5, 123+17, 42.25+17.5)/1000) # 10.618 Hz
# This also produces roughly 10 Hz. Wtf is happening. 
# Why is measuring timings always an emotional rollercoaster? 

# Btw I just copied a few samples from the recording stream because I didn't have a USB stick. 
# The whole stream looked like this, so always 123+17 and 42.25+17.5 taking turns. 
# The first value is always the duration of the "on" period.


# Test 5: 60/2 = 30Hz 
# Awful. I hate it. But what frequency will it produce?
# PLOT TWIST, IT ISN'T EVEN DISPLAYED. THE SCREEN IS JUST BLANK.

# F*** this I will go home now. This is not even a Merle-has-no-skills-whatsoever-problem, 
# it's just the shittiest setup you could think of for visual stimulation.

# -------------------------------------------------------------------------------------

# Plot twist: The girl is back in her office, she did not quit her PhD although she thought about it. 


# This is all using the Martin PC:

# I think maybe there are 2 separate problems:
# 1. The non-uniform oscillation. I think sometimes frames are skipped and then there's a "gap" in the oscillation.
# 2. The 60 Hz refresh rate.

# Solution for Problem 1: Even with a 60 Hz refresh rate I should be able to present nice, smoothly oscillating 
# flickers without weird gaps in them. So maybe a part of the problem is how I build the flicker. 
# Currently, I send the stimulus to the screen, do other stuff like checking for responses or sending triggers,
# then I prepare the stimulus for the next phase and present it again. So there's a lot going on 
# between the stimulus updates that might explain the weird frame skipping. 
# I could use multithreading here, but in the PsychoPy forum, Jon said this is really tricky, hard to debug, 
# and most of the time just not a good idea.
# Another problem might be how I time my stimuli. I mostly use core.wait(), which just halts the execution of the script
# completely and can mess with timing for some reason. 

# Non slip timing solution instead of using core.wait():
#https://discourse.psychopy.org/t/non-slip-timing-core-wait-vs-while-loop/9790
            # Python code:
            #clock = core.Clock()
            #for vol in range(1, 10):
            #  # experiment here
            #  while clock.getTime() < vol:
            #   pass

# Also PsychoPy itself might cause timing problems. From the docs: 
# "As of version 1.62 PsychoPy® ‘blocks’ on the vertical blank interval meaning that, 
#  once Window.flip() has been called, no code will be executed until that flip actually takes place."
# https://www.psychopy.org/general/timing/detectingFrameDrops.html
# F*** you, PsychoPy. Why would I want to stop everything when I could use this time to prepare the next stimuli?!

# And then there's the problem with the slow TextStim updating that I already ran into before:
# "calls to the following functions are comparatively slow; they require more CPU time than most 
# other functions and then have to send a large amount of data to the graphics card. 
# Try to use these methods in inter-trial intervals. TextStim.setText() "
# --> did that, so shouldn't cause problems unless it disturbs the flicker


# Solution for Problem 2: Use another screen with a higher refresh rate, 
# e.g. a CRT screen or a gaming screen with a super high frame rate, 
# or (ideally) a GSYNC-compatible graphics card and gaming monitor by NVIDIA + a DisplayPort cable.
# --> https://link.springer.com/article/10.3758/s13428-017-1003-6
# --> expensive, ordering it is time-consuming, only necessary for visual 
# stimulation studies where super accurate timing is crucial.


# Test 6: try  to delete some of the win.flip() lines where they might not be necessary, delete all print() calls in the loop
# and measure actual frame rate instead of just assuming it's exactly 60 Hz.
1/mean(c(60.5+6.25, 60.5+6.25, 60.5+6.25, 60.5+6.25, 60.5+6.25, 60.5+6.25)/1000) # 14.9812 is looking good - I set the frequency to 15 Hz! Also there are no gaps anymore!
# The on-phases are longer than the off-phases. 
# Is this intended? I don't remember the duty cycle, I thought I set it to 50:50.
# test 60/3 HZ = 20 Hz now:
1/mean(c(33.25+16.75, 33.25+16.75, 33.25+16.75, 33.25+16.75, 33+17, 33+17, 33+17, 33.25+16.75, 33.25+16.75)/1000) # perfect 20 Hz. In the 1.5min recording have about 2 or 3 gaps (5016 ms), but I assume that was because the camera moved a bit or so.

# Test 7: test the flicker of the text stims:
1/mean(c(35+15, 35+15, 35+15, 35+15, 35+15, 35+15, 35+15, 35+15, 35+15, 35+15, 35+15, 35+15, 35+15)/1000) # also 20 Hz. In the 1.5min recording have about 2 or 3 gaps (5016 ms), but I assume that was because the camera moved a bit or so.
# Problem: This is just a part of the sample. We have way more gaps in the signal (80 ms or 153 ms) where frames were skipped than in the perfect rectangle conditions. 
# I guess that's because here we update & send 2 stimuli instead of 1 and Text Stims are more difficult to generate than rectangles.

# Test 8: also try 15 Hz again
1/mean(c(49.5+17.25, 49.5+17.25, 49.5+17.25, 49.5+17.25, 49.5+17.25, 49.5+17.25, 49.5+17.25, 49.5+17.25, 49.5+17.25)/1000) # 14.98 Hz. I don't see any gaps in the signal.

# Conclusion: remove unneccessary win.flip()s and remove all print() calls in the loop, use "slower" 
# frequency where we have more time in between screen refreshes to send triggers & do other stuff.
# And maybe invest in a nicer screen & graphics card one day. :-)

# -------------------------------------------------------------------------------------

# Test 9: Test everything with activated triggers & connected devices on the lab PC




