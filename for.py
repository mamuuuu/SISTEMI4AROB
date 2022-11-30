from xml.dom.expatbuilder import parseString

l = [11,22,33,44,55]

#modo preferito (pythonico)
""""""
for elemento in l:
    print(elemento)

#modo c-style
for i in range(0,len(l)):
    print(l[i], end="-")
""""""

min = l[0]
max = l[0]

for elemento in l[1:]:
    if min > elemento:
        min = elemento
    else:
        pass
    if max < elemento:
        max = elemento
    else:
        pass

print(f"Il minore e': {min}, il maggiore e': {max}")
