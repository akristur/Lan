import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from lanareikn import reiknalan
from getdata import getuppl


av = 3.0
avpr = av/100
avprk = avpr/12

H = 60000000
rN = 4.2
rR = 2.24
ir = 4.8
L = 40

PV = []

[G,A,V,Eeg,Nr] = reiknalan(H,rN,rR,ir,L)

PVojg = np.matmul(G[1:,0],1/np.power((1+avprk),Nr[1:]))
PVoja = np.matmul(G[1:,1],1/np.power((1+avprk),Nr[1:]))
PVvjg = np.matmul(G[1:,2],1/np.power((1+avprk),Nr[1:]))
PVvja = np.matmul(G[1:,3],1/np.power((1+avprk),Nr[1:]))
PV.append(PVojg)
PV.append(PVoja)
PV.append(PVvjg)
PV.append(PVvja)

[lanveitandi,lantokugjald,vobint,vofint,vvbint,vvfint,vobintvidb,vofintvidb,vvbintvidb,vvfintbidb,uppgreidslugjald] = getuppl()

Gall = []

[G,A,V,Eeg,Nr] = reiknalan(H,vobint[16],vvbint[16],ir,L)

PVAojgbv = np.matmul(G[1:,0],1/np.power((1+avprk),Nr[1:]))
PVAojabv = np.matmul(G[1:,1],1/np.power((1+avprk),Nr[1:]))
PVAvjgbv = np.matmul(G[1:,2],1/np.power((1+avprk),Nr[1:]))
PVAvjabv = np.matmul(G[1:,3],1/np.power((1+avprk),Nr[1:]))
PV.append(PVAojgbv)
PV.append(PVAojabv)
PV.append(PVAvjgbv)
PV.append(PVAvjabv)

[G,A,V,Eeg,Nr] = reiknalan(H,vofint[16],vvfint[16],ir,L)

PVAojgfv = np.matmul(G[1:,0],1/np.power((1+avprk),Nr[1:]))
PVAojafv = np.matmul(G[1:,1],1/np.power((1+avprk),Nr[1:]))
PVAvjgfv = np.matmul(G[1:,2],1/np.power((1+avprk),Nr[1:]))
PVAvjafv = np.matmul(G[1:,3],1/np.power((1+avprk),Nr[1:]))
PV.append(PVAojgfv)
PV.append(PVAojafv)
PV.append(PVAvjgfv)
PV.append(PVAvjgfv)

nr = np.linspace(0, 11, 12)
print(nr)

plt.bar(nr,PV)
plt.show()
print(PV)
#for i in range(0:len(lanveitandi)):
#    [G,A,V,Eeg,Nr] = reiknalan(H,vobint[0],vvint[0],ir,L)
#    PVojgbv = np.matmul(G[1:,0],1/np.power((1+avprk),Nr[1:]))
#    PVojabv = np.matmul(G[1:,1],1/np.power((1+avprk),Nr[1:]))
#    PVvjgbv = np.matmul(G[1:,2],1/np.power((1+avprk),Nr[1:]))
#    PVvjabv = np.matmul(G[1:,3],1/np.power((1+avprk),Nr[1:]))

print(lanveitandi)

print(sum(G[1:,0]))
print(sum(G[1:,1]))
print(sum(G[1:,2]))
print(sum(G[1:,3]))
print(PVojg)
print(PVoja)
print(PVvjg)
print(PVvja)
