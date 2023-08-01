# Analysis for EXNAT-2 Flicker Pilot (Behavioural Lab Study)

# Author: Merle Schuckart (merle.schuckart@gmx.de)
# Version: July 2023

################################################################################

### -------- What does this script do? --------
# I built an EEG experiment version of the EXNAT-1 study in Psychopy. 
# In the EEG study, I want to flicker the words at a frequency of 17.3 Hz. 
# I'm using a Windows 7 PC with a sampling freq of 60 Hz.

# In the pilot study, I made the participants read 6 texts, 2 BL, 2 with a 1-back 
# and 2 with a 2-back task, and I flickered stimuli in 3 of the blocks.
# What I want to know now is whether the flicker makes people substantially slower 
# in all of the blocks, which would indicate that the task gets more challenging if 
# the words are flickered (we don't really want to increase cognitive load).

# I also included 1 visual task block that's new in the eeg study to see 
# if the task works as intended and if it's okay or too hard to do.


################################################################################

# -------- 0. Settings --------

# Turn off scientific notation
options(scipen = 999)

# Clear environment
remove(list = ls())

# Create a list with needed libraries
pkgs <- c("rstudioapi", # for getting path of this file
          "stringr", # for getting substrings
          "ggplot2", # for plots
          "dplyr", # for replacing multiple values in vector with different values
          "reshape2", # for reshaping df format
          "data.table", # for data tables
          "tidyverse", # for aggregating
          "R.utils", # for deleting all empty csv files in the directory
          "psycho", # for computing d-prime values
          "yarrr", # for plotting
          "devtools", # for getting packages from github
          "lattice", # for quick & dirty density plots
          "gtools", # for getting tuples from list
          "DescTools", # for checking normality of distribution in QQ plot
          "easystats", # also for working with lme4 model output, contains "performance" & "see" I think?
          "see", # for plotting residuals of lme4 model
          "performance", # needed for plotting the lme4 model output summary
          "lme4", # also for linear mixed models, but no p-values in the summary
          #"lmerTest", # extension of lme4 - this also gives you p-values
          "car", # for Anova function & aGSIFs (= basically weird adjusted VIFs)
          "BayesFactor", # that's self-explanatory
          "patchwork", # needed for check_model plotting function
          "glmnet", # for elastic net regression
          "caret", # for choosing the best tuning parameters for elastic net regression
          "beepr", # to play Super Mario sound when script finished running
          "effects", # for plotting lmm interaction & main effects
          "gridExtra") # for showing several plots in a grid

# Load each listed library, check if it's already installed
# and install if necessary
for (pkg in pkgs){
  if(!require(pkg, character.only = TRUE)){
    install.packages(pkg)
    library(pkg, character.only = TRUE)
  }
}

# install package with lists of stop words from github
devtools::install_github("quanteda/stopwords")
library(stopwords)

# everything's loaded, so remove helper variables from environment
rm(pkg, pkgs)


# set working directory:
# get path of this file
current_path = rstudioapi::getActiveDocumentContext()$path
# set it as our wd
setwd(dirname(current_path))
# print it just to make sure it's correct:
print(getwd())


# import get_dprime() function from another script I built
source("get_dprime.R") # get script

# -------- 1. Get data --------

# Set directory to data folder:
path_data_folder <- "../data/" 

# Get list of all .csv files in the data folder
file_list <- list.files(path = path_data_folder, pattern='.csv')

# Placeholders df for demographics, questions & text data
df_demogr           <- data.frame()
df_text_data        <- data.frame()
df_comprehension_Qs <- data.frame()

# Loop files in my file list aka directory
for (i in 1:length(file_list)) {

  # PREPARE FILE FOR PREPROCESSING
  # Read in current file
  subj_df <- read.csv(paste(path_data_folder, file_list[i],sep = ""), sep = ",")

  # get demographical data:
  id         <- unique(subj_df$participant) # individual code
  age        <- unique(subj_df$age) # age in years
  gender     <- unique(subj_df$gender) # gender in passport
  handedness <- unique(subj_df$handedness) # left- or right-handed?
  
  # print message
  message(paste(i, " - Reading in file ", file_list[i], ", participant ID: ", id, sep = ""))
  
  # if it's by the non-German-speaking HiWis, set native_speaker to False:
  if (id == "eg" | id == "at"){
    native_speaker <-  FALSE
  } else { 
    native_speaker <- TRUE
  }
  
  # add column with info on whether participant should be excluded
  excl <- FALSE
  
  # append to demographics df
  df_demogr <- as.data.frame(rbind(df_demogr,
                                   cbind(id, age, gender, handedness, native_speaker)))
  
  # remove helper variables to keep things tidy
  rm (age, gender, handedness, excl)
  
  ###########################
  
  # GET RAW TEXT & N-BACK DATA
  
  # get rid of some unimportant columns:
  subj_df <- subj_df[ , c("flicker_freq", "flicker_on", "colour", "target", "nback_response", 
                          "nback_RT", "duration", "text_nr", "trial_nr", "block_nr", 
                          "block_name", "word", "question", "chosen_ans", "ans_correct",
                           "block_cond", "participant", "age", "handedness", "gender","frameRate")]

  # name column "block_name" "block_kind" and "participant" "ID" so it matches the EXNAT-1 variables
  names(subj_df)[which(names(subj_df) == "block_name")] <- "block_kind"
  names(subj_df)[which(names(subj_df) == "participant")] <- "ID"

  # add native speaker column
  subj_df$native_speaker <- native_speaker
  
  # get rid of reading baseline training (that was just a practice block for the participants)
  subj_df <- subset(subj_df, block_kind != "Reading_Baseline_training")
  
  # save raw df for later
  subj_df_raw <- subj_df
  
  ###########################
  
  ### ADD NUMBERED BLOCK NAMES ####
  
  # We have each main block twice, but I would like to exclude outliers by block and not by condition.
  # Reason: Reading times in second block might be slightly different than in first block, so don't mix them up.
  
  # first, just copy the "old" block names
  subj_df$block_names_numbered <- subj_df$block_kind
  
  # Get all 1-back blocks and call the first 300 trials "1back_dual_main_1". Call the remaining 300 trials "1back_dual_main_1".
  # Do this for Reading BL & 2-back main, too. The single-task blocks don't have to be changed because they're only presented once.
  change_blocknames <- c("Reading_Baseline_main", "1back_dual_main", "2back_dual_main")
  
  for (change_block_name in change_blocknames){
    # get the first 309 rows (each block has 300 trials so the first 300 trials = 1st block + 9 question rows).
    subj_df[which(subj_df$block_names_numbered == change_block_name), ]$block_names_numbered[c(1:309)] <- paste(change_block_name,"_1", sep = "")
    subj_df[which(subj_df$block_names_numbered == change_block_name), ]$block_names_numbered <- paste(change_block_name,"_2", sep = "")
  }

  # Also add block number aka position of the block in the experiment.
  # This way, I can control for tiredness effects.
  
  # loop block_names_numbered aka individual blocks
  block_nr <-  1
  subj_df$block_nr <- NA
  blocks <- c("Reading_Baseline_main_1", "Reading_Baseline_main_2", "1back_dual_main_1", "1back_dual_main_2", "2back_dual_main_1", "2back_dual_main_2")
  for (block in unique(subj_df$block_names_numbered)){
    # if the current block name is one of the main blocks, add block number
    if (block %in% blocks){
      subj_df[which(subj_df$block_names_numbered == block), "block_nr"] <- block_nr
      # go to next block
      block_nr <-  block_nr + 1
    }
  }  
  
  
  ###########################

  ### COMPUTE READING SPEED ####
  
  # append column with log-transformed reading times
  #subj_df$duration_log <- log(subj_df$duration)
  
  # append reading speed column (words / 100 s as in Lea's thesis)
  # reading speed = 100 seconds * 100 ms/s * reading time
  subj_df$reading_speed <- 100 * 1000 / subj_df$duration
  
  ###########################
  
  # GET ADDITIONAL INFORMATION ON THE TEXTS:
  
  ### PUNCTUATION ####
  
  # Edit the texts a bit. Currently, we have words & punctuation
  # mixed up. Would be nice if we had one word column
  # and some others with info on punctuation.
  
  punctuation <- c(rep("", times = length(subj_df$ID)))
  
  # get all .
  punctuation[grep("[.]", subj_df$word)] <- "point"
  # get all ?
  punctuation[grep("[?]", subj_df$word)] <- "question_mark"
  # get all !
  punctuation[grep("[!]", subj_df$word)] <- "exclamation_mark"
  # get all ,
  punctuation[grep("[,]", subj_df$word)] <- "comma"
  # get all ;
  punctuation[grep("[;]", subj_df$word)] <- "semicolon"
  # get all :
  punctuation[grep("[:]", subj_df$word)] <- "colon"
  
  # get all "
  # This is tricky for various reasons:
  
  # 1. there could be quotes directly after or
  # before a point for example
  
  # Idea: Separate column for quotes
  quotes <- c(rep("", times = length(subj_df$ID)))
  
  # 2. I want to differentiate between opening and closing quotes,
  # but they look the same.
  
  # Idea: make them all "opening quotes" and change every second one to
  # "closing_quote". This should do the trick.
  quotes[grep("\"", subj_df$word)] <- "opening_quote"
  opening <- TRUE
  
  # loop list of quotes
  for (x in 1:length(quotes)){
    # get current value in vector "quotes" & current word
    curr_val  <- quotes[x]
    curr_word <- subj_df$word[x]
    
    if (curr_val == "opening_quote" & # if the current value is not empty
        opening == TRUE & # and we set "opening" to TRUE
        grepl("\"[A-Za-z0-9]+\"", curr_word) == FALSE){ # and there are not 2 quotes around the word
      
      # leave it as is, next quote is the closing one
      opening <- FALSE
      
      # if we have a quote, but it has to be a closing one, change it accordingly
    } else if (curr_val == "opening_quote" &
               opening == FALSE &
               grepl("\"[A-Za-z0-9]+\"", curr_word) == FALSE){
      # change value to closing quote
      quotes[x] <- "closing_quote"
      # next quote is the opening one
      opening <- TRUE
      # if it's a quote around a single word, mark as "both"
    } else if (curr_val == "opening_quote" &
               grepl("\"[A-Za-z0-9]+\"", curr_word) == TRUE){
      # change value to both
      quotes[x] <- "both"
    }
  }
  
  # remove all punctuation
  word_single <- gsub('[[:punct:] ]+',' ', subj_df$word)
  # "trim" away spaces before and after words
  word_single <- trimws(word_single, which = c("left"))
  word_single <- trimws(word_single, which = c("right"))
  # put dashes into spaces between words (words like "ice-cream" for example)
  word_single <- gsub(" ", "-", word_single, fixed = TRUE)
  
  # get word length for single words
  word_length_single <- nchar(word_single)
  
  
  ### N-BACK RESPONSES ####
  
  # check if we had an n-back reaction while the word was shown
  # create vector with only FALSEs
  reaction <- c(rep(FALSE, times = length(subj_df$ID)))
  # check where in subj_df we have responses (hit or false alarm) and change value in reaction vector to TRUE at that index
  reaction[which(subj_df$nback_response == "hit" | subj_df$nback_response == "false alarm")] <- TRUE
  
  # do the same for the subj_df_raw dataframe, because we'll need it later
  subj_df_raw$reaction <- FALSE
  # get idx of all rows where n-back response was recorded, mark those as TRUE in the reaction column.
  subj_df_raw[which(subj_df_raw$nback_response == "hit" | subj_df_raw$nback_response == "false alarm"), "reaction"] <- TRUE
  
  # Then get idx of all rows containing n-back responses again, but this time only of
  # slides where sender == word. We're only looking for the dual-task blocks.
  # Subtract 1 from each idx in this list to get all the slides before. Those should be the "fix_word" slides.
  # Mark the reaction in those slides as TRUE, too. We need them later.
  subj_df_raw[which((subj_df_raw$nback_response == "hit" | subj_df_raw$nback_response == "false alarm") & subj_df_raw$sender == "word") - 1, "reaction"] <- TRUE
  
  
  # APPEND NEW COLUMNS
  # append punctuation and quotes column, column with words without punctuation
  # column with length of each the single words and reaction column as
  # additional columns to subj_df:
  subj_df <- data.frame(cbind(subj_df, word_single, punctuation,
                              quotes, word_length_single, reaction))
  
  
  
  ### STOP WORDS, PUNCTUATION, REACTION AND DURATION OF PREVIOUS WORD ####
  
  # Now also get previous punctuation, previous quotes, previous
  # word and previous duration because why not.
  # First, append empty columns to df:
  subj_df[, c("previous_word", "previous_punctuation", "previous_quotes", "previous_duration", "previous_reaction", "stop_word")] <- ""
  
  # get list of German stop_words
  stop_words <- stopwords("de", source = "snowball")
  # snowball = stopwords list based on the Snowball stemmer's word lists.
  # --> https://snowballstem.org/texts/introduction.html
  
  # now loop rows and gradually fill in the empty columns.
  for (idx in 1:length(subj_df$ID)){
    # if it's the first trial of a new block, go to next iteration
    # because in this case we don't have previous data.
    # Also skip the following part if it's a block without text.
    if (subj_df$trial_nr[idx] > 1 && subj_df$word[idx] != ""){
      # fill in the missing data by getting the values from the previous trial:
      subj_df$previous_word[idx]        <- subj_df$word_single[idx-1]
      subj_df$previous_punctuation[idx] <- subj_df$punctuation[idx-1]
      subj_df$previous_quotes[idx]      <- subj_df$quotes[idx-1]
      subj_df$previous_duration[idx]    <- subj_df$duration[idx-1]
      subj_df$previous_reaction[idx]    <- subj_df$reaction[idx-1]
    }
    
    # check if current word is a stop word or not
    if (subj_df$word[idx] != "" && subj_df$word_single[idx] %in% stop_words){
      subj_df$stop_word[idx] <- TRUE
    } else {
      subj_df$stop_word[idx] <- FALSE
    }
  }
  
  
  
  # Fix messed up block numbers:
  # Loop rows, if task_name changes, add 1 to block counter.
  block_counter <- 1
  subj_df$block_nr <- ""
  # loop rows, but skip the first one
  for (row_idx in 2:length(subj_df$ID)){
    curr_row <- subj_df[row_idx, ]
    # if it's the same text_nr as in the row before, 
    # assign block counter as in the row before. Only do this for the main blocks though, I don't care about the rest for now:
    if (curr_row$text_nr == subj_df[row_idx-1, ]$text_nr & curr_row$block_kind %in% c("visual_task", "Reading_Baseline_main", "1back_dual_main", "2back_dual_main")){
      subj_df[row_idx, ]$block_nr <- block_counter 
    } else if (curr_row$text_nr != subj_df[row_idx-1, ]$text_nr & curr_row$block_kind %in% c("visual_task", "Reading_Baseline_main", "1back_dual_main", "2back_dual_main")){
      block_counter <- block_counter + 1
      subj_df[row_idx, ]$block_nr <- block_counter 
    }
  }
  # The block numbers are still a bit odd but who cares.
  
  
  ### WORD FREQUENCIES & SURPRISAL SCORES ####
  
  # Include word frequencies & surprisal scores for each word
  
  # append "empty" word frequency & surprisal score columns to df
  # to do so, create a vector of column names
  col_names <- c("word_frequency", paste0("surprisal_", c(1, 4, 12, 60)))#,
  # then add "empty" columns to data frame subj_df
  subj_df[, col_names] <- 0
  
  # get word frequency & surprisal scores for each word
  # load word freq df
  word_freqs_df = read.csv("./word frequencies/Word_freqs.csv", sep = ";", header=TRUE)[2:4]

  # load surprisal scores / similarity scores df with TS = context chunk size
  surprisal_df = read.csv("./surprisal scores/surprisal_scores_masked_context.csv", sep = ",", header = TRUE)
  
  # loop individual texts
  for (curr_text_nr in unique(subj_df$text_nr)){
    
    # in some blocks we don't have texts, so skip those
    # skip BL training as well
    if (curr_text_nr != "" & !is.na(curr_text_nr) & curr_text_nr != "reading_bl_training_text" & curr_text_nr != "None"){

      
      print(curr_text_nr) # uncomment this if you'd like to show the texts each participant read
      
      # get word frequencies for current text nr
      curr_word_freqs <- subset(word_freqs_df, text_nr == curr_text_nr)$word_frequency
      
      # get surprisal scores:
      curr_surprisals <- subset(surprisal_df, text_nr == curr_text_nr)
      
      # find out where in the subj_df text the text is located and add the word frequencies there. 
      # Take only the first 300 rows because the rest are the questions' rows.
      # If the text occurs twice in the df, that's because it was shown again in the visual task block, so 
      # add the word frequencies twice there.
      if (length(subj_df[which(subj_df$text_nr == curr_text_nr),]$word) > 400){
        print("block was repeated for vis task")
        # loop block numbers and assign word frequencies to the words in both blocks
        curr_block_nrs = as.vector(na.exclude(unique(subset(subj_df, text_nr == curr_text_nr)$block_nr)))
        for (block_nr in curr_block_nrs){
          # add word frequencies:
          subj_df[which(subj_df$text_nr == curr_text_nr & subj_df$block_nr == block_nr),]$word_frequency[0:300] <- curr_word_freqs
          # add surprisal scores:
          curr_row <- which(subj_df$text_nr == curr_text_nr & subj_df$block_nr == block_nr & subj_df$word != "")
          subj_df[curr_row, c("surprisal_1", "surprisal_4",
                              "surprisal_12", "surprisal_60")]  <- curr_surprisals[c("surprisal_1", "surprisal_4",
                                                                                     "surprisal_12",  "surprisal_60")]
        }
      # if the block was only shown once:
      } else {
        print("block was only shown once")
        # assign word frequencies only once
        subj_df[which(subj_df$text_nr == curr_text_nr),]$word_frequency[0:300] <- curr_word_freqs
        # add surprisal scores:
        curr_row <- which(subj_df$text_nr == curr_text_nr & subj_df$word != "")
        subj_df[curr_row, c("surprisal_1", "surprisal_4",
                            "surprisal_12", "surprisal_60")]  <- curr_surprisals[c("surprisal_1", "surprisal_4",
                                                                                   "surprisal_12",  "surprisal_60")]
      }
      print("---------------------")
    }
  
    
  }# END loop texts 

  
  ### GET SURPRISAL SCORES OF PREVIOUS WORD ####
  # --> skipped this part from the EXNAT-1 analysis
  
  
  ###########################
  # GET PERFORMANCE MEASURES:
  
  ### COMPREHENSION QUESTION PERFORMANCE ####
  # Check the performance in the reading comprehension questions in the 2 baseline blocks:
  # If they don't have 3/3 in at least one of the blocks, exclude their data.
  
  # We now get all question data:
  Q_df <- subset(subj_df, chosen_ans != "")[,c("question", "chosen_ans", "ans_correct", "text_nr", "block_kind", "ID", "block_names_numbered")]
  
  # Just look at the MC questions:
  # For now I don't really care about the answer, I only want to know if they chose the correct one or not.

  # typecast everything to logical
  Q_df$ans_correct <- as.logical(Q_df$ans_correct)
  
  # get performance in Qs
  Q_df$nr_correct <- c(rep(NA, times = length(Q_df$ID)))
  
  # for each block, count how many questions were answered correctly.
  for (curr_block in unique(Q_df$block_names_numbered)){
    curr_Q_df <- subset(Q_df, block_names_numbered == curr_block)
    # count how many questions were answered correctly in the current block
    nr_correct <- length(subset(curr_Q_df, ans_correct == TRUE)$ans_correct)
    # append to Q_df & subj_df$Q_nr_correct
    Q_df[which(Q_df$block_names_numbered == curr_block), ]$nr_correct <- nr_correct
  }
  
  # append Q_df to bigger df for all participants
  df_comprehension_Qs <- as.data.frame(rbind(df_comprehension_Qs, Q_df))


  ### N-BACK PERFORMANCE ####

  # check n-back performance in each block:
  # --> important: don't check by condition, but by block here!
  nback_block_names = c("1back_single_training1", "1back_single_training2", "1back_single_main", "1back_dual_main_1","1back_dual_main_2",
                        "2back_single_training1", "2back_single_training2", "2back_single_main", "2back_dual_main_1", "2back_dual_main_2")
  
  # append empty d-prime column to df:
  subj_df$dprime <- c(rep(NA, times = length(subj_df$word)))
  
  # loop block names:
  for (block_name in nback_block_names){

    # check if block name exists in df:
    if (length(which(unique(subj_df$block_names_numbered) == block_name)) > 0){
      # if so, compute d-primes:
      
      # get data for current block
      curr_block <- subset(subj_df, block_names_numbered == block_name)
      
      # remove trials where the RT was way too fast
      # (= participant reacted by accident)
      curr_block <- subset(curr_block, (nback_RT >= 100 | is.na(nback_RT)))
      
      # if there are still some trials left, compute d-prime
      if (length(curr_block$ID) > 10){
        
        # the main blocks are played twice in the experiment, so separate them
        if (length(curr_block$ID) > 400){
          # get first half, compute d-prime & add to bigger df
          d_prime <- get_dprime(curr_block[c(1:300),]$nback_response)
          subj_df[which(subj_df$block_names_numbered == block_name)[c(1:300)],]$dprime <- d_prime
          
          # same procedure for the second half
          d_prime <- get_dprime(curr_block[c(301:600),]$nback_response)
          subj_df[which(subj_df$block_names_numbered == block_name)[c(310:618)],]$dprime <- d_prime
          
          # if there's only one block:
        } else if (length(curr_block$ID) <= 310){
          # do it only once
          d_prime <- get_dprime(curr_block$nback_response)
          subj_df[which(subj_df$block_names_numbered == block_name),]$dprime <- d_prime
        } # END if loop - check if block exists twice
      } # END if loop - check if there are still enough trials left
    } # END if loop - check for block name in df
  }# END loop - compute d-primes
  
  ###########################
  
  # get rid of all rows where flicker_freq is NA
  # (they shouldn't be there actually, there's some kind of weird error in my script I guess)
  subj_df <- subset(subj_df, !is.na(flicker_freq))
  
  ###########################
  
  ### MARK PARTICIPANTS / TRIALS FOR EXCLUSION:
  
  # append "empty" exclude trial / exclude participant columns to df
  subj_df$excl_trial       <- FALSE
  subj_df$excl_participant <- FALSE
  
  
  ### EXCLUDE PARTICIPANTS ####
  # Skipped this because I was sitting right next to them and everything worked as intended.
  
  
  # append subj_df chunk to df_text_data where we collect the data of all participants
  df_text_data <- as.data.frame(rbind(df_text_data, subj_df))
  message("------------------------")
          
}# END LOOP PARTICIPANTS

# clean up!
rm(list=ls()[! ls() %in% c("df_text_data", "df_demogr", "df_comprehension_Qs", "word_freqs_df", "surprisal_df", "blocks")])

# save preprocessed data for further analysis:
#write.csv(df_text_data,       file = "/Users/merleschuckart/Desktop/EXNAT1 data/preproc_data/preproc_data.csv")
#write.csv(df_text_data_clean, file = "/Users/merleschuckart/Desktop/EXNAT1 data/preproc_data/preproc_data_clean.csv")
#write.csv(df_demogr,          file = "/Users/merleschuckart/Desktop/EXNAT1 data/preproc_data/preproc_demogr_data.csv")




###########################

### CLEAN DATA (at least a bit, exclude breaks & outliers & stuff)

# only use data from the main blocks from now on:
df_text_data_clean <- subset(df_text_data, block_kind == "Reading_Baseline_main" |
                               block_kind == "1back_dual_main" |
                               block_kind == "2back_dual_main")

### EXCLUDE BREAKS ####
# --> Exclude all trials where participants took more than 3 seconds (arbitrary value)
#     I don't want breaks to influence the scaling of my "usable" data in the next steps
# to go to the next word
df_text_data_clean <- subset(df_text_data_clean, duration <= 3000)

# Now have a look at the distribution of the reading times (basically reaction times) in comparison to the
# reading speed data
# in comparison to the reading times data (those are basically reaction times)
#--> which distribution looks more normal? (probably the reading speed distributions, but better check this.)

plot_reading_times <- subset(df_text_data_clean, reading_speed <= 500)
#densityplot(subset(plot_reading_times)$reading_speed)
#densityplot(subset(plot_reading_times)$duration)
# Okay so it's pretty obvious that the reading speed data distribution looks better. We'll work with that one.



### TRANSFORM DATA, EXCLUDE OUTLIERS ####

#range(df_text_data_clean$reading_speed)
#range(df_text_data_clean$duration)

# Try outlier exclusion as described in Cousineau & Chartier, 2010
# I found this approach in this paper, where it's recommended as the best outlier exclusion method for skewed data
# https://doi.org/10.3389/fpsyg.2021.675558

# "For each transformed value, the square root of the untransformed value minus the minimum value of the sample divided
# through the sample range is calculated. The fraction bounds all values between 0 and 1,
# while the square root enlarges small values (Cousineau and Chartier, 2010).
# Afterwards, these values are z-transformed and values exceeding a particular z-score (e.g., 2 or 3)
# are excluded. For the present simulations, we excluded RTs associated with a z-score larger/smaller than ±2 as outliers."
# (Berger & Kiefer, 2021)

# Long story short:
# transf_val = sqrt (  ( x - sample_min ) / ( sample_max - sample_min)  )
# --> after this, z-transform all values and exclude all values exceeding a value of ± 2 (or ± 3, but they used 2 in the paper)

# This is basically a POMS (Little (2013), read in Moeller (2013)) transformation where you get
# the square root of the output afterwards and z-transform everything.

# Careful, you have to to the transformation over all participants & conditions, so
# everything gets "pulled" into the same range.
# If I'd do this for each subject & condition separately, I couldn't compare means
# anymore, because every subset of data would have its own scale.


# get min reading speed
# sample_min <- min(df_text_data$reading_speed)
sample_min <- 0 # use smallest possible value here (this is described in a book by Little, 2013) - in this case: 0 words / 100 ms

# get max reading speed (use sample maximum here)
sample_max <- max(df_text_data_clean$reading_speed)

# do sqrt(POMS) transform of raw reading speed values
df_text_data_clean$reading_speed_standardized <- sqrt((df_text_data_clean$reading_speed - sample_min) / (sample_max - sample_min))

# z-transform reading data
df_text_data_clean$reading_speed_standardized <- as.vector(scale(df_text_data_clean$reading_speed_standardized, center = T, scale = T))


# Check out the new distribution!
#densityplot(subset(df_text_data_clean)$reading_speed_standardized)


### Mark outliers for exclusion ####

# --> exclude single trials that are outliers

# get index of all values < - 2 or > 2 in subj_df$reading_speed_standardized & exclude those trials
excl_row_idx <- which(df_text_data_clean$reading_speed_standardized < -2 | df_text_data_clean$reading_speed_standardized > 2)

message(paste("excluding", length(excl_row_idx), "outlier trials now because they fell out of the -2 - 2 range after the z-sqrt-POMS transformation", sep = " "))

# check how the corresponding untransformed RTs look like so we get a feeling for what's being excluded:
#summary(df_text_data[excl_row_idx, "duration"]) # looks good!

# kick them out
df_text_data_clean[excl_row_idx, "excl_trial"] <- TRUE
df_text_data_clean <- subset(df_text_data_clean, excl_trial == FALSE)

# plot again:
#densityplot(df_text_data_clean$reading_speed_standardized)

# The data are still not normally distributed if I divide them by n-back condition & block
# --> Is this a problem for my linear mixed model?!
#qqnorm(subset(df_text_data_clean, block_names_numbered == "1back_main_2")$reading_speed_standardized)
#qqline(subset(df_text_data_clean, block_names_numbered == "1back_main_2")$reading_speed_standardized)



# ---- PLOT STANDARDIZED READING SPEED x N-BACK x FLICKER ----

# Maybe exclude non-native speakers?

plot_df <- subset(df_text_data_clean, 
                  reaction == F 
                  #& native_speaker == T
                  ) # exclude trials where you had a reaction & data by non-native speakers

plot_df <- setNames(aggregate(plot_df$reading_speed_standardized,
                              by = list(plot_df$ID, plot_df$block_kind, plot_df$flicker_on),
                              FUN = mean),
                    c("ID", "Condition", "Flicker", "reading_speed_standardized"))


# change order of n-back levels:
plot_df$Condition <- as.factor(plot_df$Condition)
plot_df$Condition <- factor(plot_df$Condition, levels = c("Reading_Baseline_main", 
                                                          "1back_dual_main",
                                                          "2back_dual_main"))

# plot normalized reading times
pirateplot(formula = reading_speed_standardized ~ Condition * Flicker,
           data = plot_df,
           theme = 1,
           pal = c("darkseagreen3", "darkgoldenrod1", "indianred1"),
           bean.b.col = c("darkseagreen3", "darkgoldenrod1", "indianred1"),
           bean.b.o = 1,
           inf.f.o = 0,
           point.o = 1,
           point.cex = 0.8,
           point.col = c("darkseagreen4", "darkgoldenrod3", "indianred3"),
           avg.line.col = c("darkseagreen4", "darkgoldenrod3", "indianred3"), # avg line col
           main = paste("Standardized reading speed in each n-back & flicker condition (N = ", length(unique(plot_df$ID)), ")", sep = ""),
           ylab = "standardized reading speed",
           ylim = c(-2, 2), # start y-lim at -2
           inf.method = "ci", # plot confidence interval as box around M
           inf.p = 0.95, # use 95% for confidence interval
           plot = T) # plot the plot
 
# The weird improvement in BL in the nd and hs datasets due to flicker is probably a Reihenfolgeeffekt 
# (BL blocks were first both not flickered and then later on flickered by chance)
# Ich lehne mich mal gefährlich weit aus dem Fenster (weil wegen N = 3 und 1 non-native speaker) und sage der Flicker macht 
# nichts oder zumindest nicht viel mit den Lesezeiten. Das ist gut.



######### Linear mixed models #########

# shrink the df a bit: exclude rows that don't have surprisal scores on all time scales
lmm_df <- subset(df_text_data_clean, !is.na(surprisal_60))

# typecast values in block_kind to ordered factors with levels Reading_BL_main as Baseline, 1back_main and 2back_main:
lmm_df$block_kind <- ordered(lmm_df$block_kind, levels = c("Reading_BL_main", "1back_dual_main", "2back_dual_main"))

# create a Simple Coding scheme for the variable block_kind
# https://stats.oarc.ucla.edu/r/library/r-library-contrast-coding-systems-for-categorical-variables/
# creating the contrast matrix manually by modifying the dummy coding scheme
c <- contr.treatment(3) # create dummy coding scheme
my.coding <- matrix(rep(1/3, 6), ncol = 2) # make matrix with only 1/3 values
# change values in dummy coding scheme to either -1/3 or 2/6 by
# subtracting 1/3 from 0s and 1s in the dummy coding scheme
my.simple <- c-my.coding
# show new coding scheme
#my.simple

#assign the new coding scheme to lmm_df$block_kind
contrasts(lmm_df$block_kind) <- my.simple

# typecast "reaction" to factor because sjplot complains about logicals
# --> I tried just typecasting it to "TRUE" and "FALSE" as factor strings, but for some reason 
# it got converted to logicals again. 
# So I recoded the factor levels as 1 and -1 (aka factor ints) and hope it doesn't get converted again 
lmm_df$reaction <- as.factor(ifelse(lmm_df$reaction == "TRUE", 1, -1)) # 1 = TRUE and -1 = FALSE

# ----------- z-transform continuous variables for mixed models -----------

# Define columns you want to z-transform:
freq_length_cols <- c("word_frequency", "word_length_single") # columns: word freq & word length

non_ortho_cols   <- c(paste0("surprisal_", c(1, 4, 12, 60))) # columns: surprisal_X with X being each of the TSs

# Apply scale function to each column
# --> set center to TRUE to subtract the sample mean from each value, set scale to TRUE to divide by standard deviation
lmm_df[paste0(freq_length_cols, "_z")] <- lapply(lmm_df[freq_length_cols], scale, center = TRUE, scale = TRUE)

lmm_df[paste0(non_ortho_cols, "_z")]   <- lapply(lmm_df[non_ortho_cols], scale, center = TRUE, scale = TRUE)

# ----------- scramble all surprisal scores & add as new columns: -----------

# scramble all timescales:
# loop timescales

for (i in c(1, 4, 12, 60)) {
  # set random seed to make sure they are all shuffled in a different way
  # --> easiest way to make sure the seed is always different: Use i as seed
  set.seed(i)
  # shuffle the current timescale x & create new column called surprisal_x_z_scrambled:
  lmm_df[[paste0("surprisal_", i, "_z_scrambled")]] <- sample(lmm_df[[paste0("surprisal_", i, "_z")]])
}


# ----------- define linear mixed model formula(s) -------------------

model_all <- reading_speed_standardized ~ block_kind      + # fixed effect: n-back condition
  flicker_on + # fixed effect: flicker on or off
  surprisal_1_z   + # fixed effect: surprisal on TS 1
  surprisal_4_z   + # fixed effect: surprisal on TS 4
  surprisal_12_z  + # fixed effect: surprisal on TS 12
  surprisal_60_z  + # fixed effect: surprisal on TS 60
  native_speaker  + # fixed effect: native speaker or not --> some of my participants might read slower because they're not native speakers
  word_frequency_z   + # fixed effect: word frequency
  word_length_single_z +
  reaction           + # nuisance regressor: people probably have longer RTs if they also reacted in the n-back task
  block_nr           + # nuisance regressor: people might be a bit slower in the later blocks due to fatigue effects
  trial_nr           + # nuisance regressor: people might be a bit slower at the end of each block due to fatigue
  #                     effects or quicker than in the beginning because they got used to the task
  # Interactions:
  block_kind : flicker_on +     # interaction n-back condition x flicker on or off
  block_kind : surprisal_1_z  + # interaction n-back condition x surprisal on TS 1
  block_kind : surprisal_4_z  + # interaction n-back condition x surprisal on TS 4
  block_kind : surprisal_12_z + # interaction n-back condition x surprisal on TS 12
  block_kind : surprisal_60_z + # interaction n-back condition x surprisal on TS 60
  
  # Random effects (aka variables that explain why some people deviate from the mean in my fixed effects conditions
  (1 | ID) +                      # random effect: ID
  (1 | text_nr) +                 # random effect: text nr: Text 1 could be different than text 2 and in a way, my texts are also just samples from the distribution of all texts I could have used
  (1 + flicker_on | ID) +         # subject-specific random slope: flicker by ID - participant might react differently to the flicker than other participants
  (1 + block_kind | ID) +         # subject-specific random slope: block_kind by ID - participant might perform differently in the tasks than other participants
  (1 + surprisal_1_z  | ID) +     # subject-specific random slope: surprisal on TS 1 by ID - participant might perform differently
                                  # when surprisal is high vs when surprisal is low compared to other participants
  (1 + surprisal_4_z  | ID) + # subject-specific random slope: surprisal on TS 4 by ID
  (1 + surprisal_12_z | ID) + # subject-specific random slope: surprisal on TS 12 by ID
  (1 + surprisal_60_z | ID) + # subject-specific random slope: surprisal on TS 60 by ID
  (1 + word_frequency_z | ID) + # subject-specific random slope: word frequency by ID
  (1 + word_length_single_z | ID) # subject-specific random slope: word length by ID


# ----------- fit frequentist linear mixed model (lmer4) ----------

# (this might take some time):
mixed.lmer_all <- lmer(formula = model_all,  data = lmm_df)
summary(mixed.lmer_all)
Anova(mixed.lmer_all)

# play super mario sound when this is finished
beep(sound = "mario")

# compute Type II Wald Chi^2 test to check
# which effects are significant:
Anova(mixed.lmer_all)
summary(mixed.lmer_all)
# Nice! Flicker on/off doesn't really seem to have an effect. 



#####################

### Check visual task performance:

# Idea: Compute time it took to respond for every target. 
# If no response and a new target is shown, count as a miss. 
# Also compare between training (with default speed 100 words/min) 
# and main block (known text with their own speed).
# --> not really comparable but will do for a rough estimate 
# I guess because they knew all the texts anyway.

# only get data for visual task:
df_vis_task <- subset(df_text_data, block_kind == "visual_task")

ID <- c() # participant ID
duration <- c() # duration of response
response_kind <- c() # hit or miss? 

# I was really really dumb and forgot to save the data from the training.
# But doesn't really matter, let's check the performance in the main block:

# loop participants:
for (curr_ID in unique(df_vis_task$ID)){
  print(curr_ID)
  
  # get part of current participant's dataset where we have either the training or the main block of the vis task:
  curr_dataset <- subset(df_vis_task, ID == curr_ID)
  first_target_shown = F
  participant_responded = F

  # loop rows in current dataset and check for targets and responses 
  # (doesn't have to be in the same row though)
  for (row_idx in 1:length(curr_dataset$ID)){
    #print(row_idx)
    # get current row
    curr_row <- curr_dataset[row_idx, ]
    
    # check if there was a target:
    if (curr_row$target == "True"){ 
      print("---------------") 
      
      print("target!")
      # reset target detection time because there's a new target
      target_detection_time = 0
      
      # check if participant noticed last target:
      
      # MISS: New target, but participant still hasn't responded for the one before:
      if (participant_responded == F){
        print("participant didn't see previous target!") 
        # save data:
        ID <- c(ID, curr_ID)
        response_kind <- c(response_kind, "miss")
        duration <- c(duration, NA) # no reaction so RT is NA
      }

      # if this was the first target, change first_target_shown to True:
      if (first_target_shown == F){
        first_target_shown = T
      }
      # reset response counter
      participant_responded = F
    }
    
    # HIT: if the participant reacted, add RT to target_detection_time and print target_detection_time
    if (curr_row$reaction == T & first_target_shown == T & participant_responded == F){ 
      print("response!")
      target_detection_time = target_detection_time + as.vector(curr_row$duration)
      print(target_detection_time)
      participant_responded = T
      # save data:
      ID <- c(ID, curr_ID)
      response_kind <- c(response_kind, "hit")
      duration <- c(duration, target_detection_time)
    
    # if they didn't react, just add RT to target_detection_time and go to next trial
    } else if (curr_row$reaction == F & first_target_shown == T) {
      target_detection_time = target_detection_time + curr_row$duration
    
    # FALSE ALARM: if participant responded but has already responded for the current target
    } else if (curr_row$reaction == T & first_target_shown == T & participant_responded == T) {
      # save data:
      ID <- c(ID, curr_ID)
      response_kind <- c(response_kind, "false alarm")
      duration <- c(duration, NA) # don't care about the false alarm RTs
  }  
 }
}

# create df:
vis_task_responses_df <- as.data.frame(cbind(ID, response_kind, duration))
vis_task_responses_df$duration <- as.numeric(vis_task_responses_df$duration)
#View(vis_task_responses_df)  


# get rid of NAs
plot_df <- na.omit(vis_task_responses_df)

# plot the raw durations from hit trials
pirateplot(formula = duration ~ response_kind * ID,
           data = plot_df,
           theme = 1,
           bean.b.o = 1,
           inf.f.o = 0,
           point.o = 1,
           point.cex = 0.8,
           main = paste("Raw RTs in the visual task (N = ", length(unique(plot_df$ID)), ")", sep = ""),
           ylab = "RT in ms",
           inf.method = "ci", # plot confidence interval as box around M
           inf.p = 0.95, # use 95% for confidence interval
           plot = T) # plot the plot

# check how many targets they missed
for (curr_id in unique(vis_task_responses_df$ID)){
  print(paste("Participant ID:", curr_id, sep = " "))
  curr_dataset <- subset(vis_task_responses_df, ID == curr_id)
  print(paste("# misses:", length(which(curr_dataset$response_kind == "miss") == T), sep = " "))
  print(paste("# hits:", length(which(curr_dataset$response_kind == "hit") == T), sep = " "))
  print(paste("# false alarms:", length(which(curr_dataset$response_kind == "false alarm") == T), sep = " "))
  print("------------")
}

# Okay so seems like for some it's easy, for some it's not (or they didn't understand the task), 
# but it's kinda difficult to compute dprimes without a measure of correct rejections 
# because the trials are way too fast to analyse it all trial-wise.
# I don't even know if it matters if they suck at the task as long as they press the 
# button sometimes so I get motor responses.





