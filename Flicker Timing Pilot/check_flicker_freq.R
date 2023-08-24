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
# Okay so 12 Hz for test 1. That's quite low, so if people are not annoyed by that, 
# they probably won't be annoyed by higher frequencies either. Lets try if we can 
# I think we can only show flickers of 60/x where x is an int. 
# So basically with our current display, I can choose between 12, 15, 20 and 30 Hz which is all not amazing:
#60/2
#60/3
#60/4
#60/5

# If I set it to 59Hz though, I could get different frequencies, 
# e.g. this rather nice 19.667 Hz:
# 59/3

# Is it a problem that sometimes samples are skipped though?


