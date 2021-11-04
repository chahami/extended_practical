# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



a = [30,35,40] #array of desired indices of age column, can take values from 1 to 51

#corresponds to ages between 1Myr and 100Gyr

z = ['020'] #array of metallicity values in the format 040 = 0.040 and em5 = 1.0 x10 ^-5

fig, ax = plt.subplots() #create new plot

#iterate over z
for i in z:
    
    #read data for that z
    
    data = pd.read_csv('C:\\Users\\Charlie\\Documents\\Uni\\Part_B\\extended_practical\\spectra\\binary\\imf135_100\\spectra-bin-imf135_100.z' + i + '.dat.gz',  delimiter='   ', compression = 'gzip', engine ='python', header = None)

    #iterate over age
    for j in a:
        
        #get data for age, normalise by dividing by 1x10^6 M_Sun
        spec = data.iloc[:,j] / 1e6


        age = 10**(0.1*(j-1)) #age in Myr
    
        ax.plot(spec, linewidth = 0.3, label = "Z = " + i + ", T = %.0f Myr" % age)
    
        #Calculate total luminosity by integrating over wavelength 
        total_lum = np.sum(spec)
        print("Z = " + i + ", Age = %.0f Myr, " % age + "L = %.3f " % total_lum + "L_{☉} M_{☉}^{-1}" )


ax.set_xlabel("λ/Å")
ax.set_xlim(0,10000)
ax.set_ylabel("Flux / $ L_{☉} Å^{-1} M_{☉}^{-1} $ ")
ax.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) #set to scientific notation on y axis

# make the line width larger in legend so colour is visible
leg = ax.legend(fontsize=11, loc = 'upper left')

for line in leg.get_lines():
    line.set_linewidth(6.0)


