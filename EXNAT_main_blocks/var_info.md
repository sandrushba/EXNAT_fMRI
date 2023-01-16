
# List of "important" variables in my experimental scripts and what they contain


## Instructions:
--> defined in code component "set_texts" in routine "nback_instr"

notice_reading_bl_training = instructions for the reading baseline training
notice_reading_bl_main = instructions for the reading baseline main

notice_1back_training_singletask: instructions for 1-back training single-task (only 1-back)
notice_2back_training_singletask: instructions for 2-back training single-task (only 2-back)
notice_3back_training_singletask: instructions for 3-back training single-task (only 3-back)

notice_1back_training_dualtask: instructions for 1-back training dual-task (reading + 1-back)
notice_2back_training_dualtask: instructions for 2-back training dual-task (reading + 2-back)
notice_3back_training_dualtask: instructions for 3-back training dual-task (reading + 3-back)

notice_1back_main: instructions for 1-back main dual-task (reading + 1-back)
notice_2back_main: instructions for 2-back main dual-task (reading + 2-back)
notice_3back_main: instructions for 3-back main dual-task (reading + 3-back)


## n-back Settings
--> defined in code component "set_texts" in routine "nback_instr"

### colours used in the experiment
colour_codes: list of unique colour codes used in the experiment

### number of targets in training and main blocks
training_target_abs_min: min absolute number of targets in training blocks
training_targets_max: max relative number of targets in training blocks
training_targets_min: min relative number of targets in training blocks

main_target_abs_min: min absolute number of targets in main blocks
main_targets_max: max relative number of targets in main blocks
main_targets_min: min relative number of targets in main blocks

### order of n-back conditions
nback_main_blocks: list of main n-back conditions (without reading baseline!) and their order in the experiment
nback_order: list of n-back conditions and their order in the experiment ("no" always first block, then "1", "2" and "3" in random order, only 4 values in total)

### stimulus lists
all_colours: list of colours for each trial in the experiment; "!END!" after each block; "!END_ALL!" after last "!END!" tag

all_nback_conditions: list of n-back condition for each trial in the experiment; "!END!" after each block; "!END_ALL!" after last "!END!" tag

all_block_nr: list of block numbers for each trial in the experiment; "!END!" after each block; "!END_ALL!" after last "!END!" tag

all_block_kind: list of block names ("reading_baseline", "training" or "main") for each trial in the experiment; "!END!" after each block; "!END_ALL!" after last "!END!" tag


all_targets = list of targets (True or False) for each trial in the experiment; "!END!" after each block; "!END_ALL!" after last "!END!" tag

all_words = list of words for each trial in the experiment; "!END!" after each block; "!END_ALL!" after last "!END!" tag

all_text_numbers = list of text numbers (format: "1_01") for each trial in the experiment; "!END!" after each block; "!END_ALL!" after last "!END!" tag


## Counters
--> defined in code component "set_texts" in routine "nback_instr"

exp_trial_counter = counter for the trials, starts at 0

exp_block_counter = counter for the blocks, starts at 0
