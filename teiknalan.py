import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from lanareikn import reiknalan

H = 38000000
rN = 10
rR = 2.6
ir = 4
L = 40

[G,A,V,Eeg,Nr] = reiknalan(H,rN,rR,ir,L)

fig, axs = plt.subplots(2, 2, figsize=(10, 7))
plt.subplots_adjust(bottom=0.25)


Eeglojg, =  axs[0,0].plot(Nr, Eeg[:,0], lw=2, label='óverðtr. jafnar gr.')
Eegloja, = axs[0,0].plot(Nr, Eeg[:,1], lw=2, label='óverðtr. jafnar afb.')
Eeglvjg, = axs[0,0].plot(Nr, Eeg[:,2], lw=2, label='verðtr. jafnar gr.')
Eeglvja, = axs[0,0].plot(Nr, Eeg[:,3], lw=2, label='verðtr. jafnar afb.')

Glojg, =  axs[0,1].plot(Nr[1:], G[1:,0], lw=2)
Gloja, = axs[0,1].plot(Nr[1:], G[1:,1], lw=2)
Glvjg, = axs[0,1].plot(Nr[1:], G[1:,2], lw=2)
Glvja, = axs[0,1].plot(Nr[1:], G[1:,3], lw=2)


Alojg, =  axs[1,0].plot(Nr[1:], A[1:,0], lw=2)
Aloja, = axs[1,0].plot(Nr[1:], A[1:,1], lw=2)
Alvjg, = axs[1,0].plot(Nr[1:], A[1:,2], lw=2)
Alvja, = axs[1,0].plot(Nr[1:], A[1:,3], lw=2)

Vlojg, =  axs[1,1].plot(Nr[1:], V[1:,0], lw=2)
Vloja, = axs[1,1].plot(Nr[1:], V[1:,1], lw=2)
Vlvjg, = axs[1,1].plot(Nr[1:], V[1:,2], lw=2)
Vlvja, = axs[1,1].plot(Nr[1:], V[1:,3], lw=2)
#ax1 = axs[0,0].gca()

axs[0,0].set_title('Eftirstöðvar höfuðstóls')
axs[0,1].set_title('Mánaðarleg greiðsla')
axs[1,0].set_title('Afborgun af höfuðstól')
axs[1,1].set_title('Vextir af greiðslu')

axs[0,0].legend(loc='lower left')

H0=H
i0=ir
L0=L
rN0=rN
rR0=rR
#allowedN=np.linspace(5,40,36)

axcolor = 'lightgoldenrodyellow'

Haxes = plt.axes([0.2, 0.05, 0.65, 0.015], facecolor=axcolor)
Laxes = plt.axes([0.2, 0.07, 0.65, 0.015], facecolor=axcolor)
iraxes = plt.axes([0.2, 0.09, 0.65, 0.015], facecolor=axcolor)
rNaxes = plt.axes([0.2, 0.11, 0.65, 0.015], facecolor=axcolor)
rRaxes = plt.axes([0.2, 0.13, 0.65, 0.015], facecolor=axcolor)

Hbr = Slider(Haxes, 'höfuðstóll', 5000000, 60000000, valinit=H0, valfmt='%0.0f')
ibr = Slider(iraxes, 'verðbólga', 0, 10, valinit=i0)
rNbr = Slider(rNaxes, 'óverðtryggðir vextir', 1, 10, valinit=rN0)
rRbr = Slider(rRaxes, 'verðtryggðir vextir', 0.1, 10, valinit=rR0)
Lbr = Slider(Laxes, 'Lengd láns', 5, 40, valinit=L0, valfmt='%0.0f')

def update(val):
    H = int(Hbr.val)
    ir = ibr.val
    rN = rNbr.val
    rR = rRbr.val
    L = int(Lbr.val)
    [G,A,V,Eeg,Nr] = reiknalan(H,rN,rR,ir,L)
    Eeglojg.set_data(Nr,Eeg[:,0])
    Eegloja.set_data(Nr,Eeg[:,1])
    Eeglvjg.set_data(Nr,Eeg[:,2])
    Eeglvja.set_data(Nr,Eeg[:,3])
    Glojg.set_data(Nr[1:],G[1:,0])
    Gloja.set_data(Nr[1:],G[1:,1])
    Glvjg.set_data(Nr[1:],G[1:,2])
    Glvja.set_data(Nr[1:],G[1:,3])
    Alojg.set_data(Nr[1:],A[1:,0])
    Aloja.set_data(Nr[1:],A[1:,1])
    Alvjg.set_data(Nr[1:],A[1:,2])
    Alvja.set_data(Nr[1:],A[1:,3])
    Vlojg.set_data(Nr[1:],V[1:,0])
    Vloja.set_data(Nr[1:],V[1:,1])
    Vlvjg.set_data(Nr[1:],V[1:,2])
    Vlvja.set_data(Nr[1:],V[1:,3])
    axs[0,0].set_xlim((0,L*12))
    axs[0,1].set_xlim((0,L*12))
    axs[1,0].set_xlim((0,L*12))
    axs[1,1].set_xlim((0,L*12))
    axs[0,0].set_ylim((0,max(Eeg[:,2])+2000000))
    axs[0,1].set_ylim((min(G[1:,1])-10000,max(G[:,2])+10000))
    axs[1,0].set_ylim((min(A[1:,0])-10000,max(A[:,2])+10000))
    axs[1,1].set_ylim((0,max(V[1:,1])+10000))
    #fig.canvas.draw_idle()

Hbr.on_changed(update)
ibr.on_changed(update)
rNbr.on_changed(update)
rRbr.on_changed(update)
Lbr.on_changed(update)

plt.show()

#[G,A,V,Eeg,Nr] = reiknalan(60000000,6,3,3,40)
#print(Eeg[420:,2])
#fig, tst = plt.subplots(2,2)
#Eegl40, =  tst[0,0].plot(Nr[0:61], Eeg[420:,2], lw=2)
#Gl40, =  tst[0,1].plot(Nr[0:60], G[421:,2], lw=2)
#Al40, =  tst[1,0].plot(Nr[0:60], A[421:,2], lw=2)
#V40, =  tst[1,1].plot(Nr[0:60], V[421:,2], lw=2)
#print(V[421:,2])
#print(A[421:,2])
#print(G[421:,2])
#print(G-A-V)
#print('skil')
#[G,A,V,Eeg,Nr] = reiknalan(33635803.85,6,3,3,5)
#Eegl5, = tst[0,0].plot(Nr, Eeg[:,2], lw=2)
#Gl5, = tst[0,1].plot(Nr[0:60], G[1:,2], lw=2)
#Al5, = tst[1,0].plot(Nr[0:60], A[1:,2], lw=2)
#Vl5, = tst[1,1].plot(Nr[0:60], V[1:,2], lw=2)
#print(Eeg[:,2])
#print(V[1:,2])
#print(A[1:,2])
#print(G[1:,2])
#print(G-A-V)
#tst[0,1].set_ylim((0,200000))

#plt.show()
