import turtle

def lettura(nome):
    with open(nome,"r") as file:                    #struttura per copiare il contenuto di un file in una stringa,apre e chiude il file
        s = file.read()
    
    s = s.replace(",", "")
      
    righe = s.count("\n")
    colonne = len(s.split("\n")[0])
        
    mat = []

    for k in range(0,righe):
        m = [0]*colonne
        for i, car in enumerate(s.split("\n")[k]):
            if car == '0':
                m[i] = -1

        mat.append(m)

    return mat, righe, colonne

def mat_numerata(mat, righe, colonne):
    mat_n = []
    k = 0
    for r in range(0, righe):
        for c in range(0, colonne):
            if mat[r][c] == 0:
                mat[r][c] += k 
                k+=1
        mat_n.append(mat[r])
    
    return mat_n, k


def matrice(mat, righe, colonne):
    mA = []
    mat_num, n_celle = mat_numerata(mat, righe, colonne)
    print(mat_num, n_celle)
    
    for i, riga in enumerate(mat):

        for j, k in enumerate(riga):
            #print(i)
            #print(riga)
            #print(j, k)
            """
            """
            #if (k == 1):
            m = [0]*n_celle 
            if i == 0:                              #caso riga 0
                if (j == 0 and k > -1):             #caso della riga 0 colonna 0
                    if (riga[1] > -1):
                        m[1] = 1
                    if (mat[1][0] > -1):
                        m [mat_num[1][0]] = 1
                
                if (j == colonne-1 and k > -1):     #caso della riga 0 colonna max
                    if (riga[colonne-2] > -1):
                        m[colonne-2] = 1
                    if (mat[1][colonne-1] > -1):
                        m [mat_num[1][colonne-1]] = 1
                
                if (j != 0 and j != colonne-1):
                    if (riga[j-1] == 0):
                        m[j-1] = 1
                    if (riga[j+1] == 0):
                        m[j+1] = 1
                    if (mat[1][j] == 0):
                        m[j] = 1
            
            """
            """
            if i == righe-1:                              #caso riga max
                if (j == 0 and k > -1):                 #caso della riga max colonna 0
                    if (riga[1] > -1):
                        m[riga[1]] = 1
                    if (mat[righe-2][0] > -1):
                        m [mat_num[righe-2][0]] = 1
                
                if (j == colonne-1 and k > -1):         #caso della riga max colonna max
                    if (riga[colonne-2] > -1):
                        m[n_celle-2] = 1
                    if (mat[righe-2][colonne-1] > -1):
                        m[n_celle-colonne-1] = 1
                
                if (j != 0 and j != colonne-1):
                    if (riga[j-1] == 0):
                        m[j-1] = 1
                    if (riga[j+1] == 0):
                        m[j+1] = 1
                    if (mat[righe-2][j] == 0):
                        m[riga[j]-1] = 1

            
            """
            """
            """
            if i != righe-1 and i != 0:
                if (j == 0 and k > -1):             #caso della riga 0 colonna 0
                    if (riga[1] > -1):
                        m[] = 1
                    if (mat[1][0] > -1):
                        m [mat_num[1][0]] = 1

                if (j == colonne-1 and k > -1):     #caso della riga 0 colonna max
                    if (riga[colonne-2] > -1):
                        m[colonne-2] = 1
                    if (mat[1][colonne-1] > -1):
                        m [mat_num[1][colonne-1]] = 1
            """    

            mA.append(m)
   
    print(mA)


def main():
    
    mat, righe, colonne = lettura("rete.csv") 
    mat_ad = matrice(mat, righe, colonne)

if __name__=="__main__":
    main()
    

