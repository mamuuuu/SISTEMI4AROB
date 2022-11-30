
l = ["ciao", print, 1.2]



exit()

d = {"w":"avanti", "a":"sinistra", "s":"indietro","d":"destra", "i":"avanti", "j":"sinistra", "k": "indietro", "l": "destra"}

comando = "avanti"
lista_pulsanti=[]

for k,v in d.items():
    if d[k]==comando:
        lista_pulsanti.append(k)

print(lista_pulsanti)


for k,v in d.items():
    print(k,v)

