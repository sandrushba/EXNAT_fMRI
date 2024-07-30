### Stimulus settings
import random

# measure frame rate (in Hz)
# frame_rate = win.getActualFrameRate() # frame rate in Hz
# print("measured frame rate:", frame_rate, "Hz")
# set flicker frequency (in Hz)
# flicker_freq = frame_rate/4 # 60/4 = 15 Hz

# set colours you want to use for background:
# light_bg_col_hex = "#FDFBF0" # ivory instructions background
# dark_bg_col_hex  = "#505050" # dark grey background for stimuli
light_bg_col = [(x / 127.5) - 1 for x in (253, 251, 240)]  # ivory instructions background (use RGB -1:1)
dark_bg_col = [(x / 127.5) - 1 for x in (80, 80, 80)]  # dark grey background for stimuli (use RGB -1:1)

# for timing test:
# dark_bg_col = [(x / 127.5) - 1 for x in (255, 255, 255)]

# make background light for a start - use rgb -1:1 colour codes
win.setColor(light_bg_col, colorSpace='rgb')

# set colours you want to use for the stimuli:
colours = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"]
print("Preparing experiment with n-back colours:", colours)
# for timing test:
# colours = ["#000000", "#F989A2", "#2AB7EF", "#88BA3F"]

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
all_main_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04", "text_05", "text_06", "text_07", "text_08"]
# shuffle text numbers
random.shuffle(all_main_texts_nrs_list)

# only get first 9 texts for the main blocks, the last one will be used for the vis task:
# vis_task_text_nr = all_main_texts_nrs_list[-1]
# all_main_texts_nrs_list = all_main_texts_nrs_list[0:-1]

# append "empty" text numbers to the list where we have blocks that are not main blocks.
all_texts_nrs_list = []

for t_idx, t in enumerate(all_main_texts_nrs_list):
    # if it's the first text, it's the reading BL main block.
    if t_idx == 0:
        all_texts_nrs_list = all_texts_nrs_list + ["", t, ""]
    elif t_idx == 1:
        all_texts_nrs_list = all_texts_nrs_list + [t, "", "", ""]
    # one text for 0back dual block with click, one text for 0-back no click
    elif t_idx == 2:
        all_texts_nrs_list = all_texts_nrs_list + [t, "", "", ""]
    # append one text for self-paced dual block 0-back,
    # then two empty blocks for n-back training, then two blocks for single n-back blocks (self-paced and paced)
    elif t_idx == 3:
        all_texts_nrs_list = all_texts_nrs_list + [t, ""]
    # one text for paced dual block, then again four empty blocks for other n-back condition
    elif t_idx == 4:
        all_texts_nrs_list = all_texts_nrs_list + [t]
    elif t_idx == 5:
        all_texts_nrs_list = all_texts_nrs_list + [t, ""]
    elif t_idx == 6:
        all_texts_nrs_list = all_texts_nrs_list + [t, ""]
    elif t_idx > 6:
        [t]
    # then finally append rest of texts (two texts)

        all_texts_nrs_list.append(t)

print(all_texts_nrs_list)

### Set order of blocks
# Currently 20 blocks in total
print("set block order")

# this always comes first in the experiment
blocks_click = ["Reading_Baseline_training_click", "Reading_Baseline_main_click", "0back_single_training",
                "0back_dual_main_click", "1back_single_training1", "1back_single_training2", "1back_single_main",
                "1back_dual_main_click", "2back_single_training1", "2back_single_training2", "2back_single_main",
                "2back_dual_main_click"]
reading_no_click = ["Reading_Baseline_training_no_click", "Reading_Baseline_main_no_click", "0back_dual_main_no_click"]

# then you get both n-back conditions with trainings (which of them is first is randomized)
oneback = ["1back_single_main_no_click", "1back_dual_main_no_click"]
twoback = ["2back_single_main_no_click", "2back_dual_main_no_click"]

# shuffle the order of the 2 lists
blocks_no_click = [oneback, twoback]
random.shuffle(blocks_no_click)

# flatten nested list
main_blocks = flatten_list(blocks_no_click)

pseudo_block = ["Reading_pseudotext_no_click"]

# put them all together:
# global all_blocks
all_blocks = blocks_click + reading_no_click + blocks_no_click + pseudo_block
all_blocks = flatten_list(all_blocks)
print(all_blocks)

### Create n-back colour lists for all blocks

print("create n-back colour lists")
# The reading bl training text has 55 trials.
# the reading bl main has 91 words
# reading training no click has 58 words
# then main reading bl no click with 91 words
# then 0-back short training with 20 trials
# then 0-back dual self-paced and paced block with 91 trials and 15 targets each

# Then we have 2 short training blocks à 20 trials each (5 targets) for n-back
# then two single n-back blocks with 90 trials each (15 targets)
# then two dual blocks with 91 trials each (15 targets)
# then again two short training blocks, two single n-back blocks with 90 trials each (15 targets), and two dual blocks with 91 trials (15 targets)
# and finally, one pseudotext block

# --> all in all, 20 blocks

# So for every block, build a list with colour codes containing the right amount of targets.
blocks_textlen = [60, 91, 20, 91,
                  20, 20, 90, 91,
                  20, 20, 90, 91,
                  60, 91, 91, 90, 91, 90, 91,
                  100]
blocks_target_counts = [15, 15, 5, 15,
                        5, 5, 15, 15,
                        5, 5, 15, 15,
                        15, 15, 15, 15,
                        15, 15, 15, 15]
# Now loop this list. Check which condition we have there and the create colour list for each text.
all_colour_lists = []
all_target_lists = []
target_colours_list = []
# target_colour = np.random.choice(colours)
for block_idx, block_length in enumerate(blocks_textlen):
    # get 1st letter of block name - that tells us the condition
    block_cond = all_blocks[block_idx][0]

    # for each condition, decide which n-back level we want to assign
    # For all no-n-back blocks, we use 1 (just for the colour list generation)
    # global curr_nback_level
    if block_cond == "R":
        curr_nback_level = 1
    elif block_cond == "0":
        curr_nback_level = 0
    elif block_cond == "1":
        curr_nback_level = 1
    else:
        curr_nback_level = 2

    # generate colour list for current block
    if curr_nback_level == 0:
        # generate random colour list for 0-back:
        # Filter out the colours that have already been used as target colours
        available_colours = [colour for colour in colours if colour not in target_colours_list]

        # Shuffle the available colours to randomize the selection
        random.shuffle(available_colours)

        # Select the first colour from the shuffled available colours as the target colour
        target_colour = available_colours[0]

        print("curr target colour:", target_colour)
        curr_colours = create_0back_stimlist(target_colour=target_colour,
                                             nr_targets=blocks_target_counts[block_idx],
                                             colour_codes=colours,
                                             nr_words=blocks_textlen[block_idx])
        # Get list of targets / non-targets
        curr_targets = [colour == target_colour for colour in curr_colours]

        # Add the selected target colour to the list of target colours
        target_colours_list.append(target_colour)

    elif curr_nback_level in [1, 2]:
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
    all_colour_lists.append(curr_colours)
    all_target_lists.append(curr_targets)

print("------ finished preparing stimuli! ------")

# ------------------------------------------

# init block counter for the whole experiment
exp_block_counter = 0

print("starting experiment now!")