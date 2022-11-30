"""
#List Comprehnsion

n = int(input("Inserisci: "))

l = [i for i in range(1,n+1)]

print(l)

l = [i * i for i in range(1,11)]
print(l)
"""
def Primo(x):
    for i in range (2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

l = [i for i in range(1,100) if Primo(i)]

"""
l = []

for i in range (1,101):
    if (Primo(i)):
        l.append(i)
print(l)
"""