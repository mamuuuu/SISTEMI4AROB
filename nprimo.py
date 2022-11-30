def Primo(x):
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

n = int(input("Inserisci un numero: "))

print(Primo(n))

"""""
i=2
Primo = True
while (i< (int(n**0.5)+1) and primo == True):
    if (n%i == 0):
        primo = False
    i+=1

for i in range (2,n):
    if (n/i == 0):
        primo = False

if primo:
    print("Il numero e' primo")
else:
    print("Il numero non e' primo")
"""