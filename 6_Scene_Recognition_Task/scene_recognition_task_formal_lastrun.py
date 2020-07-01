#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 六月 15, 2020, at 21:34
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'Scene_Recognition_Task_formal'  # from the Builder filename that created this script
expInfo = {'participant': '', '姓名拼音': '', '男1/女2': '', '入院1/出院2': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\zhang\\Desktop\\张以昊\\课题组\\6_Scene_Cognitive_Task\\scene_recognition_task_formal_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instuction1"
instuction1Clock = core.Clock()
instruction1 = visual.TextStim(win=win, name='instruction1',
    text='欢迎参加测试\n（正式部分）\n\n本测试分三种类型\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instruction5"
instruction5Clock = core.Clock()
instruction_5 = visual.TextStim(win=win, name='instruction_5',
    text='如果准备好了，请开始测试\n\n（继续请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "tip1"
tip1Clock = core.Clock()
tip_1 = visual.TextStim(win=win, name='tip_1',
    text='现在开始，第一种类型测试\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "instuction2"
instuction2Clock = core.Clock()
key_resp_2 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='image\\instrimage\\the_first.png', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "formal1"
formal1Clock = core.Clock()
concentration1_1 = visual.TextStim(win=win, name='concentration1_1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
formal1_1 = visual.ImageStim(
    win=win,
    name='formal1_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.52,0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
formal1_2 = visual.ImageStim(
    win=win,
    name='formal1_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
formal1_3 = visual.ImageStim(
    win=win,
    name='formal1_3', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp_formal1 = keyboard.Keyboard()

# Initialize components for Routine "tip2"
tip2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='第二种类型\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "instruction3"
instruction3Clock = core.Clock()
key_resp_3 = keyboard.Keyboard()
instruction_1 = visual.ImageStim(
    win=win,
    name='instruction_1', 
    image='image\\instrimage\\the_second.png', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "formal2"
formal2Clock = core.Clock()
concentration2_1 = visual.TextStim(win=win, name='concentration2_1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image2_1 = visual.ImageStim(
    win=win,
    name='image2_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image2_2 = visual.ImageStim(
    win=win,
    name='image2_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image2_3 = visual.ImageStim(
    win=win,
    name='image2_3', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp_formal2 = keyboard.Keyboard()

# Initialize components for Routine "tip3"
tip3Clock = core.Clock()
tip_3 = visual.TextStim(win=win, name='tip_3',
    text='第三种类型\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "instruction4"
instruction4Clock = core.Clock()
key_resp_4 = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='image\\instrimage\\the_third.png', mask=None,
    ori=0, pos=(0, 0), size=(1.4,0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "formal3"
formal3Clock = core.Clock()
concentration3_1 = visual.TextStim(win=win, name='concentration3_1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image3_1 = visual.ImageStim(
    win=win,
    name='image3_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image3_2 = visual.ImageStim(
    win=win,
    name='image3_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image3_3 = visual.ImageStim(
    win=win,
    name='image3_3', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp_formal3 = keyboard.Keyboard()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='测试结束，谢谢您的参与',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instuction1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instuction1Components = [instruction1, key_resp]
for thisComponent in instuction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instuction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instuction1"-------
while continueRoutine:
    # get current time
    t = instuction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instuction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction1* updates
    if instruction1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction1.frameNStart = frameN  # exact frame index
        instruction1.tStart = t  # local t and not account for scr refresh
        instruction1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction1, 'tStartRefresh')  # time at next scr refresh
        instruction1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instuction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instuction1"-------
for thisComponent in instuction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction1.started', instruction1.tStartRefresh)
thisExp.addData('instruction1.stopped', instruction1.tStopRefresh)
# the Routine "instuction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
instruction5Components = [instruction_5, key_resp_11]
for thisComponent in instruction5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction5"-------
while continueRoutine:
    # get current time
    t = instruction5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_5* updates
    if instruction_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_5.frameNStart = frameN  # exact frame index
        instruction_5.tStart = t  # local t and not account for scr refresh
        instruction_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_5, 'tStartRefresh')  # time at next scr refresh
        instruction_5.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction5"-------
for thisComponent in instruction5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_5.started', instruction_5.tStartRefresh)
thisExp.addData('instruction_5.stopped', instruction_5.tStopRefresh)
# the Routine "instruction5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "tip1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
tip1Components = [tip_1, key_resp_5]
for thisComponent in tip1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
tip1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "tip1"-------
while continueRoutine:
    # get current time
    t = tip1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=tip1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tip_1* updates
    if tip_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tip_1.frameNStart = frameN  # exact frame index
        tip_1.tStart = t  # local t and not account for scr refresh
        tip_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tip_1, 'tStartRefresh')  # time at next scr refresh
        tip_1.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in tip1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "tip1"-------
for thisComponent in tip1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tip_1.started', tip_1.tStartRefresh)
thisExp.addData('tip_1.stopped', tip_1.tStopRefresh)
# the Routine "tip1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instuction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instuction2Components = [key_resp_2, image]
for thisComponent in instuction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instuction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instuction2"-------
while continueRoutine:
    # get current time
    t = instuction2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instuction2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instuction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instuction2"-------
for thisComponent in instuction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# the Routine "instuction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_condition1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\formal_condition1.xlsx'),
    seed=None, name='loop_condition1')
thisExp.addLoop(loop_condition1)  # add the loop to the experiment
thisLoop_condition1 = loop_condition1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_condition1.rgb)
if thisLoop_condition1 != None:
    for paramName in thisLoop_condition1:
        exec('{} = thisLoop_condition1[paramName]'.format(paramName))

for thisLoop_condition1 in loop_condition1:
    currentLoop = loop_condition1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_condition1.rgb)
    if thisLoop_condition1 != None:
        for paramName in thisLoop_condition1:
            exec('{} = thisLoop_condition1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "formal1"-------
    continueRoutine = True
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    formal1_1.setImage(study1)
    formal1_2.setImage(path1_1)
    formal1_3.setImage(path1_2)
    key_resp_formal1.keys = []
    key_resp_formal1.rt = []
    _key_resp_formal1_allKeys = []
    # keep track of which components have finished
    formal1Components = [concentration1_1, formal1_1, formal1_2, formal1_3, key_resp_formal1]
    for thisComponent in formal1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    formal1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "formal1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = formal1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=formal1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration1_1* updates
        if concentration1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration1_1.frameNStart = frameN  # exact frame index
            concentration1_1.tStart = t  # local t and not account for scr refresh
            concentration1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration1_1, 'tStartRefresh')  # time at next scr refresh
            concentration1_1.setAutoDraw(True)
        if concentration1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration1_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration1_1.tStop = t  # not accounting for scr refresh
                concentration1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration1_1, 'tStopRefresh')  # time at next scr refresh
                concentration1_1.setAutoDraw(False)
        
        # *formal1_1* updates
        if formal1_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            formal1_1.frameNStart = frameN  # exact frame index
            formal1_1.tStart = t  # local t and not account for scr refresh
            formal1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal1_1, 'tStartRefresh')  # time at next scr refresh
            formal1_1.setAutoDraw(True)
        if formal1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal1_1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                formal1_1.tStop = t  # not accounting for scr refresh
                formal1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(formal1_1, 'tStopRefresh')  # time at next scr refresh
                formal1_1.setAutoDraw(False)
        
        # *formal1_2* updates
        if formal1_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            formal1_2.frameNStart = frameN  # exact frame index
            formal1_2.tStart = t  # local t and not account for scr refresh
            formal1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal1_2, 'tStartRefresh')  # time at next scr refresh
            formal1_2.setAutoDraw(True)
        if formal1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal1_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                formal1_2.tStop = t  # not accounting for scr refresh
                formal1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(formal1_2, 'tStopRefresh')  # time at next scr refresh
                formal1_2.setAutoDraw(False)
        
        # *formal1_3* updates
        if formal1_3.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            formal1_3.frameNStart = frameN  # exact frame index
            formal1_3.tStart = t  # local t and not account for scr refresh
            formal1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal1_3, 'tStartRefresh')  # time at next scr refresh
            formal1_3.setAutoDraw(True)
        if formal1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal1_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                formal1_3.tStop = t  # not accounting for scr refresh
                formal1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(formal1_3, 'tStopRefresh')  # time at next scr refresh
                formal1_3.setAutoDraw(False)
        
        # *key_resp_formal1* updates
        waitOnFlip = False
        if key_resp_formal1.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            key_resp_formal1.frameNStart = frameN  # exact frame index
            key_resp_formal1.tStart = t  # local t and not account for scr refresh
            key_resp_formal1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_formal1, 'tStartRefresh')  # time at next scr refresh
            key_resp_formal1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_formal1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_formal1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_formal1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_formal1.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_formal1.tStop = t  # not accounting for scr refresh
                key_resp_formal1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_formal1, 'tStopRefresh')  # time at next scr refresh
                key_resp_formal1.status = FINISHED
        if key_resp_formal1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_formal1.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_formal1_allKeys.extend(theseKeys)
            if len(_key_resp_formal1_allKeys):
                key_resp_formal1.keys = _key_resp_formal1_allKeys[-1].name  # just the last key pressed
                key_resp_formal1.rt = _key_resp_formal1_allKeys[-1].rt
                # was this correct?
                if (key_resp_formal1.keys == str(corresp1)) or (key_resp_formal1.keys == corresp1):
                    key_resp_formal1.corr = 1
                else:
                    key_resp_formal1.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in formal1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "formal1"-------
    for thisComponent in formal1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_condition1.addData('concentration1_1.started', concentration1_1.tStartRefresh)
    loop_condition1.addData('concentration1_1.stopped', concentration1_1.tStopRefresh)
    loop_condition1.addData('formal1_1.started', formal1_1.tStartRefresh)
    loop_condition1.addData('formal1_1.stopped', formal1_1.tStopRefresh)
    loop_condition1.addData('formal1_2.started', formal1_2.tStartRefresh)
    loop_condition1.addData('formal1_2.stopped', formal1_2.tStopRefresh)
    loop_condition1.addData('formal1_3.started', formal1_3.tStartRefresh)
    loop_condition1.addData('formal1_3.stopped', formal1_3.tStopRefresh)
    # check responses
    if key_resp_formal1.keys in ['', [], None]:  # No response was made
        key_resp_formal1.keys = None
        # was no response the correct answer?!
        if str(corresp1).lower() == 'none':
           key_resp_formal1.corr = 1;  # correct non-response
        else:
           key_resp_formal1.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_condition1 (TrialHandler)
    loop_condition1.addData('key_resp_formal1.keys',key_resp_formal1.keys)
    loop_condition1.addData('key_resp_formal1.corr', key_resp_formal1.corr)
    if key_resp_formal1.keys != None:  # we had a response
        loop_condition1.addData('key_resp_formal1.rt', key_resp_formal1.rt)
    loop_condition1.addData('key_resp_formal1.started', key_resp_formal1.tStartRefresh)
    loop_condition1.addData('key_resp_formal1.stopped', key_resp_formal1.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_condition1'


# ------Prepare to start Routine "tip2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
tip2Components = [text, key_resp_7]
for thisComponent in tip2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
tip2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "tip2"-------
while continueRoutine:
    # get current time
    t = tip2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=tip2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in tip2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "tip2"-------
for thisComponent in tip2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "tip2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction3Components = [key_resp_3, instruction_1]
for thisComponent in instruction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction3"-------
while continueRoutine:
    # get current time
    t = instruction3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instruction_1* updates
    if instruction_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_1.frameNStart = frameN  # exact frame index
        instruction_1.tStart = t  # local t and not account for scr refresh
        instruction_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_1, 'tStartRefresh')  # time at next scr refresh
        instruction_1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction3"-------
for thisComponent in instruction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_1.started', instruction_1.tStartRefresh)
thisExp.addData('instruction_1.stopped', instruction_1.tStopRefresh)
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_condition2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\formal_condition2.xlsx'),
    seed=None, name='loop_condition2')
thisExp.addLoop(loop_condition2)  # add the loop to the experiment
thisLoop_condition2 = loop_condition2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_condition2.rgb)
if thisLoop_condition2 != None:
    for paramName in thisLoop_condition2:
        exec('{} = thisLoop_condition2[paramName]'.format(paramName))

for thisLoop_condition2 in loop_condition2:
    currentLoop = loop_condition2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_condition2.rgb)
    if thisLoop_condition2 != None:
        for paramName in thisLoop_condition2:
            exec('{} = thisLoop_condition2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "formal2"-------
    continueRoutine = True
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    image2_1.setImage(study2)
    image2_2.setImage(path2_1)
    image2_3.setImage(path2_2)
    key_resp_formal2.keys = []
    key_resp_formal2.rt = []
    _key_resp_formal2_allKeys = []
    # keep track of which components have finished
    formal2Components = [concentration2_1, image2_1, image2_2, image2_3, key_resp_formal2]
    for thisComponent in formal2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    formal2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "formal2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = formal2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=formal2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration2_1* updates
        if concentration2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration2_1.frameNStart = frameN  # exact frame index
            concentration2_1.tStart = t  # local t and not account for scr refresh
            concentration2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration2_1, 'tStartRefresh')  # time at next scr refresh
            concentration2_1.setAutoDraw(True)
        if concentration2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration2_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration2_1.tStop = t  # not accounting for scr refresh
                concentration2_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration2_1, 'tStopRefresh')  # time at next scr refresh
                concentration2_1.setAutoDraw(False)
        
        # *image2_1* updates
        if image2_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            image2_1.frameNStart = frameN  # exact frame index
            image2_1.tStart = t  # local t and not account for scr refresh
            image2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2_1, 'tStartRefresh')  # time at next scr refresh
            image2_1.setAutoDraw(True)
        if image2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image2_1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                image2_1.tStop = t  # not accounting for scr refresh
                image2_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image2_1, 'tStopRefresh')  # time at next scr refresh
                image2_1.setAutoDraw(False)
        
        # *image2_2* updates
        if image2_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            image2_2.frameNStart = frameN  # exact frame index
            image2_2.tStart = t  # local t and not account for scr refresh
            image2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2_2, 'tStartRefresh')  # time at next scr refresh
            image2_2.setAutoDraw(True)
        if image2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image2_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                image2_2.tStop = t  # not accounting for scr refresh
                image2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image2_2, 'tStopRefresh')  # time at next scr refresh
                image2_2.setAutoDraw(False)
        
        # *image2_3* updates
        if image2_3.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            image2_3.frameNStart = frameN  # exact frame index
            image2_3.tStart = t  # local t and not account for scr refresh
            image2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2_3, 'tStartRefresh')  # time at next scr refresh
            image2_3.setAutoDraw(True)
        if image2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image2_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                image2_3.tStop = t  # not accounting for scr refresh
                image2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image2_3, 'tStopRefresh')  # time at next scr refresh
                image2_3.setAutoDraw(False)
        
        # *key_resp_formal2* updates
        waitOnFlip = False
        if key_resp_formal2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            key_resp_formal2.frameNStart = frameN  # exact frame index
            key_resp_formal2.tStart = t  # local t and not account for scr refresh
            key_resp_formal2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_formal2, 'tStartRefresh')  # time at next scr refresh
            key_resp_formal2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_formal2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_formal2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_formal2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_formal2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_formal2.tStop = t  # not accounting for scr refresh
                key_resp_formal2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_formal2, 'tStopRefresh')  # time at next scr refresh
                key_resp_formal2.status = FINISHED
        if key_resp_formal2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_formal2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_formal2_allKeys.extend(theseKeys)
            if len(_key_resp_formal2_allKeys):
                key_resp_formal2.keys = _key_resp_formal2_allKeys[-1].name  # just the last key pressed
                key_resp_formal2.rt = _key_resp_formal2_allKeys[-1].rt
                # was this correct?
                if (key_resp_formal2.keys == str(corresp2)) or (key_resp_formal2.keys == corresp2):
                    key_resp_formal2.corr = 1
                else:
                    key_resp_formal2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in formal2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "formal2"-------
    for thisComponent in formal2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_condition2.addData('concentration2_1.started', concentration2_1.tStartRefresh)
    loop_condition2.addData('concentration2_1.stopped', concentration2_1.tStopRefresh)
    loop_condition2.addData('image2_1.started', image2_1.tStartRefresh)
    loop_condition2.addData('image2_1.stopped', image2_1.tStopRefresh)
    loop_condition2.addData('image2_2.started', image2_2.tStartRefresh)
    loop_condition2.addData('image2_2.stopped', image2_2.tStopRefresh)
    loop_condition2.addData('image2_3.started', image2_3.tStartRefresh)
    loop_condition2.addData('image2_3.stopped', image2_3.tStopRefresh)
    # check responses
    if key_resp_formal2.keys in ['', [], None]:  # No response was made
        key_resp_formal2.keys = None
        # was no response the correct answer?!
        if str(corresp2).lower() == 'none':
           key_resp_formal2.corr = 1;  # correct non-response
        else:
           key_resp_formal2.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_condition2 (TrialHandler)
    loop_condition2.addData('key_resp_formal2.keys',key_resp_formal2.keys)
    loop_condition2.addData('key_resp_formal2.corr', key_resp_formal2.corr)
    if key_resp_formal2.keys != None:  # we had a response
        loop_condition2.addData('key_resp_formal2.rt', key_resp_formal2.rt)
    loop_condition2.addData('key_resp_formal2.started', key_resp_formal2.tStartRefresh)
    loop_condition2.addData('key_resp_formal2.stopped', key_resp_formal2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_condition2'


# ------Prepare to start Routine "tip3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
tip3Components = [tip_3, key_resp_9]
for thisComponent in tip3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
tip3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "tip3"-------
while continueRoutine:
    # get current time
    t = tip3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=tip3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tip_3* updates
    if tip_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tip_3.frameNStart = frameN  # exact frame index
        tip_3.tStart = t  # local t and not account for scr refresh
        tip_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tip_3, 'tStartRefresh')  # time at next scr refresh
        tip_3.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in tip3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "tip3"-------
for thisComponent in tip3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tip_3.started', tip_3.tStartRefresh)
thisExp.addData('tip_3.stopped', tip_3.tStopRefresh)
# the Routine "tip3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instruction4Components = [key_resp_4, image_2]
for thisComponent in instruction4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction4"-------
while continueRoutine:
    # get current time
    t = instruction4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction4"-------
for thisComponent in instruction4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
# the Routine "instruction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_condition3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\formal_condition3.xlsx'),
    seed=None, name='loop_condition3')
thisExp.addLoop(loop_condition3)  # add the loop to the experiment
thisLoop_condition3 = loop_condition3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_condition3.rgb)
if thisLoop_condition3 != None:
    for paramName in thisLoop_condition3:
        exec('{} = thisLoop_condition3[paramName]'.format(paramName))

for thisLoop_condition3 in loop_condition3:
    currentLoop = loop_condition3
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_condition3.rgb)
    if thisLoop_condition3 != None:
        for paramName in thisLoop_condition3:
            exec('{} = thisLoop_condition3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "formal3"-------
    continueRoutine = True
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    image3_1.setImage(study3)
    image3_2.setImage(path3_1)
    image3_3.setImage(path3_2)
    key_resp_formal3.keys = []
    key_resp_formal3.rt = []
    _key_resp_formal3_allKeys = []
    # keep track of which components have finished
    formal3Components = [concentration3_1, image3_1, image3_2, image3_3, key_resp_formal3]
    for thisComponent in formal3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    formal3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "formal3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = formal3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=formal3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration3_1* updates
        if concentration3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration3_1.frameNStart = frameN  # exact frame index
            concentration3_1.tStart = t  # local t and not account for scr refresh
            concentration3_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration3_1, 'tStartRefresh')  # time at next scr refresh
            concentration3_1.setAutoDraw(True)
        if concentration3_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration3_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration3_1.tStop = t  # not accounting for scr refresh
                concentration3_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration3_1, 'tStopRefresh')  # time at next scr refresh
                concentration3_1.setAutoDraw(False)
        
        # *image3_1* updates
        if image3_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            image3_1.frameNStart = frameN  # exact frame index
            image3_1.tStart = t  # local t and not account for scr refresh
            image3_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3_1, 'tStartRefresh')  # time at next scr refresh
            image3_1.setAutoDraw(True)
        if image3_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image3_1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                image3_1.tStop = t  # not accounting for scr refresh
                image3_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image3_1, 'tStopRefresh')  # time at next scr refresh
                image3_1.setAutoDraw(False)
        
        # *image3_2* updates
        if image3_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            image3_2.frameNStart = frameN  # exact frame index
            image3_2.tStart = t  # local t and not account for scr refresh
            image3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3_2, 'tStartRefresh')  # time at next scr refresh
            image3_2.setAutoDraw(True)
        if image3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image3_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                image3_2.tStop = t  # not accounting for scr refresh
                image3_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image3_2, 'tStopRefresh')  # time at next scr refresh
                image3_2.setAutoDraw(False)
        
        # *image3_3* updates
        if image3_3.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            image3_3.frameNStart = frameN  # exact frame index
            image3_3.tStart = t  # local t and not account for scr refresh
            image3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3_3, 'tStartRefresh')  # time at next scr refresh
            image3_3.setAutoDraw(True)
        if image3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image3_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                image3_3.tStop = t  # not accounting for scr refresh
                image3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image3_3, 'tStopRefresh')  # time at next scr refresh
                image3_3.setAutoDraw(False)
        
        # *key_resp_formal3* updates
        waitOnFlip = False
        if key_resp_formal3.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            key_resp_formal3.frameNStart = frameN  # exact frame index
            key_resp_formal3.tStart = t  # local t and not account for scr refresh
            key_resp_formal3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_formal3, 'tStartRefresh')  # time at next scr refresh
            key_resp_formal3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_formal3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_formal3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_formal3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_formal3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_formal3.tStop = t  # not accounting for scr refresh
                key_resp_formal3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_formal3, 'tStopRefresh')  # time at next scr refresh
                key_resp_formal3.status = FINISHED
        if key_resp_formal3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_formal3.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_formal3_allKeys.extend(theseKeys)
            if len(_key_resp_formal3_allKeys):
                key_resp_formal3.keys = _key_resp_formal3_allKeys[-1].name  # just the last key pressed
                key_resp_formal3.rt = _key_resp_formal3_allKeys[-1].rt
                # was this correct?
                if (key_resp_formal3.keys == str(corresp3)) or (key_resp_formal3.keys == corresp3):
                    key_resp_formal3.corr = 1
                else:
                    key_resp_formal3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in formal3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "formal3"-------
    for thisComponent in formal3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_condition3.addData('concentration3_1.started', concentration3_1.tStartRefresh)
    loop_condition3.addData('concentration3_1.stopped', concentration3_1.tStopRefresh)
    loop_condition3.addData('image3_1.started', image3_1.tStartRefresh)
    loop_condition3.addData('image3_1.stopped', image3_1.tStopRefresh)
    loop_condition3.addData('image3_2.started', image3_2.tStartRefresh)
    loop_condition3.addData('image3_2.stopped', image3_2.tStopRefresh)
    loop_condition3.addData('image3_3.started', image3_3.tStartRefresh)
    loop_condition3.addData('image3_3.stopped', image3_3.tStopRefresh)
    # check responses
    if key_resp_formal3.keys in ['', [], None]:  # No response was made
        key_resp_formal3.keys = None
        # was no response the correct answer?!
        if str(corresp3).lower() == 'none':
           key_resp_formal3.corr = 1;  # correct non-response
        else:
           key_resp_formal3.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_condition3 (TrialHandler)
    loop_condition3.addData('key_resp_formal3.keys',key_resp_formal3.keys)
    loop_condition3.addData('key_resp_formal3.corr', key_resp_formal3.corr)
    if key_resp_formal3.keys != None:  # we had a response
        loop_condition3.addData('key_resp_formal3.rt', key_resp_formal3.rt)
    loop_condition3.addData('key_resp_formal3.started', key_resp_formal3.tStartRefresh)
    loop_condition3.addData('key_resp_formal3.stopped', key_resp_formal3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_condition3'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text_2]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
