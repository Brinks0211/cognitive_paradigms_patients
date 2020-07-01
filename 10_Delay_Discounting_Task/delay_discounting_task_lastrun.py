#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 六月 16, 2020, at 20:53
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
expName = 'Delay_Discounting_Task'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zhang\\Desktop\\张以昊\\课题组\\10_Delay_Discounting_Task\\delay_discounting_task_lastrun.py',
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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction1"
instruction1Clock = core.Clock()
text0_1 = visual.TextStim(win=win, name='text0_1',
    text='欢迎参加测试\n\n答案没有对错之分,希望你能仔细考虑,认真回答。\n\n（继续，请按空格键）\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp0_1 = keyboard.Keyboard()

# Initialize components for Routine "instruction2"
instruction2Clock = core.Clock()
text0_2 = visual.TextStim(win=win, name='text0_2',
    text='测试开始时,首先在屏幕中间会出现注视点“+“\n\n接着将成对出现两种大小不同\n并且给予时间不同的虚拟金币\n\n左边是立即可以得到的虚拟金币\n右边是需要等待一段时间才能得到的虚拟金币\n\n等待时间分一周、两周、一个月、\n六个月、一年、五年、二十五年\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp0_2 = keyboard.Keyboard()

# Initialize components for Routine "instruction3"
instruction3Clock = core.Clock()
text0_3 = visual.TextStim(win=win, name='text0_3',
    text='如果选择左侧的虚拟金币,请按键盘的左键,\n如果选择右侧的虚拟金币,请按键盘的右键。\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp0_3 = keyboard.Keyboard()

# Initialize components for Routine "instruction4"
instruction4Clock = core.Clock()
text0_4 = visual.TextStim(win=win, name='text0_4',
    text='在您做出选择之后，程序会反馈您的选择。\n测试结束后，这些虚拟金币最终会换成小礼物。\n\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_0_4 = keyboard.Keyboard()

# Initialize components for Routine "instruction5"
instruction5Clock = core.Clock()
text0_5 = visual.TextStim(win=win, name='text0_5',
    text='如果准备好了，请进入正式测试\n\n（继续，请按空格键）',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp0_5 = keyboard.Keyboard()

# Initialize components for Routine "tip1"
tip1Clock = core.Clock()
tip_1 = visual.TextStim(win=win, name='tip_1',
    text='（第一阶段）\n\n即时选择的奖赏\n对比\n                的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='延迟一周',
    font='Arial',
    pos=(-0.075, -0.085), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "choice_week_2"
choice_week_2Clock = core.Clock()
concentration1 = visual.TextStim(win=win, name='concentration1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_1_1 = visual.TextStim(win=win, name='text_1_1',
    text='即时选择的奖赏         延迟一周的奖赏\n',
    font='Arial',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_1_2 = visual.TextStim(win=win, name='text_1_2',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_1_3 = visual.TextStim(win=win, name='text_1_3',
    text='1000',
    font='Arial',
    pos=(0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_1week = keyboard.Keyboard()
x1=500
n1=4
z1=500
y=0

# Initialize components for Routine "feed_back1"
feed_back1Clock = core.Clock()
feedback1_1 = visual.TextStim(win=win, name='feedback1_1',
    text='default text',
    font='Arial',
    pos=(-0.1, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
feedback1_2 = visual.TextStim(win=win, name='feedback1_2',
    text='您的选择是',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedback1_3 = visual.TextStim(win=win, name='feedback1_3',
    text='default text',
    font='Arial',
    pos=(0.2, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "tip2"
tip2Clock = core.Clock()
tip_2 = visual.TextStim(win=win, name='tip_2',
    text='（第二阶段）\n\n即时选择的奖赏\n对比\n                的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='延迟两周',
    font='Arial',
    pos=(-0.075, -0.085), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "choice_2weeks"
choice_2weeksClock = core.Clock()
concentration6 = visual.TextStim(win=win, name='concentration6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text6_1 = visual.TextStim(win=win, name='text6_1',
    text='即时选择的奖赏         延迟两周的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text6_2 = visual.TextStim(win=win, name='text6_2',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text6_3 = visual.TextStim(win=win, name='text6_3',
    text='1000',
    font='Arial',
    pos=(0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_2weeks = keyboard.Keyboard()
x6=500
n6=4
z5=500

# Initialize components for Routine "feed_back5"
feed_back5Clock = core.Clock()
feedback5_1 = visual.TextStim(win=win, name='feedback5_1',
    text='default text',
    font='Arial',
    pos=(-0.1, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
feedback5_2 = visual.TextStim(win=win, name='feedback5_2',
    text='您的选择是',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedback5_3 = visual.TextStim(win=win, name='feedback5_3',
    text='default text',
    font='Arial',
    pos=(0.2, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "tip3"
tip3Clock = core.Clock()
tip_3 = visual.TextStim(win=win, name='tip_3',
    text='（第三阶段）\n\n即时选择的奖赏\n对比\n                的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='延迟一个月',
    font='Arial',
    pos=(-0.1, -0.085), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "choice_month"
choice_monthClock = core.Clock()
concentration3 = visual.TextStim(win=win, name='concentration3',
    text='+\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text3_1 = visual.TextStim(win=win, name='text3_1',
    text='即时选择的奖赏         延迟一月的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text3_2 = visual.TextStim(win=win, name='text3_2',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text3_3 = visual.TextStim(win=win, name='text3_3',
    text='1000',
    font='Arial',
    pos=(0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_1month = keyboard.Keyboard()
x3=500
n3=4
z2=500

# Initialize components for Routine "feed_back2"
feed_back2Clock = core.Clock()
feedback2_1 = visual.TextStim(win=win, name='feedback2_1',
    text='default text',
    font='Arial',
    pos=(-0.1, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
feedback2_2 = visual.TextStim(win=win, name='feedback2_2',
    text='您的选择是',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedback2_3 = visual.TextStim(win=win, name='feedback2_3',
    text='default text',
    font='Arial',
    pos=(0.2, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "tip4"
tip4Clock = core.Clock()
tip_4 = visual.TextStim(win=win, name='tip_4',
    text='（第四阶段）\n\n即时选择的奖赏\n对比\n                的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='延迟六个月',
    font='Arial',
    pos=(-0.1, -0.085), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "choice_months"
choice_monthsClock = core.Clock()
concentration4 = visual.TextStim(win=win, name='concentration4',
    text='+\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text4_1 = visual.TextStim(win=win, name='text4_1',
    text='即时选择的奖赏         延迟六个月的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text4_2 = visual.TextStim(win=win, name='text4_2',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text4_3 = visual.TextStim(win=win, name='text4_3',
    text='1000\n',
    font='Arial',
    pos=(0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_6months = keyboard.Keyboard()
x4=500
n4=4
z3=500

# Initialize components for Routine "feed_back3"
feed_back3Clock = core.Clock()
feedback3_1 = visual.TextStim(win=win, name='feedback3_1',
    text='default text',
    font='Arial',
    pos=(-0.1, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
feedback3_2 = visual.TextStim(win=win, name='feedback3_2',
    text='您的选择是',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedback3_3 = visual.TextStim(win=win, name='feedback3_3',
    text='default text',
    font='Arial',
    pos=(0.2, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "tip5"
tip5Clock = core.Clock()
tip_5 = visual.TextStim(win=win, name='tip_5',
    text='（第五阶段）\n\n即时选择的奖赏\n对比\n                的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='延迟一年',
    font='Arial',
    pos=(-0.075, -0.085), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "choice_year"
choice_yearClock = core.Clock()
concentration5 = visual.TextStim(win=win, name='concentration5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text5_1 = visual.TextStim(win=win, name='text5_1',
    text='即时选择的奖赏         延迟一年的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text5_2 = visual.TextStim(win=win, name='text5_2',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text5_3 = visual.TextStim(win=win, name='text5_3',
    text='1000',
    font='Arial',
    pos=(0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_1year = keyboard.Keyboard()
x5=500
n5=4
z4=500

# Initialize components for Routine "feed_back4"
feed_back4Clock = core.Clock()
feedback4_1 = visual.TextStim(win=win, name='feedback4_1',
    text='default text',
    font='Arial',
    pos=(-0.1, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
feedback4_2 = visual.TextStim(win=win, name='feedback4_2',
    text='您的选择是',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedback4_3 = visual.TextStim(win=win, name='feedback4_3',
    text='default text',
    font='Arial',
    pos=(0.2, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "tip6"
tip6Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='（第六阶段）\n\n即时选择的奖赏\n对比\n                的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='延迟五年',
    font='Arial',
    pos=(-0.075, -0.085), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "choice_5years_2"
choice_5years_2Clock = core.Clock()
concentration8 = visual.TextStim(win=win, name='concentration8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text8_1 = visual.TextStim(win=win, name='text8_1',
    text='即时选择的奖赏         延迟五年的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text8_2 = visual.TextStim(win=win, name='text8_2',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text8_3 = visual.TextStim(win=win, name='text8_3',
    text='1000',
    font='Arial',
    pos=(0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp5years = keyboard.Keyboard()
x8=500
n8=4
z6=500

# Initialize components for Routine "feed_back6"
feed_back6Clock = core.Clock()
feedback6_1 = visual.TextStim(win=win, name='feedback6_1',
    text='default text',
    font='Arial',
    pos=(-0.1, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
feedback6_2 = visual.TextStim(win=win, name='feedback6_2',
    text='您的选择是',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedback6_3 = visual.TextStim(win=win, name='feedback6_3',
    text='default text',
    font='Arial',
    pos=(0.2, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "tip7"
tip7Clock = core.Clock()
tip_7 = visual.TextStim(win=win, name='tip_7',
    text='（第七阶段）\n\n即时选择的奖赏\n对比\n                的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='延迟二十五年',
    font='Arial',
    pos=(-0.13, -0.085), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "choice_25years"
choice_25yearsClock = core.Clock()
concentration9 = visual.TextStim(win=win, name='concentration9',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text9_1 = visual.TextStim(win=win, name='text9_1',
    text='即时选择的奖赏         延迟二十五年的奖赏\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text9_2 = visual.TextStim(win=win, name='text9_2',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text9_3 = visual.TextStim(win=win, name='text9_3',
    text='default text',
    font='Arial',
    pos=(0.2, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp25years = keyboard.Keyboard()
x9=500
n9=4
z7=500

# Initialize components for Routine "feedback7"
feedback7Clock = core.Clock()
feedback7_1 = visual.TextStim(win=win, name='feedback7_1',
    text='default text',
    font='Arial',
    pos=(-0.1, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
feedback7_2 = visual.TextStim(win=win, name='feedback7_2',
    text='您的选择是',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedback7_3 = visual.TextStim(win=win, name='feedback7_3',
    text='default text',
    font='Arial',
    pos=(0.2, 0), height=0.05, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='测试结束，谢谢您的参与',
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
key_resp0_1.keys = []
key_resp0_1.rt = []
_key_resp0_1_allKeys = []
# keep track of which components have finished
instruction1Components = [text0_1, key_resp0_1]
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
    
    # *text0_1* updates
    if text0_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text0_1.frameNStart = frameN  # exact frame index
        text0_1.tStart = t  # local t and not account for scr refresh
        text0_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text0_1, 'tStartRefresh')  # time at next scr refresh
        text0_1.setAutoDraw(True)
    
    # *key_resp0_1* updates
    waitOnFlip = False
    if key_resp0_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp0_1.frameNStart = frameN  # exact frame index
        key_resp0_1.tStart = t  # local t and not account for scr refresh
        key_resp0_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp0_1, 'tStartRefresh')  # time at next scr refresh
        key_resp0_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp0_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp0_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp0_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp0_1.getKeys(keyList=['space'], waitRelease=False)
        _key_resp0_1_allKeys.extend(theseKeys)
        if len(_key_resp0_1_allKeys):
            key_resp0_1.keys = _key_resp0_1_allKeys[-1].name  # just the last key pressed
            key_resp0_1.rt = _key_resp0_1_allKeys[-1].rt
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
thisExp.addData('text0_1.started', text0_1.tStartRefresh)
thisExp.addData('text0_1.stopped', text0_1.tStopRefresh)
# the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp0_2.keys = []
key_resp0_2.rt = []
_key_resp0_2_allKeys = []
# keep track of which components have finished
instruction2Components = [text0_2, key_resp0_2]
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
    
    # *text0_2* updates
    if text0_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text0_2.frameNStart = frameN  # exact frame index
        text0_2.tStart = t  # local t and not account for scr refresh
        text0_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text0_2, 'tStartRefresh')  # time at next scr refresh
        text0_2.setAutoDraw(True)
    
    # *key_resp0_2* updates
    waitOnFlip = False
    if key_resp0_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp0_2.frameNStart = frameN  # exact frame index
        key_resp0_2.tStart = t  # local t and not account for scr refresh
        key_resp0_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp0_2, 'tStartRefresh')  # time at next scr refresh
        key_resp0_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp0_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp0_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp0_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp0_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp0_2_allKeys.extend(theseKeys)
        if len(_key_resp0_2_allKeys):
            key_resp0_2.keys = _key_resp0_2_allKeys[-1].name  # just the last key pressed
            key_resp0_2.rt = _key_resp0_2_allKeys[-1].rt
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
thisExp.addData('text0_2.started', text0_2.tStartRefresh)
thisExp.addData('text0_2.stopped', text0_2.tStopRefresh)
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp0_3.keys = []
key_resp0_3.rt = []
_key_resp0_3_allKeys = []
# keep track of which components have finished
instruction3Components = [text0_3, key_resp0_3]
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
    
    # *text0_3* updates
    if text0_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text0_3.frameNStart = frameN  # exact frame index
        text0_3.tStart = t  # local t and not account for scr refresh
        text0_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text0_3, 'tStartRefresh')  # time at next scr refresh
        text0_3.setAutoDraw(True)
    
    # *key_resp0_3* updates
    waitOnFlip = False
    if key_resp0_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp0_3.frameNStart = frameN  # exact frame index
        key_resp0_3.tStart = t  # local t and not account for scr refresh
        key_resp0_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp0_3, 'tStartRefresh')  # time at next scr refresh
        key_resp0_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp0_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp0_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp0_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp0_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp0_3_allKeys.extend(theseKeys)
        if len(_key_resp0_3_allKeys):
            key_resp0_3.keys = _key_resp0_3_allKeys[-1].name  # just the last key pressed
            key_resp0_3.rt = _key_resp0_3_allKeys[-1].rt
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
thisExp.addData('text0_3.started', text0_3.tStartRefresh)
thisExp.addData('text0_3.stopped', text0_3.tStopRefresh)
# check responses
if key_resp0_3.keys in ['', [], None]:  # No response was made
    key_resp0_3.keys = None
thisExp.addData('key_resp0_3.keys',key_resp0_3.keys)
if key_resp0_3.keys != None:  # we had a response
    thisExp.addData('key_resp0_3.rt', key_resp0_3.rt)
thisExp.addData('key_resp0_3.started', key_resp0_3.tStartRefresh)
thisExp.addData('key_resp0_3.stopped', key_resp0_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_0_4.keys = []
key_resp_0_4.rt = []
_key_resp_0_4_allKeys = []
# keep track of which components have finished
instruction4Components = [text0_4, key_resp_0_4]
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
    
    # *text0_4* updates
    if text0_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text0_4.frameNStart = frameN  # exact frame index
        text0_4.tStart = t  # local t and not account for scr refresh
        text0_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text0_4, 'tStartRefresh')  # time at next scr refresh
        text0_4.setAutoDraw(True)
    
    # *key_resp_0_4* updates
    waitOnFlip = False
    if key_resp_0_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_0_4.frameNStart = frameN  # exact frame index
        key_resp_0_4.tStart = t  # local t and not account for scr refresh
        key_resp_0_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_0_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_0_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_0_4_allKeys.extend(theseKeys)
        if len(_key_resp_0_4_allKeys):
            key_resp_0_4.keys = _key_resp_0_4_allKeys[-1].name  # just the last key pressed
            key_resp_0_4.rt = _key_resp_0_4_allKeys[-1].rt
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
thisExp.addData('text0_4.started', text0_4.tStartRefresh)
thisExp.addData('text0_4.stopped', text0_4.tStopRefresh)
# the Routine "instruction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp0_5.keys = []
key_resp0_5.rt = []
_key_resp0_5_allKeys = []
# keep track of which components have finished
instruction5Components = [text0_5, key_resp0_5]
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
    
    # *text0_5* updates
    if text0_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text0_5.frameNStart = frameN  # exact frame index
        text0_5.tStart = t  # local t and not account for scr refresh
        text0_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text0_5, 'tStartRefresh')  # time at next scr refresh
        text0_5.setAutoDraw(True)
    
    # *key_resp0_5* updates
    waitOnFlip = False
    if key_resp0_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp0_5.frameNStart = frameN  # exact frame index
        key_resp0_5.tStart = t  # local t and not account for scr refresh
        key_resp0_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp0_5, 'tStartRefresh')  # time at next scr refresh
        key_resp0_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp0_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp0_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp0_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp0_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp0_5_allKeys.extend(theseKeys)
        if len(_key_resp0_5_allKeys):
            key_resp0_5.keys = _key_resp0_5_allKeys[-1].name  # just the last key pressed
            key_resp0_5.rt = _key_resp0_5_allKeys[-1].rt
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
thisExp.addData('text0_5.started', text0_5.tStartRefresh)
thisExp.addData('text0_5.stopped', text0_5.tStopRefresh)
# the Routine "instruction5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "tip1"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
tip1Components = [tip_1, text_3]
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if tip_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tip_1.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            tip_1.tStop = t  # not accounting for scr refresh
            tip_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tip_1, 'tStopRefresh')  # time at next scr refresh
            tip_1.setAutoDraw(False)
    
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
        if tThisFlipGlobal > text_3.tStartRefresh + 3-frameTolerance:
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
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop1 = data.TrialHandler(nReps=7, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "choice_week_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_1_2.setText(x1
)
    key_resp_1week.keys = []
    key_resp_1week.rt = []
    _key_resp_1week_allKeys = []
    # keep track of which components have finished
    choice_week_2Components = [concentration1, text_1_1, text_1_2, text_1_3, key_resp_1week]
    for thisComponent in choice_week_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choice_week_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice_week_2"-------
    while continueRoutine:
        # get current time
        t = choice_week_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choice_week_2Clock)
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
        
        # *text_1_1* updates
        if text_1_1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            text_1_1.frameNStart = frameN  # exact frame index
            text_1_1.tStart = t  # local t and not account for scr refresh
            text_1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1_1, 'tStartRefresh')  # time at next scr refresh
            text_1_1.setAutoDraw(True)
        
        # *text_1_2* updates
        if text_1_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_1_2.frameNStart = frameN  # exact frame index
            text_1_2.tStart = t  # local t and not account for scr refresh
            text_1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1_2, 'tStartRefresh')  # time at next scr refresh
            text_1_2.setAutoDraw(True)
        
        # *text_1_3* updates
        if text_1_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_1_3.frameNStart = frameN  # exact frame index
            text_1_3.tStart = t  # local t and not account for scr refresh
            text_1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1_3, 'tStartRefresh')  # time at next scr refresh
            text_1_3.setAutoDraw(True)
        
        # *key_resp_1week* updates
        waitOnFlip = False
        if key_resp_1week.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_1week.frameNStart = frameN  # exact frame index
            key_resp_1week.tStart = t  # local t and not account for scr refresh
            key_resp_1week.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1week, 'tStartRefresh')  # time at next scr refresh
            key_resp_1week.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1week.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1week.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_1week.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1week.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_1week_allKeys.extend(theseKeys)
            if len(_key_resp_1week_allKeys):
                key_resp_1week.keys = _key_resp_1week_allKeys[-1].name  # just the last key pressed
                key_resp_1week.rt = _key_resp_1week_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choice_week_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice_week_2"-------
    for thisComponent in choice_week_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop1.addData('concentration1.started', concentration1.tStartRefresh)
    loop1.addData('concentration1.stopped', concentration1.tStopRefresh)
    loop1.addData('text_1_1.started', text_1_1.tStartRefresh)
    loop1.addData('text_1_1.stopped', text_1_1.tStopRefresh)
    loop1.addData('text_1_2.started', text_1_2.tStartRefresh)
    loop1.addData('text_1_2.stopped', text_1_2.tStopRefresh)
    loop1.addData('text_1_3.started', text_1_3.tStartRefresh)
    loop1.addData('text_1_3.stopped', text_1_3.tStopRefresh)
    # check responses
    if key_resp_1week.keys in ['', [], None]:  # No response was made
        key_resp_1week.keys = None
    loop1.addData('key_resp_1week.keys',key_resp_1week.keys)
    if key_resp_1week.keys != None:  # we had a response
        loop1.addData('key_resp_1week.rt', key_resp_1week.rt)
    loop1.addData('key_resp_1week.started', key_resp_1week.tStartRefresh)
    loop1.addData('key_resp_1week.stopped', key_resp_1week.tStopRefresh)
    if "left"in key_resp_1week.keys: 
        z1=x1
        x1-=1000/n1
        n1*=2
        y="即时奖励:"
    if 'right' in key_resp_1week.keys:
        x1+=1000/n1
        n1*=2
        z1=1000
        y="一周后的奖励:"
    # the Routine "choice_week_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feed_back1"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    feedback1_1.setText(y)
    feedback1_3.setText(z1)
    # keep track of which components have finished
    feed_back1Components = [feedback1_1, feedback1_2, feedback1_3]
    for thisComponent in feed_back1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feed_back1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feed_back1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feed_back1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feed_back1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback1_1* updates
        if feedback1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback1_1.frameNStart = frameN  # exact frame index
            feedback1_1.tStart = t  # local t and not account for scr refresh
            feedback1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback1_1, 'tStartRefresh')  # time at next scr refresh
            feedback1_1.setAutoDraw(True)
        if feedback1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback1_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback1_1.tStop = t  # not accounting for scr refresh
                feedback1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback1_1, 'tStopRefresh')  # time at next scr refresh
                feedback1_1.setAutoDraw(False)
        
        # *feedback1_2* updates
        if feedback1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback1_2.frameNStart = frameN  # exact frame index
            feedback1_2.tStart = t  # local t and not account for scr refresh
            feedback1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback1_2, 'tStartRefresh')  # time at next scr refresh
            feedback1_2.setAutoDraw(True)
        if feedback1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback1_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback1_2.tStop = t  # not accounting for scr refresh
                feedback1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback1_2, 'tStopRefresh')  # time at next scr refresh
                feedback1_2.setAutoDraw(False)
        
        # *feedback1_3* updates
        if feedback1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback1_3.frameNStart = frameN  # exact frame index
            feedback1_3.tStart = t  # local t and not account for scr refresh
            feedback1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback1_3, 'tStartRefresh')  # time at next scr refresh
            feedback1_3.setAutoDraw(True)
        if feedback1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback1_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback1_3.tStop = t  # not accounting for scr refresh
                feedback1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback1_3, 'tStopRefresh')  # time at next scr refresh
                feedback1_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feed_back1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feed_back1"-------
    for thisComponent in feed_back1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop1.addData('feedback1_1.started', feedback1_1.tStartRefresh)
    loop1.addData('feedback1_1.stopped', feedback1_1.tStopRefresh)
    loop1.addData('feedback1_2.started', feedback1_2.tStartRefresh)
    loop1.addData('feedback1_2.stopped', feedback1_2.tStopRefresh)
    loop1.addData('feedback1_3.started', feedback1_3.tStartRefresh)
    loop1.addData('feedback1_3.stopped', feedback1_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 7 repeats of 'loop1'


# ------Prepare to start Routine "tip2"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
tip2Components = [tip_2, text_4]
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if tip_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tip_2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            tip_2.tStop = t  # not accounting for scr refresh
            tip_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tip_2, 'tStopRefresh')  # time at next scr refresh
            tip_2.setAutoDraw(False)
    
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
        if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
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
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "choice_2weeks"-------
    continueRoutine = True
    # update component parameters for each repeat
    text6_2.setText(x6
)
    key_resp_2weeks.keys = []
    key_resp_2weeks.rt = []
    _key_resp_2weeks_allKeys = []
    # keep track of which components have finished
    choice_2weeksComponents = [concentration6, text6_1, text6_2, text6_3, key_resp_2weeks]
    for thisComponent in choice_2weeksComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choice_2weeksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice_2weeks"-------
    while continueRoutine:
        # get current time
        t = choice_2weeksClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choice_2weeksClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration6* updates
        if concentration6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration6.frameNStart = frameN  # exact frame index
            concentration6.tStart = t  # local t and not account for scr refresh
            concentration6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration6, 'tStartRefresh')  # time at next scr refresh
            concentration6.setAutoDraw(True)
        if concentration6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration6.tStop = t  # not accounting for scr refresh
                concentration6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration6, 'tStopRefresh')  # time at next scr refresh
                concentration6.setAutoDraw(False)
        
        # *text6_1* updates
        if text6_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text6_1.frameNStart = frameN  # exact frame index
            text6_1.tStart = t  # local t and not account for scr refresh
            text6_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text6_1, 'tStartRefresh')  # time at next scr refresh
            text6_1.setAutoDraw(True)
        
        # *text6_2* updates
        if text6_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text6_2.frameNStart = frameN  # exact frame index
            text6_2.tStart = t  # local t and not account for scr refresh
            text6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text6_2, 'tStartRefresh')  # time at next scr refresh
            text6_2.setAutoDraw(True)
        
        # *text6_3* updates
        if text6_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text6_3.frameNStart = frameN  # exact frame index
            text6_3.tStart = t  # local t and not account for scr refresh
            text6_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text6_3, 'tStartRefresh')  # time at next scr refresh
            text6_3.setAutoDraw(True)
        
        # *key_resp_2weeks* updates
        waitOnFlip = False
        if key_resp_2weeks.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2weeks.frameNStart = frameN  # exact frame index
            key_resp_2weeks.tStart = t  # local t and not account for scr refresh
            key_resp_2weeks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2weeks, 'tStartRefresh')  # time at next scr refresh
            key_resp_2weeks.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2weeks.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2weeks.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2weeks.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2weeks.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_2weeks_allKeys.extend(theseKeys)
            if len(_key_resp_2weeks_allKeys):
                key_resp_2weeks.keys = _key_resp_2weeks_allKeys[-1].name  # just the last key pressed
                key_resp_2weeks.rt = _key_resp_2weeks_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choice_2weeksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice_2weeks"-------
    for thisComponent in choice_2weeksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('concentration6.started', concentration6.tStartRefresh)
    trials.addData('concentration6.stopped', concentration6.tStopRefresh)
    trials.addData('text6_1.started', text6_1.tStartRefresh)
    trials.addData('text6_1.stopped', text6_1.tStopRefresh)
    trials.addData('text6_2.started', text6_2.tStartRefresh)
    trials.addData('text6_2.stopped', text6_2.tStopRefresh)
    trials.addData('text6_3.started', text6_3.tStartRefresh)
    trials.addData('text6_3.stopped', text6_3.tStopRefresh)
    # check responses
    if key_resp_2weeks.keys in ['', [], None]:  # No response was made
        key_resp_2weeks.keys = None
    trials.addData('key_resp_2weeks.keys',key_resp_2weeks.keys)
    if key_resp_2weeks.keys != None:  # we had a response
        trials.addData('key_resp_2weeks.rt', key_resp_2weeks.rt)
    trials.addData('key_resp_2weeks.started', key_resp_2weeks.tStartRefresh)
    trials.addData('key_resp_2weeks.stopped', key_resp_2weeks.tStopRefresh)
    if 'left'in key_resp_2weeks.keys:
        z5=x6
        x6-=1000/n6
        n6*=2
        y="即时奖励"
    if 'right' in key_resp_2weeks.keys:
        x6+=1000/n6
        n6*=2
        z5=1000
        y="两周后的奖励"
    # the Routine "choice_2weeks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feed_back5"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    feedback5_1.setText(y)
    feedback5_3.setText(z5)
    # keep track of which components have finished
    feed_back5Components = [feedback5_1, feedback5_2, feedback5_3]
    for thisComponent in feed_back5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feed_back5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feed_back5"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feed_back5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feed_back5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback5_1* updates
        if feedback5_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback5_1.frameNStart = frameN  # exact frame index
            feedback5_1.tStart = t  # local t and not account for scr refresh
            feedback5_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback5_1, 'tStartRefresh')  # time at next scr refresh
            feedback5_1.setAutoDraw(True)
        if feedback5_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback5_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback5_1.tStop = t  # not accounting for scr refresh
                feedback5_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback5_1, 'tStopRefresh')  # time at next scr refresh
                feedback5_1.setAutoDraw(False)
        
        # *feedback5_2* updates
        if feedback5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback5_2.frameNStart = frameN  # exact frame index
            feedback5_2.tStart = t  # local t and not account for scr refresh
            feedback5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback5_2, 'tStartRefresh')  # time at next scr refresh
            feedback5_2.setAutoDraw(True)
        if feedback5_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback5_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback5_2.tStop = t  # not accounting for scr refresh
                feedback5_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback5_2, 'tStopRefresh')  # time at next scr refresh
                feedback5_2.setAutoDraw(False)
        
        # *feedback5_3* updates
        if feedback5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback5_3.frameNStart = frameN  # exact frame index
            feedback5_3.tStart = t  # local t and not account for scr refresh
            feedback5_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback5_3, 'tStartRefresh')  # time at next scr refresh
            feedback5_3.setAutoDraw(True)
        if feedback5_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback5_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback5_3.tStop = t  # not accounting for scr refresh
                feedback5_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback5_3, 'tStopRefresh')  # time at next scr refresh
                feedback5_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feed_back5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feed_back5"-------
    for thisComponent in feed_back5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedback5_1.started', feedback5_1.tStartRefresh)
    trials.addData('feedback5_1.stopped', feedback5_1.tStopRefresh)
    trials.addData('feedback5_2.started', feedback5_2.tStartRefresh)
    trials.addData('feedback5_2.stopped', feedback5_2.tStopRefresh)
    trials.addData('feedback5_3.started', feedback5_3.tStartRefresh)
    trials.addData('feedback5_3.stopped', feedback5_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


# ------Prepare to start Routine "tip3"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
tip3Components = [tip_3, text_5]
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
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = tip3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=tip3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tip_3* updates
    if tip_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tip_3.frameNStart = frameN  # exact frame index
        tip_3.tStart = t  # local t and not account for scr refresh
        tip_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tip_3, 'tStartRefresh')  # time at next scr refresh
        tip_3.setAutoDraw(True)
    if tip_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tip_3.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            tip_3.tStop = t  # not accounting for scr refresh
            tip_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tip_3, 'tStopRefresh')  # time at next scr refresh
            tip_3.setAutoDraw(False)
    
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
        if tThisFlipGlobal > text_5.tStartRefresh + 3-frameTolerance:
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
thisExp.addData('tip_3.started', tip_3.tStartRefresh)
thisExp.addData('tip_3.stopped', tip_3.tStopRefresh)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop3 = data.TrialHandler(nReps=7, method='random', 
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
    
    # ------Prepare to start Routine "choice_month"-------
    continueRoutine = True
    # update component parameters for each repeat
    text3_2.setText(x3)
    key_resp_1month.keys = []
    key_resp_1month.rt = []
    _key_resp_1month_allKeys = []
    # keep track of which components have finished
    choice_monthComponents = [concentration3, text3_1, text3_2, text3_3, key_resp_1month]
    for thisComponent in choice_monthComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choice_monthClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice_month"-------
    while continueRoutine:
        # get current time
        t = choice_monthClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choice_monthClock)
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
        
        # *text3_1* updates
        if text3_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text3_1.frameNStart = frameN  # exact frame index
            text3_1.tStart = t  # local t and not account for scr refresh
            text3_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text3_1, 'tStartRefresh')  # time at next scr refresh
            text3_1.setAutoDraw(True)
        
        # *text3_2* updates
        if text3_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text3_2.frameNStart = frameN  # exact frame index
            text3_2.tStart = t  # local t and not account for scr refresh
            text3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text3_2, 'tStartRefresh')  # time at next scr refresh
            text3_2.setAutoDraw(True)
        
        # *text3_3* updates
        if text3_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text3_3.frameNStart = frameN  # exact frame index
            text3_3.tStart = t  # local t and not account for scr refresh
            text3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text3_3, 'tStartRefresh')  # time at next scr refresh
            text3_3.setAutoDraw(True)
        
        # *key_resp_1month* updates
        waitOnFlip = False
        if key_resp_1month.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_1month.frameNStart = frameN  # exact frame index
            key_resp_1month.tStart = t  # local t and not account for scr refresh
            key_resp_1month.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1month, 'tStartRefresh')  # time at next scr refresh
            key_resp_1month.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1month.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1month.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_1month.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1month.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_1month_allKeys.extend(theseKeys)
            if len(_key_resp_1month_allKeys):
                key_resp_1month.keys = _key_resp_1month_allKeys[-1].name  # just the last key pressed
                key_resp_1month.rt = _key_resp_1month_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choice_monthComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice_month"-------
    for thisComponent in choice_monthComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop3.addData('concentration3.started', concentration3.tStartRefresh)
    loop3.addData('concentration3.stopped', concentration3.tStopRefresh)
    loop3.addData('text3_1.started', text3_1.tStartRefresh)
    loop3.addData('text3_1.stopped', text3_1.tStopRefresh)
    loop3.addData('text3_2.started', text3_2.tStartRefresh)
    loop3.addData('text3_2.stopped', text3_2.tStopRefresh)
    loop3.addData('text3_3.started', text3_3.tStartRefresh)
    loop3.addData('text3_3.stopped', text3_3.tStopRefresh)
    # check responses
    if key_resp_1month.keys in ['', [], None]:  # No response was made
        key_resp_1month.keys = None
    loop3.addData('key_resp_1month.keys',key_resp_1month.keys)
    if key_resp_1month.keys != None:  # we had a response
        loop3.addData('key_resp_1month.rt', key_resp_1month.rt)
    loop3.addData('key_resp_1month.started', key_resp_1month.tStartRefresh)
    loop3.addData('key_resp_1month.stopped', key_resp_1month.tStopRefresh)
    if 'left'in key_resp_1month.keys:
        z2=x3
        x3-=1000/n3
        n3*=2
        y="即时奖励"
    if 'right' in key_resp_1month.keys:
        x3+=1000/n3
        n3*=2
        z2=1000
        y="一个月后的奖励"
    # the Routine "choice_month" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feed_back2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    feedback2_1.setText(y)
    feedback2_3.setText(z2)
    # keep track of which components have finished
    feed_back2Components = [feedback2_1, feedback2_2, feedback2_3]
    for thisComponent in feed_back2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feed_back2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feed_back2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feed_back2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feed_back2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback2_1* updates
        if feedback2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback2_1.frameNStart = frameN  # exact frame index
            feedback2_1.tStart = t  # local t and not account for scr refresh
            feedback2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback2_1, 'tStartRefresh')  # time at next scr refresh
            feedback2_1.setAutoDraw(True)
        if feedback2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback2_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback2_1.tStop = t  # not accounting for scr refresh
                feedback2_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback2_1, 'tStopRefresh')  # time at next scr refresh
                feedback2_1.setAutoDraw(False)
        
        # *feedback2_2* updates
        if feedback2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback2_2.frameNStart = frameN  # exact frame index
            feedback2_2.tStart = t  # local t and not account for scr refresh
            feedback2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback2_2, 'tStartRefresh')  # time at next scr refresh
            feedback2_2.setAutoDraw(True)
        if feedback2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback2_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback2_2.tStop = t  # not accounting for scr refresh
                feedback2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback2_2, 'tStopRefresh')  # time at next scr refresh
                feedback2_2.setAutoDraw(False)
        
        # *feedback2_3* updates
        if feedback2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback2_3.frameNStart = frameN  # exact frame index
            feedback2_3.tStart = t  # local t and not account for scr refresh
            feedback2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback2_3, 'tStartRefresh')  # time at next scr refresh
            feedback2_3.setAutoDraw(True)
        if feedback2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback2_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback2_3.tStop = t  # not accounting for scr refresh
                feedback2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback2_3, 'tStopRefresh')  # time at next scr refresh
                feedback2_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feed_back2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feed_back2"-------
    for thisComponent in feed_back2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop3.addData('feedback2_1.started', feedback2_1.tStartRefresh)
    loop3.addData('feedback2_1.stopped', feedback2_1.tStopRefresh)
    loop3.addData('feedback2_2.started', feedback2_2.tStartRefresh)
    loop3.addData('feedback2_2.stopped', feedback2_2.tStopRefresh)
    loop3.addData('feedback2_3.started', feedback2_3.tStartRefresh)
    loop3.addData('feedback2_3.stopped', feedback2_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 7 repeats of 'loop3'


# ------Prepare to start Routine "tip4"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
tip4Components = [tip_4, text_6]
for thisComponent in tip4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
tip4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "tip4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = tip4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=tip4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tip_4* updates
    if tip_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tip_4.frameNStart = frameN  # exact frame index
        tip_4.tStart = t  # local t and not account for scr refresh
        tip_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tip_4, 'tStartRefresh')  # time at next scr refresh
        tip_4.setAutoDraw(True)
    if tip_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tip_4.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            tip_4.tStop = t  # not accounting for scr refresh
            tip_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tip_4, 'tStopRefresh')  # time at next scr refresh
            tip_4.setAutoDraw(False)
    
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
        if tThisFlipGlobal > text_6.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
            text_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in tip4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "tip4"-------
for thisComponent in tip4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tip_4.started', tip_4.tStartRefresh)
thisExp.addData('tip_4.stopped', tip_4.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop4 = data.TrialHandler(nReps=7, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop4')
thisExp.addLoop(loop4)  # add the loop to the experiment
thisLoop4 = loop4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop4.rgb)
if thisLoop4 != None:
    for paramName in thisLoop4:
        exec('{} = thisLoop4[paramName]'.format(paramName))

for thisLoop4 in loop4:
    currentLoop = loop4
    # abbreviate parameter names if possible (e.g. rgb = thisLoop4.rgb)
    if thisLoop4 != None:
        for paramName in thisLoop4:
            exec('{} = thisLoop4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "choice_months"-------
    continueRoutine = True
    # update component parameters for each repeat
    text4_2.setText(x4)
    key_resp_6months.keys = []
    key_resp_6months.rt = []
    _key_resp_6months_allKeys = []
    # keep track of which components have finished
    choice_monthsComponents = [concentration4, text4_1, text4_2, text4_3, key_resp_6months]
    for thisComponent in choice_monthsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choice_monthsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice_months"-------
    while continueRoutine:
        # get current time
        t = choice_monthsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choice_monthsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration4* updates
        if concentration4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration4.frameNStart = frameN  # exact frame index
            concentration4.tStart = t  # local t and not account for scr refresh
            concentration4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration4, 'tStartRefresh')  # time at next scr refresh
            concentration4.setAutoDraw(True)
        if concentration4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration4.tStop = t  # not accounting for scr refresh
                concentration4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration4, 'tStopRefresh')  # time at next scr refresh
                concentration4.setAutoDraw(False)
        
        # *text4_1* updates
        if text4_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text4_1.frameNStart = frameN  # exact frame index
            text4_1.tStart = t  # local t and not account for scr refresh
            text4_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text4_1, 'tStartRefresh')  # time at next scr refresh
            text4_1.setAutoDraw(True)
        
        # *text4_2* updates
        if text4_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text4_2.frameNStart = frameN  # exact frame index
            text4_2.tStart = t  # local t and not account for scr refresh
            text4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text4_2, 'tStartRefresh')  # time at next scr refresh
            text4_2.setAutoDraw(True)
        
        # *text4_3* updates
        if text4_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text4_3.frameNStart = frameN  # exact frame index
            text4_3.tStart = t  # local t and not account for scr refresh
            text4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text4_3, 'tStartRefresh')  # time at next scr refresh
            text4_3.setAutoDraw(True)
        
        # *key_resp_6months* updates
        waitOnFlip = False
        if key_resp_6months.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6months.frameNStart = frameN  # exact frame index
            key_resp_6months.tStart = t  # local t and not account for scr refresh
            key_resp_6months.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6months, 'tStartRefresh')  # time at next scr refresh
            key_resp_6months.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6months.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6months.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6months.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6months.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_6months_allKeys.extend(theseKeys)
            if len(_key_resp_6months_allKeys):
                key_resp_6months.keys = _key_resp_6months_allKeys[-1].name  # just the last key pressed
                key_resp_6months.rt = _key_resp_6months_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choice_monthsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice_months"-------
    for thisComponent in choice_monthsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop4.addData('concentration4.started', concentration4.tStartRefresh)
    loop4.addData('concentration4.stopped', concentration4.tStopRefresh)
    loop4.addData('text4_1.started', text4_1.tStartRefresh)
    loop4.addData('text4_1.stopped', text4_1.tStopRefresh)
    loop4.addData('text4_2.started', text4_2.tStartRefresh)
    loop4.addData('text4_2.stopped', text4_2.tStopRefresh)
    loop4.addData('text4_3.started', text4_3.tStartRefresh)
    loop4.addData('text4_3.stopped', text4_3.tStopRefresh)
    # check responses
    if key_resp_6months.keys in ['', [], None]:  # No response was made
        key_resp_6months.keys = None
    loop4.addData('key_resp_6months.keys',key_resp_6months.keys)
    if key_resp_6months.keys != None:  # we had a response
        loop4.addData('key_resp_6months.rt', key_resp_6months.rt)
    loop4.addData('key_resp_6months.started', key_resp_6months.tStartRefresh)
    loop4.addData('key_resp_6months.stopped', key_resp_6months.tStopRefresh)
    if 'left'in key_resp_6months.keys:
        z3=x4
        x4-=1000/n4
        n4*=2
        y="即时奖励"
    if 'right' in key_resp_6months.keys:
        x4+=1000/n4
        n4*=2
        z3=1000
        y="六个月后的奖励"
    # the Routine "choice_months" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feed_back3"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    feedback3_1.setText(y)
    feedback3_3.setText(z3)
    # keep track of which components have finished
    feed_back3Components = [feedback3_1, feedback3_2, feedback3_3]
    for thisComponent in feed_back3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feed_back3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feed_back3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feed_back3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feed_back3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback3_1* updates
        if feedback3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback3_1.frameNStart = frameN  # exact frame index
            feedback3_1.tStart = t  # local t and not account for scr refresh
            feedback3_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback3_1, 'tStartRefresh')  # time at next scr refresh
            feedback3_1.setAutoDraw(True)
        if feedback3_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback3_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback3_1.tStop = t  # not accounting for scr refresh
                feedback3_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback3_1, 'tStopRefresh')  # time at next scr refresh
                feedback3_1.setAutoDraw(False)
        
        # *feedback3_2* updates
        if feedback3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback3_2.frameNStart = frameN  # exact frame index
            feedback3_2.tStart = t  # local t and not account for scr refresh
            feedback3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback3_2, 'tStartRefresh')  # time at next scr refresh
            feedback3_2.setAutoDraw(True)
        if feedback3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback3_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback3_2.tStop = t  # not accounting for scr refresh
                feedback3_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback3_2, 'tStopRefresh')  # time at next scr refresh
                feedback3_2.setAutoDraw(False)
        
        # *feedback3_3* updates
        if feedback3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback3_3.frameNStart = frameN  # exact frame index
            feedback3_3.tStart = t  # local t and not account for scr refresh
            feedback3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback3_3, 'tStartRefresh')  # time at next scr refresh
            feedback3_3.setAutoDraw(True)
        if feedback3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback3_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback3_3.tStop = t  # not accounting for scr refresh
                feedback3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback3_3, 'tStopRefresh')  # time at next scr refresh
                feedback3_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feed_back3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feed_back3"-------
    for thisComponent in feed_back3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop4.addData('feedback3_1.started', feedback3_1.tStartRefresh)
    loop4.addData('feedback3_1.stopped', feedback3_1.tStopRefresh)
    loop4.addData('feedback3_2.started', feedback3_2.tStartRefresh)
    loop4.addData('feedback3_2.stopped', feedback3_2.tStopRefresh)
    loop4.addData('feedback3_3.started', feedback3_3.tStartRefresh)
    loop4.addData('feedback3_3.stopped', feedback3_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 7 repeats of 'loop4'


# ------Prepare to start Routine "tip5"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
tip5Components = [tip_5, text_7]
for thisComponent in tip5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
tip5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "tip5"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = tip5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=tip5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tip_5* updates
    if tip_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tip_5.frameNStart = frameN  # exact frame index
        tip_5.tStart = t  # local t and not account for scr refresh
        tip_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tip_5, 'tStartRefresh')  # time at next scr refresh
        tip_5.setAutoDraw(True)
    if tip_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tip_5.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            tip_5.tStop = t  # not accounting for scr refresh
            tip_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tip_5, 'tStopRefresh')  # time at next scr refresh
            tip_5.setAutoDraw(False)
    
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
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in tip5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "tip5"-------
for thisComponent in tip5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tip_5.started', tip_5.tStartRefresh)
thisExp.addData('tip_5.stopped', tip_5.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop5 = data.TrialHandler(nReps=7, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop5')
thisExp.addLoop(loop5)  # add the loop to the experiment
thisLoop5 = loop5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop5.rgb)
if thisLoop5 != None:
    for paramName in thisLoop5:
        exec('{} = thisLoop5[paramName]'.format(paramName))

for thisLoop5 in loop5:
    currentLoop = loop5
    # abbreviate parameter names if possible (e.g. rgb = thisLoop5.rgb)
    if thisLoop5 != None:
        for paramName in thisLoop5:
            exec('{} = thisLoop5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "choice_year"-------
    continueRoutine = True
    # update component parameters for each repeat
    text5_2.setText(x5
)
    key_resp_1year.keys = []
    key_resp_1year.rt = []
    _key_resp_1year_allKeys = []
    # keep track of which components have finished
    choice_yearComponents = [concentration5, text5_1, text5_2, text5_3, key_resp_1year]
    for thisComponent in choice_yearComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choice_yearClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice_year"-------
    while continueRoutine:
        # get current time
        t = choice_yearClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choice_yearClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration5* updates
        if concentration5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration5.frameNStart = frameN  # exact frame index
            concentration5.tStart = t  # local t and not account for scr refresh
            concentration5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration5, 'tStartRefresh')  # time at next scr refresh
            concentration5.setAutoDraw(True)
        if concentration5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration5.tStop = t  # not accounting for scr refresh
                concentration5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration5, 'tStopRefresh')  # time at next scr refresh
                concentration5.setAutoDraw(False)
        
        # *text5_1* updates
        if text5_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text5_1.frameNStart = frameN  # exact frame index
            text5_1.tStart = t  # local t and not account for scr refresh
            text5_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text5_1, 'tStartRefresh')  # time at next scr refresh
            text5_1.setAutoDraw(True)
        
        # *text5_2* updates
        if text5_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text5_2.frameNStart = frameN  # exact frame index
            text5_2.tStart = t  # local t and not account for scr refresh
            text5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text5_2, 'tStartRefresh')  # time at next scr refresh
            text5_2.setAutoDraw(True)
        
        # *text5_3* updates
        if text5_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text5_3.frameNStart = frameN  # exact frame index
            text5_3.tStart = t  # local t and not account for scr refresh
            text5_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text5_3, 'tStartRefresh')  # time at next scr refresh
            text5_3.setAutoDraw(True)
        
        # *key_resp_1year* updates
        waitOnFlip = False
        if key_resp_1year.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_1year.frameNStart = frameN  # exact frame index
            key_resp_1year.tStart = t  # local t and not account for scr refresh
            key_resp_1year.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1year, 'tStartRefresh')  # time at next scr refresh
            key_resp_1year.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1year.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1year.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_1year.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1year.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_1year_allKeys.extend(theseKeys)
            if len(_key_resp_1year_allKeys):
                key_resp_1year.keys = _key_resp_1year_allKeys[-1].name  # just the last key pressed
                key_resp_1year.rt = _key_resp_1year_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choice_yearComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice_year"-------
    for thisComponent in choice_yearComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop5.addData('concentration5.started', concentration5.tStartRefresh)
    loop5.addData('concentration5.stopped', concentration5.tStopRefresh)
    loop5.addData('text5_1.started', text5_1.tStartRefresh)
    loop5.addData('text5_1.stopped', text5_1.tStopRefresh)
    loop5.addData('text5_2.started', text5_2.tStartRefresh)
    loop5.addData('text5_2.stopped', text5_2.tStopRefresh)
    loop5.addData('text5_3.started', text5_3.tStartRefresh)
    loop5.addData('text5_3.stopped', text5_3.tStopRefresh)
    # check responses
    if key_resp_1year.keys in ['', [], None]:  # No response was made
        key_resp_1year.keys = None
    loop5.addData('key_resp_1year.keys',key_resp_1year.keys)
    if key_resp_1year.keys != None:  # we had a response
        loop5.addData('key_resp_1year.rt', key_resp_1year.rt)
    loop5.addData('key_resp_1year.started', key_resp_1year.tStartRefresh)
    loop5.addData('key_resp_1year.stopped', key_resp_1year.tStopRefresh)
    if 'left'in key_resp_1year.keys:
        z4=x5
        x5-=1000/n5
        n5*=2
        y="即时奖励"
    if 'right' in key_resp_1year.keys:
        x5+=1000/n5
        n5*=2
        z4=1000
        y="一年后的奖励"
    # the Routine "choice_year" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feed_back4"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    feedback4_1.setText(y)
    feedback4_3.setText(z4)
    # keep track of which components have finished
    feed_back4Components = [feedback4_1, feedback4_2, feedback4_3]
    for thisComponent in feed_back4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feed_back4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feed_back4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feed_back4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feed_back4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback4_1* updates
        if feedback4_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback4_1.frameNStart = frameN  # exact frame index
            feedback4_1.tStart = t  # local t and not account for scr refresh
            feedback4_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback4_1, 'tStartRefresh')  # time at next scr refresh
            feedback4_1.setAutoDraw(True)
        if feedback4_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback4_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback4_1.tStop = t  # not accounting for scr refresh
                feedback4_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback4_1, 'tStopRefresh')  # time at next scr refresh
                feedback4_1.setAutoDraw(False)
        
        # *feedback4_2* updates
        if feedback4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback4_2.frameNStart = frameN  # exact frame index
            feedback4_2.tStart = t  # local t and not account for scr refresh
            feedback4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback4_2, 'tStartRefresh')  # time at next scr refresh
            feedback4_2.setAutoDraw(True)
        if feedback4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback4_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback4_2.tStop = t  # not accounting for scr refresh
                feedback4_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback4_2, 'tStopRefresh')  # time at next scr refresh
                feedback4_2.setAutoDraw(False)
        
        # *feedback4_3* updates
        if feedback4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback4_3.frameNStart = frameN  # exact frame index
            feedback4_3.tStart = t  # local t and not account for scr refresh
            feedback4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback4_3, 'tStartRefresh')  # time at next scr refresh
            feedback4_3.setAutoDraw(True)
        if feedback4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback4_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback4_3.tStop = t  # not accounting for scr refresh
                feedback4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback4_3, 'tStopRefresh')  # time at next scr refresh
                feedback4_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feed_back4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feed_back4"-------
    for thisComponent in feed_back4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop5.addData('feedback4_1.started', feedback4_1.tStartRefresh)
    loop5.addData('feedback4_1.stopped', feedback4_1.tStopRefresh)
    loop5.addData('feedback4_2.started', feedback4_2.tStartRefresh)
    loop5.addData('feedback4_2.stopped', feedback4_2.tStopRefresh)
    loop5.addData('feedback4_3.started', feedback4_3.tStartRefresh)
    loop5.addData('feedback4_3.stopped', feedback4_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 7 repeats of 'loop5'


# ------Prepare to start Routine "tip6"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
tip6Components = [text, text_8]
for thisComponent in tip6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
tip6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "tip6"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = tip6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=tip6Clock)
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
        if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
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
        if tThisFlipGlobal > text_8.tStartRefresh + 3-frameTolerance:
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
    for thisComponent in tip6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "tip6"-------
for thisComponent in tip6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop8 = data.TrialHandler(nReps=7, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop8')
thisExp.addLoop(loop8)  # add the loop to the experiment
thisLoop8 = loop8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop8.rgb)
if thisLoop8 != None:
    for paramName in thisLoop8:
        exec('{} = thisLoop8[paramName]'.format(paramName))

for thisLoop8 in loop8:
    currentLoop = loop8
    # abbreviate parameter names if possible (e.g. rgb = thisLoop8.rgb)
    if thisLoop8 != None:
        for paramName in thisLoop8:
            exec('{} = thisLoop8[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "choice_5years_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    text8_2.setText(x8)
    key_resp5years.keys = []
    key_resp5years.rt = []
    _key_resp5years_allKeys = []
    # keep track of which components have finished
    choice_5years_2Components = [concentration8, text8_1, text8_2, text8_3, key_resp5years]
    for thisComponent in choice_5years_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choice_5years_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice_5years_2"-------
    while continueRoutine:
        # get current time
        t = choice_5years_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choice_5years_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration8* updates
        if concentration8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration8.frameNStart = frameN  # exact frame index
            concentration8.tStart = t  # local t and not account for scr refresh
            concentration8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration8, 'tStartRefresh')  # time at next scr refresh
            concentration8.setAutoDraw(True)
        if concentration8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration8.tStop = t  # not accounting for scr refresh
                concentration8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration8, 'tStopRefresh')  # time at next scr refresh
                concentration8.setAutoDraw(False)
        
        # *text8_1* updates
        if text8_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text8_1.frameNStart = frameN  # exact frame index
            text8_1.tStart = t  # local t and not account for scr refresh
            text8_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text8_1, 'tStartRefresh')  # time at next scr refresh
            text8_1.setAutoDraw(True)
        
        # *text8_2* updates
        if text8_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text8_2.frameNStart = frameN  # exact frame index
            text8_2.tStart = t  # local t and not account for scr refresh
            text8_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text8_2, 'tStartRefresh')  # time at next scr refresh
            text8_2.setAutoDraw(True)
        
        # *text8_3* updates
        if text8_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text8_3.frameNStart = frameN  # exact frame index
            text8_3.tStart = t  # local t and not account for scr refresh
            text8_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text8_3, 'tStartRefresh')  # time at next scr refresh
            text8_3.setAutoDraw(True)
        
        # *key_resp5years* updates
        waitOnFlip = False
        if key_resp5years.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp5years.frameNStart = frameN  # exact frame index
            key_resp5years.tStart = t  # local t and not account for scr refresh
            key_resp5years.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp5years, 'tStartRefresh')  # time at next scr refresh
            key_resp5years.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp5years.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp5years.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp5years.status == STARTED and not waitOnFlip:
            theseKeys = key_resp5years.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp5years_allKeys.extend(theseKeys)
            if len(_key_resp5years_allKeys):
                key_resp5years.keys = _key_resp5years_allKeys[-1].name  # just the last key pressed
                key_resp5years.rt = _key_resp5years_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choice_5years_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice_5years_2"-------
    for thisComponent in choice_5years_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop8.addData('concentration8.started', concentration8.tStartRefresh)
    loop8.addData('concentration8.stopped', concentration8.tStopRefresh)
    loop8.addData('text8_1.started', text8_1.tStartRefresh)
    loop8.addData('text8_1.stopped', text8_1.tStopRefresh)
    loop8.addData('text8_2.started', text8_2.tStartRefresh)
    loop8.addData('text8_2.stopped', text8_2.tStopRefresh)
    loop8.addData('text8_3.started', text8_3.tStartRefresh)
    loop8.addData('text8_3.stopped', text8_3.tStopRefresh)
    # check responses
    if key_resp5years.keys in ['', [], None]:  # No response was made
        key_resp5years.keys = None
    loop8.addData('key_resp5years.keys',key_resp5years.keys)
    if key_resp5years.keys != None:  # we had a response
        loop8.addData('key_resp5years.rt', key_resp5years.rt)
    loop8.addData('key_resp5years.started', key_resp5years.tStartRefresh)
    loop8.addData('key_resp5years.stopped', key_resp5years.tStopRefresh)
    if 'left'in key_resp5years.keys:
        z6=x8
        x8-=1000/n8
        n8*=2
        y="即时奖励"
    if 'right' in key_resp5years.keys:
        x8+=1000/n8
        n8*=2
        z6=1000
        y="五年后的奖励"
    # the Routine "choice_5years_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feed_back6"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    feedback6_1.setText(y)
    feedback6_3.setText(z6)
    # keep track of which components have finished
    feed_back6Components = [feedback6_1, feedback6_2, feedback6_3]
    for thisComponent in feed_back6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feed_back6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feed_back6"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feed_back6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feed_back6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback6_1* updates
        if feedback6_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback6_1.frameNStart = frameN  # exact frame index
            feedback6_1.tStart = t  # local t and not account for scr refresh
            feedback6_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback6_1, 'tStartRefresh')  # time at next scr refresh
            feedback6_1.setAutoDraw(True)
        if feedback6_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback6_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback6_1.tStop = t  # not accounting for scr refresh
                feedback6_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback6_1, 'tStopRefresh')  # time at next scr refresh
                feedback6_1.setAutoDraw(False)
        
        # *feedback6_2* updates
        if feedback6_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback6_2.frameNStart = frameN  # exact frame index
            feedback6_2.tStart = t  # local t and not account for scr refresh
            feedback6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback6_2, 'tStartRefresh')  # time at next scr refresh
            feedback6_2.setAutoDraw(True)
        if feedback6_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback6_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback6_2.tStop = t  # not accounting for scr refresh
                feedback6_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback6_2, 'tStopRefresh')  # time at next scr refresh
                feedback6_2.setAutoDraw(False)
        
        # *feedback6_3* updates
        if feedback6_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback6_3.frameNStart = frameN  # exact frame index
            feedback6_3.tStart = t  # local t and not account for scr refresh
            feedback6_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback6_3, 'tStartRefresh')  # time at next scr refresh
            feedback6_3.setAutoDraw(True)
        if feedback6_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback6_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback6_3.tStop = t  # not accounting for scr refresh
                feedback6_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback6_3, 'tStopRefresh')  # time at next scr refresh
                feedback6_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feed_back6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feed_back6"-------
    for thisComponent in feed_back6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop8.addData('feedback6_1.started', feedback6_1.tStartRefresh)
    loop8.addData('feedback6_1.stopped', feedback6_1.tStopRefresh)
    loop8.addData('feedback6_2.started', feedback6_2.tStartRefresh)
    loop8.addData('feedback6_2.stopped', feedback6_2.tStopRefresh)
    loop8.addData('feedback6_3.started', feedback6_3.tStartRefresh)
    loop8.addData('feedback6_3.stopped', feedback6_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 7 repeats of 'loop8'


# ------Prepare to start Routine "tip7"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
tip7Components = [tip_7, text_9]
for thisComponent in tip7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
tip7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "tip7"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = tip7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=tip7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tip_7* updates
    if tip_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tip_7.frameNStart = frameN  # exact frame index
        tip_7.tStart = t  # local t and not account for scr refresh
        tip_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tip_7, 'tStartRefresh')  # time at next scr refresh
        tip_7.setAutoDraw(True)
    if tip_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tip_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            tip_7.tStop = t  # not accounting for scr refresh
            tip_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tip_7, 'tStopRefresh')  # time at next scr refresh
            tip_7.setAutoDraw(False)
    
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
        if tThisFlipGlobal > text_9.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_9.tStop = t  # not accounting for scr refresh
            text_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
            text_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in tip7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "tip7"-------
for thisComponent in tip7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tip_7.started', tip_7.tStartRefresh)
thisExp.addData('tip_7.stopped', tip_7.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop9 = data.TrialHandler(nReps=7, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop9')
thisExp.addLoop(loop9)  # add the loop to the experiment
thisLoop9 = loop9.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop9.rgb)
if thisLoop9 != None:
    for paramName in thisLoop9:
        exec('{} = thisLoop9[paramName]'.format(paramName))

for thisLoop9 in loop9:
    currentLoop = loop9
    # abbreviate parameter names if possible (e.g. rgb = thisLoop9.rgb)
    if thisLoop9 != None:
        for paramName in thisLoop9:
            exec('{} = thisLoop9[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "choice_25years"-------
    continueRoutine = True
    # update component parameters for each repeat
    text9_2.setText(x9)
    text9_3.setText('1000\n')
    key_resp25years.keys = []
    key_resp25years.rt = []
    _key_resp25years_allKeys = []
    # keep track of which components have finished
    choice_25yearsComponents = [concentration9, text9_1, text9_2, text9_3, key_resp25years]
    for thisComponent in choice_25yearsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choice_25yearsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice_25years"-------
    while continueRoutine:
        # get current time
        t = choice_25yearsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choice_25yearsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration9* updates
        if concentration9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            concentration9.frameNStart = frameN  # exact frame index
            concentration9.tStart = t  # local t and not account for scr refresh
            concentration9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration9, 'tStartRefresh')  # time at next scr refresh
            concentration9.setAutoDraw(True)
        if concentration9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration9.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                concentration9.tStop = t  # not accounting for scr refresh
                concentration9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration9, 'tStopRefresh')  # time at next scr refresh
                concentration9.setAutoDraw(False)
        
        # *text9_1* updates
        if text9_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text9_1.frameNStart = frameN  # exact frame index
            text9_1.tStart = t  # local t and not account for scr refresh
            text9_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text9_1, 'tStartRefresh')  # time at next scr refresh
            text9_1.setAutoDraw(True)
        
        # *text9_2* updates
        if text9_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text9_2.frameNStart = frameN  # exact frame index
            text9_2.tStart = t  # local t and not account for scr refresh
            text9_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text9_2, 'tStartRefresh')  # time at next scr refresh
            text9_2.setAutoDraw(True)
        
        # *text9_3* updates
        if text9_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text9_3.frameNStart = frameN  # exact frame index
            text9_3.tStart = t  # local t and not account for scr refresh
            text9_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text9_3, 'tStartRefresh')  # time at next scr refresh
            text9_3.setAutoDraw(True)
        
        # *key_resp25years* updates
        waitOnFlip = False
        if key_resp25years.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp25years.frameNStart = frameN  # exact frame index
            key_resp25years.tStart = t  # local t and not account for scr refresh
            key_resp25years.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp25years, 'tStartRefresh')  # time at next scr refresh
            key_resp25years.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp25years.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp25years.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp25years.status == STARTED and not waitOnFlip:
            theseKeys = key_resp25years.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp25years_allKeys.extend(theseKeys)
            if len(_key_resp25years_allKeys):
                key_resp25years.keys = _key_resp25years_allKeys[-1].name  # just the last key pressed
                key_resp25years.rt = _key_resp25years_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choice_25yearsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice_25years"-------
    for thisComponent in choice_25yearsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop9.addData('concentration9.started', concentration9.tStartRefresh)
    loop9.addData('concentration9.stopped', concentration9.tStopRefresh)
    loop9.addData('text9_1.started', text9_1.tStartRefresh)
    loop9.addData('text9_1.stopped', text9_1.tStopRefresh)
    loop9.addData('text9_2.started', text9_2.tStartRefresh)
    loop9.addData('text9_2.stopped', text9_2.tStopRefresh)
    loop9.addData('text9_3.started', text9_3.tStartRefresh)
    loop9.addData('text9_3.stopped', text9_3.tStopRefresh)
    # check responses
    if key_resp25years.keys in ['', [], None]:  # No response was made
        key_resp25years.keys = None
    loop9.addData('key_resp25years.keys',key_resp25years.keys)
    if key_resp25years.keys != None:  # we had a response
        loop9.addData('key_resp25years.rt', key_resp25years.rt)
    loop9.addData('key_resp25years.started', key_resp25years.tStartRefresh)
    loop9.addData('key_resp25years.stopped', key_resp25years.tStopRefresh)
    if 'left'in key_resp25years.keys:
        z7=x9
        x9-=1000/n9
        n9*=2
        y="即时奖励"
    if 'right' in key_resp25years.keys:
        x9+=1000/n9
        n9*=2
        z7=1000
        y="二十五年后的奖励"
    # the Routine "choice_25years" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback7"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    feedback7_1.setText(y)
    feedback7_3.setText(z7)
    # keep track of which components have finished
    feedback7Components = [feedback7_1, feedback7_2, feedback7_3]
    for thisComponent in feedback7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback7"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback7_1* updates
        if feedback7_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback7_1.frameNStart = frameN  # exact frame index
            feedback7_1.tStart = t  # local t and not account for scr refresh
            feedback7_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback7_1, 'tStartRefresh')  # time at next scr refresh
            feedback7_1.setAutoDraw(True)
        if feedback7_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback7_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback7_1.tStop = t  # not accounting for scr refresh
                feedback7_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback7_1, 'tStopRefresh')  # time at next scr refresh
                feedback7_1.setAutoDraw(False)
        
        # *feedback7_2* updates
        if feedback7_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback7_2.frameNStart = frameN  # exact frame index
            feedback7_2.tStart = t  # local t and not account for scr refresh
            feedback7_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback7_2, 'tStartRefresh')  # time at next scr refresh
            feedback7_2.setAutoDraw(True)
        if feedback7_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback7_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback7_2.tStop = t  # not accounting for scr refresh
                feedback7_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback7_2, 'tStopRefresh')  # time at next scr refresh
                feedback7_2.setAutoDraw(False)
        
        # *feedback7_3* updates
        if feedback7_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback7_3.frameNStart = frameN  # exact frame index
            feedback7_3.tStart = t  # local t and not account for scr refresh
            feedback7_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback7_3, 'tStartRefresh')  # time at next scr refresh
            feedback7_3.setAutoDraw(True)
        if feedback7_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback7_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback7_3.tStop = t  # not accounting for scr refresh
                feedback7_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback7_3, 'tStopRefresh')  # time at next scr refresh
                feedback7_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback7"-------
    for thisComponent in feedback7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop9.addData('feedback7_1.started', feedback7_1.tStartRefresh)
    loop9.addData('feedback7_1.stopped', feedback7_1.tStopRefresh)
    loop9.addData('feedback7_2.started', feedback7_2.tStartRefresh)
    loop9.addData('feedback7_2.stopped', feedback7_2.tStopRefresh)
    loop9.addData('feedback7_3.started', feedback7_3.tStartRefresh)
    loop9.addData('feedback7_3.stopped', feedback7_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 7 repeats of 'loop9'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
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
        if tThisFlipGlobal > text_2.tStartRefresh + 2-frameTolerance:
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
