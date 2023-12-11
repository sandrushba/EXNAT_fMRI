# Analysis for EXNAT-2 (Behavioural Data from the EEG Study)

# Author: Merle Schuckart (merle.schuckart@gmx.de)
# Version: July 2023

################################################################################

### -------- What does this script do? --------
# I built an EEG experiment version of the EXNAT-1 study in Psychopy. 
# In my study, I made the participants read 10 texts, 3 BL, 3 with a 1-back 
# and 3 with a 2-back task, and finally 1 automatically paced block with a 0-back colour-detection task.

# I would like to...
# 1. ...create a df for each participant containing the stimuli and their reading times so I can use that for the EEG analysis.
# 2. ...know whether we can replicate the findings from EXNAT-1.

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
#print(getwd())


# import get_dprime() function from another script I built
source("get_dprime.R") # get script

# -------- 1. Get data --------

# Set directory to data folder:
path_data_folder <- "Data/"

# Get list of all folders in the data folder
file_list <- list.files(path = path_data_folder)

# Placeholders df for demographics, questions & text data
df_demogr_all           <- data.frame()
df_text_data        <- data.frame()
df_comprehension_Qs <- data.frame()

# Loop files in my file list aka directory
for (i in 1:length(file_list)) {
 
 
  # PREPARE FILE FOR PREPROCESSING
  
  # get names of csv files for current participant: There should be one file containing the experimental 
  # data from the psychopy experiment and one with the AQ-SSQ questionnaire data and the demographics.
  # We need to read in both.
  curr_files <- list.files(path = paste(path_data_folder, file_list[i], "/", sep = ""), pattern = ".csv")

  # now get the one with the longer name, that's the psychopy one:
  idx_psychopy_file <- which.max(nchar(curr_files))
  subj_df <- read.csv(paste(path_data_folder, file_list[i], "/", curr_files[idx_psychopy_file], sep = ""), sep = ",")
  
  # get the other one, that's the questionnaire one:
  idx_questionnaire_file <- which.min(nchar(curr_files))
  subj_quest_df <- read.csv(paste(path_data_folder, file_list[i], "/", curr_files[idx_questionnaire_file], sep = ""), sep = ",")
  
  # get demographical data from the questionnaire df:
  id             <- subset(subj_quest_df, sender == "ID")$ID # individual code
  message(paste(i, " - Reading in file of participant with ID: ", id, sep = ""))
  
  age            <- subset(subj_quest_df, sender == "demographics")$age # age in years
  gender         <- subset(subj_quest_df, sender == "demographics")$gender # gender in passport
  handedness     <- subset(subj_quest_df, sender == "demographics")$handedness # left- or right-handed?
  native_speaker <- as.logical(subset(subj_quest_df, sender == "demographics")$native_speaker) # native German speaker?
  drugs          <- as.logical(subset(subj_quest_df, sender == "demographics")$drugs)
  alcohol        <- as.logical(subset(subj_quest_df, sender == "demographics")$alcohol)
  education      <- subset(subj_quest_df, sender == "demographics")$education
  medicine       <- as.logical(subset(subj_quest_df, sender == "demographics")$medicine)
  neur_disorder  <- as.logical(subset(subj_quest_df, sender == "demographics")$neur_disorder)
  stroke         <- as.logical(subset(subj_quest_df, sender == "demographics")$stroke)
  psych_disorder <- as.logical(subset(subj_quest_df, sender == "demographics")$psych_disorder)
  reading_weakness <- as.logical(subset(subj_quest_df, sender == "demographics")$reading_weakness)
  seeing_impaired  <- as.logical(subset(subj_quest_df, sender == "demographics")$seeing_impaired)
  colour_vision_impaired <- as.logical(subset(subj_quest_df, sender == "demographics")$colour_vision_impaired)
  hearing_impaired  <- as.logical(subset(subj_quest_df, sender == "demographics")$hearing_impaired)
  CI_or_hearing_aid <- as.logical(subset(subj_quest_df, sender == "demographics")$CI_or_hearing_aid)
  flicker_freq   <-  "15 Hz" # we only used a 15 Hz flicker
  excl           <- FALSE # Should participant be excluded from further analysis? Default: No.

  # Calculate AQ - SPQ Continuum Scores for all participants:
  AQ_SS   <- NA
  AQ_AS   <- NA
  AQ_AD   <- NA
  AQ_C    <- NA
  AQ_I    <- NA
  AQ_all  <- NA
  SQP_RI  <- NA
  SQP_SA  <- NA
  SQP_MD  <- NA
  SQP_UW  <- NA 
  SQP_EV  <- NA
  SQP_KEF <- NA
  SQP_US  <- NA
  SQP_EA  <- NA
  SQP_AW  <- NA
  SPQ_all <- NA
  

  # append them to df_demogr:
  df_demogr <- as.data.frame(cbind(id, age, gender,
                                   handedness, native_speaker,
                                   drugs, alcohol, education, medicine,
                                   neur_disorder, stroke, psych_disorder,
                                   reading_weakness, seeing_impaired, colour_vision_impaired,
                                   hearing_impaired, CI_or_hearing_aid,
                                   AQ_SS, AQ_AS, AQ_AD, AQ_C, AQ_I, AQ_all,
                                   SQP_RI, SQP_SA, SQP_MD, SQP_UW, SQP_EV, 
                                   SQP_KEF, SQP_US, SQP_EA, SQP_AW, SPQ_all,
                                   flicker_freq, excl))
  
  ### SPQ: 
  # From the Original Questionnaire: "Alle mit „Ja“ beantworteten Items werden mit 1 verrechnet. 
  #                                   Der Gesamtwert ist die Summe aller Subskalenwerte."
  # So basically all items where participant answered "yes" is counted as 1, "no" is counted as 0. 
  # If you get the sum for each of the scales, you have the sub scale score
  
  # Loop scales in SPQ and count sub scales scores
  
  SPQ_scales <- c("RI",  # Referenzideen (counterintuitively, RI ≠ Rihanna here)
                  "SA",  # (exzessive) soziale Angst
                  "MD",  # Ungwöhnliche Glaubensinhalte / Magisches Denken
                  "UW",  # Ungewöhnliche Wahrnehmungen
                  "EV",  # Ungewöhnliches oder exzentrisches Verhalten
                  "KEF", # Keine engen Freunde
                  "US",  # Ungewöhnliche Sprache
                  "EA",  # Eingeschränkter Affekt
                  "AW")  #Argwohn / Wahnähnliche Vorstellungen
  
  for (curr_subscale in SPQ_scales){
    #print(curr_subscale)
    # get names of all columns that end with the current sub scale name
    curr_columns <- as.vector(names(subj_quest_df)[grep("AW", names(subj_quest_df))])
    # get subset of df where columns have these names:
    curr_columns <- subj_quest_df[curr_columns]
    
    # get only the row where we have values:
    curr_columns <- curr_columns[which(subj_quest_df$sender == "SPQ-G"), ]
    
    # now count how many times participant answered "yes" (label = 1)
    curr_subscale_score <- sum(curr_columns)
    #print(curr_subscale_score)
    
    # put subscale score into demographics df:
    df_demogr[paste("SQP_", curr_subscale, sep = "")] <- as.numeric(curr_subscale_score)
    
  } 
  
  # also assign overall score:
  df_demogr$SPQ_all <- sum(subj_quest_df[which(subj_quest_df$sender == "SPQ-G"), 
                                    as.vector(names(subj_quest_df)[grep("SPQ", names(subj_quest_df))])])
  
  

  ### Autism-Spectrum Quotient (AQ)
  
  #Baron-Cohen, S., Wheelwright, S., Skinner, R., Martin, J., & Clubley, E. (2001). 
  # The autism-spectrum quotient (AQ): Evidence from asperger syndrome/high-functioning autism, 
  # males and females, scientists and mathematicians. Journal of autism and developmental disorders, 31(1), 5-17.
  
  # First, we have to recode some of the item scores:
  # Recode all positive values to 1, recode all negative values to 0:
  
  AQ_df <- subj_quest_df[which(subj_quest_df$sender == "AQ-G"), as.vector(names(subj_quest_df)[grep("AQ", names(subj_quest_df))])]
  AQ_df[1,] <- ifelse(as.vector(unlist(AQ_df)) > 0, 1, 0)
  
  
  # Now we have to change the polarity of some of the items. 
  
  # The scores 1 and 0 for the following items can stay as they are: 
  # 2, 4, 5, 6, 7, 9, 12, 13, 16, 18, 19, 20, 21, 22, 23, 26, 33, 35, 39, 41, 42, 43, 45 und 46 
  
  # The scores 1 and 0 for the following items have to be reversed to 0 and 1: 
  # 1, 3, 8, 10, 11, 14, 15, 17, 24, 25, 27, 28, 29, 30, 31, 32, 34, 36, 37, 38, 40, 44, 47, 48, 49 und 50 
  
  reverse_indices <- c(1, 3, 8, 10, 11, 14, 15, 17, 24, 25, 27, 28, 29, 
                       30, 31, 32, 34, 36, 37, 38, 40, 44, 47, 48, 49, 50)
  
  # reverse the values for the items I specified above
  AQ_df[1, reverse_indices] <- ifelse(AQ_df[1, reverse_indices] == 0, 1, 0)
  
  # Now we're all set for counting the subscale scores. 
  
  # The AQ-50 has 5 subscales. 
  # It's a bit difficult to find them as most sites only report how to get & interpret 
  # the overall score, but I found a key here and the scales make sense 
  # to me if I look at the corresponding items: 
  #     https://novopsych.com.au/assessments/diagnosis/autism-spectrum-quotient/
  
  # Social skill:        items 01,11,13,15,22,36,44,45,47,48
  # Attention switching: items 02,04,10,16,25,32,34,37,43,46
  # Attention to detail: items 05,06,09,12,19,23,28,29,30,49
  # Communication:       items 07,17,18,26,27,31,33,35,38,39
  # Imagination:         items 03,08,14,20,21,24,40,41,42,50
  
  df_demogr$AQ_SS <- sum(AQ_df[ , c("AQ_01", "AQ_11", "AQ_13", 
                                    "AQ_15", "AQ_22", "AQ_36", 
                                    "AQ_44", "AQ_45", "AQ_47", 
                                    "AQ_48")])
  
  df_demogr$AQ_AS <- sum(AQ_df[ , c("AQ_02", "AQ_04", "AQ_10",
                                    "AQ_16", "AQ_25","AQ_32",
                                    "AQ_34","AQ_37","AQ_43",
                                    "AQ_46")])
  
  df_demogr$AQ_AD <- sum(AQ_df[ , c("AQ_05","AQ_06","AQ_09",
                                    "AQ_12","AQ_19","AQ_23",
                                    "AQ_28","AQ_29","AQ_30",
                                    "AQ_49")])
  
  df_demogr$AQ_C <- sum(AQ_df[ , c("AQ_07","AQ_17","AQ_18",
                                   "AQ_26","AQ_27","AQ_31",
                                   "AQ_33","AQ_35","AQ_38",
                                   "AQ_39")])
  
  df_demogr$AQ_I <- sum(AQ_df[ , c("AQ_03","AQ_08","AQ_14",
                                   "AQ_20","AQ_21","AQ_24",
                                   "AQ_40","AQ_41","AQ_42",
                                   "AQ_50")])
  
  # get overall AQ score: 
  df_demogr$AQ_all <- sum(AQ_df[ ,])
  
  # add current participant's data to df with data of all participants:
  df_demogr_all <- as.data.frame(rbind(df_demogr_all, df_demogr))
  
  # remove helper variables to keep things tidy
  rm (age, gender, handedness, native_speaker,
      drugs, alcohol, education, medicine,
      neur_disorder, stroke, psych_disorder,
      reading_weakness, seeing_impaired, colour_vision_impaired,
      hearing_impaired, CI_or_hearing_aid,
      flicker_freq, excl)
  
  # save backup of demographics df in current participant's folder
  write.csv(df_demogr, paste(path_data_folder, file_list[i], "/", file_list[i], "_demographics.csv", sep = ""), row.names = FALSE)
  #--> update this later with info on excluded trials & stuff
  
  
  ###########################
  
  # GET RAW TEXT & N-BACK DATA
  
  # save raw df for later
  subj_df_raw <- subj_df
  
  # get rid of some unimportant columns:
  subj_df <- subj_df[ ,  c("colour", "target", "nback_response", "nback_RT", "duration", 
                           "text_nr", "trial_nr", "word",
                           "block_nr", "block_name", "block_kind", "block_cond",
                           "question", "chosen_ans", "ans_correct",             
                           "vistask_RT_per_letter", "vistask_target", 
                           "participant", "age", "handedness", "gender", 
                           "meas_hearing", "skip_prediction_tendency")]
  
  # delete weird empty rows (I think they sometimes occur after the dual task blocks, 
  # but it doesn't seem like something is missing.)
  subj_df <- subset(subj_df, !is.na(block_nr))

  # name column "block_name" "block_kind" and "participant" "ID" so it matches the EXNAT-1 variables
  names(subj_df)[which(names(subj_df) == "block_name")] <- "block_kind"
  names(subj_df)[which(names(subj_df) == "participant")] <- "ID"
  
  # add excl column:
  subj_df$excl <- FALSE

  # get rid of reading baseline training (that was just a practice block for the participants)
  #subj_df <- subset(subj_df, block_kind != "Reading_Baseline_training")
  
  ###########################
  
  ### ADD NUMBERED BLOCK NAMES ####
  
  # Problem: 
  # In some cases, 3 blocks of the same kind could just directly follow each other, so 
  # there's no way to tell them apart. If we want to compute d-primes by block, though, 
  # it would be nice if they had unique names and I wouldn't have to build 
  # something from the block numbers and block conditions.
  
  # Idea: 
  # Create counters for BL, 1-back and 2-back main blocks, loop rows, 
  # if a new block starts, update counter and add new block label.
  # Keep in mind that we have more than 300 trials in each block 
  # because we also need labels for the question rows.
  
  # first, just copy the "old" block names
  subj_df$block_names_numbered <- subj_df$block_kind
  
  BL_counter <- 1
  oneback_counter <- 0
  twoback_counter <- 0
  previous_block_counter <- NA
  curr_block_trials <- 1 # count trials of current block
  

  for (curr_row_idx in 1:length(subj_df$block_names_numbered)){
  
    #print(curr_bl_name)
    curr_block_name <- subj_df$block_names_numbered[curr_row_idx]
    
    # For BL: 
    if (curr_block_name == "Reading_Baseline_main"){
      # if we already counted more than 300 trials and it's 
      # the first trial again, reset trial counter and add 1 to block counter:
      if (curr_block_trials > 300 & !is.na(subj_df$trial_nr[curr_row_idx]) & subj_df$trial_nr[curr_row_idx] == 1){
        curr_block_trials <- 1
        BL_counter <- BL_counter + 1
        #print(paste(curr_block_name, "_", BL_counter, sep = "") )
      }
      # rename block: 
      subj_df$block_names_numbered[curr_row_idx] <- paste(curr_block_name, "_", BL_counter, sep = "") 
      # go to next trial: 
      curr_block_trials <- curr_block_trials + 1
    
      
    # FOR 1-back:
    } else if (curr_block_name == "1back_dual_main"){
      # if we already counted more than 300 trials and it's 
      # the first trial again, reset trial counter and add 1 to block counter:
      if (curr_block_trials > 300 & !is.na(subj_df$trial_nr[curr_row_idx]) & subj_df$trial_nr[curr_row_idx] == 1){
        curr_block_trials <- 1
        oneback_counter <- oneback_counter + 1
        #print(paste(curr_block_name, "_", oneback_counter, sep = "") )
      }
      # rename block: 
      subj_df$block_names_numbered[curr_row_idx] <- paste(curr_block_name, "_", oneback_counter, sep = "") 
      # go to next trial: 
      curr_block_trials <- curr_block_trials + 1
    
    # FOR 2-back:
    } else if (curr_block_name == "2back_dual_main"){
      # if we already counted more than 300 trials and it's 
      # the first trial again, reset trial counter and add 1 to block counter:
      if (curr_block_trials > 300 & !is.na(subj_df$trial_nr[curr_row_idx]) & subj_df$trial_nr[curr_row_idx] == 1){
        curr_block_trials <- 1
        twoback_counter <- twoback_counter + 1
        #print(paste(curr_block_name, "_", twoback_counter, sep = "") )
      }
      # rename block: 
      subj_df$block_names_numbered[curr_row_idx] <- paste(curr_block_name, "_", twoback_counter, sep = "") 
      # go to next trial: 
      curr_block_trials <- curr_block_trials + 1
    }  
  }
  
  # check if it worked:
  #print(unique(subj_df$block_names_numbered))
  
  
  ###########################
  
  ### COMPUTE READING SPEED ####
  
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
  
  
  ### WORD FREQUENCIES & SURPRISAL SCORES ####
  
  # Include word frequencies & surprisal scores for each word
  
  # append "empty" word frequency & surprisal score columns to df
  # to do so, create a vector of column names
  col_names <- c("word_frequency", paste0("surprisal_", c(1, 4, 12, 60)))#,
  # then add "empty" columns to data frame subj_df
  subj_df[, col_names] <- 0
  
  # get word frequency & surprisal scores for each word
  # load word freq df
  word_freqs_df = read.csv(paste(getwd(), "/word frequencies/Word_freqs.csv", sep = ""), sep = ";", header=TRUE)[2:4]
  
  # load surprisal scores / similarity scores df with TS = context chunk size
  surprisal_df = read.csv(paste(getwd(),"/surprisal scores/surprisal_scores_masked_context.csv", sep = ""), sep = ",", header = TRUE)

  # loop individual texts
  for (curr_text_nr in unique(subj_df$text_nr)){

    # in some blocks we don't have texts, so skip those
    # skip BL training & vistask training as well
    if (curr_text_nr != "" & !is.na(curr_text_nr) & curr_text_nr != "None" & curr_text_nr != "reading_bl_training_text" & curr_text_nr != "vis_task_training"){

      # get word frequencies for current text nr
      curr_word_freqs <- subset(word_freqs_df, text_nr == curr_text_nr)$word_frequency
      
      # get surprisal scores:
      curr_surprisals <- subset(surprisal_df, text_nr == curr_text_nr)
      
      # find out where in the subj_df text the text is located and add the word frequencies there. 
      # Take only the first 300 rows because the rest are the questions' rows.

      # assign word frequencies only once
      subj_df[which(subj_df$text_nr == curr_text_nr),]$word_frequency[0:300] <- curr_word_freqs
      # add surprisal scores:
      curr_row <- which(subj_df$text_nr == curr_text_nr & subj_df$word != "")
      subj_df[curr_row, c("surprisal_1", "surprisal_4",
                          "surprisal_12", "surprisal_60")]  <- curr_surprisals[c("surprisal_1", "surprisal_4",
                                                                                 "surprisal_12",  "surprisal_60")]
    }
  }# END loop texts 
  
  
  ### GET SURPRISAL SCORES OF PREVIOUS WORD ####
  # --> skipped this part from the EXNAT-1 analysis
  
  # TO DO: ADD THIS PART!
  
  
  
  
  
  
  
  
  
  
  ###########################
  # GET PERFORMANCE MEASURES:
  
  ### COMPREHENSION QUESTION PERFORMANCE ####

  # We now get all question data for the main blocks
  Q_df <- subset(subj_df, chosen_ans != "" & block_kind %in% c("Reading_Baseline_main", "2back_dual_main", "1back_dual_main"))[,c("question", "chosen_ans", "ans_correct", "text_nr", "block_kind", "ID", "block_nr")]

  # Just look at the MC questions:
  # For now I don't really care about the answer, I only want to know if they chose the correct one or not.
  
  # typecast everything to logical
  Q_df$ans_correct <- as.logical(Q_df$ans_correct)
  
  # get performance in Qs
  Q_df$nr_correct <- c(rep(NA, times = length(Q_df$ID)))
  
  # for each main block, count how many questions were answered correctly.
  for (curr_block in unique(Q_df$block_nr)){
    curr_Q_df <- subset(Q_df, block_nr == curr_block)
    # count how many questions were answered correctly in the current block
    nr_correct <- length(subset(curr_Q_df, ans_correct == TRUE)$ans_correct)
    # append to Q_df & subj_df$Q_nr_correct
    Q_df[which(Q_df$block_nr == curr_block), ]$nr_correct <- nr_correct
  }
  
  # append Q_df to bigger df for all participants
  df_comprehension_Qs <- as.data.frame(rbind(df_comprehension_Qs, Q_df))
  
  # save in participant's folder:
  write.csv(df_comprehension_Qs,
            file = paste(path_data_folder, file_list[i], "/", file_list[i], "_df_comprehension_Qs.csv", sep = ""), 
            row.names = FALSE)

  
  
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
  
  # save current participant's data in their folder:
  write.csv(subj_df,
            file = paste(path_data_folder, file_list[i], "/", file_list[i], "_behav_data.csv", sep = ""), 
            row.names = FALSE)
  
  ###########################
  
  ### MARK PARTICIPANTS / TRIALS FOR EXCLUSION:
  
  # append "empty" exclude trial / exclude participant columns to df
  subj_df$excl_trial       <- FALSE
  subj_df$excl_participant <- FALSE
  
  
  # append subj_df chunk to df_text_data where we collect the data of all participants
  df_text_data <- as.data.frame(rbind(df_text_data, subj_df))
  message("------------------------")
  
}# END LOOP PARTICIPANTS

# clean up!
rm(list=ls()[! ls() %in% c("df_text_data", "df_demogr_all", "df_comprehension_Qs", "word_freqs_df")])

# save preprocessed data for further analysis:
#write.csv(df_text_data, file = paste(getwd(), "/Data/preproc_behav_data_all.csv", sep = ""), row.names = FALSE)
#write.csv(df_demogr_all, file = paste(getwd(), "Data/preproc_demogr_data_all.csv", sep = ""), row.names = FALSE)

###########################



# Bring the AQ and SPQ subscale scores together & 
# calculate prediction strategy style score for each participant

# get all subscale values
subscale_data <- df_demogr_all[,c("AQ_SS", "AQ_AS", "AQ_AD", "AQ_C", "AQ_I",
                              "SQP_RI","SQP_SA", "SQP_MD", "SQP_UW", "SQP_EV", 
                              "SQP_KEF", "SQP_US", "SQP_EA", "SQP_AW") ]

# compute correlation matrix
# --> doesn't make sense for 1 participant. I think I need all other participant's data here, too.
correlation_matrix <- cor(subscale_data)

# run PCA
pca_result <- prcomp(correlation_matrix)

# get the second principal component from the PCA
PC2 <- pca_result$rotation[, 2]

df_demogr$PC2 <- subscale_data %*% PC2






# TO DO:



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
                  reaction == F # uncomment to exclude trials where we had an n-back reaction
                  #& flicker_freq == "12 Hz (but unstable)"# # "12 Hz (but unstable)" or "15 Hz"
                  #& native_speaker == T # uncomment to exclude non-native speakers
) 

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
pirateplot(formula = reading_speed_standardized ~ Flicker * Condition,
           data = plot_df,
           theme = 1,
           pal = c("darkseagreen3","darkseagreen3", "darkgoldenrod1", "darkgoldenrod1", "indianred1","indianred1"),
           bean.b.col = c("darkseagreen3","darkseagreen3", "darkgoldenrod1", "darkgoldenrod1", "indianred1","indianred1"),
           bean.b.o = 1,
           inf.f.o = 0,
           point.o = 1,
           point.cex = 0.8,
           point.col = c("darkseagreen4","darkseagreen4", "darkgoldenrod3", "darkgoldenrod3", "indianred3", "indianred3"),
           avg.line.col = c("darkseagreen4","darkseagreen4", "darkgoldenrod3", "darkgoldenrod3", "indianred3", "indianred3"), # avg line col
           main = paste("Standardized reading speed in each n-back & flicker condition (N = ", length(unique(plot_df$ID)), ")", sep = ""),
           ylab = "standardized reading speed",
           #ylim = c(-2, 2), # start y-lim at -2
           inf.method = "ci", # plot confidence interval as box around M
           inf.p = 0.95, # use 95% for confidence interval
           plot = T) # plot the plot

# The weird improvement in BL in the nd and hs datasets due to flicker is probably a Reihenfolgeeffekt 
# (BL blocks were first both not flickered and then later on flickered by chance)



######### Linear mixed models #########

# shrink the df a bit: exclude rows that don't have surprisal scores on all time scales
lmm_df <- subset(df_text_data_clean, !is.na(surprisal_60))

# typecast values in block_kind to ordered factors with levels Reading_BL_main as Baseline, 1back_main and 2back_main:
lmm_df$block_kind <- ordered(lmm_df$block_kind, levels = c("Reading_Baseline_main", "1back_dual_main", "2back_dual_main"))

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
  # --> easiest way to make sure the seed is always different between 
  #     time scales but the same every time I read this script: Use i as seed
  set.seed(i)
  # shuffle the current timescale x & create new column called surprisal_x_z_scrambled:
  lmm_df[[paste0("surprisal_", i, "_z_scrambled")]] <- sample(lmm_df[[paste0("surprisal_", i, "_z")]])
}


# ----------- define linear mixed model formula(s) -------------------

model_all <- reading_speed_standardized ~ block_kind + # fixed effect: n-back condition
  flicker_on + # fixed effect: flicker on or off
  flicker_freq + # fixed effect: flicker frequency 12 or 15 Hz
  surprisal_1_z   + # fixed effect: surprisal on TS 1
  surprisal_4_z             + # fixed effect: surprisal on TS 4
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
  flicker_on:surprisal_1_z   +  # interaction: flicker on/off x surprisal_1_z
  flicker_on:surprisal_4_z   +  # interaction: flicker on/off x surprisal_4_z
  flicker_on:surprisal_12_z  +  # interaction: flicker on/off x surprisal_12_z
  flicker_on:surprisal_60_z  +  # interaction: flicker on/off x surprisal_60_z
  # Random effects (aka variables that explain why some people deviate from the mean in my fixed effects conditions
  (1 | text_nr) + # random effect: text nr
  # subject-specific random slopes:
  (1 | ID) 


# also create formulas with scrambled time scales:
model_TS1_intact <- reading_speed_standardized ~ block_kind + # fixed effect: n-back condition
  flicker_on + # fixed effect: flicker on or off
  flicker_freq + # fixed effect: flicker frequency 12 or 15 Hz
  surprisal_1_z   + # fixed effect: surprisal on TS 1
  surprisal_4_z_scrambled             + # fixed effect: surprisal on TS 4
  surprisal_12_z_scrambled  + # fixed effect: surprisal on TS 12
  surprisal_60_z_scrambled  + # fixed effect: surprisal on TS 60
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
  block_kind : surprisal_4_z_scrambled            + # interaction n-back condition x surprisal on TS 4
  block_kind : surprisal_12_z_scrambled + # interaction n-back condition x surprisal on TS 12
  block_kind : surprisal_60_z_scrambled + # interaction n-back condition x surprisal on TS 60
  flicker_on:surprisal_1_z            +  # interaction: flicker on/off x surprisal_1_z
  flicker_on:surprisal_4_z_scrambled  +  # interaction: flicker on/off x surprisal_4_z
  flicker_on:surprisal_12_z_scrambled +  # interaction: flicker on/off x surprisal_12_z
  flicker_on:surprisal_60_z_scrambled +  # interaction: flicker on/off x surprisal_60_z
  # Random effects (aka variables that explain why some people deviate from the mean in my fixed effects conditions
  (1 | text_nr) + # random effect: text nr
  # subject-specific random slopes:
  (1 | ID) 

model_TS4_intact <- reading_speed_standardized ~ block_kind + # fixed effect: n-back condition
  flicker_on + # fixed effect: flicker on or off
  flicker_freq + # fixed effect: flicker frequency 12 or 15 Hz
  surprisal_1_z_scrambled   + # fixed effect: surprisal on TS 1
  surprisal_4_z             + # fixed effect: surprisal on TS 4
  surprisal_12_z_scrambled  + # fixed effect: surprisal on TS 12
  surprisal_60_z_scrambled  + # fixed effect: surprisal on TS 60
  native_speaker  + # fixed effect: native speaker or not --> some of my participants might read slower because they're not native speakers
  word_frequency_z   + # fixed effect: word frequency
  word_length_single_z +
  reaction           + # nuisance regressor: people probably have longer RTs if they also reacted in the n-back task
  block_nr           + # nuisance regressor: people might be a bit slower in the later blocks due to fatigue effects
  trial_nr           + # nuisance regressor: people might be a bit slower at the end of each block due to fatigue
  #                     effects or quicker than in the beginning because they got used to the task
  # Interactions:
  block_kind : flicker_on +     # interaction n-back condition x flicker on or off
  block_kind : surprisal_1_z_scrambled  + # interaction n-back condition x surprisal on TS 1
  block_kind : surprisal_4_z            + # interaction n-back condition x surprisal on TS 4
  block_kind : surprisal_12_z_scrambled + # interaction n-back condition x surprisal on TS 12
  block_kind : surprisal_60_z_scrambled + # interaction n-back condition x surprisal on TS 60
  flicker_on:surprisal_1_z_scrambled +  # interaction: flicker on/off x surprisal_1_z
  flicker_on:surprisal_4_z           +  # interaction: flicker on/off x surprisal_4_z
  flicker_on:surprisal_12_z_scrambled +  # interaction: flicker on/off x surprisal_12_z
  flicker_on:surprisal_60_z_scrambled +  # interaction: flicker on/off x surprisal_60_z
  # Random effects (aka variables that explain why some people deviate from the mean in my fixed effects conditions
  (1 | text_nr) + # random effect: text nr
  # subject-specific random slopes:
  (1 | ID) 

model_TS12_intact <- reading_speed_standardized ~ block_kind + # fixed effect: n-back condition
  flicker_on + # fixed effect: flicker on or off
  flicker_freq + # fixed effect: flicker frequency 12 or 15 Hz
  surprisal_1_z_scrambled   + # fixed effect: surprisal on TS 1
  surprisal_4_z_scrambled   + # fixed effect: surprisal on TS 4
  surprisal_12_z +            # fixed effect: surprisal on TS 12
  surprisal_60_z_scrambled  + # fixed effect: surprisal on TS 60
  native_speaker  + # fixed effect: native speaker or not --> some of my participants might read slower because they're not native speakers
  word_frequency_z   + # fixed effect: word frequency
  word_length_single_z +
  reaction           + # nuisance regressor: people probably have longer RTs if they also reacted in the n-back task
  block_nr           + # nuisance regressor: people might be a bit slower in the later blocks due to fatigue effects
  trial_nr           + # nuisance regressor: people might be a bit slower at the end of each block due to fatigue
  #                     effects or quicker than in the beginning because they got used to the task
  # Interactions:
  block_kind : flicker_on +     # interaction n-back condition x flicker on or off
  block_kind : surprisal_1_z_scrambled  + # interaction n-back condition x surprisal on TS 1
  block_kind : surprisal_4_z_scrambled  + # interaction n-back condition x surprisal on TS 4
  block_kind : surprisal_12_z + # interaction n-back condition x surprisal on TS 12
  block_kind : surprisal_60_z_scrambled + # interaction n-back condition x surprisal on TS 60
  flicker_on:surprisal_1_z_scrambled +  # interaction: flicker on/off x surprisal_1_z
  flicker_on:surprisal_4_z_scrambled +  # interaction: flicker on/off x surprisal_4_z
  flicker_on:surprisal_12_z +  # interaction: flicker on/off x surprisal_12_z
  flicker_on:surprisal_60_z_scrambled +  # interaction: flicker on/off x surprisal_60_z
  # Random effects (aka variables that explain why some people deviate from the mean in my fixed effects conditions
  (1 | text_nr) + # random effect: text nr
  # subject-specific random slopes:
  (1 | ID) 

model_TS60_intact <- reading_speed_standardized ~ block_kind      + # fixed effect: n-back condition
  flicker_on + # fixed effect: flicker on or off
  flicker_freq +
  surprisal_1_z_scrambled   + # fixed effect: surprisal on TS 1
  surprisal_4_z_scrambled   + # fixed effect: surprisal on TS 4
  surprisal_12_z_scrambled  + # fixed effect: surprisal on TS 12
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
  block_kind : surprisal_1_z_scrambled  + # interaction n-back condition x surprisal on TS 1
  block_kind : surprisal_4_z_scrambled  + # interaction n-back condition x surprisal on TS 4
  block_kind : surprisal_12_z_scrambled + # interaction n-back condition x surprisal on TS 12
  block_kind : surprisal_60_z + # interaction n-back condition x surprisal on TS 60
  flicker_on : surprisal_1_z_scrambled +  # interaction: flicker on/off x surprisal_1_z
  flicker_on : surprisal_4_z_scrambled +  # interaction: flicker on/off x surprisal_4_z
  flicker_on : surprisal_12_z_scrambled +  # interaction: flicker on/off x surprisal_12_z
  flicker_on : surprisal_60_z +  # interaction: flicker on/off x surprisal_60_z
  # Random effects (aka variables that explain why some people deviate from the mean in my fixed effects conditions
  (1 | text_nr) +                 # random effect: text nr: Text 1 could be different than text 2 and in a way, my texts are also just samples from the distribution of all texts I could have used
  (1 | ID) 

# ----------- fit frequentist linear mixed models (lmer4) ----------

# (this might take some time):
mixed.lmer_all <- lmer(formula = model_all,  data = lmm_df)

# play super mario sound when this is finished
#beep(sound = "mario")

# compute Type II Wald Chi^2 test to check
# which effects are significant:
Anova(mixed.lmer_all)
#summary(mixed.lmer_all)

# For all data (12 + 15 Hz): N = 8 
# No main effect for flicker on/off, but there's an interaction effect with block 
# kind which is not so nice. I'd say the flicker doesn't really make a difference unless the task is really difficult.

# Only 15 Hz data: N = 2
# No flicker effects whatsoever, but a) tiny N and b) looks a bit like there's also an interaction of block x flicker.


# also check models with scrambled time scales:
mixed.lmer_TS1 <- lmer(formula = model_TS1_intact,  data = lmm_df)
Anova(mixed.lmer_TS1)
#summary(mixed.lmer_TS1)

mixed.lmer_TS4 <- lmer(formula = model_TS4_intact,  data = lmm_df)
Anova(mixed.lmer_TS4)
#summary(mixed.lmer_TS4)

mixed.lmer_TS12 <- lmer(formula = model_TS12_intact,  data = lmm_df)
Anova(mixed.lmer_TS12)
#summary(mixed.lmer_TS12)

mixed.lmer_TS60 <- lmer(formula = model_TS60_intact,  data = lmm_df)
Anova(mixed.lmer_TS60)
#summary(mixed.lmer_TS60)

beep(sound = "mario")

# check model output with FDR corrected p-values:
tab_model(mixed.lmer_TS60, 
          show.se = TRUE, 
          show.stat = TRUE,
          show.df = TRUE,
          p.val = 'wald', 
          p.adjust='fdr', 
          #p.style='scientific', 
          digits = 3, 
          digits.p = 3)


# save environment in current wd:
#save.image(file = 'EXNAT2_FlickerPilot_Analysis_REnvironment.RData')

#####################

# Check how participants rated the difficulty of the flicker vs. non-flicker blocks

# get ratings for subj_reading_effort1 and subj_text_difficulty, then 
# get the mean of the 2 ratings for each block kind (1-back, 2-back, baseline).

df_difficulty <- subset(df_comprehension_Qs, question == "subj_text_difficulty" | question == "subj_reading_effort1")

# get subj_reading_effort1 and subj_text_difficulty ratings and compute mean rating for each pair:
df_difficulty <- aggregate(as.numeric(chosen_ans) ~ text_nr + block_kind + ID + native_speaker + flicker_freq + block_nr + flicker_on + nr_correct, df_difficulty, mean)
names(df_difficulty)[length(names(df_difficulty))] <- "difficulty_rating"

# sort by ID
df_difficulty <- df_difficulty[order(df_difficulty$ID), ]


# prepare data for lmm:

# typecast values in block_kind to ordered factors with levels Reading_BL_main as Baseline, 1back_main and 2back_main:
df_difficulty$block_kind <- ordered(df_difficulty$block_kind, levels = c("Reading_Baseline_main", "1back_dual_main", "2back_dual_main"))

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
contrasts(df_difficulty$block_kind) <- my.simple

# z-transform difficulty rating column:
# --> set center to TRUE to subtract the sample mean from each value, set scale to TRUE to divide by standard deviation
df_difficulty$difficulty_rating_z <- scale(df_difficulty$difficulty_rating,  center = TRUE, scale = TRUE)

# put everything into a lmm:
model_difficulty_ratings <- difficulty_rating_z ~ block_kind +
  flicker_on + 
  flicker_freq + 
  native_speaker +
  block_nr +
  # Interactions:
  block_kind : flicker_on +
  # Random effects:
  (1 | text_nr) +
  (1 | ID)

mixed.lmer_difficulty_ratings <- lmer(formula = model_difficulty_ratings,  
                                      data = df_difficulty)
Anova(mixed.lmer_difficulty_ratings)
#summary(mixed.lmer_difficulty_ratings)


