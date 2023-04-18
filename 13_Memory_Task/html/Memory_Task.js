/******************** 
 * Memory_Task Test *
 ********************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.2.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Memory_Task';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
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
flowScheduler.add(introductionRoutineBegin());
flowScheduler.add(introductionRoutineEachFrame());
flowScheduler.add(introductionRoutineEnd());
flowScheduler.add(fourRoutineBegin());
flowScheduler.add(fourRoutineEachFrame());
flowScheduler.add(fourRoutineEnd());
flowScheduler.add(fiveRoutineBegin());
flowScheduler.add(fiveRoutineEachFrame());
flowScheduler.add(fiveRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.2';
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

async function experimentInit() {
  // Initialize components for Routine "introduction"
  introductionClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'image/introduction.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.76, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  introduction_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "four"
  fourClock = new util.Clock();
  concentration_four = new visual.TextStim({
    win: psychoJS.window,
    name: 'concentration_four',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  four_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'four_1',
    text: '8',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  four_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'four_2',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.1), 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  four_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'four_3',
    text: '7',
    font: 'Arial',
    units: undefined, 
    pos: [0.1, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  four_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'four_4',
    text: '4',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  four_input = new visual.TextStim({
    win: psychoJS.window,
    name: 'four_input',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  four_tip = new visual.TextStim({
    win: psychoJS.window,
    name: 'four_tip',
    text: '请顺序输入呈现的数字\n  （回车键结束）',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  
          // add-on: list(s: string): string[]
          function list(s) {
              // if s is a string, we return a list of its characters
              if (typeof s === 'string')
                  return s.split('');
              else
                  // otherwise we return s:
                  return s;
          }
          
          import * as string from 'string';
  var allLetters;
  allLetters = list(string.digits);
  
  // Initialize components for Routine "five"
  fiveClock = new util.Clock();
  concentration_five = new visual.TextStim({
    win: psychoJS.window,
    name: 'concentration_five',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  five_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_1',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.4), 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  five_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_2',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  five_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_3',
    text: '6\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.07)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  five_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_4',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.2, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  five_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_5',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.4, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  five_input = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_input',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  five_tip = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_tip',
    text: '请顺序输入呈现的数字\n  （回车键结束）',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function introductionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'introduction'-------
    t = 0;
    introductionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    introduction_key.keys = undefined;
    introduction_key.rt = undefined;
    _introduction_key_allKeys = [];
    // keep track of which components have finished
    introductionComponents = [];
    introductionComponents.push(image);
    introductionComponents.push(introduction_key);
    
    for (const thisComponent of introductionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function introductionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'introduction'-------
    // get current time
    t = introductionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    
    // *introduction_key* updates
    if (t >= 0.0 && introduction_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      introduction_key.tStart = t;  // (not accounting for frame time here)
      introduction_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { introduction_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { introduction_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { introduction_key.clearEvents(); });
    }

    if (introduction_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = introduction_key.getKeys({keyList: ['space'], waitRelease: false});
      _introduction_key_allKeys = _introduction_key_allKeys.concat(theseKeys);
      if (_introduction_key_allKeys.length > 0) {
        introduction_key.keys = _introduction_key_allKeys[_introduction_key_allKeys.length - 1].name;  // just the last key pressed
        introduction_key.rt = _introduction_key_allKeys[_introduction_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
    for (const thisComponent of introductionComponents)
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

function introductionRoutineEnd() {
  return async function () {
    //------Ending Routine 'introduction'-------
    for (const thisComponent of introductionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    introduction_key.stop();
    // the Routine "introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function fourRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'four'-------
    t = 0;
    fourClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textFill = "";
    
    // keep track of which components have finished
    fourComponents = [];
    fourComponents.push(concentration_four);
    fourComponents.push(four_1);
    fourComponents.push(four_2);
    fourComponents.push(four_3);
    fourComponents.push(four_4);
    fourComponents.push(four_input);
    fourComponents.push(four_tip);
    
    for (const thisComponent of fourComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function fourRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'four'-------
    // get current time
    t = fourClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *concentration_four* updates
    if (t >= 0.0 && concentration_four.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      concentration_four.tStart = t;  // (not accounting for frame time here)
      concentration_four.frameNStart = frameN;  // exact frame index
      
      concentration_four.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (concentration_four.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      concentration_four.setAutoDraw(false);
    }
    
    // *four_1* updates
    if (t >= 0.5 && four_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four_1.tStart = t;  // (not accounting for frame time here)
      four_1.frameNStart = frameN;  // exact frame index
      
      four_1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (four_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      four_1.setAutoDraw(false);
    }
    
    // *four_2* updates
    if (t >= 0.8 && four_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four_2.tStart = t;  // (not accounting for frame time here)
      four_2.frameNStart = frameN;  // exact frame index
      
      four_2.setAutoDraw(true);
    }

    frameRemains = 0.8 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (four_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      four_2.setAutoDraw(false);
    }
    
    // *four_3* updates
    if (t >= 1.1 && four_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four_3.tStart = t;  // (not accounting for frame time here)
      four_3.frameNStart = frameN;  // exact frame index
      
      four_3.setAutoDraw(true);
    }

    frameRemains = 1.1 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (four_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      four_3.setAutoDraw(false);
    }
    
    // *four_4* updates
    if (t >= 1.4 && four_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four_4.tStart = t;  // (not accounting for frame time here)
      four_4.frameNStart = frameN;  // exact frame index
      
      four_4.setAutoDraw(true);
    }

    frameRemains = 1.4 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (four_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      four_4.setAutoDraw(false);
    }
    
    // *four_input* updates
    if (t >= 1.7 && four_input.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four_input.tStart = t;  // (not accounting for frame time here)
      four_input.frameNStart = frameN;  // exact frame index
      
      four_input.setAutoDraw(true);
    }

    
    // *four_tip* updates
    if (t >= 1.7 && four_tip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four_tip.tStart = t;  // (not accounting for frame time here)
      four_tip.frameNStart = frameN;  // exact frame index
      
      four_tip.setAutoDraw(true);
    }

    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    if (_pj.in_es6("escape", keys)) {
        core.quit();
    } else {
        if (keys) {
            if ((keys[0] === "space")) {
                textFill += " ";
            } else {
                if ((keys[0] === "backspace")) {
                    textFill = textFill.slice(0, (- 1));
                } else {
                    if (_pj.in_es6(keys[0], allLetters)) {
                        textFill += keys[0];
                    }
                }
            }
            four_input.setText(textFill);
            if ((keys[0] === "return")) {
                textFill.strip();
                psychoJS.experiment.addData("four", textFill);
                if ((textFill === "8174")) {
                    console.log(textFill);
                    psychoJS.experiment.addData("four_corr", 1);
                    psychoJS.experiment.entry();
                } else {
                    console.log(textFill);
                    psychoJS.experiment.addData("four_corr", 0);
                    psychoJS.experiment.entry();
                }
                four_input.setText(textFill);
                continueRoutine = false;
            }
        }
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
    for (const thisComponent of fourComponents)
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

function fourRoutineEnd() {
  return async function () {
    //------Ending Routine 'four'-------
    for (const thisComponent of fourComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "four" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function fiveRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'five'-------
    t = 0;
    fiveClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textFill = "";
    
    // keep track of which components have finished
    fiveComponents = [];
    fiveComponents.push(concentration_five);
    fiveComponents.push(five_1);
    fiveComponents.push(five_2);
    fiveComponents.push(five_3);
    fiveComponents.push(five_4);
    fiveComponents.push(five_5);
    fiveComponents.push(five_input);
    fiveComponents.push(five_tip);
    
    for (const thisComponent of fiveComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function fiveRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'five'-------
    // get current time
    t = fiveClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *concentration_five* updates
    if (t >= 0.0 && concentration_five.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      concentration_five.tStart = t;  // (not accounting for frame time here)
      concentration_five.frameNStart = frameN;  // exact frame index
      
      concentration_five.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (concentration_five.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      concentration_five.setAutoDraw(false);
    }
    
    // *five_1* updates
    if (t >= 0.5 && five_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_1.tStart = t;  // (not accounting for frame time here)
      five_1.frameNStart = frameN;  // exact frame index
      
      five_1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (five_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      five_1.setAutoDraw(false);
    }
    
    // *five_2* updates
    if (t >= 0.8 && five_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_2.tStart = t;  // (not accounting for frame time here)
      five_2.frameNStart = frameN;  // exact frame index
      
      five_2.setAutoDraw(true);
    }

    frameRemains = 0.8 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (five_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      five_2.setAutoDraw(false);
    }
    
    // *five_3* updates
    if (t >= 1.1 && five_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_3.tStart = t;  // (not accounting for frame time here)
      five_3.frameNStart = frameN;  // exact frame index
      
      five_3.setAutoDraw(true);
    }

    frameRemains = 1.1 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (five_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      five_3.setAutoDraw(false);
    }
    
    // *five_4* updates
    if (t >= 1.4 && five_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_4.tStart = t;  // (not accounting for frame time here)
      five_4.frameNStart = frameN;  // exact frame index
      
      five_4.setAutoDraw(true);
    }

    frameRemains = 1.4 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (five_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      five_4.setAutoDraw(false);
    }
    
    // *five_5* updates
    if (t >= 1.7 && five_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_5.tStart = t;  // (not accounting for frame time here)
      five_5.frameNStart = frameN;  // exact frame index
      
      five_5.setAutoDraw(true);
    }

    frameRemains = 1.7 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (five_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      five_5.setAutoDraw(false);
    }
    
    // *five_input* updates
    if (t >= 2 && five_input.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_input.tStart = t;  // (not accounting for frame time here)
      five_input.frameNStart = frameN;  // exact frame index
      
      five_input.setAutoDraw(true);
    }

    
    // *five_tip* updates
    if (t >= 2 && five_tip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_tip.tStart = t;  // (not accounting for frame time here)
      five_tip.frameNStart = frameN;  // exact frame index
      
      five_tip.setAutoDraw(true);
    }

    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    if (_pj.in_es6("escape", keys)) {
        core.quit();
    } else {
        if (keys) {
            if ((keys[0] === "space")) {
                textFill += " ";
            } else {
                if ((keys[0] === "backspace")) {
                    textFill = textFill.slice(0, (- 1));
                } else {
                    if (_pj.in_es6(keys[0], allLetters)) {
                        textFill += keys[0];
                    }
                }
            }
            five_input.setText(textFill);
            if ((keys[0] === "return")) {
                textFill.strip();
                psychoJS.experiment.addData("five", textFill);
                if ((textFill === "34613")) {
                    psychoJS.experiment.addData("five_corr", 1);
                } else {
                    psychoJS.experiment.addData("five_corr", 0);
                }
                five_input.setText(textFill);
                continueRoutine = false;
            }
        }
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
    for (const thisComponent of fiveComponents)
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

function fiveRoutineEnd() {
  return async function () {
    //------Ending Routine 'five'-------
    for (const thisComponent of fiveComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "five" was not non-slip safe, so reset the non-slip timer
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
