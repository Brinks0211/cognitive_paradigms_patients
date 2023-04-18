#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on 八月 19, 2021, at 11:00
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
    originPath='D:\\张以昊\\张以昊\\个人\\psychopy\\psychopy实验范式\\13_Memory_Task\\Memory_Task_lastrun.py',
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
button_re =4
textFill = ''
over = 0
over_re = 0

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
text = visual.TextStim(win=win, name='text',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
concentration_five = visual.TextStim(win=win, name='concentration_five',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
five_1 = visual.TextStim(win=win, name='five_1',
    text='3',
    font='Open Sans',
    pos=(-0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
five_2 = visual.TextStim(win=win, name='five_2',
    text='4',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
five_3 = visual.TextStim(win=win, name='five_3',
    text='6\n',
    font='Open Sans',
    pos=(0, -0.07), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
five_4 = visual.TextStim(win=win, name='five_4',
    text='1',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
five_5 = visual.TextStim(win=win, name='five_5',
    text='3',
    font='Open Sans',
    pos=(0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
five_input = visual.TextStim(win=win, name='five_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
five_tip = visual.TextStim(win=win, name='five_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "six"
sixClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
concentration_six = visual.TextStim(win=win, name='concentration_six',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
six_1 = visual.TextStim(win=win, name='six_1',
    text='2',
    font='Open Sans',
    pos=(-0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
six_2 = visual.TextStim(win=win, name='six_2',
    text='2',
    font='Open Sans',
    pos=(-0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
six_3 = visual.TextStim(win=win, name='six_3',
    text='7',
    font='Open Sans',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
six_4 = visual.TextStim(win=win, name='six_4',
    text='4',
    font='Open Sans',
    pos=(0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
six_5 = visual.TextStim(win=win, name='six_5',
    text='8',
    font='Open Sans',
    pos=(0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
six_6 = visual.TextStim(win=win, name='six_6',
    text='5',
    font='Open Sans',
    pos=(0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
six_input = visual.TextStim(win=win, name='six_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
six_tip = visual.TextStim(win=win, name='six_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "seven"
sevenClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
concentration_seven = visual.TextStim(win=win, name='concentration_seven',
    text='+\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
seven_1 = visual.TextStim(win=win, name='seven_1',
    text='3',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
seven_2 = visual.TextStim(win=win, name='seven_2',
    text='8',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
seven_3 = visual.TextStim(win=win, name='seven_3',
    text='6',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
seven_4 = visual.TextStim(win=win, name='seven_4',
    text='4',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
seven_5 = visual.TextStim(win=win, name='seven_5',
    text='1',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
seven_6 = visual.TextStim(win=win, name='seven_6',
    text='4',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
seven_7 = visual.TextStim(win=win, name='seven_7',
    text='7',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
seven_input = visual.TextStim(win=win, name='seven_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
seven_tip = visual.TextStim(win=win, name='seven_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "eight"
eightClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
eight_concentration = visual.TextStim(win=win, name='eight_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
eight_1 = visual.TextStim(win=win, name='eight_1',
    text='4',
    font='Open Sans',
    pos=(-0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
eight_2 = visual.TextStim(win=win, name='eight_2',
    text='3',
    font='Open Sans',
    pos=(-0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
eight_3 = visual.TextStim(win=win, name='eight_3',
    text='7',
    font='Open Sans',
    pos=(-0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
eight_4 = visual.TextStim(win=win, name='eight_4',
    text='8',
    font='Open Sans',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
eight_5 = visual.TextStim(win=win, name='eight_5',
    text='9',
    font='Open Sans',
    pos=(0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
eight_6 = visual.TextStim(win=win, name='eight_6',
    text='7',
    font='Open Sans',
    pos=(0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
eight_7 = visual.TextStim(win=win, name='eight_7',
    text='8',
    font='Open Sans',
    pos=(0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
eight_8 = visual.TextStim(win=win, name='eight_8',
    text='6',
    font='Open Sans',
    pos=(0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
eight_input = visual.TextStim(win=win, name='eight_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
eight_tip = visual.TextStim(win=win, name='eight_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "nine"
nineClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
nine_concentration = visual.TextStim(win=win, name='nine_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
nine_1 = visual.TextStim(win=win, name='nine_1',
    text='4',
    font='Open Sans',
    pos=(-0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
nine_2 = visual.TextStim(win=win, name='nine_2',
    text='4',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
nine_3 = visual.TextStim(win=win, name='nine_3',
    text='3',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
nine_4 = visual.TextStim(win=win, name='nine_4',
    text='5',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
nine_5 = visual.TextStim(win=win, name='nine_5',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
nine_6 = visual.TextStim(win=win, name='nine_6',
    text='1',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
nine_7 = visual.TextStim(win=win, name='nine_7',
    text='7',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
nine_8 = visual.TextStim(win=win, name='nine_8',
    text='2',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
nine_9 = visual.TextStim(win=win, name='nine_9',
    text='9',
    font='Open Sans',
    pos=(0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
nine_input = visual.TextStim(win=win, name='nine_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
nine_tip = visual.TextStim(win=win, name='nine_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "ten"
tenClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ten_concentration = visual.TextStim(win=win, name='ten_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ten_1 = visual.TextStim(win=win, name='ten_1',
    text='3',
    font='Open Sans',
    pos=(-0.45, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ten_2 = visual.TextStim(win=win, name='ten_2',
    text='5',
    font='Open Sans',
    pos=(-0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ten_3 = visual.TextStim(win=win, name='ten_3',
    text='4',
    font='Open Sans',
    pos=(-0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ten_4 = visual.TextStim(win=win, name='ten_4',
    text='4',
    font='Open Sans',
    pos=(-0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
ten_5 = visual.TextStim(win=win, name='ten_5',
    text='2',
    font='Open Sans',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
ten_6 = visual.TextStim(win=win, name='ten_6',
    text='6',
    font='Open Sans',
    pos=(0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
ten_7 = visual.TextStim(win=win, name='ten_7',
    text='7',
    font='Open Sans',
    pos=(0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
ten_8 = visual.TextStim(win=win, name='ten_8',
    text='9',
    font='Open Sans',
    pos=(0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
ten_9 = visual.TextStim(win=win, name='ten_9',
    text='8',
    font='Open Sans',
    pos=(0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
ten_10 = visual.TextStim(win=win, name='ten_10',
    text='1',
    font='Open Sans',
    pos=(0.45, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
ten_input = visual.TextStim(win=win, name='ten_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
ten_tip = visual.TextStim(win=win, name='ten_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "eleven"
elevenClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
eleven_concentration = visual.TextStim(win=win, name='eleven_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
eleven_1 = visual.TextStim(win=win, name='eleven_1',
    text='6',
    font='Open Sans',
    pos=(-0.5, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
eleven_2 = visual.TextStim(win=win, name='eleven_2',
    text='0',
    font='Open Sans',
    pos=(-0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
eleven_3 = visual.TextStim(win=win, name='eleven_3',
    text='2',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
eleven_4 = visual.TextStim(win=win, name='eleven_4',
    text='8',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
eleven_5 = visual.TextStim(win=win, name='eleven_5',
    text='4',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
eleven_6 = visual.TextStim(win=win, name='eleven_6',
    text='0',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
eleven_7 = visual.TextStim(win=win, name='eleven_7',
    text='9',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
eleven_8 = visual.TextStim(win=win, name='eleven_8',
    text='6',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
eleven_9 = visual.TextStim(win=win, name='eleven_9',
    text='3',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
eleven_10 = visual.TextStim(win=win, name='eleven_10',
    text='3',
    font='Open Sans',
    pos=(0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
eleven_11 = visual.TextStim(win=win, name='eleven_11',
    text='5',
    font='Open Sans',
    pos=(0.5, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
eleven_input = visual.TextStim(win=win, name='eleven_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
eleven_tip = visual.TextStim(win=win, name='eleven_tip',
    text='请顺序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);

# Initialize components for Routine "four_re"
four_reClock = core.Clock()
four_re_concentration = visual.TextStim(win=win, name='four_re_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
four_re1 = visual.TextStim(win=win, name='four_re1',
    text='1',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
four_re2 = visual.TextStim(win=win, name='four_re2',
    text='8',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
four_re3 = visual.TextStim(win=win, name='four_re3',
    text='3',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
four_re4 = visual.TextStim(win=win, name='four_re4',
    text='3',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
four_re_input = visual.TextStim(win=win, name='four_re_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
four_re_tip = visual.TextStim(win=win, name='four_re_tip',
    text='请倒序输入呈现的数字\n（回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "five_re"
five_reClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
five_re_concentration = visual.TextStim(win=win, name='five_re_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
five_re1 = visual.TextStim(win=win, name='five_re1',
    text='6',
    font='Open Sans',
    pos=(-0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
five_re2 = visual.TextStim(win=win, name='five_re2',
    text='3',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
five_re3 = visual.TextStim(win=win, name='five_re3',
    text='1',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
five_re4 = visual.TextStim(win=win, name='five_re4',
    text='5',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
five_re5 = visual.TextStim(win=win, name='five_re5',
    text='2',
    font='Open Sans',
    pos=(0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
five_re_input = visual.TextStim(win=win, name='five_re_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
five_re_tip = visual.TextStim(win=win, name='five_re_tip',
    text='请倒序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "six_re"
six_reClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
six_re_concentration = visual.TextStim(win=win, name='six_re_concentration',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
six_re1 = visual.TextStim(win=win, name='six_re1',
    text='8',
    font='Open Sans',
    pos=(-0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
six_re2 = visual.TextStim(win=win, name='six_re2',
    text='7',
    font='Open Sans',
    pos=(-0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
six_re3 = visual.TextStim(win=win, name='six_re3',
    text='4',
    font='Open Sans',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
six_re4 = visual.TextStim(win=win, name='six_re4',
    text='2',
    font='Open Sans',
    pos=(0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
six_re5 = visual.TextStim(win=win, name='six_re5',
    text='4',
    font='Open Sans',
    pos=(0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
six_re6 = visual.TextStim(win=win, name='six_re6',
    text='8',
    font='Open Sans',
    pos=(0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
six_re_input = visual.TextStim(win=win, name='six_re_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
six_re_tip = visual.TextStim(win=win, name='six_re_tip',
    text='请倒序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "seven_re"
seven_reClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
seven_re_concentration = visual.TextStim(win=win, name='seven_re_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
seven_re1 = visual.TextStim(win=win, name='seven_re1',
    text='7',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
seven_re2 = visual.TextStim(win=win, name='seven_re2',
    text='5',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
seven_re3 = visual.TextStim(win=win, name='seven_re3',
    text='9',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
seven_re4 = visual.TextStim(win=win, name='seven_re4',
    text='3',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
seven_re5 = visual.TextStim(win=win, name='seven_re5',
    text='4',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
seven_re6 = visual.TextStim(win=win, name='seven_re6',
    text='0',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
seven_re7 = visual.TextStim(win=win, name='seven_re7',
    text='4',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
seven_re_input = visual.TextStim(win=win, name='seven_re_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
seven_re_tip = visual.TextStim(win=win, name='seven_re_tip',
    text='请倒序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "eight_re"
eight_reClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
eight_re_concentration = visual.TextStim(win=win, name='eight_re_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
eight_re1 = visual.TextStim(win=win, name='eight_re1',
    text='4',
    font='Open Sans',
    pos=(-0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
eight_re2 = visual.TextStim(win=win, name='eight_re2',
    text='1',
    font='Open Sans',
    pos=(-0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
eight_re3 = visual.TextStim(win=win, name='eight_re3',
    text='3',
    font='Open Sans',
    pos=(-0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
eight_re4 = visual.TextStim(win=win, name='eight_re4',
    text='5',
    font='Open Sans',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
eight_re5 = visual.TextStim(win=win, name='eight_re5',
    text='9',
    font='Open Sans',
    pos=(0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
eight_re6 = visual.TextStim(win=win, name='eight_re6',
    text='3',
    font='Open Sans',
    pos=(0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
eight_re7 = visual.TextStim(win=win, name='eight_re7',
    text='2',
    font='Open Sans',
    pos=(0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
eight_re8 = visual.TextStim(win=win, name='eight_re8',
    text='8',
    font='Open Sans',
    pos=(0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
eight_re_input = visual.TextStim(win=win, name='eight_re_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
eight_re_tip = visual.TextStim(win=win, name='eight_re_tip',
    text='请倒序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "nine_re"
nine_reClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
nine_re_concentration = visual.TextStim(win=win, name='nine_re_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
nine_re1 = visual.TextStim(win=win, name='nine_re1',
    text='8',
    font='Open Sans',
    pos=(-0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
nine_re2 = visual.TextStim(win=win, name='nine_re2',
    text='6',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
nine_re3 = visual.TextStim(win=win, name='nine_re3',
    text='8',
    font='Open Sans',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
nine_re4 = visual.TextStim(win=win, name='nine_re4',
    text='2',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
nine_re5 = visual.TextStim(win=win, name='nine_re5',
    text='4',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
nine_re6 = visual.TextStim(win=win, name='nine_re6',
    text='3',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
nine_re7 = visual.TextStim(win=win, name='nine_re7',
    text='5',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
nine_re8 = visual.TextStim(win=win, name='nine_re8',
    text='2',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
nine_re9 = visual.TextStim(win=win, name='nine_re9',
    text='1',
    font='Open Sans',
    pos=(0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
nine_re_input = visual.TextStim(win=win, name='nine_re_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
nine_re_tip = visual.TextStim(win=win, name='nine_re_tip',
    text='请倒序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "ten_re"
ten_reClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ten_re_concentration = visual.TextStim(win=win, name='ten_re_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ten_re1 = visual.TextStim(win=win, name='ten_re1',
    text='6',
    font='Open Sans',
    pos=(-0.45, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ten_re2 = visual.TextStim(win=win, name='ten_re2',
    text='0',
    font='Open Sans',
    pos=(-0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ten_re3 = visual.TextStim(win=win, name='ten_re3',
    text='3',
    font='Open Sans',
    pos=(-0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ten_re4 = visual.TextStim(win=win, name='ten_re4',
    text='8',
    font='Open Sans',
    pos=(-0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
ten_re5 = visual.TextStim(win=win, name='ten_re5',
    text='2',
    font='Open Sans',
    pos=(-0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
ten_re6 = visual.TextStim(win=win, name='ten_re6',
    text='8',
    font='Open Sans',
    pos=(0.05, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
ten_re7 = visual.TextStim(win=win, name='ten_re7',
    text='3',
    font='Open Sans',
    pos=(0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
ten_re8 = visual.TextStim(win=win, name='ten_re8',
    text='7',
    font='Open Sans',
    pos=(0.25, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
ten_re9 = visual.TextStim(win=win, name='ten_re9',
    text='5',
    font='Open Sans',
    pos=(0.35, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
ten_re10 = visual.TextStim(win=win, name='ten_re10',
    text='6',
    font='Open Sans',
    pos=(0.45, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
ten_re_input = visual.TextStim(win=win, name='ten_re_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
ten_re_tip = visual.TextStim(win=win, name='ten_re_tip',
    text='请倒序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "eleven_re"
eleven_reClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='下一道题目',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
eleven_re_concentration = visual.TextStim(win=win, name='eleven_re_concentration',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
eleven_re1 = visual.TextStim(win=win, name='eleven_re1',
    text='9',
    font='Open Sans',
    pos=(-0.5, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
eleven_re2 = visual.TextStim(win=win, name='eleven_re2',
    text='6',
    font='Open Sans',
    pos=(-0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
eleven_re3 = visual.TextStim(win=win, name='eleven_re3',
    text='5',
    font='Open Sans',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
eleven_re4 = visual.TextStim(win=win, name='eleven_re4',
    text='6',
    font='Open Sans',
    pos=(-0.15, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
eleven_re5 = visual.TextStim(win=win, name='eleven_re5',
    text='8',
    font='Open Sans',
    pos=(-0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
eleven_re6 = visual.TextStim(win=win, name='eleven_re6',
    text='9',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
eleven_re7 = visual.TextStim(win=win, name='eleven_re7',
    text='6',
    font='Open Sans',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
eleven_re8 = visual.TextStim(win=win, name='eleven_re8',
    text='8',
    font='Open Sans',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
eleven_re9 = visual.TextStim(win=win, name='eleven_re9',
    text='0',
    font='Open Sans',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
eleven_re10 = visual.TextStim(win=win, name='eleven_re10',
    text='4',
    font='Open Sans',
    pos=(0.4, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
eleven_re11 = visual.TextStim(win=win, name='eleven_re11',
    text='2',
    font='Open Sans',
    pos=(0.5, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
eleven_re_input = visual.TextStim(win=win, name='eleven_re_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
eleven_re_tip = visual.TextStim(win=win, name='eleven_re_tip',
    text='请倒序输入呈现的数字\n  （回车键结束）',
    font='Open Sans',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);

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
        four_input.setText(textFill)
        win.flip()
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
                            win.flip()
                    else: 
                        thisExp.addData('four_corr', 0)
                        thisExp.addData('result', 0)
                        textFill = ''
                        four_input.setText(textFill)
                        win.flip()
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
        five_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    fiveComponents = [text, concentration_five, five_1, five_2, five_3, five_4, five_5, five_input, five_tip]
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
            if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *concentration_five* updates
        if concentration_five.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
        if five_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
        if five_2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
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
        if five_3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
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
        if five_4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
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
        if five_5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
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
        if five_input.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            five_input.frameNStart = frameN  # exact frame index
            five_input.tStart = t  # local t and not account for scr refresh
            five_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_input, 'tStartRefresh')  # time at next scr refresh
            five_input.setAutoDraw(True)
        
        # *five_tip* updates
        if five_tip.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
                            win.flip()
                    else: 
                        thisExp.addData('five_corr', 0)
                        over = 1
                        button -= 1
                        textFill = ''
                        five_input.setText(textFill)
                        win.flip()
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
    if button ==6:
        textFill = ''
        six_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    sixComponents = [text_2, concentration_six, six_1, six_2, six_3, six_4, six_5, six_6, six_input, six_tip]
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
            if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *concentration_six* updates
        if concentration_six.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
        if six_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
        if six_2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
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
        if six_3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
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
        if six_4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
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
        if six_5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
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
        if six_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        if six_input.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            six_input.frameNStart = frameN  # exact frame index
            six_input.tStart = t  # local t and not account for scr refresh
            six_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_input, 'tStartRefresh')  # time at next scr refresh
            six_input.setAutoDraw(True)
        
        # *six_tip* updates
        if six_tip.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
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
                            textFill = ''
                            six_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('six_corr', 0)
                        over = 1
                        button -= 1
                        textFill = ''
                        six_input.setText(textFill)
                        win.flip()
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
    
    # ------Prepare to start Routine "seven"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button == 7:
        textFill = ''
        seven_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    sevenComponents = [text_3, concentration_seven, seven_1, seven_2, seven_3, seven_4, seven_5, seven_6, seven_7, seven_input, seven_tip]
    for thisComponent in sevenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sevenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "seven"-------
    while continueRoutine:
        # get current time
        t = sevenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sevenClock)
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
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *concentration_seven* updates
        if concentration_seven.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
        if seven_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
        if seven_2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
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
        if seven_3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
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
        if seven_4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
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
        if seven_5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
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
        if seven_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        if seven_7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
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
        if seven_input.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
            # keep track of start time/frame for later
            seven_input.frameNStart = frameN  # exact frame index
            seven_input.tStart = t  # local t and not account for scr refresh
            seven_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_input, 'tStartRefresh')  # time at next scr refresh
            seven_input.setAutoDraw(True)
        
        # *seven_tip* updates
        if seven_tip.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
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
                        if over == 1:
                            loop_or.finished = True
                            button -= 1
                            thisExp.addData('result', button)
                            textFill = ''
                            seven_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('seven_corr', 0)
                        over = 1
                        button -= 1
                        textFill = ''
                        seven_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sevenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "seven"-------
    for thisComponent in sevenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "seven" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "eight"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button == 8:
        textFill = ''
        eight_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    eightComponents = [text_4, eight_concentration, eight_1, eight_2, eight_3, eight_4, eight_5, eight_6, eight_7, eight_8, eight_input, eight_tip]
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
            if tThisFlipGlobal > text_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *eight_concentration* updates
        if eight_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
        if eight_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
        if eight_2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
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
        if eight_3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
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
        if eight_4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
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
        if eight_5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
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
        if eight_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        if eight_7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
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
        if eight_8.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
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
        if eight_input.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
            # keep track of start time/frame for later
            eight_input.frameNStart = frameN  # exact frame index
            eight_input.tStart = t  # local t and not account for scr refresh
            eight_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_input, 'tStartRefresh')  # time at next scr refresh
            eight_input.setAutoDraw(True)
        
        # *eight_tip* updates
        if eight_tip.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
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
                        if over == 1:
                            loop_or.finished = True
                            button -= 1
                            thisExp.addData('result', button)
                            textFill = ''
                            eight_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('eight_corr', 0)
                        over = 1
                        button -= 1
                        textFill = ''
                        eight_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
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
        nine_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    nineComponents = [text_5, nine_concentration, nine_1, nine_2, nine_3, nine_4, nine_5, nine_6, nine_7, nine_8, nine_9, nine_input, nine_tip]
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
            if tThisFlipGlobal > text_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # *nine_concentration* updates
        if nine_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
        if nine_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
        if nine_2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
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
        if nine_3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
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
        if nine_4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
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
        if nine_5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
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
        if nine_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        if nine_7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
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
        if nine_8.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
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
        if nine_9.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
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
        if nine_input.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
            # keep track of start time/frame for later
            nine_input.frameNStart = frameN  # exact frame index
            nine_input.tStart = t  # local t and not account for scr refresh
            nine_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_input, 'tStartRefresh')  # time at next scr refresh
            nine_input.setAutoDraw(True)
        
        # *nine_tip* updates
        if nine_tip.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
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
                    if textFill == '43789786':
                        thisExp.addData('nine_corr', 1)
                        button += 1
                        if over == 1:
                            loop_or.finished = True
                            button -= 1
                            thisExp.addData('result', button)
                            textFill = ''
                            nine_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('nine_corr', 0)
                        over = 1
                        button -= 1
                        textFill = ''
                        nine_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
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
    
    # ------Prepare to start Routine "ten"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button == 10:
        textFill = ''
        ten_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    tenComponents = [text_6, ten_concentration, ten_1, ten_2, ten_3, ten_4, ten_5, ten_6, ten_7, ten_8, ten_9, ten_10, ten_input, ten_tip]
    for thisComponent in tenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    tenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ten"-------
    while continueRoutine:
        # get current time
        t = tenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=tenClock)
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
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # *ten_concentration* updates
        if ten_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ten_concentration.frameNStart = frameN  # exact frame index
            ten_concentration.tStart = t  # local t and not account for scr refresh
            ten_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_concentration, 'tStartRefresh')  # time at next scr refresh
            ten_concentration.setAutoDraw(True)
        if ten_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ten_concentration.tStop = t  # not accounting for scr refresh
                ten_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_concentration, 'tStopRefresh')  # time at next scr refresh
                ten_concentration.setAutoDraw(False)
        
        # *ten_1* updates
        if ten_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            ten_1.frameNStart = frameN  # exact frame index
            ten_1.tStart = t  # local t and not account for scr refresh
            ten_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_1, 'tStartRefresh')  # time at next scr refresh
            ten_1.setAutoDraw(True)
        if ten_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_1.tStop = t  # not accounting for scr refresh
                ten_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_1, 'tStopRefresh')  # time at next scr refresh
                ten_1.setAutoDraw(False)
        
        # *ten_2* updates
        if ten_2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            ten_2.frameNStart = frameN  # exact frame index
            ten_2.tStart = t  # local t and not account for scr refresh
            ten_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_2, 'tStartRefresh')  # time at next scr refresh
            ten_2.setAutoDraw(True)
        if ten_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_2.tStop = t  # not accounting for scr refresh
                ten_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_2, 'tStopRefresh')  # time at next scr refresh
                ten_2.setAutoDraw(False)
        
        # *ten_3* updates
        if ten_3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            ten_3.frameNStart = frameN  # exact frame index
            ten_3.tStart = t  # local t and not account for scr refresh
            ten_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_3, 'tStartRefresh')  # time at next scr refresh
            ten_3.setAutoDraw(True)
        if ten_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_3.tStop = t  # not accounting for scr refresh
                ten_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_3, 'tStopRefresh')  # time at next scr refresh
                ten_3.setAutoDraw(False)
        
        # *ten_4* updates
        if ten_4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
            # keep track of start time/frame for later
            ten_4.frameNStart = frameN  # exact frame index
            ten_4.tStart = t  # local t and not account for scr refresh
            ten_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_4, 'tStartRefresh')  # time at next scr refresh
            ten_4.setAutoDraw(True)
        if ten_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_4.tStop = t  # not accounting for scr refresh
                ten_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_4, 'tStopRefresh')  # time at next scr refresh
                ten_4.setAutoDraw(False)
        
        # *ten_5* updates
        if ten_5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            ten_5.frameNStart = frameN  # exact frame index
            ten_5.tStart = t  # local t and not account for scr refresh
            ten_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_5, 'tStartRefresh')  # time at next scr refresh
            ten_5.setAutoDraw(True)
        if ten_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_5.tStop = t  # not accounting for scr refresh
                ten_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_5, 'tStopRefresh')  # time at next scr refresh
                ten_5.setAutoDraw(False)
        
        # *ten_6* updates
        if ten_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            ten_6.frameNStart = frameN  # exact frame index
            ten_6.tStart = t  # local t and not account for scr refresh
            ten_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_6, 'tStartRefresh')  # time at next scr refresh
            ten_6.setAutoDraw(True)
        if ten_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_6.tStop = t  # not accounting for scr refresh
                ten_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_6, 'tStopRefresh')  # time at next scr refresh
                ten_6.setAutoDraw(False)
        
        # *ten_7* updates
        if ten_7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            ten_7.frameNStart = frameN  # exact frame index
            ten_7.tStart = t  # local t and not account for scr refresh
            ten_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_7, 'tStartRefresh')  # time at next scr refresh
            ten_7.setAutoDraw(True)
        if ten_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_7.tStop = t  # not accounting for scr refresh
                ten_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_7, 'tStopRefresh')  # time at next scr refresh
                ten_7.setAutoDraw(False)
        
        # *ten_8* updates
        if ten_8.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
            # keep track of start time/frame for later
            ten_8.frameNStart = frameN  # exact frame index
            ten_8.tStart = t  # local t and not account for scr refresh
            ten_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_8, 'tStartRefresh')  # time at next scr refresh
            ten_8.setAutoDraw(True)
        if ten_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_8.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_8.tStop = t  # not accounting for scr refresh
                ten_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_8, 'tStopRefresh')  # time at next scr refresh
                ten_8.setAutoDraw(False)
        
        # *ten_9* updates
        if ten_9.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
            # keep track of start time/frame for later
            ten_9.frameNStart = frameN  # exact frame index
            ten_9.tStart = t  # local t and not account for scr refresh
            ten_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_9, 'tStartRefresh')  # time at next scr refresh
            ten_9.setAutoDraw(True)
        if ten_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_9.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_9.tStop = t  # not accounting for scr refresh
                ten_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_9, 'tStopRefresh')  # time at next scr refresh
                ten_9.setAutoDraw(False)
        
        # *ten_10* updates
        if ten_10.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
            # keep track of start time/frame for later
            ten_10.frameNStart = frameN  # exact frame index
            ten_10.tStart = t  # local t and not account for scr refresh
            ten_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_10, 'tStartRefresh')  # time at next scr refresh
            ten_10.setAutoDraw(True)
        if ten_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_10.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_10.tStop = t  # not accounting for scr refresh
                ten_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_10, 'tStopRefresh')  # time at next scr refresh
                ten_10.setAutoDraw(False)
        
        # *ten_input* updates
        if ten_input.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            ten_input.frameNStart = frameN  # exact frame index
            ten_input.tStart = t  # local t and not account for scr refresh
            ten_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_input, 'tStartRefresh')  # time at next scr refresh
            ten_input.setAutoDraw(True)
        
        # *ten_tip* updates
        if ten_tip.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            ten_tip.frameNStart = frameN  # exact frame index
            ten_tip.tStart = t  # local t and not account for scr refresh
            ten_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_tip, 'tStartRefresh')  # time at next scr refresh
            ten_tip.setAutoDraw(True)
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
                ten_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('ten', textFill)
                    if textFill == '43789786':
                        thisExp.addData('ten_corr', 1)
                        button += 1
                        if over == 1:
                            loop_or.finished = True
                            button -= 1
                            thisExp.addData('result', button)
                            textFill = ''
                            ten_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('ten_corr', 0)
                        over = 1
                        button -= 1
                        textFill = ''
                        ten_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ten"-------
    for thisComponent in tenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ten" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "eleven"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button == 11:
        textFill = ''
        eleven_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    elevenComponents = [text_7, eleven_concentration, eleven_1, eleven_2, eleven_3, eleven_4, eleven_5, eleven_6, eleven_7, eleven_8, eleven_9, eleven_10, eleven_11, eleven_input, eleven_tip]
    for thisComponent in elevenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    elevenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "eleven"-------
    while continueRoutine:
        # get current time
        t = elevenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=elevenClock)
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
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # *eleven_concentration* updates
        if eleven_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            eleven_concentration.frameNStart = frameN  # exact frame index
            eleven_concentration.tStart = t  # local t and not account for scr refresh
            eleven_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_concentration, 'tStartRefresh')  # time at next scr refresh
            eleven_concentration.setAutoDraw(True)
        if eleven_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                eleven_concentration.tStop = t  # not accounting for scr refresh
                eleven_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_concentration, 'tStopRefresh')  # time at next scr refresh
                eleven_concentration.setAutoDraw(False)
        
        # *eleven_1* updates
        if eleven_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            eleven_1.frameNStart = frameN  # exact frame index
            eleven_1.tStart = t  # local t and not account for scr refresh
            eleven_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_1, 'tStartRefresh')  # time at next scr refresh
            eleven_1.setAutoDraw(True)
        if eleven_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_1.tStop = t  # not accounting for scr refresh
                eleven_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_1, 'tStopRefresh')  # time at next scr refresh
                eleven_1.setAutoDraw(False)
        
        # *eleven_2* updates
        if eleven_2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            eleven_2.frameNStart = frameN  # exact frame index
            eleven_2.tStart = t  # local t and not account for scr refresh
            eleven_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_2, 'tStartRefresh')  # time at next scr refresh
            eleven_2.setAutoDraw(True)
        if eleven_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_2.tStop = t  # not accounting for scr refresh
                eleven_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_2, 'tStopRefresh')  # time at next scr refresh
                eleven_2.setAutoDraw(False)
        
        # *eleven_3* updates
        if eleven_3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            eleven_3.frameNStart = frameN  # exact frame index
            eleven_3.tStart = t  # local t and not account for scr refresh
            eleven_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_3, 'tStartRefresh')  # time at next scr refresh
            eleven_3.setAutoDraw(True)
        if eleven_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_3.tStop = t  # not accounting for scr refresh
                eleven_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_3, 'tStopRefresh')  # time at next scr refresh
                eleven_3.setAutoDraw(False)
        
        # *eleven_4* updates
        if eleven_4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
            # keep track of start time/frame for later
            eleven_4.frameNStart = frameN  # exact frame index
            eleven_4.tStart = t  # local t and not account for scr refresh
            eleven_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_4, 'tStartRefresh')  # time at next scr refresh
            eleven_4.setAutoDraw(True)
        if eleven_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_4.tStop = t  # not accounting for scr refresh
                eleven_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_4, 'tStopRefresh')  # time at next scr refresh
                eleven_4.setAutoDraw(False)
        
        # *eleven_5* updates
        if eleven_5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            eleven_5.frameNStart = frameN  # exact frame index
            eleven_5.tStart = t  # local t and not account for scr refresh
            eleven_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_5, 'tStartRefresh')  # time at next scr refresh
            eleven_5.setAutoDraw(True)
        if eleven_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_5.tStop = t  # not accounting for scr refresh
                eleven_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_5, 'tStopRefresh')  # time at next scr refresh
                eleven_5.setAutoDraw(False)
        
        # *eleven_6* updates
        if eleven_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            eleven_6.frameNStart = frameN  # exact frame index
            eleven_6.tStart = t  # local t and not account for scr refresh
            eleven_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_6, 'tStartRefresh')  # time at next scr refresh
            eleven_6.setAutoDraw(True)
        if eleven_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_6.tStop = t  # not accounting for scr refresh
                eleven_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_6, 'tStopRefresh')  # time at next scr refresh
                eleven_6.setAutoDraw(False)
        
        # *eleven_7* updates
        if eleven_7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            eleven_7.frameNStart = frameN  # exact frame index
            eleven_7.tStart = t  # local t and not account for scr refresh
            eleven_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_7, 'tStartRefresh')  # time at next scr refresh
            eleven_7.setAutoDraw(True)
        if eleven_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_7.tStop = t  # not accounting for scr refresh
                eleven_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_7, 'tStopRefresh')  # time at next scr refresh
                eleven_7.setAutoDraw(False)
        
        # *eleven_8* updates
        if eleven_8.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
            # keep track of start time/frame for later
            eleven_8.frameNStart = frameN  # exact frame index
            eleven_8.tStart = t  # local t and not account for scr refresh
            eleven_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_8, 'tStartRefresh')  # time at next scr refresh
            eleven_8.setAutoDraw(True)
        if eleven_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_8.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_8.tStop = t  # not accounting for scr refresh
                eleven_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_8, 'tStopRefresh')  # time at next scr refresh
                eleven_8.setAutoDraw(False)
        
        # *eleven_9* updates
        if eleven_9.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
            # keep track of start time/frame for later
            eleven_9.frameNStart = frameN  # exact frame index
            eleven_9.tStart = t  # local t and not account for scr refresh
            eleven_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_9, 'tStartRefresh')  # time at next scr refresh
            eleven_9.setAutoDraw(True)
        if eleven_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_9.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_9.tStop = t  # not accounting for scr refresh
                eleven_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_9, 'tStopRefresh')  # time at next scr refresh
                eleven_9.setAutoDraw(False)
        
        # *eleven_10* updates
        if eleven_10.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
            # keep track of start time/frame for later
            eleven_10.frameNStart = frameN  # exact frame index
            eleven_10.tStart = t  # local t and not account for scr refresh
            eleven_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_10, 'tStartRefresh')  # time at next scr refresh
            eleven_10.setAutoDraw(True)
        if eleven_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_10.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_10.tStop = t  # not accounting for scr refresh
                eleven_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_10, 'tStopRefresh')  # time at next scr refresh
                eleven_10.setAutoDraw(False)
        
        # *eleven_11* updates
        if eleven_11.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            eleven_11.frameNStart = frameN  # exact frame index
            eleven_11.tStart = t  # local t and not account for scr refresh
            eleven_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_11, 'tStartRefresh')  # time at next scr refresh
            eleven_11.setAutoDraw(True)
        if eleven_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_11.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_11.tStop = t  # not accounting for scr refresh
                eleven_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_11, 'tStopRefresh')  # time at next scr refresh
                eleven_11.setAutoDraw(False)
        
        # *eleven_input* updates
        if eleven_input.status == NOT_STARTED and tThisFlip >= 4.3-frameTolerance:
            # keep track of start time/frame for later
            eleven_input.frameNStart = frameN  # exact frame index
            eleven_input.tStart = t  # local t and not account for scr refresh
            eleven_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_input, 'tStartRefresh')  # time at next scr refresh
            eleven_input.setAutoDraw(True)
        
        # *eleven_tip* updates
        if eleven_tip.status == NOT_STARTED and tThisFlip >= 4.3-frameTolerance:
            # keep track of start time/frame for later
            eleven_tip.frameNStart = frameN  # exact frame index
            eleven_tip.tStart = t  # local t and not account for scr refresh
            eleven_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_tip, 'tStartRefresh')  # time at next scr refresh
            eleven_tip.setAutoDraw(True)
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
                eleven_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('eleven', textFill)
                    if textFill == '60284096335':
                        thisExp.addData('eleven_corr', 1)
                        button += 1
                        thisExp.addData('result', 11)
                        loop_or.finished = True
                        if over == 1:
                            loop_or.finished = True
                            button -= 1
                            thisExp.addData('result', button)
                            textFill = ''
                            eleven_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('eleven_corr', 0)
                        over = 1
                        button -= 1
                        textFill = ''
                        eleven_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in elevenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "eleven"-------
    for thisComponent in elevenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "eleven" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 7.0 repeats of 'loop_or'


# set up handler to look after randomisation of conditions etc
loop_re = data.TrialHandler(nReps=7.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_re')
thisExp.addLoop(loop_re)  # add the loop to the experiment
thisLoop_re = loop_re.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_re.rgb)
if thisLoop_re != None:
    for paramName in thisLoop_re:
        exec('{} = thisLoop_re[paramName]'.format(paramName))

for thisLoop_re in loop_re:
    currentLoop = loop_re
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_re.rgb)
    if thisLoop_re != None:
        for paramName in thisLoop_re:
            exec('{} = thisLoop_re[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "four_re"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button_re == 4:
        textFill = ''
        four_re_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    four_reComponents = [four_re_concentration, four_re1, four_re2, four_re3, four_re4, four_re_input, four_re_tip]
    for thisComponent in four_reComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    four_reClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "four_re"-------
    while continueRoutine:
        # get current time
        t = four_reClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=four_reClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *four_re_concentration* updates
        if four_re_concentration.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            four_re_concentration.frameNStart = frameN  # exact frame index
            four_re_concentration.tStart = t  # local t and not account for scr refresh
            four_re_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_re_concentration, 'tStartRefresh')  # time at next scr refresh
            four_re_concentration.setAutoDraw(True)
        if four_re_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four_re_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                four_re_concentration.tStop = t  # not accounting for scr refresh
                four_re_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four_re_concentration, 'tStopRefresh')  # time at next scr refresh
                four_re_concentration.setAutoDraw(False)
        
        # *four_re1* updates
        if four_re1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            four_re1.frameNStart = frameN  # exact frame index
            four_re1.tStart = t  # local t and not account for scr refresh
            four_re1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_re1, 'tStartRefresh')  # time at next scr refresh
            four_re1.setAutoDraw(True)
        if four_re1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four_re1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                four_re1.tStop = t  # not accounting for scr refresh
                four_re1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four_re1, 'tStopRefresh')  # time at next scr refresh
                four_re1.setAutoDraw(False)
        
        # *four_re2* updates
        if four_re2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            four_re2.frameNStart = frameN  # exact frame index
            four_re2.tStart = t  # local t and not account for scr refresh
            four_re2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_re2, 'tStartRefresh')  # time at next scr refresh
            four_re2.setAutoDraw(True)
        if four_re2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four_re2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                four_re2.tStop = t  # not accounting for scr refresh
                four_re2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four_re2, 'tStopRefresh')  # time at next scr refresh
                four_re2.setAutoDraw(False)
        
        # *four_re3* updates
        if four_re3.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            four_re3.frameNStart = frameN  # exact frame index
            four_re3.tStart = t  # local t and not account for scr refresh
            four_re3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_re3, 'tStartRefresh')  # time at next scr refresh
            four_re3.setAutoDraw(True)
        if four_re3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four_re3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                four_re3.tStop = t  # not accounting for scr refresh
                four_re3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four_re3, 'tStopRefresh')  # time at next scr refresh
                four_re3.setAutoDraw(False)
        
        # *four_re4* updates
        if four_re4.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
            # keep track of start time/frame for later
            four_re4.frameNStart = frameN  # exact frame index
            four_re4.tStart = t  # local t and not account for scr refresh
            four_re4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_re4, 'tStartRefresh')  # time at next scr refresh
            four_re4.setAutoDraw(True)
        if four_re4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four_re4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                four_re4.tStop = t  # not accounting for scr refresh
                four_re4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four_re4, 'tStopRefresh')  # time at next scr refresh
                four_re4.setAutoDraw(False)
        
        # *four_re_input* updates
        if four_re_input.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            four_re_input.frameNStart = frameN  # exact frame index
            four_re_input.tStart = t  # local t and not account for scr refresh
            four_re_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_re_input, 'tStartRefresh')  # time at next scr refresh
            four_re_input.setAutoDraw(True)
        
        # *four_re_tip* updates
        if four_re_tip.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            four_re_tip.frameNStart = frameN  # exact frame index
            four_re_tip.tStart = t  # local t and not account for scr refresh
            four_re_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_re_tip, 'tStartRefresh')  # time at next scr refresh
            four_re_tip.setAutoDraw(True)
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
                four_re_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('four_re', textFill)
                    if int(textFill) == 3381:
                        thisExp.addData('four_re_corr', 1)
                        button_re += 1
                        if over_re == 1:
                            loop_re.finished = True
                            button_re -= 1
                            thisExp.addData('result_re', button_re)
                            textFill = ''
                            four_re_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('four_re_corr', 0)
                        thisExp.addData('result_re', 0)
                        textFill = ''
                        four_re_input.setText(textFill)
                        win.flip()
                        loop_re.finished = True
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in four_reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "four_re"-------
    for thisComponent in four_reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "four_re" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "five_re"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button_re == 5:
        textFill = ''
        five_re_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    five_reComponents = [text_8, five_re_concentration, five_re1, five_re2, five_re3, five_re4, five_re5, five_re_input, five_re_tip]
    for thisComponent in five_reComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    five_reClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "five_re"-------
    while continueRoutine:
        # get current time
        t = five_reClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=five_reClock)
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
        
        # *five_re_concentration* updates
        if five_re_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            five_re_concentration.frameNStart = frameN  # exact frame index
            five_re_concentration.tStart = t  # local t and not account for scr refresh
            five_re_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_re_concentration, 'tStartRefresh')  # time at next scr refresh
            five_re_concentration.setAutoDraw(True)
        if five_re_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_re_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                five_re_concentration.tStop = t  # not accounting for scr refresh
                five_re_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_re_concentration, 'tStopRefresh')  # time at next scr refresh
                five_re_concentration.setAutoDraw(False)
        
        # *five_re1* updates
        if five_re1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            five_re1.frameNStart = frameN  # exact frame index
            five_re1.tStart = t  # local t and not account for scr refresh
            five_re1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_re1, 'tStartRefresh')  # time at next scr refresh
            five_re1.setAutoDraw(True)
        if five_re1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_re1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_re1.tStop = t  # not accounting for scr refresh
                five_re1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_re1, 'tStopRefresh')  # time at next scr refresh
                five_re1.setAutoDraw(False)
        
        # *five_re2* updates
        if five_re2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            five_re2.frameNStart = frameN  # exact frame index
            five_re2.tStart = t  # local t and not account for scr refresh
            five_re2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_re2, 'tStartRefresh')  # time at next scr refresh
            five_re2.setAutoDraw(True)
        if five_re2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_re2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_re2.tStop = t  # not accounting for scr refresh
                five_re2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_re2, 'tStopRefresh')  # time at next scr refresh
                five_re2.setAutoDraw(False)
        
        # *five_re3* updates
        if five_re3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            five_re3.frameNStart = frameN  # exact frame index
            five_re3.tStart = t  # local t and not account for scr refresh
            five_re3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_re3, 'tStartRefresh')  # time at next scr refresh
            five_re3.setAutoDraw(True)
        if five_re3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_re3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_re3.tStop = t  # not accounting for scr refresh
                five_re3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_re3, 'tStopRefresh')  # time at next scr refresh
                five_re3.setAutoDraw(False)
        
        # *five_re4* updates
        if five_re4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
            # keep track of start time/frame for later
            five_re4.frameNStart = frameN  # exact frame index
            five_re4.tStart = t  # local t and not account for scr refresh
            five_re4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_re4, 'tStartRefresh')  # time at next scr refresh
            five_re4.setAutoDraw(True)
        if five_re4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_re4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_re4.tStop = t  # not accounting for scr refresh
                five_re4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_re4, 'tStopRefresh')  # time at next scr refresh
                five_re4.setAutoDraw(False)
        
        # *five_re5* updates
        if five_re5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            five_re5.frameNStart = frameN  # exact frame index
            five_re5.tStart = t  # local t and not account for scr refresh
            five_re5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_re5, 'tStartRefresh')  # time at next scr refresh
            five_re5.setAutoDraw(True)
        if five_re5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_re5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                five_re5.tStop = t  # not accounting for scr refresh
                five_re5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_re5, 'tStopRefresh')  # time at next scr refresh
                five_re5.setAutoDraw(False)
        
        # *five_re_input* updates
        if five_re_input.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            five_re_input.frameNStart = frameN  # exact frame index
            five_re_input.tStart = t  # local t and not account for scr refresh
            five_re_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_re_input, 'tStartRefresh')  # time at next scr refresh
            five_re_input.setAutoDraw(True)
        
        # *five_re_tip* updates
        if five_re_tip.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            five_re_tip.frameNStart = frameN  # exact frame index
            five_re_tip.tStart = t  # local t and not account for scr refresh
            five_re_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_re_tip, 'tStartRefresh')  # time at next scr refresh
            five_re_tip.setAutoDraw(True)
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
                five_re_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('five_re', textFill)
                    if textFill == '25136':
                        thisExp.addData('five_re_corr', 1)
                        button_re += 1
                        if over_re == 1:
                            loop_re.finished = True
                            button -= 1
                            thisExp.addData('result_re', button)
                            textFill = ''
                            five_re_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('five_re_corr', 0)
                        over_re = 1
                        button_re -= 1
                        textFill = ''
                        five_re_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in five_reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "five_re"-------
    for thisComponent in five_reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "five_re" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "six_re"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button_re == 6:
        textFill = ''
        six_re_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    six_reComponents = [text_9, six_re_concentration, six_re1, six_re2, six_re3, six_re4, six_re5, six_re6, six_re_input, six_re_tip]
    for thisComponent in six_reComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    six_reClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "six_re"-------
    while continueRoutine:
        # get current time
        t = six_reClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=six_reClock)
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
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # *six_re_concentration* updates
        if six_re_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            six_re_concentration.frameNStart = frameN  # exact frame index
            six_re_concentration.tStart = t  # local t and not account for scr refresh
            six_re_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_re_concentration, 'tStartRefresh')  # time at next scr refresh
            six_re_concentration.setAutoDraw(True)
        if six_re_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_re_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                six_re_concentration.tStop = t  # not accounting for scr refresh
                six_re_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_re_concentration, 'tStopRefresh')  # time at next scr refresh
                six_re_concentration.setAutoDraw(False)
        
        # *six_re1* updates
        if six_re1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            six_re1.frameNStart = frameN  # exact frame index
            six_re1.tStart = t  # local t and not account for scr refresh
            six_re1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_re1, 'tStartRefresh')  # time at next scr refresh
            six_re1.setAutoDraw(True)
        if six_re1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_re1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_re1.tStop = t  # not accounting for scr refresh
                six_re1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_re1, 'tStopRefresh')  # time at next scr refresh
                six_re1.setAutoDraw(False)
        
        # *six_re2* updates
        if six_re2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            six_re2.frameNStart = frameN  # exact frame index
            six_re2.tStart = t  # local t and not account for scr refresh
            six_re2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_re2, 'tStartRefresh')  # time at next scr refresh
            six_re2.setAutoDraw(True)
        if six_re2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_re2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_re2.tStop = t  # not accounting for scr refresh
                six_re2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_re2, 'tStopRefresh')  # time at next scr refresh
                six_re2.setAutoDraw(False)
        
        # *six_re3* updates
        if six_re3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            six_re3.frameNStart = frameN  # exact frame index
            six_re3.tStart = t  # local t and not account for scr refresh
            six_re3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_re3, 'tStartRefresh')  # time at next scr refresh
            six_re3.setAutoDraw(True)
        if six_re3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_re3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_re3.tStop = t  # not accounting for scr refresh
                six_re3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_re3, 'tStopRefresh')  # time at next scr refresh
                six_re3.setAutoDraw(False)
        
        # *six_re4* updates
        if six_re4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
            # keep track of start time/frame for later
            six_re4.frameNStart = frameN  # exact frame index
            six_re4.tStart = t  # local t and not account for scr refresh
            six_re4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_re4, 'tStartRefresh')  # time at next scr refresh
            six_re4.setAutoDraw(True)
        if six_re4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_re4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_re4.tStop = t  # not accounting for scr refresh
                six_re4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_re4, 'tStopRefresh')  # time at next scr refresh
                six_re4.setAutoDraw(False)
        
        # *six_re5* updates
        if six_re5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            six_re5.frameNStart = frameN  # exact frame index
            six_re5.tStart = t  # local t and not account for scr refresh
            six_re5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_re5, 'tStartRefresh')  # time at next scr refresh
            six_re5.setAutoDraw(True)
        if six_re5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_re5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_re5.tStop = t  # not accounting for scr refresh
                six_re5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_re5, 'tStopRefresh')  # time at next scr refresh
                six_re5.setAutoDraw(False)
        
        # *six_re6* updates
        if six_re6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            six_re6.frameNStart = frameN  # exact frame index
            six_re6.tStart = t  # local t and not account for scr refresh
            six_re6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_re6, 'tStartRefresh')  # time at next scr refresh
            six_re6.setAutoDraw(True)
        if six_re6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_re6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                six_re6.tStop = t  # not accounting for scr refresh
                six_re6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_re6, 'tStopRefresh')  # time at next scr refresh
                six_re6.setAutoDraw(False)
        
        # *six_re_input* updates
        if six_re_input.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            six_re_input.frameNStart = frameN  # exact frame index
            six_re_input.tStart = t  # local t and not account for scr refresh
            six_re_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_re_input, 'tStartRefresh')  # time at next scr refresh
            six_re_input.setAutoDraw(True)
        
        # *six_re_tip* updates
        if six_re_tip.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            six_re_tip.frameNStart = frameN  # exact frame index
            six_re_tip.tStart = t  # local t and not account for scr refresh
            six_re_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_re_tip, 'tStartRefresh')  # time at next scr refresh
            six_re_tip.setAutoDraw(True)
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
                six_re_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('six_re', textFill)
                    if textFill == '842478':
                        thisExp.addData('six_re_corr', 1)
                        button_re += 1
                        if over_re == 1:
                            loop_re.finished = True
                            button_re -= 1
                            thisExp.addData('result_re', button_re)
                            textFill = ''
                            six_re_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('six_re_corr', 0)
                        over_re = 1
                        button_re -= 1
                        textFill = ''
                        six_re_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
                    
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in six_reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "six_re"-------
    for thisComponent in six_reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_re.addData('six_re_concentration.started', six_re_concentration.tStartRefresh)
    loop_re.addData('six_re_concentration.stopped', six_re_concentration.tStopRefresh)
    loop_re.addData('six_re_input.started', six_re_input.tStartRefresh)
    loop_re.addData('six_re_input.stopped', six_re_input.tStopRefresh)
    # the Routine "six_re" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "seven_re"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button_re == 7:
        textFill = ''
        seven_re_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    seven_reComponents = [text_10, seven_re_concentration, seven_re1, seven_re2, seven_re3, seven_re4, seven_re5, seven_re6, seven_re7, seven_re_input, seven_re_tip]
    for thisComponent in seven_reComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    seven_reClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "seven_re"-------
    while continueRoutine:
        # get current time
        t = seven_reClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=seven_reClock)
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
            if tThisFlipGlobal > text_10.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                text_10.setAutoDraw(False)
        
        # *seven_re_concentration* updates
        if seven_re_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            seven_re_concentration.frameNStart = frameN  # exact frame index
            seven_re_concentration.tStart = t  # local t and not account for scr refresh
            seven_re_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re_concentration, 'tStartRefresh')  # time at next scr refresh
            seven_re_concentration.setAutoDraw(True)
        if seven_re_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_re_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                seven_re_concentration.tStop = t  # not accounting for scr refresh
                seven_re_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_re_concentration, 'tStopRefresh')  # time at next scr refresh
                seven_re_concentration.setAutoDraw(False)
        
        # *seven_re1* updates
        if seven_re1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            seven_re1.frameNStart = frameN  # exact frame index
            seven_re1.tStart = t  # local t and not account for scr refresh
            seven_re1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re1, 'tStartRefresh')  # time at next scr refresh
            seven_re1.setAutoDraw(True)
        if seven_re1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_re1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_re1.tStop = t  # not accounting for scr refresh
                seven_re1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_re1, 'tStopRefresh')  # time at next scr refresh
                seven_re1.setAutoDraw(False)
        
        # *seven_re2* updates
        if seven_re2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            seven_re2.frameNStart = frameN  # exact frame index
            seven_re2.tStart = t  # local t and not account for scr refresh
            seven_re2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re2, 'tStartRefresh')  # time at next scr refresh
            seven_re2.setAutoDraw(True)
        if seven_re2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_re2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_re2.tStop = t  # not accounting for scr refresh
                seven_re2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_re2, 'tStopRefresh')  # time at next scr refresh
                seven_re2.setAutoDraw(False)
        
        # *seven_re3* updates
        if seven_re3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            seven_re3.frameNStart = frameN  # exact frame index
            seven_re3.tStart = t  # local t and not account for scr refresh
            seven_re3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re3, 'tStartRefresh')  # time at next scr refresh
            seven_re3.setAutoDraw(True)
        if seven_re3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_re3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_re3.tStop = t  # not accounting for scr refresh
                seven_re3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_re3, 'tStopRefresh')  # time at next scr refresh
                seven_re3.setAutoDraw(False)
        
        # *seven_re4* updates
        if seven_re4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
            # keep track of start time/frame for later
            seven_re4.frameNStart = frameN  # exact frame index
            seven_re4.tStart = t  # local t and not account for scr refresh
            seven_re4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re4, 'tStartRefresh')  # time at next scr refresh
            seven_re4.setAutoDraw(True)
        if seven_re4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_re4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_re4.tStop = t  # not accounting for scr refresh
                seven_re4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_re4, 'tStopRefresh')  # time at next scr refresh
                seven_re4.setAutoDraw(False)
        
        # *seven_re5* updates
        if seven_re5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            seven_re5.frameNStart = frameN  # exact frame index
            seven_re5.tStart = t  # local t and not account for scr refresh
            seven_re5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re5, 'tStartRefresh')  # time at next scr refresh
            seven_re5.setAutoDraw(True)
        if seven_re5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_re5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_re5.tStop = t  # not accounting for scr refresh
                seven_re5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_re5, 'tStopRefresh')  # time at next scr refresh
                seven_re5.setAutoDraw(False)
        
        # *seven_re6* updates
        if seven_re6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            seven_re6.frameNStart = frameN  # exact frame index
            seven_re6.tStart = t  # local t and not account for scr refresh
            seven_re6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re6, 'tStartRefresh')  # time at next scr refresh
            seven_re6.setAutoDraw(True)
        if seven_re6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_re6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_re6.tStop = t  # not accounting for scr refresh
                seven_re6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_re6, 'tStopRefresh')  # time at next scr refresh
                seven_re6.setAutoDraw(False)
        
        # *seven_re7* updates
        if seven_re7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            seven_re7.frameNStart = frameN  # exact frame index
            seven_re7.tStart = t  # local t and not account for scr refresh
            seven_re7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re7, 'tStartRefresh')  # time at next scr refresh
            seven_re7.setAutoDraw(True)
        if seven_re7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_re7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                seven_re7.tStop = t  # not accounting for scr refresh
                seven_re7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_re7, 'tStopRefresh')  # time at next scr refresh
                seven_re7.setAutoDraw(False)
        
        # *seven_re_input* updates
        if seven_re_input.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
            # keep track of start time/frame for later
            seven_re_input.frameNStart = frameN  # exact frame index
            seven_re_input.tStart = t  # local t and not account for scr refresh
            seven_re_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re_input, 'tStartRefresh')  # time at next scr refresh
            seven_re_input.setAutoDraw(True)
        
        # *seven_re_tip* updates
        if seven_re_tip.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
            # keep track of start time/frame for later
            seven_re_tip.frameNStart = frameN  # exact frame index
            seven_re_tip.tStart = t  # local t and not account for scr refresh
            seven_re_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_re_tip, 'tStartRefresh')  # time at next scr refresh
            seven_re_tip.setAutoDraw(True)
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
                seven_re_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('seven_re', textFill)
                    if textFill == '4043957':
                        thisExp.addData('seven_re_corr', 1)
                        button_re += 1
                        if over == 1:
                            loop_re.finished = True
                            button_re -= 1
                            thisExp.addData('result_re', button_re)
                            textFill = ''
                            seven_re_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('seven_re_corr', 0)
                        over = 1
                        button_re -= 1
                        textFill = ''
                        seven_re_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in seven_reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "seven_re"-------
    for thisComponent in seven_reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_re.addData('seven_re_concentration.started', seven_re_concentration.tStartRefresh)
    loop_re.addData('seven_re_concentration.stopped', seven_re_concentration.tStopRefresh)
    # the Routine "seven_re" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "eight_re"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button_re == 8:
        textFill = ''
        eight_re_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    eight_reComponents = [text_11, eight_re_concentration, eight_re1, eight_re2, eight_re3, eight_re4, eight_re5, eight_re6, eight_re7, eight_re8, eight_re_input, eight_re_tip]
    for thisComponent in eight_reComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    eight_reClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "eight_re"-------
    while continueRoutine:
        # get current time
        t = eight_reClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=eight_reClock)
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
        if text_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_11.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_11.tStop = t  # not accounting for scr refresh
                text_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                text_11.setAutoDraw(False)
        
        # *eight_re_concentration* updates
        if eight_re_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            eight_re_concentration.frameNStart = frameN  # exact frame index
            eight_re_concentration.tStart = t  # local t and not account for scr refresh
            eight_re_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re_concentration, 'tStartRefresh')  # time at next scr refresh
            eight_re_concentration.setAutoDraw(True)
        if eight_re_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_re_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                eight_re_concentration.tStop = t  # not accounting for scr refresh
                eight_re_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_re_concentration, 'tStopRefresh')  # time at next scr refresh
                eight_re_concentration.setAutoDraw(False)
        
        # *eight_re1* updates
        if eight_re1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            eight_re1.frameNStart = frameN  # exact frame index
            eight_re1.tStart = t  # local t and not account for scr refresh
            eight_re1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re1, 'tStartRefresh')  # time at next scr refresh
            eight_re1.setAutoDraw(True)
        if eight_re1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_re1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_re1.tStop = t  # not accounting for scr refresh
                eight_re1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_re1, 'tStopRefresh')  # time at next scr refresh
                eight_re1.setAutoDraw(False)
        
        # *eight_re2* updates
        if eight_re2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            eight_re2.frameNStart = frameN  # exact frame index
            eight_re2.tStart = t  # local t and not account for scr refresh
            eight_re2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re2, 'tStartRefresh')  # time at next scr refresh
            eight_re2.setAutoDraw(True)
        if eight_re2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_re2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_re2.tStop = t  # not accounting for scr refresh
                eight_re2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_re2, 'tStopRefresh')  # time at next scr refresh
                eight_re2.setAutoDraw(False)
        
        # *eight_re3* updates
        if eight_re3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            eight_re3.frameNStart = frameN  # exact frame index
            eight_re3.tStart = t  # local t and not account for scr refresh
            eight_re3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re3, 'tStartRefresh')  # time at next scr refresh
            eight_re3.setAutoDraw(True)
        if eight_re3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_re3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_re3.tStop = t  # not accounting for scr refresh
                eight_re3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_re3, 'tStopRefresh')  # time at next scr refresh
                eight_re3.setAutoDraw(False)
        
        # *eight_re4* updates
        if eight_re4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
            # keep track of start time/frame for later
            eight_re4.frameNStart = frameN  # exact frame index
            eight_re4.tStart = t  # local t and not account for scr refresh
            eight_re4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re4, 'tStartRefresh')  # time at next scr refresh
            eight_re4.setAutoDraw(True)
        if eight_re4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_re4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_re4.tStop = t  # not accounting for scr refresh
                eight_re4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_re4, 'tStopRefresh')  # time at next scr refresh
                eight_re4.setAutoDraw(False)
        
        # *eight_re5* updates
        if eight_re5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            eight_re5.frameNStart = frameN  # exact frame index
            eight_re5.tStart = t  # local t and not account for scr refresh
            eight_re5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re5, 'tStartRefresh')  # time at next scr refresh
            eight_re5.setAutoDraw(True)
        if eight_re5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_re5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_re5.tStop = t  # not accounting for scr refresh
                eight_re5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_re5, 'tStopRefresh')  # time at next scr refresh
                eight_re5.setAutoDraw(False)
        
        # *eight_re6* updates
        if eight_re6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            eight_re6.frameNStart = frameN  # exact frame index
            eight_re6.tStart = t  # local t and not account for scr refresh
            eight_re6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re6, 'tStartRefresh')  # time at next scr refresh
            eight_re6.setAutoDraw(True)
        if eight_re6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_re6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_re6.tStop = t  # not accounting for scr refresh
                eight_re6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_re6, 'tStopRefresh')  # time at next scr refresh
                eight_re6.setAutoDraw(False)
        
        # *eight_re7* updates
        if eight_re7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            eight_re7.frameNStart = frameN  # exact frame index
            eight_re7.tStart = t  # local t and not account for scr refresh
            eight_re7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re7, 'tStartRefresh')  # time at next scr refresh
            eight_re7.setAutoDraw(True)
        if eight_re7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_re7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_re7.tStop = t  # not accounting for scr refresh
                eight_re7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_re7, 'tStopRefresh')  # time at next scr refresh
                eight_re7.setAutoDraw(False)
        
        # *eight_re8* updates
        if eight_re8.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
            # keep track of start time/frame for later
            eight_re8.frameNStart = frameN  # exact frame index
            eight_re8.tStart = t  # local t and not account for scr refresh
            eight_re8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re8, 'tStartRefresh')  # time at next scr refresh
            eight_re8.setAutoDraw(True)
        if eight_re8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_re8.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eight_re8.tStop = t  # not accounting for scr refresh
                eight_re8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_re8, 'tStopRefresh')  # time at next scr refresh
                eight_re8.setAutoDraw(False)
        
        # *eight_re_input* updates
        if eight_re_input.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
            # keep track of start time/frame for later
            eight_re_input.frameNStart = frameN  # exact frame index
            eight_re_input.tStart = t  # local t and not account for scr refresh
            eight_re_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re_input, 'tStartRefresh')  # time at next scr refresh
            eight_re_input.setAutoDraw(True)
        
        # *eight_re_tip* updates
        if eight_re_tip.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
            # keep track of start time/frame for later
            eight_re_tip.frameNStart = frameN  # exact frame index
            eight_re_tip.tStart = t  # local t and not account for scr refresh
            eight_re_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_re_tip, 'tStartRefresh')  # time at next scr refresh
            eight_re_tip.setAutoDraw(True)
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
                eight_re_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('eight_re', textFill)
                    if textFill == '82395314':
                        thisExp.addData('eight_re_corr', 1)
                        button_re += 1
                        if over == 1:
                            loop_re.finished = True
                            button_re -= 1
                            thisExp.addData('result_re', button_re)
                            textFill = ''
                            eight_re_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('eight_re_corr', 0)
                        over = 1
                        button_re -= 1
                        textFill = ''
                        eight_re_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eight_reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "eight_re"-------
    for thisComponent in eight_reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_re.addData('eight_re_concentration.started', eight_re_concentration.tStartRefresh)
    loop_re.addData('eight_re_concentration.stopped', eight_re_concentration.tStopRefresh)
    # the Routine "eight_re" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "nine_re"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button_re == 9:
        textFill = ''
        nine_re_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    nine_reComponents = [text_12, nine_re_concentration, nine_re1, nine_re2, nine_re3, nine_re4, nine_re5, nine_re6, nine_re7, nine_re8, nine_re9, nine_re_input, nine_re_tip]
    for thisComponent in nine_reComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    nine_reClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "nine_re"-------
    while continueRoutine:
        # get current time
        t = nine_reClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=nine_reClock)
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
        if text_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_12.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_12.tStop = t  # not accounting for scr refresh
                text_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                text_12.setAutoDraw(False)
        
        # *nine_re_concentration* updates
        if nine_re_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            nine_re_concentration.frameNStart = frameN  # exact frame index
            nine_re_concentration.tStart = t  # local t and not account for scr refresh
            nine_re_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re_concentration, 'tStartRefresh')  # time at next scr refresh
            nine_re_concentration.setAutoDraw(True)
        if nine_re_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                nine_re_concentration.tStop = t  # not accounting for scr refresh
                nine_re_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re_concentration, 'tStopRefresh')  # time at next scr refresh
                nine_re_concentration.setAutoDraw(False)
        
        # *nine_re1* updates
        if nine_re1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            nine_re1.frameNStart = frameN  # exact frame index
            nine_re1.tStart = t  # local t and not account for scr refresh
            nine_re1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re1, 'tStartRefresh')  # time at next scr refresh
            nine_re1.setAutoDraw(True)
        if nine_re1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_re1.tStop = t  # not accounting for scr refresh
                nine_re1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re1, 'tStopRefresh')  # time at next scr refresh
                nine_re1.setAutoDraw(False)
        
        # *nine_re2* updates
        if nine_re2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            nine_re2.frameNStart = frameN  # exact frame index
            nine_re2.tStart = t  # local t and not account for scr refresh
            nine_re2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re2, 'tStartRefresh')  # time at next scr refresh
            nine_re2.setAutoDraw(True)
        if nine_re2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_re2.tStop = t  # not accounting for scr refresh
                nine_re2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re2, 'tStopRefresh')  # time at next scr refresh
                nine_re2.setAutoDraw(False)
        
        # *nine_re3* updates
        if nine_re3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            nine_re3.frameNStart = frameN  # exact frame index
            nine_re3.tStart = t  # local t and not account for scr refresh
            nine_re3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re3, 'tStartRefresh')  # time at next scr refresh
            nine_re3.setAutoDraw(True)
        if nine_re3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_re3.tStop = t  # not accounting for scr refresh
                nine_re3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re3, 'tStopRefresh')  # time at next scr refresh
                nine_re3.setAutoDraw(False)
        
        # *nine_re4* updates
        if nine_re4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
            # keep track of start time/frame for later
            nine_re4.frameNStart = frameN  # exact frame index
            nine_re4.tStart = t  # local t and not account for scr refresh
            nine_re4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re4, 'tStartRefresh')  # time at next scr refresh
            nine_re4.setAutoDraw(True)
        if nine_re4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_re4.tStop = t  # not accounting for scr refresh
                nine_re4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re4, 'tStopRefresh')  # time at next scr refresh
                nine_re4.setAutoDraw(False)
        
        # *nine_re5* updates
        if nine_re5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            nine_re5.frameNStart = frameN  # exact frame index
            nine_re5.tStart = t  # local t and not account for scr refresh
            nine_re5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re5, 'tStartRefresh')  # time at next scr refresh
            nine_re5.setAutoDraw(True)
        if nine_re5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_re5.tStop = t  # not accounting for scr refresh
                nine_re5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re5, 'tStopRefresh')  # time at next scr refresh
                nine_re5.setAutoDraw(False)
        
        # *nine_re6* updates
        if nine_re6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            nine_re6.frameNStart = frameN  # exact frame index
            nine_re6.tStart = t  # local t and not account for scr refresh
            nine_re6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re6, 'tStartRefresh')  # time at next scr refresh
            nine_re6.setAutoDraw(True)
        if nine_re6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_re6.tStop = t  # not accounting for scr refresh
                nine_re6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re6, 'tStopRefresh')  # time at next scr refresh
                nine_re6.setAutoDraw(False)
        
        # *nine_re7* updates
        if nine_re7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            nine_re7.frameNStart = frameN  # exact frame index
            nine_re7.tStart = t  # local t and not account for scr refresh
            nine_re7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re7, 'tStartRefresh')  # time at next scr refresh
            nine_re7.setAutoDraw(True)
        if nine_re7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_re7.tStop = t  # not accounting for scr refresh
                nine_re7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re7, 'tStopRefresh')  # time at next scr refresh
                nine_re7.setAutoDraw(False)
        
        # *nine_re8* updates
        if nine_re8.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
            # keep track of start time/frame for later
            nine_re8.frameNStart = frameN  # exact frame index
            nine_re8.tStart = t  # local t and not account for scr refresh
            nine_re8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re8, 'tStartRefresh')  # time at next scr refresh
            nine_re8.setAutoDraw(True)
        if nine_re8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re8.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_re8.tStop = t  # not accounting for scr refresh
                nine_re8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re8, 'tStopRefresh')  # time at next scr refresh
                nine_re8.setAutoDraw(False)
        
        # *nine_re9* updates
        if nine_re9.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
            # keep track of start time/frame for later
            nine_re9.frameNStart = frameN  # exact frame index
            nine_re9.tStart = t  # local t and not account for scr refresh
            nine_re9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re9, 'tStartRefresh')  # time at next scr refresh
            nine_re9.setAutoDraw(True)
        if nine_re9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_re9.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                nine_re9.tStop = t  # not accounting for scr refresh
                nine_re9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_re9, 'tStopRefresh')  # time at next scr refresh
                nine_re9.setAutoDraw(False)
        
        # *nine_re_input* updates
        if nine_re_input.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
            # keep track of start time/frame for later
            nine_re_input.frameNStart = frameN  # exact frame index
            nine_re_input.tStart = t  # local t and not account for scr refresh
            nine_re_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re_input, 'tStartRefresh')  # time at next scr refresh
            nine_re_input.setAutoDraw(True)
        
        # *nine_re_tip* updates
        if nine_re_tip.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
            # keep track of start time/frame for later
            nine_re_tip.frameNStart = frameN  # exact frame index
            nine_re_tip.tStart = t  # local t and not account for scr refresh
            nine_re_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_re_tip, 'tStartRefresh')  # time at next scr refresh
            nine_re_tip.setAutoDraw(True)
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
                nine_re_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('nine_re', textFill)
                    if textFill == '34613':
                        thisExp.addData('nine_re_corr', 1)
                        button_re_re += 1
                        if over == 1:
                            loop_re.finished = True
                            button_re -= 1
                            thisExp.addData('result_re', button_re)
                            textFill = ''
                            nine_re_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('nine_re_corr', 0)
                        over = 1
                        button_re -= 1
                        textFill = ''
                        nine_re_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nine_reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nine_re"-------
    for thisComponent in nine_reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_re.addData('nine_re4.started', nine_re4.tStartRefresh)
    loop_re.addData('nine_re4.stopped', nine_re4.tStopRefresh)
    loop_re.addData('nine_re_input.started', nine_re_input.tStartRefresh)
    loop_re.addData('nine_re_input.stopped', nine_re_input.tStopRefresh)
    # the Routine "nine_re" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ten_re"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button_re == 10:
        textFill = ''
        ten_re_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    ten_reComponents = [text_13, ten_re_concentration, ten_re1, ten_re2, ten_re3, ten_re4, ten_re5, ten_re6, ten_re7, ten_re8, ten_re9, ten_re10, ten_re_input, ten_re_tip]
    for thisComponent in ten_reComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ten_reClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ten_re"-------
    while continueRoutine:
        # get current time
        t = ten_reClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ten_reClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        if text_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_13.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_13.tStop = t  # not accounting for scr refresh
                text_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
                text_13.setAutoDraw(False)
        
        # *ten_re_concentration* updates
        if ten_re_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ten_re_concentration.frameNStart = frameN  # exact frame index
            ten_re_concentration.tStart = t  # local t and not account for scr refresh
            ten_re_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re_concentration, 'tStartRefresh')  # time at next scr refresh
            ten_re_concentration.setAutoDraw(True)
        if ten_re_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ten_re_concentration.tStop = t  # not accounting for scr refresh
                ten_re_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re_concentration, 'tStopRefresh')  # time at next scr refresh
                ten_re_concentration.setAutoDraw(False)
        
        # *ten_re1* updates
        if ten_re1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            ten_re1.frameNStart = frameN  # exact frame index
            ten_re1.tStart = t  # local t and not account for scr refresh
            ten_re1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re1, 'tStartRefresh')  # time at next scr refresh
            ten_re1.setAutoDraw(True)
        if ten_re1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re1.tStop = t  # not accounting for scr refresh
                ten_re1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re1, 'tStopRefresh')  # time at next scr refresh
                ten_re1.setAutoDraw(False)
        
        # *ten_re2* updates
        if ten_re2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            ten_re2.frameNStart = frameN  # exact frame index
            ten_re2.tStart = t  # local t and not account for scr refresh
            ten_re2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re2, 'tStartRefresh')  # time at next scr refresh
            ten_re2.setAutoDraw(True)
        if ten_re2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re2.tStop = t  # not accounting for scr refresh
                ten_re2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re2, 'tStopRefresh')  # time at next scr refresh
                ten_re2.setAutoDraw(False)
        
        # *ten_re3* updates
        if ten_re3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            ten_re3.frameNStart = frameN  # exact frame index
            ten_re3.tStart = t  # local t and not account for scr refresh
            ten_re3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re3, 'tStartRefresh')  # time at next scr refresh
            ten_re3.setAutoDraw(True)
        if ten_re3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re3.tStop = t  # not accounting for scr refresh
                ten_re3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re3, 'tStopRefresh')  # time at next scr refresh
                ten_re3.setAutoDraw(False)
        
        # *ten_re4* updates
        if ten_re4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
            # keep track of start time/frame for later
            ten_re4.frameNStart = frameN  # exact frame index
            ten_re4.tStart = t  # local t and not account for scr refresh
            ten_re4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re4, 'tStartRefresh')  # time at next scr refresh
            ten_re4.setAutoDraw(True)
        if ten_re4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re4.tStop = t  # not accounting for scr refresh
                ten_re4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re4, 'tStopRefresh')  # time at next scr refresh
                ten_re4.setAutoDraw(False)
        
        # *ten_re5* updates
        if ten_re5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            ten_re5.frameNStart = frameN  # exact frame index
            ten_re5.tStart = t  # local t and not account for scr refresh
            ten_re5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re5, 'tStartRefresh')  # time at next scr refresh
            ten_re5.setAutoDraw(True)
        if ten_re5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re5.tStop = t  # not accounting for scr refresh
                ten_re5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re5, 'tStopRefresh')  # time at next scr refresh
                ten_re5.setAutoDraw(False)
        
        # *ten_re6* updates
        if ten_re6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            ten_re6.frameNStart = frameN  # exact frame index
            ten_re6.tStart = t  # local t and not account for scr refresh
            ten_re6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re6, 'tStartRefresh')  # time at next scr refresh
            ten_re6.setAutoDraw(True)
        if ten_re6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re6.tStop = t  # not accounting for scr refresh
                ten_re6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re6, 'tStopRefresh')  # time at next scr refresh
                ten_re6.setAutoDraw(False)
        
        # *ten_re7* updates
        if ten_re7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            ten_re7.frameNStart = frameN  # exact frame index
            ten_re7.tStart = t  # local t and not account for scr refresh
            ten_re7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re7, 'tStartRefresh')  # time at next scr refresh
            ten_re7.setAutoDraw(True)
        if ten_re7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re7.tStop = t  # not accounting for scr refresh
                ten_re7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re7, 'tStopRefresh')  # time at next scr refresh
                ten_re7.setAutoDraw(False)
        
        # *ten_re8* updates
        if ten_re8.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
            # keep track of start time/frame for later
            ten_re8.frameNStart = frameN  # exact frame index
            ten_re8.tStart = t  # local t and not account for scr refresh
            ten_re8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re8, 'tStartRefresh')  # time at next scr refresh
            ten_re8.setAutoDraw(True)
        if ten_re8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re8.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re8.tStop = t  # not accounting for scr refresh
                ten_re8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re8, 'tStopRefresh')  # time at next scr refresh
                ten_re8.setAutoDraw(False)
        
        # *ten_re9* updates
        if ten_re9.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
            # keep track of start time/frame for later
            ten_re9.frameNStart = frameN  # exact frame index
            ten_re9.tStart = t  # local t and not account for scr refresh
            ten_re9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re9, 'tStartRefresh')  # time at next scr refresh
            ten_re9.setAutoDraw(True)
        if ten_re9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re9.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re9.tStop = t  # not accounting for scr refresh
                ten_re9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re9, 'tStopRefresh')  # time at next scr refresh
                ten_re9.setAutoDraw(False)
        
        # *ten_re10* updates
        if ten_re10.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
            # keep track of start time/frame for later
            ten_re10.frameNStart = frameN  # exact frame index
            ten_re10.tStart = t  # local t and not account for scr refresh
            ten_re10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re10, 'tStartRefresh')  # time at next scr refresh
            ten_re10.setAutoDraw(True)
        if ten_re10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_re10.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ten_re10.tStop = t  # not accounting for scr refresh
                ten_re10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_re10, 'tStopRefresh')  # time at next scr refresh
                ten_re10.setAutoDraw(False)
        
        # *ten_re_input* updates
        if ten_re_input.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            ten_re_input.frameNStart = frameN  # exact frame index
            ten_re_input.tStart = t  # local t and not account for scr refresh
            ten_re_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re_input, 'tStartRefresh')  # time at next scr refresh
            ten_re_input.setAutoDraw(True)
        
        # *ten_re_tip* updates
        if ten_re_tip.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            ten_re_tip.frameNStart = frameN  # exact frame index
            ten_re_tip.tStart = t  # local t and not account for scr refresh
            ten_re_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_re_tip, 'tStartRefresh')  # time at next scr refresh
            ten_re_tip.setAutoDraw(True)
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
                ten_re_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('ten_re', textFill)
                    if textFill == '6573828306':
                        thisExp.addData('ten_re_corr', 1)
                        button_re_re += 1
                        if over == 1:
                            loop_re.finished = True
                            button_re -= 1
                            thisExp.addData('result_re', button_re)
                            textFill = ''
                            ten_re_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('ten_re_corr', 0)
                        over = 1
                        button_re -= 1
                        textFill = ''
                        ten_re_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ten_reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ten_re"-------
    for thisComponent in ten_reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_re.addData('ten_re_concentration.started', ten_re_concentration.tStartRefresh)
    loop_re.addData('ten_re_concentration.stopped', ten_re_concentration.tStopRefresh)
    # the Routine "ten_re" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "eleven_re"-------
    continueRoutine = True
    # update component parameters for each repeat
    if button_re == 11:
        textFill = ''
        eleven_re_input.setText(textFill)
        win.flip()
    else:
        continueRoutine = False
    # keep track of which components have finished
    eleven_reComponents = [text_14, eleven_re_concentration, eleven_re1, eleven_re2, eleven_re3, eleven_re4, eleven_re5, eleven_re6, eleven_re7, eleven_re8, eleven_re9, eleven_re10, eleven_re11, eleven_re_input, eleven_re_tip]
    for thisComponent in eleven_reComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    eleven_reClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "eleven_re"-------
    while continueRoutine:
        # get current time
        t = eleven_reClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=eleven_reClock)
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
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        
        # *eleven_re_concentration* updates
        if eleven_re_concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            eleven_re_concentration.frameNStart = frameN  # exact frame index
            eleven_re_concentration.tStart = t  # local t and not account for scr refresh
            eleven_re_concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re_concentration, 'tStartRefresh')  # time at next scr refresh
            eleven_re_concentration.setAutoDraw(True)
        if eleven_re_concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re_concentration.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re_concentration.tStop = t  # not accounting for scr refresh
                eleven_re_concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re_concentration, 'tStopRefresh')  # time at next scr refresh
                eleven_re_concentration.setAutoDraw(False)
        
        # *eleven_re1* updates
        if eleven_re1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            eleven_re1.frameNStart = frameN  # exact frame index
            eleven_re1.tStart = t  # local t and not account for scr refresh
            eleven_re1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re1, 'tStartRefresh')  # time at next scr refresh
            eleven_re1.setAutoDraw(True)
        if eleven_re1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re1.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re1.tStop = t  # not accounting for scr refresh
                eleven_re1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re1, 'tStopRefresh')  # time at next scr refresh
                eleven_re1.setAutoDraw(False)
        
        # *eleven_re2* updates
        if eleven_re2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            eleven_re2.frameNStart = frameN  # exact frame index
            eleven_re2.tStart = t  # local t and not account for scr refresh
            eleven_re2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re2, 'tStartRefresh')  # time at next scr refresh
            eleven_re2.setAutoDraw(True)
        if eleven_re2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re2.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re2.tStop = t  # not accounting for scr refresh
                eleven_re2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re2, 'tStopRefresh')  # time at next scr refresh
                eleven_re2.setAutoDraw(False)
        
        # *eleven_re3* updates
        if eleven_re3.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            eleven_re3.frameNStart = frameN  # exact frame index
            eleven_re3.tStart = t  # local t and not account for scr refresh
            eleven_re3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re3, 'tStartRefresh')  # time at next scr refresh
            eleven_re3.setAutoDraw(True)
        if eleven_re3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re3.tStop = t  # not accounting for scr refresh
                eleven_re3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re3, 'tStopRefresh')  # time at next scr refresh
                eleven_re3.setAutoDraw(False)
        
        # *eleven_re4* updates
        if eleven_re4.status == NOT_STARTED and tThisFlip >= 1.9-frameTolerance:
            # keep track of start time/frame for later
            eleven_re4.frameNStart = frameN  # exact frame index
            eleven_re4.tStart = t  # local t and not account for scr refresh
            eleven_re4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re4, 'tStartRefresh')  # time at next scr refresh
            eleven_re4.setAutoDraw(True)
        if eleven_re4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re4.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re4.tStop = t  # not accounting for scr refresh
                eleven_re4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re4, 'tStopRefresh')  # time at next scr refresh
                eleven_re4.setAutoDraw(False)
        
        # *eleven_re5* updates
        if eleven_re5.status == NOT_STARTED and tThisFlip >= 2.2-frameTolerance:
            # keep track of start time/frame for later
            eleven_re5.frameNStart = frameN  # exact frame index
            eleven_re5.tStart = t  # local t and not account for scr refresh
            eleven_re5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re5, 'tStartRefresh')  # time at next scr refresh
            eleven_re5.setAutoDraw(True)
        if eleven_re5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re5.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re5.tStop = t  # not accounting for scr refresh
                eleven_re5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re5, 'tStopRefresh')  # time at next scr refresh
                eleven_re5.setAutoDraw(False)
        
        # *eleven_re6* updates
        if eleven_re6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            eleven_re6.frameNStart = frameN  # exact frame index
            eleven_re6.tStart = t  # local t and not account for scr refresh
            eleven_re6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re6, 'tStartRefresh')  # time at next scr refresh
            eleven_re6.setAutoDraw(True)
        if eleven_re6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re6.tStop = t  # not accounting for scr refresh
                eleven_re6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re6, 'tStopRefresh')  # time at next scr refresh
                eleven_re6.setAutoDraw(False)
        
        # *eleven_re7* updates
        if eleven_re7.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            eleven_re7.frameNStart = frameN  # exact frame index
            eleven_re7.tStart = t  # local t and not account for scr refresh
            eleven_re7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re7, 'tStartRefresh')  # time at next scr refresh
            eleven_re7.setAutoDraw(True)
        if eleven_re7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re7.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re7.tStop = t  # not accounting for scr refresh
                eleven_re7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re7, 'tStopRefresh')  # time at next scr refresh
                eleven_re7.setAutoDraw(False)
        
        # *eleven_re8* updates
        if eleven_re8.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
            # keep track of start time/frame for later
            eleven_re8.frameNStart = frameN  # exact frame index
            eleven_re8.tStart = t  # local t and not account for scr refresh
            eleven_re8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re8, 'tStartRefresh')  # time at next scr refresh
            eleven_re8.setAutoDraw(True)
        if eleven_re8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re8.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re8.tStop = t  # not accounting for scr refresh
                eleven_re8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re8, 'tStopRefresh')  # time at next scr refresh
                eleven_re8.setAutoDraw(False)
        
        # *eleven_re9* updates
        if eleven_re9.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
            # keep track of start time/frame for later
            eleven_re9.frameNStart = frameN  # exact frame index
            eleven_re9.tStart = t  # local t and not account for scr refresh
            eleven_re9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re9, 'tStartRefresh')  # time at next scr refresh
            eleven_re9.setAutoDraw(True)
        if eleven_re9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re9.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re9.tStop = t  # not accounting for scr refresh
                eleven_re9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re9, 'tStopRefresh')  # time at next scr refresh
                eleven_re9.setAutoDraw(False)
        
        # *eleven_re10* updates
        if eleven_re10.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
            # keep track of start time/frame for later
            eleven_re10.frameNStart = frameN  # exact frame index
            eleven_re10.tStart = t  # local t and not account for scr refresh
            eleven_re10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re10, 'tStartRefresh')  # time at next scr refresh
            eleven_re10.setAutoDraw(True)
        if eleven_re10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re10.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re10.tStop = t  # not accounting for scr refresh
                eleven_re10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re10, 'tStopRefresh')  # time at next scr refresh
                eleven_re10.setAutoDraw(False)
        
        # *eleven_re11* updates
        if eleven_re11.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            eleven_re11.frameNStart = frameN  # exact frame index
            eleven_re11.tStart = t  # local t and not account for scr refresh
            eleven_re11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re11, 'tStartRefresh')  # time at next scr refresh
            eleven_re11.setAutoDraw(True)
        if eleven_re11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eleven_re11.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                eleven_re11.tStop = t  # not accounting for scr refresh
                eleven_re11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eleven_re11, 'tStopRefresh')  # time at next scr refresh
                eleven_re11.setAutoDraw(False)
        
        # *eleven_re_input* updates
        if eleven_re_input.status == NOT_STARTED and tThisFlip >= 4.3-frameTolerance:
            # keep track of start time/frame for later
            eleven_re_input.frameNStart = frameN  # exact frame index
            eleven_re_input.tStart = t  # local t and not account for scr refresh
            eleven_re_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re_input, 'tStartRefresh')  # time at next scr refresh
            eleven_re_input.setAutoDraw(True)
        
        # *eleven_re_tip* updates
        if eleven_re_tip.status == NOT_STARTED and tThisFlip >= 4.3-frameTolerance:
            # keep track of start time/frame for later
            eleven_re_tip.frameNStart = frameN  # exact frame index
            eleven_re_tip.tStart = t  # local t and not account for scr refresh
            eleven_re_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eleven_re_tip, 'tStartRefresh')  # time at next scr refresh
            eleven_re_tip.setAutoDraw(True)
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
                eleven_re_input.setText(textFill)  # Set new text on screen
                if keys[0] == 'return':
                    textFill.strip()
                    thisExp.addData('eleven_re', textFill)
                    if textFill == '24086986569':
                        thisExp.addData('eleven_re_corr', 1)
                        button_re_re += 1
                        thisExp.addData('result', 11)
                        loop_re.finished = True
                        if over == 1:
                            loop_re.finished = True
                            button_re -= 1
                            thisExp.addData('result_re', button_re)
                            textFill = ''
                            eleven_re_input.setText(textFill)
                            win.flip()
                    else: 
                        thisExp.addData('eleven_re_corr', 0)
                        over = 1
                        button_re -= 1
                        textFill = ''
                        eleven_re_input.setText(textFill)
                        win.flip()
                        continueRoutine = False
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eleven_reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "eleven_re"-------
    for thisComponent in eleven_reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "eleven_re" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 7.0 repeats of 'loop_re'


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
