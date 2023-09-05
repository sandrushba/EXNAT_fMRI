
# Script for Orthogonalizing Surprisal Scores
# (surprisal scores are calculated using the script "GPT_Surprisal_Score_Calculation.ipynb" --> same WD)

# Author: Merle Schuckart (merle.schuckart@gmx.de)
# Version: February 2023

##############################

# Settings
#install.packages("heplots")
#library(heplots)


# set working directory & read in csv with surprisal scores
setwd("/Users/merleschuckart/Github/PhD/EXNAT/Onlinestudy_EXNAT-1/Analysis/surprisal scores")
surprisal_scores_df <- read.csv("surprisal_and_similarity_scores.csv")

# compute orthogonal surprisal scores for surprisal on time scales 1, 2, 8, 16 & 32, 
# so subset of df containing those:
surprisal_scores <- surprisal_scores_df[ , c("X", "surprisal_1", "surprisal_2", "surprisal_8", "surprisal_16", "surprisal_32")]

# only get subset without NAs
surprisal_scores <- subset(surprisal_scores, !is.na(surprisal_32))

# orthogonalize vectors in columns in df surprisal_scores:
surprisal_scores_ortho <- gsorth(surprisal_scores[ ,c(2:length(surprisal_scores))],
                                 recenter = T, # new columns have same column means as original columns
                                 rescale = T) # new columns have same column standard deviations as original columns

# append indices
surprisal_scores_ortho <- as.data.frame(cbind(surprisal_scores$X, surprisal_scores_ortho))
# rename columns:
names(surprisal_scores_ortho) <- c("X", "surprisal_1_ortho", "surprisal_2_ortho", "surprisal_8_ortho", "surprisal_16_ortho", "surprisal_32_ortho")

# append 5 new NA columns to the original surprisal score df
surprisal_scores_df$surprisal_1_ortho  <- NA
surprisal_scores_df$surprisal_2_ortho  <- NA
surprisal_scores_df$surprisal_8_ortho  <- NA
surprisal_scores_df$surprisal_16_ortho <- NA
surprisal_scores_df$surprisal_32_ortho <- NA

# now put orthogonailzed values into the right columns/positions
surprisal_scores_ortho$X <- surprisal_scores_ortho$X + 1
surprisal_scores_df[surprisal_scores_ortho$X , "surprisal_1_ortho"] <- surprisal_scores_ortho$surprisal_1_ortho
surprisal_scores_df[surprisal_scores_ortho$X , "surprisal_2_ortho"] <- surprisal_scores_ortho$surprisal_2_ortho
surprisal_scores_df[surprisal_scores_ortho$X , "surprisal_8_ortho"] <- surprisal_scores_ortho$surprisal_8_ortho
surprisal_scores_df[surprisal_scores_ortho$X , "surprisal_16_ortho"] <- surprisal_scores_ortho$surprisal_16_ortho
surprisal_scores_df[surprisal_scores_ortho$X , "surprisal_32_ortho"] <- surprisal_scores_ortho$surprisal_32_ortho

# overwrite old surprisal score csv
write.csv(surprisal_scores_df, file = "surprisal_and_similarity_scores.csv")