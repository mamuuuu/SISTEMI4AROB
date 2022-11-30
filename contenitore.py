#TUPLE
import math

punto = (1.5,3.6)
print(f"Coordinate: {punto}")
triangolo = [(0,0),(0,2),(3,0)]
print(f"Vertici: {triangolo[0]}, {triangolo[1]}, {triangolo[2]}")

print(1/2*abs(triangolo[0][0]*triangolo[1][1] + triangolo[0][1]*triangolo[2][0] + triangolo[1][0]*triangolo[2][1] 
    - triangolo[2][0]*triangolo[1][1] + triangolo[2][1]*triangolo[0][0] + triangolo[1][0]*triangolo[0][1]))