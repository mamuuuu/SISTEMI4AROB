def leggi_file(nome_fp):
    file = open(nome_fp,"r")
#lista contente righe del file
    lista_righe=file.readlines()
#chiusura
    file.close()

    diz_nomi={"id":[],"nomi":[]}#id nomi, nomi str

    for riga in lista_righe[1:]:
        riga_senza_acapo = riga[:-1]
    
    #chiamiamo una ovlta per riga lo split sulla str, e restitutisce tutti i campi
        lista_campi = riga_senza_acapo.split(",")
        id = int(lista_campi[0])
        nome = lista_campi[1]

    #carica nel dizionario nomi e id
        diz_nomi["id"].append(id)
        diz_nomi["nomi"].append(nome[1:])

    return diz_nomi

#leggere un file open("path","modalità")
diz_nomi = leggi_file("fp.csv")

print (diz_nomi)