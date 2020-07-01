#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 五月 13, 2020, at 19:13
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
expName = 'stroop'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\zhang\\Desktop\\张以昊\\课题组\\psychopy\\stroop\\stroop.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='接下来你将看到红，蓝，绿三种\n颜色的字。如果字颜色为红色，\n按下键盘左键；如果字颜色为\n黄色，按下键盘上建；如果为\n蓝色，按下键盘下键。下面按下\n空格键开始练习。（不计入数据）\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
startbutton = keyboard.Keyboard()

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

# Initialize components for Routine "justice"
justiceClock = core.Clock()
choose = visual.TextStim(win=win, name='choose',
    text='感觉自己熟悉了吗？如果不熟悉，\n按键盘左键，我们继续练习；如果\n已经熟悉，按键盘右键，实验正式\n开始。',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

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
    text='现在休息20秒吧',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
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
    text='实验结束，感谢您参与本次实验。\n请按空格键退出',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
startbutton.keys = []
startbutton.rt = []
_startbutton_allKeys = []
# keep track of which components have finished
instructionComponents = [text, startbutton]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
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
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial1.xlsx'),
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
    while continueRoutine:
        # get current time
        t = preparationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=preparationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *preparation3* updates
        if preparation3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        if character_pre.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
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
        if key_resp_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
            theseKeys = key_resp_5.getKeys(keyList=['left', 'right', 'up'], waitRelease=False)
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
    trials.addData('preparation3.started', preparation3.tStartRefresh)
    trials.addData('preparation3.stopped', preparation3.tStopRefresh)
    trials.addData('character_pre.started', character_pre.tStartRefresh)
    trials.addData('character_pre.stopped', character_pre.tStopRefresh)
    # the Routine "preparation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


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
thisExp.addData('choose.started', choose.tStartRefresh)
thisExp.addData('choose.stopped', choose.tStopRefresh)
# the Routine "justice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop1 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial1.xlsx'),
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
    while continueRoutine:
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
        if character1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
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
        if key_resp.status == STARTED and not waitOnFlip:
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
    loop1.addData('key_resp.started', key_resp.tStartRefresh)
    loop1.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
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
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
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
    trialList=data.importConditions('trial2.xlsx'),
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
    while continueRoutine:
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
        if character2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
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
            theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
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
    loop2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        loop2.addData('key_resp_2.rt', key_resp_2.rt)
    loop2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    loop2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop2'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
thanksComponents = [thank, key_resp_4]
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
while continueRoutine:
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
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
