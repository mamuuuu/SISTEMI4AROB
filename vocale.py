vocali = ["a","e","i","o","u"]

s = input("Inserisci una stringa: ")
l = [c for c in s if not(c in vocali)]

print(l)