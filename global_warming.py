"""
Tracciamento grafico
ragiona su una figura (fig) al suo interno si possono fare più grafici.
fig, (ax1, ax2) = plt.subplots(2, 1) divide la figura in due righe e cuna colonna
restituisce per ogni parte una coppia di assi (ax1 e ax2, due coppie di assi)
fig.suptitle(): titolo della figura

chiamate per coppia di assi 
ax1.plot(mesi_n, voti, 'o-g') 
ax1.set_xlabel('Mese') 
ax1.set_ylabel('Voto medio di tutte le materie')

stile linea
o- : linea continua che per ogni punto c'è il pallino 
g : green
r : red
...

correlazione e anticorrelazione --> andamento simile dei due grafici
"""

#import matplotlib as mpl 
#mpl.use('TkAgg') 
import matplotlib.pyplot as plt 
import csv 

"""
Lettura file e caricamento liste
"""
year = []
total =[]
gas_fuel = [] 
liquid_fuel = []
solid_fuel = []
cement = [] 
gas_flaring = []
per_capita = []

year1 = []
anomaly = []

data_file1 = open("./CO2_emissions.csv") 
data_file2 = open("./Temperature_Anomaly.csv")
data_reader1 = csv.reader(data_file2, delimiter=",")
data_reader = csv.reader(data_file1, delimiter=',') 
next(data_reader) 
next(data_reader1)

for row in data_reader1:
    year1.append(int(row[0]))
    anomaly.append(float(row[1]))

for row in data_reader: 
    year.append(int(row[0])) 
    total.append(float(row[1])) 
    gas_fuel.append(int(row[2]))
    liquid_fuel.append(int(row[3]))
    solid_fuel.append(float(row[4]))
    cement.append(float(row[5]))
    gas_flaring.append(float(row[6]))
    #per_capita.append((row[7]))


fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, 1) 
#fig.suptitle('Media dei voti di tutte le materie e  ore di studio giornaliere medie nel periodo  Gennaio-Giugno') 

ax1.plot(year, total, '-r') 
ax1.set_xlabel('Year') 
ax1.set_ylabel('total')

ax2.plot(year, gas_fuel, '-g') 
ax2.set_xlabel('Year') 
ax2.set_ylabel('gas_fuel') 

ax3.plot(year, liquid_fuel, '-y') 
ax3.set_xlabel('Year') 
ax3.set_ylabel('liquid_fuel') 

ax4.plot(year, solid_fuel, '-g') 
ax4.set_xlabel('Year') 
ax4.set_ylabel('solid_fuel') 

ax5.plot(year, cement, '-b') 
ax5.set_xlabel('Year') 
ax5.set_ylabel('cement') 

ax6.plot(year, gas_flaring, '-r') 
ax6.set_xlabel('Year') 
ax6.set_ylabel('gas_flaring') 

ax7.plot(year1, anomaly, '-b') 
ax7.set_xlabel('Year') 
ax7.set_ylabel('anomaly') 

data_file1 = open("./CO2_emissions.csv") 
data_reader = csv.reader(data_file1, delimiter=',') 

plt.show()
