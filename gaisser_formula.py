import numpy as np
import scipy.integrate as int
import scipy.special as special
import matplotlib.pyplot as plt
"""
This code is meant to model and numerically calculate the traditional Gaisser Formula for the muon flux spectrum as a function of energy 
(valid from ~100GeV and above) as well as a modified formula that correctly handles lower energy muons. 
"""

def gaisser_formula(E, theta):

    """
    dF/dE = [cm^-2*s^-1*sr^-1]
    """

    return 0.14 * E**-2.7 * ( (1/(1+((1.1*E*np.cos(theta))/115))) + (0.054/(1+((1.1*E*np.cos(theta))/850))) )

def modified_gaisser_formula(E, theta):
    
    p_1 = 0.102573 ; p_2 = 0.068287 ; p_3 = 0.958633; p_4 = 0.0407253 ; p_5 = 0.817285

    cos_star = np.sqrt((np.cos(theta)**2 + p_1**2 + (p_2 * np.cos(theta)**p_3) + (p_4 * np.cos(theta)**p_5)) / (1 + p_1**2 + p_2 + p_4))

    E_star = E * (1 + (3.64/(E*cos_star**1.29)))

    return 0.14 * E_star**-2.7 * ( (1/(1+((1.1*E*cos_star)/115))) + (0.054/(1+((1.1*E*cos_star)/850))) )


if __name__ == "__main__":
    zenith_points = np.linspace(0, np.pi/2, 90)
    int_list = []
    cosine_list = []
    for theta in zenith_points:
        theta = theta
        I_mod = 10000 * int.quad(modified_gaisser_formula, .5, np.inf, args=(theta))[0]
        I_org = 10000 * int.quad(gaisser_formula, 100, np.inf, args=(theta))[0]

        int_list.append([I_mod, I_org])
        cosine_list.append(int_list[0][0]*np.cos(theta)**2)
    int_list = np.array(int_list)
    plt.plot(zenith_points*180/np.pi, int_list[:,0], label = 'Modified Gaisser')
    plt.scatter(zenith_points*180/np.pi, cosine_list, c = 'red', label = 'cos^2(x)')

    #plt.plot(zenith_points*180/np.pi, int_list[:,1])
    plt.xlabel("Zenith (Degrees)")
    plt.ylabel("Muon Flux (m^-2 s^-1 sr^-1)")
    plt.title("Estimation of Muon Flux at Surfave Using Modified Gaisser Model")
    plt.legend()
    plt.show()