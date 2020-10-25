#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Sun Oct  4 15:49:36 2020
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
psychopyVersion = '3.2.4'
expName = 'cntracs_wm'  # from the Builder filename that created this script
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
    originPath='/Users/shubhaviarya/Desktop/Courses/UMN/tricam/CNTRACS_WM/cntracs_wm_lastrun.py',
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
    size=[1920, 1200], fullscr=True, screen=0, 
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

# Initialize components for Routine "testColors"
testColorsClock = core.Clock()
probeCircle = visual.Polygon(
    win=win, name='probeCircle',
    edges=100, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
testPos0 = visual.Rect(
    win=win, name='testPos0',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0-90, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
testPos20 = visual.Rect(
    win=win, name='testPos20',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=(100-20)*3.6-90, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
testPos40 = visual.Rect(
    win=win, name='testPos40',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=(100-40)*3.6-90, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
testPos60 = visual.Rect(
    win=win, name='testPos60',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=(100-60)*3.6-90, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
testPos80 = visual.Rect(
    win=win, name='testPos80',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=(100-80)*3.6-90, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
testColorsExplained = visual.TextStim(win=win, name='testColorsExplained',
    text='Click the bar whose color matches the central circle.',
    font='Arial',
    pos=(0, -0.3), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
mouseTestColors = event.Mouse(win=win)
x, y = [None, None]
mouseTestColors.mouseClock = core.Clock()
clickablePos0 = visual.Rect(
    win=win, name='clickablePos0',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-8.0, interpolate=True)
clickablePos20 = visual.Rect(
    win=win, name='clickablePos20',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=(100-20)*3.6-90, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-9.0, interpolate=True)
clickablePos40 = visual.Rect(
    win=win, name='clickablePos40',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=(100-40)*3.6-90, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-10.0, interpolate=True)
clickablePos60 = visual.Rect(
    win=win, name='clickablePos60',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=(100-60)*3.6-90, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-11.0, interpolate=True)
clickablePos80 = visual.Rect(
    win=win, name='clickablePos80',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=(100-80)*3.6-90, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-12.0, interpolate=True)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
textInstructions = visual.TextStim(win=win, name='textInstructions',
    text='Welcome!\n\nIn this experiment we will test your memory for the location of some colored rectangles.\n\nTry to remember where each rectangle is located.\n\nWhen the rectangles disappear a single colored circle will appear in the center of the screen.\n\nClick on the screen where you remember having seen a rectangle matching the color of the circle.\n\nClick any button to begin.',
    font='Arial',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouseInstructions = event.Mouse(win=win)
x, y = [None, None]
mouseInstructions.mouseClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
centralFixation = visual.Rect(
    win=win, name='centralFixation',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0),
    lineWidth=2, lineColor=[0.5,0.5,0.5], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
stim1 = visual.Rect(
    win=win, name='stim1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
stim2 = visual.Rect(
    win=win, name='stim2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
stim3 = visual.Rect(
    win=win, name='stim3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
stim4 = visual.Rect(
    win=win, name='stim4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
stim5 = visual.Rect(
    win=win, name='stim5',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)

# Initialize components for Routine "responseDemo"
responseDemoClock = core.Clock()
respRingDemo = visual.Polygon(
    win=win, name='respRingDemo',
    edges=100, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
probeDemo = visual.Polygon(
    win=win, name='probeDemo',
    edges=100, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
mouseResponseDemo = event.Mouse(win=win)
x, y = [None, None]
mouseResponseDemo.mouseClock = core.Clock()
textDemo = visual.TextStim(win=win, name='textDemo',
    text='Click on the ring where you remember having seen a bar whose color matches the color of the circle at screen center.',
    font='Arial',
    pos=(0, -0.3), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
arrowImage = visual.ImageStim(
    win=win,
    name='arrowImage', 
    image='images/arrow.png', mask=None,
    ori=0, pos=[0,0], size=(0.05, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "startBlock"
startBlockClock = core.Clock()
firstTrial = 0
trialsPerBlock = 40
clickToBegin = visual.TextStim(win=win, name='clickToBegin',
    text='When you are ready, click the mouse to begin the task.',
    font='Arial',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouseToStartBlock = event.Mouse(win=win)
x, y = [None, None]
mouseToStartBlock.mouseClock = core.Clock()

# Initialize components for Routine "fixPrepare"
fixPrepareClock = core.Clock()
centralFixation_Long = visual.Rect(
    win=win, name='centralFixation_Long',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0),
    lineWidth=2, lineColor=[0.5,0.5,0.5], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
centralFixation = visual.Rect(
    win=win, name='centralFixation',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0),
    lineWidth=2, lineColor=[0.5,0.5,0.5], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
stim1 = visual.Rect(
    win=win, name='stim1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
stim2 = visual.Rect(
    win=win, name='stim2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
stim3 = visual.Rect(
    win=win, name='stim3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
stim4 = visual.Rect(
    win=win, name='stim4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
stim5 = visual.Rect(
    win=win, name='stim5',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)

# Initialize components for Routine "response"
responseClock = core.Clock()
respRing = visual.Polygon(
    win=win, name='respRing',
    edges=100, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
probe = visual.Polygon(
    win=win, name='probe',
    edges=100, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
mouseResponse = event.Mouse(win=win)
x, y = [None, None]
mouseResponse.mouseClock = core.Clock()
pos0 = visual.Rect(
    win=win, name='pos0',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-4.0, interpolate=True)
pos5 = visual.Rect(
    win=win, name='pos5',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*5, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-5.0, interpolate=True)
pos10 = visual.Rect(
    win=win, name='pos10',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*10, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-6.0, interpolate=True)
pos15 = visual.Rect(
    win=win, name='pos15',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*15, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-7.0, interpolate=True)
pos20 = visual.Rect(
    win=win, name='pos20',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*20, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-8.0, interpolate=True)
pos25 = visual.Rect(
    win=win, name='pos25',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*25, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-9.0, interpolate=True)
pos30 = visual.Rect(
    win=win, name='pos30',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*30, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-10.0, interpolate=True)
pos35 = visual.Rect(
    win=win, name='pos35',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*35, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-11.0, interpolate=True)
pos40 = visual.Rect(
    win=win, name='pos40',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*40, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-12.0, interpolate=True)
pos45 = visual.Rect(
    win=win, name='pos45',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*45, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-13.0, interpolate=True)
pos50 = visual.Rect(
    win=win, name='pos50',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*50, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-14.0, interpolate=True)
pos55 = visual.Rect(
    win=win, name='pos55',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*55, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-15.0, interpolate=True)
pos60 = visual.Rect(
    win=win, name='pos60',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*60, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-16.0, interpolate=True)
pos65 = visual.Rect(
    win=win, name='pos65',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*65, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-17.0, interpolate=True)
pos70 = visual.Rect(
    win=win, name='pos70',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*70, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-18.0, interpolate=True)
pos75 = visual.Rect(
    win=win, name='pos75',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*75, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-19.0, interpolate=True)
pos80 = visual.Rect(
    win=win, name='pos80',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*80, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-20.0, interpolate=True)
pos85 = visual.Rect(
    win=win, name='pos85',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*85, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-21.0, interpolate=True)
pos90 = visual.Rect(
    win=win, name='pos90',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*90, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-22.0, interpolate=True)
pos95 = visual.Rect(
    win=win, name='pos95',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=3.6*95, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-23.0, interpolate=True)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
taskLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('parameterFiles/taskParameters.xlsx'),
    seed=None, name='taskLoop')
thisExp.addLoop(taskLoop)  # add the loop to the experiment
thisTaskLoop = taskLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTaskLoop.rgb)
if thisTaskLoop != None:
    for paramName in thisTaskLoop:
        exec('{} = thisTaskLoop[paramName]'.format(paramName))

for thisTaskLoop in taskLoop:
    currentLoop = taskLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTaskLoop.rgb)
    if thisTaskLoop != None:
        for paramName in thisTaskLoop:
            exec('{} = thisTaskLoop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    testColorsLoop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('parameterFiles/testColorsSequence.xlsx', selection='0:5'),
        seed=None, name='testColorsLoop')
    thisExp.addLoop(testColorsLoop)  # add the loop to the experiment
    thisTestColorsLoop = testColorsLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestColorsLoop.rgb)
    if thisTestColorsLoop != None:
        for paramName in thisTestColorsLoop:
            exec('{} = thisTestColorsLoop[paramName]'.format(paramName))
    
    for thisTestColorsLoop in testColorsLoop:
        currentLoop = testColorsLoop
        # abbreviate parameter names if possible (e.g. rgb = thisTestColorsLoop.rgb)
        if thisTestColorsLoop != None:
            for paramName in thisTestColorsLoop:
                exec('{} = thisTestColorsLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "testColors"-------
        # update component parameters for each repeat
        probeCircle.setSize([fixSize*2,fixSize*2])
        probeCircle.setFillColor(testColorsColor)
        probeCircle.setLineColor(testColorsColor)
        testPos0.setPos([pos0_x,pos0_y])
        testPos0.setSize([stimWidth,stimHeight])
        testPos0.setFillColor(color0)
        testPos0.setLineColor(color0)
        testPos20.setPos([pos20_x,pos20_y])
        testPos20.setSize([stimWidth,stimHeight])
        testPos20.setFillColor(color1)
        testPos20.setLineColor(color1)
        testPos40.setPos([pos40_x,pos40_y])
        testPos40.setSize([stimWidth,stimHeight])
        testPos40.setFillColor(color2)
        testPos40.setLineColor(color2)
        testPos60.setPos([pos60_x,pos60_y])
        testPos60.setSize([stimWidth,stimHeight])
        testPos60.setFillColor(color3)
        testPos60.setLineColor(color3)
        testPos80.setPos([pos80_x,pos80_y])
        testPos80.setSize([stimWidth,stimHeight])
        testPos80.setFillColor(color4)
        testPos80.setLineColor(color4)
        testColorsExplained.setHeight(fontSize)
        # setup some python lists for storing info about the mouseTestColors
        mouseTestColors.clicked_name = []
        gotValidClick = False  # until a click is received
        clickablePos0.setPos([pos0_x,pos0_y])
        clickablePos0.setSize([stimWidth*2,stimHeight*2])
        clickablePos20.setPos([pos20_x,pos20_y])
        clickablePos20.setSize([stimWidth*2,stimHeight*2])
        clickablePos40.setPos([pos40_x,pos40_y])
        clickablePos40.setSize([stimWidth*2,stimHeight*2])
        clickablePos60.setPos([pos60_x,pos60_y])
        clickablePos60.setSize([stimWidth*2,stimHeight*2])
        clickablePos80.setPos([pos80_x,pos80_y])
        clickablePos80.setSize([stimWidth*2,stimHeight*2])
        # keep track of which components have finished
        testColorsComponents = [probeCircle, testPos0, testPos20, testPos40, testPos60, testPos80, testColorsExplained, mouseTestColors, clickablePos0, clickablePos20, clickablePos40, clickablePos60, clickablePos80]
        for thisComponent in testColorsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        testColorsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "testColors"-------
        while continueRoutine:
            # get current time
            t = testColorsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=testColorsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *probeCircle* updates
            if probeCircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probeCircle.frameNStart = frameN  # exact frame index
                probeCircle.tStart = t  # local t and not account for scr refresh
                probeCircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probeCircle, 'tStartRefresh')  # time at next scr refresh
                probeCircle.setAutoDraw(True)
            
            # *testPos0* updates
            if testPos0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                testPos0.frameNStart = frameN  # exact frame index
                testPos0.tStart = t  # local t and not account for scr refresh
                testPos0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testPos0, 'tStartRefresh')  # time at next scr refresh
                testPos0.setAutoDraw(True)
            
            # *testPos20* updates
            if testPos20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                testPos20.frameNStart = frameN  # exact frame index
                testPos20.tStart = t  # local t and not account for scr refresh
                testPos20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testPos20, 'tStartRefresh')  # time at next scr refresh
                testPos20.setAutoDraw(True)
            
            # *testPos40* updates
            if testPos40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                testPos40.frameNStart = frameN  # exact frame index
                testPos40.tStart = t  # local t and not account for scr refresh
                testPos40.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testPos40, 'tStartRefresh')  # time at next scr refresh
                testPos40.setAutoDraw(True)
            
            # *testPos60* updates
            if testPos60.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                testPos60.frameNStart = frameN  # exact frame index
                testPos60.tStart = t  # local t and not account for scr refresh
                testPos60.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testPos60, 'tStartRefresh')  # time at next scr refresh
                testPos60.setAutoDraw(True)
            
            # *testPos80* updates
            if testPos80.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                testPos80.frameNStart = frameN  # exact frame index
                testPos80.tStart = t  # local t and not account for scr refresh
                testPos80.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testPos80, 'tStartRefresh')  # time at next scr refresh
                testPos80.setAutoDraw(True)
            
            # *testColorsExplained* updates
            if testColorsExplained.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                testColorsExplained.frameNStart = frameN  # exact frame index
                testColorsExplained.tStart = t  # local t and not account for scr refresh
                testColorsExplained.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testColorsExplained, 'tStartRefresh')  # time at next scr refresh
                testColorsExplained.setAutoDraw(True)
            # *mouseTestColors* updates
            if mouseTestColors.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseTestColors.frameNStart = frameN  # exact frame index
                mouseTestColors.tStart = t  # local t and not account for scr refresh
                mouseTestColors.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseTestColors, 'tStartRefresh')  # time at next scr refresh
                mouseTestColors.status = STARTED
                mouseTestColors.mouseClock.reset()
                prevButtonState = mouseTestColors.getPressed()  # if button is down already this ISN'T a new click
            if mouseTestColors.status == STARTED:  # only update if started and not finished!
                buttons = mouseTestColors.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [clickablePos0,clickablePos20,clickablePos40,clickablePos60,clickablePos80]:
                            if obj.contains(mouseTestColors):
                                gotValidClick = True
                                mouseTestColors.clicked_name.append(obj.name)
                        # abort routine on response
                        continueRoutine = False
            
            # *clickablePos0* updates
            if clickablePos0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clickablePos0.frameNStart = frameN  # exact frame index
                clickablePos0.tStart = t  # local t and not account for scr refresh
                clickablePos0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clickablePos0, 'tStartRefresh')  # time at next scr refresh
                clickablePos0.setAutoDraw(True)
            
            # *clickablePos20* updates
            if clickablePos20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clickablePos20.frameNStart = frameN  # exact frame index
                clickablePos20.tStart = t  # local t and not account for scr refresh
                clickablePos20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clickablePos20, 'tStartRefresh')  # time at next scr refresh
                clickablePos20.setAutoDraw(True)
            
            # *clickablePos40* updates
            if clickablePos40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clickablePos40.frameNStart = frameN  # exact frame index
                clickablePos40.tStart = t  # local t and not account for scr refresh
                clickablePos40.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clickablePos40, 'tStartRefresh')  # time at next scr refresh
                clickablePos40.setAutoDraw(True)
            
            # *clickablePos60* updates
            if clickablePos60.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clickablePos60.frameNStart = frameN  # exact frame index
                clickablePos60.tStart = t  # local t and not account for scr refresh
                clickablePos60.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clickablePos60, 'tStartRefresh')  # time at next scr refresh
                clickablePos60.setAutoDraw(True)
            
            # *clickablePos80* updates
            if clickablePos80.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clickablePos80.frameNStart = frameN  # exact frame index
                clickablePos80.tStart = t  # local t and not account for scr refresh
                clickablePos80.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clickablePos80, 'tStartRefresh')  # time at next scr refresh
                clickablePos80.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in testColorsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "testColors"-------
        for thisComponent in testColorsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        testColorsLoop.addData('testColorsExplained.started', testColorsExplained.tStartRefresh)
        testColorsLoop.addData('testColorsExplained.stopped', testColorsExplained.tStopRefresh)
        # store data for testColorsLoop (TrialHandler)
        x, y = mouseTestColors.getPos()
        buttons = mouseTestColors.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [clickablePos0,clickablePos20,clickablePos40,clickablePos60,clickablePos80]:
                if obj.contains(mouseTestColors):
                    gotValidClick = True
                    mouseTestColors.clicked_name.append(obj.name)
        testColorsLoop.addData('mouseTestColors.x', x)
        testColorsLoop.addData('mouseTestColors.y', y)
        testColorsLoop.addData('mouseTestColors.leftButton', buttons[0])
        testColorsLoop.addData('mouseTestColors.midButton', buttons[1])
        testColorsLoop.addData('mouseTestColors.rightButton', buttons[2])
        if len(mouseTestColors.clicked_name):
            testColorsLoop.addData('mouseTestColors.clicked_name', mouseTestColors.clicked_name[0])
        testColorsLoop.addData('clickablePos0.started', clickablePos0.tStartRefresh)
        testColorsLoop.addData('clickablePos0.stopped', clickablePos0.tStopRefresh)
        testColorsLoop.addData('clickablePos20.started', clickablePos20.tStartRefresh)
        testColorsLoop.addData('clickablePos20.stopped', clickablePos20.tStopRefresh)
        testColorsLoop.addData('clickablePos40.started', clickablePos40.tStartRefresh)
        testColorsLoop.addData('clickablePos40.stopped', clickablePos40.tStopRefresh)
        testColorsLoop.addData('clickablePos60.started', clickablePos60.tStartRefresh)
        testColorsLoop.addData('clickablePos60.stopped', clickablePos60.tStopRefresh)
        testColorsLoop.addData('clickablePos80.started', clickablePos80.tStartRefresh)
        testColorsLoop.addData('clickablePos80.stopped', clickablePos80.tStopRefresh)
        # the Routine "testColors" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'testColorsLoop'
    
    
    # ------Prepare to start Routine "instructions"-------
    # update component parameters for each repeat
    textInstructions.setHeight(fontSize)
    # setup some python lists for storing info about the mouseInstructions
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionsComponents = [textInstructions, mouseInstructions]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInstructions* updates
        if textInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstructions.frameNStart = frameN  # exact frame index
            textInstructions.tStart = t  # local t and not account for scr refresh
            textInstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructions, 'tStartRefresh')  # time at next scr refresh
            textInstructions.setAutoDraw(True)
        # *mouseInstructions* updates
        if mouseInstructions.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseInstructions.frameNStart = frameN  # exact frame index
            mouseInstructions.tStart = t  # local t and not account for scr refresh
            mouseInstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseInstructions, 'tStartRefresh')  # time at next scr refresh
            mouseInstructions.status = STARTED
            mouseInstructions.mouseClock.reset()
            prevButtonState = mouseInstructions.getPressed()  # if button is down already this ISN'T a new click
        if mouseInstructions.status == STARTED:  # only update if started and not finished!
            buttons = mouseInstructions.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for taskLoop (TrialHandler)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    demoTrials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('parameterFiles/trialDemoSequence_forJS.xlsx'),
        seed=None, name='demoTrials')
    thisExp.addLoop(demoTrials)  # add the loop to the experiment
    thisDemoTrial = demoTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDemoTrial.rgb)
    if thisDemoTrial != None:
        for paramName in thisDemoTrial:
            exec('{} = thisDemoTrial[paramName]'.format(paramName))
    
    for thisDemoTrial in demoTrials:
        currentLoop = demoTrials
        # abbreviate parameter names if possible (e.g. rgb = thisDemoTrial.rgb)
        if thisDemoTrial != None:
            for paramName in thisDemoTrial:
                exec('{} = thisDemoTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        # update component parameters for each repeat
        centralFixation.setSize([fixSize,fixSize])
        stim1.setPos([stim1_x, stim1_y])
        stim1.setSize([stimWidth,stimHeight])
        stim1.setOri(stim1_orientation)
        stim1.setFillColor(stim1_color)
        stim1.setLineColor(stim1_color)
        stim2.setPos([stim2_x,stim2_y])
        stim2.setSize([stimWidth,stimHeight])
        stim2.setOri(stim2_orientation)
        stim2.setFillColor(stim2_color)
        stim2.setLineColor(stim2_color)
        stim3.setPos([stim3_x,stim3_y])
        stim3.setSize([stimWidth,stimHeight])
        stim3.setOri(stim3_orientation)
        stim3.setFillColor(stim3_color)
        stim3.setLineColor(stim3_color)
        stim4.setPos([stim4_x,stim4_y])
        stim4.setSize([stimWidth,stimHeight])
        stim4.setOri(stim4_orientation)
        stim4.setFillColor(stim4_color)
        stim4.setLineColor(stim4_color)
        stim5.setPos([stim5_x,stim5_y])
        stim5.setSize([stimWidth,stimHeight])
        stim5.setOri(stim5_orientation)
        stim5.setFillColor(stim5_color)
        stim5.setLineColor(stim5_color)
        # keep track of which components have finished
        trialComponents = [centralFixation, stim1, stim2, stim3, stim4, stim5]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *centralFixation* updates
            if centralFixation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                centralFixation.frameNStart = frameN  # exact frame index
                centralFixation.tStart = t  # local t and not account for scr refresh
                centralFixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(centralFixation, 'tStartRefresh')  # time at next scr refresh
                centralFixation.setAutoDraw(True)
            if centralFixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > centralFixation.tStartRefresh + preProbeDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    centralFixation.tStop = t  # not accounting for scr refresh
                    centralFixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(centralFixation, 'tStopRefresh')  # time at next scr refresh
                    centralFixation.setAutoDraw(False)
            
            # *stim1* updates
            if stim1.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                # keep track of start time/frame for later
                stim1.frameNStart = frameN  # exact frame index
                stim1.tStart = t  # local t and not account for scr refresh
                stim1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim1, 'tStartRefresh')  # time at next scr refresh
                stim1.setAutoDraw(True)
            if stim1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim1.tStartRefresh + stimDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    stim1.tStop = t  # not accounting for scr refresh
                    stim1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim1, 'tStopRefresh')  # time at next scr refresh
                    stim1.setAutoDraw(False)
            
            # *stim2* updates
            if stim2.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                # keep track of start time/frame for later
                stim2.frameNStart = frameN  # exact frame index
                stim2.tStart = t  # local t and not account for scr refresh
                stim2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim2, 'tStartRefresh')  # time at next scr refresh
                stim2.setAutoDraw(True)
            if stim2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim2.tStartRefresh + stimDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    stim2.tStop = t  # not accounting for scr refresh
                    stim2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim2, 'tStopRefresh')  # time at next scr refresh
                    stim2.setAutoDraw(False)
            
            # *stim3* updates
            if stim3.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                # keep track of start time/frame for later
                stim3.frameNStart = frameN  # exact frame index
                stim3.tStart = t  # local t and not account for scr refresh
                stim3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim3, 'tStartRefresh')  # time at next scr refresh
                stim3.setAutoDraw(True)
            if stim3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim3.tStartRefresh + stimDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    stim3.tStop = t  # not accounting for scr refresh
                    stim3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim3, 'tStopRefresh')  # time at next scr refresh
                    stim3.setAutoDraw(False)
            
            # *stim4* updates
            if stim4.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                # keep track of start time/frame for later
                stim4.frameNStart = frameN  # exact frame index
                stim4.tStart = t  # local t and not account for scr refresh
                stim4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim4, 'tStartRefresh')  # time at next scr refresh
                stim4.setAutoDraw(True)
            if stim4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim4.tStartRefresh + stimDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    stim4.tStop = t  # not accounting for scr refresh
                    stim4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim4, 'tStopRefresh')  # time at next scr refresh
                    stim4.setAutoDraw(False)
            
            # *stim5* updates
            if stim5.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                # keep track of start time/frame for later
                stim5.frameNStart = frameN  # exact frame index
                stim5.tStart = t  # local t and not account for scr refresh
                stim5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim5, 'tStartRefresh')  # time at next scr refresh
                stim5.setAutoDraw(True)
            if stim5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim5.tStartRefresh + stimDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    stim5.tStop = t  # not accounting for scr refresh
                    stim5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim5, 'tStopRefresh')  # time at next scr refresh
                    stim5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        demoTrials.addData('centralFixation.started', centralFixation.tStartRefresh)
        demoTrials.addData('centralFixation.stopped', centralFixation.tStopRefresh)
        demoTrials.addData('stim4.started', stim4.tStartRefresh)
        demoTrials.addData('stim4.stopped', stim4.tStopRefresh)
        demoTrials.addData('stim5.started', stim5.tStartRefresh)
        demoTrials.addData('stim5.stopped', stim5.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "responseDemo"-------
        # update component parameters for each repeat
        respRingDemo.setSize([stimRadius*2,stimRadius*2])
        probeDemo.setSize([fixSize*2,fixSize*2])
        probeDemo.setFillColor(stim1_color)
        probeDemo.setLineColor(stim1_color)
        # setup some python lists for storing info about the mouseResponseDemo
        gotValidClick = False  # until a click is received
        textDemo.setHeight(fontSize)
        arrowImage.setPos([stim1_x+0.025,stim1_y+0.025])
        # keep track of which components have finished
        responseDemoComponents = [respRingDemo, probeDemo, mouseResponseDemo, textDemo, arrowImage]
        for thisComponent in responseDemoComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        responseDemoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "responseDemo"-------
        while continueRoutine:
            # get current time
            t = responseDemoClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=responseDemoClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *respRingDemo* updates
            if respRingDemo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respRingDemo.frameNStart = frameN  # exact frame index
                respRingDemo.tStart = t  # local t and not account for scr refresh
                respRingDemo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respRingDemo, 'tStartRefresh')  # time at next scr refresh
                respRingDemo.setAutoDraw(True)
            
            # *probeDemo* updates
            if probeDemo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probeDemo.frameNStart = frameN  # exact frame index
                probeDemo.tStart = t  # local t and not account for scr refresh
                probeDemo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probeDemo, 'tStartRefresh')  # time at next scr refresh
                probeDemo.setAutoDraw(True)
            # *mouseResponseDemo* updates
            if mouseResponseDemo.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseResponseDemo.frameNStart = frameN  # exact frame index
                mouseResponseDemo.tStart = t  # local t and not account for scr refresh
                mouseResponseDemo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseResponseDemo, 'tStartRefresh')  # time at next scr refresh
                mouseResponseDemo.status = STARTED
                mouseResponseDemo.mouseClock.reset()
                prevButtonState = mouseResponseDemo.getPressed()  # if button is down already this ISN'T a new click
            if mouseResponseDemo.status == STARTED:  # only update if started and not finished!
                buttons = mouseResponseDemo.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # abort routine on response
                        continueRoutine = False
            
            # *textDemo* updates
            if textDemo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textDemo.frameNStart = frameN  # exact frame index
                textDemo.tStart = t  # local t and not account for scr refresh
                textDemo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textDemo, 'tStartRefresh')  # time at next scr refresh
                textDemo.setAutoDraw(True)
            
            # *arrowImage* updates
            if arrowImage.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                arrowImage.frameNStart = frameN  # exact frame index
                arrowImage.tStart = t  # local t and not account for scr refresh
                arrowImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrowImage, 'tStartRefresh')  # time at next scr refresh
                arrowImage.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseDemoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "responseDemo"-------
        for thisComponent in responseDemoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        demoTrials.addData('respRingDemo.started', respRingDemo.tStartRefresh)
        demoTrials.addData('respRingDemo.stopped', respRingDemo.tStopRefresh)
        demoTrials.addData('probeDemo.started', probeDemo.tStartRefresh)
        demoTrials.addData('probeDemo.stopped', probeDemo.tStopRefresh)
        # store data for demoTrials (TrialHandler)
        x, y = mouseResponseDemo.getPos()
        buttons = mouseResponseDemo.getPressed()
        demoTrials.addData('mouseResponseDemo.x', x)
        demoTrials.addData('mouseResponseDemo.y', y)
        demoTrials.addData('mouseResponseDemo.leftButton', buttons[0])
        demoTrials.addData('mouseResponseDemo.midButton', buttons[1])
        demoTrials.addData('mouseResponseDemo.rightButton', buttons[2])
        demoTrials.addData('mouseResponseDemo.started', mouseResponseDemo.tStart)
        demoTrials.addData('mouseResponseDemo.stopped', mouseResponseDemo.tStop)
        demoTrials.addData('textDemo.started', textDemo.tStartRefresh)
        demoTrials.addData('textDemo.stopped', textDemo.tStopRefresh)
        demoTrials.addData('arrowImage.started', arrowImage.tStartRefresh)
        demoTrials.addData('arrowImage.stopped', arrowImage.tStopRefresh)
        # the Routine "responseDemo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ITI"-------
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = [ISI]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "ITI"-------
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ITIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *ISI* period
            if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI.frameNStart = frameN  # exact frame index
                ISI.tStart = t  # local t and not account for scr refresh
                ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                ISI.start(durITI)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                ISI.complete()  # finish the static period
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        demoTrials.addData('ISI.started', ISI.tStart)
        demoTrials.addData('ISI.stopped', ISI.tStop)
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'demoTrials'
    
    
    # set up handler to look after randomisation of conditions etc
    blockOfTrials = data.TrialHandler(nReps=10, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockOfTrials')
    thisExp.addLoop(blockOfTrials)  # add the loop to the experiment
    thisBlockOfTrial = blockOfTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockOfTrial.rgb)
    if thisBlockOfTrial != None:
        for paramName in thisBlockOfTrial:
            exec('{} = thisBlockOfTrial[paramName]'.format(paramName))
    
    for thisBlockOfTrial in blockOfTrials:
        currentLoop = blockOfTrials
        # abbreviate parameter names if possible (e.g. rgb = thisBlockOfTrial.rgb)
        if thisBlockOfTrial != None:
            for paramName in thisBlockOfTrial:
                exec('{} = thisBlockOfTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "startBlock"-------
        # update component parameters for each repeat
        currentBlockRows = str(firstTrial) + ":" + str(firstTrial+trialsPerBlock-1)
        firstTrial = firstTrial+trialsPerBlock
        clickToBegin.setHeight(fontSize)
        # setup some python lists for storing info about the mouseToStartBlock
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        startBlockComponents = [clickToBegin, mouseToStartBlock]
        for thisComponent in startBlockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        startBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "startBlock"-------
        while continueRoutine:
            # get current time
            t = startBlockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=startBlockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *clickToBegin* updates
            if clickToBegin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clickToBegin.frameNStart = frameN  # exact frame index
                clickToBegin.tStart = t  # local t and not account for scr refresh
                clickToBegin.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clickToBegin, 'tStartRefresh')  # time at next scr refresh
                clickToBegin.setAutoDraw(True)
            # *mouseToStartBlock* updates
            if mouseToStartBlock.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseToStartBlock.frameNStart = frameN  # exact frame index
                mouseToStartBlock.tStart = t  # local t and not account for scr refresh
                mouseToStartBlock.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseToStartBlock, 'tStartRefresh')  # time at next scr refresh
                mouseToStartBlock.status = STARTED
                mouseToStartBlock.mouseClock.reset()
                prevButtonState = mouseToStartBlock.getPressed()  # if button is down already this ISN'T a new click
            if mouseToStartBlock.status == STARTED:  # only update if started and not finished!
                buttons = mouseToStartBlock.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in startBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "startBlock"-------
        for thisComponent in startBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blockOfTrials.addData('clickToBegin.started', clickToBegin.tStartRefresh)
        blockOfTrials.addData('clickToBegin.stopped', clickToBegin.tStopRefresh)
        # store data for blockOfTrials (TrialHandler)
        # the Routine "startBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixPrepare"-------
        # update component parameters for each repeat
        centralFixation_Long.setSize([fixSize,fixSize])
        # keep track of which components have finished
        fixPrepareComponents = [centralFixation_Long]
        for thisComponent in fixPrepareComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixPrepareClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "fixPrepare"-------
        while continueRoutine:
            # get current time
            t = fixPrepareClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixPrepareClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *centralFixation_Long* updates
            if centralFixation_Long.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                centralFixation_Long.frameNStart = frameN  # exact frame index
                centralFixation_Long.tStart = t  # local t and not account for scr refresh
                centralFixation_Long.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(centralFixation_Long, 'tStartRefresh')  # time at next scr refresh
                centralFixation_Long.setAutoDraw(True)
            if centralFixation_Long.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > centralFixation_Long.tStartRefresh + fixDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    centralFixation_Long.tStop = t  # not accounting for scr refresh
                    centralFixation_Long.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(centralFixation_Long, 'tStopRefresh')  # time at next scr refresh
                    centralFixation_Long.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixPrepareComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixPrepare"-------
        for thisComponent in fixPrepareComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "fixPrepare" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('parameterFiles/trialSequence_forJS.xlsx', selection=currentBlockRows),
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
            
            # ------Prepare to start Routine "trial"-------
            # update component parameters for each repeat
            centralFixation.setSize([fixSize,fixSize])
            stim1.setPos([stim1_x, stim1_y])
            stim1.setSize([stimWidth,stimHeight])
            stim1.setOri(stim1_orientation)
            stim1.setFillColor(stim1_color)
            stim1.setLineColor(stim1_color)
            stim2.setPos([stim2_x,stim2_y])
            stim2.setSize([stimWidth,stimHeight])
            stim2.setOri(stim2_orientation)
            stim2.setFillColor(stim2_color)
            stim2.setLineColor(stim2_color)
            stim3.setPos([stim3_x,stim3_y])
            stim3.setSize([stimWidth,stimHeight])
            stim3.setOri(stim3_orientation)
            stim3.setFillColor(stim3_color)
            stim3.setLineColor(stim3_color)
            stim4.setPos([stim4_x,stim4_y])
            stim4.setSize([stimWidth,stimHeight])
            stim4.setOri(stim4_orientation)
            stim4.setFillColor(stim4_color)
            stim4.setLineColor(stim4_color)
            stim5.setPos([stim5_x,stim5_y])
            stim5.setSize([stimWidth,stimHeight])
            stim5.setOri(stim5_orientation)
            stim5.setFillColor(stim5_color)
            stim5.setLineColor(stim5_color)
            # keep track of which components have finished
            trialComponents = [centralFixation, stim1, stim2, stim3, stim4, stim5]
            for thisComponent in trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "trial"-------
            while continueRoutine:
                # get current time
                t = trialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *centralFixation* updates
                if centralFixation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    centralFixation.frameNStart = frameN  # exact frame index
                    centralFixation.tStart = t  # local t and not account for scr refresh
                    centralFixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(centralFixation, 'tStartRefresh')  # time at next scr refresh
                    centralFixation.setAutoDraw(True)
                if centralFixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > centralFixation.tStartRefresh + preProbeDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        centralFixation.tStop = t  # not accounting for scr refresh
                        centralFixation.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(centralFixation, 'tStopRefresh')  # time at next scr refresh
                        centralFixation.setAutoDraw(False)
                
                # *stim1* updates
                if stim1.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                    # keep track of start time/frame for later
                    stim1.frameNStart = frameN  # exact frame index
                    stim1.tStart = t  # local t and not account for scr refresh
                    stim1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim1, 'tStartRefresh')  # time at next scr refresh
                    stim1.setAutoDraw(True)
                if stim1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim1.tStartRefresh + stimDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        stim1.tStop = t  # not accounting for scr refresh
                        stim1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(stim1, 'tStopRefresh')  # time at next scr refresh
                        stim1.setAutoDraw(False)
                
                # *stim2* updates
                if stim2.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                    # keep track of start time/frame for later
                    stim2.frameNStart = frameN  # exact frame index
                    stim2.tStart = t  # local t and not account for scr refresh
                    stim2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim2, 'tStartRefresh')  # time at next scr refresh
                    stim2.setAutoDraw(True)
                if stim2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim2.tStartRefresh + stimDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        stim2.tStop = t  # not accounting for scr refresh
                        stim2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(stim2, 'tStopRefresh')  # time at next scr refresh
                        stim2.setAutoDraw(False)
                
                # *stim3* updates
                if stim3.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                    # keep track of start time/frame for later
                    stim3.frameNStart = frameN  # exact frame index
                    stim3.tStart = t  # local t and not account for scr refresh
                    stim3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim3, 'tStartRefresh')  # time at next scr refresh
                    stim3.setAutoDraw(True)
                if stim3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim3.tStartRefresh + stimDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        stim3.tStop = t  # not accounting for scr refresh
                        stim3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(stim3, 'tStopRefresh')  # time at next scr refresh
                        stim3.setAutoDraw(False)
                
                # *stim4* updates
                if stim4.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                    # keep track of start time/frame for later
                    stim4.frameNStart = frameN  # exact frame index
                    stim4.tStart = t  # local t and not account for scr refresh
                    stim4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim4, 'tStartRefresh')  # time at next scr refresh
                    stim4.setAutoDraw(True)
                if stim4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim4.tStartRefresh + stimDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        stim4.tStop = t  # not accounting for scr refresh
                        stim4.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(stim4, 'tStopRefresh')  # time at next scr refresh
                        stim4.setAutoDraw(False)
                
                # *stim5* updates
                if stim5.status == NOT_STARTED and tThisFlip >= fixDuration-frameTolerance:
                    # keep track of start time/frame for later
                    stim5.frameNStart = frameN  # exact frame index
                    stim5.tStart = t  # local t and not account for scr refresh
                    stim5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim5, 'tStartRefresh')  # time at next scr refresh
                    stim5.setAutoDraw(True)
                if stim5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim5.tStartRefresh + stimDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        stim5.tStop = t  # not accounting for scr refresh
                        stim5.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(stim5, 'tStopRefresh')  # time at next scr refresh
                        stim5.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('centralFixation.started', centralFixation.tStartRefresh)
            trials.addData('centralFixation.stopped', centralFixation.tStopRefresh)
            trials.addData('stim4.started', stim4.tStartRefresh)
            trials.addData('stim4.stopped', stim4.tStopRefresh)
            trials.addData('stim5.started', stim5.tStartRefresh)
            trials.addData('stim5.stopped', stim5.tStopRefresh)
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "response"-------
            # update component parameters for each repeat
            respRing.setSize([stimRadius*2,stimRadius*2])
            probe.setSize([fixSize*2,fixSize*2])
            probe.setFillColor(stim1_color)
            probe.setLineColor(stim1_color)
            # setup some python lists for storing info about the mouseResponse
            mouseResponse.clicked_name = []
            gotValidClick = False  # until a click is received
            pos0.setPos([pos0_x,pos0_y])
            pos0.setSize([stimHeight*2,stimHeight*2])
            pos5.setPos([pos5_x,pos5_y])
            pos5.setSize([stimHeight*2,stimHeight*2])
            pos10.setPos([pos10_x,pos10_y])
            pos10.setSize([stimHeight*2,stimHeight*2])
            pos15.setPos([pos15_x,pos15_y])
            pos15.setSize([stimHeight*2,stimHeight*2])
            pos20.setPos([pos20_x,pos20_y])
            pos20.setSize([stimHeight*2,stimHeight*2])
            pos25.setPos([pos25_x,pos25_y])
            pos25.setSize([stimHeight*2,stimHeight*2])
            pos30.setPos([pos30_x,pos30_y])
            pos30.setSize([stimHeight*2,stimHeight*2])
            pos35.setPos([pos35_x,pos35_y])
            pos35.setSize([stimHeight*2,stimHeight*2])
            pos40.setPos([pos40_x,pos40_y])
            pos40.setSize([stimHeight*2,stimHeight*2])
            pos45.setPos([pos45_x,pos45_y])
            pos45.setSize([stimHeight*2,stimHeight*2])
            pos50.setPos([pos50_x,pos50_y])
            pos50.setSize([stimHeight*2,stimHeight*2])
            pos55.setPos([pos55_x,pos55_y])
            pos55.setSize([stimHeight*2,stimHeight*2])
            pos60.setPos([pos60_x,pos60_y])
            pos60.setSize([stimHeight*2,stimHeight*2])
            pos65.setPos([pos65_x,pos65_y])
            pos65.setSize([stimHeight*2,stimHeight*2])
            pos70.setPos([pos70_x,pos70_y])
            pos70.setSize([stimHeight*2,stimHeight*2])
            pos75.setPos([pos75_x,pos75_y])
            pos75.setSize([stimHeight*2,stimHeight*2])
            pos80.setPos([pos80_x,pos80_y])
            pos80.setSize([stimHeight*2,stimHeight*2])
            pos85.setPos([pos85_x,pos85_y])
            pos85.setSize([stimHeight*2,stimHeight*2])
            pos90.setPos([pos90_x,pos90_y])
            pos90.setSize([stimHeight*2,stimHeight*2])
            pos95.setPos([pos95_x,pos95_y])
            pos95.setSize([stimHeight*2,stimHeight*2])
            # keep track of which components have finished
            responseComponents = [respRing, probe, mouseResponse, pos0, pos5, pos10, pos15, pos20, pos25, pos30, pos35, pos40, pos45, pos50, pos55, pos60, pos65, pos70, pos75, pos80, pos85, pos90, pos95]
            for thisComponent in responseComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "response"-------
            while continueRoutine:
                # get current time
                t = responseClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=responseClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *respRing* updates
                if respRing.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    respRing.frameNStart = frameN  # exact frame index
                    respRing.tStart = t  # local t and not account for scr refresh
                    respRing.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(respRing, 'tStartRefresh')  # time at next scr refresh
                    respRing.setAutoDraw(True)
                
                # *probe* updates
                if probe.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    probe.frameNStart = frameN  # exact frame index
                    probe.tStart = t  # local t and not account for scr refresh
                    probe.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(probe, 'tStartRefresh')  # time at next scr refresh
                    probe.setAutoDraw(True)
                # *mouseResponse* updates
                if mouseResponse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouseResponse.frameNStart = frameN  # exact frame index
                    mouseResponse.tStart = t  # local t and not account for scr refresh
                    mouseResponse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouseResponse, 'tStartRefresh')  # time at next scr refresh
                    mouseResponse.status = STARTED
                    mouseResponse.mouseClock.reset()
                    prevButtonState = mouseResponse.getPressed()  # if button is down already this ISN'T a new click
                if mouseResponse.status == STARTED:  # only update if started and not finished!
                    buttons = mouseResponse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [pos0,pos5,pos10,pos15,pos20,pos25,pos30,pos35,pos40,pos45,pos50,pos55,pos60,pos65,pos70,pos75,pos80,pos85,pos90,pos95]:
                                if obj.contains(mouseResponse):
                                    gotValidClick = True
                                    mouseResponse.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *pos0* updates
                if pos0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos0.frameNStart = frameN  # exact frame index
                    pos0.tStart = t  # local t and not account for scr refresh
                    pos0.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos0, 'tStartRefresh')  # time at next scr refresh
                    pos0.setAutoDraw(True)
                
                # *pos5* updates
                if pos5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos5.frameNStart = frameN  # exact frame index
                    pos5.tStart = t  # local t and not account for scr refresh
                    pos5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos5, 'tStartRefresh')  # time at next scr refresh
                    pos5.setAutoDraw(True)
                
                # *pos10* updates
                if pos10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos10.frameNStart = frameN  # exact frame index
                    pos10.tStart = t  # local t and not account for scr refresh
                    pos10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos10, 'tStartRefresh')  # time at next scr refresh
                    pos10.setAutoDraw(True)
                
                # *pos15* updates
                if pos15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos15.frameNStart = frameN  # exact frame index
                    pos15.tStart = t  # local t and not account for scr refresh
                    pos15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos15, 'tStartRefresh')  # time at next scr refresh
                    pos15.setAutoDraw(True)
                
                # *pos20* updates
                if pos20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos20.frameNStart = frameN  # exact frame index
                    pos20.tStart = t  # local t and not account for scr refresh
                    pos20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos20, 'tStartRefresh')  # time at next scr refresh
                    pos20.setAutoDraw(True)
                
                # *pos25* updates
                if pos25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos25.frameNStart = frameN  # exact frame index
                    pos25.tStart = t  # local t and not account for scr refresh
                    pos25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos25, 'tStartRefresh')  # time at next scr refresh
                    pos25.setAutoDraw(True)
                
                # *pos30* updates
                if pos30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos30.frameNStart = frameN  # exact frame index
                    pos30.tStart = t  # local t and not account for scr refresh
                    pos30.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos30, 'tStartRefresh')  # time at next scr refresh
                    pos30.setAutoDraw(True)
                
                # *pos35* updates
                if pos35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos35.frameNStart = frameN  # exact frame index
                    pos35.tStart = t  # local t and not account for scr refresh
                    pos35.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos35, 'tStartRefresh')  # time at next scr refresh
                    pos35.setAutoDraw(True)
                
                # *pos40* updates
                if pos40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos40.frameNStart = frameN  # exact frame index
                    pos40.tStart = t  # local t and not account for scr refresh
                    pos40.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos40, 'tStartRefresh')  # time at next scr refresh
                    pos40.setAutoDraw(True)
                
                # *pos45* updates
                if pos45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos45.frameNStart = frameN  # exact frame index
                    pos45.tStart = t  # local t and not account for scr refresh
                    pos45.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos45, 'tStartRefresh')  # time at next scr refresh
                    pos45.setAutoDraw(True)
                
                # *pos50* updates
                if pos50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos50.frameNStart = frameN  # exact frame index
                    pos50.tStart = t  # local t and not account for scr refresh
                    pos50.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos50, 'tStartRefresh')  # time at next scr refresh
                    pos50.setAutoDraw(True)
                
                # *pos55* updates
                if pos55.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos55.frameNStart = frameN  # exact frame index
                    pos55.tStart = t  # local t and not account for scr refresh
                    pos55.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos55, 'tStartRefresh')  # time at next scr refresh
                    pos55.setAutoDraw(True)
                
                # *pos60* updates
                if pos60.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos60.frameNStart = frameN  # exact frame index
                    pos60.tStart = t  # local t and not account for scr refresh
                    pos60.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos60, 'tStartRefresh')  # time at next scr refresh
                    pos60.setAutoDraw(True)
                
                # *pos65* updates
                if pos65.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos65.frameNStart = frameN  # exact frame index
                    pos65.tStart = t  # local t and not account for scr refresh
                    pos65.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos65, 'tStartRefresh')  # time at next scr refresh
                    pos65.setAutoDraw(True)
                
                # *pos70* updates
                if pos70.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos70.frameNStart = frameN  # exact frame index
                    pos70.tStart = t  # local t and not account for scr refresh
                    pos70.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos70, 'tStartRefresh')  # time at next scr refresh
                    pos70.setAutoDraw(True)
                
                # *pos75* updates
                if pos75.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos75.frameNStart = frameN  # exact frame index
                    pos75.tStart = t  # local t and not account for scr refresh
                    pos75.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos75, 'tStartRefresh')  # time at next scr refresh
                    pos75.setAutoDraw(True)
                
                # *pos80* updates
                if pos80.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos80.frameNStart = frameN  # exact frame index
                    pos80.tStart = t  # local t and not account for scr refresh
                    pos80.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos80, 'tStartRefresh')  # time at next scr refresh
                    pos80.setAutoDraw(True)
                
                # *pos85* updates
                if pos85.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos85.frameNStart = frameN  # exact frame index
                    pos85.tStart = t  # local t and not account for scr refresh
                    pos85.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos85, 'tStartRefresh')  # time at next scr refresh
                    pos85.setAutoDraw(True)
                
                # *pos90* updates
                if pos90.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos90.frameNStart = frameN  # exact frame index
                    pos90.tStart = t  # local t and not account for scr refresh
                    pos90.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos90, 'tStartRefresh')  # time at next scr refresh
                    pos90.setAutoDraw(True)
                
                # *pos95* updates
                if pos95.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pos95.frameNStart = frameN  # exact frame index
                    pos95.tStart = t  # local t and not account for scr refresh
                    pos95.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pos95, 'tStartRefresh')  # time at next scr refresh
                    pos95.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in responseComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "response"-------
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('respRing.started', respRing.tStartRefresh)
            trials.addData('respRing.stopped', respRing.tStopRefresh)
            trials.addData('probe.started', probe.tStartRefresh)
            trials.addData('probe.stopped', probe.tStopRefresh)
            # store data for trials (TrialHandler)
            x, y = mouseResponse.getPos()
            buttons = mouseResponse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [pos0,pos5,pos10,pos15,pos20,pos25,pos30,pos35,pos40,pos45,pos50,pos55,pos60,pos65,pos70,pos75,pos80,pos85,pos90,pos95]:
                    if obj.contains(mouseResponse):
                        gotValidClick = True
                        mouseResponse.clicked_name.append(obj.name)
            trials.addData('mouseResponse.x', x)
            trials.addData('mouseResponse.y', y)
            trials.addData('mouseResponse.leftButton', buttons[0])
            trials.addData('mouseResponse.midButton', buttons[1])
            trials.addData('mouseResponse.rightButton', buttons[2])
            if len(mouseResponse.clicked_name):
                trials.addData('mouseResponse.clicked_name', mouseResponse.clicked_name[0])
            trials.addData('mouseResponse.started', mouseResponse.tStart)
            trials.addData('mouseResponse.stopped', mouseResponse.tStop)
            trials.addData('pos0.started', pos0.tStartRefresh)
            trials.addData('pos0.stopped', pos0.tStopRefresh)
            trials.addData('pos5.started', pos5.tStartRefresh)
            trials.addData('pos5.stopped', pos5.tStopRefresh)
            trials.addData('pos10.started', pos10.tStartRefresh)
            trials.addData('pos10.stopped', pos10.tStopRefresh)
            trials.addData('pos15.started', pos15.tStartRefresh)
            trials.addData('pos15.stopped', pos15.tStopRefresh)
            trials.addData('pos20.started', pos20.tStartRefresh)
            trials.addData('pos20.stopped', pos20.tStopRefresh)
            trials.addData('pos25.started', pos25.tStartRefresh)
            trials.addData('pos25.stopped', pos25.tStopRefresh)
            trials.addData('pos30.started', pos30.tStartRefresh)
            trials.addData('pos30.stopped', pos30.tStopRefresh)
            trials.addData('pos35.started', pos35.tStartRefresh)
            trials.addData('pos35.stopped', pos35.tStopRefresh)
            trials.addData('pos40.started', pos40.tStartRefresh)
            trials.addData('pos40.stopped', pos40.tStopRefresh)
            trials.addData('pos45.started', pos45.tStartRefresh)
            trials.addData('pos45.stopped', pos45.tStopRefresh)
            trials.addData('pos50.started', pos50.tStartRefresh)
            trials.addData('pos50.stopped', pos50.tStopRefresh)
            trials.addData('pos55.started', pos55.tStartRefresh)
            trials.addData('pos55.stopped', pos55.tStopRefresh)
            trials.addData('pos60.started', pos60.tStartRefresh)
            trials.addData('pos60.stopped', pos60.tStopRefresh)
            trials.addData('pos65.started', pos65.tStartRefresh)
            trials.addData('pos65.stopped', pos65.tStopRefresh)
            trials.addData('pos70.started', pos70.tStartRefresh)
            trials.addData('pos70.stopped', pos70.tStopRefresh)
            trials.addData('pos75.started', pos75.tStartRefresh)
            trials.addData('pos75.stopped', pos75.tStopRefresh)
            trials.addData('pos80.started', pos80.tStartRefresh)
            trials.addData('pos80.stopped', pos80.tStopRefresh)
            trials.addData('pos85.started', pos85.tStartRefresh)
            trials.addData('pos85.stopped', pos85.tStopRefresh)
            trials.addData('pos90.started', pos90.tStartRefresh)
            trials.addData('pos90.stopped', pos90.tStopRefresh)
            trials.addData('pos95.started', pos95.tStartRefresh)
            trials.addData('pos95.stopped', pos95.tStopRefresh)
            # the Routine "response" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "ITI"-------
            # update component parameters for each repeat
            # keep track of which components have finished
            ITIComponents = [ISI]
            for thisComponent in ITIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "ITI"-------
            while continueRoutine:
                # get current time
                t = ITIClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ITIClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # *ISI* period
                if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISI.frameNStart = frameN  # exact frame index
                    ISI.tStart = t  # local t and not account for scr refresh
                    ISI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                    ISI.start(durITI)
                elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                    ISI.complete()  # finish the static period
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ITI"-------
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('ISI.started', ISI.tStart)
            trials.addData('ISI.stopped', ISI.tStop)
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials'
        
    # completed 10 repeats of 'blockOfTrials'
    
# completed 1 repeats of 'taskLoop'


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
