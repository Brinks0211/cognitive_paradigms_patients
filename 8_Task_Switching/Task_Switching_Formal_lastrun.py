#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 六月 14, 2020, at 15:42
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
expName = 'Task_Switching_Formal'  # from the Builder filename that created this script
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
    originPath='D:\\jianguoyun\\课题组\\8_Task_Switching\\Task_Switching_Formal_lastrun.py',
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

# Initialize components for Routine "instruction1"
instruction1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='欢迎参加测试\n（正式测试）\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instruction2"
instruction2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='首先屏幕会出现一个注视点"+"\n之后会出现一个正方形图片\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "instruction3"
instruction3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='如果中心红色箭头为水平方向，\n则判断红色圆圈位于正方块的左侧还是右侧。\n\n如果为左侧，请按键盘左键\n如果为右侧，请按键盘右键\n\n（继续，请按空格键）\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "instruction3_2"
instruction3_2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='如果中心红色箭头为垂直方向，\n则判断红色圆圈位于正方块的上方还是下方。\n\n如果为上方，请按键盘上键\n如果为下方，请按键盘下键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "instruction4"
instruction4Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='下面进入正式测试\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "formal1"
formal1Clock = core.Clock()
concentration = visual.TextStim(win=win, name='concentration',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.53, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_formal = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='现在是休息阶段\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "formal1"
formal1Clock = core.Clock()
concentration = visual.TextStim(win=win, name='concentration',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.53, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_formal = keyboard.Keyboard()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='测试结束，感谢您的参与',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instruction1Components = [text, key_resp]
for thisComponent in instruction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction1"-------
while continueRoutine:
    # get current time
    t = instruction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction1Clock)
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
    for thisComponent in instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction1"-------
for thisComponent in instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instruction2Components = [text_2, key_resp_2]
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
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
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
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction3Components = [text_3, key_resp_3]
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
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
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
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction3_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
instruction3_2Components = [text_6, key_resp_6]
for thisComponent in instruction3_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction3_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction3_2"-------
while continueRoutine:
    # get current time
    t = instruction3_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction3_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
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
    for thisComponent in instruction3_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction3_2"-------
for thisComponent in instruction3_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "instruction3_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instruction4Components = [text_4, key_resp_4]
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
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
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
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "instruction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_formal = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\formal.xlsx'),
    seed=None, name='loop_formal')
thisExp.addLoop(loop_formal)  # add the loop to the experiment
thisLoop_formal = loop_formal.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_formal.rgb)
if thisLoop_formal != None:
    for paramName in thisLoop_formal:
        exec('{} = thisLoop_formal[paramName]'.format(paramName))

for thisLoop_formal in loop_formal:
    currentLoop = loop_formal
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_formal.rgb)
    if thisLoop_formal != None:
        for paramName in thisLoop_formal:
            exec('{} = thisLoop_formal[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "formal1"-------
    continueRoutine = True
    routineTimer.add(5.300000)
    # update component parameters for each repeat
    image.setImage(path)
    key_resp_formal.keys = []
    key_resp_formal.rt = []
    _key_resp_formal_allKeys = []
    # keep track of which components have finished
    formal1Components = [concentration, image, key_resp_formal]
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
        
        # *concentration* updates
        if concentration.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            concentration.frameNStart = frameN  # exact frame index
            concentration.tStart = t  # local t and not account for scr refresh
            concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration, 'tStartRefresh')  # time at next scr refresh
            concentration.setAutoDraw(True)
        if concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration.tStop = t  # not accounting for scr refresh
                concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration, 'tStopRefresh')  # time at next scr refresh
                concentration.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp_formal* updates
        waitOnFlip = False
        if key_resp_formal.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            key_resp_formal.frameNStart = frameN  # exact frame index
            key_resp_formal.tStart = t  # local t and not account for scr refresh
            key_resp_formal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_formal, 'tStartRefresh')  # time at next scr refresh
            key_resp_formal.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_formal.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_formal.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_formal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_formal.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_formal.tStop = t  # not accounting for scr refresh
                key_resp_formal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_formal, 'tStopRefresh')  # time at next scr refresh
                key_resp_formal.status = FINISHED
        if key_resp_formal.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_formal.getKeys(keyList=['left', 'right', 'up', 'down'], waitRelease=False)
            _key_resp_formal_allKeys.extend(theseKeys)
            if len(_key_resp_formal_allKeys):
                key_resp_formal.keys = _key_resp_formal_allKeys[-1].name  # just the last key pressed
                key_resp_formal.rt = _key_resp_formal_allKeys[-1].rt
                # was this correct?
                if (key_resp_formal.keys == str(corresp)) or (key_resp_formal.keys == corresp):
                    key_resp_formal.corr = 1
                else:
                    key_resp_formal.corr = 0
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
    loop_formal.addData('concentration.started', concentration.tStartRefresh)
    loop_formal.addData('concentration.stopped', concentration.tStopRefresh)
    loop_formal.addData('image.started', image.tStartRefresh)
    loop_formal.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_formal.keys in ['', [], None]:  # No response was made
        key_resp_formal.keys = None
        # was no response the correct answer?!
        if str(corresp).lower() == 'none':
           key_resp_formal.corr = 1;  # correct non-response
        else:
           key_resp_formal.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_formal (TrialHandler)
    loop_formal.addData('key_resp_formal.keys',key_resp_formal.keys)
    loop_formal.addData('key_resp_formal.corr', key_resp_formal.corr)
    if key_resp_formal.keys != None:  # we had a response
        loop_formal.addData('key_resp_formal.rt', key_resp_formal.rt)
    loop_formal.addData('key_resp_formal.started', key_resp_formal.tStartRefresh)
    loop_formal.addData('key_resp_formal.stopped', key_resp_formal.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_formal'


# ------Prepare to start Routine "rest"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
restComponents = [text_7, key_resp_7]
for thisComponent in restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rest"-------
while continueRoutine:
    # get current time
    t = restClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=restClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
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
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# the Routine "rest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_formal2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\formal.xlsx'),
    seed=None, name='loop_formal2')
thisExp.addLoop(loop_formal2)  # add the loop to the experiment
thisLoop_formal2 = loop_formal2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_formal2.rgb)
if thisLoop_formal2 != None:
    for paramName in thisLoop_formal2:
        exec('{} = thisLoop_formal2[paramName]'.format(paramName))

for thisLoop_formal2 in loop_formal2:
    currentLoop = loop_formal2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_formal2.rgb)
    if thisLoop_formal2 != None:
        for paramName in thisLoop_formal2:
            exec('{} = thisLoop_formal2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "formal1"-------
    continueRoutine = True
    routineTimer.add(5.300000)
    # update component parameters for each repeat
    image.setImage(path)
    key_resp_formal.keys = []
    key_resp_formal.rt = []
    _key_resp_formal_allKeys = []
    # keep track of which components have finished
    formal1Components = [concentration, image, key_resp_formal]
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
        
        # *concentration* updates
        if concentration.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            concentration.frameNStart = frameN  # exact frame index
            concentration.tStart = t  # local t and not account for scr refresh
            concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration, 'tStartRefresh')  # time at next scr refresh
            concentration.setAutoDraw(True)
        if concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration.tStop = t  # not accounting for scr refresh
                concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration, 'tStopRefresh')  # time at next scr refresh
                concentration.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp_formal* updates
        waitOnFlip = False
        if key_resp_formal.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            key_resp_formal.frameNStart = frameN  # exact frame index
            key_resp_formal.tStart = t  # local t and not account for scr refresh
            key_resp_formal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_formal, 'tStartRefresh')  # time at next scr refresh
            key_resp_formal.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_formal.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_formal.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_formal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_formal.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_formal.tStop = t  # not accounting for scr refresh
                key_resp_formal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_formal, 'tStopRefresh')  # time at next scr refresh
                key_resp_formal.status = FINISHED
        if key_resp_formal.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_formal.getKeys(keyList=['left', 'right', 'up', 'down'], waitRelease=False)
            _key_resp_formal_allKeys.extend(theseKeys)
            if len(_key_resp_formal_allKeys):
                key_resp_formal.keys = _key_resp_formal_allKeys[-1].name  # just the last key pressed
                key_resp_formal.rt = _key_resp_formal_allKeys[-1].rt
                # was this correct?
                if (key_resp_formal.keys == str(corresp)) or (key_resp_formal.keys == corresp):
                    key_resp_formal.corr = 1
                else:
                    key_resp_formal.corr = 0
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
    loop_formal2.addData('concentration.started', concentration.tStartRefresh)
    loop_formal2.addData('concentration.stopped', concentration.tStopRefresh)
    loop_formal2.addData('image.started', image.tStartRefresh)
    loop_formal2.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_formal.keys in ['', [], None]:  # No response was made
        key_resp_formal.keys = None
        # was no response the correct answer?!
        if str(corresp).lower() == 'none':
           key_resp_formal.corr = 1;  # correct non-response
        else:
           key_resp_formal.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_formal2 (TrialHandler)
    loop_formal2.addData('key_resp_formal.keys',key_resp_formal.keys)
    loop_formal2.addData('key_resp_formal.corr', key_resp_formal.corr)
    if key_resp_formal.keys != None:  # we had a response
        loop_formal2.addData('key_resp_formal.rt', key_resp_formal.rt)
    loop_formal2.addData('key_resp_formal.started', key_resp_formal.tStartRefresh)
    loop_formal2.addData('key_resp_formal.stopped', key_resp_formal.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_formal2'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text_5]
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
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    
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
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)

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
