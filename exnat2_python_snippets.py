#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Script for preparing Python snippets for EXNAT-2 EEG study

Created on Fri Sep  9 13:27:05 2022

@author: merleschuckart

"""

############### Before experiment ###################

# import packages:

import random

# for seeded shuffle:
from random import Random

# for simple calculations
import numpy as np


### Custom functions

# function for drawing w/o replacement from list that is smaller than sample you want to draw
# --> start over again if you run out of values, then shuffle everything
def draw_without_replacement(sampling_list, sample_size):
    # careful, sample size is counted from 0

    # repeat colour_codes_list as often as needed
    rep_times = round(sample_size / len(sampling_list))
    
    rep_sampling_list = list(np.repeat(value = sampling_list, 
                                    times = rep_times))
        
    # check if we need some more values, if yes, draw some randomly 
    # from colour_codes and append to our list
    if len(rep_sampling_list) < sample_size:
                
        rep_sampling_list.extend(random.sample(sampling_list, 
                                         k = sample_size - len(rep_sampling_list) ))

    # now shuffle the list
    random.shuffle(rep_sampling_list)
    
    # return result
    return(list(rep_sampling_list))     
# END FUNCTION

# test function:
draw_without_replacement([1,2,3], 8)  



# Function for preparing stimulus list for colour n-back:

# arguments:
# nback_level = n-back level (numerics, e.g. 2 for 2-back)
# colour_codes = colour codes you want to use (strings)
# story = text you want to generate colours for (list with strings, e.g. ["blue", "red"]
# target_abs_min = absolute min. number of targets you need (numeric, e.g. 10 for at least 10 targets)
# targets_max = max. percentage of targets you need (numeric, e.g. 0.2 for max. 20% targets)
# targets_min = min. percentage of targets you need (numeric, e.g. 0.2 for min. 20% targets)
# zeroback_target = the target colour (as string) for the 0-back, Default if not specified: None

def create_nback_stimlist(nback_level, 
                          colour_codes, 
                          story, 
                          target_abs_min, 
                          targets_max, 
                          targets_min,
                          zeroback_target = None):

    # 1.1 chunk settings
    # make sure you can't repeat a colour more than 3x, so if you concatenate 2 
    # chunks, in the worst case you can only get the same color 6x
    chunk_size = len(colour_codes) * 3 
    
    # see how many whole chunks + incomplete chunks we need:
    chunk_nr = int(len(story) / chunk_size)
    chunk_missing = len(story) - chunk_size * chunk_nr
    
    # ---------------------------------------------------------------------------
    
    # 1.2 loop whole chunks

    random_colour_list = []
    for chunk in range(0,chunk_nr):
        
        # There's no function to draw without replacement & start over if the sample 
        # is larger than the list of values you draw from. So I wrote my own function for this (see above). 
        rep_colours = draw_without_replacement(sampling_list = colour_codes, 
                                               sample_size = chunk_size)
        
        # append chunk to list
        random_colour_list.extend(rep_colours)
    
    # ---------------------------------------------------------------------------
    
    # 1.3 fill up colour list with missing incomplete chunk
    
    # if you need some more values to fill the list...
    if chunk_missing > 0:
        
        # get some more random colour values as last chunk
        missing_chunk = draw_without_replacement(sampling_list = colour_codes, 
                                                 sample_size = chunk_missing)

        # also append to colour list
        random_colour_list.extend(missing_chunk)

    # ---------------------------------------------------------------------------
    
    # 2. loop colour list, find & count targets for the given n-back level """
    
    # create empty list to collect targets / non-targets
    target = list()

    for colour_idx in range(0, len(random_colour_list)):
        
        # if there are enough colours before the current colour to compare with, go on
        if colour_idx >= nback_level:
            
            # For the 0-back, we have to compare each colour with a given target colour
            if nback_level == 0:
                curr_colour = random_colour_list[colour_idx]
                curr_target = curr_colour == zeroback_target
                
            # For the 1-back - 3-back, we compare each colour with one of its precedessors    
            else:
                # get current colour and the colour n times before
                curr_colour = random_colour_list[colour_idx]
                colour_before = random_colour_list[colour_idx - nback_level] 

                # compare colours: is it a match?
                curr_target = curr_colour == colour_before
               
            # save result in target list
            target.append(curr_target)

        # if there are no colours to compare, save target as False    
        else:
            target.append(False)

    # now check how many targets there are in our list
    target_count = target.count(True)
    
    # 2 things can happen now:
    # Thing 1 is that the colour list already has the right amount 
    # of targets and everything's fine. This is unlikely but possible.
    # Thing 2 is that there are either too many or not enough targets in our colour list.
    # In this case, we have to take away some targets or add some without creating more targets by accident.
    # Example: 2-back, but we want 1 target less
    # b, r, r, g, o, r, o, b, r, b, g, o, o, o
    #                   ^        ^           ^
    # If we replace the first target by another letter (let's say r), 
    # we're creating a target later in the stream by accident:
    # b, r, r, g, o, r, r, b, r, b, g, o, o, o
    #                         ^  ^           ^

    # ---------------------------------------------------------------------------
    
    # 3. If the number of targets falls into our range... """
    
    # if the number of targets falls out of our range and/or there are 
    # less targets than needed needed, remove or add some targets
    
    # if everything's okay, save target_count as definite target number and go on:
    if target_count/len(target) >= targets_min and target_count/len(target) <= targets_max and target_count >= target_abs_min:

        target_nr = target_count
        
    
    elif target_count/len(target) < targets_min or target_count/len(target) > targets_max or target_count < target_abs_min:

     
        # 3.1 determine how many targets there should be
        
        found_target_nr = False
        while found_target_nr == False:
        
            # generate a random number of targets between targets_min and targets_max
            targets_percent = random.uniform(targets_min, targets_max)
            
            # check how many targets we would have in absolute numbers
            target_nr = round(len(story) * targets_percent)
            
            # check if this amount of targets is enough
            if target_nr >= target_abs_min:
                # if yes, end while loop and keep target number
                found_target_nr = True
        
        # ---------------------------------------------------------------------------
        
        # 3.2 Check if there are too many or not enough targets in our list & make adjustments

        # 3.2.1 Case 1: targets missing
        # if there are not enough targets (aka more needed targets than targets counted) ...
        if target_count - target_nr < 0:
            
            # check how many replacements we need to do
            nr_replacements = int(abs(target_count - target_nr))
            
            # find indices of non-targets in list "target" and replace by target colours, also replace False by True in "target" list
            #indices_targets = [i for i, idx in enumerate(target) if idx == False] # Careful, JS might have problems with the enumerate function and/or list comprehensions
            indices_targets = []
            for t in range(0, len(target)):
                if target[t] == False: 
                    indices_targets.append(t)
            
            # select as many of them as need to be replaced, make sure not to select non-targets from the beginning of the list
            # --> in 0-back, we don't memorize targets from former trials, so start at idx = 0 
            if nback_level == 0: start = 0
            # for every other n-back level: start at n - 1 (because python indexing starts with 0, 
            # so start = 2 would mean we start with the 3rd element and not the 2nd)
            else: start = nback_level-1   
            
            idx_replacements = random.sample(indices_targets[start:len(indices_targets)], 
                                             k = nr_replacements)

            # loop replacements, get colour n times before the current idx, use that colour as replacement and mutate colour list
            for replace_this_colour in idx_replacements:
                
                # Special case 0-back: replace with target colour
                if nback_level == 0:
                    replacement_colour = zeroback_target
                # all other n-back levels: replace with random colour that's not the colour of the stimulus at position x+n
                else:
                    # choose colour you want to use as a replacement
                    replacement_colour = random_colour_list[replace_this_colour - nback_level]
    
                # now put this replacement colour in the position of the non-target you want to replace
                random_colour_list[replace_this_colour] = replacement_colour
                    
                # you also have a list of target positions - change that one, 
                # too, so there's a False at the current index
                target[replace_this_colour] = True
        # ---------------------------------------------------------------------------
        #  3.2.2 Case 2: too many targets  
        # else if there are too many targets (--> more targets in the list than needed)...    
        elif target_count - target_nr > 0:
            
            # check how many replacements we need to do
            nr_replacements = int(abs(target_count - target_nr))
            
            # find indices of targets in list "target" and replace by non-target colours, also replace True by False in "target" list
            #indices_targets = [i for i, idx in enumerate(target) if idx == True] # Careful, JS might have problems with the enumerate function / list comprehensions
            indices_targets = []
            for t in range(0, len(target)):
                if target[t] == True: 
                    indices_targets.append(t)
                    
            # select as many of them as need to be replaced
            idx_replacements = random.sample(indices_targets, 
                                             k = nr_replacements)

            # loop replacements, get colour n times after the current idx, use different colour as replacement and mutate colour list
            for replace_this_colour in idx_replacements:
                
                # if there is a colour n times after current idx left, make sure you use another one as a replacement
                if len(random_colour_list)-1 >= replace_this_colour + nback_level: 
                
                    # choose colour you DON'T want to use as a replacement
                    if nback_level == 0:
                        not_this_colour = zeroback_target
                        
                    else:
                        not_this_colour = random_colour_list[replace_this_colour + nback_level]
                    
                    # create list with colour codes that doesn't contain this value, then choose one of those randomly
                    colour_codes_replacements = colour_codes.copy()
                    colour_codes_replacements.remove(not_this_colour) 
                    replacement_colour = random.sample(colour_codes_replacements, k = 1)[0]            
                
                # if not, you can use any colour
                else: replacement_colour = random.sample(colour_codes, k = 1)[0]            
                    
                # now put this replacement colour in the position of the target you want to remove
                random_colour_list[replace_this_colour] = replacement_colour
                
                # you also have a list of target positions - change that one, 
                # too, so there's a False at the current index
                target[replace_this_colour] = False

    # ---------------------------------------------------------------------------

    #  4. Check output for unwanted patterns """
    # The number of colours should be balanced (e.g. not way more blue than green),
    # the colours of the targets should be random (e.g. not all targets red)
    # and the change probabilities should be balanced (e.g. probability to change from orange to green)
    
    # We already made sure the colours are evenly distributed across the list by using our fancy chunk-sampling-system. 
    # We changed a few colours afterwards, but I guess that should affect the distribution of the colours over the course of the trials that much.
    # --> maybe run a simulation afterwards to check this.
    # In any case, we have to check the targets and the change probabilities:
    
    # 4.1 check change probabilities
    # find colour pairs and count their occurances

    pairs = []
        
    for idx in range(0, len(random_colour_list) - 1):

        # save current colour and next colour as a pair
        curr_colour = random_colour_list[idx] + " -> " + random_colour_list[idx + 1]
        # append it to a list             
        pairs.append(curr_colour)
                
    # count occurances of the unique pairs
    colourpairs_dict = {}
    # loop pairs
    for pair in pairs:
        # if the current pair has an entry already, add 1 to count the occurence 
        if pair in colourpairs_dict: 
            colourpairs_dict[pair] = colourpairs_dict[pair] + 1
        # if there's no entry for the pair, create one and set occurence counter to 1
        else: 
            colourpairs_dict[pair] = 1    
    
    # compute mean of occurences, if one of the change probabilities is > mean + 2*SD 
    # or < mean - 2*SD, assume that change probabilities are not really balanced
    # compute cutoffs:
    change_prob_cutoff_lower = np.mean(list( colourpairs_dict.values() )) - 2 * np.std(list( colourpairs_dict.values() ))
    change_prob_cutoff_upper = np.mean(list( colourpairs_dict.values() )) + 2 * np.std(list( colourpairs_dict.values() ))
    
    # get min and max value to see if the data are in an okayish range
    min_change_prob = np.min(list(colourpairs_dict.values()))
    max_change_prob = np.max(list(colourpairs_dict.values()))
    
    # check if everything's fine
    if min_change_prob < change_prob_cutoff_lower or max_change_prob > change_prob_cutoff_upper:
        change_prob_equal = False
    else: change_prob_equal = True

    # ---------------------------------------------------------------------------
    
    # 4.2 check target colour probabilities
    
    # only get targets, then count occurences for each colour
    #indices_targets = [idx for idx, x in enumerate(target) if x == True]
    indices_targets = []
    for t in range(0, len(target)):
        if target[t] == False: 
            indices_targets.append(t)
    
    target_colours = [random_colour_list[i] for i in indices_targets]
    
    # count occurences of target colours
    targetcolours_dict = {}
    for i in target_colours:
        if i in targetcolours_dict: 
            targetcolours_dict[i] += 1
        else: 
            targetcolours_dict[i] = 1   
    
    # same procedure as with the change probabilities (although we don't have as many values)
    # compute mean of occurences, if one of the colours has a probability that is > mean + 2*SD 
    # or < mean - 2*SD, assume that target probabilities are not really balanced
    # compute cutoffs:
    target_prob_cutoff_lower = np.mean(list( targetcolours_dict.values() )) - 2 * np.std( list(targetcolours_dict.values() ))
    target_prob_cutoff_upper = np.mean(list( targetcolours_dict.values() )) + 2 * np.std( list(targetcolours_dict.values() ))
    
    # get min and max value to see if the data are in an okayish range
    min_target_prob = np.min(list(targetcolours_dict.values()))
    max_target_prob = np.max(list(targetcolours_dict.values()))
    
    # check if everything's fine
    if min_target_prob < target_prob_cutoff_lower or max_target_prob > target_prob_cutoff_upper:
        target_colours_equal = False
    else: 
        target_colours_equal = True
    
    # ---------------------------------------------------------------------------
    
    # 4.3 if everything's fine, return colour list and target to non-target ratio
    if target_colours_equal and change_prob_equal:
        #print("finished - returning n-back list now")
        return(random_colour_list)
        
    # If not: Recursion!
    else: 
        return(create_nback_stimlist(nback_level, colour_codes, story, target_abs_min, targets_max, targets_min, zeroback_target))
        
# END FUNCTION

# test function

test_story = ["William", "Shakespeare", "war", "etwa", "fünf", "Jahre", "alt,", "als", "gar", "nicht", "weit", "entfernt", "von", "seinem", "Heimatdorf", "die", "nur", "zweijährige", "Jane", "Shaxspere", "ums", "Leben", "kam.", "Das", "kleine", "Mädchen", "wollte", "Ringelblumen", "pflücken,", "die", "am", "Ufer", "eines", "Mühlteichs", "wuchsen.", "Beim", "Blumenpflücken", "rutschte", "Jane", "aus,", "fiel", "ins", "Wasser", "und", "ertrank.", "William", "Shakespeare,", "der", "etwa", "20", "Kilometer", "entfernt", "im", "Dorf", "Stratford-upon-Avon", "aufwuchs,", "sollte", "später", "zum", "größten", "Dramatiker", "aller", "Zeiten", "heranwachsen.", "Forscher", "der", "Universität", "von", "Oxford", "vermuten", "nun", "einen", "Zusammenhang", "dieses", "Unfalls", "mit", "Shakespeares", "Stück", "\"Hamlet\".", "Eine", "Nebenhandlung", "des", "Stücks", "erzählt", "die", "Geschichte", "der", "fiktiven", "Edeldame", "Ophelia,", "der", "Tochter", "eines", "Kämmerers.", "Ophelia", "wächst", "am", "dänischen", "Königshof", "auf,", "wo", "sie", "die", "Geliebte", "des", "Prinzen", "Hamlet", "wird.", "Ihre", "Beziehung", "wird", "von", "ihrem", "Vater", "und", "ihrem", "Bruder", "jedoch", "missbilligt.", "Sie", "bezweifeln,", "dass", "Hamlet", "die", "ehrliche", "Absicht", "hat,", "Ophelia", "zu", "heiraten.", "Als", "Hamlet", "aus", "Versehen", "Ophelias", "Vater", "tötet,", "verzweifelt", "sie", "und", "erleidet", "ein", "ähnliches", "Schicksal", "wie", "die", "kleine", "Jane.", "Beim", "Blumenpflücken", "an", "einem", "Bachufer", "verliert", "sie", "das", "Gleichgewicht", "und", "fällt", "in", "den", "Bach.", "Ihr", "Kleid", "saugt", "sich", "mit", "Wasser", "voll", "und", "zieht", "sie", "wie", "ein", "Gewicht", "nach", "unten.", "Ob", "ihr", "Tod", "ein", "Unfall", "ist", "oder", "sie", "sich", "mit", "Absicht", "nicht", "aus", "dem", "Wasser", "rettet,", "wird", "im", "Stück", "offengelassen.", "Die", "erstaunliche", "Verbindung", "zwischen", "realen", "Ereignissen", "und", "Shakespeares", "\"Hamlet\"", "fiel", "Historikern", "auf,", "als", "sie", "alte", "medizinische", "Akten", "untersuchten.", "Die", "Ähnlichkeit", "der", "Nachnamen", "könnte", "sogar", "darauf", "hinweisen,", "dass", "William", "und", "Jane", "Verwandte", "gewesen", "sein", "könnten.", "Feste", "Schreibweisen", "von", "Namen", "gab", "es", "zu", "Shakespeares", "Zeiten", "nicht.", "Für", "eine", "der", "Forscherinnen", "aus", "Oxford", "ist", "dieses", "Detail", "aber", "nicht", "entscheidend:", "\"Selbst", "wenn", "sie", "nicht", "verwandt", "gewesen", "sind,", "hat", "sich", "die", "Geschichte", "durch", "die", "Ähnlichkeit", "der", "Namen", "vielleicht", "in", "Shakespeares", "Kopf", "verankert.\"", "Neben", "historischen", "Grundlagen", "seien", "Shakespeares", "Stücke", "auch", "von", "Klatsch", "und", "Tratsch-Geschichten", "beeinflusst", "worden.", "Dazu", "könnte", "auch", "die", "Geschichte", "über", "den", "Tod", "von", "Jane", "Shaxspere", "gezählt", "haben."]
print("create_nback_stimlist: ", create_nback_stimlist(nback_level = 1, 
                                                       colour_codes = ["blue", "red", "green"], 
                                                       story = test_story, 
                                                       target_abs_min = 30, 
                                                       targets_max = 0.4, 
                                                       targets_min = 0.1,
                                                       zeroback_target = None))


#################################################################################

### Stimulus settings

# set keys to use here:
# to go from word to word, I use the Space bar
# to indicate that an n-back target was detected, I want to use
# the key C for right-handed people and the 
# key M for left-handed people (but you can change that):
target_key_right = "c"
target_key_left = "m"
print("Target keys are", target_key_right, "for right-handed people and", target_key_left, "for left-handed people")

# set colours you want to use here:
# important: I set the colours "manually" in the trainings, 
# so change them there, too, if you change them here.

baseline_colour = ["#000000"] # colour for the baseline blocks (black)
colours = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"]
print("Preparing experiment with n-back colours:", colours)

#  #D292F3 = weird lilac with a 2000s vibe
#   #F989A2 = bubblegum pink
#   #2AB7EF = Twitter blue
#   #88BA3F = medium grass green
#   (#D8A244 = dark curry-ish yellow --> excluded!)

#   All colours have a luminance of 70 and a chroma of 74.

#   The colours are selected for distinguishability (is that a word?!) 
#   for people with "normal" colour vision as well as for 
#   people with protanomaly (red olour vision deficiency (CVD)), 
#   deuteranomaly (green CVD) and 
#   tritanomaly (blue CVD).

#   People with a "true" colour blindness 
#   (i.e. protanopia, deuteranopia, tritanopia)
#   shouldn't participate in this study. */



# Settings for the nback blocks:

settings_target_abs_min = 30
settings_targets_max = 0.4 
settings_targets_min = 0.1
settings_zeroback_target = None


# ----------------------------------------------

# Prepare lists with words & additional information on the blocks
# hint: escape " characters like this \"

# Giant Squid
text_01 = ["Beim", "Anblick", "der", "Tiere", "wird", "klar,", "warum", "die", "Seeleute", "vergangener", "Jahrhunderte", "Angst", "vor", "Seeungeheuern", "hatten.", "Meterlange", "Fangarme,", "spitze", "Mäuler", "und", "riesige", "Augen", "verleihen", "den", "großen", "Kalmaren", "ein", "furchterregendes", "Aussehen.", "Vor", "der", "Küste", "Chiles", "sind", "sie", "aktuell", "in", "Massen", "zu", "sehen.", "Hunderte", "von", "riesigen", "Tintenfischen", "schwimmen", "in", "den", "flachen", "Gewässern", "und", "fressen", "dort", "die", "Fische.", "Normalerweise", "sind", "die", "großen", "Kalmare", "nur", "schwer", "zu", "beobachten.", "Sie", "leben", "eigentlich", "im", "offenen", "Meer.", "Nur", "nachts", "kommen", "sie", "an", "die", "Oberfläche,", "um", "kleine", "Fische", "zu", "jagen.", "Seit", "zwei", "Wochen", "aber", "sind", "sie", "auch", "bei", "Tageslicht", "vor", "der", "Küste", "zu", "sehen.", "Zunächst", "wurden", "mehr", "als", "200", "Kalmare", "vor", "einer", "Insel", "vor", "Chile", "gesichtet.", "Später", "wurden", "dann", "weitere", "Kalmare", "an", "anderen", "Orten", "entlang", "der", "Küste", "Chiles", "beobachtet.", "Vor", "allem", "für", "die", "Fischer", "ist", "das", "ärgerlich.", "Die", "Kalmare", "fressen", "Hechte,", "Sardinen", "und", "Sardellen.", "Und", "sie", "haben", "großen", "Hunger -", "schlechte", "Karten", "für", "die", "kleineren", "Fische.", "Die", "Kalmare", "selbst", "haben", "hingegen", "Glück:", "Sie", "gelten", "zwar", "in", "manchen", "Ländern", "als", "Delikatesse,", "werden", "in", "Chile", "jedoch", "nicht", "gegessen.", "Meeresbiologen", "standen", "wegen", "des", "plötzlichen", "Erscheinens", "der", "Kalmare", "zunächst", "vor", "einem", "großen", "Rätsel.", "Nun", "ist", "jedoch", "klar,", "weshalb", "die", "Kalmare", "plötzlich", "auftauchten.", "Im", "Februar", "erwärmte", "sich", "das", "Meer", "verglichen", "mit", "den", "Temperaturen", "in", "den", "Vorjahren", "ungewöhnlich", "stark.", "Es", "sammelten", "sich", "viele", "kleine", "Fische", "vor", "der", "Küste.", "Die", "Kalmare", "wurden", "dadurch", "magisch", "angezogen.", "Die", "kleinen", "Fische", "bedeuten", "für", "sie", "reiche", "Beute.", "Für", "Forscher", "ist", "das", "ein", "besonderer", "Glücksfall.", "Normalerweise", "sind", "die", "großen", "Kalmare", "so", "schwer", "vor", "die", "Kamera", "zu", "bekommen,", "dass", "Forscher", "teilweise", "auf", "seltsame", "Ideen", "kommen.", "Ein", "Biologe", "aus", "Neuseeland", "etwa", "will", "versuchen,", "den", "legendären", "Riesenkalmar", "mit", "Sexualhormonen", "vor", "die", "Linse", "zu", "locken.", "Der", "Riesenkalmar", "ist", "mit", "bis", "zu", "20", "Metern", "Länge", "und", "einer", "halben", "Tonne", "Gewicht", "das", "größte", "wirbellose", "Tier", "der", "Welt.", "Bisher", "wurde", "er", "aber", "noch", "nie", "innerhalb", "seines", "natürlichen", "Lebensraums", "gefilmt."]

# Hemingway / The old man and the sea
text_02 = ["Zwanzig", "Jahre", "verbrachte", "Ernest", "Hemingway", "auf", "Kuba.", "Die", "meiste", "Zeit", "davon", "lebte", "er", "in", "Vigía,", "seinem", "legendären", "Haus", "vor", "den", "Toren", "Havannas.", "Seit", "seinem", "Tod", "Anfang", "der", "1960er", "lagern", "in", "Vigía", "etwa", "3000", "Manuskripte", "des", "Autors.", "In", "den", "vergangenen", "Jahren", "sind", "sie", "nach", "und", "nach", "digitalisiert", "worden.", "Nun", "will", "man", "sie", "zunächst", "in", "Kuba", "zeigen,", "bevor", "sie", "dann", "der", "Bibliothek", "von", "Boston", "übergeben", "werden.", "Die", "Leiterin", "des", "Archivs", "in", "Vigía", "sagte", "am", "Montag", "im", "kubanischen", "Fernsehen,", "es", "handele", "sich", "um", "bisher", "unveröffentlichte", "Stücke.", "Die", "Digitalisierung", "war", "zwischen", "den", "USA", "und", "Kuba", "bereits", "2002", "vereinbart", "worden.", "Damals", "berichtete", "die", "\"New", "York", "Times\",", "unter", "den", "Dokumenten", "befänden", "sich", "Texte,", "die", "auf", "lose", "Blätter", "und", "Buchrücken", "gekritzelt", "worden", "seien.", "Dies", "seien", "vor", "allem", "Briefe,", "Entwürfe", "und", "Aufzeichnungen", "zu", "Hemingways", "großen", "Romanen.", "Der", "Biograf", "Hemingways", "nannte", "den", "gesamten", "Nachlass", "eine", "\"Computertomografie", "von", "Hemingways", "Gehirn\".", "In", "Kuba", "schrieb", "Hemingway", "unter", "anderem", "seine", "berühmte", "Novelle", "\"Der", "alte", "Mann", "und", "das", "Meer\".", "Die", "Novelle", "handelt", "vom", "Kampf", "eines", "alten", "Fischers", "mit", "einem", "riesigen", "Schwertfisch.", "Zwei", "Tage", "und", "zwei", "Nächte", "ringt", "der", "Fischer", "mit", "dem", "Schwertfisch,", "bis", "er", "ihn", "schließlich", "am", "dritten", "Tag", "überwältigen", "kann.", "Da", "der", "Fisch", "zu", "groß", "ist,", "um", "ihn", "ins", "Boot", "zu", "ziehen,", "bindet", "er", "ihn", "von", "außen", "ans", "Boot.", "Das", "Blut", "des", "Schwertfisches", "lockt", "auf", "der", "Heimfahrt", "jedoch", "Haie", "an.", "Die", "Haie", "fressen", "nach", "und", "nach", "Teile", "des", "Schwertfischs,", "sodass", "dem", "Fischer", "nur", "das", "Skelett", "bleibt,", "als", "er", "wieder", "in", "den", "Heimathafen", "zurückkehrt.", "Die", "Figur", "des", "Fischers", "ist", "vermutlich", "angelehnt", "an", "den", "Fischer", "Gregorio", "Fuentes,", "der", "sich", "auf", "Kuba", "um", "Hemingways", "Boot", "kümmerte.", "Für", "sein", "Werk", "wurde", "Hemingway", "mit", "dem", "Literaturnobelpreis", "ausgezeichnet.", "Die", "Nobelpreis-Medaille", "schenkte", "er", "aus", "Verbundenheit", "zu", "Kuba", "der", "Wallfahrtskirche", "der", "barmherzigen", "Jungfrau", "von", "Cobre.", "Sie", "ist", "die", "Schutzpatronin", "Kubas.", "Die", "Medaille", "ist", "auch", "heute", "noch", "in", "der", "Kirche", "zu", "sehen."]

# Einstein
text_03 = ["Sie", "besuchte", "ihn", "oft", "in", "seinem", "Haus", "und", "bekam", "Briefe", "und", "Gedichte", "von", "ihm.", "Manchmal", "durfte", "sie", "ihm", "sogar", "die", "Haare", "schneiden.", "Johanna", "Fantova", "galt", "als", "letzte", "Freundin", "von", "Albert", "Einstein.", "Die", "beiden", "trafen", "sich", "regelmäßig,", "telefonierten", "viel", "und", "gingen", "miteinander", "segeln.", "Nun", "wurde", "bekannt,", "was", "offenbar", "nicht", "einmal", "Einstein", "wusste:", "Johanna", "Fantova", "fertigte", "Notizen", "über", "den", "Inhalt", "ihrer", "Gespräche", "an.", "In", "ihren", "Aufzeichnungen", "zeigt", "sie", "ihn", "nicht", "als", "den", "großen", "Mann,", "der", "zu", "Lebzeiten", "zur", "Legende", "wurde,", "sondern", "als", "Einstein,", "den", "Menschenfreund.", "Die", "Nachwelt", "dürfte", "ihr", "dankbar", "sein.", "Ohne", "die", "Notizen", "wüssten", "wir", "heute", "nichts", "von", "Bibo,", "dem", "traurigen", "Papagei.", "Auch", "eine", "ganze", "Reihe", "kluger", "und", "lustiger", "Zitate", "von", "Einstein", "wären", "verloren", "gegangen.", "Es", "ist", "bisher", "das", "einzige", "bekannte", "Tagebuch", "von", "einer", "Person,", "die", "während", "seiner", "letzten", "Jahre", "eng", "mit", "Einstein", "befreundet", "war.", "Die", "22", "Jahre", "jüngere", "Johanna", "Fantova", "stammte", "wie", "Einstein", "aus", "Europa.", "Die", "Eltern", "ihres", "Ehemannes", "Otto", "Fanta", "empfingen", "vor", "dem", "Krieg", "viele", "berühmte", "Gäste", "in", "ihrem", "Salon.", "Neben", "Einstein", "zählte", "dazu", "auch", "Franz", "Kafka.", "Johanna", "Fantova", "war", "für", "Einstein", "daher", "ein", "Teil", "der", "alten", "Welt.", "Sie", "war", "eine", "Verbindung", "zu", "Dingen,", "die", "er", "vermisste.", "In", "Fantovas", "Manuskript", "erscheint", "Einstein", "als", "komischer", "Eigenbrötler.", "Zugleich", "beschreibt", "sie", "ihn", "aber", "auch", "als", "Menschenfreund,", "der", "vielen", "seiner", "Freunde", "bei", "persönlichen", "Problemen", "half.", "Und", "doch", "fühlte", "sich", "Einstein", "nie", "wirklich", "mit", "seinen", "Mitmenschen", "verbunden.", "Angesichts", "seiner", "eigenen", "gescheiterten", "Beziehungen", "betrachtete", "er", "die", "Beziehungen", "seiner", "Freunde", "mit", "spöttischer", "Distanz:", "\"Ich", "war", "bei", "einem", "Nachbarn.", "Es", "besteht", "die", "Gefahr,", "dass", "sein", "Sohn", "heiratet.\"", "Rührend", "kümmerte", "er", "sich", "dagegen", "um", "sein", "Haustier,", "einen", "deprimierten", "Papagei", "namens", "Bibo.", "\"Der", "Papagei", "ist", "noch", "ganz", "verschüchtert.", "Er", "kam", "mit", "der", "Post.\"", "Einstein", "schritt", "sofort", "zur", "Tat.", "Der", "Erfolg", "blieb", "jedoch", "leider", "aus:", "\"Der", "Papagei", "ist", "traurig.", "Ich", "versuche", "ihn", "aufzuheitern,", "aber", "er", "versteht", "leider", "meine", "Witze", "nicht.\""]

# Batman's Joker
text_04 = ["Jerry", "Robinson", "war", "erst", "17,", "als", "er", "die", "wichtigste", "Entscheidung", "seines", "Lebens", "traf -", "und", "möglicherweise", "seinen", "größten", "Fehler", "beging.", "Statt", "wie", "geplant", "aufs", "College", "zu", "gehen,", "ließ", "er", "sich", "von", "einem", "Mann", "namens", "Bob", "Kane", "als", "Zeichner", "engagieren.", "Kane", "hatte", "gerade", "die", "Zeichnungen", "für", "ein", "Comicheft", "abgeliefert,", "in", "dem", "er", "eine", "völlig", "neue", "Figur", "auftreten", "ließ,", "genannt", "\"Batman\".", "Jetzt", "machte", "er", "Urlaub", "in", "den", "Poconos,", "einem", "Ausflugsgebiet", "in", "Pennsylvania.", "Der", "untergewichtige", "Jerry", "Robinson", "war", "auf", "einer", "Kur", "dort,", "um", "Gewicht", "zuzulegen.", "Um", "Bob", "Kane", "von", "seinem", "Talent", "als", "Zeichner", "zu", "überzeugen,", "fertigte", "Jerry", "Robinson", "für", "ihn", "ein", "paar", "Zeichnungen", "an.", "Da", "er", "kein", "Papier", "zur", "Hand", "hatte,", "zeichnete", "er", "kurzerhand", "auf", "seiner", "Jacke.", "Beeindruckt", "stellte", "Kane", "den", "Jungen", "an.", "Bereits", "ab", "der", "dritten", "Ausgabe", "der", "Batman-Comics", "war", "er", "der", "Hauptzeichner", "der", "Serie.", "Seine", "Zeichnungen", "fertigte", "er", "vor", "allem", "nachts", "an.", "Tagsüber", "studierte", "er", "Journalistik", "in", "New", "York.", "Neben", "dem", "Zeichnen", "tat", "er", "sich", "auch", "bei", "der", "Entwicklung", "der", "Figuren", "hervor.", "Von", "ihm", "stammten", "die", "Entwürfe", "für", "Batmans", "Butler", "Alfred", "und", "Batmans", "Helfer,", "den", "jungen", "Robin.", "Fast", "zeitgleich", "hatte", "der", "Joker,", "Batmans", "Erzfeind,", "seinen", "ersten", "Auftritt", "in", "einem", "weiteren", "Heft.", "Robinson", "behauptete", "später,", "die", "Idee", "zur", "Figur", "des", "Jokers", "sei", "von", "ihm", "ausgegangen.", "Inspiriert", "wurde", "er", "dabei", "durch", "ein", "Kartenspiel,", "das", "seine", "Kollegen", "immer", "zur", "Hand", "hatten.", "Laut", "Bob", "Kane", "beruht", "der", "Entwurf", "des", "Schurken", "dagegen", "auf", "einer", "Szene", "aus", "einem", "Stummfilm.", "\"Robinson", "hatte", "nichts", "damit", "zu", "tun\",", "war", "sein", "drastisches", "Urteil.", "Hier", "rächte", "es", "sich,", "dass", "Jerry", "Robinson", "lediglich", "als", "Assistent", "engagiert", "war,", "auch", "wenn", "er", "der", "Hauptzeichner", "war.", "Kane", "dagegen", "hatte", "sich", "alle", "Rechte", "an", "den", "Figuren", "zugesichert.", "Nicht", "zuletzt", "deshalb", "begann", "Jerry", "Robinson", "ab", "1940", "nicht", "mehr", "für", "Kane,", "sondern", "für", "den", "Comic-Verlag", "direkt", "zu", "arbeiten.", "In", "dessen", "Studio", "saß", "er", "zeitweise", "neben", "\"Superman\"-Miterfinder", "Joe", "Shuster", "am", "Zeichentisch."]

# tiny chameleons
text_05 = ["Die", "Korallenriffe", "und", "die", "sandigen", "Buchten", "sind", "perfekt", "für", "jede", "Urlaubsbroschüre.", "Insgesamt", "ist", "die", "Inselgruppe", "namens", "Nosy", "Hara", "vor", "Madagaskar", "aber", "doch", "recht", "karg.", "In", "dieser", "eher", "lebensfeindlichen", "Umgebung", "haben", "Biologen", "nun", "eine", "neue", "Tierart", "entdeckt:", "Das", "winzige", "Chamäleon", "Brookesia", "micra.", "Von", "der", "Schnauze", "bis", "zum", "Schwanzende", "misst", "es", "weniger", "als", "drei", "Zentimeter.", "Farblich", "machen", "die", "braunen", "Tierchen", "wenig", "her.", "Doch", "ihre", "winzige", "Körpergröße", "fasziniert", "die", "Forscher.", "\"Das", "ist", "nichts,", "wo", "man", "viele", "Untersuchungen", "machen", "muss.", "Man", "erkennt", "auch", "so,", "dass", "das", "etwas", "Neues", "ist\",", "sagt", "Miguel", "Vences.", "Der", "Zoologe", "berichtet", "in", "einem", "Fachartikel", "gleich", "von", "vier", "neuen", "Arten", "von", "Mini-Chamäleons.", "Laut", "den", "Forschern", "weiß", "man", "von", "den", "Tieren", "jedoch", "kaum", "mehr,", "als", "dass", "es", "sie", "gibt.", "Zu", "ihrer", "Lebensweise", "ist", "nur", "sehr", "wenig", "bekannt.", "Tagsüber", "leben", "die", "kleinen", "Chamäleons", "am", "Boden.", "Wenn", "möglich", "verbergen", "sie", "sich", "dabei", "unter", "einer", "Schicht", "Laub.", "Nachts", "geht", "es", "dann", "auf", "niedrig", "gelegene", "Äste", "zum", "Schlafen.", "Direkte", "Fressfeinde", "haben", "die", "Tierchen", "allerdings", "wohl", "eher", "nicht.", "Zu", "ihrem", "Glück,", "so", "die", "Forscher.", "Auf", "solchen", "kleinen", "Inseln", "kann", "die", "Konkurrenz", "zwischen", "den", "Tierarten", "schnell", "sehr", "groß", "werden.", "Auch", "die", "anderen", "neuen", "Chamäleon-Arten", "besiedeln", "nur", "kleine", "Gebiete", "auf", "Madagaskar.", "Durch", "die", "Zerstörung", "ihres", "Lebensraums", "sind", "sie", "jedoch", "besonders", "bedroht.", "Rund", "40", "Prozent", "der", "Reptilien-Arten", "auf", "Madagaskar", "gelten", "mittlerweile", "als", "gefährdet.", "Die", "Forscher", "befürchten,", "dass", "auch", "Brookesia", "tristis,", "eine", "weitere", "neu", "entdeckte", "Art,", "einer", "ungewissen", "Zukunft", "entgegen", "sieht.", "Zwar", "ist", "der", "Lebensraum", "des", "Chamäleons", "vor", "wenigen", "Jahren", "unter", "Schutz", "gestellt", "worden,", "doch", "die", "Abholzung", "des", "Gebiets", "hat", "seitdem", "leider", "sogar", "noch", "zugenommen.", "Mit", "der", "Wahl", "der", "Namen", "der", "neu", "entdeckten", "Chamäleon-Arten", "wollen", "sie", "auf", "die", "große", "Gefahr", "hinweisen,", "die", "den", "Chamäleons", "droht.", "Die", "Botschaft", "hinter", "den", "Namen", "Brookesia", "desperata", "und", "Brookesia", "tristis", "versteht", "man", "auch", "ohne", "Latein", "zu", "können:", "Desperata", "heißt", "verzweifelt", "und", "tristis", "so", "viel", "wie", "traurig."]

# Mauritius
text_06 = ["In", "den", "siebziger", "Jahren", "war", "Mauritius", "eine", "kleine", "Insel", "mitten", "im", "Indischen", "Ozean,", "die", "im", "Ausland", "niemand", "kannte.", "Heute", "ist", "sie", "dagegen", "weltweit", "als", "paradiesisches", "Urlaubsziel", "bekannt.", "Doch", "schon", "lange", "bevor", "die", "ersten", "Touristen", "kamen,", "war", "Mauritius", "in", "einigen", "Teilen", "der", "Welt", "sehr", "bekannt.", "Die", "Portugiesen", "waren", "die", "Ersten,", "die", "die", "Insel", "entdeckten.", "Sie", "nannten", "sie", "\"Schwaneninsel\",", "ließen", "sich", "aber", "nicht", "auf", "ihr", "nieder.", "Erst", "fast", "hundert", "Jahre", "später", "kamen", "die", "Holländer.", "Sie", "gaben", "der", "Insel", "zu", "Ehren", "des", "holländischen", "Prinzen", "Moritz", "den", "Namen", "\"Mauritius\".", "Den", "Namen", "Mauritius", "hat", "sie", "bis", "heute", "behalten.", "Die", "Holländer", "begannen,", "an", "der", "Küste", "Felder", "anzulegen.", "Sie", "brachten", "Zuckerrohr,", "Wild", "und", "Affen", "mit", "auf", "die", "Insel.", "Sie", "bauten", "Häuser", "und", "Festungen", "und", "holzten", "die", "dichten", "Wälder", "aus", "Ebenholz", "ab.", "Zu", "dieser", "Zeit", "lebten", "auf", "Mauritius", "noch", "viele", "Dodos.", "Die", "flugunfähigen", "Vögel", "hatten", "keine", "natürlichen", "Feinde", "auf", "der", "Insel", "und", "waren", "daher", "zu", "ihrem", "eigenen", "Unglück", "sehr", "zahm.", "Für", "die", "Holländer", "machte", "sie", "das", "zur", "perfekten", "Jagdbeute.", "Der", "Dodo", "wurde", "so", "stark", "bejagt,", "dass", "er", "schon", "einige", "Jahrzehnte", "nach", "Ankunft", "der", "Holländer", "vollständig", "ausgerottet", "war.", "Heute", "ist", "er", "das", "Nationalsymbol", "von", "Mauritius.", "Als", "kein", "Holz", "mehr", "zu", "holen", "und", "die", "Natur", "schwer", "geschädigt", "war,", "verließen", "die", "Holländer", "Mauritius.", "Um", "die", "Kontrolle", "der", "Insel", "brach", "ein", "erbitterter", "Krieg", "zwischen", "Briten", "und", "Franzosen", "aus.", "Aber", "wer", "lebt", "heute", "dort?", "Die", "Bevölkerung", "von", "Mauritius", "ist", "das", "Ergebnis", "einer", "Vermischung", "verschiedener", "Kulturen", "und", "Religionen.", "Viele", "der", "Menschen", "kamen", "nicht", "freiwillig.", "Die", "Holländer", "brachten", "afrikanische", "Sklaven", "mit", "auf", "die", "Insel.", "Aus", "Indien", "kamen", "Arbeiter", "für", "die", "Zuckerrohr-Plantagen", "und", "Handwerker,", "die", "beim", "Bau", "von", "Brücken", "und", "Straßen", "halfen.", "Zeitgleich", "mit", "den", "Indern", "kamen", "auch", "muslimische", "und", "chinesische", "Händler", "nach", "Mauritius. ", "Die", "Nachfahren", "von", "Indern,", "Franzosen,", "Chinesen,", "Arabern", "und", "afrikanischen", "Sklaven", "bilden", "heute", "auf", "Mauritius", "eine", "der", "wenigen", "echten", "multikulturellen", "Gesellschaften", "der", "Welt."]

# Angkor Wat
text_07 = ["Wer", "Angkor", "sagt,", "meint", "in", "der", "Regel", "Angkor", "Wat.", "Die", "berühmte", "Tempel-Anlage", "wurde", "vermutlich", "vor", "knapp", "900", "Jahren", "in", "den", "Dschungel", "Kambodschas", "gebaut.", "Seit", "mehr", "als", "hundert", "Jahren", "hat", "sich", "die", "Wissenschaft", "auf", "die", "riesigen", "Tempelanlagen", "und", "ihre", "Inschriften", "konzentriert.", "Für", "die", "Lebensweise", "der", "Bewohner", "der", "Region", "hat", "sich", "hingegen", "kaum", "jemand", "interessiert.", "Das", "Team", "um", "den", "Forscher", "Damian", "Evans", "hat", "nun", "erstmals", "eine", "Karte", "von", "Angkor", "Wat", "erstellt.", "Die", "Karte", "zeigt,", "dass", "Angkor", "Wat", "eine", "richtige", "Stadt", "war,", "nicht", "nur", "eine", "kleine", "Tempelanlage.", "Die", "Forscher", "gehen", "davon", "aus,", "dass", "Ihre", "Größe", "sogar", "New", "York", "übertroffen", "haben", "könnte.", "Damit", "ist", "\"Groß-Angkor\"", "die", "mit", "Abstand", "größte", "vorindustrielle", "Siedlung", "der", "Welt.", "Selbst", "die", "riesigen", "Städte", "der", "Maya", "erscheinen", "dagegen", "winzig.", "Die", "Forscher", "fanden", "außerdem", "heraus,", "dass", "Angkor", "eine", "hydraulische", "Stadt", "war.", "Dank", "eines", "komplizierten", "Bewässerungssystems", "konnten", "die", "mehr", "als", "eine", "Million", "Bewohner", "versorgt", "werden.", "Durch", "das", "riesige", "Netz", "aus", "Flüssen,", "Kanälen", "und", "Stauseen", "hat", "die", "mittelalterliche", "Stadt", "mehrmals", "im", "Jahr", "Reis", "ernten", "können.", "Das", "verschaffte", "den", "Bewohnern", "nicht", "nur", "volle", "Teller,", "sondern", "auch", "einen", "enormen", "Reichtum.", "Die", "Stadt", "umgab", "ein", "riesiges", "Geflecht", "aus", "Äckern,", "Häusern", "und", "Seen,", "das", "sich", "über", "mindestens", "tausend", "Quadratkilometer", "erstreckte.", "Auf", "dieser", "Fläche", "gibt", "es", "kaum", "einen", "Fleck,", "der", "nicht", "genutzt", "worden", "ist.", "Das", "Bewässerungsnetz", "war", "sogar", "dazu", "geeignet,", "den", "Reisanbau", "zu", "stärken.", "Für", "den", "Anbau", "von", "Reis", "braucht", "man", "jedoch", "extrem", "viel", "Wasser", "und", "riesige", "Flächen.", "Um", "die", "Felder", "und", "die", "künstlichen", "Seen,", "Flüsse", "und", "Kanäle", "anzulegen,", "mussten", "große", "Waldflächen", "gerodet", "werden.", "Mit", "der", "Zeit", "führte", "das", "wahrscheinlich", "zu", "riesigen", "Problemen", "wie", "Erdrutschen.", "Das", "gesamte", "System", "dürfte", "daher", "auch", "sehr", "empfindlich", "auf", "Naturkatastrophen", "reagiert", "haben.", "Insbesondere", "im", "Norden", "der", "Stadt", "fand", "man", "Spuren", "von", "hektischen", "Anpassungen", "und", "Deichbrüchen.", "Genaueres", "weiß", "man", "aber", "nicht.", "Die", "neue", "Karte", "der", "Stadt", "verrät", "aber", "zumindest,", "wo", "man", "nach", "Antworten", "suchen", "sollte."]

# Petra
text_08 = ["Ein", "solcher", "Anblick", "lässt", "selbst", "Indiana", "Jones", "Kinnlade", "herunterklappen:", "Nach", "einem", "spektakulären", "Ritt", "durch", "eine", "teils", "nur", "zwei", "Meter", "schmale", "Schlucht", "erhebt", "sich", "vor", "dem", "Filmhelden", "eine", "riesige", "Fassade.", "Die", "Szene", "aus", "dem", "Kinofilm", "machte", "die", "antike", "Felsenstadt", "Petra", "endgültig", "weltberühmt.", "Die", "prachtvolle", "Fassade", "ist", "eine", "der", "schönsten", "Bauten", "in", "der", "Felsenstadt", "mitten", "in", "der", "Wüste", "Jordaniens.", "Die", "Metropole", "war", "einst", "die", "Hauptstadt", "der", "Nabatäer.", "Zwei", "Jahrhunderte", "beherrschten", "die", "Nabatäer", "große", "Teile", "des", "Handels", "im", "Nahen", "Osten.", "So", "reich", "und", "mächtig", "wurde", "das", "Wüstenvolk,", "dass", "es", "sogar", "die", "Römer", "herausforderte.", "Doch", "wie", "ihre", "riesige", "Hauptstadt", "mitten", "in", "der", "Wüste", "funktioniert", "hat,", "weiß", "niemand", "genau.", "Sicher", "ist,", "dass", "die", "Stadt", "in", "atemberaubend", "kurzer", "Zeit", "entstand.", "Als", "die", "Nabatäer", "ins", "heutige", "Jordanien", "vordrangen,", "war", "die", "Region", "die", "reinste", "Goldgrube.", "Bei", "Petra", "kreuzten", "sich", "mehrere", "Handelswege,", "darunter", "die", "uralte", "Weihrauchstraße.", "Binnen", "weniger", "Jahrzehnte", "entstanden", "hunderte", "Höhlen", "mit", "prunkvollen", "Fassaden", "und", "teils", "gewaltigen", "Räumen.", "Von", "der", "eigentlichen", "Stadt", "ist", "heute", "nichts", "geblieben", "außer", "Steinhaufen", "und", "Mauerreste.", "Bis", "in", "die", "siebziger", "Jahre", "glaubte", "man", "daher,", "Petra", "sei", "eine", "Stadt", "für", "die", "Toten", "und", "die", "Götter", "gewesen,", "und", "die", "Menschen", "hätten", "woanders", "gewohnt.", "Aber", "Petra", "war", "eine", "ganz", "normale", "Stadt,", "nur", "an", "einem", "unmöglichen", "Ort.", "Die", "seltenen", "Regenfälle", "nutzten", "die", "Nabatäer", "mit", "einem", "genialen", "Bewässerungssystem.", "Überall", "in", "der", "Stadt", "waren", "Wasserbecken", "in", "den", "Fels", "geschlagen.", "Viele", "Kilometer", "Wasserleitungen", "leiteten", "das", "Wasser", "zuerst", "in", "die", "Speicher", "und", "von", "dort", "aus", "zu", "den", "Bewohnern.", "Die", "vielen", "Leitungen,", "die", "den", "Regen", "einst", "von", "den", "wertvollen", "Fassaden", "fernhielten,", "wurden", "von", "den", "Nabatäern", "dauernd", "instand", "gehalten.", "Doch", "wenn", "es", "jetzt", "regnet,", "strömt", "das", "Wasser", "unkontrolliert", "die", "Fassaden", "herab.", "Für", "den", "Sandstein", "ist", "das", "eine", "Katastrophe.", "Versuche", "zur", "Rettung", "der", "Fassaden", "gab", "es,", "doch", "wirklich", "erfolgreich", "war", "bislang", "leider", "keiner.", "Die", "antike", "Felsenstadt", "wird", "daher", "wohl", "eines", "Tages", "wieder", "zu", "Sand", "zerfallen."]

# Shakespeare / Hamlet
text_09 = ["William", "Shakespeare", "war", "etwa", "fünf", "Jahre", "alt,", "als", "gar", "nicht", "weit", "entfernt", "von", "seinem", "Heimatdorf", "die", "nur", "zweijährige", "Jane", "Shaxspere", "ums", "Leben", "kam.", "Das", "kleine", "Mädchen", "wollte", "Ringelblumen", "pflücken,", "die", "am", "Ufer", "eines", "Mühlteichs", "wuchsen.", "Beim", "Blumenpflücken", "rutschte", "Jane", "aus,", "fiel", "ins", "Wasser", "und", "ertrank.", "William", "Shakespeare,", "der", "etwa", "20", "Kilometer", "entfernt", "im", "Dorf", "Stratford-upon-Avon", "aufwuchs,", "sollte", "später", "zum", "größten", "Dramatiker", "aller", "Zeiten", "heranwachsen.", "Forscher", "der", "Universität", "von", "Oxford", "vermuten", "nun", "einen", "Zusammenhang", "dieses", "Unfalls", "mit", "Shakespeares", "Stück", "\"Hamlet\".", "Eine", "Nebenhandlung", "des", "Stücks", "erzählt", "die", "Geschichte", "der", "fiktiven", "Edeldame", "Ophelia,", "der", "Tochter", "eines", "Kämmerers.", "Ophelia", "wächst", "am", "dänischen", "Königshof", "auf,", "wo", "sie", "die", "Geliebte", "des", "Prinzen", "Hamlet", "wird.", "Ihre", "Beziehung", "wird", "von", "ihrem", "Vater", "und", "ihrem", "Bruder", "jedoch", "missbilligt.", "Sie", "bezweifeln,", "dass", "Hamlet", "die", "ehrliche", "Absicht", "hat,", "Ophelia", "zu", "heiraten.", "Als", "Hamlet", "aus", "Versehen", "Ophelias", "Vater", "tötet,", "verzweifelt", "sie", "und", "erleidet", "ein", "ähnliches", "Schicksal", "wie", "die", "kleine", "Jane.", "Beim", "Blumenpflücken", "an", "einem", "Bachufer", "verliert", "sie", "das", "Gleichgewicht", "und", "fällt", "in", "den", "Bach.", "Ihr", "Kleid", "saugt", "sich", "mit", "Wasser", "voll", "und", "zieht", "sie", "wie", "ein", "Gewicht", "nach", "unten.", "Ob", "ihr", "Tod", "ein", "Unfall", "ist", "oder", "sie", "sich", "mit", "Absicht", "nicht", "aus", "dem", "Wasser", "rettet,", "wird", "im", "Stück", "offengelassen.", "Die", "erstaunliche", "Verbindung", "zwischen", "realen", "Ereignissen", "und", "Shakespeares", "\"Hamlet\"", "fiel", "Historikern", "auf,", "als", "sie", "alte", "medizinische", "Akten", "untersuchten.", "Die", "Ähnlichkeit", "der", "Nachnamen", "könnte", "sogar", "darauf", "hinweisen,", "dass", "William", "und", "Jane", "Verwandte", "gewesen", "sein", "könnten.", "Feste", "Schreibweisen", "von", "Namen", "gab", "es", "zu", "Shakespeares", "Zeiten", "nicht.", "Für", "eine", "der", "Forscherinnen", "aus", "Oxford", "ist", "dieses", "Detail", "aber", "nicht", "entscheidend:", "\"Selbst", "wenn", "sie", "nicht", "verwandt", "gewesen", "sind,", "hat", "sich", "die", "Geschichte", "durch", "die", "Ähnlichkeit", "der", "Namen", "vielleicht", "in", "Shakespeares", "Kopf", "verankert.\"", "Neben", "historischen", "Grundlagen", "seien", "Shakespeares", "Stücke", "auch", "von", "Klatsch", "und", "Tratsch-Geschichten", "beeinflusst", "worden.", "Dazu", "könnte", "auch", "die", "Geschichte", "über", "den", "Tod", "von", "Jane", "Shaxspere", "gezählt", "haben."]

# --------------------------------

# SELECT TEXTS

# put the texts into nested lists, shuffle 
# them, then get as many texts as you need for each 
# part of the experiment

# collect texts in lists
# IMPORTANT: DELETE THE ONES FROM THIS LIST THAT YOU DON'T WANT TO USE!
all_texts_list = [text_01, text_02, text_03, text_04, text_05, text_06, text_07, text_08, text_09]

# collect the text IDs in lists so I know which text was shown
all_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04", "text_05", "text_06", "text_07", "text_08", "text_09"]


# choose random seed 
# the seed should be random number over participants but the same within a participant
seed = np.random.uniform(0, 100)
print("seed: ", seed)

# shuffle texts and numbers using the same seed
Random(seed).shuffle(all_texts_list)
Random(seed).shuffle(all_texts_nrs_list)

# select 9 of the texts for each of the main blocks
# (3x reading baseline, 3x 1-back, 3x 2-back)
all_texts_list = all_texts_list[0:9]
all_texts_nrs_list = all_texts_nrs_list[0:9]
# (we have only 9 texts, so this step is a bit weird. I keep it in case we want less blocks.)

# print info on text selection in console
print("Chose these texts: ", all_texts_nrs_list)
print("finished preparing stimuli")


# set order of n-back tasks in experiment:
# 0 = reading baseline
# 1 = 1-back
# 2 = 2-back
# important: first block should be baseline, so only shuffle the following blocks!
# --> we can use the seed we set before
block_conditions = [0, 0, 1, 1, 1, 2, 2, 2]
Random(seed).shuffle(block_conditions)

all_nbacks_list = [0] + block_conditions
print("order of block conditions: ", all_nbacks_list)


# --------------------------------

# N-Back colour settings

# Idea: Generate n-back colour list for each block.

tmp_counter = 0

all_colour_lists = []
all_targets = []
all_block_kinds = []
    
# loop list of block conditions
for block_cond in all_nbacks_list:
        
    # get length of text
    len_curr_text = len(all_texts_list[tmp_counter])
    
    # 0 = Reading Baseline without n-back task:
    if block_cond == 0:
        
        # The baseline blocks don't get fancy colours, so make their font black.
        # repeat colour code for baseline blocks as often as the text is long
        curr_colour_list = [baseline_colour] * len_curr_text
        
        # target list: no nback task in this block, so no targets to be detected
        curr_target_list = [False] * len_curr_text
        
        # save info on kind of block
        curr_block_kind = ["reading_baseline"] * len_curr_text
        
        # save number of block so I know in which order they were presented
        curr_block_nr = [tmp_counter] * len_curr_text
        
    # if it's one of the nback blocks, generate colour list
    else:
        curr_colour_list = create_nback_stimlist(nback_level = block_cond, 
                                                 colour_codes = colours, 
                                                 story = all_texts_list[tmp_counter], 
                                                 target_abs_min = settings_target_abs_min, 
                                                 targets_max = settings_targets_max, 
                                                 targets_min = settings_targets_min,
                                                 zeroback_target = None)

        # target list: compute targets for given n-back level
        # (starting from block_cond - this means for the 1-back I start 
        # looking for targets everywhere but at position 0 (because it can't 
        # be a target) and for the two back I ignore the first 2 positions)
        tmp_trial_counter = 0
        curr_target_list = [False] * block_cond
        
        for curr_colour in curr_colour_list[block_cond: ]:
            print(tmp_trial_counter)
        
            if curr_colour == curr_colour_list[tmp_trial_counter]:
                curr_target_list = curr_target_list + [True]
            else:
                curr_target_list = curr_target_list + [False]
            # go to next position
            tmp_trial_counter = tmp_trial_counter + 1
        
        # save info on kind of block
        curr_block_kind = [str(block_cond) + "-back main"]* len_curr_text
    
    # add small lists to  main lists where I collect everything:
    all_colour_lists.append(curr_colour_list)
    all_targets.append(curr_target_list)
    all_block_kinds.append(curr_block_kind)
    
    # go to next block / text
    tmp_counter = tmp_counter + 1


# ------------------------------------------

# init trial counter for the whole experiment
exp_trial_counter = 0

# init block counter for the whole experiment
exp_block_counter = 0


################################################

### Prepare information for first trial

curr_colour = all_colour_lists[exp_block_counter][exp_trial_counter]
curr_block_kind = all_block_kinds[exp_block_counter][exp_trial_counter]
curr_target = all_targets[exp_block_counter][exp_trial_counter]


""" IMPORTANT: """
# Don't forget to set trial counter back to 0 after each main block!
# Don't forget to add 1 to trial_counter after each trial and to block_counter after each block!









