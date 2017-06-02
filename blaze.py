"""
Lily Zhao
January 2017

with some minor changes/comments by Allen Davis
"""

import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

sigma=31.64557*1000
sb=75.55*np.pi/180.

def BF(m,lambs,sigma=sigma,sb=sb):
    #Returns Blaze Function Values for given order, m, at specified wavelengths, lambs
    
    #sigma: line spacing, nanometers
    #sb: blaze angle, radians
    lamb_b=2.*sigma/m*np.sin(sb)
    
    nu=m*np.pi*(lamb_b-lambs)/lambs
    blaze=(np.sin(nu)/nu)**2

    return blaze
   
def blazeFunc(m,num_lamb=24,specific_lambs=[],sigma=sigma,sb=sb,gamma=0.5*np.pi/180.):
    #Find free spectral range
    alpha=beta=sb
    c0=sigma*np.cos(gamma)
    c1=c0*(np.sin(alpha)+np.sin(beta))
    lamb_m=c1/m #central wavelength
    lamb_b=2.*sigma/m*np.sin(sb)
    dlamb_m=lamb_b/m/2.

    #Blaze values with side-lobes cut off
    lambs=np.linspace(lamb_m-dlamb_m*2,lamb_m+dlamb_m*2,num_lamb)
    lambs=np.concatenate([lambs,specific_lambs,[lamb_m]])
    blaze=BF(m,lambs,sigma=sigma,sb=sb)
    
    #Blaze values of just the free spectra range segment
    fsr=np.linspace(lamb_m-dlamb_m,lamb_m+dlamb_m,num_lamb)
    blaze_fsr=BF(m,fsr,sigma=sigma,sb=sb)
    
    return lambs, blaze, fsr, blaze_fsr

"""
#Stuff for testing
m=[161,160,157,153,148,143,138,134,133,132,127,121,114,107,99,91,90]
lambs=np.linspace(350,8700,10000)

colors=sns.color_palette('Oranges_r',10)
counter=0
for i in np.arange(90,161,10):
    plt.plot(lambs,bf(i,lambs),color=colors[counter])
    counter+=1
"""
