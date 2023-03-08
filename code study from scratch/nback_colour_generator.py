######################################################################
#                                                                    #
#   Colour List Generator Function for the n-Back Tasks in EXNAT-2   #
#                                                                    #    
######################################################################


# Author: Merle Schuckart (Auditory Cognition Group, Dep. for Psych. 1, University of Lübeck)
# Contact: merle.schuckart@uni-luebeck.de
# Version: 1.0 (08.03.2023)



''' ---- Settings ----------------------------------------'''

import numpy as np
import random
from random import shuffle
import math as Math



''' ---- 1. Function: draw w/o replacement with sample size > sampling list ----------'''
# --> Idea: draw w/o replacement, start over again if you run out of
#           values, then shuffle your sample
#           draw without replacement from list with sample size > list
#           start over again if no values left for drawing, shuffle everything in the end
def draw_without_replacement(sampling_list, sample_size):

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

print(draw_without_replacement(["a", "b", "c"], 4))
print("defined sample w/o replacement function")





''' ---- 2. Function: generate n-back colour list with given target number ----------'''

# Function for generating n-back stimulus list
# for given...
# ... n-back level (= nback_level) - should be a numeric
# ... stimulus list (= colour_codes) - an array of colour codes
# ... words (= story) - an array of strings (words)
# ... min. abs. number of targets (= target_abs_min) - a numeric
# ... max. abs. number of targets (= target_abs_max) - a numeric
# ... zeroback target stimulus (zeroback_target = None) - a string with a colour code

def create_nback_stimlist(nback_level, colour_codes, story, target_abs_min, target_abs_max, zeroback_target = None):

  # create pseudorandomized list of colour codes
  # idea: generate small random lists of colour codes with a balanced number of colours, then append them so I get an even distribution of colour codes & even numbers of colour codes over the whole block

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

  print("nr of targets in random colour list:", target_count)


  # if we have more targets than min. targets and less than max. targets,
  # everything's fine:
  if target_count >= target_abs_min and target_count <= target_abs_max:
    target_nr = target_count
    print("target count is correct! We have", target_count,
          "targets and we needed at least", target_abs_min,
          "and at most", target_abs_max, "targets")

  # if our target count is not in the correct range...
  else:
    # if we don't have enough targets or too many targets...
    if target_count < target_abs_min or target_count > target_abs_max:
        #print("target count is not correct. There are", target_count, "targets currently." )
        found_target_nr = False

        # randomly draw a target number to use for adding/taking away targets



# TO DO: FIX THE FOLLOWING PART




    	target_nr = Math.round(uniform.call(this, min = target_abs_min, max = target_abs_max))
        print("adding/removing", target_nr - target_count, "targets now.")

        # MISSING TARGETS:
		# --> turn non-target trials into target trials to reach the desired number of targets

        # if there are targets missing (aka if the number of targets
        # we have is smaller than the number of targets we need):
        if target_count - target_nr < 0:
            # check how many there are missing
            var nr_replacements = int.parseInt(abs(target_count - target_nr))
            #print("Targets missing, adding ", nr_replacements, " targets")

        # get indices of all false values in target list
				var indices_targets = []
				for var t = 0, _pj_a = target.length; t < _pj_a; t += 1:
          if target[t] is False:
            indices_targets = extend.call(this, indices_targets, [t])



        # if it's a 0-back task, you can start adding targets at the first position of the colour list
        //if nback_level is 0:
        #  start = 0;
        # if it's at least a 1-back, we have to move a few elements down the list to be able to start comparing to predecessors
        // else {
        #  //start = nback_level - 1;
        #  start = nback_level;
        //}


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

        # loop list of indices of non-targets:
        var idx_replacements = []
        var replacement_colours = []
        for var nontarget_idx, _pj_c = 0, _pj_a = indices_targets, _pj_b = indices_targets.length; _pj_c < _pj_b; _pj_c += 1:
          # get current index from indices_targets list
          nontarget_idx = indices_targets[_pj_c]

					# we can only put targets into the array where we have enough predecessor values.
          # So make sure not to start at idx = 0.
          # Also the next non-target we could replace with a target shouldn't be too close to
          # the last one or we mess things up again if we change them. So make sure they're a few trials apart.
          if nontarget_idx > nback_level and
              (nontarget_idx >= (idx_replacements[idx_replacements.length-1] + nback_level + 2) ||
              idx_replacements.length is 0)){
            # check if colour of current idx and idx + nback level match
            # reason: We don't want to remove targets, so don't change this
            # if it's the target colour for another trial
            var colours_match1 = random_colour_list[nontarget_idx] is random_colour_list[nontarget_idx + nback_level]
            # we also need to check if the colour n trials before is the same as the one n trials after the current trial
            # reason:
            # if we have this situation (1-back): red yellow red
            # we can't turn yellow into red to create a target because then the next trial would also turn into a target trial.
            var colours_match2 = random_colour_list[nontarget_idx + nback_level] is random_colour_list[nontarget_idx - nback_level]

            # if the colours don't match, we can replace the
            # colour without messing everything up.

            # we also need to check if there are any values left after the
            # index or we'll get problems with indexing
            if colours_match1 is False and colours_match2 is False and (nontarget_idx + nback_level) <= random_colour_list.length-1){

              # get colour at idx - nback level, so we know which colour we need to create a target
              # for the current trial:
              var replacement_col = random_colour_list[nontarget_idx - nback_level]

              # save index and replacement colour in array for later use:
              idx_replacements.append(nontarget_idx)
              replacement_colours.append(replacement_col)
              //print(replacement_col, nontarget_idx)

            }# END if cond for setting replacement colour loop
          }# END if cond for suitable target trials
        } # END for loop for potential target trials

       # now we need to draw from this list of possible replacements as many indices/colours
       # as we need to make up for the missing targets.

       # shuffle arrays with indices and colours

       # use a seed, but it's okay if it's always the same seed
       # we use 42 because it's the answer to the "Ultimate Question of Life,
       # the Universe, and Everything", but you knew that because
       # if you're reading this you're a nerd (no offense, honey).
       var seed = 42
       idx_replacements = random_shuffle_seeded(idx_replacements, seed)
       replacement_colours = random_shuffle_seeded(replacement_colours, seed)

       # take the first x values from both as replacements for non-targets
       idx_replacements = idx_replacements.slice(0, target_nr - target_count);
       replacement_colours = replacement_colours.slice(0, target_nr - target_count);

       # replace colours and "false"s in target array with colours / "true"s at the chosen indices:
       # loop the replacements
       [...Array(target_nr - target_count)].forEach((_, repl_idx) => {
       		# replace the values in the original colour and target lists
       		random_colour_list[idx_replacements[repl_idx]] = replacement_colours[repl_idx]
          target[idx_replacements[repl_idx]] = True
       })


      # TOO MANY TARGETS:

      # too many targets, get rid of some
      else:
        if target_count - target_nr > 0:
          var nr_replacements = int.parseInt(abs(target_count - target_nr))
          print("Too many targets, replacing ", nr_replacements, "targets by non-targets")

          # find indices of targets we could get rid of
          indices_targets = []
          for var t = 0, _pj_a = target.length; t < _pj_a; t += 1:
            if target[t] is True:
              indices_targets = extend.call(this, indices_targets, [t])



          # get random indices of some of those targets (as many as we need to replace)
          var k
          idx_replacements = random_sample.call(this, indices_targets, k = nr_replacements)

          # replace target by non-target colour (aka colour that doesn't match
          # target colour from n trials before or current colour
          for var replace_this_colour, _pj_c = 0, _pj_a = idx_replacements, _pj_b = _pj_a.length; _pj_c < _pj_b; _pj_c += 1:
						# get idx of colour you want to replace
            var replace_this_colour = _pj_a[_pj_c]

            # if we haven't reached the end of the colour array yet, we have to make sure
            # the new colour doesn't match the one n trials after, so we don't create more
            # targets by accident.
            if random_colour_list.length - 1 >= replace_this_colour + nback_level:
              # select colour you DON'T want to use:
              var not_this_colour = random_colour_list[replace_this_colour + nback_level]
              print("not this colour:", not_this_colour);
              # and we also don't want to replace the current colour with itself, so
              # keep current colour in mind, too:
              var curr_colour = random_colour_list[replace_this_colour]
							print("current colour:", curr_colour);

              var colour_codes_replacements = colour_codes.concat()

              # filter out the colours we don't want:
              colour_codes_replacements = colour_codes_replacements.filter(e => e is not not_this_colour)
              colour_codes_replacements = colour_codes_replacements.filter(e => e is not curr_colour)
              print("possible replacements:", colour_codes_replacements)
              # get random colour from suitable replacement colours
              var replacement_colour = random_sample.call(this, colour_codes_replacements, k = 1)[0]

            # if it's the end of the array anyway and we can't mess anything up, just
            # use random replacement colour that isn't current colour:
            else:
              print("END")
            	var colour_codes_replacements = colour_codes.concat()
              var curr_colour = random_colour_list[replace_this_colour]
              print("current colour:", curr_colour)
              colour_codes_replacements = colour_codes_replacements.filter(e => e is not curr_colour)
              print("possible replacements:", colour_codes_replacements)
              var replacement_colour = random_sample.call(this, colour_codes_replacements, k = 1)[0]

            # actually replace colours

            //print("replacing", random_colour_list[replace_this_colour], "with", replacement_colour)
            print("idx:", replace_this_colour, "target:", target[replace_this_colour])

            random_colour_list[replace_this_colour] = replacement_colour
            target[replace_this_colour] = False

           # END loop target indices
         # END if loop
      } # END TOO MANY TARGETS loop
    } # END replace values to reach desired target count loop
  } # END loop for adjusting target counts


  # count targets again:
  # create an empty array for collecting the info on targets / non-targets:
  target = []

  # loop colours
  for var col_idx, _pj_c = 0, _pj_a = random_colour_list, _pj_b = _pj_a.length; _pj_c < _pj_b; _pj_c += 1:

    # get current colour
    var colour = random_colour_list[_pj_c]
    //print(colour)

    # get colour from n trials before (1 for 1-back, 2 for 2-back)
    var nback_number = nback_level;

    # check if it's the beginning of the array - if the trial is
    # the first one (for the 1-back) or the first or second one (for the 2-back),
    # the colour can't be a target because there were not enough colours before.

    # if the trial is < our n-back level
    if _pj_c < nback_number){
      # save target as false
      var curr_target = False
    # if it's one of the following trials, check if we have a match
    else:
      # get colour from n trials back
      var previous_colour = random_colour_list[_pj_c - nback_number]

      # check if colour matches the one n trials before
      # if they match, save target as true
      if colour is previous_colour){
        var curr_target = True
      # if it's not, save target as false
      else:
        var curr_target = False
      }
   }

    # add target to bigger target list
    target.append(curr_target)

  }

  # check if it worked:
  var target_count = 0;
  for(var i = 0; i < target.length; i++){

      if(target[i] is True)
         target_count = target_count + 1
  }
  print("nr of targets after replacements:", target_count)


  # weird stuff is happening and I'm losing my patience with this:
  # sometimes, the target counts are not correct after the replacements.
  # So do recursion if the target count is still not correct and hope it fixes the problem.
  # Yes I know this is a horrible solution and the runtime gets
  # even more awful, but who cares. Certainly not me.

  if target_count is not target_nr){
    print("current target number is", target_count, "but should be", target_nr, "- recursion!")
 	# recursion: generate new colour list
    return create_nback_stimlist(nback_level, colour_codes, story, target_abs_min, target_abs_max, zeroback_target)
  else:

    # If everything is looking good, we can run some checks on the distribution of the
    # colours and then return the colour list if everything's fine

    # check if colour transition probabilities are more or less evenly distributed

    def _pj_snippets(container):
      def in_es6(left, right):
        if right instanceof Arrayor typeof right is "string":
          return right.indexOf(left) > -1
        else:
          if right instanceof Mapor right instanceof Setor right instanceof WeakMapor right instanceof WeakSet:
            return right.has(left)
          else:
            return left in right




      container["in_es6"] = in_es6
      return container


    pairs = []
    pairs_counter = []

    for var idx = 0, _pj_a = random_colour_list.length - 1; idx < _pj_a; idx += 1:
      curr_colour = random_colour_list[idx] + " -> " + random_colour_list[idx + 1]

      if _pj.in_es6(curr_colour, pairs):
        idx_pair = pairs.index(curr_colour)
        pairs_counter[idx_pair] += 1
      else:
        pairs.append(curr_colour)
        pairs_counter.append(1)



    change_prob_cutoff_lower = np.mean(pairs_counter) - 2 * np.sd(pairs_counter)
    change_prob_cutoff_upper = np.mean(pairs_counter) + 2 * np.sd(pairs_counter)
    min_change_prob          = np.min(pairs_counter)
    max_change_prob          = np.max(pairs_counter)

    if min_change_prob < change_prob_cutoff_loweror max_change_prob > change_prob_cutoff_upper:
      change_prob_equal = False
    else:
      change_prob_equal = True


	# now also check if some colours are more often targets than others:
    target_colours = []
    target_colours_counter = []

    for var t = 0, _pj_a = target.length; t < _pj_a; t += 1:
      if target[t] == True:
        target_colour = random_colour_list[t]


      if _pj.in_es6(target_colour, target_colours):
        idx_target_colour = target_colours.index(target_colour)
        target_colours_counter[idx_target_colour] += 1
      else:
        target_colours.append(target_colour)
        target_colours_counter.append(1)








    target_prob_cutoff_lower = np.mean(target_colours_counter) - 2 * np.sd(target_colours_counter)
    target_prob_cutoff_upper = np.mean(target_colours_counter) + 2 * np.sd(target_colours_counter)
    min_target_prob          = np.min(target_colours_counter)
    max_target_prob          = np.max(target_colours_counter)

    if min_target_prob < target_prob_cutoff_lower or max_target_prob > target_prob_cutoff_upper:
      target_colours_equal = False
    else:
      target_colours_equal = True


    # if everything's fine...
    if target_colours_equal and change_prob_equal:
      # return colour list:
      print("current target number is", target_count, "and should be", target_nr, "- all fine!")
      print("returning colour list")
      return random_colour_list

    # if change probabilities or distribution of target colours is not balanced...
    else:
      # recursion: generate new colour list
      print("recursion")
      return create_nback_stimlist(nback_level, colour_codes, story, target_abs_min, target_abs_max, zeroback_target)


create_nback_stimlist(1, ["red", "blue", "green", "yellow"], Array(30).fill("x"), 5, 5,
  zeroback_target = None)




