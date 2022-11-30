class quadrato():
    def __init__(self,t1,t2,t3,t4,p):
        self.l = [t1,t2,t3,t4]
        self.p = p
    
    def area(self):
        return 1/2*abs(self.l[0][0]*self.l[1][1] + self.l[1][0]*self.l[2][1] + self.l[2][0]*self.l[3][1] + self.l[3][0]*self.l[0][1] - self.l[1][0]*self.l[0][1] - self.l[2][0]*self.l[1][1] - self.l[3][0]*self.l[2][1] - self.l[0][0]*self.l[3][1])

    def per(self):
        return (quadrato.area(self)**0.5)*4

    def esterno(self):
        minx = self.l[0][0]
        miny = self.l[0][1]

        maxx = self.l[0][0]
        maxy = self.l[0][1]

        for i in range(1,4):
            if (self.l[i][0]>maxx):
                maxx = self.l[i][0]
            if (self.l[i][1]>maxy):
                maxy = self.l[i][1]
            if (self.l[i][0]<minx):
                minx = self.l[i][0]
            if (self.l[i][1]<miny):
                miny = self.l[i][1]

        if (self.p[0]<minx or self.p[0]>maxx or self.p[1]<miny or self.p[1]>maxy):
            print("Il punto è esterno")
        else:
            print("Il punto è interno")
            
def main():
    quad = quadrato((0,5),(0,0),(5,0),(5,5),(11,2))

    print(f"L'area vale: {quad.area()}")
    print(f"Il perimetro vale: {quad.per()}")

    quad.esterno()

if __name__=="__main__":
    main()