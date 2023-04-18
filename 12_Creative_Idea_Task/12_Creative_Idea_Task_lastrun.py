#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on 八月 07, 2021, at 09:58
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.2'
expName = 'Creative_Idea_Task'  # from the Builder filename that created this script
expInfo = {'participant': '', '姓名频音': '', '男1/女2': '', '入院1/出院2': ''}
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
    originPath='D:\\张以昊\\张以昊\\个人\\psychopy\\psychopy实验范式\\12_Creative_Idea_Task\\12_Creative_Idea_Task_lastrun.py',
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

# Initialize components for Routine "introduction_tot"
introduction_totClock = core.Clock()
introduction_1 = visual.TextStim(win=win, name='introduction_1',
    text='欢迎参加创造力测试\n\n本测试包括两个部分\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_total = keyboard.Keyboard()

# Initialize components for Routine "introduction_part1"
introduction_part1Clock = core.Clock()
key_part1_1 = keyboard.Keyboard()
introduction_2 = visual.TextStim(win=win, name='introduction_2',
    text='这是第一种类型：聚合思维能力\n\n测试开始时，屏幕中间会出现注视点“+”，\n之后每个题目会出现三个有某种联系的字，\n需要你找到另外一个字，分别和这三个字\n都能组成词。\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "introduction_part1_1"
introduction_part1_1Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='例如，“贯/看/透”。\n“穿”是和这三个字都存在联系的其中一个字。\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "introduction_part1_2"
introduction_part1_2Clock = core.Clock()
key_part1_2 = keyboard.Keyboard()
introduction_3 = visual.TextStim(win=win, name='introduction_3',
    text='请将后面30道题目的答案写在答题纸上。\n每个题目，您有15s思考时间和5s作答时间。\n\n(继续，请按空格键)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "introduction_part1_4"
introduction_part1_4Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='本部分没有练习！\n\n如果准备好了，请进入正式测试！\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trial1_1"
trial1_1Clock = core.Clock()
concentration = visual.TextStim(win=win, name='concentration',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
question_num = visual.TextStim(win=win, name='question_num',
    text='',
    font='Arial',
    pos=(0, 0.25), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
left_character = visual.TextStim(win=win, name='left_character',
    text='',
    font='Arial',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
middle_character = visual.TextStim(win=win, name='middle_character',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
right_character = visual.TextStim(win=win, name='right_character',
    text='',
    font='Arial',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
write_answer1 = visual.TextStim(win=win, name='write_answer1',
    text='请将答案写在答题纸上',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "trial1_break1"
trial1_break1Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='已完成10道\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "trial1_2"
trial1_2Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='',
    font='Open Sans',
    pos=(0, 0.25), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='请将答案写在答题纸上',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "trial1_break2"
trial1_break2Clock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='已完成20道\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "trial1_3"
trial1_3Clock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='',
    font='Open Sans',
    pos=(0, 0.25), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_20 = visual.TextStim(win=win, name='text_20',
    text='',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='请将答案写在答题纸上',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "breaking"
breakingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='第一种类型测试结束！\n\n现在是休息阶段\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "introduction_part1_3"
introduction_part1_3Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='现在进入第二种类型的测试：发散思维能力\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_part1_3 = keyboard.Keyboard()

# Initialize components for Routine "introduction_part2_1"
introduction_part2_1Clock = core.Clock()
key_part2_1 = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='这是第二种类型：发散思维能力\n\n测试开始时，屏幕中间会出现注视点“+”\n之后屏幕上会出现我们生活中常见的\n物品词汇。请您尽可能地写出该物品\n的不同新颖用途，想法越多越好。\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "introduction_part2_2"
introduction_part2_2Clock = core.Clock()
key_part2_2 = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='请您将后面6道题的答案写在答题纸上。\n每个题目您有2min的思考和作答时间。\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "introduction_part2_3"
introduction_part2_3Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='本部分没有练习！\n\n如果准备好了，请进入正式测试！\n\n（继续，请按空格键）',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
concentra = visual.TextStim(win=win, name='concentra',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
word = visual.TextStim(win=win, name='word',
    text='',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
trial2_num = visual.TextStim(win=win, name='trial2_num',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
over = visual.TextStim(win=win, name='over',
    text='实验结束，感谢您参与实验！',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction_tot"-------
continueRoutine = True
# update component parameters for each repeat
key_total.keys = []
key_total.rt = []
_key_total_allKeys = []
# keep track of which components have finished
introduction_totComponents = [introduction_1, key_total]
for thisComponent in introduction_totComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_totClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_tot"-------
while continueRoutine:
    # get current time
    t = introduction_totClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_totClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction_1* updates
    if introduction_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_1.frameNStart = frameN  # exact frame index
        introduction_1.tStart = t  # local t and not account for scr refresh
        introduction_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_1, 'tStartRefresh')  # time at next scr refresh
        introduction_1.setAutoDraw(True)
    
    # *key_total* updates
    waitOnFlip = False
    if key_total.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_total.frameNStart = frameN  # exact frame index
        key_total.tStart = t  # local t and not account for scr refresh
        key_total.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_total, 'tStartRefresh')  # time at next scr refresh
        key_total.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_total.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_total.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_total.status == STARTED and not waitOnFlip:
        theseKeys = key_total.getKeys(keyList=['space'], waitRelease=False)
        _key_total_allKeys.extend(theseKeys)
        if len(_key_total_allKeys):
            key_total.keys = _key_total_allKeys[-1].name  # just the last key pressed
            key_total.rt = _key_total_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction_totComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_tot"-------
for thisComponent in introduction_totComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction_tot" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction_part1"-------
continueRoutine = True
# update component parameters for each repeat
key_part1_1.keys = []
key_part1_1.rt = []
_key_part1_1_allKeys = []
# keep track of which components have finished
introduction_part1Components = [key_part1_1, introduction_2]
for thisComponent in introduction_part1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_part1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_part1"-------
while continueRoutine:
    # get current time
    t = introduction_part1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_part1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_part1_1* updates
    waitOnFlip = False
    if key_part1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_part1_1.frameNStart = frameN  # exact frame index
        key_part1_1.tStart = t  # local t and not account for scr refresh
        key_part1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_part1_1, 'tStartRefresh')  # time at next scr refresh
        key_part1_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_part1_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_part1_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_part1_1.status == STARTED and not waitOnFlip:
        theseKeys = key_part1_1.getKeys(keyList=['space'], waitRelease=False)
        _key_part1_1_allKeys.extend(theseKeys)
        if len(_key_part1_1_allKeys):
            key_part1_1.keys = _key_part1_1_allKeys[-1].name  # just the last key pressed
            key_part1_1.rt = _key_part1_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *introduction_2* updates
    if introduction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_2.frameNStart = frameN  # exact frame index
        introduction_2.tStart = t  # local t and not account for scr refresh
        introduction_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_2, 'tStartRefresh')  # time at next scr refresh
        introduction_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction_part1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_part1"-------
for thisComponent in introduction_part1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction_part1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction_part1_1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
introduction_part1_1Components = [text_7, key_resp_4]
for thisComponent in introduction_part1_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_part1_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_part1_1"-------
while continueRoutine:
    # get current time
    t = introduction_part1_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_part1_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *key_resp_4* updates
    if key_resp_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        key_resp_4.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
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
    for thisComponent in introduction_part1_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_part1_1"-------
for thisComponent in introduction_part1_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction_part1_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction_part1_2"-------
continueRoutine = True
# update component parameters for each repeat
key_part1_2.keys = []
key_part1_2.rt = []
_key_part1_2_allKeys = []
# keep track of which components have finished
introduction_part1_2Components = [key_part1_2, introduction_3]
for thisComponent in introduction_part1_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_part1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_part1_2"-------
while continueRoutine:
    # get current time
    t = introduction_part1_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_part1_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_part1_2* updates
    waitOnFlip = False
    if key_part1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_part1_2.frameNStart = frameN  # exact frame index
        key_part1_2.tStart = t  # local t and not account for scr refresh
        key_part1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_part1_2, 'tStartRefresh')  # time at next scr refresh
        key_part1_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_part1_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_part1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_part1_2.status == STARTED and not waitOnFlip:
        theseKeys = key_part1_2.getKeys(keyList=['space'], waitRelease=False)
        _key_part1_2_allKeys.extend(theseKeys)
        if len(_key_part1_2_allKeys):
            key_part1_2.keys = _key_part1_2_allKeys[-1].name  # just the last key pressed
            key_part1_2.rt = _key_part1_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *introduction_3* updates
    if introduction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_3.frameNStart = frameN  # exact frame index
        introduction_3.tStart = t  # local t and not account for scr refresh
        introduction_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_3, 'tStartRefresh')  # time at next scr refresh
        introduction_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction_part1_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_part1_2"-------
for thisComponent in introduction_part1_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction_part1_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction_part1_4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
introduction_part1_4Components = [text_5, key_resp_2]
for thisComponent in introduction_part1_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_part1_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_part1_4"-------
while continueRoutine:
    # get current time
    t = introduction_part1_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_part1_4Clock)
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
    
    # *key_resp_2* updates
    if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
    for thisComponent in introduction_part1_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_part1_4"-------
for thisComponent in introduction_part1_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction_part1_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('document/part1_1.xlsx', selection='1'),
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
    
    # ------Prepare to start Routine "trial1_1"-------
    continueRoutine = True
    routineTimer.add(20.500000)
    # update component parameters for each repeat
    question_num.setText(num)
    left_character.setText(left)
    middle_character.setText(middle)
    right_character.setText(right)
    # keep track of which components have finished
    trial1_1Components = [concentration, question_num, left_character, middle_character, right_character, write_answer1]
    for thisComponent in trial1_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1_1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration* updates
        if concentration.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration.frameNStart = frameN  # exact frame index
            concentration.tStart = t  # local t and not account for scr refresh
            concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration, 'tStartRefresh')  # time at next scr refresh
            concentration.setAutoDraw(True)
        if concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                concentration.tStop = t  # not accounting for scr refresh
                concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration, 'tStopRefresh')  # time at next scr refresh
                concentration.setAutoDraw(False)
        
        # *question_num* updates
        if question_num.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            question_num.frameNStart = frameN  # exact frame index
            question_num.tStart = t  # local t and not account for scr refresh
            question_num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_num, 'tStartRefresh')  # time at next scr refresh
            question_num.setAutoDraw(True)
        if question_num.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > question_num.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                question_num.tStop = t  # not accounting for scr refresh
                question_num.frameNStop = frameN  # exact frame index
                win.timeOnFlip(question_num, 'tStopRefresh')  # time at next scr refresh
                question_num.setAutoDraw(False)
        
        # *left_character* updates
        if left_character.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            left_character.frameNStart = frameN  # exact frame index
            left_character.tStart = t  # local t and not account for scr refresh
            left_character.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_character, 'tStartRefresh')  # time at next scr refresh
            left_character.setAutoDraw(True)
        if left_character.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > left_character.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                left_character.tStop = t  # not accounting for scr refresh
                left_character.frameNStop = frameN  # exact frame index
                win.timeOnFlip(left_character, 'tStopRefresh')  # time at next scr refresh
                left_character.setAutoDraw(False)
        
        # *middle_character* updates
        if middle_character.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            middle_character.frameNStart = frameN  # exact frame index
            middle_character.tStart = t  # local t and not account for scr refresh
            middle_character.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(middle_character, 'tStartRefresh')  # time at next scr refresh
            middle_character.setAutoDraw(True)
        if middle_character.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > middle_character.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                middle_character.tStop = t  # not accounting for scr refresh
                middle_character.frameNStop = frameN  # exact frame index
                win.timeOnFlip(middle_character, 'tStopRefresh')  # time at next scr refresh
                middle_character.setAutoDraw(False)
        
        # *right_character* updates
        if right_character.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            right_character.frameNStart = frameN  # exact frame index
            right_character.tStart = t  # local t and not account for scr refresh
            right_character.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_character, 'tStartRefresh')  # time at next scr refresh
            right_character.setAutoDraw(True)
        if right_character.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right_character.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                right_character.tStop = t  # not accounting for scr refresh
                right_character.frameNStop = frameN  # exact frame index
                win.timeOnFlip(right_character, 'tStopRefresh')  # time at next scr refresh
                right_character.setAutoDraw(False)
        
        # *write_answer1* updates
        if write_answer1.status == NOT_STARTED and tThisFlip >= 15.5-frameTolerance:
            # keep track of start time/frame for later
            write_answer1.frameNStart = frameN  # exact frame index
            write_answer1.tStart = t  # local t and not account for scr refresh
            write_answer1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(write_answer1, 'tStartRefresh')  # time at next scr refresh
            write_answer1.setAutoDraw(True)
        if write_answer1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > write_answer1.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                write_answer1.tStop = t  # not accounting for scr refresh
                write_answer1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(write_answer1, 'tStopRefresh')  # time at next scr refresh
                write_answer1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1_1"-------
    for thisComponent in trial1_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop1.addData('question_num.started', question_num.tStartRefresh)
    loop1.addData('question_num.stopped', question_num.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop1'


# ------Prepare to start Routine "trial1_break1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
trial1_break1Components = [text_14, key_resp_5]
for thisComponent in trial1_break1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial1_break1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial1_break1"-------
while continueRoutine:
    # get current time
    t = trial1_break1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial1_break1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
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
    for thisComponent in trial1_break1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial1_break1"-------
for thisComponent in trial1_break1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
# the Routine "trial1_break1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('document/part1_2.xlsx', selection='1'),
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
    
    # ------Prepare to start Routine "trial1_2"-------
    continueRoutine = True
    routineTimer.add(20.500000)
    # update component parameters for each repeat
    text_9.setText(left)
    text_10.setText(middle)
    text_11.setText(right)
    text_12.setText(num)
    # keep track of which components have finished
    trial1_2Components = [text_8, text_9, text_10, text_11, text_12, text_13]
    for thisComponent in trial1_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1_2Clock)
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
            if tThisFlipGlobal > text_8.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_10.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                text_10.setAutoDraw(False)
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        if text_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_11.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_11.tStop = t  # not accounting for scr refresh
                text_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                text_11.setAutoDraw(False)
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        if text_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_12.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_12.tStop = t  # not accounting for scr refresh
                text_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                text_12.setAutoDraw(False)
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 15.5-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        if text_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_13.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_13.tStop = t  # not accounting for scr refresh
                text_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
                text_13.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1_2"-------
    for thisComponent in trial1_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_8.started', text_8.tStartRefresh)
    trials.addData('text_8.stopped', text_8.tStopRefresh)
    trials.addData('text_13.started', text_13.tStartRefresh)
    trials.addData('text_13.stopped', text_13.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "trial1_break2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
trial1_break2Components = [text_15, key_resp_6]
for thisComponent in trial1_break2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial1_break2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial1_break2"-------
while continueRoutine:
    # get current time
    t = trial1_break2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial1_break2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # *key_resp_6* updates
    if key_resp_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        key_resp_6.clock.reset()  # now t=0
        key_resp_6.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
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
    for thisComponent in trial1_break2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial1_break2"-------
for thisComponent in trial1_break2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial1_break2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('document/part1_3.xlsx', selection='1'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1_3"-------
    continueRoutine = True
    routineTimer.add(20.500000)
    # update component parameters for each repeat
    text_17.setText(num)
    text_18.setText(left)
    text_19.setText(middle)
    text_20.setText(right)
    # keep track of which components have finished
    trial1_3Components = [text_16, text_17, text_18, text_19, text_20, text_21]
    for thisComponent in trial1_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        if text_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_16.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_16.tStop = t  # not accounting for scr refresh
                text_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
                text_16.setAutoDraw(False)
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        if text_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_17.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_17.tStop = t  # not accounting for scr refresh
                text_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
                text_17.setAutoDraw(False)
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            text_18.setAutoDraw(True)
        if text_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_18.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_18.tStop = t  # not accounting for scr refresh
                text_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_18, 'tStopRefresh')  # time at next scr refresh
                text_18.setAutoDraw(False)
        
        # *text_19* updates
        if text_19.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_19.frameNStart = frameN  # exact frame index
            text_19.tStart = t  # local t and not account for scr refresh
            text_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
            text_19.setAutoDraw(True)
        if text_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_19.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_19.tStop = t  # not accounting for scr refresh
                text_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_19, 'tStopRefresh')  # time at next scr refresh
                text_19.setAutoDraw(False)
        
        # *text_20* updates
        if text_20.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_20.frameNStart = frameN  # exact frame index
            text_20.tStart = t  # local t and not account for scr refresh
            text_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
            text_20.setAutoDraw(True)
        if text_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_20.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_20.tStop = t  # not accounting for scr refresh
                text_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_20, 'tStopRefresh')  # time at next scr refresh
                text_20.setAutoDraw(False)
        
        # *text_21* updates
        if text_21.status == NOT_STARTED and tThisFlip >= 15.5-frameTolerance:
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            text_21.setAutoDraw(True)
        if text_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_21.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_21.tStop = t  # not accounting for scr refresh
                text_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
                text_21.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1_3"-------
    for thisComponent in trial1_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_16.started', text_16.tStartRefresh)
    trials_2.addData('text_16.stopped', text_16.tStopRefresh)
    trials_2.addData('text_17.started', text_17.tStartRefresh)
    trials_2.addData('text_17.stopped', text_17.tStopRefresh)
    trials_2.addData('text_21.started', text_21.tStartRefresh)
    trials_2.addData('text_21.stopped', text_21.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "breaking"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
breakingComponents = [text, key_resp]
for thisComponent in breakingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
breakingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "breaking"-------
while continueRoutine:
    # get current time
    t = breakingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=breakingClock)
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
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
    for thisComponent in breakingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "breaking"-------
for thisComponent in breakingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "breaking" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction_part1_3"-------
continueRoutine = True
# update component parameters for each repeat
key_part1_3.keys = []
key_part1_3.rt = []
_key_part1_3_allKeys = []
# keep track of which components have finished
introduction_part1_3Components = [text_2, key_part1_3]
for thisComponent in introduction_part1_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_part1_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_part1_3"-------
while continueRoutine:
    # get current time
    t = introduction_part1_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_part1_3Clock)
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
    
    # *key_part1_3* updates
    waitOnFlip = False
    if key_part1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_part1_3.frameNStart = frameN  # exact frame index
        key_part1_3.tStart = t  # local t and not account for scr refresh
        key_part1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_part1_3, 'tStartRefresh')  # time at next scr refresh
        key_part1_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_part1_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_part1_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_part1_3.status == STARTED and not waitOnFlip:
        theseKeys = key_part1_3.getKeys(keyList=['space'], waitRelease=False)
        _key_part1_3_allKeys.extend(theseKeys)
        if len(_key_part1_3_allKeys):
            key_part1_3.keys = _key_part1_3_allKeys[-1].name  # just the last key pressed
            key_part1_3.rt = _key_part1_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction_part1_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_part1_3"-------
for thisComponent in introduction_part1_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction_part1_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction_part2_1"-------
continueRoutine = True
# update component parameters for each repeat
key_part2_1.keys = []
key_part2_1.rt = []
_key_part2_1_allKeys = []
# keep track of which components have finished
introduction_part2_1Components = [key_part2_1, text_3]
for thisComponent in introduction_part2_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_part2_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_part2_1"-------
while continueRoutine:
    # get current time
    t = introduction_part2_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_part2_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_part2_1* updates
    waitOnFlip = False
    if key_part2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_part2_1.frameNStart = frameN  # exact frame index
        key_part2_1.tStart = t  # local t and not account for scr refresh
        key_part2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_part2_1, 'tStartRefresh')  # time at next scr refresh
        key_part2_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_part2_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_part2_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_part2_1.status == STARTED and not waitOnFlip:
        theseKeys = key_part2_1.getKeys(keyList=['space'], waitRelease=False)
        _key_part2_1_allKeys.extend(theseKeys)
        if len(_key_part2_1_allKeys):
            key_part2_1.keys = _key_part2_1_allKeys[-1].name  # just the last key pressed
            key_part2_1.rt = _key_part2_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction_part2_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_part2_1"-------
for thisComponent in introduction_part2_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction_part2_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction_part2_2"-------
continueRoutine = True
# update component parameters for each repeat
key_part2_2.keys = []
key_part2_2.rt = []
_key_part2_2_allKeys = []
# keep track of which components have finished
introduction_part2_2Components = [key_part2_2, text_4]
for thisComponent in introduction_part2_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_part2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_part2_2"-------
while continueRoutine:
    # get current time
    t = introduction_part2_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_part2_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_part2_2* updates
    waitOnFlip = False
    if key_part2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_part2_2.frameNStart = frameN  # exact frame index
        key_part2_2.tStart = t  # local t and not account for scr refresh
        key_part2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_part2_2, 'tStartRefresh')  # time at next scr refresh
        key_part2_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_part2_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_part2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_part2_2.status == STARTED and not waitOnFlip:
        theseKeys = key_part2_2.getKeys(keyList=['space'], waitRelease=False)
        _key_part2_2_allKeys.extend(theseKeys)
        if len(_key_part2_2_allKeys):
            key_part2_2.keys = _key_part2_2_allKeys[-1].name  # just the last key pressed
            key_part2_2.rt = _key_part2_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction_part2_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_part2_2"-------
for thisComponent in introduction_part2_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction_part2_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction_part2_3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
introduction_part2_3Components = [text_6, key_resp_3]
for thisComponent in introduction_part2_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_part2_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_part2_3"-------
while continueRoutine:
    # get current time
    t = introduction_part2_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_part2_3Clock)
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
    
    # *key_resp_3* updates
    if key_resp_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        key_resp_3.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
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
    for thisComponent in introduction_part2_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_part2_3"-------
for thisComponent in introduction_part2_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction_part2_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('document/part_2.xlsx', selection='2'),
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
    routineTimer.add(120.500000)
    # update component parameters for each repeat
    word.setText(object)
    trial2_num.setText(num)
    # keep track of which components have finished
    trial2Components = [concentra, word, trial2_num]
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
        
        # *concentra* updates
        if concentra.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentra.frameNStart = frameN  # exact frame index
            concentra.tStart = t  # local t and not account for scr refresh
            concentra.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentra, 'tStartRefresh')  # time at next scr refresh
            concentra.setAutoDraw(True)
        if concentra.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentra.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                concentra.tStop = t  # not accounting for scr refresh
                concentra.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentra, 'tStopRefresh')  # time at next scr refresh
                concentra.setAutoDraw(False)
        
        # *word* updates
        if word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            word.frameNStart = frameN  # exact frame index
            word.tStart = t  # local t and not account for scr refresh
            word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word, 'tStartRefresh')  # time at next scr refresh
            word.setAutoDraw(True)
        if word.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word.tStartRefresh + 120-frameTolerance:
                # keep track of stop time/frame for later
                word.tStop = t  # not accounting for scr refresh
                word.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word, 'tStopRefresh')  # time at next scr refresh
                word.setAutoDraw(False)
        
        # *trial2_num* updates
        if trial2_num.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            trial2_num.frameNStart = frameN  # exact frame index
            trial2_num.tStart = t  # local t and not account for scr refresh
            trial2_num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2_num, 'tStartRefresh')  # time at next scr refresh
            trial2_num.setAutoDraw(True)
        if trial2_num.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2_num.tStartRefresh + 120-frameTolerance:
                # keep track of stop time/frame for later
                trial2_num.tStop = t  # not accounting for scr refresh
                trial2_num.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2_num, 'tStopRefresh')  # time at next scr refresh
                trial2_num.setAutoDraw(False)
        
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
    loop2.addData('word.started', word.tStartRefresh)
    loop2.addData('word.stopped', word.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop2'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [over]
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
    
    # *over* updates
    if over.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        over.frameNStart = frameN  # exact frame index
        over.tStart = t  # local t and not account for scr refresh
        over.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(over, 'tStartRefresh')  # time at next scr refresh
        over.setAutoDraw(True)
    if over.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > over.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            over.tStop = t  # not accounting for scr refresh
            over.frameNStop = frameN  # exact frame index
            win.timeOnFlip(over, 'tStopRefresh')  # time at next scr refresh
            over.setAutoDraw(False)
    
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
