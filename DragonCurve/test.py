import sys
import turtle

def border(t, screen_x, screen_y):
	
	"""Draws a border around the canvas in red."""
	t.penup()
	t.home()

	#Move to lower left, turtle faces west
	t.forward(screen_x/2)
	t.right(90)
	t.forward(screen_y/2)
	t.setheading(180)

	t.pencolor('red')
	t.pendown()
	t.pensize(10)
	for distance in (screen_x, screen_y, screen_x, screen_y):
		t.forward(distance)
		t.right(90)

	#Raise pen and move home
	t.penup()
	t.home()

def square(t, size, color):
	#Draw a square of given color, size
	t.pencolor(color)
	t.pendown()
	for i in range(4):
		t.forward(size)
		t.right(90)
def step(turns):
	result = turns.copy()
	result.append(1)
	rev = turns.copy()
	rev.reverse()
	for turn in rev:
		result.append(turn * -1)
	return result

def turnMove(t, turn):
	if turn == 1:
		t.right(90)
	else:
		t.left(90)
	t.forward(1)

def main():
	#Create screen and turtle
	screen = turtle.Screen()
	screen.title('Square Demo')
	screen_x, screen_y = screen.screensize()
	t = turtle.Turtle()

	t.speed(0)

	#border(t, screen_x, screen_y)

	colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
	"""
	t.pensize(3)
	#for i, color in enumerate(colors):
		square(t, (screen_y / 2) / 10 * (i + 1), color)
	turtle.write("this is a test", True, align="center", font=('Arial', 32, 'normal'))
	"""

	turns = [1]

	t.pensize(3)
	t.pendown()
	t.pencolor('red')
	t.forward(1)


	for i in range(0, 25):
		t.penup()
		t.home()
		t.pendown()
		turns = step(turns)
		print("Calculated: ", i)
		if i > 23:
			for turn in turns:
				turnMove(t, turn)


	print("Hit any key to exit")
	dummy=input()

if __name__ == '__main__':
	main()
