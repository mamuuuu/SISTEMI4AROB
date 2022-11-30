from cgi import print_form
import random
def somma(n1,n2):
    return n1+n2

def differenza(n1,n2):
    return n1-n2

def divisione(n1,n2):
        return n1/n2

def prodotto(n1,n2):
    return n1*n2

n1,n2 = int(input("Inserisci un numero: ")),int(input("Inserisci un numero: "))

d = {0:somma,1:differenza,2:divisione,3:prodotto}

print(d[random.randint(0,3)](n1,n2))
exit()
def somma(n1,n2):
    return n1+n2

def differenza(n1,n2):
    return n1-n2

def divisione(n1,n2):
        return n1/n2

def prodotto(n1,n2):
    return n1*n2

op = input("Inserisci la operazione: ")
n1,n2 = int(input("Inserisci un numero: ")),int(input("Inserisci un numero: "))
# n2 = int(input("Inserisci un numero: "))

d = {"+":somma,"-":differenza,"/":divisione,"*":prodotto}

print(d[op](n1,n2))

exit()
n = int(input("Inserisci un numero: "))

if n % 2 == 0:
    if n % 3 ==0:
        if n % 5 == 0:
            print("Il numero è divisibile per 2,3 e 5")
        else :
            print("Il numero è divisibile per 2 e 3")
    else:
        if n % 5 == 0:
            print("Il numero è divisibile per 2 e 5")
else:
    if n % 3 ==0:
        if n % 5 == 0:
            print("Il numero è divisibile per 3 e 5")
        else :
            print("Il numero è divisibile per 3")
    else:
        print("Non è divisibile")
exit()

n = int(input("Inserisci un numero: "))

if n % 3 == 0:
    print("Si")
else :
    print("no")