from gaisser_formula import modified_gaisser_formula
import numpy as np
from scipy import integrate

#-----Detector Variables-----

#Hodoscope:

A = 1.056 * 1.056 #Area in m^2
theta_max = np.arctan(105.6/30) #Max Angular acceptance
#To calculate the total flux I need to integrate over all possible energies and solid angle with a detector area projection correction term

def KoNova_rate_estimate(E, theta):
    """
    *10000 is to convert to m^2 ; cos(theta) term is for a float detector ; 2pisin(theta) is solid angle correction
    """
    
    return (10000 * modified_gaisser_formula(E, theta) * A * np.cos(theta) * 2 * np.pi * np.sin(theta))

I = integrate.nquad(KoNova_rate_estimate, [[0.01, np.inf], [0, theta_max]])

print(I)