#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on 八月 05, 2021, at 09:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import string
allLetters = list(string.digits)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.2'
expName = '第一次正误'  # from the Builder filename that created this script
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
    originPath='D:\\张以昊\\张以昊\\个人\\psychopy\\psychopy实验范式\\13_Memory_Task\\reference\\修复第一次记忆正误判断\\第一次正误_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instruction_1 = visual.ImageStim(
    win=win,
    name='instruction_1', 
    image='image/introduction.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.76, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_instruction = keyboard.Keyboard()

# Initialize components for Routine "four"
fourClock = core.Clock()
four_concentration = visual.TextStim(win=win, name='four_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
four_1 = visual.TextStim(win=win, name='four_1',
    text='8',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
four_2 = visual.TextStim(win=win, name='four_2',
    text='1',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
four_3 = visual.TextStim(win=win, name='four_3',
    text='7',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
four_input = visual.TextStim(win=win, name='four_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
textFill = ''

# Initialize components for Routine "five"
fiveClock = core.Clock()
five_input = visual.TextStim(win=win, name='five_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_instruction.keys = []
key_instruction.rt = []
_key_instruction_allKeys = []
# keep track of which components have finished
instructionComponents = [instruction_1, key_instruction]
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
    
    # *instruction_1* updates
    if instruction_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_1.frameNStart = frameN  # exact frame index
        instruction_1.tStart = t  # local t and not account for scr refresh
        instruction_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_1, 'tStartRefresh')  # time at next scr refresh
        instruction_1.setAutoDraw(True)
    
    # *key_instruction* updates
    if key_instruction.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_instruction.frameNStart = frameN  # exact frame index
        key_instruction.tStart = t  # local t and not account for scr refresh
        key_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_instruction, 'tStartRefresh')  # time at next scr refresh
        key_instruction.status = STARTED
        # keyboard checking is just starting
        key_instruction.clock.reset()  # now t=0
        key_instruction.clearEvents(eventType='keyboard')
    if key_instruction.status == STARTED:
        theseKeys = key_instruction.getKeys(keyList=['space'], waitRelease=False)
        _key_instruction_allKeys.extend(theseKeys)
        if len(_key_instruction_allKeys):
            key_instruction.keys = _key_instruction_allKeys[-1].name  # just the last key pressed
            key_instruction.rt = _key_instruction_allKeys[-1].rt
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
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "four"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
fourComponents = [four_concentration, four_1, four_2, four_3, four_input]
for thisComponent in fourComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fourClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "four"-------
while continueRoutine:
    # get current time
    t = fourClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fourClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *four_concentration* updates
    if four_concentration.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_concentration.frameNStart = frameN  # exact frame index
        four_concentration.tStart = t  # local t and not account for scr refresh
        four_concentration.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_concentration, 'tStartRefresh')  # time at next scr refresh
        four_concentration.setAutoDraw(True)
    if four_concentration.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > four_concentration.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            four_concentration.tStop = t  # not accounting for scr refresh
            four_concentration.frameNStop = frameN  # exact frame index
            win.timeOnFlip(four_concentration, 'tStopRefresh')  # time at next scr refresh
            four_concentration.setAutoDraw(False)
    
    # *four_1* updates
    if four_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        four_1.frameNStart = frameN  # exact frame index
        four_1.tStart = t  # local t and not account for scr refresh
        four_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_1, 'tStartRefresh')  # time at next scr refresh
        four_1.setAutoDraw(True)
    if four_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > four_1.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            four_1.tStop = t  # not accounting for scr refresh
            four_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(four_1, 'tStopRefresh')  # time at next scr refresh
            four_1.setAutoDraw(False)
    
    # *four_2* updates
    if four_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
        # keep track of start time/frame for later
        four_2.frameNStart = frameN  # exact frame index
        four_2.tStart = t  # local t and not account for scr refresh
        four_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_2, 'tStartRefresh')  # time at next scr refresh
        four_2.setAutoDraw(True)
    if four_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > four_2.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            four_2.tStop = t  # not accounting for scr refresh
            four_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(four_2, 'tStopRefresh')  # time at next scr refresh
            four_2.setAutoDraw(False)
    
    # *four_3* updates
    if four_3.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
        # keep track of start time/frame for later
        four_3.frameNStart = frameN  # exact frame index
        four_3.tStart = t  # local t and not account for scr refresh
        four_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_3, 'tStartRefresh')  # time at next scr refresh
        four_3.setAutoDraw(True)
    if four_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > four_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            four_3.tStop = t  # not accounting for scr refresh
            four_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(four_3, 'tStopRefresh')  # time at next scr refresh
            four_3.setAutoDraw(False)
    
    # *four_input* updates
    if four_input.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
        # keep track of start time/frame for later
        four_input.frameNStart = frameN  # exact frame index
        four_input.tStart = t  # local t and not account for scr refresh
        four_input.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_input, 'tStartRefresh')  # time at next scr refresh
        four_input.setAutoDraw(True)
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()  # So you can quit
    else:
        if keys:
            if keys[0] == 'space':
                textFill += ' '  # Adds a space instead of 'space'
            elif keys[0] == 'backspace':
                textFill = textFill[:-1]  # Deletes
            elif keys[0] in allLetters:
                textFill+=keys[0]  # Adds character to text if in alphabet.
            four_input.setText(textFill)  # Set new text on screen
            if keys[0] == 'return':
                textFill.strip()
                thisExp.addData('four', textFill)
                if textFill == '8174':
                    thisExp.addData('four_corr', 1)
                else: 
                    thisExp.addData('four_corr', 0)
                four_input.setText(textFill)
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fourComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "four"-------
for thisComponent in fourComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('four_input.started', four_input.tStartRefresh)
thisExp.addData('four_input.stopped', four_input.tStopRefresh)
# the Routine "four" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "five"-------
continueRoutine = True
# update component parameters for each repeat
textFill = ''
# keep track of which components have finished
fiveComponents = [five_input]
for thisComponent in fiveComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fiveClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "five"-------
while continueRoutine:
    # get current time
    t = fiveClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fiveClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *five_input* updates
    if five_input.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_input.frameNStart = frameN  # exact frame index
        five_input.tStart = t  # local t and not account for scr refresh
        five_input.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_input, 'tStartRefresh')  # time at next scr refresh
        five_input.setAutoDraw(True)
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()  # So you can quit
    else:
        if keys:
            if keys[0] == 'space':
                textFill += ' '  # Adds a space instead of 'space'
            elif keys[0] == 'backspace':
                textFill = textFill[:-1]  # Deletes
            elif keys[0] in allLetters:
                textFill+=keys[0]  # Adds character to text if in alphabet.
            five_input.setText(textFill)  # Set new text on screen
            if keys[0] == 'return':
                textFill.strip()
                thisExp.addData('five', textFill)
                if textFill == '81742':
                    thisExp.addData('five_corr', 1)
                else: 
                    thisExp.addData('five_corr', 0)
                five_input.setText(textFill)
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fiveComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "five"-------
for thisComponent in fiveComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('five_input.started', five_input.tStartRefresh)
thisExp.addData('five_input.stopped', five_input.tStopRefresh)
# the Routine "five" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
