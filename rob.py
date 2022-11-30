import random
import turtle

VEL = 100
TEMP = 7200

MIN = 1
MAX = 4

SPOSTAMENTO = 5

diz = {1:0,2:90,3:180,4:270}

def movimento(robot):
    robot.right(diz[random.randint(MIN,MAX)])
    robot.forward(SPOSTAMENTO)    

def main():
    finestra = turtle.Screen()
    robot = turtle.Turtle()

    robot.speed(VEL)
    robot.color("lime")
    robot.shape("turtle")

    for _ in range(TEMP):
        movimento(robot) 
    
    robot.done()

if __name__ == "__main__":
    main()
