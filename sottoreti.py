import math

NUM = 32

def bin2dec(Ip):
    """
    Conversione di una stringa di ip in binario in decimale
    """
    lista_bin_Rete=Ip.split(".")
    d = ""
    for num in lista_bin_Rete:
        temp = int(num,2)
        d = d + str(temp) +"."
    return d[:-1]

def ip_def(ip):
    """
    Scrittura dell'ip 
    """
    ip_stringa = ""
    s, e = 0,8
    while (e<=32):
        ip_stringa += ip[s:e] + "."
        s += 8
        e += 8
    return ip_stringa[:-1]

class Sottoreti():
    def __init__(self, ip, n):
        self.ip = ip
        self.n = n
        self.lista_ip_sm = []               #lista con posizione 0 IP stringa con "." e 1 SM
        self.lista_ip = []                  #lista con IP int 
        self.ip_bin = ""                    #stringa con IP in binario
        self.ip_notazione_bin_sp = ""       #stringa con IP in binario senza punto
        self.new_sm = None                  #nuova sm
        self.lista_combinazioni = []

    def ip_split(self):
        self.lista_ip_sm  = self.ip.split("/")
        self.lista_ip = self.lista_ip_sm[0].split(".")
            
    
        
    def new_SM(self):
        self.new_sm = (int)(self.lista_ip_sm[1]) + math.ceil(math.log((float)(self.n),2))

    def combinazioni(self):
        for i in range (0,self.n):
            s = bin(i)[2:]
            self.lista_combinazioni.append("0"*(math.ceil(math.log((float)(self.n),2))-len(s)))
            self.lista_combinazioni[i]+=s
    
    def sottoreti(self):
        for i in range (0,self.n):
            temp = self.ip_notazione_bin_sp[:(int)(self.lista_ip_sm[1])] + self.lista_combinazioni[i]
            ip_r = temp + "0"*(NUM-len(temp))
            ip_b = temp + "1"*(NUM-len(temp))

            print(f"\nIP SOTTORETE {i+1}:")

            print(f"Ip rete: \t", end="")
            print(f"{ip_def(ip_r)}", end="")
            print(f" - \t{bin2dec(ip_def(ip_r))}", end="")

            print(f"\nIp brodcast: \t", end="")
            print(f"{ip_def(ip_b)}", end="")
            print(f" - \t{bin2dec(ip_def(ip_b))}", end="\n")

def main():
    ip = input("inserisci l'ip: ")
    n = (int)(input("Inserisci il numero di sottoreti: "))

    sottoreti = Sottoreti(ip,n)
    
    sottoreti.ip_split()
    sottoreti.dec2bin()
    sottoreti.new_SM()
    sottoreti.combinazioni()
    sottoreti.sottoreti()

if __name__=="__main__":
    main()