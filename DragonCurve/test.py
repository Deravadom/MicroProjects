import sys
import turtle

def step(turns):
	result = turns.copy()
	result.append(1)
	rev = turns.copy()
	rev.reverse()
	for turn in rev:
		result.append(turn * -1)
	return result

def turnMove(t, turn, walk):
	if turn == 1:
		t.right(90)
	else:
		t.left(90)
	t.forward(walk)

def parseArgs(argc, argv):
	dArgs = [4, 10, 3]

	for i in range(1, argc):
		dArgs[i-1] = argv[i]

	return dArgs

def reset(t, offset):
	x, y = offset
	t.penup()
	t.setpos(x, y)
	t.pendown()

def dragonCurve(t, dArgs):
	turns = [1]

	folds = int(dArgs[0])
	walk = int(dArgs[1])
	pensize = int(dArgs[2])

	offset = (0, folds * walk)
	t.penup()

	t.pensize(pensize)
	t.pendown()

	colors = ['red', 'blue', 'green', 'purple']
	
	for i in range(0, folds):
		turns = step(turns)

		reset(t, offset)
		t.setheading(90 * (i%4))
	
		t.color(colors[i%4])
		t.forward(walk)

	
		for turn in turns:
			turnMove(t, turn, walk)
	

def main():
	argc = len(sys.argv)
	argv = sys.argv

	#Create screen and turtle
	screen = turtle.Screen()
	screen.title('Dragon Curve Demo')

	t = turtle.Turtle()
	t.speed(0)

	dragonCurve(t, parseArgs(argc, argv))

	t.hideturtle()
	print("Hit any key to exit")
	dummy=input()

if __name__ == '__main__':
	main()
