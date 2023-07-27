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
  
  # add column with info on whether participant should be excluded
  excl <- FALSE
  
  # append to demographics df
  df_demogr <- as.data.frame(rbind(df_demogr,
                                   cbind(id, age, gender, handedness)))
  
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
  
  # get rid of reading baseline training (that was just a practice block for the participants)
  subj_df <- subset(subj_df, block_kind != "Reading_Baseline_training")
  
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
    # get the first 300 trials (each block has 300 trials so the first 300 trials = 1st block.
    # There are 2 rows for each trial, which means we need the first 600 rows for the 1st block.)
    subj_df[which(subj_df$block_names_numbered == change_block_name), ]$block_names_numbered[c(1:300)] <- paste(change_block_name,"_1", sep = "")
    subj_df[which(subj_df$block_names_numbered == change_block_name), ]$block_names_numbered           <- paste(change_block_name,"_2", sep = "")
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
  
  
  
  # TO DO: 
  
  
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
    if (curr_text_nr == "" | is.na(curr_text_nr)){
      next
      # if it's a text block, though, assign word frequencies from csv
    } else {
      #print(curr_text_nr) # uncomment this if you'd like to show the texts each participant read
      
      # get word frequencies for current text nr
      curr_word_freqs <- subset(word_freqs_df, text_nr == curr_text_nr)$word_frequency
      # find out where in the subj_df text the text is located and add the word frequencies there
      subj_df[which(subj_df$text_nr == curr_text_nr),]$word_frequency <- curr_word_freqs
      
      # Do the same for the surprisal scores.
      curr_surprisals <- subset(surprisal_df, text_nr == curr_text_nr)
      
      # find out where in the subj_df text the current text nr is located
      curr_row <- which(subj_df$text_nr == curr_text_nr)
      
      # add the surprisal scores (untransformed & orthogonalized scores) there
      subj_df[curr_row, c("surprisal_1", "surprisal_4",
                          "surprisal_12", "surprisal_60")]  <- curr_surprisals[c("surprisal_1", "surprisal_4",
                                                                                 "surprisal_12",  "surprisal_60")]

    }# END if
  }# END loop texts
  
  