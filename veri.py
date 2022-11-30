"""
1)Stampare il valore totale degli incassi e restituire se si è raggiunto il totale di 2,200 euro
indicando in modo preciso le possibili anomalie (Esempio: mancano 80 euro) (punti 3)
2) Ricerca il vostro nome, salvarlo in una struttura (campi: Cognome, quota) e verificare se avete
pagato tutto la quota. Gestire questa parte utilizzando una sola riga della struct (punti 3.5)
3)Restituire un report che indichi la situazione di tutti gli studenti, aggiungere un semplice
messaggio nella printf in caso di anomalie (punti 3,5)
"""
def leggi_file(nome_fp):
    file = open(nome_fp,"r")
    lista_righe=file.readlines()
    file.close()

    tot = 0
    diz_nomi={}

    for riga in lista_righe:
        lista_campi = riga[:-1].split(";")

        tot += int(lista_campi[2])

        if (lista_campi[1] in diz_nomi):
            diz_nomi[lista_campi[1]]+=int(lista_campi[2])
        else:
            diz_nomi[lista_campi[1]]=int(lista_campi[2])

    return diz_nomi,tot

def controllo(tot):
    if (tot == 2200):
        print("Ci sono esattamente 2200 euro.")
    else:
        if (tot > 2200):
            print(f"Ci sono in più {tot-2200} euro.")
        else:
            print(f"Ci sono in meno {2200-tot} euro.")

def alunno(nome,nomi):

    tot = 0
    for k,v in nomi.items():
        if k==nome:
            tot += v
    
    return tot

def riepilog(nomi):

    for k,v in nomi.items():
        print(f"{k}: {v}", end = "")
        if (v<100):
            print("-- DA CONTROLLARE\n")
        else:
            print("\n")

def main():
    nomi,totale = leggi_file("./fp.csv")

    controllo(totale)

    io = {}
    io ["Meinero"] = alunno("Meinero", nomi)

    print(io)

    riepilog(nomi)

if __name__=="__main__":
    main()



