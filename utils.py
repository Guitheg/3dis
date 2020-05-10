import os
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def is_in(e, l):
    for x in l:
        if e == x:
            return True
    return False

def inp(text, values = None):
    choix = input(str(text)+" ")
    if not (values == None or values == []):
        while not is_in(choix, values):
            choix = input(str(text) + " (Valeurs accepté : " + str(values)+") ")
    return choix

def afficher_image(img, figure, nrows, nrcols, it, title, clear = False):
    fig = plt.figure(figure, figsize=(6,6), clear = clear)
    fig.add_subplot(nrows, nrcols, it)
    plt.imshow(img, aspect='equal')
    plt.gray()
    plt.axis('off')
    plt.title(title)

def plot_fig(data, figure, nrows, ncols, it, title, clear = False):
    fig = plt.figure(figure, figsize=(6,6), clear = clear)
    fig.add_subplot(nrows, ncols, it)
    plt.plot(data)
    plt.title(title)

def apply_img(I, f, *args, **kwargs):
    I = np.array(I)
    if I.ndim == 3:
        r = f(I[:,:,0], *args, **kwargs)
        g = f(I[:,:,1], *args, **kwargs)
        b = f(I[:,:,2], *args, **kwargs)
        # afficher_image(abs(I[:,:,0]), "test",3,2,1,"I[0]")
        # afficher_image(np.log10(abs(r)), "test",3,2,2,"r")
        # afficher_image(abs(I[:,:,1]), "test",3,2,3,"I[1]")
        # afficher_image(np.log10(abs(g)), "test",3,2,4,"g")
        # afficher_image(abs(I[:,:,2]), "test",3,2,5,"I[2]")
        # afficher_image(np.log10(abs(b)), "test",3,2,6,"b")
        # afficher_image(abs(np.stack([I[:,:,0], I[:,:,1], I[:,:,2]], axis = -1)), "resultat",1,2,1,"res")
        # afficher_image(abs(np.stack([r, g, b], axis = -1)).astype(np.uint8), "resultat",1,2,2,"freq")
        # plt.show()
        return np.stack([r, g, b], axis = -1)
    else :
        return f(I, *args, **kwargs)

def normalize(m, M = 1, dtype = np.float):
    return ((m - np.min(m)) / (np.max(m) - np.min(m)) * M).astype(dtype)

def lister_images(path):
    images = []
    if not os.path.isfile(path):
        open(path, "x")       
    else:
        with open(path, "r") as file:
            for line in file.readlines():
                l = line[:-1]
                if os.path.isfile(l):
                    images.append(l)

        with open(path, "w") as file:
            for i in images :
                file.write(i+"\n")
    return images

def afficher_images(images):
    for c,i in enumerate(images):
        print("["+str(c)+"] - "+str(i))


def factoriel(n):
    return n * factoriel(n-1) if n > 0 else 1

def _addition(a, b, m, M):
    r = a+b
    if r < m:
        return m
    elif r > M:
        return M
    else:
        return r

def addition(A, B, m, M):
    A = np.array(A)
    B = np.array(B)
    add = np.vectorize(_addition, excluded=['m','M'])
    return add(A, B, m, M)