import random
import numpy as np
from model.pt_to_pt import pt_to_pt, opt
from utils import factoriel, normalize, addition

def bruit_s_p(image, prob, m = 255):
    I = np.array(image)
    if I.ndim == 3:
        R = pt_to_pt(image, poivre, prob, signature='(c),()->(c)')
        return pt_to_pt(R, sel, prob, signature='(c),()->(c)')
    else :
        R = pt_to_pt(image, poivre, prob)
        return pt_to_pt(R, sel, prob)

def poivre(p, P):
    return p if P <= random.randint(0, 100) else (0 if type(p) == int else [0,0,0])

def sel(p, P, m = 255):
    return p if P <= random.randint(0, 100) else (m if type(p) == int else [m,m,m])

def bruit_gauss(image, u = 0, s = 10, m = 255):
    img = np.array(image, dtype=np.uint8)
    gauss = np.random.normal(u, s, (len(img),len(img[0])))
    if img.ndim == 3:
        return np.stack([addition(img[:,:,0], gauss, 0, m).astype(np.uint8), 
                        addition(img[:,:,1], gauss, 0, m).astype(np.uint8), 
                        addition(img[:,:,2], gauss, 0, m).astype(np.uint8)], axis=2)
    return addition(img, gauss, 0, m).astype(np.uint8)

def bruit_uniform(image, a, b, m=255):
    img = np.array(image, dtype=np.uint8)
    uniform = np.random.uniform(a, b, size=(len(img),len(img[0])))
    if img.ndim == 3:
        return np.stack([addition(img[:,:,0], uniform, 0, m).astype(np.uint8), 
                        addition(img[:,:,1], uniform, 0, m).astype(np.uint8), 
                        addition(img[:,:,2], uniform, 0, m).astype(np.uint8)], axis=2)
    return addition(img, uniform, 0, m).astype(np.uint8)

def bruit_periodique(image, u0=0.1, v0=0.1, A = 2, m = 255):
    img = np.array(image, dtype=np.uint8)
    for u in range(len(img)):
        for v in range(len(img[0])):
            B = np.cos(2*np.pi*(u0*u+v0*v)) * A
            if img.ndim == 3:
                for b in range(len(img[u,v])):
                    if (B + img[u,v,b] < 0):
                        img[u,v,b] = 0
                    elif (B + img[u,v,b]  > m):
                        img[u,v,b]  = m
                    else:
                        img[u,v,b]  += B
            else:
                if (B + img[u,v] < 0):
                    img[u,v] = 0
                elif (B + img[u,v] > m):
                    img[u,v] = m
                else:
                    img[u,v] += B
    return img.astype(np.uint8)

# def uniforme(p, a, b):
#     if 0 <= a and a < b:
#         return (1 / (b-a)) if a <= p and p <= b else 0
#     raise Exception("0 <= a < b  => a:"+str(a)+ ", b:"+str(b))

# def rayleigh(p, a, b):
#     if 0 <= a and a < b:
#         return ((2/b)*(p-a)*np.exp(-((p-a)**2)/b)) if p >= a else 0
#     raise Exception("0 <= a < b  => a:"+str(a)+ ", b:"+str(b))

# def erland(p, a, b):
#     if a <= 0:
#         raise Exception("a should be > 0")
#     return (((a**b)*(p**(b-1))*np.exp(-a*p))/factoriel(b-1)) if p >= 0 else 0

# def exponentiel(p, a):
#     return (a*np.exp(-a*p)) if p >= 0 else 0

    
