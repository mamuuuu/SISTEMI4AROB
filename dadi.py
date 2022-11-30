import random

def main():
    l1 = [random.randint(1,6) for _ in range(0,10)]
    l2 = [random.randint(1,6) for _ in range(0,10)]

    file = open("./dadi/dadi.txt","w")

    for k in range(0,10):
        file.write(f"n{k+1}: {l1[k]}, {l2[k]}\n")
        
    print(l1)
    print(l2)

    file.close()

if __name__=="__main__":
    main()