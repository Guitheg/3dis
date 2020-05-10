import numpy as np
from scipy.signal import convolve2d
from utils import apply_img, normalize
from model.masque import H_filtre_laplacien, H_passe_bas_butterworth, H_passe_bas_gaussien, H_passe_bas_ideal
from model.masque import M_SOBEL_1, M_SOBEL_2, M_LAPLACIEN, M_masque_moyenneur

def _idt(x):
    return x    

def _to_freq(image):
    I = np.array(image)
    I = apply_img(I, np.fft.fft2)
    return apply_img(I , np.fft.fftshift)

def _to_time(spectre):
    J = np.array(spectre)
    J = apply_img(J, np.fft.ifftshift) 
    return apply_img(J, np.fft.ifft2)

def _N8(l, c, img):
    return [img[l-1,c-1], img[l-1,c], img[l-1,c+1],
         img[l,c-1], img[l,c], img[l,c+1],
         img[l+1,c-1], img[l+1,c],img[l+1,c+1]]

def _N4(l, c, img):
    return [img[l-1,c], img[l+1,c], img[l,c], img[l,c-1], img[l,c+1]]

def _median(l):
    """
    gray
    """
    l_sort = sorted(l)
    n = len(l_sort)
    return (l_sort[n//2]+l_sort[(n//2)+1])/2 if n % 2 == 0 else l_sort[n//2]

def norm_fft(image):
    return normalize(abs(image), M=255, dtype=np.uint8)

def filtre_conv(image, M, pretrai = _idt, postrai = _idt):
    img = pretrai(np.array(image, dtype=np.uint8))
    norm = np.sum(np.sum(M))
    if norm == 0:
        norm = 1
    if img.ndim == 3:
        r = convolve2d(img[:,:,0], M, boundary='symm', mode='same')//norm
        g = convolve2d(img[:,:,1], M, boundary='symm', mode='same')//norm
        b = convolve2d(img[:,:,2], M, boundary='symm', mode='same')//norm
        res = np.stack([r,g,b], axis=2).astype(int)
    else :
        res = convolve2d(image, M, boundary='symm', mode='same')//norm
    
    return postrai(res)

def appliquer_op_sobel(image, a = 1):
    img = np.array(image, dtype=np.uint8)
    r1 = filtre_conv(img, M_SOBEL_1)
    r2 = filtre_conv(img, M_SOBEL_2)
    return a*img + (r2 + r1)

def appliquer_filtre_moyenneur(image, n=3, pretrai=_idt, postrai=_idt):
    return filtre_conv(image, M_masque_moyenneur(n), pretrai=pretrai, postrai=postrai)

def appliquer_laplacien(image, masque = M_LAPLACIEN):
    img = np.array(image, dtype=np.uint8)
    r = filtre_conv(image, masque)
    return img + (r * (1 if masque[1,1] >= 0 else -1))

def appliquer_filtre_median(image, voisinage=_N4):
    """
    gray
    """
    img = np.array(image)
    r = np.zeros(img.shape)
    for l in range(1, len(img)-1):
        for c in range(1, len(img[0])-1):
            r[l,c] = _median(voisinage(l, c, img))
    return r

def filtre_fft(image, H, pretrai = _idt, postrai = _idt):
    I = np.array(image)
    J = _to_freq(pretrai(I))
    j_h = apply_img(J, lambda x, H : x * H, H)
    return postrai(_to_time(j_h))

def appliquer_PB_ideal(image, D = 1, pretrai = _idt, postrai = _idt):
    I = np.array(image)
    M = len(I)
    N = len(I[0])
    return filtre_fft(I, H_passe_bas_ideal(M, N, D), pretrai=pretrai, postrai=postrai)

def appliquer_PB_butterworth(image, D = 1, n = 1, pretrai = _idt, postrai = _idt):
    I = np.array(image)
    M = len(I)
    N = len(I[0])
    return filtre_fft(I, H_passe_bas_butterworth(M, N, D, n), pretrai=pretrai, postrai=postrai)

def appliquer_PB_gaussien(image, D = 1, pretrai = _idt, postrai = _idt):
    I = np.array(image)
    M = len(I)
    N = len(I[0])
    return filtre_fft(I, H_passe_bas_gaussien(M, N, D), pretrai=pretrai, postrai=postrai)

def appliquer_laplacien_fft(image, pretrai = _idt, postrai = _idt):
    I = np.array(image)
    M = len(I)
    N = len(I[0])
    return filtre_fft(I, H_filtre_laplacien(M, N), pretrai=pretrai, postrai=postrai)

def appliquer_PH_ideal(image, D = 1, pretrai = _idt, postrai = _idt):
    I = np.array(image)
    M = len(I)
    N = len(I[0])
    return filtre_fft(I, 1-H_passe_bas_ideal(M, N, D), pretrai=pretrai, postrai=postrai)

def appliquer_PH_butterworth(image, D = 1, n = 1, pretrai = _idt, postrai = _idt):
    I = np.array(image)
    M = len(I)
    N = len(I[0])
    return filtre_fft(I, 1-H_passe_bas_butterworth(M, N, D, n), pretrai=pretrai, postrai=postrai)

def appliquer_PH_gaussien(image, D = 1, pretrai = _idt, postrai = _idt):
    I = np.array(image)
    M = len(I)
    N = len(I[0])
    return filtre_fft(I, 1-H_passe_bas_gaussien(M, N, D), pretrai=pretrai, postrai=postrai)

