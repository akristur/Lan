import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def reiknalan(H,rN,rR,ir,L):

    rNp = rN/100
    rNpk = rNp/12
    rRp=rR/100
    rRpk=rRp/12
    irp=ir/100
    irpk=np.exp(np.log(irp+1)/12)-1
    Ln = L*12

    A = np.empty((Ln+1,4), dtype = float)
    V = np.empty((Ln+1,4), dtype = float)
    Efg = np.empty((Ln+1,4), dtype = float)
    Eeg = np.empty((Ln+1,4), dtype = float)
    G = np.empty((Ln+1,4), dtype = float)
    GH = np.empty((Ln+1,4), dtype = float)
    Nr = np.full(Ln+1,0)
    Gg = 130

    Efg[0,:]=0
    Eeg[0,:]=H
    G[:,0] = ((rNpk*H)*np.power(1+rNpk,Ln))/(np.power(1+rNpk,Ln)-1)
    G[0,:] = 0
    A[:,1] = H/Ln
    A[0,:] = 0
    V[0,:] = 0


    for i in range(1, Ln+1):
        Nr[i]=i

        #óverðtryggt ójafnar greiðslur
        Efg[i,0]=Eeg[i-1,0]
        A[i,0]=(rNpk*Efg[1,0]*np.power(1+rNpk,Nr[i-1]))/(np.power(1+rNpk,Ln)-1)
        V[i,0]=G[i,0]-A[i,0]
        Eeg[i,0]=Efg[i,0]-A[i,0]
        GH[i,0]=G[i,0]+Gg

        #óverðtryggt jafnar afborganir
        G[i,1]=H/Ln+rNpk*H*(1-Nr[i-1]/Ln)
        V[i,1]=G[i,1]-A[i,1]
        Efg[i,1]=Eeg[i-1,1]
        Eeg[i,1]=Efg[i,1]-A[i,1]
        GH[i,1]=G[i,1]+Gg

        #verðtryggt jafnar greiðslur
        Efg[i,2]=Eeg[i-1,2]*(1+irpk)
        G[i,2]=Efg[i,2]*(rRpk+rRpk/(np.power(1+rRpk,Ln-Nr[i-1])-1))
        A[i,2]=G[i,2]-(Efg[i,2]*rRpk)
        V[i,2]=G[i,2]-A[i,2]
        Eeg[i,2]=Efg[i,2]-A[i,2]
        GH[i,2]=G[i,2]+Gg

        #verðtryggt jafnar afborganir
        Efg[i,3]=Eeg[i-1,3]*(1+irpk)
        A[i,3]=Efg[i,3]/(Ln-Nr[i-1])
        V[i,3]=Efg[i,3]*rRpk
        G[i,3]=A[i,3]+V[i,3]
        Eeg[i,3]=Efg[i,3]-A[i,3]
        GH[i,3]=G[i,3]+Gg

    return G,A,V,Eeg,Nr

#print(Nr)
#print(A)
#print(V)
#print(Efg)
#print(Eeg)
