import numpy as np
import matplotlib.pyplot as plt
from butcher_tableau import ButcherTableau
from erk import solve_erk

C_RK4 = np.array([0,0.5,0.5,1])
A_RK4 = np.array([[0,0,0,0],[0.5,0,0,0],[0,0.5,0,0],[0,0,1,0]])
B_RK4 = np.array([1.0/6, 1.0/3, 1.0/3, 1.0/6])
RK4_TABLEAU = ButcherTableau(C_RK4,A_RK4,B_RK4)

if __name__ == '__main__':
    f = lambda t,x: -2*x
    T = np.arange(0, 10, 0.5)
    x0 = np.mat([1])
    x = solve_erk(RK4_TABLEAU, f, T, x0)
    plt.plot(T,x.T)
    plt.show()
