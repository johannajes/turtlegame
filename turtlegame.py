# Turtle Game using the package 'turtle'

import turtle
import random
import time

# Setting up a screen
screen=turtle.Screen()		# Standart screen form turtle package
screen.bgcolor('lightblue') # background color

# Setting up two players
playerone=turtle.Turtle()	# Luo kilpparin(nuolen) ruudulle
playerone.color('blue')
playerone.shape('turtle')

playertwo=playerone.clone()	
playertwo.color('red')

# Positioning players
playerone.penup()			# Ei piirra viivaa perassa, kun pelaaja liikkuu
playerone.goto(-300,200)
playertwo.penup()
playertwo.goto(-300,-200)

# Drawing a finish line
playerone.goto(300,-250)
playerone.left(90)
playerone.pendown()
playerone.color('black')
playerone.forward(500)
playerone.write('Finish!', font=24)

# Returning player one
playerone.penup()
playerone.color('blue')
playerone.goto(-300,200)
playerone.right(90)

time.sleep(1)

# Players' pens need to be down
playerone.pendown()
playertwo.pendown()

# Creating values for a die
die=[1,2,3,4,5,6]

for i in range(30):
	if playerone.pos() >= (300,250):		#.pos = position
		print("Player One wins the game!")
		break
	elif playertwo.pos() >= (300,250):
		print("Player Two wins the game!")
		break
	else:
		dieroll=random.choice(die)		# Valitsee random arvon noppa-listasta
		playerone.forward(30*dieroll)	# Kerrotaan noppaluku, ettei siirto ole liian lyhyt
		time.sleep(1)					# Peli pysahtyy 1 sekunniksi
		dieroll2=random.choice(die)
		playertwo.forward(30*dieroll2)
		time.sleep(1)
		
turtle.done() # keeps the turtle drawing on screen
				# Jos se poistetaan peli sulkeutuu, kun joku voittaa
