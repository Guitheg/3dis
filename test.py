import os
import sys
from model.filtrage import N4, N8, filtre, masque_moyenneur, LAPLACIEN, laplacien, filtre_median, op_sobel
from model.pt_to_pt import opt 
from model.histogramme import histogramme_luminance, histogramme_valeur, egalisation, ddp, ddp_cumule
from model.bruit import bruit_s_p, bruit_gauss, bruit, exponentiel, poivre, sel, rayleigh, uniforme, bruit_periodique, bruit_uniform
from model.op_freq import filtre_freq, to_freq, to_time, passe_bas_ideal, passe_bas_butterworth, passe_bas_gaussien, filtre_laplacien, filtre_pum

from utils import afficher_image, plot_fig, normalize

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


MAIN = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(MAIN, "data")

IMAGE = {
    '0' : os.path.join(DATA, "porte.bmp"),
    '1' : os.path.join(DATA, "lena.jpg"),
    '2' : os.path.join(DATA, "coat_of_arms.png")
}


def test(p):
    return p



def main():

    # l = [1,5,3,2,11,7,8,4]


    image = np.array(Image.open(IMAGE[sys.argv[1]]))
    I = np.array(image)
    M = len(I)
    N = len(I[0])

    # P = ddp_cumule(image)
    # J = normalize(opt(image, egalisation, P=P, excluded=["P"]), 255, dtype=np.uint8)

    # afficher_image(image, "Figure", 1, 2, 1, "Original")
    # afficher_image(J, "Figure", 1, 2, 2, "Resultat")
    # plot_fig(P, "Info", 1, 2, 1, "Plot")
    # plot_fig(ddp_cumule(J), "Info", 1, 2, 2, "Resultat")
    # plt.show()




    # # img = filtre_median(image, N8)
    # bruite = bruit_s_p(image, prob=0.05)
    # bruite = bruit_gauss(bruite, s=10)
    # # print(LAPLACIEN)
    # # print(masque_moyenneur(3))
    # img = filtre(bruite, masque_moyenneur(5))
    # med = filtre(img, masque_moyenneur(5))
    # r = laplacien(med, LAPLACIEN)
    # sobel = op_sobel(r)

    
    # afficher_image(image, "Figure", 2, 3, 1, "Original")
    # afficher_image(bruite, "Figure", 2, 3, 2, "Bruité")
    # afficher_image(img, "Figure", 2, 3, 3, "Moyenne")
    # afficher_image(med, "Figure", 2, 3, 4, "Median")
    # afficher_image(r, "Figure", 2, 3, 5, "Réhaussé")
    # afficher_image(sobel, "Figure", 2, 3, 6, "Réhaussé")
    # plt.show()





    # afficher_image(image, "Figure", 1, 3, 1, "Original")
    # # H = 1-passe_bas_gaussien(len(image), len(image[0]), 10)
    # H = filtre_pum(passe_bas_butterworth, 0.5, 2, M, N, 20)
    # afficher_image(H, "Figure", 1, 3, 2, "Filtre")
    # rehausse, spectre, j_h = filtre_freq(image, H)
    # # afficher_image(normalize(np.log10(abs(spectre)), 255, np.uint8), "Figure", 1, 4, 3, "Spectre")
    # afficher_image(normalize(abs(rehausse), 255, np.uint8), "Figure", 1, 3, 3, "Resultat")
    # plt.show()


    i_sp = bruit(bruit(I, poivre, 0.05), sel, 0.05)
    i_gauss = bruit_gauss(image, u=0, s=50)
    i_uniforme = bruit_uniform(image, 2, 80)
    i_rayleigh = normalize(bruit(I, rayleigh, a=1, b=10000))
    i_exp = normalize(bruit(I, exponentiel, a=0.01))
    i_periodique = bruit_periodique(image, 0.2, 0.2, A=30)

    afficher_image(image, "Bruit", 2, 3, 1, "Original")
    afficher_image(i_periodique, "Bruit", 2, 3, 2, "Periodique")
    afficher_image(i_gauss, "Bruit", 2, 3, 3, "Gauss")
    afficher_image(i_uniforme, "Bruit", 2, 3, 4, "Uniforme")
    afficher_image(i_sp, "Bruit", 2, 3, 5, "Rayleigh")
    afficher_image(i_exp, "Bruit", 2, 3, 6, "Erland")

    # afficher_image(i_exp, "Bruit2", 2, 3, 1, "Original")
    # afficher_image(image, "Bruit2", 2, 3, 2, "Exponentiel")
    # afficher_image(image, "Bruit2", 2, 3, 3, "PS+Gauss+Uniforme")
    # afficher_image(image, "Bruit2", 2, 3, 4, "")
    # afficher_image(image, "Bruit2", 2, 3, 5, "")
    # afficher_image(image, "Bruit2", 2, 3, 6, "")

    plt.show()


if __name__ == "__main__":
    main()