#!env python3
import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt("errors.txt")

h = data[:,0]      # h=first column
errL2 = data[:,1]  # errL2 = 2nd column
errH1 = data[:,2]  # errH1 = 3rd column

plt.loglog(h,errL2,"-rs",label="Error L2")
plt.loglog(h,errH1,"-b^",label="Error H1")
plt.legend()
plt.show()
