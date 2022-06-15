# Connect-4-If-You-Can
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/urastogi885/connect-4-if-you-can/blob/master/LICENSE)

## Overview
A self-learning connect-4 game with a simple GUI. I used the blog on [reinforcement learning](https://blog.floydhub.com/an-introduction-to-q-learning-reinforcement-learning/) to come up with my Q-Learning solution. The blog provides an excellent step-by-step approach to implement a solution using RL. 

Connect-4 has a huge state space that renders Q-Learning ineffective. An approach using Deep Q-Learning will make a better self-learning AI agent for the game.

<p align="center">
  <img src="https://github.com/urastogi885/connect-4-if-you-can/blob/master/images/ai_vs_human.gif">
  <br><b>Figure 1 - AI agent (Yellow) playing against a human (Red)</b><br>
</p>

## Dependencies

- Python3
- Python3 Libraries: [Numpy](https://numpy.org/), [PyGame](https://www.pygame.org/wiki/GettingStarted)

## Install Dependencies

- Install Python3, and the necessary libraries: (if not already installed)
````
sudo apt install python3
sudo apt install python3-pip
pip3 install numpy pygame
````

- Check if your system successfully installed all the dependencies
- Open terminal using Ctrl+Alt+T and enter python3
- The terminal should now present a new area represented by >>> to enter python commands
- Now use the following commands to check libraries: (Exit python window using Ctrl+Z if an error pops up while
running the below commands)
````
import numpy
import pygame
````

## Run

- Using the terminal, clone this repository and go into the project directory, and run:
````
git clone https://github.com/urastogi885/connect-4-if-you-can
cd connect-4-if-you-can
python3 connect_4.py
````
