# Analysis of the Timing Test Data for the Flicker Pilot Study

# EXNAT-2 Flicker Pilot
# Author: Merle Schuckart
# Version: 24. August 2023
# Win7 PC with 60 Hz Display
# Timings were measured using a BBTKv2 and the "Michelangelo" Dell Laptop with Win10.

# ---------------------------------------------------------

# read in csv with timing data
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


# Test 2: It didn't work, for some reason I get a weird 10 Hz flicker with 500ms breaks in between so that it 
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
intervals = c(42.25+17.75, 123+17, 42.25+17.5, 123+17, 42.25+17.5, 123+17, 42.25+17.5)/1000
# This also produces roughly 10 Hz. Wtf is happening. 
# Why is measuring timings always an emotional rollercoaster? 

# Test 5: 60/2 = 30Hz 
# Awful. I hate it. But what frequency will it produce?
# PLOT TWIST, IT ISN'T EVEN DISPLAYED. THE SCREEN IS JUST BLANK.

# F*** this I will go home now. This is not even a Merle-has-no-skills-whatsoever-problem, 
# it's just the shittiest setup you could think of for visual stimulation.
# The only solution I can think of would be using 2 slower flickers, 
# but does that make sense??? Would it work? I doubt it.

# Conclusion: No thank you, I can't use SSVEPs in my EEG study.

