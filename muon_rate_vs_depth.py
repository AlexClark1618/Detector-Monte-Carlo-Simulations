import numpy as np
from gaisser_formula import modified_gaisser_formula
from scipy import integrate
 
m_muon = 0.1057 #GeV

def minimum_energy(d, theta):
    """
    Minimum energy for a muon to traverse a distance x
    Should be equal to stopping power * density * distance
    """
    alpha = 2 #MeV cm^2/g #1.9 + 0.08*np.log(E/m_muon) #Approximate energy dependence
    epsilon = 2.55*10**5 #g/cm**2; for standard rock
    p = 2.65 #g/cm^3

    return alpha * epsilon * (np.exp((p*d)/(np.cos(theta)*epsilon)) - 1)/ 1000


A = 105.6 * 105.6 #Area in cm^2
#theta_max = np.arctan(105.6/33) #Max Angular acceptance
#To calculate the total flux I need to integrate over all possible energies and solid angle with a detector area projection correction term

def KoNova_rate_estimate(E, theta):
    """
    *10000 is to convert to m^2 ; cos(theta) term is for a float detector ; 2pisin(theta) is solid angle correction
    """
    
    return (10000*modified_gaisser_formula(E, theta))  #2 * np.pi * np.sin(theta)

int_list = []
depth_list = np.arange(0,100001, 1000)
for d in depth_list:
    I, err = integrate.nquad(KoNova_rate_estimate, [
        lambda theta: [minimum_energy(d, theta), np.inf],
        [0, np.pi/2]
    ])
    int_list.append(I)
    print(f"Depth: {d/100:.0f} m, Rate: {I:.4f} Hz")

import matplotlib.pyplot as plt


plt.plot(depth_list/100, int_list)
plt.yscale('log')
plt.ylabel("Muon Rate (m^-2 s^-1 sr^-1)")
plt.xlabel("Vertical Depth (m)")
plt.title("Muon Flux as a Function of Vertical Depth (Standard Rock)")
plt.show()


    