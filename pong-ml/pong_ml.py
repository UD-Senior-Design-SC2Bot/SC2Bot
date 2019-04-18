'''
pong_ml.py

Pong game, modified from 
http://www.pygame.org/project-Very+simple+Pong+game-816-.html
Utilizes a tensorflow model as the agent

Command line arguments:
    -nf     The number of frames to use from the dataset
    -d      The name of the dataset to load

'''

import sys
import numpy
import pygame
from pygame.locals import *
import random
import ml_model
import datasets
import pygame.surfarray as surfarray
import matplotlib.pyplot as plt
import data_collect
from frame_data import FrameData




print("\n===== Parsing user arguments... =====")
numframes = -1
chosen_dataset = 'ideal'

i = 0
while (i < len(sys.argv)):
    arg = sys.argv[i]
    
    if (arg == '-nf' and (i + 1) < len(sys.argv)):
        # numframes
        numframes = int(sys.argv[i + 1])
        i += 1

    if (arg == '-d' and (i + 1) < len(sys.argv)):
        # chosen dataset
        chosen_dataset = sys.argv[i + 1]
        i += 1

    i += 1

if (numframes == -1):
    print("Using all frames of data")
else:
    print("Using {} frames of data".format(numframes))
print("Using the '{}' dataset".format(chosen_dataset))

print("=====================================\n")

pygame.init()
model = ml_model.PongModel(datasets.loadn(chosen_dataset, numframes))

screen = pygame.display.set_mode((640, 480), 0, 32)

# Creating 2 bars, a ball and background.
back = pygame.Surface((640, 480))
background = back.convert()
background.fill((0, 0, 0))
bar = pygame.Surface((10, 50))
bar1 = bar.convert()
bar1.fill((255, 255, 255))
bar2 = bar.convert()
bar2.fill((255, 255, 255))
circ_sur = pygame.Surface((15, 15))
circ = pygame.draw.circle(circ_sur, (255, 255, 255), ((int)(15 / 2), (int)(15 / 2)), (int)(15 / 2))
circle = circ_sur.convert()
circle.set_colorkey((0, 0, 0))

# some definitions
bar1_x, bar2_x = 10. , 620.
bar1_y, bar2_y = 215. , 215.
circle_x, circle_y = 307.5, 232.5
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 250.
bar1_score, bar2_score = 0, 0

# clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 40)

# ML objects
session_training_data = []

frame_num = 0
hits = 0

done = False

while done == False:
    frame_num += 1
    if frame_num >= 10000:
        done = True       
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0
    ai_speed = speed_circ * time_sec

    # Use the model to predict the next move
    frame_tensor = FrameData(frame_num, -1, bar1_y, circle_x, circle_y).to_processed_tensor()
    move = model.get_next_move(frame_tensor)
    # Respond to the model
    if (move == 1): # Up
        bar1_move = -ai_speed
    elif (move == 2): # Down
        bar1_move = ai_speed

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        
    score1 = font.render(str(bar1_score), True, (255, 255, 255))
    score2 = font.render(str(bar2_score), True, (255, 255, 255))

    screen.blit(background, (0, 0))
    frame = pygame.draw.rect(screen, (255, 255, 255), Rect((5, 5), (630, 470)), 2)
    middle_line = pygame.draw.aaline(screen, (255, 255, 255), (330, 5), (330, 475))
    screen.blit(bar1, (bar1_x, bar1_y))
    screen.blit(bar2, (bar2_x, bar2_y))
    screen.blit(circle, (circle_x, circle_y))
    screen.blit(score1, (250., 210.))
    screen.blit(score2, (380., 210.))

    bar1_y += bar1_move
        
    # movement of circle
    
        
    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    
    
    # AI of the computer.
    if circle_x >= 305.:
        if not bar2_y == circle_y + 7.5:
            if bar2_y < circle_y + 7.5:
                bar2_y += ai_speed
            if  bar2_y > circle_y - 42.5:
                bar2_y -= ai_speed
        else:
            bar2_y == circle_y + 7.5
    
    # Safety out of bound reset
    if bar1_y >= 420.:
        bar1_y = 420.
    elif bar1_y <= 10. :
        bar1_y = 10.
    if bar2_y >= 420.:
        bar2_y = 420.
    elif bar2_y <= 10.:
        bar2_y = 10.
        
    # Simple Bar collision
    if circle_x <= bar1_x + 10.:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            speed_x = -speed_x
            hits += 1
    if circle_x >= bar2_x - 15.:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            speed_x = -speed_x
                
    # Detects North South bounds
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5
    
    # Win condition.
    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = 320., 232.5
        bar1_y, bar_2_y = 215., 215.
    elif circle_x > 620.:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    
    # Stop movement
    bar1_move = 0.
    pygame.display.update()

accuracy = hits/(hits + bar2_score)
print("Hits: ", hits, " Score 1: ", bar1_score, " Score 2: ", bar2_score, "Accuracy: ", accuracy)
pygame.quit()
