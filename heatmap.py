#Author: lucco
import matplotlib.pyplot as plt 
import csv 
import turtle

X_START = -550
Y_START = 250
MAX_VALUE = 388
WIDTH = 8

"""
Lettura file e caricamento liste
"""

anomaly = []

data_file2 = open("./Temperature_Anomaly.csv")
data_reader1 = csv.reader(data_file2, delimiter=",")

colour = {"r": 0, "g": 0, "b": 0}

curs = turtle.Turtle()
finesta = turtle.Screen()

turtle.colormode(255)           #rgb mode

curs.speed(0.3)
curs.width(WIDTH)

next(data_reader1)

for row in data_reader1:
    anomaly.append(float(row[1]))

MIN_TEMP = min(anomaly)
MAX_TEMP = max(anomaly)

curs.right(90)

for temp in anomaly:

    curs.penup()
    curs.setposition(X_START, Y_START)
    curs.pendown()
    
    if temp > 0:
        c = int((abs(temp)*MAX_VALUE)/MAX_TEMP)
                
        if c > 255:
            colour["r"] = 255 - (c-255)
            colour["g"] = 0
            colour["b"] = 0  
        else: 
            colour["r"] = 255
            colour["g"] = 255 - int((abs(temp)*MAX_VALUE)/MAX_TEMP)
            colour["b"] = 255 - int((abs(temp)*MAX_VALUE)/MAX_TEMP)
    
    elif temp < 0:
        c = int((abs(temp)*MAX_VALUE)/abs(MIN_TEMP))

        if c > 255:
            colour["b"] = 255 - (c-255)
            colour["g"] = 0
            colour["r"] = 0
        else:
            colour["b"] = 255
            colour["g"] = 255 - int((abs(temp)*MAX_VALUE)/abs(MIN_TEMP))
            colour["r"] = 255 - int((abs(temp)*MAX_VALUE)/abs(MIN_TEMP))
    
    else:
        colour["b"] = 255
        colour["g"] = 255
        colour["r"] = 255
    
    curs.pencolor((colour["r"], colour["g"], colour["b"]))

    curs.forward(500)

    X_START+=WIDTH


turtle.done()