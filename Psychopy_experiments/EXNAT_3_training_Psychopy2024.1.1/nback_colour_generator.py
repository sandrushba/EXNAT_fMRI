######################################################################
#                                                                    #
#      Colour List Generator Function for n-back tasks               #
#                                                                    #    
######################################################################


# Author: Merle Schuckart
# Version: 1.0 (09.03.2023)



''' ---- Settings ----------------------------------------'''

import numpy as np
import random
import math as Math



''' ---- 1st Function: draw w/o replacement with sample size > sampling list ----------'''

def draw_without_replacement(sampling_list, sample_size):
    
    """
    draw w/o replacement, start over again if you run out of
    values, then shuffle your sample draw without replacement 
    from list with sample size > list start over again if no values 
    left for drawing, shuffle everything in the end

    Parameters:
    sampling_list (list): The list of objects you want to sample from
    sample_size (int): The number of samples you want to draw
    
    Returns:
    A list of samples of length sample_size
    
    """


    # repeat colour_codes_list as often as needed
    rep_times = Math.floor(sample_size / len(sampling_list))
    rep_sampling_list = sampling_list * rep_times

    # check if we need some more values, if yes, draw some randomly
    # from colour_codes and append to our list
    if len(rep_sampling_list) < sample_size:
        rep_sampling_list = rep_sampling_list + random.sample(sampling_list, sample_size - len(rep_sampling_list))

    # shuffle everything
    random.shuffle(rep_sampling_list)
    
    # return finished sample
    return rep_sampling_list




''' ---- 2nd Function: generate n-back colour list with given target number ----------'''


def create_nback_stimlist(nback_level, colour_codes, story, target_abs_min, target_abs_max, zeroback_target = None):
  

  """
  Create pseudorandomized list of colour codes
  Idea: generate small random lists of colour codes with a balanced number of 
  colours, then append them so I get an even distribution of colour codes & 
  even numbers of colour codes over the whole block.

  Parameters:
  nback_level (int): Which n-back level to use (e.g. 1 or 2)
  colour_codes (list): The colour codes you want to use
  story (list): A list of words you want to generate colours for
  target_abs_min (int): How many targets do you want at least (absolute number, not percentage)
  target_abs_max (int): How many targets do you want at most (absolute number, not percentage)
  zeroback_target (str): Which colour code do you want to use as a 0-back target? (Default for all other n-backs: None)

  Returns:
  A list of colours of the same length as story
    
  """


  # chunk size should be number of distinct stimuli x 3, so there can't be more than 6x the same stimulus in a row if we concatenate 2 chunks
  chunk_size = len(colour_codes) * 3
  # given the chunk size and the number of stimuli we need, how many chunks do we need?
  chunk_nr = int(len(story) / chunk_size)
  # check if there are still stimuli missing that we have to add at the end
  chunk_missing = len(story) - chunk_size * chunk_nr

  # placeholder for the colour list we want to create
  random_colour_list = []

  # loop whole chunks, generate small stim list, append the lists
  for chunk in range(0, chunk_nr):
      rep_colours = draw_without_replacement(sampling_list = colour_codes, sample_size = chunk_size)
      random_colour_list = random_colour_list + rep_colours

  # if there are not enough values, randomly sample some and add them
  # to the end of the colour list
  if chunk_missing > 0:
    missing_chunk = draw_without_replacement(sampling_list = colour_codes, sample_size = chunk_missing)
    random_colour_list = random_colour_list + missing_chunk

  #print("random colour list: ", random_colour_list)

  # count how many targets there are (using the given n-back level
  # create an empty array for collecting the info on targets / non-targets:
  target = []

  # loop colours
  for col_idx in range(0, len(random_colour_list)):
     
    # get current colour
    colour = random_colour_list[col_idx]
    
    # get colour from n trials before (1 for 1-back, 2 for 2-back)
    nback_number = nback_level

    # check if it's the beginning of the array - if the trial is
    # the first one (for the 1-back) or the first or second one (for the 2-back),
    # the colour can't be a target because there were not enough colours before.

    # if the trial is < our n-back level
    if col_idx < nback_number:
      # save target as false
      curr_target = False
    # if it's one of the following trials, check if we have a match
    else:
      # get colour from n trials back
      previous_colour = random_colour_list[col_idx - nback_number]

      # check if colour matches the one n trials before
      # if they match, save target as true
      if colour == previous_colour:
        curr_target = True
      # if it's not, save target as false
      else:
        curr_target = False
   
    # add target to bigger target list
    target.append(curr_target)

  

  # check if it worked:
  target_count = 0;
  for i in range(0, len(target)):
      if target[i] == True:
          target_count = target_count + 1

  #print("nr of targets in random colour list:", target_count)


  # if we have more targets than min. targets and less than max. targets,
  # everything's fine:
  if target_count >= target_abs_min and target_count <= target_abs_max:
    target_nr = target_count
    #print("target count is correct! We have", target_count,
          # "targets and we needed at least", target_abs_min,
          # "and at most", target_abs_max, "targets")

  # if our target count is not in the correct range...
  else:
    # if we don't have enough targets or too many targets...
    if target_count < target_abs_min or target_count > target_abs_max:
        ##print("target count is not correct. There are", target_count, "targets currently." )

        # randomly draw a target number to use for adding/taking away targets
        target_nr = round(random.uniform(target_abs_min, target_abs_max))
        
        #print("adding/removing", target_nr - target_count, "targets now.")

        # MISSING TARGETS:
		# --> turn non-target trials into target trials to reach the desired number of targets

        # if there are targets missing (aka if the number of targets
        # we have is smaller than the number of targets we need):
        if target_count - target_nr < 0:
            # check how many are missing
            nr_replacements = abs(target_count - target_nr)
            # print("Targets missing, adding", nr_replacements, "targets")
        
            # get indices of all false values in target list
            indices_targets = []
            for t in range(len(target)):
                if target[t] == False:
                    indices_targets.extend([t])

            # Now it gets a little complicated: We want to add targets by replacing non-targets, but
            # we don't want to turn other targets into non-targets by taking away their match.
            # Here's a 1-back example (imagine we're replacing the one in the brackets with "green"):
            # red - green - [yellow] - yellow
    
            # Solution: find out where we have non-targets followed by non-targets
            # also the follower-colour should not match the one before:
    
            # Example: by replacing "green" by "yellow", we would create not
            # only 1 but 2 new 1-back targets:
            # red - yellow - [green] - yellow
    
            # Idea: get the colour list and find the indices of all colours that...
            # a) are non-targets and...
            # b) don't match the colour of the nth next trial.
            # example for 1-back: current colour shouldn't match the one at idx + 1
            # example for 1-back: current colour shouldn't match the one at idx + 2
    
    		# for each index, check if colour of index before and next index match
            # if they don't match, save index because we can replace
            # that colour without getting double targets.
    
            # create placeholder for all replacement indices and replacement colours
            idx_replacements = []
            replacement_colours = []
            
            # loop list of indices with non-targets
            for nontarget_idx in indices_targets:

              # Explanation of the following if-conditions:
                  
    		  # 1. We can only put targets into the array where we have enough predecessor values.
              # So make sure not to start at idx = 0         
              # --> nontarget_idx > nback_level
              
              # 2. We always get the current colour and the colour at idx + n-back level, so make sure we are not at the end of the colour list already:
              # --> nontarget_idx + nback_level < len(random_colour_list)
                  
              # 3. Also the next non-target we could replace with a target shouldn't be too close to
              # the last one or we mess things up again if we change them. So make sure they're a few trials apart.
              # --> nontarget_idx >= (idx_replacements[-1] + nback_level + 2)
    
              # 4. If we have not saved any replacement colours yet that we compare with the current colour, we can also proceed.
              # This condition has to come before the one I explained before because if idx_replacements is empty, we 
              # cannot check idx_replacements[-1]
              # --> len(idx_replacements) == 0
              
              
              if nontarget_idx > nback_level and (nontarget_idx + nback_level < len(random_colour_list)) and (len(idx_replacements) == 0 or nontarget_idx >= (idx_replacements[-1] + nback_level + 2)):
             

                # check if colour of current idx and next possible match (idx + nback level) match
                # reason: We don't want to remove targets, so don't change this
                # if it's the target colour for another trial
                colours_match1 = random_colour_list[nontarget_idx] == random_colour_list[nontarget_idx + nback_level]

                # we also need to check if the colour n trials before is the same as the one n trials after the current trial
                # reason:
                # if we have this situation (1-back): red yellow red
                # we can't turn yellow into red to create a target because then the next trial would also turn into a target trial.
                colours_match2 = random_colour_list[nontarget_idx + nback_level] == random_colour_list[nontarget_idx - nback_level]
                # if the colours don't match, we can replace the
                # colour without messing everything up.
    
                # we also need to check if there are any values left after the
                # index or we'll get problems with indexing
                if colours_match1 == False and colours_match2 == False and (nontarget_idx + nback_level) <= len(random_colour_list)-1:
                  # get colour at idx - nback level, so we know which colour we need to create a target
                  # for the current trial:
                  replacement_col = random_colour_list[nontarget_idx - nback_level]

                  # save index and replacement colour in array for later use:
                  idx_replacements.append(nontarget_idx)
                  replacement_colours.append(replacement_col)
                  #print(replacement_col, nontarget_idx)
                  

            # now we need to draw from this list of possible replacements as many indices/colours
            # as we need to make up for the missing targets.
    
            # if for some reason there are less replacement colours than we need, use recursion
            if (len(replacement_colours) < target_nr - target_count):
                #print("did not find enough replacement colours")
                #print("-------------- recursion -------------")
                return create_nback_stimlist(nback_level, colour_codes, story, target_abs_min, target_abs_max, zeroback_target = None)

            # if everything's fine, go on: 
                
            # shuffle arrays with indices and colours
    
            # use a seed, but it's okay if it's always the same seed
            # we use 42 because it's the answer to the "Ultimate Question of Life,
            # the Universe, and Everything", but you knew that because
            # if you're reading this you're a nerd (no offense, honey).
            seed = 42            
            random.Random(seed).shuffle(idx_replacements)
            random.Random(seed).shuffle(replacement_colours)
     
            # take the first x values from both as replacements for non-targets
            idx_replacements    = idx_replacements[ :target_nr - target_count]
            replacement_colours = replacement_colours[ :target_nr - target_count]
            

            # replace colours and "false"s in target array with colours / "true"s at the chosen indices:
            # loop the replacements
            for repl_idx in range(target_nr - target_count):

                # Replace the values in the original colour and target lists             
                random_colour_list[idx_replacements[repl_idx]] = replacement_colours[repl_idx]
 

        # TOO MANY TARGETS:

        # too many targets, get rid of some
        else:

            if target_count - target_nr > 0:
                nr_replacements = abs(target_count - target_nr)
                #print("Too many targets, replacing ", nr_replacements, "targets by non-targets")

                # find indices of targets we could get rid of
                indices_targets = [t for t, x in enumerate(target) if x]

                # get random indices of some of those targets (as many as we need to replace)
                idx_replacements = random.sample(indices_targets, k = nr_replacements)

                # replace target by non-target colour (aka colour that doesn't match
                # target colour from n trials before or current colour
                for replace_this_colour in idx_replacements:

                    # if we haven't reached the end of the colour array yet, we have to make sure
                    # the new colour doesn't match the one n trials after, so we don't create more
                    # targets by accident.
                    if len(random_colour_list) - 1 >= replace_this_colour + nback_level:

                      # select colour you DON'T want to use:
                      not_this_colour = random_colour_list[replace_this_colour + nback_level]
                      
                      # and we also don't want to replace the current colour with itself, so
                      # keep current colour in mind, too:
                      curr_colour = random_colour_list[replace_this_colour]
        
                      colour_codes_replacements = colour_codes.copy()
        
                      # filter out the colours we don't want:
                      colour_codes_replacements = list(filter(lambda e: e != not_this_colour, colour_codes_replacements))
                      colour_codes_replacements = list(filter(lambda e: e != curr_colour, colour_codes_replacements))
           
                      # get random colour from suitable replacement colours
                      replacement_colour = random.sample(colour_codes_replacements, k = 1)[0]



                    # if it's the end of the array anyway and we can't mess anything up, just
                    # use random replacement colour that isn't current colour:
                    else:                        
                        colour_codes_replacements = colour_codes.copy()
                        curr_colour = random_colour_list[replace_this_colour]
                        colour_codes_replacements = [e for e in colour_codes_replacements if e != curr_colour]
                        replacement_colour = random.sample(colour_codes_replacements, k = 1)[0]

                    # actually replace colours               
                    random_colour_list[replace_this_colour] = replacement_colour
                    target[replace_this_colour] = False


        # count targets again:
        # create an empty array for collecting the info on targets / non-targets:
        target = []

        # loop colours, get colour and index of colour
        for col_idx, colour in enumerate(random_colour_list):

            # get colour from n trials before (1 for 1-back, 2 for 2-back)
            nback_number = nback_level

            # check if it's the beginning of the array - if the trial is
            # the first one (for the 1-back) or the first or second one (for the 2-back),
            # the colour can't be a target because there were not enough colours before.

            # if the trial is < our n-back level
            if col_idx < nback_number:
                # save target as false
                curr_target = False

            # if it's one of the following trials, check if we have a match
            else:
                # get colour from n trials back
                previous_colour = random_colour_list[col_idx - nback_number]

                # check if colour matches the one n trials before
                # if they match, save target as true
                if colour == previous_colour:
                    curr_target = True
                # if it's not, save target as false
                else:
                    curr_target = False


            # add target to bigger target list
            target.append(curr_target)

  
        # check if it worked:
        target_count = 0
        for i in range(len(target)):
            if target[i] == True:
                target_count = target_count + 1

  
        #print("nr of targets after replacements:", target_count)


        # weird stuff is happening and I'm losing my patience with this:
        # sometimes, the target counts are not correct after the replacements.
        # So do recursion if the target count is still not correct and hope it fixes the problem.
        # Yes I know this is a horrible solution and the runtime gets
        # even more awful, but who cares. Certainly not me.

        if target_count != target_nr:

            #print("current target number is", target_count, "but should be", target_nr)
            #print("-------------- recursion -------------")
            # recursion: generate new colour list
            return create_nback_stimlist(nback_level, colour_codes, story, target_abs_min, target_abs_max, zeroback_target = None)

        
  # If everything is looking good, we can run some checks on the distribution of the
  # colours and then return the colour list if everything's fine
   
  # check if colour transition probabilities are more or less evenly distributed

  pairs = []
  pairs_counter = []
   
  for idx in range(len(random_colour_list) - 1):
       curr_colour = random_colour_list[idx] + " -> " + random_colour_list[idx + 1]
   
       if curr_colour in pairs:
           idx_pair = pairs.index(curr_colour)
           pairs_counter[idx_pair] += 1

       else:
           pairs.append(curr_colour)
           pairs_counter.append(1)


  change_prob_cutoff_lower = np.mean(pairs_counter) - 2 * np.std(pairs_counter)
  change_prob_cutoff_upper = np.mean(pairs_counter) + 2 * np.std(pairs_counter)
  min_change_prob          = np.min(pairs_counter)
  max_change_prob          = np.max(pairs_counter)

  if min_change_prob < change_prob_cutoff_lower or max_change_prob > change_prob_cutoff_upper:
       change_prob_equal = False
  else:
       change_prob_equal = True


  # now also check if some colours are more often targets than others:
  target_colours = []
  target_colours_counter = []

  for t in range(len(target)):
     if target[t] == True:
         target_colour = random_colour_list[t]
   
         if target_colour in target_colours:
           idx_target_colour = target_colours.index(target_colour)
           target_colours_counter[idx_target_colour] += 1
         else:
           target_colours.append(target_colour)
           target_colours_counter.append(1)

   
  target_prob_cutoff_lower = np.mean(target_colours_counter) - 2 * np.std(target_colours_counter)
  target_prob_cutoff_upper = np.mean(target_colours_counter) + 2 * np.std(target_colours_counter)
  min_target_prob          = np.min(target_colours_counter)
  max_target_prob          = np.max(target_colours_counter)
   
  if min_target_prob < target_prob_cutoff_lower or max_target_prob > target_prob_cutoff_upper:
       target_colours_equal = False
  else:
       target_colours_equal = True
   
   
  # if everything's fine...
  if target_colours_equal and change_prob_equal:
       # return colour list:
       #print("current target number is", target_count, "and should be", target_nr, "- all fine!")
       #print("returning colour list")
       return random_colour_list
   
  # if change probabilities or distribution of target colours is not balanced...
  else:
       # recursion: generate new colour list
       #print("distribution of target colours & change probabilities were a little off")
       #print("-------------- recursion -------------")
       return create_nback_stimlist(nback_level, colour_codes, story, target_abs_min, target_abs_max, zeroback_target = None)




''' ---- 3rd Function: Create stimulus list for 0-back ----------'''

def create_0back_stimlist(target_colour, nr_targets, colour_codes, nr_words):

  """
  Create pseudorandomized list of colour codes
  Idea: generate small random lists of colour codes with a balanced number of 
  colours, then append them so I get an even distribution of colour codes & 
  even numbers of colour codes over the whole block.

  Parameters:
  target_colour (str): Which colour code to use as the 0-back target colour
  nr_targets (int): How many 0-back targets do you want?
  colour_codes (list): The colour codes you want to use, default: ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"] 
  nr_words = 300 (int): How many colours do you want to generate? Should equal the nr of words in your text.
    
  Returns:
  A list of colours of length nr_words
      
  """
  

  # count how often a colour was drawn in succession, 
  # shouldn't be more than 6x
  # targets shouldn't occur more than 2x in a row
  consecutive_count = 0
  # store previous colour
  prev_color = ""

  # how many non-targets do we need?
  sequence_length = nr_words - nr_targets

  # get colour codes for the non-targets
  non_target_colours = [colour for colour in colour_codes if colour != target_colour]
  #print(non_target_colours)

  # Calculate the number of occurrences for each non-target color:
  non_target_color_count = sequence_length // len(non_target_colours)
  #print("non_target_color_count", non_target_color_count)
    
  nr_remaining = sequence_length - non_target_color_count*len(non_target_colours)
  #print("nr_remaining", nr_remaining)

  # create color sequence list
  colour_sequence = []

  # generate sequence of random non-target colours, 
  # make sure not to use 6x the same colour in succession though
  count_consecutive = 0
  last_col = ""


  for x in range(nr_words):
    #print(x)

    # randomly sprinkle in a target if we have some left:
    if random.choices([0, 1], [5, 1])[0] == 1 and colour_sequence.count(target_colour) < nr_targets:
      #print("TARGET")
      next_col = [target_colour]
      count_consecutive = 0

    else:
      # check if/which colours are still available
      if len(non_target_colours) == 0:
        if colour_sequence.count(target_colour) < nr_targets:
          #print("TARGET (because other colours are used up)")
          next_col = [target_colour]
          count_consecutive = 0
        else:
          break
      for col in non_target_colours:
        # count occurences of colour in sequence
        # if we have already reached the number of occurences we 
        # need for each colour, remove it from the list of non-target colours
        if colour_sequence.count(col) == non_target_color_count:
          #print("remove non-target colour")
          non_target_colours.remove(col)

      # generate next colour:
        
      if len(non_target_colours) == 0:  
        if colour_sequence.count(target_colour) < nr_targets:
          #print("TARGET (because other colours are used up)")
          next_col = [target_colour]
          count_consecutive = 0
        else: break
      else:
        # if it doesn't matter which colour we choose,
        # use any colour as the next one
        if count_consecutive < 6:
          # get random colour
          #print("get any non-target colour")
          #print(non_target_colours)
          next_col = random.sample(non_target_colours, 1)
          # if the colour we chose is the same as the one 
          # before, add 1 to count_consecutive
          if next_col == last_col:
            count_consecutive = count_consecutive + 1
          # if it's a different colour, reset counter
          else: 
            count_consecutive = 0

        # if the same colour occurred at least 6x in 
        # succession before, use a different colour
        else: 
          #print("use different non-target colour than before")
          available_colors = [colour for colour in non_target_colours if colour != last_col]
          #print(available_colors)
          next_col = random.sample(available_colors, 1)
          # reset counter
          count_consecutive = 0

    # append next_col to sequence & save as new last_col
    #print(next_col)
    colour_sequence.extend(next_col)
    #print(len(colour_sequence))
    #print("-----------")
    last_col = next_col 

  #print(len(colour_sequence)) # nailed it!
  # now fill up list with random colours:
  non_target_colours = [colour for colour in colour_codes if colour != target_colour]
  remaining_colours = random.sample(non_target_colours, nr_remaining)
  colour_sequence.extend(remaining_colours)
  # check whether we have the correct sequence length & number of targets:
  #print(len(colour_sequence), colour_sequence.count(target_colour)) # nailed it!

  return colour_sequence


# test it!  
#print(create_0back_stimlist(target_colour = "#D292F3", nr_targets = 50, colour_codes = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"], nr_words = 300))




''' ---- 4th Function: Get n-back targets ----------'''


def get_targets(stim_list, nback_level):
    """
    For each index in the list, state if stimulus is target or not (given the n-back level).

    Parameters:
    stim_list (list): The stimulus list
    nback_level (int): Which n-back level to use (e.g. 1 or 2)
  
    Returns:
    List with booleans where True = target and False = no target
    
    """    
    
    # create target list
    target_list = []

    # loop colours, get colour and index of colour
    for col_idx, colour in enumerate(stim_list):
        # if the trial is >= our n-back level and colour matches 
        # the one n trials before, we found a target
        if col_idx >= nback_level: 
            # also get previous colour from idx - n-back level
            previous_colour = stim_list[col_idx - nback_level]
            if colour == previous_colour:
                # add 1 to target counter
                target_list.append(True)
            else: 
                target_list.append(False)
        else: target_list.append(False)
    return target_list

    print("---------------------")

