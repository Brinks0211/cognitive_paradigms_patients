#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 六月 14, 2020, at 14:59
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
expName = 'Stroop'  # from the Builder filename that created this script
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
    originPath='D:\\jianguoyun\\课题组\\5_Stroop\\stroop_lastrun.py',
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

# Initialize components for Routine "introduction1"
introduction1Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='欢迎参加测试\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "instruction2"
instruction2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='接下来你将看到红、黄、蓝三种颜色的字。\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
startbutton = keyboard.Keyboard()

# Initialize components for Routine "instruction3"
instruction3Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='如果字颜色为红色，按下键盘左键\n如果字颜色为黄色，按下键盘上键\n如果字颜色为蓝色，按下键盘右键\n\n（继续，请按空格键）\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "introduction4"
introduction4Clock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='下面是练习阶段\n\n（继续，请按空格键）\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "preparation"
preparationClock = core.Clock()
preparation3 = visual.TextStim(win=win, name='preparation3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
character_pre = visual.TextStim(win=win, name='character_pre',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()
text3=0
m=0
n=0

# Initialize components for Routine "consequence1"
consequence1Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "justice"
justiceClock = core.Clock()
choose = visual.TextStim(win=win, name='choose',
    text='感觉自己熟悉了吗？\n\n如果不熟悉，请按左键，继续练习\n如果已经熟悉，请按右键，开始正式实验\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "tip1"
tip1Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='下面进入正式测试\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
preparation1 = visual.TextStim(win=win, name='preparation1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
character1 = visual.TextStim(win=win, name='character1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='现在是休息阶段\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
preparation2 = visual.TextStim(win=win, name='preparation2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
character2 = visual.TextStim(win=win, name='character2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thank = visual.TextStim(win=win, name='thank',
    text='测试结束，谢谢您的参与。',
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
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
introduction1Components = [text_9, key_resp_8]
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
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
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
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# the Routine "introduction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction2"-------
continueRoutine = True
# update component parameters for each repeat
startbutton.keys = []
startbutton.rt = []
_startbutton_allKeys = []
# keep track of which components have finished
instruction2Components = [text, startbutton]
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
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *startbutton* updates
    waitOnFlip = False
    if startbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startbutton.frameNStart = frameN  # exact frame index
        startbutton.tStart = t  # local t and not account for scr refresh
        startbutton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startbutton, 'tStartRefresh')  # time at next scr refresh
        startbutton.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startbutton.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startbutton.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startbutton.status == STARTED and not waitOnFlip:
        theseKeys = startbutton.getKeys(keyList=['space'], waitRelease=False)
        _startbutton_allKeys.extend(theseKeys)
        if len(_startbutton_allKeys):
            startbutton.keys = _startbutton_allKeys[-1].name  # just the last key pressed
            startbutton.rt = _startbutton_allKeys[-1].rt
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
instruction3Components = [text_10, key_resp_9]
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
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
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
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
introduction4Components = [text_11, key_resp_10]
for thisComponent in introduction4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction4"-------
while continueRoutine:
    # get current time
    t = introduction4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction4Clock)
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
    for thisComponent in introduction4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction4"-------
for thisComponent in introduction4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# the Routine "introduction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop3 = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('documents\\trial1.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "preparation"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        character_pre.setColor(color, colorSpace='rgb')
        character_pre.setText(characters
)
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        preparationComponents = [preparation3, character_pre, key_resp_5]
        for thisComponent in preparationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        preparationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "preparation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = preparationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=preparationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *preparation3* updates
            if preparation3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                preparation3.frameNStart = frameN  # exact frame index
                preparation3.tStart = t  # local t and not account for scr refresh
                preparation3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(preparation3, 'tStartRefresh')  # time at next scr refresh
                preparation3.setAutoDraw(True)
            if preparation3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > preparation3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    preparation3.tStop = t  # not accounting for scr refresh
                    preparation3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(preparation3, 'tStopRefresh')  # time at next scr refresh
                    preparation3.setAutoDraw(False)
            
            # *character_pre* updates
            if character_pre.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                character_pre.frameNStart = frameN  # exact frame index
                character_pre.tStart = t  # local t and not account for scr refresh
                character_pre.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(character_pre, 'tStartRefresh')  # time at next scr refresh
                character_pre.setAutoDraw(True)
            if character_pre.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > character_pre.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    character_pre.tStop = t  # not accounting for scr refresh
                    character_pre.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(character_pre, 'tStopRefresh')  # time at next scr refresh
                    character_pre.setAutoDraw(False)
            
            # *key_resp_5* updates
            if key_resp_5.status == NOT_STARTED and t >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                key_resp_5.clock.reset()  # now t=0
                key_resp_5.clearEvents(eventType='keyboard')
            if key_resp_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_5.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_5.tStop = t  # not accounting for scr refresh
                    key_resp_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                    key_resp_5.status = FINISHED
            if key_resp_5.status == STARTED:
                theseKeys = key_resp_5.getKeys(keyList=['left', 'right', 'up'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_5.keys == str(corresp)) or (key_resp_5.keys == corresp):
                        key_resp_5.corr = 1
                    else:
                        key_resp_5.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in preparationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "preparation"-------
        for thisComponent in preparationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
            # was no response the correct answer?!
            if str(corresp).lower() == 'none':
               key_resp_5.corr = 1;  # correct non-response
            else:
               key_resp_5.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp_5.keys',key_resp_5.keys)
        trials.addData('key_resp_5.corr', key_resp_5.corr)
        if key_resp_5.keys != None:  # we had a response
            trials.addData('key_resp_5.rt', key_resp_5.rt)
        trials.addData('key_resp_5.started', key_resp_5.tStart)
        trials.addData('key_resp_5.stopped', key_resp_5.tStop)
        if key_resp_5.corr:
            text3='回答正确'
            n+=1
        else:
            text3='回答错误'
        
        
        # ------Prepare to start Routine "consequence1"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text_3.setText(text3)
        # keep track of which components have finished
        consequence1Components = [text_3]
        for thisComponent in consequence1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        consequence1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "consequence1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = consequence1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=consequence1Clock)
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
            for thisComponent in consequence1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "consequence1"-------
        for thisComponent in consequence1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('text_3.started', text_3.tStartRefresh)
        trials.addData('text_3.stopped', text_3.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "justice"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    justiceComponents = [choose, key_resp_6]
    for thisComponent in justiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    justiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "justice"-------
    while continueRoutine:
        # get current time
        t = justiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=justiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choose* updates
        if choose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choose.frameNStart = frameN  # exact frame index
            choose.tStart = t  # local t and not account for scr refresh
            choose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choose, 'tStartRefresh')  # time at next scr refresh
            choose.setAutoDraw(True)
        
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
            theseKeys = key_resp_6.getKeys(keyList=['left', 'right'], waitRelease=False)
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
        for thisComponent in justiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "justice"-------
    for thisComponent in justiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop3.addData('choose.started', choose.tStartRefresh)
    loop3.addData('choose.stopped', choose.tStopRefresh)
    if 'right'in key_resp_6.keys:
        loop3.finished=True
    # the Routine "justice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'loop3'


# ------Prepare to start Routine "tip1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
tip1Components = [text_12, key_resp_11]
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
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
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
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# the Routine "tip1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop1 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\trial2.xlsx'),
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
    
    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    character1.setColor(color, colorSpace='rgb')
    character1.setText(characters)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trial1Components = [preparation1, character1, key_resp]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *preparation1* updates
        if preparation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            preparation1.frameNStart = frameN  # exact frame index
            preparation1.tStart = t  # local t and not account for scr refresh
            preparation1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(preparation1, 'tStartRefresh')  # time at next scr refresh
            preparation1.setAutoDraw(True)
        if preparation1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > preparation1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                preparation1.tStop = t  # not accounting for scr refresh
                preparation1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(preparation1, 'tStopRefresh')  # time at next scr refresh
                preparation1.setAutoDraw(False)
        
        # *character1* updates
        if character1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            character1.frameNStart = frameN  # exact frame index
            character1.tStart = t  # local t and not account for scr refresh
            character1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(character1, 'tStartRefresh')  # time at next scr refresh
            character1.setAutoDraw(True)
        if character1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > character1.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                character1.tStop = t  # not accounting for scr refresh
                character1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(character1, 'tStopRefresh')  # time at next scr refresh
                character1.setAutoDraw(False)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['right', 'left', 'up'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corresp)) or (key_resp.keys == corresp):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop1.addData('preparation1.started', preparation1.tStartRefresh)
    loop1.addData('preparation1.stopped', preparation1.tStopRefresh)
    loop1.addData('character1.started', character1.tStartRefresh)
    loop1.addData('character1.stopped', character1.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corresp).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for loop1 (TrialHandler)
    loop1.addData('key_resp.keys',key_resp.keys)
    loop1.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        loop1.addData('key_resp.rt', key_resp.rt)
    loop1.addData('key_resp.started', key_resp.tStart)
    loop1.addData('key_resp.stopped', key_resp.tStop)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop1'


# ------Prepare to start Routine "rest"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
restComponents = [text_2, key_resp_3]
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
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
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
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "rest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop2 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\trial2.xlsx'),
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
    
    # ------Prepare to start Routine "trial2"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    character2.setColor(color, colorSpace='rgb')
    character2.setText(characters)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    trial2Components = [preparation2, character2, key_resp_2]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *preparation2* updates
        if preparation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            preparation2.frameNStart = frameN  # exact frame index
            preparation2.tStart = t  # local t and not account for scr refresh
            preparation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(preparation2, 'tStartRefresh')  # time at next scr refresh
            preparation2.setAutoDraw(True)
        if preparation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > preparation2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                preparation2.tStop = t  # not accounting for scr refresh
                preparation2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(preparation2, 'tStopRefresh')  # time at next scr refresh
                preparation2.setAutoDraw(False)
        
        # *character2* updates
        if character2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            character2.frameNStart = frameN  # exact frame index
            character2.tStart = t  # local t and not account for scr refresh
            character2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(character2, 'tStartRefresh')  # time at next scr refresh
            character2.setAutoDraw(True)
        if character2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > character2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                character2.tStop = t  # not accounting for scr refresh
                character2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(character2, 'tStopRefresh')  # time at next scr refresh
                character2.setAutoDraw(False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['left', 'right', 'up'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # was this correct?
                if (key_resp_2.keys == str(corresp)) or (key_resp_2.keys == corresp):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop2.addData('preparation2.started', preparation2.tStartRefresh)
    loop2.addData('preparation2.stopped', preparation2.tStopRefresh)
    loop2.addData('character2.started', character2.tStartRefresh)
    loop2.addData('character2.stopped', character2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(corresp).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for loop2 (TrialHandler)
    loop2.addData('key_resp_2.keys',key_resp_2.keys)
    loop2.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        loop2.addData('key_resp_2.rt', key_resp_2.rt)
    loop2.addData('key_resp_2.started', key_resp_2.tStart)
    loop2.addData('key_resp_2.stopped', key_resp_2.tStop)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop2'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thank]
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
    
    # *thank* updates
    if thank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank.frameNStart = frameN  # exact frame index
        thank.tStart = t  # local t and not account for scr refresh
        thank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank, 'tStartRefresh')  # time at next scr refresh
        thank.setAutoDraw(True)
    if thank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            thank.tStop = t  # not accounting for scr refresh
            thank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thank, 'tStopRefresh')  # time at next scr refresh
            thank.setAutoDraw(False)
    
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
thisExp.addData('thank.started', thank.tStartRefresh)
thisExp.addData('thank.stopped', thank.tStopRefresh)

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
