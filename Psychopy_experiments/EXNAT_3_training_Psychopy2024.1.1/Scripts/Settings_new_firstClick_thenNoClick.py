### Stimulus settings
import random
import re

# set colours you want to use for background:
# light_bg_col_hex = "#FDFBF0" # ivory instructions background
# dark_bg_col_hex  = "#505050" # dark grey background for stimuli
light_bg_col = [(x / 127.5) - 1 for x in (253, 251, 240)]  # ivory instructions background (use RGB -1:1)
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
all_main_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04"]
# shuffle text numbers
random.shuffle(all_main_texts_nrs_list)

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
    # elif t_idx == 4:
    #     all_texts_nrs_list = all_texts_nrs_list + [t]
    # elif t_idx == 5:
    #     all_texts_nrs_list = all_texts_nrs_list + [t, ""]
    # elif t_idx == 6:
    #     all_texts_nrs_list = all_texts_nrs_list + [t, ""]
    # elif t_idx > 6:
    #     [t]
    # then finally append rest of texts (two texts)

    #    all_texts_nrs_list.append(t)

# print(all_texts_nrs_list)

short_texts = ["text_05", "text_06", "text_07", "text_08"]
random.shuffle(short_texts)

all_short_texts_nrs_list = []

for t_idx, t in enumerate(short_texts):
    # if it's the first text, it's the reading BL main block.
    if t_idx == 0:
        all_short_texts_nrs_list = all_short_texts_nrs_list + [t]
    elif t_idx == 1:
        all_short_texts_nrs_list = all_short_texts_nrs_list + [t, ""]
    # one text for 0back dual block with click, one text for 0-back no click
    elif t_idx == 2:
        all_short_texts_nrs_list = all_short_texts_nrs_list + [t, ""]
    # append one text for self-paced dual block 0-back,
    # then two empty blocks for n-back training, then two blocks for single n-back blocks (self-paced and paced)
    elif t_idx == 3:
        all_short_texts_nrs_list = all_short_texts_nrs_list + [t, ""]

# print(all_short_texts_nrs_list)

all_texts_nrs_list = all_texts_nrs_list, all_short_texts_nrs_list
all_texts_nrs_list = flatten_list(all_texts_nrs_list)
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
# The reading bl training text has 30 trials.
# the reading bl main has 91 words
# then 0-back training with 20 trials
# then 0-back dual self-paced and paced block with 91 trials and 15 targets each
# Then we have 2 short training blocks à 20 trials each (5 targets) for n-back
# then two single n-back blocks with 60 trials each (15 targets)
# then two dual blocks with 91 trials each (15 targets)
# then we repeat everything in the paced version; except that blocks are much shorter
# --> all in all, 20 blocks

# So for every block, build a list with colour codes containing the right amount of targets.
# this is the old set-up with all texts in the same length
# blocks_textlen = [60, 91, 20, 91,
#                   20, 20, 90, 91,
#                   20, 20, 90, 91,
#                   60, 91, 91, 90, 91, 90, 91,
#                   100]
# alternative, shorter:
# Schachnovelle training texts: each 30 words
# pseudotext: 30 words
# dual task blocks:
# single n-back blocks: 60 trials
# bl = 30*1.5 + 30*1.5 + 91*1.5 + 91*1.5
# ps = 60*1.5
# single_nback = 2*60*1.5 + 2*60*2 + 40*1.5 + 40*2
# dual = 2*91*2 + 2*91*2.5
# sum = (bl + ps + single_nback + dual)/60

blocks_textlen = [30, 91, 20, 91,
                  20, 20, 60, 91,
                  20, 20, 60, 91,
                  30, 30, 30, 40,
                  30, 40, 30, 30]

blocks_target_counts = [5, 15, 5, 15,
                        5, 5, 10, 15,
                        5, 5, 10, 15,
                        5, 15, 15, 6,
                        15, 6, 15, 5]
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
# exp_block_counter = 0

# There is the option to skip the demographics part and the self-paced block if for instance the experiment crashed in the middle or the participant needs to repeat the paced blocks
# In this case, the RTs per condition are entered and the experiment directly starts with the paced blocks
if expInfo['self-paced_blocks'] == "yes":
    exp_block_counter = 0
elif expInfo['self-paced_blocks'] == "no":
    exp_block_counter = 12

    # Define the form items
    info = {
        'RT_per_letter_baseline': '',
        'RT_per_letter_0back': '',
        'RT_per_letter_1bck': '',
        'RT_per_letter_2bck': '',
        'RT_per_rect_1back_single': '',
        'RT_per_rect_2back_single': ''
    }

    # Create the dialog
    dlg = gui.DlgFromDict(dictionary=info, title='User Information')

    # Check if the user pressed OK
    if dlg.OK:
        RT_per_letter_baseline = int(info['RT_per_letter_baseline'])
        RT_per_letter_0back = int(info['RT_per_letter_0back'])
        RT_per_letter_1bck = int(info['RT_per_letter_1bck'])
        RT_per_letter_2bck = int(info['RT_per_letter_2bck'])
        RT_per_rectangle_oneback_single = int(info['RT_per_rect_1back_single'])
        RT_per_rectangle_twoback_single = int(info['RT_per_rect_2back_single'])
        print(f'RT_per_letter_baseline: {RT_per_letter_baseline},\nRT_per_letter_0back: {RT_per_letter_0back},\n'
              f'RT_per_letter_1bck: {RT_per_letter_1bck},\nRT_per_letter_2bck: {RT_per_letter_2bck},\n'
              f'RT_per_rect_1back_single: {RT_per_rectangle_oneback_single},\nRT_per_rect_2back_single: {RT_per_rectangle_twoback_single}')
    else:
        core.quit()

print("starting experiment now!")