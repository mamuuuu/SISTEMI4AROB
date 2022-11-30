#es5

s = "ckikakok"
s1 = ""

s1 = s[::2]

print(s1)
exit()
#es6

n = int(input("Inserisci: "))

l1 = [1] * n
l1[0],l1[n-1]=0,0

print(l1)

exit()
#es7

n = int(input("Inserisci: "))
l=[]

for i in range (1,n+1):
    l.append(i)

print(l)

exit()