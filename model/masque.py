import numpy as np

M_LAPLACIEN_S = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
M_LAPLACIEN = np.array([[0,1,0],[1,-4,1],[0,1,0]])
M_LAPLACIEN_DIAG = np.array([[1,1,1],[1,-8,1],[1,1,1]])
M_LAPLACIEN_OPP = -M_LAPLACIEN
M_LAPLACIEN_DIAG_OPP = -M_LAPLACIEN_DIAG
M_SOBEL_1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
M_SOBEL_2 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

def D(u, v, M, N):
    return np.sqrt( np.power(u - (M/2), 2) + np.power(v - (N/2), 2) )

def M_masque_moyenneur(n):
    return np.ones((n,n))/9

def H_passe_bas_ideal(M, N, D0 = 1):
    H = np.zeros((M,N))
    for u in range(M):
        for v in range(N):
            H[u,v] = 1 if D(u, v, M, N) <= D0 else 0
    return H

def H_passe_bas_butterworth(M, N, D0 = 1, n = 1):
    H = np.zeros((M,N))
    for u in range(M):
        for v in range(N):
            H[u,v] = 1 / (1 + np.power(D(u, v, M, N) / D0, 2*n))
    return H

def H_passe_bas_gaussien(M, N, D0 = 1):
    H = np.zeros((M,N))
    for u in range(M):
        for v in range(N):
            H[u,v] = np.exp(-(D(u, v, M, N)**2) / (2 * (D0**2)))
    return H

def H_filtre_laplacien(M, N):
    H = np.zeros((M,N))
    for u in range(M):
        for v in range(N):
            H[u,v] = -((u - (M/2))**2 + (v - (N/2))**2)
    return H

def get_filtre_rehaussement(H, a, b, M, N, *args, **kwargs):
    if a < 0:
        raise Exception ("a compris généralement entre 0.25 et 0.5")
    if b < a:
        raise Exception(" b has to be greater than a")
    if a < 0.25 or a > 0.5:
        print("Attention ! a est compris généralement entre 0.25 et 0.5")
    if b < 1.5 or b > 2 :
        print("Attention ! b est compris généralement entre 1.5 et 2")
    return a + (b * (1-H(M, N,*args, **kwargs))) # 1 - H car mes H sont des passe bas