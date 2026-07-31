import numpy as np
import matplotlib.pyplot as plt

def read_pdg_data(file):
    with open(file, 'r') as f:
        #      T         p     Ionization  brems     pair     photonuc  Radloss    dE/dx   CSDA Range  delta   beta   dE/dx_R

        collated_data = []

        for _ in range(10):
            next(f)

        for line in f:
            line = line.strip().split()

            #Convert to floats, skipping any non-numeric tokens (e.g. "Minimum ionization")
            temp_list = []
            for element in line:
                try:
                    temp_list.append(float(element))
                except ValueError:
                    continue

            #Only keep complete rows (the 2 annotated rows are short and would make the array ragged)
            if len(temp_list) == 12:
                collated_data.append(temp_list)

    return np.array(collated_data)

def plotter(collated_data):
    kinetic_energy = collated_data[:,0]
    momentum = collated_data[:,1]
    ionization_loss = collated_data[:,2]
    brems_loss = collated_data[:,3]
    pair_loss = collated_data[:,4]
    photonuc_loss = collated_data[:,5]
    radloss = collated_data[:,6]
    stopping_power = collated_data[:,7] #Total energy loss
    CSDA_range = collated_data[:,8] #Range in material
    delta = collated_data[:,9] #Density correction
    beta = collated_data[:,10] #v/c
    restricted_stopping_power = collated_data[:,11]


    '''
    plt.plot(kinetic_energy, stopping_power, label = 'Stopping Power')
    plt.plot(kinetic_energy, CSDA_range, label = 'CSDA Range')

    plt.axvline(x=296.9, ls = '--', c = 'red', label = "Minimum Ionization")
    plt.axvline(x=69270, ls = '--', c = 'red', label = 'Muon Critical Energy')
    plt.xlabel('Kinetic Energy (MeV)')
    plt.ylabel('Stopping Power (MeV cm^2/g)')
    plt.title("Muon Stopping Power in Standard Rock as a Function of Energy")
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()
    '''

    plt.plot(kinetic_energy, ionization_loss, label = 'Ionization Loss')
    plt.plot(kinetic_energy, radloss, label = 'Radiation Loss')
    plt.plot(kinetic_energy, stopping_power, label= 'Total Stopping Power')

    plt.xlabel('Kinetic Energy (MeV)')
    plt.ylabel('Energy Loss (MeV cm^2/g)')
    plt.title("Muon Energy Loss By Mechanism")
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()


    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Kinetic Energy (MeV)')
    ax1.set_xscale('log')
    ax1.set_ylabel('Stopping Power (MeV cm^2/g)', color=color)
    ax1.set_yscale('log')
    ax1.plot(kinetic_energy, stopping_power, color=color)

    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis

    color = 'tab:green'
    ax2.set_ylabel('CSDA Range (g/cm^2)', color=color)  # we already handled the x-label with ax1
    ax2.plot(kinetic_energy, CSDA_range, color=color)
    ax2.set_yscale('log')

    ax2.tick_params(axis='y', labelcolor=color)
    ax2.axvline(x=296.9, ls = '--', c = 'red', label = "Minimum Ionization")
    ax2.axvline(x=69270, ls = '--', c = 'red', label = 'Muon Critical Energy')
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.legend()
    plt.show()

if __name__ == "__main__":

    file = 'C:\\Users\\alexc\\Desktop\\Imaging Practice\\muon_stopping_power_in_rock.txt'
    collated_data = read_pdg_data(file)

    plotter(collated_data)
