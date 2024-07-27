### Stimulus settings

# set colours you want to use for background:
# light_bg_col_hex = "#FDFBF0" # ivory instructions background
# dark_bg_col_hex  = "#505050" # dark grey background for stimuli
#light_bg_col = [(x / 127.5) - 1 for x in (253, 251, 240)]
light_bg_col = [(x / 127.5) - 1 for x in (186, 186, 186)] # ivory instructions background (use RGB -1:1)
dark_bg_col = [(x / 127.5) - 1 for x in (80, 80, 80)]  # dark grey background for stimuli (use RGB -1:1)

# make background light for a start - use rgb -1:1 colour codes
win.setColor(light_bg_col, colorSpace='rgb')

# set colours you want to use for the stimuli:
colours = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"]
print("Preparing experiment with n-back colours:", colours)

#  #D292F3 = weird lilac with a 2000s vibe
#  #F989A2 = Barbie pink
#  #2AB7EF = Twitter blue
#  #88BA3F = medium grass green
# (#D8A244 = dark curry-ish yellow --> excluded!)

#   All colours have a luminance of 70 and a chroma of 74.

#   The colours are selected for distinguishability (is that a word?!)
#   for people with "normal" colour vision as well as for
#   people with protanomaly (red olour vision deficiency (CVD)),
#   deuteranomaly (green CVD) and
#   tritanomaly (blue CVD).

#   People with a "true" colour blindness
#   (i.e. protanopia, deuteranopia, tritanopia)
#   shouldn't participate in this study. */


# ----------------------------------------------
### Shuffle order of texts
print("shuffle texts")
# collect the text IDs in lists so I know which text was shown
all_main_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04", "text_05", "text_06", "text_07", "text_08",
                           "text_09", "text_10"]
all_pseudotexts_nrs_list = ["pseudo_text_01", "pseudo_text_02", "pseudo_text_03", "pseudo_text_04", "pseudo_text_05",
                            "pseudo_text_06", "pseudo_text_07", "pseudo_text_08", "pseudo_text_09"]
# shuffle text numbers
random.shuffle(all_main_texts_nrs_list)
random.shuffle(all_pseudotexts_nrs_list)

# only get first 5 texts for the main blocks
all_main_texts_nrs_list = all_main_texts_nrs_list[0:5]

# only get first text for pseudotext
all_pseudotexts_nrs_list = all_pseudotexts_nrs_list[0:1]

# append "empty" text numbers to the list where we have blocks that are not main blocks.
all_texts_nrs_list = []

# Loop through the range of the length of texts since it's the longer list
for t_idx in range(len(all_main_texts_nrs_list)):
    # if it's the first text, it's the reading BL main block.
    if t_idx == 0:
        # Append 1 text for baseline reading
        all_texts_nrs_list.append(all_main_texts_nrs_list[t_idx])
        # Then append 1 text for pseudotext plus 4 empty blocks for n-back single task
        all_texts_nrs_list.extend([all_pseudotexts_nrs_list[0], "", "", "", ""])
    elif t_idx >= 1:
        # Then 4 reading blocks for dual task
        all_texts_nrs_list.append(all_main_texts_nrs_list[t_idx])

# This will result in a list following your described logic
print(all_texts_nrs_list)

### Set order of blocks
print("set block order for runs")

# RUN 1
# always starts with single reading (BL + PS)
single_reading = ["Reading_Baseline_main_no_click", "Reading_pseudotext_no_click"]

run1_blocks = single_reading
print("Blocks for run1:", run1_blocks)

# RUN 2
# then you get both single n-back conditions
nback1 = ["1back_single_main_no_click", "2back_single_main_no_click"]
random.shuffle(nback1)

nback2 = ["1back_single_main_no_click", "2back_single_main_no_click"]
random.shuffle(nback2)

run2_blocks = nback1 + nback2
print("Blocks for run2:", run2_blocks)

# RUNS 3, 4, 5 & 6
# one dual-task block per run, order randomized
dual_blocks = ["1back_dual_main_no_click", "2back_dual_main_no_click", "1back_dual_main_no_click", "2back_dual_main_no_click"]

random.shuffle(dual_blocks)

run3_blocks = dual_blocks[0]
run4_blocks = dual_blocks[1]
run5_blocks = dual_blocks[2]
run6_blocks = dual_blocks[3]

print("Blocks for run3:", run3_blocks)
print("Blocks for run4:", run4_blocks)
print("Blocks for run5:", run5_blocks)
print("Blocks for run6:", run6_blocks)

### Create n-back colour lists for all blocks

print("create n-back colour lists")
# There are 10 blocks in total
# For run 1, 6 blocks (2 text blocks + 4 single n-back)
# Run 2 and 3 each have 2 dual-task blocks with 300 stimuli each (50 targets)

# So for every block, build a list with colour codes containing the right amount of targets.
# The function is defined in another script bc it's super long,
# I import it at the beginning of this script.

# RUN 1
# First, create list with length of all texts. The length of the blocks is
# always in the same order, only the conditions change.
blocks_textlen = [300, 100] # reading blocks
blocks_target_counts = [25, 25]  # reading blocks

# Now loop this list. Check which condition we have there and then create colour list for each text.
run1_colour_lists = []
run1_target_lists = []
for block_idx, block_length in enumerate(blocks_textlen):
    # get 1st letter of block name - that tells us the condition
    block_cond = run1_blocks[block_idx][0]

    # for each condition, decide which n-back level we want to assign
    # For all no-n-back blocks, we use 1 (just for the colour list generation)
    # global curr_nback_level
    if block_cond == "R":
        curr_nback_level = 1
    elif block_cond == "1":
        curr_nback_level = 1
    else:
        curr_nback_level = 2

    # generate colour list for current block
    # global curr_colours
    curr_colours = create_nback_stimlist(nback_level=curr_nback_level,
                                         colour_codes=colours,
                                         story=["x"] * block_length,
                                         target_abs_min=blocks_target_counts[block_idx],
                                         target_abs_max=blocks_target_counts[block_idx],
                                         zeroback_target=None)

    # get list of targets / non-targets
    curr_targets = get_targets(stim_list=curr_colours,
                               nback_level=curr_nback_level)

    # add to bigger lists
    run1_colour_lists.append(curr_colours)
    run1_target_lists.append(curr_targets)

# RUN 2
blocks_textlen = [90, 90, 90, 90]  # single n-back blocks
blocks_target_counts = [15, 15, 15, 15]

# Now loop this list. Check which condition we have there and then create colour list for each text.
run2_colour_lists = []
run2_target_lists = []
for block_idx, block_length in enumerate(blocks_textlen):
    # get 1st letter of block name - that tells us the condition
    block_cond = run2_blocks[block_idx][0]

    # for each condition, decide which n-back level we want to assign
    # For all no-n-back blocks, we use 1 (just for the colour list generation)
    # global curr_nback_level
    if block_cond == "R":
        curr_nback_level = 1
    elif block_cond == "1":
        curr_nback_level = 1
    else:
        curr_nback_level = 2

    # generate colour list for current block
    # global curr_colours
    curr_colours = create_nback_stimlist(nback_level=curr_nback_level,
                                         colour_codes=colours,
                                         story=["x"] * block_length,
                                         target_abs_min=blocks_target_counts[block_idx],
                                         target_abs_max=blocks_target_counts[block_idx],
                                         zeroback_target=None)

    # get list of targets / non-targets
    curr_targets = get_targets(stim_list=curr_colours,
                               nback_level=curr_nback_level)

    # add to bigger lists
    run2_colour_lists.append(curr_colours)
    run2_target_lists.append(curr_targets)

# RUNS 3, 4, 5 & 6
blocks_textlen = [300, 300, 300, 300] # dual-task blocks
blocks_target_counts = [50, 50, 50, 50]  # dual-task blocks

# Now loop this list. Check which condition we have there and then create colour list for each text.
dual_blocks = run3_blocks + run4_blocks + run5_blocks + run6_blocks
run3_4_5_6_colour_lists = []
run3_4_5_6_target_lists = []
for block_idx, block_length in enumerate(blocks_textlen):
    # get 1st letter of block name - that tells us the condition
    block_cond = dual_blocks[block_idx][0]

    # for each condition, decide which n-back level we want to assign
    # For all no-n-back blocks, we use 1 (just for the colour list generation)
    # global curr_nback_level
    if block_cond == "R":
        curr_nback_level = 1
    elif block_cond == "1":
        curr_nback_level = 1
    else:
        curr_nback_level = 2

    # generate colour list for current block
    # global curr_colours
    curr_colours = create_nback_stimlist(nback_level=curr_nback_level,
                                         colour_codes=colours,
                                         story=["x"] * block_length,
                                         target_abs_min=blocks_target_counts[block_idx],
                                         target_abs_max=blocks_target_counts[block_idx],
                                         zeroback_target=None)

    # get list of targets / non-targets
    curr_targets = get_targets(stim_list=curr_colours,
                               nback_level=curr_nback_level)

    # add to bigger lists
    run3_4_5_6_colour_lists.append(curr_colours)
    run3_4_5_6_target_lists.append(curr_targets)

run3_colour_lists = run3_4_5_6_colour_lists[0]
run4_colour_lists = run3_4_5_6_colour_lists[1]
run5_colour_lists = run3_4_5_6_colour_lists[2]
run6_colour_lists = run3_4_5_6_colour_lists[3]

run3_target_lists = run3_4_5_6_target_lists[0]
run4_target_lists = run3_4_5_6_target_lists[1]
run5_target_lists = run3_4_5_6_target_lists[2]
run6_target_lists = run3_4_5_6_target_lists[3]

print("------ finished preparing stimuli! ------")

# ------------------------------------------

# init block counter for the whole experiment and for each run
exp_block_counter = 0
# init block counter for run1 (two blocks in total)
run1_block_counter = 0
# init block counter for run2 (four blocks in total)
run2_block_counter = 0
# init block counter for run3 (one block in total)
run3_block_counter = 0
# init block counter for run4 (one block in total)
run4_block_counter = 0
# init block counter for run5 (one block in total)
run5_block_counter = 0
# init block counter for run6 (one block in total)
run6_block_counter = 0

print("starting experiment now!")