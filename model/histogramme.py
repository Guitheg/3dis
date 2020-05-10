import numpy as np
from model.pt_to_pt import opt
from utils import normalize

def histogramme_valeur(image, m = 255):
    I = np.array(image)
    if I.ndim == 3:
        H = np.zeros((m,))
        for g in range(m):
            h = sum(sum(I==g))
            H[g] = int(1/3*h[0] + 1/3*h[1] + 1/3*h[2])
    else :
        H = np.zeros((m,))
        for g in range(m):
            H[g] = sum(sum(I==g))
    return H

def histogramme_luminance(image, m = 255):
    I = np.array(image)
    if I.ndim == 3:
        H = np.zeros((m,))
        for g in range(m):
            h = sum(sum(I==g))
            H[g] = int(0.299*h[0] + 0.587*h[1] + 0.114*h[2])
    else :
        H = np.zeros((m,))
        for g in range(m):
            H[g] = sum(sum(I==g))
    return H

def ddp(image, m = 255):
    H = histogramme_valeur(image)
    A = sum(H)
    return [(1/A) * H[g] for g in range(m)]

def ddp_cumule(image, m = 255):
    H = histogramme_valeur(image)
    A = sum(H)
    return [sum([(1/A) * H[v] for v in range(g)]) for g in range(m)]

# def histogram_equalization(p, P, mi, Mi, mj, Mj):
#     return (Mj - mj)*((P[p+1]-P[mi+1])/(1-P[mi+1]))+mj

def egalisation(p, P, m = 255):
    P = np.array(P)
    return 255*P[p if p < m else m-1]

def appliquer_egalisation_histogramme(image):
    P = ddp_cumule(image)
    return normalize(opt(image, egalisation, P=P, excluded=["P"]), M=255, dtype=np.uint8)
