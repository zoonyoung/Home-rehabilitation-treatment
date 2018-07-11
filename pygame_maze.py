#grape!
#this file is maze_game
#using turtle
#using GPIO(TACT)
import time
import turtle
import math
import RPi.GPIO as GP
import pygame
from maze.map import map

def maze(step):
#set tact
    sw=[22,23,24,25]
    GP.setmode(GP.BCM)
    GP.setup(5,GP.IN,pull_up_down=GP.PUD_UP)
    for j in range(22,26):
        GP.setup(j,GP.IN,pull_up_down=GP.PUD_UP)

    #set turtle.screen
    wn=turtle.Screen()
    wn.bgcolor("black")
    wn.title("A Maze Gmae")
    wn.setup(700,700)

    #box
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("white")
            self.penup()
            self.speed(0)
    #player
    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("blue")
            self.penup()
            self.speed(0)
            self.gold=0
            #set up KEY (with sensor)
        def go_up(self):
            move_to_x = player.xcor()
            move_to_y = player.ycor()+24

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def go_down(self):
            move_to_x = player.xcor()
            move_to_y = player.ycor()-24

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
        def go_left(self):
            move_to_x = player.xcor()-24
            move_to_y = player.ycor()

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
        def go_right(self):
            move_to_x = player.xcor()+24
            move_to_y = player.ycor()

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def is_collision(self,other):
            a= self.xcor()-other.xcor()
            b= self.ycor()-other.ycor()
            distance = math.sqrt((a**2)+(b**2))

            if distance <5:
                return True
            else:
                return False
    #goal
    class Treasure(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("circle")
            self.color("gold")
            self.penup()
            self.speed(0)
            self.gold = 100
            self.goto(x,y)

        def destroy(self):
            self.goto(2000,2000)
            self.hideturtle()


    #loading map
    levels=[]
    levels=map()

    treasures=[]
    #Level setup

    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = -288 + (x*24)
                screen_y = 288 - (y * 24)
                if character =="X":
                    pen.goto(screen_x,screen_y)
                    pen.stamp()
                    walls.append((screen_x,screen_y))

                if character == "P":
                    player.goto(screen_x,screen_y)
                if character =="T":
                    treasures.append(Treasure(screen_x,screen_y))
    #setting
    pen=Pen()
    player=Player()
    walls=[]
    setup_maze(levels[step])


    turtle.listen()

    wn.tracer(0)

    #use tact!
    while True:
        if GP.input(22)==0:
            player.go_left()
            time.sleep(0.2)
        if GP.input(23)==0:
            player.go_up()
            time.sleep(0.2)
        if GP.input(24)==0:
            player.go_down()
            time.sleep(0.2)
        if GP.input(25)==0:
            player.go_right()
            time.sleep(0.2)
        if GP.input(5)==0:
            pygame.quit()
            print("\n ******\n 아쉽습니다. 게임을 포기하셨습니다.")
            return 0,0
            break
        for treasure in treasures:
            if player.is_collision(treasure):
                player.gold += treasure.gold
                treasure.destroy()
                treasures.remove(treasure)
                time.sleep(1)
                print("\n ******\n 축하합니다. 미로를 해결하였습니다!")
                pygame.quit()
                time.sleep(1)
                return 0,0
                break
        wn.update()
    GP.cleanup()