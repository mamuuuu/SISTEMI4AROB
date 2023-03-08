def somma(a,b):
    return a+b

def main():
    somma.descrizione = "Calcolo Somma"
    print(somma(5,3))
    print(somma)
    print(somma.descrizione)

if __name__=="__main__":
    main()