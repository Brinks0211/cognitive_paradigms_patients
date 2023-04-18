#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on 八月 08, 2021, at 08:48
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
expName = 'Memory_Task'  # from the Builder filename that created this script
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
    originPath='D:\\张以昊\\张以昊\\个人\\psychopy\\psychopy实验范式\\13_Memory_Task\\Memory_Task.py',
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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='image/introduction.png', mask=None,
    ori=0, pos=(0, 0), size=(1.76, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
introduction_key = keyboard.Keyboard()
button = 4
textFill = ''
over = 0

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
four_4 = visual.TextStim(win=win, name='four_4',
    text='4',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
four_input = visual.TextStim(win=win, name='four_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
four_tip = visual.TextStim(win=win, name='four_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "five"
fiveClock = core.Clock()
concentration_five = visual.TextStim(win=win, name='concentration_five',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
five_1 = visual.TextStim(win=win, name='five_1',
    text='3',
    font='Open Sans',
    pos=(-0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
five_2 = visual.TextStim(win=win, name='five_2',
    text='4',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
five_3 = visual.TextStim(win=win, name='five_3',
    text='6\n',
    font='Open Sans',
    pos=(0, -0.07), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
five_4 = visual.TextStim(win=win, name='five_4',
    text='1',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
five_5 = visual.TextStim(win=win, name='five_5',
    text='3',
    font='Open Sans',
    pos=(0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
five_input = visual.TextStim(win=win, name='five_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
five_tip = visual.TextStim(win=win, name='five_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "six"
sixClock = core.Clock()
concentration_six = visual.TextStim(win=win, name='concentration_six',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
six_1 = visual.TextStim(win=win, name='six_1',
    text='2',
    font='Open Sans',
    pos=(-0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
six_2 = visual.TextStim(win=win, name='six_2',
    text='2',
    font='Open Sans',
    pos=(-0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
six_3 = visual.TextStim(win=win, name='six_3',
    text='7',
    font='Open Sans',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
six_4 = visual.TextStim(win=win, name='six_4',
    text='4',
    font='Open Sans',
    pos=(0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
six_5 = visual.TextStim(win=win, name='six_5',
    text='8',
    font='Open Sans',
    pos=(0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
six_6 = visual.TextStim(win=win, name='six_6',
    text='5',
    font='Open Sans',
    pos=(0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
six_input = visual.TextStim(win=win, name='six_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
six_tip = visual.TextStim(win=win, name='six_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "severn"
severnClock = core.Clock()
concentration_seven = visual.TextStim(win=win, name='concentration_seven',
    text='+\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
seven_1 = visual.TextStim(win=win, name='seven_1',
    text='3',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
seven_2 = visual.TextStim(win=win, name='seven_2',
    text='8',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
seven_3 = visual.TextStim(win=win, name='seven_3',
    text='6',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
seven_4 = visual.TextStim(win=win, name='seven_4',
    text='4',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
seven_5 = visual.TextStim(win=win, name='seven_5',
    text='1',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
seven_6 = visual.TextStim(win=win, name='seven_6',
    text='4',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
seven_7 = visual.TextStim(win=win, name='seven_7',
    text='7',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
seven_input = visual.TextStim(win=win, name='seven_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
seven_tip = visual.TextStim(win=win, name='seven_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "eight"
eightClock = core.Clock()
eight_concentration = visual.TextStim(win=win, name='eight_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
eight_1 = visual.TextStim(win=win, name='eight_1',
    text='4',
    font='Open Sans',
    pos=(-0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
eight_2 = visual.TextStim(win=win, name='eight_2',
    text='3',
    font='Open Sans',
    pos=(-0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
eight_3 = visual.TextStim(win=win, name='eight_3',
    text='7',
    font='Open Sans',
    pos=(-0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
eight_4 = visual.TextStim(win=win, name='eight_4',
    text='8',
    font='Open Sans',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
eight_5 = visual.TextStim(win=win, name='eight_5',
    text='9',
    font='Open Sans',
    pos=(0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
eight_6 = visual.TextStim(win=win, name='eight_6',
    text='7',
    font='Open Sans',
    pos=(0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
eight_7 = visual.TextStim(win=win, name='eight_7',
    text='8',
    font='Open Sans',
    pos=(0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
eight_8 = visual.TextStim(win=win, name='eight_8',
    text='6',
    font='Open Sans',
    pos=(0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
eight_input = visual.TextStim(win=win, name='eight_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
eight_tip = visual.TextStim(win=win, name='eight_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "nine"
nineClock = core.Clock()
nine_concentration = visual.TextStim(win=win, name='nine_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
nine_1 = visual.TextStim(win=win, name='nine_1',
    text='4',
    font='Open Sans',
    pos=(-0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
nine_2 = visual.TextStim(win=win, name='nine_2',
    text='4',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
nine_3 = visual.TextStim(win=win, name='nine_3',
    text='3',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
nine_4 = visual.TextStim(win=win, name='nine_4',
    text='5',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
nine_5 = visual.TextStim(win=win, name='nine_5',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
nine_6 = visual.TextStim(win=win, name='nine_6',
    text='1',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
nine_7 = visual.TextStim(win=win, name='nine_7',
    text='7',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
nine_8 = visual.TextStim(win=win, name='nine_8',
    text='2',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
nine_9 = visual.TextStim(win=win, name='nine_9',
    text='9',
    font='Open Sans',
    pos=(0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
nine_input = visual.TextStim(win=win, name='nine_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
nine_tip = visual.TextStim(win=win, name='nine_tip',
    text=None,
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thank = visual.TextStim(win=win, name='thank',
    text='感谢您参与本次实验！',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction"-------
continueRoutine = True
# update component parameters for each repeat
introduction_key.keys = []
introduction_key.rt = []
_introduction_key_allKeys = []
# keep track of which components have finished
introductionComponents = [image, introduction_key]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *introduction_key* updates
    waitOnFlip = False
    if introduction_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_key.frameNStart = frameN  # exact frame index
        introduction_key.tStart = t  # local t and not account for scr refresh
        introduction_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_key, 'tStartRefresh')  # time at next scr refresh
        introduction_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(introduction_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(introduction_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if introduction_key.status == STARTED and not waitOnFlip:
        theseKeys = introduction_key.getKeys(keyList=['space'], waitRelease=False)
        _introduction_key_allKeys.extend(theseKeys)
        if len(_introduction_key_allKeys):
            introduction_key.keys = _introduction_key_allKeys[-1].name  # just the last key pressed
            introduction_key.rt = _introduction_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_or = data.TrialHandler(nReps=7.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_or')
thisExp.addLoop(loop_or)  # add the loop to the experiment
thisLoop_or = loop_or.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_or.rgb)
if thisLoop_or != None:
    for paramName in thisLoop_or:
        exec('{} = thisLoop_or[paramName]'.format(paramName))

for thisLoop_or in loop_or:
    currentLoop = loop_or
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_or.rgb)
    if thisLoop_or != None:
        for paramName in thisLoop_or:
            exec('{} = thisLoop_or[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "four"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button == 4:
        textFill = ''
    else:
        continueRoutine = False
    # keep track of which components have finished
    fourComponents = [four_concentration, four_1, four_2, four_3, four_4, four_input, four_tip]
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
        
        # *four_4* updates
        if four_4.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
            # keep track of start time/frame for later
            four_4.frameNStart = frameN  # exact frame index
            four_4.tStart = t  # local t and not account for scr refresh
            four_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_4, 'tStartRefresh')  # time at next scr refresh
            four_4.setAutoDraw(True)
        if four_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four_4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                four_4.tStop = t  # not accounting for scr refresh
                four_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four_4, 'tStopRefresh')  # time at next scr refresh
                four_4.setAutoDraw(False)
        
        # *four_input* updates
        if four_input.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            four_input.frameNStart = frameN  # exact frame index
            four_input.tStart = t  # local t and not account for scr refresh
            four_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_input, 'tStartRefresh')  # time at next scr refresh
            four_input.setAutoDraw(True)
        
        # *four_tip* updates
        if four_tip.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            four_tip.frameNStart = frameN  # exact frame index
            four_tip.tStart = t  # local t and not account for scr refresh
            four_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_tip, 'tStartRefresh')  # time at next scr refresh
            four_tip.setAutoDraw(True)
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
                    if int(textFill) == 8174:
                        thisExp.addData('four_corr', 1)
                        button += 1
                        if over == 1:
                            loop_or.finished = True
                            button -= 1
                            thisExp.addData('result', button)
                            textFill = ''
                            four_input.setText(textFill)
                    else: 
                        thisExp.addData('four_corr', 0)
                        thisExp.addData('result', 0)
                        textFill = ''
                        four_input.setText(textFill)
                        loop_or.finished = True
                        continueRoutine = False
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
    # the Routine "four" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "five"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button ==5:
        textFill = ''
    else:
        continueRoutine = False
    # keep track of which components have finished
    fiveComponents = [concentration_five, five_1, five_2, five_3, five_4, five_5, five_input, five_tip]
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
        
        # *concentration_five* updates
        if concentration_five.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration_five.frameNStart = frameN  # exact frame index
            concentration_five.tStart = t  # local t and not account for scr refresh
            concentration_five.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration_five, 'tStartRefresh')  # time at next scr refresh
            concentration_five.setAutoDraw(True)
        if concentration_five.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration_five.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                concentration_five.tStop = t  # not accounting for scr refresh
                concentration_five.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration_five, 'tStopRefresh')  # time at next scr refresh
                concentration_five.setAutoDraw(False)
        
        # *five_1* updates
        if five_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            five_1.frameNStart = frameN  # exact frame index
            five_1.tStart = t  # local t and not account for scr refresh
            five_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_1, 'tStartRefresh')  # time at next scr refresh
            five_1.setAutoDraw(True)
        if five_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_1.tStop = t  # not accounting for scr refresh
                five_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_1, 'tStopRefresh')  # time at next scr refresh
                five_1.setAutoDraw(False)
        
        # *five_2* updates
        if five_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            five_2.frameNStart = frameN  # exact frame index
            five_2.tStart = t  # local t and not account for scr refresh
            five_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_2, 'tStartRefresh')  # time at next scr refresh
            five_2.setAutoDraw(True)
        if five_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_2.tStop = t  # not accounting for scr refresh
                five_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_2, 'tStopRefresh')  # time at next scr refresh
                five_2.setAutoDraw(False)
        
        # *five_3* updates
        if five_3.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            five_3.frameNStart = frameN  # exact frame index
            five_3.tStart = t  # local t and not account for scr refresh
            five_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_3, 'tStartRefresh')  # time at next scr refresh
            five_3.setAutoDraw(True)
        if five_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_3.tStop = t  # not accounting for scr refresh
                five_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_3, 'tStopRefresh')  # time at next scr refresh
                five_3.setAutoDraw(False)
        
        # *five_4* updates
        if five_4.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
            # keep track of start time/frame for later
            five_4.frameNStart = frameN  # exact frame index
            five_4.tStart = t  # local t and not account for scr refresh
            five_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_4, 'tStartRefresh')  # time at next scr refresh
            five_4.setAutoDraw(True)
        if five_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_4.tStop = t  # not accounting for scr refresh
                five_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_4, 'tStopRefresh')  # time at next scr refresh
                five_4.setAutoDraw(False)
        
        # *five_5* updates
        if five_5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            five_5.frameNStart = frameN  # exact frame index
            five_5.tStart = t  # local t and not account for scr refresh
            five_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_5, 'tStartRefresh')  # time at next scr refresh
            five_5.setAutoDraw(True)
        if five_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_5.tStop = t  # not accounting for scr refresh
                five_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_5, 'tStopRefresh')  # time at next scr refresh
                five_5.setAutoDraw(False)
        
        # *five_input* updates
        if five_input.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            five_input.frameNStart = frameN  # exact frame index
            five_input.tStart = t  # local t and not account for scr refresh
            five_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_input, 'tStartRefresh')  # time at next scr refresh
            five_input.setAutoDraw(True)
        
        # *five_tip* updates
        if five_tip.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            five_tip.frameNStart = frameN  # exact frame index
            five_tip.tStart = t  # local t and not account for scr refresh
            five_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_tip, 'tStartRefresh')  # time at next scr refresh
            five_tip.setAutoDraw(True)
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
                    if textFill == '34613':
                        thisExp.addData('five_corr', 1)
                        button += 1
                        if over == 1:
                            loop_or.finished = True
                            button -= 1
                            thisExp.addData('result', button)
                            textFill = ''
                            five_input.setText(textFill)
                    else: 
                        thisExp.addData('five_corr', 0)
                        over = 1
                        button -= 1
                        textFill = ''
                        five_input.setText(textFill)
                        continueRoutine = False
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
    # the Routine "five" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "six"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button == 6:
        textFill = '' 
    else:
        continueRoutine = False
    # keep track of which components have finished
    sixComponents = [concentration_six, six_1, six_2, six_3, six_4, six_5, six_6, six_input, six_tip]
    for thisComponent in sixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "six"-------
    while continueRoutine:
        # get current time
        t = sixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration_six* updates
        if concentration_six.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration_six.frameNStart = frameN  # exact frame index
            concentration_six.tStart = t  # local t and not account for scr refresh
            concentration_six.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration_six, 'tStartRefresh')  # time at next scr refresh
            concentration_six.setAutoDraw(True)
        if concentration_six.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration_six.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                concentration_six.tStop = t  # not accounting for scr refresh
                concentration_six.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration_six, 'tStopRefresh')  # time at next scr refresh
                concentration_six.setAutoDraw(False)
        
        # *six_1* updates
        if six_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            six_1.frameNStart = frameN  # exact frame index
            six_1.tStart = t  # local t and not account for scr refresh
            six_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_1, 'tStartRefresh')  # time at next scr refresh
            six_1.setAutoDraw(True)
        if six_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_1.tStop = t  # not accounting for scr refresh
                six_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_1, 'tStopRefresh')  # time at next scr refresh
                six_1.setAutoDraw(False)
        
        # *six_2* updates
        if six_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            six_2.frameNStart = frameN  # exact frame index
            six_2.tStart = t  # local t and not account for scr refresh
            six_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_2, 'tStartRefresh')  # time at next scr refresh
            six_2.setAutoDraw(True)
        if six_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_2.tStop = t  # not accounting for scr refresh
                six_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_2, 'tStopRefresh')  # time at next scr refresh
                six_2.setAutoDraw(False)
        
        # *six_3* updates
        if six_3.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            six_3.frameNStart = frameN  # exact frame index
            six_3.tStart = t  # local t and not account for scr refresh
            six_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_3, 'tStartRefresh')  # time at next scr refresh
            six_3.setAutoDraw(True)
        if six_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_3.tStop = t  # not accounting for scr refresh
                six_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_3, 'tStopRefresh')  # time at next scr refresh
                six_3.setAutoDraw(False)
        
        # *six_4* updates
        if six_4.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
            # keep track of start time/frame for later
            six_4.frameNStart = frameN  # exact frame index
            six_4.tStart = t  # local t and not account for scr refresh
            six_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_4, 'tStartRefresh')  # time at next scr refresh
            six_4.setAutoDraw(True)
        if six_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_4.tStop = t  # not accounting for scr refresh
                six_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_4, 'tStopRefresh')  # time at next scr refresh
                six_4.setAutoDraw(False)
        
        # *six_5* updates
        if six_5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            six_5.frameNStart = frameN  # exact frame index
            six_5.tStart = t  # local t and not account for scr refresh
            six_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_5, 'tStartRefresh')  # time at next scr refresh
            six_5.setAutoDraw(True)
        if six_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_5.tStop = t  # not accounting for scr refresh
                six_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_5, 'tStopRefresh')  # time at next scr refresh
                six_5.setAutoDraw(False)
        
        # *six_6* updates
        if six_6.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            six_6.frameNStart = frameN  # exact frame index
            six_6.tStart = t  # local t and not account for scr refresh
            six_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_6, 'tStartRefresh')  # time at next scr refresh
            six_6.setAutoDraw(True)
        if six_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_6.tStop = t  # not accounting for scr refresh
                six_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_6, 'tStopRefresh')  # time at next scr refresh
                six_6.setAutoDraw(False)
        
        # *six_input* updates
        if six_input.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            six_input.frameNStart = frameN  # exact frame index
            six_input.tStart = t  # local t and not account for scr refresh
            six_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_input, 'tStartRefresh')  # time at next scr refresh
            six_input.setAutoDraw(True)
        
        # *six_tip* updates
        if six_tip.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            six_tip.frameNStart = frameN  # exact frame index
            six_tip.tStart = t  # local t and not account for scr refresh
            six_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_tip, 'tStartRefresh')  # time at next scr refresh
            six_tip.setAutoDraw(True)
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
                six_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('six', textFill)
                    if textFill == '227485':
                        thisExp.addData('six_corr', 1)
                        button += 1
                        if over == 1:
                            loop_or.finished = True
                            button -= 1
                            thisExp.addData('result', button)
                    else: 
                        thisExp.addData('six_corr', 0)
                        over = 1
                        button -= 1
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "six"-------
    for thisComponent in sixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "six" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "severn"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button == 7:
        textFill = '' 
    else:
        continueRoutine = False
    # keep track of which components have finished
    severnComponents = [concentration_seven, seven_1, seven_2, seven_3, seven_4, seven_5, seven_6, seven_7, seven_input, seven_tip]
    for thisComponent in severnComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    severnClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "severn"-------
    while continueRoutine:
        # get current time
        t = severnClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=severnClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration_seven* updates
        if concentration_seven.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration_seven.frameNStart = frameN  # exact frame index
            concentration_seven.tStart = t  # local t and not account for scr refresh
            concentration_seven.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration_seven, 'tStartRefresh')  # time at next scr refresh
            concentration_seven.setAutoDraw(True)
        if concentration_seven.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration_seven.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                concentration_seven.tStop = t  # not accounting for scr refresh
                concentration_seven.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration_seven, 'tStopRefresh')  # time at next scr refresh
                concentration_seven.setAutoDraw(False)
        
        # *seven_1* updates
        if seven_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            seven_1.frameNStart = frameN  # exact frame index
            seven_1.tStart = t  # local t and not account for scr refresh
            seven_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_1, 'tStartRefresh')  # time at next scr refresh
            seven_1.setAutoDraw(True)
        if seven_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_1.tStop = t  # not accounting for scr refresh
                seven_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_1, 'tStopRefresh')  # time at next scr refresh
                seven_1.setAutoDraw(False)
        
        # *seven_2* updates
        if seven_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            seven_2.frameNStart = frameN  # exact frame index
            seven_2.tStart = t  # local t and not account for scr refresh
            seven_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_2, 'tStartRefresh')  # time at next scr refresh
            seven_2.setAutoDraw(True)
        if seven_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_2.tStop = t  # not accounting for scr refresh
                seven_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_2, 'tStopRefresh')  # time at next scr refresh
                seven_2.setAutoDraw(False)
        
        # *seven_3* updates
        if seven_3.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            seven_3.frameNStart = frameN  # exact frame index
            seven_3.tStart = t  # local t and not account for scr refresh
            seven_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_3, 'tStartRefresh')  # time at next scr refresh
            seven_3.setAutoDraw(True)
        if seven_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_3.tStop = t  # not accounting for scr refresh
                seven_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_3, 'tStopRefresh')  # time at next scr refresh
                seven_3.setAutoDraw(False)
        
        # *seven_4* updates
        if seven_4.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
            # keep track of start time/frame for later
            seven_4.frameNStart = frameN  # exact frame index
            seven_4.tStart = t  # local t and not account for scr refresh
            seven_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_4, 'tStartRefresh')  # time at next scr refresh
            seven_4.setAutoDraw(True)
        if seven_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_4.tStop = t  # not accounting for scr refresh
                seven_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_4, 'tStopRefresh')  # time at next scr refresh
                seven_4.setAutoDraw(False)
        
        # *seven_5* updates
        if seven_5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            seven_5.frameNStart = frameN  # exact frame index
            seven_5.tStart = t  # local t and not account for scr refresh
            seven_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_5, 'tStartRefresh')  # time at next scr refresh
            seven_5.setAutoDraw(True)
        if seven_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_5.tStop = t  # not accounting for scr refresh
                seven_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_5, 'tStopRefresh')  # time at next scr refresh
                seven_5.setAutoDraw(False)
        
        # *seven_6* updates
        if seven_6.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            seven_6.frameNStart = frameN  # exact frame index
            seven_6.tStart = t  # local t and not account for scr refresh
            seven_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_6, 'tStartRefresh')  # time at next scr refresh
            seven_6.setAutoDraw(True)
        if seven_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_6.tStop = t  # not accounting for scr refresh
                seven_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_6, 'tStopRefresh')  # time at next scr refresh
                seven_6.setAutoDraw(False)
        
        # *seven_7* updates
        if seven_7.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            seven_7.frameNStart = frameN  # exact frame index
            seven_7.tStart = t  # local t and not account for scr refresh
            seven_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_7, 'tStartRefresh')  # time at next scr refresh
            seven_7.setAutoDraw(True)
        if seven_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_7.tStop = t  # not accounting for scr refresh
                seven_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_7, 'tStopRefresh')  # time at next scr refresh
                seven_7.setAutoDraw(False)
        
        # *seven_input* updates
        if seven_input.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
            # keep track of start time/frame for later
            seven_input.frameNStart = frameN  # exact frame index
            seven_input.tStart = t  # local t and not account for scr refresh
            seven_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_input, 'tStartRefresh')  # time at next scr refresh
            seven_input.setAutoDraw(True)
        
        # *seven_tip* updates
        if seven_tip.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
            # keep track of start time/frame for later
            seven_tip.frameNStart = frameN  # exact frame index
            seven_tip.tStart = t  # local t and not account for scr refresh
            seven_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_tip, 'tStartRefresh')  # time at next scr refresh
            seven_tip.setAutoDraw(True)
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
                seven_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('seven', textFill)
                    if textFill == '3864147':
                        thisExp.addData('seven_corr', 1)
                        button += 1
                    else: 
                        thisExp.addData('seven_corr', 0)
                    seven_input.setText(textFill)
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in severnComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "severn"-------
    for thisComponent in severnComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "severn" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "eight"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button == 8:
        textFill = '' 
    else:
        continueRoutine = False
    # keep track of which components have finished
    eightComponents = [eight_concentration, eight_1, eight_2, eight_3, eight_4, eight_5, eight_6, eight_7, eight_8, eight_input, eight_tip]
    for thisComponent in eightComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    eightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "eight"-------
    while continueRoutine:
        # get current time
        t = eightClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=eightClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *eight_concentration* updates
        if eight_concentration.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eight_concentration.frameNStart = frameN  # exact frame index
            eight_concentration.tStart = t  # local t and not account for scr refresh
            eight_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_concentration, 'tStartRefresh')  # time at next scr refresh
            eight_concentration.setAutoDraw(True)
        if eight_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                eight_concentration.tStop = t  # not accounting for scr refresh
                eight_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_concentration, 'tStopRefresh')  # time at next scr refresh
                eight_concentration.setAutoDraw(False)
        
        # *eight_1* updates
        if eight_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            eight_1.frameNStart = frameN  # exact frame index
            eight_1.tStart = t  # local t and not account for scr refresh
            eight_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_1, 'tStartRefresh')  # time at next scr refresh
            eight_1.setAutoDraw(True)
        if eight_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_1.tStop = t  # not accounting for scr refresh
                eight_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_1, 'tStopRefresh')  # time at next scr refresh
                eight_1.setAutoDraw(False)
        
        # *eight_2* updates
        if eight_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            eight_2.frameNStart = frameN  # exact frame index
            eight_2.tStart = t  # local t and not account for scr refresh
            eight_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_2, 'tStartRefresh')  # time at next scr refresh
            eight_2.setAutoDraw(True)
        if eight_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_2.tStop = t  # not accounting for scr refresh
                eight_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_2, 'tStopRefresh')  # time at next scr refresh
                eight_2.setAutoDraw(False)
        
        # *eight_3* updates
        if eight_3.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            eight_3.frameNStart = frameN  # exact frame index
            eight_3.tStart = t  # local t and not account for scr refresh
            eight_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_3, 'tStartRefresh')  # time at next scr refresh
            eight_3.setAutoDraw(True)
        if eight_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_3.tStop = t  # not accounting for scr refresh
                eight_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_3, 'tStopRefresh')  # time at next scr refresh
                eight_3.setAutoDraw(False)
        
        # *eight_4* updates
        if eight_4.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
            # keep track of start time/frame for later
            eight_4.frameNStart = frameN  # exact frame index
            eight_4.tStart = t  # local t and not account for scr refresh
            eight_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_4, 'tStartRefresh')  # time at next scr refresh
            eight_4.setAutoDraw(True)
        if eight_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_4.tStop = t  # not accounting for scr refresh
                eight_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_4, 'tStopRefresh')  # time at next scr refresh
                eight_4.setAutoDraw(False)
        
        # *eight_5* updates
        if eight_5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            eight_5.frameNStart = frameN  # exact frame index
            eight_5.tStart = t  # local t and not account for scr refresh
            eight_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_5, 'tStartRefresh')  # time at next scr refresh
            eight_5.setAutoDraw(True)
        if eight_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_5.tStop = t  # not accounting for scr refresh
                eight_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_5, 'tStopRefresh')  # time at next scr refresh
                eight_5.setAutoDraw(False)
        
        # *eight_6* updates
        if eight_6.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            eight_6.frameNStart = frameN  # exact frame index
            eight_6.tStart = t  # local t and not account for scr refresh
            eight_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_6, 'tStartRefresh')  # time at next scr refresh
            eight_6.setAutoDraw(True)
        if eight_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_6.tStop = t  # not accounting for scr refresh
                eight_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_6, 'tStopRefresh')  # time at next scr refresh
                eight_6.setAutoDraw(False)
        
        # *eight_7* updates
        if eight_7.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            eight_7.frameNStart = frameN  # exact frame index
            eight_7.tStart = t  # local t and not account for scr refresh
            eight_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_7, 'tStartRefresh')  # time at next scr refresh
            eight_7.setAutoDraw(True)
        if eight_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_7.tStop = t  # not accounting for scr refresh
                eight_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_7, 'tStopRefresh')  # time at next scr refresh
                eight_7.setAutoDraw(False)
        
        # *eight_8* updates
        if eight_8.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
            # keep track of start time/frame for later
            eight_8.frameNStart = frameN  # exact frame index
            eight_8.tStart = t  # local t and not account for scr refresh
            eight_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_8, 'tStartRefresh')  # time at next scr refresh
            eight_8.setAutoDraw(True)
        if eight_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_8.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_8.tStop = t  # not accounting for scr refresh
                eight_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_8, 'tStopRefresh')  # time at next scr refresh
                eight_8.setAutoDraw(False)
        
        # *eight_input* updates
        if eight_input.status == NOT_STARTED and tThisFlip >= 2.9-frameTolerance:
            # keep track of start time/frame for later
            eight_input.frameNStart = frameN  # exact frame index
            eight_input.tStart = t  # local t and not account for scr refresh
            eight_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_input, 'tStartRefresh')  # time at next scr refresh
            eight_input.setAutoDraw(True)
        
        # *eight_tip* updates
        if eight_tip.status == NOT_STARTED and tThisFlip >= 2.9-frameTolerance:
            # keep track of start time/frame for later
            eight_tip.frameNStart = frameN  # exact frame index
            eight_tip.tStart = t  # local t and not account for scr refresh
            eight_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_tip, 'tStartRefresh')  # time at next scr refresh
            eight_tip.setAutoDraw(True)
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
                eight_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('eight', textFill)
                    if textFill == '43789786':
                        thisExp.addData('eight_corr', 1)
                        button += 1
                    else: 
                        thisExp.addData('eight_corr', 0)
                    eight_input.setText(textFill)
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eightComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "eight"-------
    for thisComponent in eightComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "eight" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "nine"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button == 9:
        textFill = '' 
    else:
        continueRoutine = False
    # keep track of which components have finished
    nineComponents = [nine_concentration, nine_1, nine_2, nine_3, nine_4, nine_5, nine_6, nine_7, nine_8, nine_9, nine_input, nine_tip]
    for thisComponent in nineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    nineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "nine"-------
    while continueRoutine:
        # get current time
        t = nineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=nineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *nine_concentration* updates
        if nine_concentration.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nine_concentration.frameNStart = frameN  # exact frame index
            nine_concentration.tStart = t  # local t and not account for scr refresh
            nine_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_concentration, 'tStartRefresh')  # time at next scr refresh
            nine_concentration.setAutoDraw(True)
        if nine_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                nine_concentration.tStop = t  # not accounting for scr refresh
                nine_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_concentration, 'tStopRefresh')  # time at next scr refresh
                nine_concentration.setAutoDraw(False)
        
        # *nine_1* updates
        if nine_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            nine_1.frameNStart = frameN  # exact frame index
            nine_1.tStart = t  # local t and not account for scr refresh
            nine_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_1, 'tStartRefresh')  # time at next scr refresh
            nine_1.setAutoDraw(True)
        if nine_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_1.tStop = t  # not accounting for scr refresh
                nine_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_1, 'tStopRefresh')  # time at next scr refresh
                nine_1.setAutoDraw(False)
        
        # *nine_2* updates
        if nine_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            nine_2.frameNStart = frameN  # exact frame index
            nine_2.tStart = t  # local t and not account for scr refresh
            nine_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_2, 'tStartRefresh')  # time at next scr refresh
            nine_2.setAutoDraw(True)
        if nine_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_2.tStop = t  # not accounting for scr refresh
                nine_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_2, 'tStopRefresh')  # time at next scr refresh
                nine_2.setAutoDraw(False)
        
        # *nine_3* updates
        if nine_3.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            nine_3.frameNStart = frameN  # exact frame index
            nine_3.tStart = t  # local t and not account for scr refresh
            nine_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_3, 'tStartRefresh')  # time at next scr refresh
            nine_3.setAutoDraw(True)
        if nine_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_3.tStop = t  # not accounting for scr refresh
                nine_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_3, 'tStopRefresh')  # time at next scr refresh
                nine_3.setAutoDraw(False)
        
        # *nine_4* updates
        if nine_4.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
            # keep track of start time/frame for later
            nine_4.frameNStart = frameN  # exact frame index
            nine_4.tStart = t  # local t and not account for scr refresh
            nine_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_4, 'tStartRefresh')  # time at next scr refresh
            nine_4.setAutoDraw(True)
        if nine_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_4.tStop = t  # not accounting for scr refresh
                nine_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_4, 'tStopRefresh')  # time at next scr refresh
                nine_4.setAutoDraw(False)
        
        # *nine_5* updates
        if nine_5.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            nine_5.frameNStart = frameN  # exact frame index
            nine_5.tStart = t  # local t and not account for scr refresh
            nine_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_5, 'tStartRefresh')  # time at next scr refresh
            nine_5.setAutoDraw(True)
        if nine_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_5.tStop = t  # not accounting for scr refresh
                nine_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_5, 'tStopRefresh')  # time at next scr refresh
                nine_5.setAutoDraw(False)
        
        # *nine_6* updates
        if nine_6.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            nine_6.frameNStart = frameN  # exact frame index
            nine_6.tStart = t  # local t and not account for scr refresh
            nine_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_6, 'tStartRefresh')  # time at next scr refresh
            nine_6.setAutoDraw(True)
        if nine_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_6.tStop = t  # not accounting for scr refresh
                nine_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_6, 'tStopRefresh')  # time at next scr refresh
                nine_6.setAutoDraw(False)
        
        # *nine_7* updates
        if nine_7.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
            # keep track of start time/frame for later
            nine_7.frameNStart = frameN  # exact frame index
            nine_7.tStart = t  # local t and not account for scr refresh
            nine_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_7, 'tStartRefresh')  # time at next scr refresh
            nine_7.setAutoDraw(True)
        if nine_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_7.tStop = t  # not accounting for scr refresh
                nine_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_7, 'tStopRefresh')  # time at next scr refresh
                nine_7.setAutoDraw(False)
        
        # *nine_8* updates
        if nine_8.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
            # keep track of start time/frame for later
            nine_8.frameNStart = frameN  # exact frame index
            nine_8.tStart = t  # local t and not account for scr refresh
            nine_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_8, 'tStartRefresh')  # time at next scr refresh
            nine_8.setAutoDraw(True)
        if nine_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_8.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_8.tStop = t  # not accounting for scr refresh
                nine_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_8, 'tStopRefresh')  # time at next scr refresh
                nine_8.setAutoDraw(False)
        
        # *nine_9* updates
        if nine_9.status == NOT_STARTED and tThisFlip >= 2.9-frameTolerance:
            # keep track of start time/frame for later
            nine_9.frameNStart = frameN  # exact frame index
            nine_9.tStart = t  # local t and not account for scr refresh
            nine_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_9, 'tStartRefresh')  # time at next scr refresh
            nine_9.setAutoDraw(True)
        if nine_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_9.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_9.tStop = t  # not accounting for scr refresh
                nine_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_9, 'tStopRefresh')  # time at next scr refresh
                nine_9.setAutoDraw(False)
        
        # *nine_input* updates
        if nine_input.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
            # keep track of start time/frame for later
            nine_input.frameNStart = frameN  # exact frame index
            nine_input.tStart = t  # local t and not account for scr refresh
            nine_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_input, 'tStartRefresh')  # time at next scr refresh
            nine_input.setAutoDraw(True)
        
        # *nine_tip* updates
        if nine_tip.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
            # keep track of start time/frame for later
            nine_tip.frameNStart = frameN  # exact frame index
            nine_tip.tStart = t  # local t and not account for scr refresh
            nine_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_tip, 'tStartRefresh')  # time at next scr refresh
            nine_tip.setAutoDraw(True)
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
                nine_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('nine', textFill)
                    if textFill == '443521729':
                        thisExp.addData('nine_corr', 1)
                        loop_or.finished = True
                    else: 
                        thisExp.addData('nine_corr', 0)
                    nine_input.setText(textFill)
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nine"-------
    for thisComponent in nineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "nine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 7.0 repeats of 'loop_or'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
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
        if tThisFlipGlobal > thank.tStartRefresh + 2-frameTolerance:
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
