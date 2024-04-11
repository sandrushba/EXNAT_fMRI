/********************** 
 * Exnat-3_Pilot *
 **********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'EXNAT-3_pilot';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
    'testing_mode': 'yes',
};

// Start code blocks for 'Before Experiment'
import {visual} from 'psychopy';
import * as datetime from 'datetime';
import * as np from 'numpy';
import * as random from 'random';
import * as pd from 'pandas';
import * as time from 'time';
import {instr_1back_dual_main, instr_1back_single_main, instr_1back_single_training1, instr_1back_single_training2, instr_2back_dual_main, instr_2back_single_main, instr_2back_single_training1, instr_2back_single_training2, instr_Reading_Baseline_main, instr_Reading_Baseline_training, instr_click_training, instr_pic_1back_dual_main, instr_pic_1back_single_main, instr_pic_1back_single_training1, instr_pic_1back_single_training2, instr_pic_2back_dual_main, instr_pic_2back_single_main, instr_pic_2back_single_training1, instr_pic_2back_single_training2, instr_pic_Reading_Baseline_main, instr_pic_Reading_Baseline_training, instr_pic_click_training, instr_pic_path, instr_pic_vis_task, instr_vis_task_1, instr_vis_task_2, reading_bl_tr_Q1, reading_bl_tr_Q1_ans, reading_bl_tr_Q1_corr, reading_bl_tr_Q2, reading_bl_tr_Q2_ans, reading_bl_tr_Q2_corr, reading_bl_tr_Q3, reading_bl_tr_Q3_ans, reading_bl_tr_Q3_corr, reading_bl_tr_text, text_01, text_01_Q1, text_01_Q1_ans, text_01_Q1_corr, text_01_Q2, text_01_Q2_ans, text_01_Q2_corr, text_01_Q3, text_01_Q3_ans, text_01_Q3_corr, text_02, text_02_Q1, text_02_Q1_ans, text_02_Q1_corr, text_02_Q2, text_02_Q2_ans, text_02_Q2_corr, text_02_Q3, text_02_Q3_ans, text_02_Q3_corr, text_03, text_03_Q1, text_03_Q1_ans, text_03_Q1_corr, text_03_Q2, text_03_Q2_ans, text_03_Q2_corr, text_03_Q3, text_03_Q3_ans, text_03_Q3_corr, text_04, text_04_Q1, text_04_Q1_ans, text_04_Q1_corr, text_04_Q2, text_04_Q2_ans, text_04_Q2_corr, text_04_Q3, text_04_Q3_ans, text_04_Q3_corr, text_05, text_05_Q1, text_05_Q1_ans, text_05_Q1_corr, text_05_Q2, text_05_Q2_ans, text_05_Q2_corr, text_05_Q3, text_05_Q3_ans, text_05_Q3_corr, text_06, text_06_Q1, text_06_Q1_ans, text_06_Q1_corr, text_06_Q2, text_06_Q2_ans, text_06_Q2_corr, text_06_Q3, text_06_Q3_ans, text_06_Q3_corr, text_07, text_07_Q1, text_07_Q1_ans, text_07_Q1_corr, text_07_Q2, text_07_Q2_ans, text_07_Q2_corr, text_07_Q3, text_07_Q3_ans, text_07_Q3_corr, text_08, text_08_Q1, text_08_Q1_ans, text_08_Q1_corr, text_08_Q2, text_08_Q2_ans, text_08_Q2_corr, text_08_Q3, text_08_Q3_ans, text_08_Q3_corr, text_09, text_09_Q1, text_09_Q1_ans, text_09_Q1_corr, text_09_Q2, text_09_Q2_ans, text_09_Q2_corr, text_09_Q3, text_09_Q3_ans, text_09_Q3_corr, text_10, text_10_Q1, text_10_Q1_ans, text_10_Q1_corr, text_10_Q2, text_10_Q2_ans, text_10_Q2_corr, text_10_Q3, text_10_Q3_ans, text_10_Q3_corr, warning_sign} from 'EXNAT2_texts_MC_Qs';
import {change_bg_colour} from 'EXNAT2_study_components';
import {create_0back_stimlist, create_nback_stimlist, draw_without_replacement, get_targets} from 'nback_colour_generator';
[SCN_W, SCN_H] = [1280, 800];
sys.stdout = open(sys.stdout.fileno(), {"mode": "w", "encoding": "utf8", "buffering": 1});
console.log(sys.executable);
function flatten_list(nested_list) {
    var flattened_list;
    flattened_list = [];
    for (var item, _pj_c = 0, _pj_a = nested_list, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        item = _pj_a[_pj_c];
        if ((item instanceof list)) {
            flattened_list.concat(flatten_list(item));
        } else {
            flattened_list.push(item);
        }
    }
    return flattened_list;
}
function escape_quotes(string) {
    return string.replace("\"", "\"\"");
}
psychoJS.window.setMouseVisible(false);
my_timer = new core.CountdownTimer(0.01);

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'deg',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
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
flowScheduler.add(SettingsRoutineBegin());
flowScheduler.add(SettingsRoutineEachFrame());
flowScheduler.add(SettingsRoutineEnd());
const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin(blocksLoopScheduler));
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);




flowScheduler.add(warning_task_changeRoutineBegin());
flowScheduler.add(warning_task_changeRoutineEachFrame());
flowScheduler.add(warning_task_changeRoutineEnd());
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.WARNING);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "Settings"
  SettingsClock = new util.Clock();
  empty_placeholder = new visual.TextStim({
    win: psychoJS.window,
    name: 'empty_placeholder',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "no_text_training"
  no_text_trainingClock = new util.Clock();
  // Initialize components for Routine "text_blocks_self_paced"
  text_blocks_self_pacedClock = new util.Clock();
  // Initialize components for Routine "text_blocks_paced"
  text_blocks_pacedClock = new util.Clock();
  // Initialize components for Routine "warning_task_change"
  warning_task_changeClock = new util.Clock();
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function SettingsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Settings' ---
    t = 0;
    SettingsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Settings.started', globalClock.getTime());
    // keep track of which components have finished
    SettingsComponents = [];
    SettingsComponents.push(empty_placeholder);
    
    for (const thisComponent of SettingsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function SettingsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Settings' ---
    // get current time
    t = SettingsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *empty_placeholder* updates
    if (t >= 0.0 && empty_placeholder.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      empty_placeholder.tStart = t;  // (not accounting for frame time here)
      empty_placeholder.frameNStart = frameN;  // exact frame index
      
      empty_placeholder.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (empty_placeholder.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      empty_placeholder.setAutoDraw(false);
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
    for (const thisComponent of SettingsComponents)
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

function SettingsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Settings' ---
    for (const thisComponent of SettingsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Settings.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function blocksLoopBegin(blocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    blocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 30, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'blocks'
    });
    psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
    currentLoop = blocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlock of blocks) {
      snapshot = blocks.getSnapshot();
      blocksLoopScheduler.add(importConditions(snapshot));
      blocksLoopScheduler.add(no_text_trainingRoutineBegin(snapshot));
      blocksLoopScheduler.add(no_text_trainingRoutineEachFrame());
      blocksLoopScheduler.add(no_text_trainingRoutineEnd(snapshot));
      blocksLoopScheduler.add(text_blocks_self_pacedRoutineBegin(snapshot));
      blocksLoopScheduler.add(text_blocks_self_pacedRoutineEachFrame());
      blocksLoopScheduler.add(text_blocks_self_pacedRoutineEnd(snapshot));
      blocksLoopScheduler.add(text_blocks_pacedRoutineBegin(snapshot));
      blocksLoopScheduler.add(text_blocks_pacedRoutineEachFrame());
      blocksLoopScheduler.add(text_blocks_pacedRoutineEnd(snapshot));
      blocksLoopScheduler.add(blocksLoopEndIteration(blocksLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function blocksLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(blocks);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function blocksLoopEndIteration(scheduler, snapshot) {
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
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function no_text_trainingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'no_text_training' ---
    t = 0;
    no_text_trainingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('no_text_training.started', globalClock.getTime());
    // Run 'Begin Routine' code from no_text_and_training_2
    /* Syntax Error: Fix Python code */
    // keep track of which components have finished
    no_text_trainingComponents = [];
    
    for (const thisComponent of no_text_trainingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function no_text_trainingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'no_text_training' ---
    // get current time
    t = no_text_trainingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of no_text_trainingComponents)
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

function no_text_trainingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'no_text_training' ---
    for (const thisComponent of no_text_trainingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('no_text_training.stopped', globalClock.getTime());
    // the Routine "no_text_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function text_blocks_self_pacedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'text_blocks_self_paced' ---
    t = 0;
    text_blocks_self_pacedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('text_blocks_self_paced.started', globalClock.getTime());
    // Run 'Begin Routine' code from text_blocks
    /* Syntax Error: Fix Python code */
    // Run 'Begin Routine' code from Q1
    psychoJS.window.setColor(light_bg_col, {"colorSpace": "rgb"});
    psychoJS.window.flip();
    psychoJS.eventManager.clearEvents();
    if (skip_questions) {
        continueRoutine = false;
    } else {
        if (((skip_questions === false) && training_Qs)) {
            Q1 = reading_bl_tr_Q1;
            Q1_answers = reading_bl_tr_Q1_ans;
            Q1_corr = reading_bl_tr_Q1_corr;
        } else {
            if (((skip_questions === false) && (training_Qs === false))) {
                Q1 = locals()[(curr_text_nr + "_Q1")];
                Q1_answers = locals()[(curr_text_nr + "_Q1_ans")];
                Q1_corr = locals()[(curr_text_nr + "_Q1_corr")];
            }
        }
    }
    question_pos = [0, 3];
    answer_xpos = (- 7);
    answer_ypos = [0, (- 2), (- 4), (- 6)];
    question = new visual.TextStim(psychoJS.window, {"text": Q1, "pos": question_pos, "color": "black", "height": 0.5, "font": "Bookman Old Style", "anchorHoriz": "center", "alignText": "center", "wrapWidth": 10});
    answers = function () {
        var _pj_a = [], _pj_b = util.range(Q1_answers.length);
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push(new visual.TextStim(psychoJS.window, {"text": Q1_answers[i], "pos": [answer_xpos, answer_ypos[i]], "color": "black", "height": 0.5, "font": "Bookman Old Style", "wrapWidth": 15, "anchorHoriz": "left", "alignText": "center"}));
        }
        return _pj_a;
    }
    .call(this);
    instr_text = new visual.TextStim(psychoJS.window, {"text": "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuw\u00e4hlen. Mit der Leertaste k\u00f6nnen Sie Ihre Auswahl best\u00e4tigen.)", "color": "grey", "pos": [0, (- 10)], "wrapWidth": 20, "height": 0.4, "font": "Bookman Old Style"});
    question.autoDraw = true;
    instr_text.autoDraw = true;
    for (var answer, _pj_c = 0, _pj_a = answers, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        answer = _pj_a[_pj_c];
        answer.autoDraw = true;
    }
    psychoJS.window.flip();
    Q1_chosen_ans = null;
    while (true) {
        if (psychoJS.eventManager.getKeys(["1"])) {
            console.log("a");
            Q1_chosen_ans = "a";
            answers[0].setColor("green");
            for (var answer, _pj_c = 0, _pj_a = answers.slice(1), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
                answer = _pj_a[_pj_c];
                answer.setColor("black");
                psychoJS.window.flip();
            }
        }
        if (psychoJS.eventManager.getKeys(["2"])) {
            console.log("b");
            Q1_chosen_ans = "b";
            answers[1].setColor("green");
            for (var answer, _pj_c = 0, _pj_a = ([answers[0]] + answers.slice(2)), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
                answer = _pj_a[_pj_c];
                answer.setColor("black");
                psychoJS.window.flip();
            }
        }
        if (psychoJS.eventManager.getKeys(["3"])) {
            console.log("c");
            Q1_chosen_ans = "c";
            answers[2].setColor("green");
            for (var answer, _pj_c = 0, _pj_a = (answers.slice(0, 2) + answers.slice(3)), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
                answer = _pj_a[_pj_c];
                answer.setColor("black");
            }
            psychoJS.window.flip();
        }
        if (psychoJS.eventManager.getKeys(["4"])) {
            console.log("d");
            Q1_chosen_ans = "d";
            answers[3].setColor("green");
            for (var answer, _pj_c = 0, _pj_a = answers.slice(0, (- 1)), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
                answer = _pj_a[_pj_c];
                answer.setColor("black");
            }
            psychoJS.window.flip();
        } else {
            if ((psychoJS.eventManager.getKeys(["space"]) && (Q1_chosen_ans !== null))) {
                break;
            }
        }
    }
    console.log(("answer for Q1:" + Q1_chosen_ans.toString()));
    if ((Q1_chosen_ans === Q1_corr)) {
        console.log("answer correct!");
    } else {
        console.log("answer incorrect!");
    }
    psychoJS.experiment.addData("question", "Q1");
    psychoJS.experiment.addData("chosen_ans", Q1_chosen_ans);
    psychoJS.experiment.addData("ans_correct", (Q1_chosen_ans === Q1_corr));
    psychoJS.experiment.addData("text_nr", curr_text_nr);
    psychoJS.experiment.addData("block_nr", exp_block_counter);
    psychoJS.experiment.addData("block_name", curr_block);
    psychoJS.experiment.addData("block_kind", curr_nback_cond);
    psychoJS.experiment.nextEntry();
    question.autoDraw = false;
    instr_text.autoDraw = false;
    for (var answer, _pj_c = 0, _pj_a = answers, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        answer = _pj_a[_pj_c];
        answer.autoDraw = false;
    }
    
    // Run 'Begin Routine' code from Q3
    ##########################################################
    #            Text Comprehension Questions - Q3           #
    ##########################################################
    
    ### Settings:
    # keep background ivory
    win.setColor(light_bg_col, colorSpace='rgb')
    win.flip()
    
    # clear buffer of all previously recorded key events:
    event.clearEvents()
    
    # check which kind of block we have
    # if there was no text before, we can skip the questions
    if skip_questions:
        continueRoutine = False
    # if we have a training text, set training questions
    elif skip_questions == False and training_Qs:
        Q3 = reading_bl_tr_Q3
        Q3_answers = reading_bl_tr_Q3_ans
        Q3_corr = reading_bl_tr_Q3_corr
        
    # if we have a main text, set regular questions
    elif skip_questions == False and training_Qs == False:
        # load first question for current text & their respective answers
        Q3 = locals()[curr_text_nr + "_Q3"]
        Q3_answers = locals()[curr_text_nr + "_Q3_ans"]
        Q3_corr = locals()[curr_text_nr + "_Q3_corr"]
    
    # Define text positions and formatting
    question_pos = (0, 3)
    answer_xpos = -7 # move questions a bit to the left 
    answer_ypos = [ 0, -2, -4, -6] # set the y axis positions of all 4 answers
    
    # Create text stim for the question:
    question = visual.TextStim(win, 
                               text = Q3, 
                               pos = question_pos,
                               color = "black",
                               height = 0.5,
                               font = "Bookman Old Style",
                               anchorHoriz = 'center',
                               alignText = 'center', 
                               wrapWidth = 10)
    # create 1 text stim for each answer option:
    answers = [visual.TextStim(win, 
                               text = Q3_answers[i], 
                               pos = (answer_xpos, answer_ypos[i]), 
                               color = "black", # set all to black as a default
                               height = 0.5, 
                               font = "Bookman Old Style",
                               wrapWidth = 15,
                               anchorHoriz = 'left', 
                               alignText = 'center') for i in range(len(Q3_answers))]
    # set up instruction text
    instr_text = visual.TextStim(win, 
                                 text = "(Bitte benutzen Sie die Tasten 1, 2, 3 und 4 um die richtige Antwort auszuwählen. Mit der Leertaste können Sie Ihre Auswahl bestätigen.)",
                                 color = "grey",
                                 pos = (0, -10),
                                 wrapWidth = 20,
                                 height = 0.4,
                                 font = "Bookman Old Style")
                                 
    ### Show all on screen until I set .autoDraw = False
    question.autoDraw = True
    instr_text.autoDraw = True
    for answer in answers:
        answer.autoDraw = True
    win.flip()
    
    
    ### Record key responses:
    Q3_chosen_ans = None
    
    while True:        
        # if 1 was pressed...
        if event.getKeys(['1']):
            print('a')
            # save Q3 answer as a 
            Q3_chosen_ans = "a"
            # set font colour of the first answer (answer a) to 
            # green and the rest to black:
            answers[0].setColor("green")
            for answer in answers[1:]:
                answer.setColor("black")
                # draw updated stimulus:
                win.flip()
        # same procedure for all other answer options:
        if event.getKeys(['2']):
            print('b')
            Q3_chosen_ans = "b"
            # set font colour of the second answer (answer b) to 
            # green and the rest to black:
            answers[1].setColor("green")
            for answer in [answers[0]] + answers[2:]:
                answer.setColor("black")
                # draw updated stimulus:
                win.flip()
        if event.getKeys(['3']):
            print('c')
            Q3_chosen_ans = "c"
            # set font colour of the third answer (answer c) to 
            # green and the rest to black:
            answers[2].setColor("green")
            for answer in answers[:2] + answers[3:]:
                answer.setColor("black")
            # draw updated stimulus:
            win.flip()
        if event.getKeys(['4']):
            print('d')
            Q3_chosen_ans = "d"
            # set font colour of the fourth answer (answer d) to 
            # green and the rest to black:
            answers[3].setColor("green")
            for answer in answers[:-1]:
                answer.setColor("black")
            # draw updated stimulus 
            win.flip()
        # if participant pressed "space", check whether they chose an answer.
        # if yes, end this routine and go to next question, if not, wait for valid answer.
        elif event.getKeys(['space']) and Q3_chosen_ans != None:
            break
    
    # print chosen answer for Q3
    print("answer for Q3:" + str(Q3_chosen_ans))
    
    # check if answer was correct:
    if Q3_chosen_ans == Q3_corr: 
        print("answer correct!")
    else: 
        print("answer incorrect!")
        
    # save data:
    thisExp.addData('question', 'Q3')
    thisExp.addData('chosen_ans', Q3_chosen_ans)
    thisExp.addData('ans_correct', Q3_chosen_ans == Q3_corr)
    thisExp.addData('text_nr', curr_text_nr)
    thisExp.addData('block_nr', exp_block_counter)
    thisExp.addData('block_name', curr_block)
    thisExp.addData('block_kind', curr_nback_cond)
    
    # start a new row in the csv
    thisExp.nextEntry()
    
    ### End Q3: Set .autoDraw = False to stop showing question & answers
    question.autoDraw = False
    instr_text.autoDraw = False
    for answer in answers:
        answer.autoDraw = False
    
    # go to next block!
    exp_block_counter += 1
    print("Going to block " + str(exp_block_counter + 1) + "/17 now!")
    continueRoutine = False
    
    # If there are still blocks left, go to next one.
    # If not, end loop here:
    if exp_block_counter == 17:
        blocks.finished = True
    
    # when text rating is included, only use this instead of "go to next block":
    # end current routine
    #continueRoutine = False
    // keep track of which components have finished
    text_blocks_self_pacedComponents = [];
    
    for (const thisComponent of text_blocks_self_pacedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function text_blocks_self_pacedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'text_blocks_self_paced' ---
    // get current time
    t = text_blocks_self_pacedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of text_blocks_self_pacedComponents)
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

function text_blocks_self_pacedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'text_blocks_self_paced' ---
    for (const thisComponent of text_blocks_self_pacedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('text_blocks_self_paced.stopped', globalClock.getTime());
    // the Routine "text_blocks_self_paced" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function text_blocks_pacedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'text_blocks_paced' ---
    t = 0;
    text_blocks_pacedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('text_blocks_paced.started', globalClock.getTime());
    // keep track of which components have finished
    text_blocks_pacedComponents = [];
    
    for (const thisComponent of text_blocks_pacedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function text_blocks_pacedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'text_blocks_paced' ---
    // get current time
    t = text_blocks_pacedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of text_blocks_pacedComponents)
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

function text_blocks_pacedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'text_blocks_paced' ---
    for (const thisComponent of text_blocks_pacedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('text_blocks_paced.stopped', globalClock.getTime());
    // the Routine "text_blocks_paced" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function warning_task_changeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'warning_task_change' ---
    t = 0;
    warning_task_changeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('warning_task_change.started', globalClock.getTime());
    // keep track of which components have finished
    warning_task_changeComponents = [];
    
    for (const thisComponent of warning_task_changeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function warning_task_changeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'warning_task_change' ---
    // get current time
    t = warning_task_changeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of warning_task_changeComponents)
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

function warning_task_changeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'warning_task_change' ---
    for (const thisComponent of warning_task_changeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('warning_task_change.stopped', globalClock.getTime());
    // the Routine "warning_task_change" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    // keep track of which components have finished
    endComponents = [];
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
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

function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
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
