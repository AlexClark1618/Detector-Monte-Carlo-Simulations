import numpy as np
import matplotlib.pyplot as plt

#----Constants-----
'''
def muon_spectrum():

    differential_flux = E**(-2.7)*np.cos(zenith)**2*np.sin(zenith)

#Open sky 
N_open = 1000
lam = 200

def simulate_measurment(integrated_density):
    ideal_count = N_open * np.exp(-(integrated_density/lam))
    
    #add gaussian noise
    N_observed = rand.gauss(ideal_count, np.sqrt(ideal_count))

    return N_observed
'''
"""
For low energy muons the energy spectrum can be approximated as 0.14E^-2.7 cm^-2s^-1sr^-1, valid only from 10GeV above

cos^2(x) angular spectrum

cos(x) from detector area projection 

sin(x) solid angle 
"""


E_min = 1 #GeV
E_max = 100 #GeV

def sample_muon_directions(N_muons):
    directions = []

    while len(directions)<N_muons:

        zenith = np.random.uniform(0, np.pi/2)

        if np.random.uniform(0,1)< (np.cos(zenith)**3)*np.sin(zenith):
            azimuth = np.random.uniform(0, 2*np.pi)
            directions.append((azimuth, zenith))  
        
    return np.array(directions)


directions = sample_muon_directions(10000)

azimuth = directions[:,0] * 180/np.pi
zenith = directions[:,1] * 180/np.pi

plt.hist(azimuth, bins = 36)
plt.show()

plt.hist(zenith, bins = 18)
plt.show()

