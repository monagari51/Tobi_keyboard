#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 09, 2022, at 18:25
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
import csv


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'KeyBoard'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
filename1 = _thisDir + os.sep + u'expInfo/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
csvfile = open(filename1+".csv", "a", newline='')
writer = csv.writer(csvfile)
writer.writerow(["Trial Number", "State", "Device timestamp","Left pupil diameter","Left pupil validity","Right pupil diameter","Right pupil validity", "Rating"])

trialImages='Stimuli_Numbers.xlsx'
print(trialImages)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\Thesis\\PupilAssistedSpellCorrectionForGazeTyping\\Research\\Trail1 - Copy_lastrun.py',
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

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
text_Welcome_Message = visual.TextStim(win=win, name='text_Welcome_Message',
    text='Wecome to the experiment\n\n\nPress SPACEBAR to start the experiment',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_Welcome = keyboard.Keyboard()

# Initialize components for Routine "Blank100"
Blank100Clock = core.Clock()
text_Blank100 = visual.TextStim(win=win, name='text_Blank100',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
import time
import tobii_research as tr
from msvcrt import getch
import sys
from psychopy import data

# ref code used
# http://devtobiipro.azurewebsites.net/tobii.research/python/reference/1.8.0.32-alpha-g5b38a1f5/gaze_data_8py-example.html

# in sec
timer = 1000
# reading per sec
frequency = 2
global_gaze_data = None
# in second
fixation_threshhold = 0.5
# minimum 
fixation_tolerance = 0.0005

textId = 1

def initTobii():
    current_eye_tracker = tr.find_all_eyetrackers()[0]
    # print(current_eye_tracker)
    return current_eye_tracker


def getTimeStamp():
    return int((time.time() - start_time) * 1000)

def gaze_data_callback(gaze_data):
    global global_gaze_data
    global_gaze_data = gaze_data

start_time = time.time()
eyetracker = initTobii();
eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
print ("tobii inilialized")
print(getTimeStamp())

# Initialize components for Routine "STIMULI"
STIMULIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "GoodBye_Screen"
GoodBye_ScreenClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Thank You',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_Welcome = keyboard.Keyboard()
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome_Screen"-------
continueRoutine = True
# update component parameters for each repeat
key_Welcome.keys = []
key_Welcome.rt = []
_key_Welcome_allKeys = []
# keep track of which components have finished
Welcome_ScreenComponents = [text_Welcome_Message, key_Welcome]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True
# -------Run Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Welcome_Message* updates
    if text_Welcome_Message.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_Welcome_Message.frameNStart = frameN  # exact frame index
        text_Welcome_Message.tStart = t  # local t and not account for scr refresh
        text_Welcome_Message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Welcome_Message, 'tStartRefresh')  # time at next scr refresh
        text_Welcome_Message.setAutoDraw(True)
    
    # *key_Welcome* updates
    waitOnFlip = False
    if key_Welcome.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_Welcome.frameNStart = frameN  # exact frame index
        key_Welcome.tStart = t  # local t and not account for scr refresh
        key_Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Welcome, 'tStartRefresh')  # time at next scr refresh
        key_Welcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_Welcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_Welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_Welcome.status == STARTED and not waitOnFlip:
        theseKeys = key_Welcome.getKeys(keyList=['space'], waitRelease=False)
        _key_Welcome_allKeys.extend(theseKeys)
        if len(_key_Welcome_allKeys):
            key_Welcome.keys = _key_Welcome_allKeys[0].name  # just the first key pressed
            key_Welcome.rt = _key_Welcome_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Welcome_Message.started', text_Welcome_Message.tStartRefresh)
thisExp.addData('text_Welcome_Message.stopped', text_Welcome_Message.tStopRefresh)
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# check responses
'''
if key_Welcome.keys in ['', [], None]:  # No response was made
    key_Welcome.keys = None
thisExp.addData('key_Welcome.keys',key_Welcome.keys)
if key_Welcome.keys != None:  # we had a response
    thisExp.addData('key_Welcome.rt', key_Welcome.rt)
thisExp.addData('key_Welcome.started', key_Welcome.tStartRefresh)
thisExp.addData('key_Welcome.stopped', key_Welcome.tStopRefresh)
thisExp.nextEntry()
'''

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli_Numbers.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    counter = 1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank100"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_Blank100.setText(Empty)
    
    start_time = time.time()
    allGazeData = []
    csvGaze=[]
    # keep track of which components have finished
    Blank100Components = [text_Blank100]
    for thisComponent in Blank100Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank100Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank100"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank100Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank100Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Blank100* updates
        if text_Blank100.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Blank100.frameNStart = frameN  # exact frame index
            text_Blank100.tStart = t  # local t and not account for scr refresh
            text_Blank100.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Blank100, 'tStartRefresh')  # time at next scr refresh
            text_Blank100.setAutoDraw(True)
        if text_Blank100.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_Blank100.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_Blank100.tStop = t  # not accounting for scr refresh
                text_Blank100.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_Blank100, 'tStopRefresh')  # time at next scr refresh
                text_Blank100.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank100Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank100"-------
    for thisComponent in Blank100Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_Blank100.started', text_Blank100.tStartRefresh)
    trials.addData('text_Blank100.stopped', text_Blank100.tStopRefresh)
    textId=textId+1
    # ------Prepare to start Routine "STIMULI"-------
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text.setText(Number)
    
    start_time = time.time()
    allGazeData = []
    # keep track of which components have finished
    STIMULIComponents = [text]
    for thisComponent in STIMULIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    STIMULIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    # -------Run Routine "STIMULI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = STIMULIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=STIMULIClock)
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
        print(global_gaze_data)
        time.sleep(1/frequency)
        print(getTimeStamp())
        
        allGazeData.append(global_gaze_data)
        csvGaze.append(['Trial'+str(counter),'stimuli',global_gaze_data['device_time_stamp'],global_gaze_data['left_pupil_diameter'],global_gaze_data['left_pupil_validity'],global_gaze_data['right_pupil_diameter'],global_gaze_data['right_pupil_validity']])
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in STIMULIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "STIMULI"-------
    for thisComponent in STIMULIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    textId=textId+1
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "GoodBye_Screen"-------

routineTimer.add(30.000000)
# update component parameters for each repeat
key_Welcome.keys = []
key_Welcome.rt = []
# keep track of which components have finished
GoodBye_ScreenComponents = [text_2,key_Welcome]
for thisComponent in GoodBye_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodBye_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True
# -------Run Routine "GoodBye_Screen"-------
while continueRoutine:
    # get current time
    t = GoodBye_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodBye_ScreenClock)
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
        
        '''
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
        '''
 # *key_Welcome* updates
    waitOnFlip = False
    if key_Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_Welcome.frameNStart = frameN  # exact frame index
        key_Welcome.tStart = t  # local t and not account for scr refresh
        key_Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Welcome, 'tStartRefresh')  # time at next scr refresh
        key_Welcome.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_Welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_Welcome.status == STARTED and not waitOnFlip:
        theseKeys = key_Welcome.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
            
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodBye_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GoodBye_Screen"-------
for thisComponent in GoodBye_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# the Routine "Thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

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
csvfile.close()
core.quit()
