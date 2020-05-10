import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Config:
    def __init__(self, datadir):
        self.X = 400
        self.Y = 800
        self.p = 0.1
        self.name = "Viso"
        self.home = "Traitement d'image"
        self.datadir = datadir
        self.figure = "Affichage"
        self.figure_param = "Informations"
        self.resultat = "Resultat"