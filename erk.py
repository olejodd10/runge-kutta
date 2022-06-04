import numpy as np

def solve_erk(tableau, f, T, x0):
    nx = len(x0)
    nt = len(T)
    K = np.zeros((nx,tableau.s))
    tk = T[0]
    x = np.zeros((nx,nt))
    x[:,0] = x0
    xk = x0
    for k in range(1,nt):
        dt = T[k]-tk
        tk = T[k]
        K[:,0] = f(tk,xk)
        for stage in range(1,tableau.s):
            a = tableau.A[stage, :stage]
            K[:,stage] = f(tk+dt*tableau.c[stage],xk+dt*K[:,:stage]@a)
        xk = xk + dt*K@tableau.b
        x[:,k] = xk
    return x

