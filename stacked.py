import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from lanareikn import reiknalan

H = 10000000
rN = 5.5
rR = 2.24
ir = 4
L = 30

[G,A,V,Eeg,Nr] = reiknalan(H,rN,rR,ir,L)

fig, axs = plt.subplots(2, 2, figsize=(10, 7))
plt.subplots_adjust(bottom=0.25)

Glojg, =  axs[0,0].plot(Nr[1:], G[1:,0], lw=2)
Gloja, = axs[0,1].plot(Nr[1:], G[1:,1], lw=2)
Glvjg, = axs[1,0].plot(Nr[1:], G[1:,2], lw=2)
Glvja, = axs[1,1].plot(Nr[1:], G[1:,3], lw=2)

AVlojg, = axs[0,0].plot(Nr[1:], A[1:,0], lw=2)
AVloja, = axs[0,1].plot(Nr[1:], A[1:,1], lw=2)
AVlvjg, = axs[1,0].plot(Nr[1:], A[1:,2], lw=2)
AVlvja, = axs[1,1].plot(Nr[1:], A[1:,3], lw=2)

Vlojg, =  axs[0,0].plot(Nr[1:], V[1:,0], lw=2)
Vloja, = axs[0,1].plot(Nr[1:], V[1:,1], lw=2)
Vlvjg, = axs[1,0].plot(Nr[1:], V[1:,2], lw=2)
Vlvja, = axs[1,1].plot(Nr[1:], V[1:,3], lw=2)
#ax1 = axs[0,0].gca()

axs[0,0].set_title('Óverðtrygggt jafnar greiðslur')
axs[0,1].set_title('Óverðtryggt jafnar afborganir')
axs[1,0].set_title('Verðtryggt jafnar greiðslur')
axs[1,1].set_title('Verðtryggt jafnar afborganir')

H0=H
i0=ir
L0=L
rN0=rN
rR0=rR
#allowedN=np.linspace(5,40,36)

axcolor = 'black'

Haxes = plt.axes([0.2, 0.05, 0.65, 0.015], facecolor=axcolor)
Laxes = plt.axes([0.2, 0.07, 0.65, 0.015], facecolor=axcolor)
iraxes = plt.axes([0.2, 0.09, 0.65, 0.015], facecolor=axcolor)
rNaxes = plt.axes([0.2, 0.11, 0.65, 0.015], facecolor=axcolor)
rRaxes = plt.axes([0.2, 0.13, 0.65, 0.015], facecolor=axcolor)

Hbr = Slider(Haxes, 'Höfuðstóll', 5000000, 60000000, valinit=H0, valfmt='%0.0f')
ibr = Slider(iraxes, 'Verðbólga', 0, 10, valinit=i0)
rNbr = Slider(rNaxes, 'Óverðtryggðir vextir', 1, 10, valinit=rN0)
rRbr = Slider(rRaxes, 'Verðtryggðir vextir', 0.1, 10, valinit=rR0)
Lbr = Slider(Laxes, 'Lengd láns', 5, 40, valinit=L0, valfmt='%0.0f')

def update(val):
    H = int(Hbr.val)
    ir = ibr.val
    rN = rNbr.val
    rR = rRbr.val
    L = int(Lbr.val)
    [G,A,V,Eeg,Nr] = reiknalan(H,rN,rR,ir,L)
    Glojg.set_data(Nr[1:],G[1:,0])
    Gloja.set_data(Nr[1:],G[1:,1])
    Glvjg.set_data(Nr[1:],G[1:,2])
    Glvja.set_data(Nr[1:],G[1:,3])
    AVlojg.set_data(Nr[1:],A[1:,0])
    AVloja.set_data(Nr[1:],A[1:,1])
    AVlvjg.set_data(Nr[1:],A[1:,2])
    AVlvja.set_data(Nr[1:],A[1:,3])
    Vlojg.set_data(Nr[1:],V[1:,0])
    Vloja.set_data(Nr[1:],V[1:,1])
    Vlvjg.set_data(Nr[1:],V[1:,2])
    Vlvja.set_data(Nr[1:],V[1:,3])
    axs[0,0].set_xlim((0,L*12))
    axs[0,1].set_xlim((0,L*12))
    axs[1,0].set_xlim((0,L*12))
    axs[1,1].set_xlim((0,L*12))
    axs[0,0].set_ylim((0,max(G[:,0])+10000))
    axs[0,1].set_ylim((0,max(G[:,1])+10000))
    axs[1,0].set_ylim((0,max(G[:,2])+10000))
    axs[1,1].set_ylim((0,max(G[:,3])+10000))
    #fig.canvas.draw_idle()

Hbr.on_changed(update)
ibr.on_changed(update)
rNbr.on_changed(update)
rRbr.on_changed(update)
Lbr.on_changed(update)

plt.show()
