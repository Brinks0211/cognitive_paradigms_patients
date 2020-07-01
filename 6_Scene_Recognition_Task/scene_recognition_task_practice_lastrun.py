#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 六月 15, 2020, at 21:32
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
expName = 'Scene_Recognition_Task_Practice'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zhang\\Desktop\\张以昊\\课题组\\6_Scene_Cognitive_Task\\scene_recognition_task_practice_lastrun.py',
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
    size=[1536, 864], fullscr=False, screen=0, 
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

# Initialize components for Routine "introduction1"
introduction1Clock = core.Clock()
instruction_1 = visual.TextStim(win=win, name='instruction_1',
    text='欢迎参加测试\n（练习部分）\n\n本测试分三种类型\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instruction5"
instruction5Clock = core.Clock()
instruction_5 = visual.TextStim(win=win, name='instruction_5',
    text='如果准备好了，请开始练习\n\n（继续请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "tip1"
tip1Clock = core.Clock()
tip_1 = visual.TextStim(win=win, name='tip_1',
    text='现在开始，第一种类型练习\n\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "instruction2"
instruction2Clock = core.Clock()
key_resp_2 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='image\\instrimage\\the_first.png', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "practice1"
practice1Clock = core.Clock()
concentration1_1 = visual.TextStim(win=win, name='concentration1_1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image1_1 = visual.ImageStim(
    win=win,
    name='image1_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image1_2 = visual.ImageStim(
    win=win,
    name='image1_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image1_3 = visual.ImageStim(
    win=win,
    name='image1_3', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.52, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp_7 = keyboard.Keyboard()
message1=""

# Initialize components for Routine "feedback1"
feedback1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "tip2"
tip2Clock = core.Clock()
tip_2 = visual.TextStim(win=win, name='tip_2',
    text='现在，开始第二种类型练习\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "instruction3"
instruction3Clock = core.Clock()
key_resp_3 = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='image\\instrimage\\the_second.png', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "practice2"
practice2Clock = core.Clock()
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
key_resp_9 = keyboard.Keyboard()
message2=""

# Initialize components for Routine "feedback2"
feedback2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "tip3"
tip3Clock = core.Clock()
tip_3 = visual.TextStim(win=win, name='tip_3',
    text='现在，开始第三种类型练习\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "instruction4"
instruction4Clock = core.Clock()
key_resp_4 = keyboard.Keyboard()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='image\\instrimage\\the_third.png', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "practice3"
practice3Clock = core.Clock()
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
key_resp_11 = keyboard.Keyboard()
message3=""

# Initialize components for Routine "feedback3"
feedback3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='练习结束，请开始正式测试',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introduction1Components = [instruction_1, key_resp]
for thisComponent in introduction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction1"-------
while continueRoutine:
    # get current time
    t = introduction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_1* updates
    if instruction_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_1.frameNStart = frameN  # exact frame index
        instruction_1.tStart = t  # local t and not account for scr refresh
        instruction_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_1, 'tStartRefresh')  # time at next scr refresh
        instruction_1.setAutoDraw(True)
    
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
    for thisComponent in introduction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction1"-------
for thisComponent in introduction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_1.started', instruction_1.tStartRefresh)
thisExp.addData('instruction_1.stopped', instruction_1.tStopRefresh)
# the Routine "introduction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
instruction5Components = [instruction_5, key_resp_5]
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
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
tip1Components = [tip_1, key_resp_6]
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
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
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
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "tip1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instruction2Components = [key_resp_2, image]
for thisComponent in instruction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction2"-------
while continueRoutine:
    # get current time
    t = instruction2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction2Clock)
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
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction2"-------
for thisComponent in instruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_practice1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\practice_condition1.xlsx'),
    seed=None, name='loop_practice1')
thisExp.addLoop(loop_practice1)  # add the loop to the experiment
thisLoop_practice1 = loop_practice1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_practice1.rgb)
if thisLoop_practice1 != None:
    for paramName in thisLoop_practice1:
        exec('{} = thisLoop_practice1[paramName]'.format(paramName))

for thisLoop_practice1 in loop_practice1:
    currentLoop = loop_practice1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_practice1.rgb)
    if thisLoop_practice1 != None:
        for paramName in thisLoop_practice1:
            exec('{} = thisLoop_practice1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice1"-------
    continueRoutine = True
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    image1_1.setImage(study1)
    image1_2.setImage(path1_1)
    image1_3.setImage(path1_2)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    practice1Components = [concentration1_1, image1_1, image1_2, image1_3, key_resp_7]
    for thisComponent in practice1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice1Clock)
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
        
        # *image1_1* updates
        if image1_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            image1_1.frameNStart = frameN  # exact frame index
            image1_1.tStart = t  # local t and not account for scr refresh
            image1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1_1, 'tStartRefresh')  # time at next scr refresh
            image1_1.setAutoDraw(True)
        if image1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image1_1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                image1_1.tStop = t  # not accounting for scr refresh
                image1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image1_1, 'tStopRefresh')  # time at next scr refresh
                image1_1.setAutoDraw(False)
        
        # *image1_2* updates
        if image1_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            image1_2.frameNStart = frameN  # exact frame index
            image1_2.tStart = t  # local t and not account for scr refresh
            image1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1_2, 'tStartRefresh')  # time at next scr refresh
            image1_2.setAutoDraw(True)
        if image1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image1_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                image1_2.tStop = t  # not accounting for scr refresh
                image1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image1_2, 'tStopRefresh')  # time at next scr refresh
                image1_2.setAutoDraw(False)
        
        # *image1_3* updates
        if image1_3.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            image1_3.frameNStart = frameN  # exact frame index
            image1_3.tStart = t  # local t and not account for scr refresh
            image1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1_3, 'tStartRefresh')  # time at next scr refresh
            image1_3.setAutoDraw(True)
        if image1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image1_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                image1_3.tStop = t  # not accounting for scr refresh
                image1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image1_3, 'tStopRefresh')  # time at next scr refresh
                image1_3.setAutoDraw(False)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
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
        if key_resp_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_7.tStop = t  # not accounting for scr refresh
                key_resp_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_7, 'tStopRefresh')  # time at next scr refresh
                key_resp_7.status = FINISHED
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # was this correct?
                if (key_resp_7.keys == str(corresp1)) or (key_resp_7.keys == corresp1):
                    key_resp_7.corr = 1
                else:
                    key_resp_7.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice1"-------
    for thisComponent in practice1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_practice1.addData('concentration1_1.started', concentration1_1.tStartRefresh)
    loop_practice1.addData('concentration1_1.stopped', concentration1_1.tStopRefresh)
    loop_practice1.addData('image1_1.started', image1_1.tStartRefresh)
    loop_practice1.addData('image1_1.stopped', image1_1.tStopRefresh)
    loop_practice1.addData('image1_2.started', image1_2.tStartRefresh)
    loop_practice1.addData('image1_2.stopped', image1_2.tStopRefresh)
    loop_practice1.addData('image1_3.started', image1_3.tStartRefresh)
    loop_practice1.addData('image1_3.stopped', image1_3.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
        # was no response the correct answer?!
        if str(corresp1).lower() == 'none':
           key_resp_7.corr = 1;  # correct non-response
        else:
           key_resp_7.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_practice1 (TrialHandler)
    loop_practice1.addData('key_resp_7.keys',key_resp_7.keys)
    loop_practice1.addData('key_resp_7.corr', key_resp_7.corr)
    if key_resp_7.keys != None:  # we had a response
        loop_practice1.addData('key_resp_7.rt', key_resp_7.rt)
    loop_practice1.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    loop_practice1.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    if key_resp_7.corr:
        message1="回答正确"
    else:
        message1="回答错误"
    if not key_resp_7.keys:
        message1="请在十秒内按键"
    
    # ------Prepare to start Routine "feedback1"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text.setText(message1)
    # keep track of which components have finished
    feedback1Components = [text]
    for thisComponent in feedback1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback1Clock)
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
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback1"-------
    for thisComponent in feedback1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_practice1.addData('text.started', text.tStartRefresh)
    loop_practice1.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_practice1'


# ------Prepare to start Routine "tip2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
tip2Components = [tip_2, key_resp_8]
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
    
    # *tip_2* updates
    if tip_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tip_2.frameNStart = frameN  # exact frame index
        tip_2.tStart = t  # local t and not account for scr refresh
        tip_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tip_2, 'tStartRefresh')  # time at next scr refresh
        tip_2.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
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
thisExp.addData('tip_2.started', tip_2.tStartRefresh)
thisExp.addData('tip_2.stopped', tip_2.tStopRefresh)
# the Routine "tip2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction3Components = [key_resp_3, image_2]
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
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_practice2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\practice_condition2.xlsx'),
    seed=None, name='loop_practice2')
thisExp.addLoop(loop_practice2)  # add the loop to the experiment
thisLoop_practice2 = loop_practice2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_practice2.rgb)
if thisLoop_practice2 != None:
    for paramName in thisLoop_practice2:
        exec('{} = thisLoop_practice2[paramName]'.format(paramName))

for thisLoop_practice2 in loop_practice2:
    currentLoop = loop_practice2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_practice2.rgb)
    if thisLoop_practice2 != None:
        for paramName in thisLoop_practice2:
            exec('{} = thisLoop_practice2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice2"-------
    continueRoutine = True
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    image2_1.setImage(study2)
    image2_2.setImage(path2_1)
    image2_3.setImage(path2_2)
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    practice2Components = [concentration2_1, image2_1, image2_2, image2_3, key_resp_9]
    for thisComponent in practice2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice2Clock)
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
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
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
        if key_resp_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_9.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_9.tStop = t  # not accounting for scr refresh
                key_resp_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_9, 'tStopRefresh')  # time at next scr refresh
                key_resp_9.status = FINISHED
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                # was this correct?
                if (key_resp_9.keys == str(corresp2)) or (key_resp_9.keys == corresp2):
                    key_resp_9.corr = 1
                else:
                    key_resp_9.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice2"-------
    for thisComponent in practice2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_practice2.addData('concentration2_1.started', concentration2_1.tStartRefresh)
    loop_practice2.addData('concentration2_1.stopped', concentration2_1.tStopRefresh)
    loop_practice2.addData('image2_1.started', image2_1.tStartRefresh)
    loop_practice2.addData('image2_1.stopped', image2_1.tStopRefresh)
    loop_practice2.addData('image2_2.started', image2_2.tStartRefresh)
    loop_practice2.addData('image2_2.stopped', image2_2.tStopRefresh)
    loop_practice2.addData('image2_3.started', image2_3.tStartRefresh)
    loop_practice2.addData('image2_3.stopped', image2_3.tStopRefresh)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
        # was no response the correct answer?!
        if str(corresp2).lower() == 'none':
           key_resp_9.corr = 1;  # correct non-response
        else:
           key_resp_9.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_practice2 (TrialHandler)
    loop_practice2.addData('key_resp_9.keys',key_resp_9.keys)
    loop_practice2.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        loop_practice2.addData('key_resp_9.rt', key_resp_9.rt)
    loop_practice2.addData('key_resp_9.started', key_resp_9.tStartRefresh)
    loop_practice2.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
    if key_resp_9.corr:
        message2="回答正确"
    else:
        message2="回答错误"
    if not key_resp_9.keys:
        message2="请在十秒内按键"
    
    # ------Prepare to start Routine "feedback2"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_2.setText(message2)
    # keep track of which components have finished
    feedback2Components = [text_2]
    for thisComponent in feedback2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback2Clock)
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
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
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
        for thisComponent in feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback2"-------
    for thisComponent in feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_practice2.addData('text_2.started', text_2.tStartRefresh)
    loop_practice2.addData('text_2.stopped', text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_practice2'


# ------Prepare to start Routine "tip3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
tip3Components = [tip_3, key_resp_10]
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
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
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
instruction4Components = [key_resp_4, image_3]
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
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
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
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)
# the Routine "instruction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_practice3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\practice_condition3.xlsx'),
    seed=None, name='loop_practice3')
thisExp.addLoop(loop_practice3)  # add the loop to the experiment
thisLoop_practice3 = loop_practice3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_practice3.rgb)
if thisLoop_practice3 != None:
    for paramName in thisLoop_practice3:
        exec('{} = thisLoop_practice3[paramName]'.format(paramName))

for thisLoop_practice3 in loop_practice3:
    currentLoop = loop_practice3
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_practice3.rgb)
    if thisLoop_practice3 != None:
        for paramName in thisLoop_practice3:
            exec('{} = thisLoop_practice3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice3"-------
    continueRoutine = True
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    image3_1.setImage(study3)
    image3_2.setImage(path3_1)
    image3_3.setImage(path3_2)
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # keep track of which components have finished
    practice3Components = [concentration3_1, image3_1, image3_2, image3_3, key_resp_11]
    for thisComponent in practice3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice3Clock)
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
        
        # *key_resp_11* updates
        waitOnFlip = False
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
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
        if key_resp_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_11.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_11.tStop = t  # not accounting for scr refresh
                key_resp_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_11, 'tStopRefresh')  # time at next scr refresh
                key_resp_11.status = FINISHED
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                # was this correct?
                if (key_resp_11.keys == str(corresp3)) or (key_resp_11.keys == corresp3):
                    key_resp_11.corr = 1
                else:
                    key_resp_11.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice3"-------
    for thisComponent in practice3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_practice3.addData('concentration3_1.started', concentration3_1.tStartRefresh)
    loop_practice3.addData('concentration3_1.stopped', concentration3_1.tStopRefresh)
    loop_practice3.addData('image3_1.started', image3_1.tStartRefresh)
    loop_practice3.addData('image3_1.stopped', image3_1.tStopRefresh)
    loop_practice3.addData('image3_2.started', image3_2.tStartRefresh)
    loop_practice3.addData('image3_2.stopped', image3_2.tStopRefresh)
    loop_practice3.addData('image3_3.started', image3_3.tStartRefresh)
    loop_practice3.addData('image3_3.stopped', image3_3.tStopRefresh)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
        # was no response the correct answer?!
        if str(corresp3).lower() == 'none':
           key_resp_11.corr = 1;  # correct non-response
        else:
           key_resp_11.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_practice3 (TrialHandler)
    loop_practice3.addData('key_resp_11.keys',key_resp_11.keys)
    loop_practice3.addData('key_resp_11.corr', key_resp_11.corr)
    if key_resp_11.keys != None:  # we had a response
        loop_practice3.addData('key_resp_11.rt', key_resp_11.rt)
    loop_practice3.addData('key_resp_11.started', key_resp_11.tStartRefresh)
    loop_practice3.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
    if key_resp_11.corr:
        message3="回答正确"
    else:
        message3="回答错误"
    if not key_resp_11.keys:
        message3="请在十秒内按键"
    
    # ------Prepare to start Routine "feedback3"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_3.setText(message3)
    # keep track of which components have finished
    feedback3Components = [text_3]
    for thisComponent in feedback3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback3"-------
    for thisComponent in feedback3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_practice3.addData('text_3.started', text_3.tStartRefresh)
    loop_practice3.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_practice3'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text_4]
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
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
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
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

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
