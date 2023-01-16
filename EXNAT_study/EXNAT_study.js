/******************** 
 * Exnat_Study Test *
 ********************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.3.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'EXNAT_study';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(settingsRoutineBegin());
flowScheduler.add(settingsRoutineEachFrame());
flowScheduler.add(settingsRoutineEnd());
flowScheduler.add(consent_onlRoutineBegin());
flowScheduler.add(consent_onlRoutineEachFrame());
flowScheduler.add(consent_onlRoutineEnd());
flowScheduler.add(end_no_consentRoutineBegin());
flowScheduler.add(end_no_consentRoutineEachFrame());
flowScheduler.add(end_no_consentRoutineEnd());
flowScheduler.add(demogr_onlRoutineBegin());
flowScheduler.add(demogr_onlRoutineEachFrame());
flowScheduler.add(demogr_onlRoutineEnd());
flowScheduler.add(end_excludedRoutineBegin());
flowScheduler.add(end_excludedRoutineEachFrame());
flowScheduler.add(end_excludedRoutineEnd());
flowScheduler.add(instr_1RoutineBegin());
flowScheduler.add(instr_1RoutineEachFrame());
flowScheduler.add(instr_1RoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var settingsClock;
var random;
var thisExp;
var win;
var event;
var test;
var loading1;
var consent_onlClock;
var loading2;
var end_no_consentClock;
var end1;
var demogr_onlClock;
var loading3;
var end_excludedClock;
var end2;
var instr_1Clock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "settings"
  settingsClock = new util.Clock();
  // import / create functions needed to run this experiment
  
  // import random
  random = Math.random;
  console.log("imported random package");
  
  // from random import shuffle
  var random_shuffle = function(array) {  
    var array, currentIndex = array.length, randomIndex;
    // While there remain elements to shuffle...
    while (currentIndex != 0) {
      // pick a random element
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
      // and swap it with the current element
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
    // return shuffled array
    return array;
  }
  console.log("defined shuffle function")
  
  // np.random.uniform()
  var uniform = function(min, max) {
    var min, max;
    return (Math.random() * (max-1 - min + 1) + min);
  }
  console.log("defined uniform function");
  
  //.append()
  // append a value to an array
  //var append = function(array, value){
  //    var array, value;
  //    return array.push(value);
  //}
  //console.log("defined append function");
  // disabled because it doesn't work - use extend instead!
  
  // .extend()
  // concatenate 2 arrays, return as new array
  var extend = function(array1, array2){
      var array1, array2;
      return array1.concat(array2);
  }
  console.log("defined extend function");
  
  
  // random.sample()
  // this function is using the Fisher-Yates shuffle and 
  // taking a part of the resulting array to create the random sample
  var random_sample = function(arr, k) {
      // with arr = some sample to draw from and k = sample size
      
      // define variables
      var arr, k, shuffled = arr.slice(0), i = arr.length, min = i - k, temp, index;
      while (i-- > min) {
          index = Math.floor((i + 1) * Math.random());
          temp = shuffled[index];
          shuffled[index] = shuffled[i];
          shuffled[i] = temp;
      }
      return shuffled.slice(min);
  }
  console.log("defined random.sample function");
  
  
  // repeat()
  var repeat = function(value, times) {
      // set variables
      var value, times;
      
      // if you want to repeat a single value
      if (typeof value === 'string' || value instanceof String){
          // just repeat value and return as array
          return Array(times).fill(value); 
      }
      // if you want to repeat an array
      else if (Array.isArray(value)){
          // save value array you want to append & mutate the original one
          var add_value = value;
          for (var i = 0; i < times-1; i++){
              // define variables again
              var array1, array2;
              value = extend.call(this, array1 = value, array2 = add_value);
          }
          // return concatenated arrays
          return value;  
      }
  }
  console.log("defined repeat function");
  
  // count
  var count = function(array, value){
      // set variables
      var array, value, counter = 0, array_val;
      // loop array, add 1 to counter if current value matches value
      for (array_val of array) {
          if (array_val == value) {
              counter = counter + 1;
          }
      }
      return counter;
  }
  console.log("defined count function");
  
  // other stuff
  thisExp = psychoJS.experiment;
  win = psychoJS.window;
  event = psychoJS.eventManager;
  
  
  // range() (adapted from Becca Hirst's version)
  var range = function(start, stop) {
      var start, stop;
      // careful, as in the Python equivalent,  
      // start is included in the range, stop isn't
      return [...Array(stop-1).keys()].map(i => i + start);
  }
  
  // function to check if value is unique
  var isUnique = function(value, index, array) {
      var value, index, array;
    return array.indexOf(value) === array.lastIndexOf(value);
  }
  
  // only get unique values from array (python "set" function)
  var set = function(array){
      var array;
      return array.filter(isUnique);
  }
  // create JS-friendly custom "numpy" functions
  
  // np.min()
  var minimum = function(data) {
      var data, min_value = data[0];
      for (var val, _pj_c = 0, _pj_a = data, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
          val = _pj_a[_pj_c];
          if ((val < min_value)) {
              min_value = val;
          }
      }
      return min_value;
  }
  console.log("defined min function");
  
  // np.max()
  var maximum = function(data) {
      var data, max_value= data[0];
      for (var val, _pj_c = 0, _pj_a = data, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
          val = _pj_a[_pj_c];
          if ((val > max_value)) {
              max_value = val;
          }
      }
      return max_value;
  }
  console.log("defined max function");
  
  // np.mean()
  var mean = function(data) {
      var data;
      return Number.parseFloat((util.sum(data) / data.length));
  }
  console.log("defined mean function");
  
  // np.var()
  var variance = function(data) {
      var data, mu = mean(data), variance = 0;
      for (var val, _pj_c = 0, _pj_a = data, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
          val = _pj_a[_pj_c];
          variance = (variance + Math.pow((val - mu), 2));
      }
      variance = (variance / data.length);
      return variance;
  }
  console.log("defined variance function");
  
  // np.std()
  var std = function(data) {
      var data;
      return sqrt(variance(data));
  }
  console.log("defined std function");
  // function for drawing w/o replacement from list that is 
  // smaller than sample you want to draw
  // --> Idea: draw w/o replacement, start over again if you run out of 
  //           values, then shuffle your sample
  // draw without replacement from list with sample size > list
  // start over again if no values left for drawing, shuffle everything in the end
  var draw_without_replacement = function(sampling_list, sample_size) {
      // set variables
      var sampling_list, sample_size, rep_sampling_list, rep_times, value, times;
      // repeat colour_codes_list as often as needed
      rep_times = Math.floor((sample_size / sampling_list.length));
      rep_sampling_list = repeat.call(this, value = sampling_list, times = rep_times);
  
      // check if we need some more values, if yes, draw some randomly 
      // from colour_codes and append to our list
      if ((rep_sampling_list.length < sample_size)) {
          var array1, array2, k;
          rep_sampling_list = extend.call(this, array1 = rep_sampling_list, array2 = random_sample.call(this, sampling_list, k = (sample_size - rep_sampling_list.length)));
      }
      // shuffle everything
      rep_sampling_list = random_shuffle.call(this, rep_sampling_list);
      return rep_sampling_list;
  }
  console.log("defined sample w/o replacement function");
  
  
  // generate font color n-back stimulus list for given...
  // ... n-back level (= nback_level)
  // ... stimulus list (= colour_codes)
  // ... words (= story)
  // ... min. abs. number of targets (= target_abs_min)
  // ... max. target to non-target ratio (= targets_max)
  // ... min. target to non-target ratio (= targets_min)
  // ﻿... zeroback target stimulus (zeroback_target = None)
  
  var create_nback_stimlist = function(nback_level, colour_codes, story, target_abs_min, targets_max, targets_min, zeroback_target = null) {
  
    // set all variables I use in this script
    var nback_level, colour_codes, story, target_abs_min, targets_max, targets_min, zeroback_target,
    sampling_list, sample_size, rep_sampling_list, rep_times,
    change_prob_cutoff_lower, change_prob_cutoff_upper, change_prob_equal,
    chunk_missing, chunk_nr, chunk_size, colour_before, colour_codes_replacements,
    colourpairs_dict, curr_colour, curr_target, found_target_nr, idx_replacements,
    indices_targets, max_change_prob, max_target_prob, min_change_prob, min_target_prob,
    missing_chunk, not_this_colour, nr_replacements, pairs, random_colour_list, rep_colours,
    replacement_colour, start, target, target_colours, target_colours_equal, target_count,
    target_nr, target_prob_cutoff_lower, target_prob_cutoff_upper,
    targetcolours_dict, targets_percent;
  
    // create pseudorandomized list of colour codes
    // idea: generate small random lists of colour codes with a balanced number of colours, then append them so I get an even distribution of colour codes & even numbers of colour codes over the whole block
  
    // chunk size should be number of distinct stimuli x 3, so there can't be more than 6x the same stimulus in a row if we concatenate 2 chunks
    chunk_size = colour_codes.length * 3;
    // given the chunk size and the number of stimuli we need, how many chunks do we need?
    chunk_nr = Number.parseInt(story.length / chunk_size);
    // check if there are still stimuli missing that we have to add at the end
    chunk_missing = story.length - chunk_size * chunk_nr;
    
    // placeholder for the colour list we want to create
    random_colour_list = [];
    
    // loop whole chunks, generate small stim list, append the lists
    for (var chunk = 0, _pj_a = chunk_nr; chunk < _pj_a; chunk += 1) {
      rep_colours = draw_without_replacement.call(this, sampling_list = colour_codes, sample_size = chunk_size);
      random_colour_list = extend.call(this, random_colour_list, rep_colours);
    }
  
    // if there are not enough values, randomly sample some and add them
    // to the end of the colour list
    if (chunk_missing > 0) {
      missing_chunk = draw_without_replacement.call(this, sampling_list = colour_codes, sample_size = chunk_missing);
      random_colour_list = extend.call(this, random_colour_list, missing_chunk);
    }
  
    // count how many targets there are (using the given n-back level)
    target =  [];
    
    // loop colour list, check if current value matches either a target stimulus (0-back) or the nth previous stimulus (1-back to 3-back)
    for (var colour_idx = 0, _pj_a = random_colour_list.length; colour_idx < _pj_a; colour_idx += 1) {
      
      if (colour_idx >= nback_level) {
        if (nback_level === 0) {
          curr_colour = random_colour_list[colour_idx];
          // 0-back: if the current colour is a target, save as true in curr_target
          curr_target = curr_colour === zeroback_target;
        } else {
          curr_colour = random_colour_list[colour_idx];
          colour_before = random_colour_list[colour_idx - nback_level];
          // 1-back to 3-back: if the current colour is a target, save as true in curr_target
          curr_target = curr_colour === colour_before;
        }
        // append curr_target to target list
        target = extend.call(this, target, curr_target);
      } else {
        // if it's not a target, save as false
        target = extend.call(this, target, false);
      }
    }
  
    // count how many targets (aka true values) we have:
    var array, value;
    target_count = count.call(this, array = target, value = true);
  
    // if we have more targets than min. target ratio and less than max. target ratio and at least the min target count, everything's fine
    if (target_count / target.length >= targets_min && target_count / target.length <= targets_max && target_count >= target_abs_min) {
      target_nr = target_count;
    // if our target count is not in the correct range...
    } else {
      
      // if we don't have enough targets or too many targets...
      if (target_count / target.length < targets_min || target_count / target.length > targets_max || target_count < target_abs_min) {
        found_target_nr = false;
        
        // randomly draw a target number to use for adding/taking away targets
        while (found_target_nr === false) {
          var min, max;
          targets_percent = uniform.call(this, min = targets_min, max = targets_max);
          target_nr = Math.floor(story.length * targets_percent);
          
          if (target_nr >= target_abs_min) {
            found_target_nr = true;
          }
        }
        // if there are targets missing:
        if (target_count - target_nr < 0) {
          nr_replacements = Number.parseInt(abs(target_count - target_nr));
          indices_targets = [];
          // get indices of random false values in target list
          for (var t = 0, _pj_a = target.length; t < _pj_a; t += 1) {
            if (target[t] === false) {
              
              indices_targets = extend.call(this, indices_targets, t);
            }
          }
          // if it's a 0-back task, you can start adding targets at the first position of the colour list
          if (nback_level === 0) {
            start = 0;
          // if it's at least a 1-back, we have to move a few elements down the list to be able to start comparing to predecessors
          } else {
            start = nback_level - 1;
          }
          var k;
          idx_replacements = random_sample.call(this, indices_targets.slice(start, indices_targets.length), k =  nr_replacements);
          
          // start replacing non-targets by targets by replacing them either by a target colour or the colour n trials before
          for (var replace_this_colour, _pj_c = 0, _pj_a = idx_replacements, _pj_b = _pj_a.length; _pj_c < _pj_b; _pj_c += 1) {
            replace_this_colour = _pj_a[_pj_c];
            
            // 0-back: replace non-target by target colour
            if (nback_level === 0) {
              replacement_colour = zeroback_target;
            // 1-back to 3-back: replace by colour from n trials before
            } else {
              replacement_colour = random_colour_list[replace_this_colour - nback_level];
            }
  
            random_colour_list[replace_this_colour] = replacement_colour;
            // change non-target to target in target counter list
            target[replace_this_colour] = true;
          }
  
        // too many targets, get rid of some
        } else {
          if (target_count - target_nr > 0) {
            nr_replacements = Number.parseInt(abs(target_count - target_nr));
            indices_targets = [];
            // find indices of targets
            for (var t = 0, _pj_a = target.length; t < _pj_a; t += 1) {
              
              if (target[t] === true) {
                indices_targets = extend.call(this, indices_targets, t);
              }
            }
            // get random indices of targets (as many as we need to replace)
            idx_replacements = random_sample.call(this, indices_targets, k = nr_replacements);
            
            // replace target by non-target colour (aka colour that doesn't match target colour for 0-back or target colour from n trials before (for 1-back to 3-back))
            for (var replace_this_colour, _pj_c = 0, _pj_a = idx_replacements, _pj_b = _pj_a.length; _pj_c < _pj_b; _pj_c += 1) {
              replace_this_colour = _pj_a[_pj_c];
  
              if (random_colour_list.length - 1 >= replace_this_colour + nback_level) {
                  
                if (nback_level === 0) {
                  not_this_colour = zeroback_target;
                } else {
                  not_this_colour = random_colour_list[replace_this_colour + nback_level];
                }
  
                colour_codes_replacements = colour_codes.copy();
                colour_codes_replacements.remove(not_this_colour);
                replacement_colour = random_sample.call(this, colour_codes_replacements, k = 1)[0];
              } else {
                replacement_colour = random_sample.call(this, colour_codes, k = 1)[0];
              }
  
              random_colour_list[replace_this_colour] = replacement_colour;
              target[replace_this_colour] = false;
            }
          }
        }
      }
    }
    // now check if colour transition probabilities are more or less evenly distributed
    var _pj;
  
    var change_prob_cutoff_lower, change_prob_cutoff_upper, change_prob_equal, curr_colour, idx_pair, idx_target_colour, max_change_prob, max_target_prob, min_change_prob, min_target_prob, pairs, pairs_counter, target_colour, target_colours, target_colours_counter, target_colours_equal, target_prob_cutoff_lower, target_prob_cutoff_upper;
  
    function _pj_snippets(container) {
      function in_es6(left, right) {
        if (right instanceof Array || typeof right === "string") {
          return right.indexOf(left) > -1;
        } else {
          if (right instanceof Map || right instanceof Set || right instanceof WeakMap || right instanceof WeakSet) {
            return right.has(left);
          } else {
            return left in right;
          }
        }
      }
  
      container["in_es6"] = in_es6;
      return container;
    }
  
    _pj = {};
  
    _pj_snippets(_pj);
  
    pairs = [];
    pairs_counter = [];
  
    for (var idx = 0, _pj_a = random_colour_list.length - 1; idx < _pj_a; idx += 1) {
      curr_colour = random_colour_list[idx] + " -> " + random_colour_list[idx + 1];
  
      if (_pj.in_es6(curr_colour, pairs)) {
        idx_pair = pairs.index(curr_colour);
        pairs_counter[idx_pair] += 1;
      } else {
        extend.call(this, pairs, curr_colour);
        extend.call(this, pairs_counter, 1);
      }
    }
  
    change_prob_cutoff_lower = mean(pairs_counter) - 2 * std(pairs_counter);
    change_prob_cutoff_upper = mean(pairs_counter) + 2 * std(pairs_counter);
    min_change_prob = minimum(pairs_counter);
    max_change_prob = maximum(pairs_counter);
  
    if (min_change_prob < change_prob_cutoff_lower || max_change_prob > change_prob_cutoff_upper) {
      change_prob_equal = false;
    } else {
      change_prob_equal = true;
    }
  
    target_colours = [];
    target_colours_counter = [];
  
    for (var t = 0, _pj_a = target.length; t < _pj_a; t += 1) {
      if (target[t] === true) {
        target_colour = random_colour_list[t];
      }
  
      if (_pj.in_es6(target_colour, target_colours)) {
        idx_target_colour = target_colours.index(target_colour);
        target_colours_counter[idx_target_colour] += 1;
      } else {
        extend.call(this, target_colours, target_colour);
        extend.call(this, target_colours_counter, 1);
      }
    }
  
    target_prob_cutoff_lower = mean(target_colours_counter) - 2 * std(target_colours_counter);
    target_prob_cutoff_upper = mean(target_colours_counter) + 2 * std(target_colours_counter);
    min_target_prob = minimum(target_colours_counter);
    max_target_prob = maximum(target_colours_counter);
  
    if (min_target_prob < target_prob_cutoff_lower || max_target_prob > target_prob_cutoff_upper) {
      target_colours_equal = false;
    } else {
      target_colours_equal = true;
    }
  
    // if everything's fine...
    if (target_colours_equal && change_prob_equal) {
      // return colour list
      return random_colour_list;
    // if change probabilities or distribution of target colours is not balanced...
    } else {
      // recursion: generate new colour list
      return create_nback_stimlist(nback_level, colour_codes, story, target_abs_min, targets_max, targets_min, zeroback_target);
    }
  }
  console.log("defined nback generator function");
  
  
  var story = Array(1000).fill("some_word");
  var nback_level, colour_codes, story, target_abs_min, targets_max, targets_min, zeroback_target;
  var test = create_nback_stimlist.call(this, nback_level = 2, colour_codes = ["r", "b", "g", "y", "o"], story = story, target_abs_min = 100, targets_max = 4/10, targets_min = 2/12, zeroback_target = null);
  test = test[0]
  console.log("defined var test");
  
  loading1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'loading1',
    text: 'Studie lädt…',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "consent_onl"
  consent_onlClock = new util.Clock();
  loading2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'loading2',
    text: 'Studie lädt…',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "end_no_consent"
  end_no_consentClock = new util.Clock();
  end1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'end1',
    text: 'Vielen Dank, \nSie können dieses Fenster \nnun schließen!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "demogr_onl"
  demogr_onlClock = new util.Clock();
  loading3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'loading3',
    text: 'Studie lädt…',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "end_excluded"
  end_excludedClock = new util.Clock();
  
  
  
  end2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'end2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instr_1"
  instr_1Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var settingsComponents;
function settingsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'settings'-------
    t = 0;
    settingsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    settingsComponents = [];
    settingsComponents.push(loading1);
    
    for (const thisComponent of settingsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function settingsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'settings'-------
    // get current time
    t = settingsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *loading1* updates
    if (t >= 0.0 && loading1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loading1.tStart = t;  // (not accounting for frame time here)
      loading1.frameNStart = frameN;  // exact frame index
      
      loading1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loading1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loading1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of settingsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function settingsRoutineEnd() {
  return async function () {
    //------Ending Routine 'settings'-------
    for (const thisComponent of settingsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var params;
var continue_routine;
var consent_onlComponents;
function consent_onlRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'consent_onl'-------
    t = 0;
    consent_onlClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // This routine should not start straight away or the screen width and height
    // may be incorrect.
    
    expInfo['xRes'] = screen.width;
    expInfo['yRes'] = screen.height;
    console.log("screen xRes",expInfo['xRes']);
    console.log("screen yRes",expInfo['yRes']);
    
    //let src = ('demographics.html?xRes='+expInfo['xRes']+'&yRes='+expInfo['yRes']);
    //let src = ('informed_consent.html');
    let src = ('comprehension_questions/Qs_Text1.html');
    
    params = {};  // Results added here after form is submitted
    continue_routine = true; // Routines can't be ended from within Begin Routine
    $(document).ready(function() {
        // Add custom contents from html file using an iframe:
        $('body').append('<div id="iframe-o" style="visibility: hidden; position: relative; display: table; margin: auto; overflow-x: hidden; overflow-y: scroll !important; -webkit-overflow-y-scrolling:touch !important;"><div id="iframe-m" style="display: table-cell; vertical-align: middle;"><div id="iframe-i" style="display: inline-block; width:100%; overflow-y: hidden; overflow-x: hidden;"><iframe id="iframe" src="'+src+'" frameborder="0" style="width: 100%; overflow-y: hidden; overflow-x: hidden; "></iframe></div></div></div>');
        $('#iframe').on('load',function(iframe){
            // Auto-adjust iframe size:
            $(this).contents().find('html').css({ 'display': 'table', 'width': '100%', 'overflow-x': 'hidden' });
            $('#iframe-o').height($(window).height()-20, true);
            $('#iframe-m').width($(this).contents().find('html').width()+100);
           $('#iframe-i').height ( Math.max ( $(this).contents().find('html').height()+20, $(window).height()-20 ), true );
            $(this).height($(this).contents().find('html').height());
            $('#iframe-o').css('visibility','visible');
    
            // If iframe contains a form, then capture its output:
            $(this).contents().find('form').on('submit',function(e){
                e.preventDefault();
                $.each($(this).serializeArray(),function(i, param){
                    params[param.name] = param.value;
                    psychoJS.experiment.addData(param.name, param.value);
                });
                console.log ( 'DEBUG:FRM', params );
                // Remove iframe and continue to next routine when done:
                $('#iframe-o').remove();
                continue_routine = false;
            });
        });
    });
    //$('#iframe').attr( 'src', function(i,val){ return val;} );
    // keep track of which components have finished
    consent_onlComponents = [];
    consent_onlComponents.push(loading2);
    
    for (const thisComponent of consent_onlComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function consent_onlRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'consent_onl'-------
    // get current time
    t = consent_onlClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *loading2* updates
    if (t >= 0.0 && loading2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loading2.tStart = t;  // (not accounting for frame time here)
      loading2.frameNStart = frameN;  // exact frame index
      
      loading2.setAutoDraw(true);
    }

    continueRoutine = continue_routine;
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of consent_onlComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consent_onlRoutineEnd() {
  return async function () {
    //------Ending Routine 'consent_onl'-------
    for (const thisComponent of consent_onlComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // expInfo variables appear on every line in the data file
    // after they are created.
    expInfo['consent'] = psychoJS.experiment._currentTrialData['consent'];
    
    // the Routine "consent_onl" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var end_no_consentComponents;
function end_no_consentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'end_no_consent'-------
    t = 0;
    end_no_consentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((expInfo["consent"] === "False")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    end_no_consentComponents = [];
    end_no_consentComponents.push(end1);
    
    for (const thisComponent of end_no_consentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_no_consentRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'end_no_consent'-------
    // get current time
    t = end_no_consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end1* updates
    if (t >= 0.0 && end1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end1.tStart = t;  // (not accounting for frame time here)
      end1.frameNStart = frameN;  // exact frame index
      
      end1.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_no_consentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_no_consentRoutineEnd() {
  return async function () {
    //------Ending Routine 'end_no_consent'-------
    for (const thisComponent of end_no_consentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "end_no_consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var demogr_onlComponents;
function demogr_onlRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'demogr_onl'-------
    t = 0;
    demogr_onlClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // This routine should not start straight away or the screen width and height
    // may be incorrect.
    
    expInfo['xRes'] = screen.width;
    expInfo['yRes'] = screen.height;
    console.log("screen xRes",expInfo['xRes']);
    console.log("screen yRes",expInfo['yRes']);
    
    //let src = ('demographics.html?xRes='+expInfo['xRes']+'&yRes='+expInfo['yRes']);
    let src = ('demographics.html');
    
    params = {};  // Results added here after form is submitted
    continue_routine = true; // Routines can't be ended from within Begin Routine
    $(document).ready(function() {
        // Add custom contents from html file using an iframe:
        $('body').append('<div id="iframe-o" style="visibility: hidden; position: relative; display: table; margin: auto; overflow-x: hidden; overflow-y: scroll !important; -webkit-overflow-y-scrolling:touch !important;"><div id="iframe-m" style="display: table-cell; vertical-align: middle;"><div id="iframe-i" style="display: inline-block; width:100%; overflow-y: hidden; overflow-x: hidden;"><iframe id="iframe" src="'+src+'" frameborder="0" style="width: 100%; overflow-y: hidden; overflow-x: hidden; "></iframe></div></div></div>');
        $('#iframe').on('load',function(iframe){
            // Auto-adjust iframe size:
            $(this).contents().find('html').css({ 'display': 'table', 'width': '100%', 'overflow-x': 'hidden' });
            $('#iframe-o').height($(window).height()-20, true);
            $('#iframe-m').width($(this).contents().find('html').width()+100);
           $('#iframe-i').height ( Math.max ( $(this).contents().find('html').height()+20, $(window).height()-20 ), true );
            $(this).height($(this).contents().find('html').height());
            $('#iframe-o').css('visibility','visible');
    
            // If iframe contains a form, then capture its output:
            $(this).contents().find('form').on('submit',function(e){
                e.preventDefault();
                $.each($(this).serializeArray(),function(i, param){
                    params[param.name] = param.value;
                    psychoJS.experiment.addData(param.name, param.value);
                });
                console.log ( 'DEBUG:FRM', params );
                // Remove iframe and continue to next routine when done:
                $('#iframe-o').remove();
                continue_routine = false;
            });
        });
    });
    //$('#iframe').attr( 'src', function(i,val){ return val;} );
    // keep track of which components have finished
    demogr_onlComponents = [];
    demogr_onlComponents.push(loading3);
    
    for (const thisComponent of demogr_onlComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function demogr_onlRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'demogr_onl'-------
    // get current time
    t = demogr_onlClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *loading3* updates
    if (t >= 0.0 && loading3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loading3.tStart = t;  // (not accounting for frame time here)
      loading3.frameNStart = frameN;  // exact frame index
      
      loading3.setAutoDraw(true);
    }

    continueRoutine = continue_routine;
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of demogr_onlComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demogr_onlRoutineEnd() {
  return async function () {
    //------Ending Routine 'demogr_onl'-------
    for (const thisComponent of demogr_onlComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // expInfo variables appear on every line in the data file
    // after they are created.
    expInfo['ID'] = psychoJS.experiment._currentTrialData['ID'];
    expInfo['gender'] = psychoJS.experiment._currentTrialData['gender'];
    expInfo['age'] = psychoJS.experiment._currentTrialData['age'];
    
    expInfo['native_speaker'] = psychoJS.experiment._currentTrialData['native_speaker'];
    expInfo['literacy'] = psychoJS.experiment._currentTrialData['literacy'];
    expInfo['dyslexia'] = psychoJS.experiment._currentTrialData['dyslexia'];
    expInfo['reading_freq'] = psychoJS.experiment._currentTrialData['reading_freq'];
    expInfo['reading_joy'] = psychoJS.experiment._currentTrialData['reading_joy'];
    
    expInfo['handedness'] = psychoJS.experiment._currentTrialData['handedness'];
    
    expInfo['impaired_eyesight'] = psychoJS.experiment._currentTrialData['impaired_eyesight'];
    expInfo['impaired_eyesight_correction'] = psychoJS.experiment._currentTrialData['impaired_eyesight_correction'];
    expInfo['colour_blindness'] = psychoJS.experiment._currentTrialData['colour_blindness'];
    
    expInfo['disease'] = psychoJS.experiment._currentTrialData['disease'];
    expInfo['drugs_last_month'] = psychoJS.experiment._currentTrialData['drugs_last_month'];
    expInfo['alcohol_drugs_now'] = psychoJS.experiment._currentTrialData['alcohol_drugs_now'];
    
    expInfo['tired'] = psychoJS.experiment._currentTrialData['tired'];
    expInfo['distractions'] = psychoJS.experiment._currentTrialData['distractions'];
    // the Routine "demogr_onl" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var end_excludedComponents;
function end_excludedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'end_excluded'-------
    t = 0;
    end_excludedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // skip this component if participant 
    // is eligible to participate in the study
    
    // get some of the "hard" exclusion criteria
    var age_minor = (expInfo["age"] < 18);
    var non_native = (expInfo["native_speaker"] === false);
    var illiteracy = (expInfo["literacy"] === false);
    var dyslexia = (expInfo["dyslexia"] === true);
    var colourblind = (expInfo["colour_blindness"] === true);
    var disease = (expInfo["disease"] === true);
    var drugs1 = (expInfo["drugs_last_month"] === true);
    var drugs2 = (expInfo["alcohol_drugs_now"] === true);
    
    var excl_criteria = [age_minor, non_native, illiteracy, dyslexia, colourblind, disease, drugs1, drugs2];
    
    // skip routine if any of the exclusion criteria apply
    var excl_criteria = [age_minor, non_native, illiteracy, dyslexia, colourblind, disease, drugs1, drugs2];
    var show_this_slide = false;
    for (var criterium, _pj_c = 0, _pj_a = excl_criteria, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        criterium = _pj_a[_pj_c];
        if ((criterium === true)) {
            show_this_slide = true;
        } 
    }
    
    if ((show_this_slide === false)) {
            continueRoutine = false;
        } else {
            continueRoutine = true;
        }
    end2.setText('Vielen Dank für Ihr Interesse an unserer Studie!\n\nLeider erfüllen Sie nicht alle Teilnahmekriterien. \n\nSie können dieses Fenster nun schließen.');
    // keep track of which components have finished
    end_excludedComponents = [];
    end_excludedComponents.push(end2);
    
    for (const thisComponent of end_excludedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_excludedRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'end_excluded'-------
    // get current time
    t = end_excludedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end2* updates
    if (t >= 0.0 && end2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end2.tStart = t;  // (not accounting for frame time here)
      end2.frameNStart = frameN;  // exact frame index
      
      end2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_excludedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_excludedRoutineEnd() {
  return async function () {
    //------Ending Routine 'end_excluded'-------
    for (const thisComponent of end_excludedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "end_excluded" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instr_1Components;
function instr_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instr_1'-------
    t = 0;
    instr_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text.setText('Vielen Dank für Ihr Interesse an unserer Studie! \n\n—> Instructions for training go here');
    // keep track of which components have finished
    instr_1Components = [];
    instr_1Components.push(text);
    
    for (const thisComponent of instr_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instr_1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instr_1'-------
    // get current time
    t = instr_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instr_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_1RoutineEnd() {
  return async function () {
    //------Ending Routine 'instr_1'-------
    for (const thisComponent of instr_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "instr_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
