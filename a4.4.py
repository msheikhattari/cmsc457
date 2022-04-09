import cmath
import math
import numpy as np
import matplotlib.pyplot as plt

def prob(j):
        r = 6.0
        n = 2.0**7.0
        con = 1/(r*n)
        aj = 0

        for k in range(0,6):
                aj += cmath.exp(complex(0,j*k*(2*math.pi)/(n)))

        c = np.conjugate(aj)

        d = abs((np.real(c)*np.real(aj))) + abs((np.imag(c)*np.imag(aj)))

        return d*con

def sum():

        arr = []
        js = np.arange(0,128,1)
        one = 0

        for j in range(0, 128):
                one+=prob(j)
                arr.append(prob(j))
                

        plt.plot(js,arr)
        plt.xlabel('j')
        plt.ylabel('probability')
        

sum()


