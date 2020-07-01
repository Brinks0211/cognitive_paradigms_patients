#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 六月 14, 2020, at 15:38
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
expName = 'Task_Switching_Practice'  # from the Builder filename that created this script
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
    originPath='D:\\jianguoyun\\课题组\\8_Task_Switching\\Task_Switching_Practice_lastrun.py',
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
text1 = visual.TextStim(win=win, name='text1',
    text='欢迎参加测试\n（练习部分）\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instruction2"
instruction2Clock = core.Clock()
text2 = visual.TextStim(win=win, name='text2',
    text='首先屏幕会出现一个注视点"+"\n之后会出现一个正方形图片\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "instruction3"
instruction3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='如果中心红色箭头为水平方向，\n则判断红色圆圈位于正方块的左侧还是右侧。\n\n如果为左侧，请按键盘左键\n如果为右侧，请按键盘右键\n\n（继续，请按空格键）\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "instruction3_2"
instruction3_2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='如果中心红色箭头为垂直方向，\n则判断红色圆圈位于正方块的上方还是下方。\n\n如果为上方，请按键盘上键\n如果为下方，请按键盘下键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "instruction4"
instruction4Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='如果准备好了，请进入练习部分\n\n（继续，请按空格键）',
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
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "practice_hor"
practice_horClock = core.Clock()
text = visual.TextStim(win=win, name='text',
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
key_resp_practice = keyboard.Keyboard()
time=0
message=""

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "rest1"
rest1Clock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='现在是休息阶段\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "instruction3_2"
instruction3_2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='如果中心红色箭头为垂直方向，\n则判断红色圆圈位于正方块的上方还是下方。\n\n如果为上方，请按键盘上键\n如果为下方，请按键盘下键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "practice_ver"
practice_verClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.53, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_practice2 = keyboard.Keyboard()
message2=""

# Initialize components for Routine "feedback2"
feedback2Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "rest1"
rest1Clock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='现在是休息阶段\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "instruction5"
instruction5Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='如果中心红色箭头为水平方向，\n则判断红色圆圈位于正方块的左侧还是右侧。\n\n如果为左侧，请按键盘左键\n如果为右侧，请按键盘右键\n\n如果中心红色箭头为垂直方向，\n则判断红色圆圈位于正方块的上方还是下方。\n\n如果为上方，请按键盘上键\n如果为下方，请按键盘下键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "practice_mix"
practice_mixClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.53, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_practice3 = keyboard.Keyboard()
message3=""

# Initialize components for Routine "feedback3"
feedback3Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='练习结束，请开始正式测试',
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
instruction1Components = [text1, key_resp]
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
    
    # *text1* updates
    if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text1.frameNStart = frameN  # exact frame index
        text1.tStart = t  # local t and not account for scr refresh
        text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
        text1.setAutoDraw(True)
    
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
thisExp.addData('text1.started', text1.tStartRefresh)
thisExp.addData('text1.stopped', text1.tStopRefresh)
# the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction2Components = [text2, key_resp_3]
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
    
    # *text2* updates
    if text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text2.frameNStart = frameN  # exact frame index
        text2.tStart = t  # local t and not account for scr refresh
        text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text2, 'tStartRefresh')  # time at next scr refresh
        text2.setAutoDraw(True)
    
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
thisExp.addData('text2.started', text2.tStartRefresh)
thisExp.addData('text2.stopped', text2.tStopRefresh)
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instruction3Components = [text_3, key_resp_4]
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
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
instruction3_2Components = [text_6, key_resp_5]
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
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instruction4Components = [text_4, key_resp_2]
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

# ------Prepare to start Routine "instruction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instruction3Components = [text_3, key_resp_4]
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

# set up handler to look after randomisation of conditions etc
loop1 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\practice1.xlsx'),
    seed=None, name='loop1')
thisExp.addLoop(loop1)  # add the loop to the experiment
thisLoop1 = loop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
if thisLoop1 != None:
    for paramName in thisLoop1:
        exec('{} = thisLoop1[paramName]'.format(paramName))

for thisLoop1 in loop1:
    currentLoop = loop1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
    if thisLoop1 != None:
        for paramName in thisLoop1:
            exec('{} = thisLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_hor"-------
    continueRoutine = True
    routineTimer.add(5.300000)
    # update component parameters for each repeat
    image.setImage(path1)
    key_resp_practice.keys = []
    key_resp_practice.rt = []
    _key_resp_practice_allKeys = []
    # keep track of which components have finished
    practice_horComponents = [text, image, key_resp_practice]
    for thisComponent in practice_horComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_horClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_hor"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_horClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_horClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
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
        
        # *key_resp_practice* updates
        waitOnFlip = False
        if key_resp_practice.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            key_resp_practice.frameNStart = frameN  # exact frame index
            key_resp_practice.tStart = t  # local t and not account for scr refresh
            key_resp_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_practice, 'tStartRefresh')  # time at next scr refresh
            key_resp_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_practice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_practice.tStop = t  # not accounting for scr refresh
                key_resp_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_practice, 'tStopRefresh')  # time at next scr refresh
                key_resp_practice.status = FINISHED
        if key_resp_practice.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_practice.getKeys(keyList=['left', 'right', 'up', 'down'], waitRelease=False)
            _key_resp_practice_allKeys.extend(theseKeys)
            if len(_key_resp_practice_allKeys):
                key_resp_practice.keys = _key_resp_practice_allKeys[-1].name  # just the last key pressed
                key_resp_practice.rt = _key_resp_practice_allKeys[-1].rt
                # was this correct?
                if (key_resp_practice.keys == str(corresp1)) or (key_resp_practice.keys == corresp1):
                    key_resp_practice.corr = 1
                else:
                    key_resp_practice.corr = 0
                # a response ends the routine
                continueRoutine = False
        if key_resp_practice.corr:
            message="回答正确"
        else:
            message="回答错误"
        if not key_resp_practice.keys:
            message="请在三秒内按键"
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_horComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_hor"-------
    for thisComponent in practice_horComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop1.addData('text.started', text.tStartRefresh)
    loop1.addData('text.stopped', text.tStopRefresh)
    loop1.addData('image.started', image.tStartRefresh)
    loop1.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_practice.keys in ['', [], None]:  # No response was made
        key_resp_practice.keys = None
        # was no response the correct answer?!
        if str(corresp1).lower() == 'none':
           key_resp_practice.corr = 1;  # correct non-response
        else:
           key_resp_practice.corr = 0;  # failed to respond (incorrectly)
    # store data for loop1 (TrialHandler)
    loop1.addData('key_resp_practice.keys',key_resp_practice.keys)
    loop1.addData('key_resp_practice.corr', key_resp_practice.corr)
    if key_resp_practice.keys != None:  # we had a response
        loop1.addData('key_resp_practice.rt', key_resp_practice.rt)
    loop1.addData('key_resp_practice.started', key_resp_practice.tStartRefresh)
    loop1.addData('key_resp_practice.stopped', key_resp_practice.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_5.setText(message)
    # keep track of which components have finished
    feedbackComponents = [text_5]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
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
            if tThisFlipGlobal > text_5.tStartRefresh + 1.0-frameTolerance:
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
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop1.addData('text_5.started', text_5.tStartRefresh)
    loop1.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop1'


# ------Prepare to start Routine "rest1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
rest1Components = [text_11, key_resp_6]
for thisComponent in rest1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rest1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rest1"-------
while continueRoutine:
    # get current time
    t = rest1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rest1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
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
    for thisComponent in rest1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rest1"-------
for thisComponent in rest1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# the Routine "rest1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction3_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
instruction3_2Components = [text_6, key_resp_5]
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

# set up handler to look after randomisation of conditions etc
loop2 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\practice1.xlsx'),
    seed=None, name='loop2')
thisExp.addLoop(loop2)  # add the loop to the experiment
thisLoop2 = loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
if thisLoop2 != None:
    for paramName in thisLoop2:
        exec('{} = thisLoop2[paramName]'.format(paramName))

for thisLoop2 in loop2:
    currentLoop = loop2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
    if thisLoop2 != None:
        for paramName in thisLoop2:
            exec('{} = thisLoop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_ver"-------
    continueRoutine = True
    routineTimer.add(5.300000)
    # update component parameters for each repeat
    image_2.setImage(path2)
    key_resp_practice2.keys = []
    key_resp_practice2.rt = []
    _key_resp_practice2_allKeys = []
    # keep track of which components have finished
    practice_verComponents = [text_7, image_2, key_resp_practice2]
    for thisComponent in practice_verComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_verClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_ver"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_verClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_verClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *key_resp_practice2* updates
        waitOnFlip = False
        if key_resp_practice2.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            key_resp_practice2.frameNStart = frameN  # exact frame index
            key_resp_practice2.tStart = t  # local t and not account for scr refresh
            key_resp_practice2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_practice2, 'tStartRefresh')  # time at next scr refresh
            key_resp_practice2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_practice2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_practice2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_practice2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_practice2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_practice2.tStop = t  # not accounting for scr refresh
                key_resp_practice2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_practice2, 'tStopRefresh')  # time at next scr refresh
                key_resp_practice2.status = FINISHED
        if key_resp_practice2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_practice2.getKeys(keyList=['up', 'down', 'left', 'right'], waitRelease=False)
            _key_resp_practice2_allKeys.extend(theseKeys)
            if len(_key_resp_practice2_allKeys):
                key_resp_practice2.keys = _key_resp_practice2_allKeys[-1].name  # just the last key pressed
                key_resp_practice2.rt = _key_resp_practice2_allKeys[-1].rt
                # was this correct?
                if (key_resp_practice2.keys == str(corresp2)) or (key_resp_practice2.keys == corresp2):
                    key_resp_practice2.corr = 1
                else:
                    key_resp_practice2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_verComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_ver"-------
    for thisComponent in practice_verComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop2.addData('text_7.started', text_7.tStartRefresh)
    loop2.addData('text_7.stopped', text_7.tStopRefresh)
    loop2.addData('image_2.started', image_2.tStartRefresh)
    loop2.addData('image_2.stopped', image_2.tStopRefresh)
    # check responses
    if key_resp_practice2.keys in ['', [], None]:  # No response was made
        key_resp_practice2.keys = None
        # was no response the correct answer?!
        if str(corresp2).lower() == 'none':
           key_resp_practice2.corr = 1;  # correct non-response
        else:
           key_resp_practice2.corr = 0;  # failed to respond (incorrectly)
    # store data for loop2 (TrialHandler)
    loop2.addData('key_resp_practice2.keys',key_resp_practice2.keys)
    loop2.addData('key_resp_practice2.corr', key_resp_practice2.corr)
    if key_resp_practice2.keys != None:  # we had a response
        loop2.addData('key_resp_practice2.rt', key_resp_practice2.rt)
    loop2.addData('key_resp_practice2.started', key_resp_practice2.tStartRefresh)
    loop2.addData('key_resp_practice2.stopped', key_resp_practice2.tStopRefresh)
    if key_resp_practice2.corr:
        message2="回答正确"
    else:
        message2="回答错误"
    if not key_resp_practice2.keys:
        message2="请在三秒内按键"
    
    # ------Prepare to start Routine "feedback2"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_8.setText(message2)
    # keep track of which components have finished
    feedback2Components = [text_8]
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
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
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
    loop2.addData('text_8.started', text_8.tStartRefresh)
    loop2.addData('text_8.stopped', text_8.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop2'


# ------Prepare to start Routine "rest1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
rest1Components = [text_11, key_resp_6]
for thisComponent in rest1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rest1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rest1"-------
while continueRoutine:
    # get current time
    t = rest1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rest1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
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
    for thisComponent in rest1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rest1"-------
for thisComponent in rest1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# the Routine "rest1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
instruction5Components = [text_12, key_resp_7]
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
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
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
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# the Routine "instruction5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\practice2.xlsx'),
    seed=None, name='loop3')
thisExp.addLoop(loop3)  # add the loop to the experiment
thisLoop3 = loop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
if thisLoop3 != None:
    for paramName in thisLoop3:
        exec('{} = thisLoop3[paramName]'.format(paramName))

for thisLoop3 in loop3:
    currentLoop = loop3
    # abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
    if thisLoop3 != None:
        for paramName in thisLoop3:
            exec('{} = thisLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_mix"-------
    continueRoutine = True
    routineTimer.add(5.300000)
    # update component parameters for each repeat
    image_3.setImage(path)
    key_resp_practice3.keys = []
    key_resp_practice3.rt = []
    _key_resp_practice3_allKeys = []
    # keep track of which components have finished
    practice_mixComponents = [text_9, image_3, key_resp_practice3]
    for thisComponent in practice_mixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_mixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_mix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_mixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_mixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # *key_resp_practice3* updates
        waitOnFlip = False
        if key_resp_practice3.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            key_resp_practice3.frameNStart = frameN  # exact frame index
            key_resp_practice3.tStart = t  # local t and not account for scr refresh
            key_resp_practice3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_practice3, 'tStartRefresh')  # time at next scr refresh
            key_resp_practice3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_practice3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_practice3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_practice3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_practice3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_practice3.tStop = t  # not accounting for scr refresh
                key_resp_practice3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_practice3, 'tStopRefresh')  # time at next scr refresh
                key_resp_practice3.status = FINISHED
        if key_resp_practice3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_practice3.getKeys(keyList=['left', 'right', 'up', 'down'], waitRelease=False)
            _key_resp_practice3_allKeys.extend(theseKeys)
            if len(_key_resp_practice3_allKeys):
                key_resp_practice3.keys = _key_resp_practice3_allKeys[-1].name  # just the last key pressed
                key_resp_practice3.rt = _key_resp_practice3_allKeys[-1].rt
                # was this correct?
                if (key_resp_practice3.keys == str(corresp)) or (key_resp_practice3.keys == corresp):
                    key_resp_practice3.corr = 1
                else:
                    key_resp_practice3.corr = 0
                # a response ends the routine
                continueRoutine = False
        if key_resp_practice3.corr:
            message3="回答正确"
        else:
            message3="回答错误"
        if not key_resp_practice3.keys:
            message3="请在三秒内按键"
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_mixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_mix"-------
    for thisComponent in practice_mixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop3.addData('text_9.started', text_9.tStartRefresh)
    loop3.addData('text_9.stopped', text_9.tStopRefresh)
    loop3.addData('image_3.started', image_3.tStartRefresh)
    loop3.addData('image_3.stopped', image_3.tStopRefresh)
    # check responses
    if key_resp_practice3.keys in ['', [], None]:  # No response was made
        key_resp_practice3.keys = None
        # was no response the correct answer?!
        if str(corresp).lower() == 'none':
           key_resp_practice3.corr = 1;  # correct non-response
        else:
           key_resp_practice3.corr = 0;  # failed to respond (incorrectly)
    # store data for loop3 (TrialHandler)
    loop3.addData('key_resp_practice3.keys',key_resp_practice3.keys)
    loop3.addData('key_resp_practice3.corr', key_resp_practice3.corr)
    if key_resp_practice3.keys != None:  # we had a response
        loop3.addData('key_resp_practice3.rt', key_resp_practice3.rt)
    loop3.addData('key_resp_practice3.started', key_resp_practice3.tStartRefresh)
    loop3.addData('key_resp_practice3.stopped', key_resp_practice3.tStopRefresh)
    
    # ------Prepare to start Routine "feedback3"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_10.setText(message3)
    # keep track of which components have finished
    feedback3Components = [text_10]
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
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_10.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                text_10.setAutoDraw(False)
        
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
    loop3.addData('text_10.started', text_10.tStartRefresh)
    loop3.addData('text_10.stopped', text_10.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop3'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(4.000000)
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
        if tThisFlipGlobal > text_2.tStartRefresh + 4-frameTolerance:
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
