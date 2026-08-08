from gaisser_formula import modified_gaisser_formula
import numpy as np
from scipy import integrate
from detector_geometrical_acceptance import calculate_acceptance, sample_directions, sample_entry_points
import matplotlib.pyplot as plt


#-----Detector Variables-----
r = 1.056   # m
h =  0.3# vertical separation (using h to avoid confusion with distance d)

#-----Geometrical Acceptance-----
acceptance_ratio = calculate_acceptance(r, h, 1_000_000)
print(f"Geometric acceptance: {acceptance_ratio:.4f}")

A = np.pi * (r/2)**2
#A = 1.056 * 1.056 #Area in m^2

#To calculate the total flux I need to integrate over all possible energies and solid angle with a detector area projection correction term

def KoNova_rate_estimate(E, theta):
    """
    *10000 is to convert to m^2 ; cos(theta) term is for a float detector ; 2pisin(theta) is solid angle correction
    """
    
    return (10000 * modified_gaisser_formula(E, theta) * A * np.cos(theta) * 2 * np.pi * np.sin(theta))

flux_List = []
E_min_list = np.arange(0, 10, 1)
for E_min in E_min_list:
    I = integrate.nquad(KoNova_rate_estimate, [[E_min, np.inf], [0, np.pi/2]])[0]
    flux_List.append(I*acceptance_ratio)

plt.plot(E_min_list, flux_List)
plt.axhline(y = 65, color = 'r', linestyle = '--', label = 'Observed Flux')
plt.title("Muon Flux on Hodoscope vs Minimum Energy Cutoff")
plt.xlabel("Minimum Energy Cutoff [GeV]")
plt.ylabel("Muon Flux (m^-2 s^-1)")
plt.show()