import numpy as np
import matplotlib.pyplot as plt

#----Constants-----
'''
def sample_muon_directions(N_muons):
    directions = []

    while len(directions)<N_muons:

        zenith = np.random.uniform(0, np.pi/2)

        if np.random.uniform(0,1)< (np.cos(zenith)**3)*np.sin(zenith):
            azimuth = np.random.uniform(0, 2*np.pi)
            directions.append((azimuth, zenith))  
        
    return np.array(directions)
'''

def sample_directions(N):
    """
    Sample zenith from cos^3(theta)*sin(theta) distribution.
    cos^2 from muon flux, cos from Lambert projection on D1.

    Inverse transform: CDF(cos theta) = cos^4(theta)
    Invert: cos(theta) = u^(1/4), u ~ Uniform(0,1)
    """
    u = np.random.uniform(0, 1, N)
    zenith = np.arccos(u ** (1/4))                
    azimuth = np.random.uniform(0, 2 * np.pi, N)
    return azimuth, zenith

N = 100000000
directions = sample_directions(N)


azimuth = directions[0] * 180/np.pi
zenith = directions[1] * 180/np.pi

zenith_bins = np.histogram(zenith, bins = 'fd')
max_zenith_bin = np.where(zenith_bins[0] == zenith_bins[0].max())[0][0]
max_zenith_angle = zenith_bins[1][max_zenith_bin]

x = np.linspace(0, 90, 1000)
A * (np.cos(x) ** 3) * np.sin(x)

plt.hist(azimuth, bins = 'fd')
plt.title(f"Azimuth Distribution of {N} Sampled Muons")
plt.xlabel("Degrees")
plt.ylabel("Frequency")
plt.show()

plt.hist(zenith, bins = 'fd')
plt.title(f"Zenith Distribution of {N} Sampled Muons | Max = {(max_zenith_angle):.2f} degrees")
plt.xlabel("Degrees")
plt.ylabel("Frequency")
plt.show()



