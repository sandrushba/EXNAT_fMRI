# EXNAT-2 – Function for Analysis of Questionnaire Data
# Version: Dec. 2023
# Author: Merle Schuckart

# -----------------------------------------------------

# build some placeholders for the AQ and SPQ subscale scores
AQ_all <- NA
AQ_SS  <- NA
AQ_AS  <- NA
AQ_AD  <- NA
AQ_C   <- NA
AQ_I   <- NA
  
# append them to df_demogr:
df_demogr <- as.data.frame(cbind(AQ_all, AQ_SS, AQ_AS, AQ_AD, AQ_C, AQ_I))
  
# -----------------------------
  
# SPQ: 
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
  print(curr_subscale)
  # get names of all columns that end with the current sub scale name
  curr_columns <- as.vector(names(input_df)[grep("AW", names(input_df))])
  # get subset of df where columns have these names:
  curr_columns <- input_df[curr_columns]
    
  # get only the row where we have values:
  curr_columns <- curr_columns[which(input_df$sender == "SPQ-G"), ]
    
  # now count how many times participant answered "yes" (label = 1)
  curr_subscale_score <- sum(curr_columns)
  print(curr_subscale_score)
    
  # put subscale score into demographics df:
  df_demogr[paste("SQP_", curr_subscale, sep = "")] <- as.numeric(curr_subscale_score)
    
} 
  
# also assign overall score:
df_demogr$SPQ_all <- sum(input_df[which(input_df$sender == "SPQ-G"), 
                                  as.vector(names(input_df)[grep("SPQ", names(input_df))])])
  
  
# -----------------------------
  
### Autism-Spectrum Quotient (AQ)
  
#Baron-Cohen, S., Wheelwright, S., Skinner, R., Martin, J., & Clubley, E. (2001). 
# The autism-spectrum quotient (AQ): Evidence from asperger syndrome/high-functioning autism, 
# males and females, scientists and mathematicians. Journal of autism and developmental disorders, 31(1), 5-17.
  
# First, we have to recode some of the item scores:
# Recode all positive values to 1, recode all negative values to 0:
  
AQ_df <- input_df[which(input_df$sender == "AQ-G"), as.vector(names(input_df)[grep("AQ", names(input_df))])]
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
  

# -----------------------------------
  
# Bring the AQ and SPQ subscale scores together & 
# calculate prediction strategy style score for each participant
  
# get all subscale values
subscale_data <- df_demogr[,c("AQ_SS", "AQ_AS", "AQ_AD", "AQ_C", "AQ_I",
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



