import numpy as np

def opt(image, function, *args, **kwargs):
    img = np.array(image, dtype=np.uint8)

    if img.ndim == 3:
        return pix_to_pix(image, function, *args, **kwargs)
    elif img.ndim <= 2 :
        return pt_to_pt(image, function, *args, **kwargs)
    else :
        Exception ("Dimension trop grande")

def pix_to_pix(image, function, *args, **kwargs):
    img = np.array(image, dtype=np.uint8)
    
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]

    R = pt_to_pt(r, function, *args, **kwargs)
    G = pt_to_pt(g, function, *args, **kwargs)
    B = pt_to_pt(b, function, *args, **kwargs)

    return np.stack([R,G,B], axis=2)

def pt_to_pt(image, function, *args, **kwargs):
    img = np.array(image, dtype=np.uint8)

    excluded = kwargs.get('excluded', None)
    if excluded:
        del kwargs['excluded']

    signature = kwargs.get('signature', None)
    if signature:
        del kwargs['signature']

    f = np.vectorize(function, excluded=excluded, signature=signature)
    return f(img, *args, **kwargs)

def brillance(p, g, m = 255):
    """
    p < 0 : diminution de la brillance
    p > 0 : augmentation de la brillance
    """
    if (p + g < m + 1) and (p + g > 0):
        return int(p + g)
    elif p + g <= 0:
        return 0
    else:
        return m

def constraste(p, a, m = 255):
    """
    a compris entre 0 et 1 => diminution du contraste
    a > 1 augmentation du contraste
    """
    if a < 0 :
        raise Exception("'a' has to be >= 0")
    T = a * (p - (m // 2)) + (m // 2)
    if T <= 0:
        return 0
    elif 0 < T and T < m:
        return int(T)
    else:
        return m

def gamma(p, g, m = 255):
    """
    g < 1 : diminution du gamma
    g > 1 : augmentation du gamma
    """
    return int(m * np.power((p/m),1/g))

def lut_sigmoid(p, a = 2, m = 255):
    return int(m / 1 + np.exp(-a*(p-m//2)/32))

def negatif(p, m = 255):
    return int(m - p)

def seuillage(p, s, m = 255):
    return int(m) if p > s else 0

def logarithmique(p, c = 1, m = 255):
    return int(c*np.log(1+p))

def puissance(p, g, c = 1):
    """
    g compris entre 0.001 et 30
    """
    return int(c*np.power(p, g))

