def scrivi(nome_fp,tav):
    file = open(nome_fp,"w")

    for r in range(0,10):
        for c in range(0,10):
            print(tav[r][c])
            file.write(f"{tav[r][c]}\t ",)
        file.write("\n")
    file.close()

def main():
    tav = [[i * n for i in range(1,11)]for n in range(1,11)]
    print(tav)
    
    scrivi("./tav/tav.txt",tav)

if __name__=="__main__":
    main()
    