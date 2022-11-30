s = "ckikakok"
s2 = s[::2]

print(s2)
exit()
d = {"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t",
    "t":"u","u":"v","v":"z","z":"a"," ":" "}

s = input("Inserisci una stringa: ")

s1=""
d1 ={}

for lettera in s:
    s1= s1 + d[lettera]
print(s1)

for k,v in d.items():#ciclo for su due variabili contemporaneamente
    #print(k,v)
    d1[v]= k

s2 = ""
for lettera in s1:
    s2= s2 + d1[lettera]
print(s2)
