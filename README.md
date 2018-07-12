# Home-rehabilitation-treatmen(by Grape)
[EDISON2018 project](https://github.com/ys7yoo/Edison2018)
+ home rehabilitation treatment device using raspberry pi

## Project description
 It is a rehabilitation device for people with paralyzed hands.
we provide some games (using video recognition and tact) and patients can rehabilitate through games

## Grape!
+ team name is Grape!
+ We're studying Electronic Engineering, University of Incheon.
+ team members
  - Park jun young: 3rd grade (9851248@gmail.com)
  - Lee jong gil: 2nd grade ()
  - shin na ra: 1st grade (naracon03@naver.com)

# Project plan

## Problems
1. Increase in stroke patients.
2. Shortage of rehabilitation hospitals.
3. Takes a lot of money and time.
4. Without rehabilitation, paralysis gets worse.

## Solutions
1. Provide services to rehabilitate at home.
2. Have fun access through games.
3. Provide low cost services.

## Contents
1. __dice game__
  + we used picamera and opencv(module in python) to recognize the dice.
  + this game is rolling dice game.
  + if you win the game, you can read good words.

2. __hand gesture game__
  + we used picamera and opencv(module in python) to recognize the hand.
  + this game is counting iteration. (finger concentration or stretching)
 
3. __pick up color card game__
  + we used picamera and opencv(module in python) to recognize the color card.
  + this game is what you pick up color cards taht computer shows. 

4. __mole game__
  + we used tact switch and pygame(module in python)
  + this game is catching that mole computer shows.

5. __maze game__
  + we used tact switch and pygame(module in python)
  + this game is solving complicated maze.

# We use...
1. raspberry pi3
2. pi camera
3. TACT switch

4. python3
5. opencv
5. RPi.GPIO
6. numpy
7. pygame
8. turtle

## Installation of dependencies
1. __install RASPBIAN__ 
  We used [RASPBIAN](https://www.raspberrypi.org/downloads/raspbian/) : Release: 2018.06.27

2. __apt-get update__
  '''bash
  pi@raspberrypi:~ $ sudo apt-get update
  pi@raspberrypi:~ $ sudo apt-get upgrade
  '''

3. __Install RPi.GPIO__
  '''bash
  pi@raspberrypi:~ $ sudo apt-get install python-dev python3-dev
  pi@raspberrypi:~ $ sudo apt-get install python-rpi.gpio
  '''

4. __Install numpy__
  '''bash
  pi@raspberrypi:~ $ sudo apt-get install python3-numpy
  '''

5. __Install opencv__
  We used [github](https://github.com/dltpdn/opencv-for-rpi.git) to install opencv
  '''bash
  pi@raspberrypi:~ $ git clone https://github.com/dltpdn/opencv-for-rpi.git
  pi@raspberrypi:~ $ cd {your path}/opencv-for-rpi/stretch/3.4.0
  pi@raspberrypi:~/...../3.4.0 $ sudo apt-get install ./OpenCV\*.deb -y
  '''
  
  Install check
  '''bash
  pi@raspberrypi:~ $ pkg-config --modversion opencv
  '''
  if you look at 3.4.0, it is a sucess!

6. __Setting picamera__
  pi camera is not USB type, so you must set it to recgnize it as a device.
  '''bash
  pi@raspberrypi:~ $ sudo modprobe bcm2835-v4l2
  '''

  Checking device
  '''bash
  pi@raspberrypi:~ $ ls /dev/video\*
  '''

7. __etc__
  python3, pygame are installed with the RASPBIAN installation.
  turtle is internal function of python3
  _if there is anything else you need Please install_

