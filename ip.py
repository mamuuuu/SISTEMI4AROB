#DATO UN QUALSIASI INDIRIZZO IP E LA SUA SM CALCOLA IN BINARIO PUNTATO E DECIMALE PUNTATO
#INDIRIZZO IP DI RETE, BROADCAST, PRIMO E ULTIMO INDIRIZZO UTILE

#conversione binaria di un numero
def bin (n,n_bin):
    for i in range (1,9):
        if n % 2 == 1:
            n_bin[-i] = 1
        n = n // 2

#conversione in decimale 
def dec (n,l):
    k = 0
    for c in range (0,4):
        for i in range (1,9):
            if n[c][-i] == 1:
                l[c]+=2**k
            k+=1
        k=0

#stampa del IP in binario puntato
def visualizzaBinario(n_bin):
    
    for i in range (0,4):
        for c in range (0,8):
            print(f"{n_bin[i][c]}", end="")
        if i<3:
            print(".", end="")
    print("\n")

#stampa del IP in decimale puntato
def visualizzaIntero(l_int):
    
    for i in range(0,4):
        print(f"{l_int[i]}",end="")
        if i<3:
            print(".", end="")
    print("\n")

#calcolo del IP di broadcast in binario
def ip_broadcast(sm,ip_broadcast_bin):

    bit_host = 32 - sm
    n_byte = bit_host // 8
    n_byte_resto = bit_host - (n_byte * 8)
    
    if n_byte > 0:
        for i in range (1,n_byte+1):
            for c in range (0,8):
                ip_broadcast_bin[-i-4][c]=1

    for k in range (1,n_byte_resto+1):
        ip_broadcast_bin[-5-n_byte][-k]=1

#calcolo del IP di rete in binario
def ip_rete(sm,ip_rete_bin):

    bit_host = 32 - sm
    n_byte = bit_host // 8
    n_byte_resto = bit_host - (n_byte * 8)
    
    if n_byte > 0:
        for i in range (1,n_byte+1):
            for c in range (0,8):
                ip_broadcast_bin[-i-4][c]=0

    for k in range (1,n_byte_resto+1):
        ip_broadcast_bin[-5-n_byte][-k]=0



n_bin = [[0]*8,[0]*8,[0]*8,[0]*8]               #lista di liste con i numeri in binario
l=[]                                            #lista coi 4 numeri dell'IP
l_int=[0]*4                                     #lista con conversione da bin a dec

ip_broadcast_bin = [[0]*8,[0]*8,[0]*8,[0]*8]    #lista di liste con valore binario dell ip di broadcast
broadcast_int = [0]*4                           #lista con IP di broadcast decimale puntato

ip_rete_bin = [[0]*8,[0]*8,[0]*8,[0]*8]         #lista di liste con valore binario dell ip di rete
ip_rete_int = [0]*4                             #lista con IP di rete decimale puntato

primo_ip_bin = [[0]*8,[0]*8,[0]*8,[0]*8]        #lista di liste con valore binario dell primo ip utile
primo_ip_dec = [0]*4                            #lista con IP dell primo ip utile

ultimo_ip_bin = [[0]*8,[0]*8,[0]*8,[0]*8]       #lista di liste con valore binario dell dell ultimo ip utile
ultimo_ip_dec = [0]*4                           #lista con IP dell ultimo ip utile decimale puntato


sm = int(input("Inserisci SM: |"))              #Subnet Mask


#Inserimento dell'IP
for i in range (0,4):
    l.append(int(input("Inserisci la prima cifra dell'IP: \n")))


#conversione inn  binario dell'IP inserito
for n,elemento in enumerate(l):
    n_bin.append(bin(elemento,n_bin[n]))


#stampa del IP 
print("IP binario puntato: ")
visualizzaBinario(n_bin)


#calcolo del IP di broadcast
ip_broadcast_bin=n_bin
ip_broadcast(sm,ip_broadcast_bin)


#stampa IP broadcast binario
print(f"IP broadcast binario puntato:")
visualizzaBinario(ip_broadcast_bin)


#conversione IP di broadcast decimale
dec(ip_broadcast_bin,broadcast_int)


#stampa IP broadcast decimale
print(f"IP broadcast decimale puntato:")
visualizzaIntero(broadcast_int)


#calcolo ultimo IP utile
ultimo_ip_bin = ip_broadcast_bin
ultimo_ip_bin [3][-1] = 0


#stampa ultimo IP utile binario puntato
print("L'ultimo IP utile in binario puntato è: ")
visualizzaBinario(ultimo_ip_bin)


#conversione ultimo IP utile in decimale puntato
dec(ultimo_ip_bin,ultimo_ip_dec)


#stampa ultimo IP utile decimale puntato
print("L'ultimo IP utile in decimale puntato è: ")
visualizzaIntero(ultimo_ip_dec)


#calcolo del IP di rete
ip_rete_bin = n_bin
ip_rete(sm,ip_rete_bin)


#stampa IP rete binario
print("IP rete binario puntato:")
visualizzaBinario(ip_rete_bin)


#conversione IP di rete decimale
dec(ip_rete_bin,ip_rete_int)


#stampa IP rete decimale
print(f"IP rete decimale puntato:")
visualizzaIntero(ip_rete_int)


#calcolo primo IP utile
primo_ip_bin = ip_rete_bin
primo_ip_bin [3][-1] = 1


#stampa primo IP utile binario puntato
print("Il primo IP utile in binario puntato è: ")
visualizzaBinario(primo_ip_bin)


#conversione primo IP utile in decimale puntato
dec(primo_ip_bin,primo_ip_dec)


#stampa primo IP utile decimale puntato
print("Il primo IP utile in decimale puntato è: ")
visualizzaIntero(primo_ip_dec)