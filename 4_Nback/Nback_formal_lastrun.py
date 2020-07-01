#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 六月 14, 2020, at 14:49
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
expName = 'Nback_formal'  # from the Builder filename that created this script
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
    originPath='D:\\jianguoyun\\课题组\\4_Nback\\Nback_formal_lastrun.py',
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
introduction0_1 = visual.TextStim(win=win, name='introduction0_1',
    text='欢迎参加测试\n\n本测试分三种类型\n现在是正式测试\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "introduction2"
introduction2Clock = core.Clock()
introduction_2 = visual.TextStim(win=win, name='introduction_2',
    text='第一种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会连续出现一系列的数字\n\n在每个数字出现时\n您只需要按下空格键即可\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "introduction3"
introduction3Clock = core.Clock()
introduction_3 = visual.TextStim(win=win, name='introduction_3',
    text='第二种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会连续出现一系列的数字\n\n从第二个数字出现时\n您需要判断该数字与上一个数字是否一致\n一致,请按左键; 不一致,请按右键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "introduction4"
introduction4Clock = core.Clock()
introduction_4 = visual.TextStim(win=win, name='introduction_4',
    text='第三种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会连续出现一系列的数字\n\n从第三个数字出现时\n您需要判断该数字与倒数第二个数字是否一致\n一致,请按左键; 不一致,请按右键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "introduction5"
introduction5Clock = core.Clock()
introduction_5 = visual.TextStim(win=win, name='introduction_5',
    text='如果准备好了，开始正式测试\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "tip1"
tip1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='现在，测试第一种类型\n\n \n（继续，请按空格键）\n\n',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "introduction2"
introduction2Clock = core.Clock()
introduction_2 = visual.TextStim(win=win, name='introduction_2',
    text='第一种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会连续出现一系列的数字\n\n在每个数字出现时\n您只需要按下空格键即可\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "_0back_pre"
_0back_preClock = core.Clock()
concentration1 = visual.TextStim(win=win, name='concentration1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "_0back"
_0backClock = core.Clock()
_0back_1 = visual.TextStim(win=win, name='_0back_1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_0back = keyboard.Keyboard()

# Initialize components for Routine "tip2"
tip2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='现在，测试第二种类型\n\n（继续请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "introduction3"
introduction3Clock = core.Clock()
introduction_3 = visual.TextStim(win=win, name='introduction_3',
    text='第二种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会连续出现一系列的数字\n\n从第二个数字出现时\n您需要判断该数字与上一个数字是否一致\n一致,请按左键; 不一致,请按右键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "_1back_pre"
_1back_preClock = core.Clock()
concentration2 = visual.TextStim(win=win, name='concentration2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
back1_pre = visual.TextStim(win=win, name='back1_pre',
    text='2\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "_1back"
_1backClock = core.Clock()
back1_1 = visual.TextStim(win=win, name='back1_1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_1back = keyboard.Keyboard()

# Initialize components for Routine "tip3"
tip3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='现在，测试第三种类型\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "introduction4"
introduction4Clock = core.Clock()
introduction_4 = visual.TextStim(win=win, name='introduction_4',
    text='第三种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会连续出现一系列的数字\n\n从第三个数字出现时\n您需要判断该数字与倒数第二个数字是否一致\n一致,请按左键; 不一致,请按右键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "_2back_pre"
_2back_preClock = core.Clock()
concentration3 = visual.TextStim(win=win, name='concentration3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
back2_1 = visual.TextStim(win=win, name='back2_1',
    text='1\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
back2_2 = visual.TextStim(win=win, name='back2_2',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "_2back"
_2backClock = core.Clock()
back2_3 = visual.TextStim(win=win, name='back2_3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2back = keyboard.Keyboard()

# Initialize components for Routine "tip2"
tip2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='现在，测试第二种类型\n\n（继续请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "introduction3"
introduction3Clock = core.Clock()
introduction_3 = visual.TextStim(win=win, name='introduction_3',
    text='第二种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会连续出现一系列的数字\n\n从第二个数字出现时\n您需要判断该数字与上一个数字是否一致\n一致,请按左键; 不一致,请按右键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "_1back_pre"
_1back_preClock = core.Clock()
concentration2 = visual.TextStim(win=win, name='concentration2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
back1_pre = visual.TextStim(win=win, name='back1_pre',
    text='2\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "_1back"
_1backClock = core.Clock()
back1_1 = visual.TextStim(win=win, name='back1_1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_1back = keyboard.Keyboard()

# Initialize components for Routine "tip3"
tip3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='现在，测试第三种类型\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "introduction4"
introduction4Clock = core.Clock()
introduction_4 = visual.TextStim(win=win, name='introduction_4',
    text='第三种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会连续出现一系列的数字\n\n从第三个数字出现时\n您需要判断该数字与倒数第二个数字是否一致\n一致,请按左键; 不一致,请按右键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "_2back_pre"
_2back_preClock = core.Clock()
concentration3 = visual.TextStim(win=win, name='concentration3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
back2_1 = visual.TextStim(win=win, name='back2_1',
    text='1\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
back2_2 = visual.TextStim(win=win, name='back2_2',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "_2back"
_2backClock = core.Clock()
back2_3 = visual.TextStim(win=win, name='back2_3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2back = keyboard.Keyboard()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='测试结束，谢谢您的参与',
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
introduction1Components = [introduction0_1, key_resp]
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
    
    # *introduction0_1* updates
    if introduction0_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction0_1.frameNStart = frameN  # exact frame index
        introduction0_1.tStart = t  # local t and not account for scr refresh
        introduction0_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction0_1, 'tStartRefresh')  # time at next scr refresh
        introduction0_1.setAutoDraw(True)
    
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
thisExp.addData('introduction0_1.started', introduction0_1.tStartRefresh)
thisExp.addData('introduction0_1.stopped', introduction0_1.tStopRefresh)
# the Routine "introduction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
introduction2Components = [introduction_2, key_resp_2]
for thisComponent in introduction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction2"-------
while continueRoutine:
    # get current time
    t = introduction2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction_2* updates
    if introduction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_2.frameNStart = frameN  # exact frame index
        introduction_2.tStart = t  # local t and not account for scr refresh
        introduction_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_2, 'tStartRefresh')  # time at next scr refresh
        introduction_2.setAutoDraw(True)
    
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
    for thisComponent in introduction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction2"-------
for thisComponent in introduction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction_2.started', introduction_2.tStartRefresh)
thisExp.addData('introduction_2.stopped', introduction_2.tStopRefresh)
# the Routine "introduction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
introduction3Components = [introduction_3, key_resp_3]
for thisComponent in introduction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction3"-------
while continueRoutine:
    # get current time
    t = introduction3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction_3* updates
    if introduction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_3.frameNStart = frameN  # exact frame index
        introduction_3.tStart = t  # local t and not account for scr refresh
        introduction_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_3, 'tStartRefresh')  # time at next scr refresh
        introduction_3.setAutoDraw(True)
    
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
    for thisComponent in introduction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction3"-------
for thisComponent in introduction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction_3.started', introduction_3.tStartRefresh)
thisExp.addData('introduction_3.stopped', introduction_3.tStopRefresh)
# the Routine "introduction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
introduction4Components = [introduction_4, key_resp_4]
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
    
    # *introduction_4* updates
    if introduction_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_4.frameNStart = frameN  # exact frame index
        introduction_4.tStart = t  # local t and not account for scr refresh
        introduction_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_4, 'tStartRefresh')  # time at next scr refresh
        introduction_4.setAutoDraw(True)
    
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
thisExp.addData('introduction_4.started', introduction_4.tStartRefresh)
thisExp.addData('introduction_4.stopped', introduction_4.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "introduction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
introduction5Components = [introduction_5, key_resp_5]
for thisComponent in introduction5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction5"-------
while continueRoutine:
    # get current time
    t = introduction5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction_5* updates
    if introduction_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_5.frameNStart = frameN  # exact frame index
        introduction_5.tStart = t  # local t and not account for scr refresh
        introduction_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_5, 'tStartRefresh')  # time at next scr refresh
        introduction_5.setAutoDraw(True)
    
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
    for thisComponent in introduction5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction5"-------
for thisComponent in introduction5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction_5.started', introduction_5.tStartRefresh)
thisExp.addData('introduction_5.stopped', introduction_5.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "introduction5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "tip1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
tip1Components = [text, key_resp_6]
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
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
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

# ------Prepare to start Routine "introduction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
introduction2Components = [introduction_2, key_resp_2]
for thisComponent in introduction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction2"-------
while continueRoutine:
    # get current time
    t = introduction2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction_2* updates
    if introduction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_2.frameNStart = frameN  # exact frame index
        introduction_2.tStart = t  # local t and not account for scr refresh
        introduction_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_2, 'tStartRefresh')  # time at next scr refresh
        introduction_2.setAutoDraw(True)
    
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
    for thisComponent in introduction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction2"-------
for thisComponent in introduction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction_2.started', introduction_2.tStartRefresh)
thisExp.addData('introduction_2.stopped', introduction_2.tStopRefresh)
# the Routine "introduction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "_0back_pre"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
_0back_preComponents = [concentration1]
for thisComponent in _0back_preComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
_0back_preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "_0back_pre"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = _0back_preClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=_0back_preClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *concentration1* updates
    if concentration1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        concentration1.frameNStart = frameN  # exact frame index
        concentration1.tStart = t  # local t and not account for scr refresh
        concentration1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(concentration1, 'tStartRefresh')  # time at next scr refresh
        concentration1.setAutoDraw(True)
    if concentration1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > concentration1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            concentration1.tStop = t  # not accounting for scr refresh
            concentration1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(concentration1, 'tStopRefresh')  # time at next scr refresh
            concentration1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in _0back_preComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "_0back_pre"-------
for thisComponent in _0back_preComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('concentration1.started', concentration1.tStartRefresh)
thisExp.addData('concentration1.stopped', concentration1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop_0back = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\document_0back.xlsx'),
    seed=None, name='loop_0back')
thisExp.addLoop(loop_0back)  # add the loop to the experiment
thisLoop_0back = loop_0back.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_0back.rgb)
if thisLoop_0back != None:
    for paramName in thisLoop_0back:
        exec('{} = thisLoop_0back[paramName]'.format(paramName))

for thisLoop_0back in loop_0back:
    currentLoop = loop_0back
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_0back.rgb)
    if thisLoop_0back != None:
        for paramName in thisLoop_0back:
            exec('{} = thisLoop_0back[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "_0back"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    _0back_1.setText(num1)
    key_resp_0back.keys = []
    key_resp_0back.rt = []
    _key_resp_0back_allKeys = []
    # keep track of which components have finished
    _0backComponents = [_0back_1, key_resp_0back]
    for thisComponent in _0backComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    _0backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "_0back"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = _0backClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=_0backClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *_0back_1* updates
        if _0back_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            _0back_1.frameNStart = frameN  # exact frame index
            _0back_1.tStart = t  # local t and not account for scr refresh
            _0back_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(_0back_1, 'tStartRefresh')  # time at next scr refresh
            _0back_1.setAutoDraw(True)
        if _0back_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > _0back_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                _0back_1.tStop = t  # not accounting for scr refresh
                _0back_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(_0back_1, 'tStopRefresh')  # time at next scr refresh
                _0back_1.setAutoDraw(False)
        
        # *key_resp_0back* updates
        waitOnFlip = False
        if key_resp_0back.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_0back.frameNStart = frameN  # exact frame index
            key_resp_0back.tStart = t  # local t and not account for scr refresh
            key_resp_0back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_0back, 'tStartRefresh')  # time at next scr refresh
            key_resp_0back.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_0back.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_0back.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_0back.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_0back.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_0back.tStop = t  # not accounting for scr refresh
                key_resp_0back.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_0back, 'tStopRefresh')  # time at next scr refresh
                key_resp_0back.status = FINISHED
        if key_resp_0back.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_0back.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_0back_allKeys.extend(theseKeys)
            if len(_key_resp_0back_allKeys):
                key_resp_0back.keys = _key_resp_0back_allKeys[-1].name  # just the last key pressed
                key_resp_0back.rt = _key_resp_0back_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in _0backComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "_0back"-------
    for thisComponent in _0backComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_0back.addData('_0back_1.started', _0back_1.tStartRefresh)
    loop_0back.addData('_0back_1.stopped', _0back_1.tStopRefresh)
    # check responses
    if key_resp_0back.keys in ['', [], None]:  # No response was made
        key_resp_0back.keys = None
    loop_0back.addData('key_resp_0back.keys',key_resp_0back.keys)
    if key_resp_0back.keys != None:  # we had a response
        loop_0back.addData('key_resp_0back.rt', key_resp_0back.rt)
    loop_0back.addData('key_resp_0back.started', key_resp_0back.tStartRefresh)
    loop_0back.addData('key_resp_0back.stopped', key_resp_0back.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop_0back'


# ------Prepare to start Routine "tip2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
tip2Components = [text_2, key_resp_7]
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
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
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
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "tip2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
introduction3Components = [introduction_3, key_resp_3]
for thisComponent in introduction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction3"-------
while continueRoutine:
    # get current time
    t = introduction3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction_3* updates
    if introduction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_3.frameNStart = frameN  # exact frame index
        introduction_3.tStart = t  # local t and not account for scr refresh
        introduction_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_3, 'tStartRefresh')  # time at next scr refresh
        introduction_3.setAutoDraw(True)
    
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
    for thisComponent in introduction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction3"-------
for thisComponent in introduction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction_3.started', introduction_3.tStartRefresh)
thisExp.addData('introduction_3.stopped', introduction_3.tStopRefresh)
# the Routine "introduction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "_1back_pre"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
_1back_preComponents = [concentration2, back1_pre]
for thisComponent in _1back_preComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
_1back_preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "_1back_pre"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = _1back_preClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=_1back_preClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *concentration2* updates
    if concentration2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        concentration2.frameNStart = frameN  # exact frame index
        concentration2.tStart = t  # local t and not account for scr refresh
        concentration2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(concentration2, 'tStartRefresh')  # time at next scr refresh
        concentration2.setAutoDraw(True)
    if concentration2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > concentration2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            concentration2.tStop = t  # not accounting for scr refresh
            concentration2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(concentration2, 'tStopRefresh')  # time at next scr refresh
            concentration2.setAutoDraw(False)
    
    # *back1_pre* updates
    if back1_pre.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        back1_pre.frameNStart = frameN  # exact frame index
        back1_pre.tStart = t  # local t and not account for scr refresh
        back1_pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back1_pre, 'tStartRefresh')  # time at next scr refresh
        back1_pre.setAutoDraw(True)
    if back1_pre.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > back1_pre.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            back1_pre.tStop = t  # not accounting for scr refresh
            back1_pre.frameNStop = frameN  # exact frame index
            win.timeOnFlip(back1_pre, 'tStopRefresh')  # time at next scr refresh
            back1_pre.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in _1back_preComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "_1back_pre"-------
for thisComponent in _1back_preComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('concentration2.started', concentration2.tStartRefresh)
thisExp.addData('concentration2.stopped', concentration2.tStopRefresh)
thisExp.addData('back1_pre.started', back1_pre.tStartRefresh)
thisExp.addData('back1_pre.stopped', back1_pre.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop_1back_1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\document_1back.xlsx'),
    seed=None, name='loop_1back_1')
thisExp.addLoop(loop_1back_1)  # add the loop to the experiment
thisLoop_1back_1 = loop_1back_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_1back_1.rgb)
if thisLoop_1back_1 != None:
    for paramName in thisLoop_1back_1:
        exec('{} = thisLoop_1back_1[paramName]'.format(paramName))

for thisLoop_1back_1 in loop_1back_1:
    currentLoop = loop_1back_1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_1back_1.rgb)
    if thisLoop_1back_1 != None:
        for paramName in thisLoop_1back_1:
            exec('{} = thisLoop_1back_1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "_1back"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    back1_1.setText(num2)
    key_resp_1back.keys = []
    key_resp_1back.rt = []
    _key_resp_1back_allKeys = []
    # keep track of which components have finished
    _1backComponents = [back1_1, key_resp_1back]
    for thisComponent in _1backComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    _1backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "_1back"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = _1backClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=_1backClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back1_1* updates
        if back1_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            back1_1.frameNStart = frameN  # exact frame index
            back1_1.tStart = t  # local t and not account for scr refresh
            back1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back1_1, 'tStartRefresh')  # time at next scr refresh
            back1_1.setAutoDraw(True)
        if back1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back1_1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                back1_1.tStop = t  # not accounting for scr refresh
                back1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back1_1, 'tStopRefresh')  # time at next scr refresh
                back1_1.setAutoDraw(False)
        
        # *key_resp_1back* updates
        waitOnFlip = False
        if key_resp_1back.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_1back.frameNStart = frameN  # exact frame index
            key_resp_1back.tStart = t  # local t and not account for scr refresh
            key_resp_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1back, 'tStartRefresh')  # time at next scr refresh
            key_resp_1back.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1back.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1back.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_1back.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_1back.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_1back.tStop = t  # not accounting for scr refresh
                key_resp_1back.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_1back, 'tStopRefresh')  # time at next scr refresh
                key_resp_1back.status = FINISHED
        if key_resp_1back.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1back.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_1back_allKeys.extend(theseKeys)
            if len(_key_resp_1back_allKeys):
                key_resp_1back.keys = _key_resp_1back_allKeys[-1].name  # just the last key pressed
                key_resp_1back.rt = _key_resp_1back_allKeys[-1].rt
                # was this correct?
                if (key_resp_1back.keys == str(num2_corr)) or (key_resp_1back.keys == num2_corr):
                    key_resp_1back.corr = 1
                else:
                    key_resp_1back.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in _1backComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "_1back"-------
    for thisComponent in _1backComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_1back_1.addData('back1_1.started', back1_1.tStartRefresh)
    loop_1back_1.addData('back1_1.stopped', back1_1.tStopRefresh)
    # check responses
    if key_resp_1back.keys in ['', [], None]:  # No response was made
        key_resp_1back.keys = None
        # was no response the correct answer?!
        if str(num2_corr).lower() == 'none':
           key_resp_1back.corr = 1;  # correct non-response
        else:
           key_resp_1back.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_1back_1 (TrialHandler)
    loop_1back_1.addData('key_resp_1back.keys',key_resp_1back.keys)
    loop_1back_1.addData('key_resp_1back.corr', key_resp_1back.corr)
    if key_resp_1back.keys != None:  # we had a response
        loop_1back_1.addData('key_resp_1back.rt', key_resp_1back.rt)
    loop_1back_1.addData('key_resp_1back.started', key_resp_1back.tStartRefresh)
    loop_1back_1.addData('key_resp_1back.stopped', key_resp_1back.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_1back_1'


# ------Prepare to start Routine "tip3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
tip3Components = [text_3, key_resp_9]
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
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
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
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "tip3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
introduction4Components = [introduction_4, key_resp_4]
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
    
    # *introduction_4* updates
    if introduction_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_4.frameNStart = frameN  # exact frame index
        introduction_4.tStart = t  # local t and not account for scr refresh
        introduction_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_4, 'tStartRefresh')  # time at next scr refresh
        introduction_4.setAutoDraw(True)
    
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
thisExp.addData('introduction_4.started', introduction_4.tStartRefresh)
thisExp.addData('introduction_4.stopped', introduction_4.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "introduction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "_2back_pre"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
_2back_preComponents = [concentration3, back2_1, back2_2]
for thisComponent in _2back_preComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
_2back_preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "_2back_pre"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = _2back_preClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=_2back_preClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *concentration3* updates
    if concentration3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        concentration3.frameNStart = frameN  # exact frame index
        concentration3.tStart = t  # local t and not account for scr refresh
        concentration3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(concentration3, 'tStartRefresh')  # time at next scr refresh
        concentration3.setAutoDraw(True)
    if concentration3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > concentration3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            concentration3.tStop = t  # not accounting for scr refresh
            concentration3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(concentration3, 'tStopRefresh')  # time at next scr refresh
            concentration3.setAutoDraw(False)
    
    # *back2_1* updates
    if back2_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        back2_1.frameNStart = frameN  # exact frame index
        back2_1.tStart = t  # local t and not account for scr refresh
        back2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back2_1, 'tStartRefresh')  # time at next scr refresh
        back2_1.setAutoDraw(True)
    if back2_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > back2_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            back2_1.tStop = t  # not accounting for scr refresh
            back2_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(back2_1, 'tStopRefresh')  # time at next scr refresh
            back2_1.setAutoDraw(False)
    
    # *back2_2* updates
    if back2_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        back2_2.frameNStart = frameN  # exact frame index
        back2_2.tStart = t  # local t and not account for scr refresh
        back2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back2_2, 'tStartRefresh')  # time at next scr refresh
        back2_2.setAutoDraw(True)
    if back2_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > back2_2.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            back2_2.tStop = t  # not accounting for scr refresh
            back2_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(back2_2, 'tStopRefresh')  # time at next scr refresh
            back2_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in _2back_preComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "_2back_pre"-------
for thisComponent in _2back_preComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('concentration3.started', concentration3.tStartRefresh)
thisExp.addData('concentration3.stopped', concentration3.tStopRefresh)
thisExp.addData('back2_1.started', back2_1.tStartRefresh)
thisExp.addData('back2_1.stopped', back2_1.tStopRefresh)
thisExp.addData('back2_2.started', back2_2.tStartRefresh)
thisExp.addData('back2_2.stopped', back2_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop_2back_1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\document_2back.xlsx'),
    seed=None, name='loop_2back_1')
thisExp.addLoop(loop_2back_1)  # add the loop to the experiment
thisLoop_2back_1 = loop_2back_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_2back_1.rgb)
if thisLoop_2back_1 != None:
    for paramName in thisLoop_2back_1:
        exec('{} = thisLoop_2back_1[paramName]'.format(paramName))

for thisLoop_2back_1 in loop_2back_1:
    currentLoop = loop_2back_1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_2back_1.rgb)
    if thisLoop_2back_1 != None:
        for paramName in thisLoop_2back_1:
            exec('{} = thisLoop_2back_1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "_2back"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    back2_3.setText(num3)
    key_resp_2back.keys = []
    key_resp_2back.rt = []
    _key_resp_2back_allKeys = []
    # keep track of which components have finished
    _2backComponents = [back2_3, key_resp_2back]
    for thisComponent in _2backComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    _2backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "_2back"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = _2backClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=_2backClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back2_3* updates
        if back2_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            back2_3.frameNStart = frameN  # exact frame index
            back2_3.tStart = t  # local t and not account for scr refresh
            back2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back2_3, 'tStartRefresh')  # time at next scr refresh
            back2_3.setAutoDraw(True)
        if back2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back2_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                back2_3.tStop = t  # not accounting for scr refresh
                back2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back2_3, 'tStopRefresh')  # time at next scr refresh
                back2_3.setAutoDraw(False)
        
        # *key_resp_2back* updates
        waitOnFlip = False
        if key_resp_2back.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2back.frameNStart = frameN  # exact frame index
            key_resp_2back.tStart = t  # local t and not account for scr refresh
            key_resp_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2back, 'tStartRefresh')  # time at next scr refresh
            key_resp_2back.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2back.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2back.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2back.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2back.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2back.tStop = t  # not accounting for scr refresh
                key_resp_2back.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2back, 'tStopRefresh')  # time at next scr refresh
                key_resp_2back.status = FINISHED
        if key_resp_2back.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2back.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_2back_allKeys.extend(theseKeys)
            if len(_key_resp_2back_allKeys):
                key_resp_2back.keys = _key_resp_2back_allKeys[-1].name  # just the last key pressed
                key_resp_2back.rt = _key_resp_2back_allKeys[-1].rt
                # was this correct?
                if (key_resp_2back.keys == str(num3_corr)) or (key_resp_2back.keys == num3_corr):
                    key_resp_2back.corr = 1
                else:
                    key_resp_2back.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in _2backComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "_2back"-------
    for thisComponent in _2backComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_2back_1.addData('back2_3.started', back2_3.tStartRefresh)
    loop_2back_1.addData('back2_3.stopped', back2_3.tStopRefresh)
    # check responses
    if key_resp_2back.keys in ['', [], None]:  # No response was made
        key_resp_2back.keys = None
        # was no response the correct answer?!
        if str(num3_corr).lower() == 'none':
           key_resp_2back.corr = 1;  # correct non-response
        else:
           key_resp_2back.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_2back_1 (TrialHandler)
    loop_2back_1.addData('key_resp_2back.keys',key_resp_2back.keys)
    loop_2back_1.addData('key_resp_2back.corr', key_resp_2back.corr)
    if key_resp_2back.keys != None:  # we had a response
        loop_2back_1.addData('key_resp_2back.rt', key_resp_2back.rt)
    loop_2back_1.addData('key_resp_2back.started', key_resp_2back.tStartRefresh)
    loop_2back_1.addData('key_resp_2back.stopped', key_resp_2back.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_2back_1'


# ------Prepare to start Routine "tip2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
tip2Components = [text_2, key_resp_7]
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
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
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
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "tip2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
introduction3Components = [introduction_3, key_resp_3]
for thisComponent in introduction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction3"-------
while continueRoutine:
    # get current time
    t = introduction3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction_3* updates
    if introduction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_3.frameNStart = frameN  # exact frame index
        introduction_3.tStart = t  # local t and not account for scr refresh
        introduction_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_3, 'tStartRefresh')  # time at next scr refresh
        introduction_3.setAutoDraw(True)
    
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
    for thisComponent in introduction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction3"-------
for thisComponent in introduction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction_3.started', introduction_3.tStartRefresh)
thisExp.addData('introduction_3.stopped', introduction_3.tStopRefresh)
# the Routine "introduction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "_1back_pre"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
_1back_preComponents = [concentration2, back1_pre]
for thisComponent in _1back_preComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
_1back_preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "_1back_pre"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = _1back_preClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=_1back_preClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *concentration2* updates
    if concentration2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        concentration2.frameNStart = frameN  # exact frame index
        concentration2.tStart = t  # local t and not account for scr refresh
        concentration2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(concentration2, 'tStartRefresh')  # time at next scr refresh
        concentration2.setAutoDraw(True)
    if concentration2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > concentration2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            concentration2.tStop = t  # not accounting for scr refresh
            concentration2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(concentration2, 'tStopRefresh')  # time at next scr refresh
            concentration2.setAutoDraw(False)
    
    # *back1_pre* updates
    if back1_pre.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        back1_pre.frameNStart = frameN  # exact frame index
        back1_pre.tStart = t  # local t and not account for scr refresh
        back1_pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back1_pre, 'tStartRefresh')  # time at next scr refresh
        back1_pre.setAutoDraw(True)
    if back1_pre.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > back1_pre.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            back1_pre.tStop = t  # not accounting for scr refresh
            back1_pre.frameNStop = frameN  # exact frame index
            win.timeOnFlip(back1_pre, 'tStopRefresh')  # time at next scr refresh
            back1_pre.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in _1back_preComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "_1back_pre"-------
for thisComponent in _1back_preComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('concentration2.started', concentration2.tStartRefresh)
thisExp.addData('concentration2.stopped', concentration2.tStopRefresh)
thisExp.addData('back1_pre.started', back1_pre.tStartRefresh)
thisExp.addData('back1_pre.stopped', back1_pre.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop_1back_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\document_1back.xlsx'),
    seed=None, name='loop_1back_2')
thisExp.addLoop(loop_1back_2)  # add the loop to the experiment
thisLoop_1back_2 = loop_1back_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_1back_2.rgb)
if thisLoop_1back_2 != None:
    for paramName in thisLoop_1back_2:
        exec('{} = thisLoop_1back_2[paramName]'.format(paramName))

for thisLoop_1back_2 in loop_1back_2:
    currentLoop = loop_1back_2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_1back_2.rgb)
    if thisLoop_1back_2 != None:
        for paramName in thisLoop_1back_2:
            exec('{} = thisLoop_1back_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "_1back"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    back1_1.setText(num2)
    key_resp_1back.keys = []
    key_resp_1back.rt = []
    _key_resp_1back_allKeys = []
    # keep track of which components have finished
    _1backComponents = [back1_1, key_resp_1back]
    for thisComponent in _1backComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    _1backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "_1back"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = _1backClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=_1backClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back1_1* updates
        if back1_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            back1_1.frameNStart = frameN  # exact frame index
            back1_1.tStart = t  # local t and not account for scr refresh
            back1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back1_1, 'tStartRefresh')  # time at next scr refresh
            back1_1.setAutoDraw(True)
        if back1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back1_1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                back1_1.tStop = t  # not accounting for scr refresh
                back1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back1_1, 'tStopRefresh')  # time at next scr refresh
                back1_1.setAutoDraw(False)
        
        # *key_resp_1back* updates
        waitOnFlip = False
        if key_resp_1back.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_1back.frameNStart = frameN  # exact frame index
            key_resp_1back.tStart = t  # local t and not account for scr refresh
            key_resp_1back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1back, 'tStartRefresh')  # time at next scr refresh
            key_resp_1back.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1back.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1back.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_1back.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_1back.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_1back.tStop = t  # not accounting for scr refresh
                key_resp_1back.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_1back, 'tStopRefresh')  # time at next scr refresh
                key_resp_1back.status = FINISHED
        if key_resp_1back.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1back.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_1back_allKeys.extend(theseKeys)
            if len(_key_resp_1back_allKeys):
                key_resp_1back.keys = _key_resp_1back_allKeys[-1].name  # just the last key pressed
                key_resp_1back.rt = _key_resp_1back_allKeys[-1].rt
                # was this correct?
                if (key_resp_1back.keys == str(num2_corr)) or (key_resp_1back.keys == num2_corr):
                    key_resp_1back.corr = 1
                else:
                    key_resp_1back.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in _1backComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "_1back"-------
    for thisComponent in _1backComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_1back_2.addData('back1_1.started', back1_1.tStartRefresh)
    loop_1back_2.addData('back1_1.stopped', back1_1.tStopRefresh)
    # check responses
    if key_resp_1back.keys in ['', [], None]:  # No response was made
        key_resp_1back.keys = None
        # was no response the correct answer?!
        if str(num2_corr).lower() == 'none':
           key_resp_1back.corr = 1;  # correct non-response
        else:
           key_resp_1back.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_1back_2 (TrialHandler)
    loop_1back_2.addData('key_resp_1back.keys',key_resp_1back.keys)
    loop_1back_2.addData('key_resp_1back.corr', key_resp_1back.corr)
    if key_resp_1back.keys != None:  # we had a response
        loop_1back_2.addData('key_resp_1back.rt', key_resp_1back.rt)
    loop_1back_2.addData('key_resp_1back.started', key_resp_1back.tStartRefresh)
    loop_1back_2.addData('key_resp_1back.stopped', key_resp_1back.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_1back_2'


# ------Prepare to start Routine "tip3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
tip3Components = [text_3, key_resp_9]
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
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
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
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "tip3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
introduction4Components = [introduction_4, key_resp_4]
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
    
    # *introduction_4* updates
    if introduction_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_4.frameNStart = frameN  # exact frame index
        introduction_4.tStart = t  # local t and not account for scr refresh
        introduction_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_4, 'tStartRefresh')  # time at next scr refresh
        introduction_4.setAutoDraw(True)
    
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
thisExp.addData('introduction_4.started', introduction_4.tStartRefresh)
thisExp.addData('introduction_4.stopped', introduction_4.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "introduction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "_2back_pre"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
_2back_preComponents = [concentration3, back2_1, back2_2]
for thisComponent in _2back_preComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
_2back_preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "_2back_pre"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = _2back_preClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=_2back_preClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *concentration3* updates
    if concentration3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        concentration3.frameNStart = frameN  # exact frame index
        concentration3.tStart = t  # local t and not account for scr refresh
        concentration3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(concentration3, 'tStartRefresh')  # time at next scr refresh
        concentration3.setAutoDraw(True)
    if concentration3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > concentration3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            concentration3.tStop = t  # not accounting for scr refresh
            concentration3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(concentration3, 'tStopRefresh')  # time at next scr refresh
            concentration3.setAutoDraw(False)
    
    # *back2_1* updates
    if back2_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        back2_1.frameNStart = frameN  # exact frame index
        back2_1.tStart = t  # local t and not account for scr refresh
        back2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back2_1, 'tStartRefresh')  # time at next scr refresh
        back2_1.setAutoDraw(True)
    if back2_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > back2_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            back2_1.tStop = t  # not accounting for scr refresh
            back2_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(back2_1, 'tStopRefresh')  # time at next scr refresh
            back2_1.setAutoDraw(False)
    
    # *back2_2* updates
    if back2_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        back2_2.frameNStart = frameN  # exact frame index
        back2_2.tStart = t  # local t and not account for scr refresh
        back2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back2_2, 'tStartRefresh')  # time at next scr refresh
        back2_2.setAutoDraw(True)
    if back2_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > back2_2.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            back2_2.tStop = t  # not accounting for scr refresh
            back2_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(back2_2, 'tStopRefresh')  # time at next scr refresh
            back2_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in _2back_preComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "_2back_pre"-------
for thisComponent in _2back_preComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('concentration3.started', concentration3.tStartRefresh)
thisExp.addData('concentration3.stopped', concentration3.tStopRefresh)
thisExp.addData('back2_1.started', back2_1.tStartRefresh)
thisExp.addData('back2_1.stopped', back2_1.tStopRefresh)
thisExp.addData('back2_2.started', back2_2.tStartRefresh)
thisExp.addData('back2_2.stopped', back2_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop_2back_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\document_2back.xlsx'),
    seed=None, name='loop_2back_2')
thisExp.addLoop(loop_2back_2)  # add the loop to the experiment
thisLoop_2back_2 = loop_2back_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_2back_2.rgb)
if thisLoop_2back_2 != None:
    for paramName in thisLoop_2back_2:
        exec('{} = thisLoop_2back_2[paramName]'.format(paramName))

for thisLoop_2back_2 in loop_2back_2:
    currentLoop = loop_2back_2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_2back_2.rgb)
    if thisLoop_2back_2 != None:
        for paramName in thisLoop_2back_2:
            exec('{} = thisLoop_2back_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "_2back"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    back2_3.setText(num3)
    key_resp_2back.keys = []
    key_resp_2back.rt = []
    _key_resp_2back_allKeys = []
    # keep track of which components have finished
    _2backComponents = [back2_3, key_resp_2back]
    for thisComponent in _2backComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    _2backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "_2back"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = _2backClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=_2backClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back2_3* updates
        if back2_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            back2_3.frameNStart = frameN  # exact frame index
            back2_3.tStart = t  # local t and not account for scr refresh
            back2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back2_3, 'tStartRefresh')  # time at next scr refresh
            back2_3.setAutoDraw(True)
        if back2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back2_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                back2_3.tStop = t  # not accounting for scr refresh
                back2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back2_3, 'tStopRefresh')  # time at next scr refresh
                back2_3.setAutoDraw(False)
        
        # *key_resp_2back* updates
        waitOnFlip = False
        if key_resp_2back.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2back.frameNStart = frameN  # exact frame index
            key_resp_2back.tStart = t  # local t and not account for scr refresh
            key_resp_2back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2back, 'tStartRefresh')  # time at next scr refresh
            key_resp_2back.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2back.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2back.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2back.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2back.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2back.tStop = t  # not accounting for scr refresh
                key_resp_2back.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2back, 'tStopRefresh')  # time at next scr refresh
                key_resp_2back.status = FINISHED
        if key_resp_2back.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2back.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_2back_allKeys.extend(theseKeys)
            if len(_key_resp_2back_allKeys):
                key_resp_2back.keys = _key_resp_2back_allKeys[-1].name  # just the last key pressed
                key_resp_2back.rt = _key_resp_2back_allKeys[-1].rt
                # was this correct?
                if (key_resp_2back.keys == str(num3_corr)) or (key_resp_2back.keys == num3_corr):
                    key_resp_2back.corr = 1
                else:
                    key_resp_2back.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in _2backComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "_2back"-------
    for thisComponent in _2backComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_2back_2.addData('back2_3.started', back2_3.tStartRefresh)
    loop_2back_2.addData('back2_3.stopped', back2_3.tStopRefresh)
    # check responses
    if key_resp_2back.keys in ['', [], None]:  # No response was made
        key_resp_2back.keys = None
        # was no response the correct answer?!
        if str(num3_corr).lower() == 'none':
           key_resp_2back.corr = 1;  # correct non-response
        else:
           key_resp_2back.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_2back_2 (TrialHandler)
    loop_2back_2.addData('key_resp_2back.keys',key_resp_2back.keys)
    loop_2back_2.addData('key_resp_2back.corr', key_resp_2back.corr)
    if key_resp_2back.keys != None:  # we had a response
        loop_2back_2.addData('key_resp_2back.rt', key_resp_2back.rt)
    loop_2back_2.addData('key_resp_2back.started', key_resp_2back.tStartRefresh)
    loop_2back_2.addData('key_resp_2back.stopped', key_resp_2back.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_2back_2'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(4.000000)
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
        if tThisFlipGlobal > text_4.tStartRefresh + 4-frameTolerance:
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
