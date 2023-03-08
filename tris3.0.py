
import turtle
import math
import random

X_START = -290
Y_START = 250
LATO = 480

posizioni = {7:(X_START+(LATO/3)/2, Y_START-(LATO/3)/2), 8:(X_START+LATO/2, Y_START-(LATO/3)/2), 9:(X_START+(LATO-(LATO/3)/2), Y_START-(LATO/3)/2),
             4:(X_START+(LATO/3)/2, Y_START-LATO/2), 5:(X_START+LATO/2, Y_START-LATO/2), 6:(X_START+(LATO-(LATO/3)/2), Y_START-LATO/2),
             1:(X_START+(LATO/3)/2, Y_START-(LATO-(LATO/3)/2)), 2:(X_START+LATO/2, Y_START-(LATO-(LATO/3)/2)), 3:(X_START+(LATO-(LATO/3)/2), Y_START-(LATO-(LATO/3)/2))}

caselle = [{0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
            ,{0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}]

mat = [[1,1,1],[1,1,1],[1,1,1]]         #7,8,9  4,5,6  1,2,3
pos = {1: [2,0], 2: [2,1], 3:[2,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[0,0], 8:[0,1], 9:[0,2]}   

somma_rig = [0,0,0]
somma_col = [0,0,0]
somma_dia = [0,0]

curs = turtle.Turtle()
finestra = turtle.Screen()

def fxn(x, y):
    
    n = None
    while n == None:
        for k,v in posizioni.items():
            if x>= v[0]-(LATO/3)/2 and x<= v[0]+(LATO/3)/2 and y>=v[1]-(LATO/3)/2 and y<=v[1]+(LATO/3)/2:
                n = k
    if not caselle[1][n] and not caselle[0][n]:
        disegnaCroce(posizioni[n][0],posizioni[n][1])
        caselle[0][n] = True
        mat[pos[n][0]][pos[n][1]] = 5  
                                
    win(0)

    s = scelta()
    print(s)
    disegnaCerchio(posizioni[s][0], posizioni[s][1])
    caselle[1][s] = True
    mat[pos[s][0]][pos[s][1]] = 3
                 
    win(1)

def somma():
    for i in range (0,3):
        somma_rig[i] = mat[i][0]*mat[i][1]*mat[i][2]
        somma_col[i] = mat[0][i]*mat[1][i]*mat[2][i]
    somma_dia[0] = mat[0][0]*mat[1][1]*mat[2][2]
    somma_dia[1] = mat[0][2]*mat[1][1]*mat[2][0]

def scelta():
    somma()

    n = 5
    if (caselle[0][n] == False and caselle[1][n] == False):
        return n
    
    for i in range (0,3):#righe 
        if somma_rig[i] == 9:
            for k in range (9-i*3-2,9-i*3+1):
                if caselle[1][k] == False:
                    return k
        if somma_rig[i] == 25:
            for k in range (9-i*3-2,9-i*3+1):
                if caselle[0][k] == False:
                    return k

    for i in range (0,3):#colonne 
        if somma_col[i] == 9:
            for k in range (0,3):
                if caselle[1][i+1+k*3] == False:
                    return i+1+k*3
        if somma_col[i] == 25:
            for k in range (0,3):
                if caselle[0][i+1+k*3] == False:
                    return i+1+k*3
        
    if somma_dia[0] == 9:#753
        if caselle[0][7] == False:    
            return 7
        if caselle[0][5] == False:
            return 5
        if caselle[0][3] == False:
            return 3

    if somma_dia[1] == 9:#951
        if caselle[1][7] == False:    
            return 9
        if caselle[1][5] == False:
            return 5
        if caselle[1][3] == False:
            return 1

    if somma_dia[1] == 25:
        if caselle[0][9] == False:    
            return 9
        if caselle[0][5] == False:
            return 5
        if caselle[0][1] == False:
            return 1 
    if somma_dia[1] == 25:
        if caselle[1][9] == False:    
            return 9
        if caselle[1][5] == False:
            return 5
        if caselle[1][1] == False:
            return 1 
    for i in range (0,3):#righe 
        if somma_rig[i] == 3:
            for k in range (9-i*3-2,9-i*3+1):
                if caselle[1][k] == False:
                    return k

    for i in range (0,3):#colonne 
        if somma_col[i] == 3:
            for k in range (0,3):
                if caselle[1][i+1+k*3] == False:
                    return i+1+k*3
        
    if somma_dia[0] == 3:#753
        if caselle[0][7] == False:    
            return 7
        if caselle[0][5] == False:
            return 5
        if caselle[0][3] == False:
            return 3
    if somma_dia[1] == 3:#951
        if caselle[1][7] == False:    
            return 9
        if caselle[1][5] == False:
            return 5
        if caselle[1][3] == False:
            return 1


    while (1):
        n = random.randint(1,9)
        
        if caselle[0][n] == False and caselle[1][n] == False:
            return n

def disegnaCroce(x,y):
    curs.penup()
    curs.setposition(x,y)
    curs.pendown()
    curs.width(9)
    curs.color("black")

    curs.right(45)
    curs.forward(70)
    curs.backward(140)
    curs.forward(70)
    curs.left(90)
    curs.forward(70)
    curs.backward(140)
       
    curs.right(45)
    curs.penup()
    curs.setposition(x,y)
    curs.pendown()
    curs.width(3)
    curs.color("red")

    curs.right(45)
    curs.forward(70)
    curs.backward(140)
    curs.forward(70)
    curs.left(90)
    curs.forward(70)
    curs.backward(140)

    curs.right(45)

def disegnaCerchio(x,y):
    curs.penup()
    curs.setposition(x,y-(LATO/4)/2)
    curs.pendown()

    curs.width(9)
    curs.color("black")
    curs.circle(60)

    curs.penup()
    curs.setposition(x,y-(LATO/4)/2)
    curs.pendown()

    curs.width(3)
    curs.color("blue")
    curs.circle(60)

def winOriz(i):
    curs.penup()
    curs.setposition(posizioni[i*3][0]+20,posizioni[i*3][1])
    curs.pendown()

    curs.width(15)
    curs.color("black")
    curs.backward(LATO*4/6 + 40)

    curs.penup()
    curs.setposition(posizioni[i*3][0]+20,posizioni[i*3][1])
    curs.pendown()

    curs.width(8)
    curs.color("lime")
    curs.backward(LATO*4/6 + 40)


def winVert(i):
    curs.penup()
    curs.setposition(posizioni[6+i][0],posizioni[6+i][1]+20)
    curs.pendown()

    curs.width(15)
    curs.color("black")
    curs.right(90)
    curs.forward(LATO*4/6 + 40)

    curs.left(90)

    curs.penup()
    curs.setposition(posizioni[6+i][0],posizioni[6+i][1]+20)
    curs.pendown()

    curs.width(8)
    curs.color("lime")
    curs.right(90)
    curs.forward(LATO*4/6 + 40)

def winObl1():
    curs.penup()
    curs.setposition(posizioni[7][0]-15,posizioni[7][1]+15)
    curs.pendown()

    curs.width(15)
    curs.color("black")
    curs.right(45)
    curs.forward(LATO + 15)

    curs.left(45)

    curs.penup()
    curs.setposition(posizioni[7][0]-15,posizioni[7][1]+15)
    curs.pendown()

    curs.width(8)
    curs.color("lime")
    curs.right(45)
    curs.forward(LATO + 15)

def winObl2():
    curs.penup()
    curs.setposition(posizioni[9][0]+15,posizioni[9][1]+15)
    curs.pendown()

    curs.width(15)
    curs.color("black")
    curs.right(135)
    curs.forward(LATO + 15)

    curs.left(135)

    curs.penup()
    curs.setposition(posizioni[9][0]+15,posizioni[9][1]+15)
    curs.pendown()

    curs.width(8)
    curs.color("lime")
    curs.right(135)
    curs.forward(LATO + 15)


def win(k):
        for i in range(1,4):#controllo vittoria orizzontale
            if caselle[k][1+(3*(i-1))] and caselle[k][2+(3*(i-1))] and caselle[k][3+(3*(i-1))]:
                winOriz(i)
                turtle.done()
        
        for i in range(1,4):#controllo vittoria verticale
            if caselle[k][i] and caselle[k][3+i] and caselle[k][6+i]:
                winVert(i)
                turtle.done()

        if caselle[k][7] and caselle[k][5] and caselle[k][3]:
            winObl1()
            turtle.done()

        if caselle[k][1] and caselle[k][5] and caselle[k][9]:
            winObl2()
            turtle.done()
    
    
class Tris():

    curs.hideturtle()

    def disegnaCampo(self):
        curs.speed(0)
        curs.penup()
        curs.setposition(X_START,Y_START)           #coordinate iniziali campo
        curs.pendown()
        curs.width(10)                              #setta spessore del
        
        curs.begin_fill()                           #colorare il campo
        for _ in range(0,4):                        #disegna il campo
            curs.forward(LATO)
            curs.right(90)

        curs.color("#FCFF8D")                       #colora il quadrato
        curs.end_fill()                             #fine colore 

        curs.color("black")
        curs.right(90)  
        for i in range(1,3):                        #caselle campo(righe verticali)
            curs.penup()
            curs.setposition(X_START+((LATO/3)*i), Y_START)
            curs.pendown()
            curs.forward(LATO)

        curs.left(90)
        for i in range(1,3):                        #caselle campo(righe orizzontali)
            curs.penup()
            curs.setposition(X_START, Y_START-((LATO/3)*i))
            curs.pendown()
            curs.forward(LATO)

        curs.penup()
        curs.setposition(X_START,Y_START)           #coordinate iniziali campo
        curs.pendown()
        curs.width(5)                              #setta spessore del
        curs.color("gold")

        for _ in range(0,4):                        #disegna il campo
            curs.forward(LATO)
            curs.right(90)

        curs.right(90)  
        for i in range(1,3):                        #caselle campo(righe verticali)
            curs.penup()
            curs.setposition(X_START+((LATO/3)*i), Y_START)
            curs.pendown()
            curs.forward(LATO)

        curs.left(90)
        for i in range(1,3):                        #caselle campo(righe orizzontali)
            curs.penup()
            curs.setposition(X_START, Y_START-((LATO/3)*i))
            curs.pendown()
            curs.forward(LATO)

    def tris(self):
        
        finestra.onclick(fxn)
        finestra.mainloop()       

        turtle.done()
        
def main():
    tris = Tris()

    tris.disegnaCampo()
    tris.tris()

if __name__=="__main__":
    main()