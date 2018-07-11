#grape!
#this file is dice_generator.
#using turtle!

import random
import turtle
import time
#Set turtle for drawing dice
def generate(randNum,num,i):
	wn=turtle.Screen()
	wn.bgcolor("black")
	wn.title("[Me]Dice_Result!")
	wn.setup(422,422)
	class Pen(turtle.Turtle):
	    def __init__(self):
	        turtle.Turtle.__init__(self)
	        self.shape("square")
	        self.color("white")
	        self.penup()
	        self.speed(0)

	class Circle(turtle.Turtle):
	    def __init__(self):
	        turtle.Turtle.__init__(self)
	        self.shape("square")
	        self.color("red")
	        self.penup()
	        self.speed(0)

	dice_1=[
	"XXXXXXXXXXX",
	"X         X",
	"X         X",
	"X         X",
	"X         X",
	"X    C    X",
	"X         X",
	"X         X",
	"X         X",
	"X         X",
	"XXXXXXXXXXX"
	]
	dice_2=[
	"XXXXXXXXXXX",
	"X         X",
	"X         X",
	"X         X",
	"X      C  X",
	"X         X",
	"X  C      X",
	"X         X",
	"X         X",
	"X         X",
	"XXXXXXXXXXX"
	]
	dice_3=[
	"XXXXXXXXXXX",
	"X         X",
	"X         X",
	"X      C  X",
	"X         X",
	"X    C    X",
	"X         X",
	"X  C      X",
	"X         X",
	"X         X",
	"XXXXXXXXXXX"
	]
	dice_4=[
	"XXXXXXXXXXX",
	"X         X",
	"X         X",
	"X  C   C  X",
	"X         X",
	"X         X",
	"X         X",
	"X  C   C  X",
	"X         X",
	"X         X",
	"XXXXXXXXXXX"
	]
	dice_5=[
	"XXXXXXXXXXX",
	"X         X",
	"X         X",
	"X  C   C  X",
	"X         X",
	"X    C    X",
	"X         X",
	"X  C   C  X",
	"X         X",
	"X         X",
	"XXXXXXXXXXX"
	]
	dice_6=[
	"XXXXXXXXXXX",
	"X         X",
	"X         X",
	"X  C C C  X",
	"X         X",
	"X         X",
	"X         X",
	"X  C C C  X",
	"X         X",
	"X         X",
	"XXXXXXXXXXX"
	]

	dice = ["",dice_1,dice_2,dice_3,dice_4,dice_5,dice_6]
	def setup_dice(dice):
	    for y in range(len(dice)):
	        for x in range(len(dice[y])):
	            character = dice[y][x]
	            screen_x = -124 + (x*24)
	            screen_y = 124- (y * 24)
	            if character =="X":
	                pen.goto(screen_x,screen_y)
	                pen.stamp()

	            if character == "C":
	                circle.goto(screen_x,screen_y)
	                circle.stamp()

	pen=Pen()
	circle=Circle()

	setup_dice(dice[randNum])
	time.sleep(3)
	wn.update()
	if i == num-1:
		turtle.bye()
	else: wn.reset()



#Set dice for displaying terminal
def dice(m):
    if m==1:
      print (""" 
          _________
         |         |
         |         |  
         |    *    | 
         |         | 
         |_________|  """)
         
    elif m == 2:
      print  ("""
          _________
         |         |
         |     *   |
         |         | 
         |   *     | 
         |_________|  """)
      
    elif m == 3:
      print ("""
          _________
         |         |
         |      *  |  
         |    *    | 
         |  *      | 
         |_________|  """) 
    
    elif m == 4:
      print ("""
          _________
         |         |
         |  *   *  |  
         |         | 
         |  *   *  | 
         |_________|  """) 
    
    
    elif m == 5:
      print (""" 
          _________
         |         |
         |  *   *  |  
         |    *    | 
         |  *   *  | 
         |_________|  """)
    
    
    elif m == 6:
      print ("""   
          _________
         |         |
         |  *   *  |  
         |  *   *  | 
         |  *   *  | 
         |_________|  """) 



