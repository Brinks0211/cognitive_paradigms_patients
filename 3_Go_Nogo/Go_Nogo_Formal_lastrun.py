#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 六月 15, 2020, at 21:14
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
expName = 'Go_Nogo_Formal'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zhang\\Desktop\\张以昊\\课题组\\3_Go_Nogo\\Go_Nogo_Formal_lastrun.py',
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
    size=[1536, 864], fullscr=True, screen=0, 
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

# Initialize components for Routine "introduction1"
introduction1Clock = core.Clock()
introduction_1 = visual.TextStim(win=win, name='introduction_1',
    text='欢迎参加测试\n（正式部分）\n\n本测试分两种类型\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "introduction4"
introduction4Clock = core.Clock()
introduction_4 = visual.TextStim(win=win, name='introduction_4',
    text='如果准备好了，请开始正式测试\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "introduction2"
introduction2Clock = core.Clock()
introduction_2 = visual.TextStim(win=win, name='introduction_2',
    text='第一种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会出现不同类型的红绿灯图片\n\n如果为绿灯或者黄灯，请按下空格键\n如果为红灯，请不要按键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "light"
lightClock = core.Clock()
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
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_light = keyboard.Keyboard()

# Initialize components for Routine "introduction3"
introduction3Clock = core.Clock()
introduction_3 = visual.TextStim(win=win, name='introduction_3',
    text='第二种类型\n\n测试开始时,屏幕中间会出现注视点“+”\n之后会出现一个表情图片\n\n在每个表情图片出现时\n如果为快乐或者中性，请按下空格键\n如果为悲伤，请不要按键\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "face"
faceClock = core.Clock()
concentration2 = visual.TextStim(win=win, name='concentration2',
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
    ori=0, pos=(0, 0), size=(0.4, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_face = keyboard.Keyboard()

# Initialize components for Routine "tip1"
tip1Clock = core.Clock()
tip_1 = visual.TextStim(win=win, name='tip_1',
    text='现在，测试第一种类型\n\n如果为绿灯或者黄灯，请按下空格键\n如果为红灯，请不要按键\n\n（继续，请按空格键）\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "light"
lightClock = core.Clock()
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
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_light = keyboard.Keyboard()

# Initialize components for Routine "tip2"
tip2Clock = core.Clock()
tip_2 = visual.TextStim(win=win, name='tip_2',
    text='现在，测试第二种类型\n\n在每个表情图片出现时\n如果为快乐或者中性，请按下空格键\n如果为悲伤，请不要按键\n\n（继续，请按空格键）\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "face"
faceClock = core.Clock()
concentration2 = visual.TextStim(win=win, name='concentration2',
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
    ori=0, pos=(0, 0), size=(0.4, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_face = keyboard.Keyboard()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='测试结束，谢谢您的参与',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
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
introduction1Components = [introduction_1, key_resp]
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
    
    # *introduction_1* updates
    if introduction_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_1.frameNStart = frameN  # exact frame index
        introduction_1.tStart = t  # local t and not account for scr refresh
        introduction_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_1, 'tStartRefresh')  # time at next scr refresh
        introduction_1.setAutoDraw(True)
    
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
thisExp.addData('introduction_1.started', introduction_1.tStartRefresh)
thisExp.addData('introduction_1.stopped', introduction_1.tStopRefresh)
# the Routine "introduction1" was not non-slip safe, so reset the non-slip timer
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
# the Routine "introduction4" was not non-slip safe, so reset the non-slip timer
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

# set up handler to look after randomisation of conditions etc
loop_light1 = data.TrialHandler(nReps=12, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\light.xlsx'),
    seed=None, name='loop_light1')
thisExp.addLoop(loop_light1)  # add the loop to the experiment
thisLoop_light1 = loop_light1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_light1.rgb)
if thisLoop_light1 != None:
    for paramName in thisLoop_light1:
        exec('{} = thisLoop_light1[paramName]'.format(paramName))

for thisLoop_light1 in loop_light1:
    currentLoop = loop_light1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_light1.rgb)
    if thisLoop_light1 != None:
        for paramName in thisLoop_light1:
            exec('{} = thisLoop_light1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "light"-------
    continueRoutine = True
    routineTimer.add(2.400000)
    # update component parameters for each repeat
    image.setImage(path1)
    key_resp_light.keys = []
    key_resp_light.rt = []
    _key_resp_light_allKeys = []
    # keep track of which components have finished
    lightComponents = [concentration, image, key_resp_light]
    for thisComponent in lightComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    lightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "light"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lightClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=lightClock)
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
            if tThisFlipGlobal > concentration.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                concentration.tStop = t  # not accounting for scr refresh
                concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration, 'tStopRefresh')  # time at next scr refresh
                concentration.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp_light* updates
        waitOnFlip = False
        if key_resp_light.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            key_resp_light.frameNStart = frameN  # exact frame index
            key_resp_light.tStart = t  # local t and not account for scr refresh
            key_resp_light.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_light, 'tStartRefresh')  # time at next scr refresh
            key_resp_light.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_light.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_light.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_light.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_light.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_light.tStop = t  # not accounting for scr refresh
                key_resp_light.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_light, 'tStopRefresh')  # time at next scr refresh
                key_resp_light.status = FINISHED
        if key_resp_light.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_light.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_light_allKeys.extend(theseKeys)
            if len(_key_resp_light_allKeys):
                key_resp_light.keys = _key_resp_light_allKeys[-1].name  # just the last key pressed
                key_resp_light.rt = _key_resp_light_allKeys[-1].rt
                # was this correct?
                if (key_resp_light.keys == str(path1_corr)) or (key_resp_light.keys == path1_corr):
                    key_resp_light.corr = 1
                else:
                    key_resp_light.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lightComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "light"-------
    for thisComponent in lightComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_light1.addData('concentration.started', concentration.tStartRefresh)
    loop_light1.addData('concentration.stopped', concentration.tStopRefresh)
    loop_light1.addData('image.started', image.tStartRefresh)
    loop_light1.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_light.keys in ['', [], None]:  # No response was made
        key_resp_light.keys = None
        # was no response the correct answer?!
        if str(path1_corr).lower() == 'none':
           key_resp_light.corr = 1;  # correct non-response
        else:
           key_resp_light.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_light1 (TrialHandler)
    loop_light1.addData('key_resp_light.keys',key_resp_light.keys)
    loop_light1.addData('key_resp_light.corr', key_resp_light.corr)
    if key_resp_light.keys != None:  # we had a response
        loop_light1.addData('key_resp_light.rt', key_resp_light.rt)
    loop_light1.addData('key_resp_light.started', key_resp_light.tStartRefresh)
    loop_light1.addData('key_resp_light.stopped', key_resp_light.tStopRefresh)
    thisExp.nextEntry()
    
# completed 12 repeats of 'loop_light1'


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

# set up handler to look after randomisation of conditions etc
loop_face1 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\face.xlsx'),
    seed=None, name='loop_face1')
thisExp.addLoop(loop_face1)  # add the loop to the experiment
thisLoop_face1 = loop_face1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_face1.rgb)
if thisLoop_face1 != None:
    for paramName in thisLoop_face1:
        exec('{} = thisLoop_face1[paramName]'.format(paramName))

for thisLoop_face1 in loop_face1:
    currentLoop = loop_face1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_face1.rgb)
    if thisLoop_face1 != None:
        for paramName in thisLoop_face1:
            exec('{} = thisLoop_face1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "face"-------
    continueRoutine = True
    routineTimer.add(2.400000)
    # update component parameters for each repeat
    image_2.setImage(path2)
    key_resp_face.keys = []
    key_resp_face.rt = []
    _key_resp_face_allKeys = []
    # keep track of which components have finished
    faceComponents = [concentration2, image_2, key_resp_face]
    for thisComponent in faceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    faceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "face"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = faceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=faceClock)
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
            if tThisFlipGlobal > concentration2.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                concentration2.tStop = t  # not accounting for scr refresh
                concentration2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration2, 'tStopRefresh')  # time at next scr refresh
                concentration2.setAutoDraw(False)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *key_resp_face* updates
        waitOnFlip = False
        if key_resp_face.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            key_resp_face.frameNStart = frameN  # exact frame index
            key_resp_face.tStart = t  # local t and not account for scr refresh
            key_resp_face.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_face, 'tStartRefresh')  # time at next scr refresh
            key_resp_face.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_face.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_face.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_face.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_face.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_face.tStop = t  # not accounting for scr refresh
                key_resp_face.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_face, 'tStopRefresh')  # time at next scr refresh
                key_resp_face.status = FINISHED
        if key_resp_face.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_face.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_face_allKeys.extend(theseKeys)
            if len(_key_resp_face_allKeys):
                key_resp_face.keys = _key_resp_face_allKeys[-1].name  # just the last key pressed
                key_resp_face.rt = _key_resp_face_allKeys[-1].rt
                # was this correct?
                if (key_resp_face.keys == str(path2_corr)) or (key_resp_face.keys == path2_corr):
                    key_resp_face.corr = 1
                else:
                    key_resp_face.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in faceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "face"-------
    for thisComponent in faceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_face1.addData('concentration2.started', concentration2.tStartRefresh)
    loop_face1.addData('concentration2.stopped', concentration2.tStopRefresh)
    loop_face1.addData('image_2.started', image_2.tStartRefresh)
    loop_face1.addData('image_2.stopped', image_2.tStopRefresh)
    # check responses
    if key_resp_face.keys in ['', [], None]:  # No response was made
        key_resp_face.keys = None
        # was no response the correct answer?!
        if str(path2_corr).lower() == 'none':
           key_resp_face.corr = 1;  # correct non-response
        else:
           key_resp_face.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_face1 (TrialHandler)
    loop_face1.addData('key_resp_face.keys',key_resp_face.keys)
    loop_face1.addData('key_resp_face.corr', key_resp_face.corr)
    if key_resp_face.keys != None:  # we had a response
        loop_face1.addData('key_resp_face.rt', key_resp_face.rt)
    loop_face1.addData('key_resp_face.started', key_resp_face.tStartRefresh)
    loop_face1.addData('key_resp_face.stopped', key_resp_face.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop_face1'


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

# set up handler to look after randomisation of conditions etc
loop_light2 = data.TrialHandler(nReps=12, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\light.xlsx'),
    seed=None, name='loop_light2')
thisExp.addLoop(loop_light2)  # add the loop to the experiment
thisLoop_light2 = loop_light2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_light2.rgb)
if thisLoop_light2 != None:
    for paramName in thisLoop_light2:
        exec('{} = thisLoop_light2[paramName]'.format(paramName))

for thisLoop_light2 in loop_light2:
    currentLoop = loop_light2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_light2.rgb)
    if thisLoop_light2 != None:
        for paramName in thisLoop_light2:
            exec('{} = thisLoop_light2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "light"-------
    continueRoutine = True
    routineTimer.add(2.400000)
    # update component parameters for each repeat
    image.setImage(path1)
    key_resp_light.keys = []
    key_resp_light.rt = []
    _key_resp_light_allKeys = []
    # keep track of which components have finished
    lightComponents = [concentration, image, key_resp_light]
    for thisComponent in lightComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    lightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "light"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lightClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=lightClock)
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
            if tThisFlipGlobal > concentration.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                concentration.tStop = t  # not accounting for scr refresh
                concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration, 'tStopRefresh')  # time at next scr refresh
                concentration.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp_light* updates
        waitOnFlip = False
        if key_resp_light.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            key_resp_light.frameNStart = frameN  # exact frame index
            key_resp_light.tStart = t  # local t and not account for scr refresh
            key_resp_light.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_light, 'tStartRefresh')  # time at next scr refresh
            key_resp_light.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_light.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_light.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_light.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_light.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_light.tStop = t  # not accounting for scr refresh
                key_resp_light.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_light, 'tStopRefresh')  # time at next scr refresh
                key_resp_light.status = FINISHED
        if key_resp_light.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_light.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_light_allKeys.extend(theseKeys)
            if len(_key_resp_light_allKeys):
                key_resp_light.keys = _key_resp_light_allKeys[-1].name  # just the last key pressed
                key_resp_light.rt = _key_resp_light_allKeys[-1].rt
                # was this correct?
                if (key_resp_light.keys == str(path1_corr)) or (key_resp_light.keys == path1_corr):
                    key_resp_light.corr = 1
                else:
                    key_resp_light.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lightComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "light"-------
    for thisComponent in lightComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_light2.addData('concentration.started', concentration.tStartRefresh)
    loop_light2.addData('concentration.stopped', concentration.tStopRefresh)
    loop_light2.addData('image.started', image.tStartRefresh)
    loop_light2.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_light.keys in ['', [], None]:  # No response was made
        key_resp_light.keys = None
        # was no response the correct answer?!
        if str(path1_corr).lower() == 'none':
           key_resp_light.corr = 1;  # correct non-response
        else:
           key_resp_light.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_light2 (TrialHandler)
    loop_light2.addData('key_resp_light.keys',key_resp_light.keys)
    loop_light2.addData('key_resp_light.corr', key_resp_light.corr)
    if key_resp_light.keys != None:  # we had a response
        loop_light2.addData('key_resp_light.rt', key_resp_light.rt)
    loop_light2.addData('key_resp_light.started', key_resp_light.tStartRefresh)
    loop_light2.addData('key_resp_light.stopped', key_resp_light.tStopRefresh)
    thisExp.nextEntry()
    
# completed 12 repeats of 'loop_light2'


# ------Prepare to start Routine "tip2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
tip2Components = [tip_2, key_resp_7]
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
thisExp.addData('tip_2.started', tip_2.tStartRefresh)
thisExp.addData('tip_2.stopped', tip_2.tStopRefresh)
# the Routine "tip2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_face2 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents\\face.xlsx'),
    seed=None, name='loop_face2')
thisExp.addLoop(loop_face2)  # add the loop to the experiment
thisLoop_face2 = loop_face2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_face2.rgb)
if thisLoop_face2 != None:
    for paramName in thisLoop_face2:
        exec('{} = thisLoop_face2[paramName]'.format(paramName))

for thisLoop_face2 in loop_face2:
    currentLoop = loop_face2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_face2.rgb)
    if thisLoop_face2 != None:
        for paramName in thisLoop_face2:
            exec('{} = thisLoop_face2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "face"-------
    continueRoutine = True
    routineTimer.add(2.400000)
    # update component parameters for each repeat
    image_2.setImage(path2)
    key_resp_face.keys = []
    key_resp_face.rt = []
    _key_resp_face_allKeys = []
    # keep track of which components have finished
    faceComponents = [concentration2, image_2, key_resp_face]
    for thisComponent in faceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    faceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "face"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = faceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=faceClock)
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
            if tThisFlipGlobal > concentration2.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                concentration2.tStop = t  # not accounting for scr refresh
                concentration2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration2, 'tStopRefresh')  # time at next scr refresh
                concentration2.setAutoDraw(False)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *key_resp_face* updates
        waitOnFlip = False
        if key_resp_face.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            key_resp_face.frameNStart = frameN  # exact frame index
            key_resp_face.tStart = t  # local t and not account for scr refresh
            key_resp_face.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_face, 'tStartRefresh')  # time at next scr refresh
            key_resp_face.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_face.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_face.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_face.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_face.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_face.tStop = t  # not accounting for scr refresh
                key_resp_face.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_face, 'tStopRefresh')  # time at next scr refresh
                key_resp_face.status = FINISHED
        if key_resp_face.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_face.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_face_allKeys.extend(theseKeys)
            if len(_key_resp_face_allKeys):
                key_resp_face.keys = _key_resp_face_allKeys[-1].name  # just the last key pressed
                key_resp_face.rt = _key_resp_face_allKeys[-1].rt
                # was this correct?
                if (key_resp_face.keys == str(path2_corr)) or (key_resp_face.keys == path2_corr):
                    key_resp_face.corr = 1
                else:
                    key_resp_face.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in faceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "face"-------
    for thisComponent in faceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_face2.addData('concentration2.started', concentration2.tStartRefresh)
    loop_face2.addData('concentration2.stopped', concentration2.tStopRefresh)
    loop_face2.addData('image_2.started', image_2.tStartRefresh)
    loop_face2.addData('image_2.stopped', image_2.tStopRefresh)
    # check responses
    if key_resp_face.keys in ['', [], None]:  # No response was made
        key_resp_face.keys = None
        # was no response the correct answer?!
        if str(path2_corr).lower() == 'none':
           key_resp_face.corr = 1;  # correct non-response
        else:
           key_resp_face.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_face2 (TrialHandler)
    loop_face2.addData('key_resp_face.keys',key_resp_face.keys)
    loop_face2.addData('key_resp_face.corr', key_resp_face.corr)
    if key_resp_face.keys != None:  # we had a response
        loop_face2.addData('key_resp_face.rt', key_resp_face.rt)
    loop_face2.addData('key_resp_face.started', key_resp_face.tStartRefresh)
    loop_face2.addData('key_resp_face.stopped', key_resp_face.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop_face2'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text]
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
        if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

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
