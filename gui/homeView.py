import sys
import tkinter as tk
from gui.entry_panel import EntryPanel, ButtonPanel, TwoEntryPanel, ThreeEntryPanel
from gui.scrollerFrame import ScrollerFrame

class HomeView(tk.Frame):

    def __init__(self, master, config):
        if sys.version_info < (3,):
            tk.Frame.__init__(self, master)
        else:
            super(HomeView, self).__init__(master)

        self.pack()
        self.config = config

        self.box1 = tk.LabelFrame(self)
        self.box1.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
        
        self.btn_charger_image = tk.Button(self.box1, text="Charger une image")
        self.btn_charger_image.pack(side=tk.TOP)

        self.reinitialiser = tk.Button(self.box1, text="Réinitialiser")
        self.reinitialiser.pack(side=tk.TOP)

        self.annuler = tk.Button(self.box1, text="Annuler derniere opération")
        self.annuler.pack(side=tk.TOP)

        self.info = tk.LabelFrame(self.box1, text="Informations")
        self.info.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
        self.afficher_valeur = tk.Button(self.info, text="Afficher Valeurs", state = tk.DISABLED)
        self.afficher_valeur.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.histogramme = tk.Button(self.info, text="Afficher Histogramme", state=tk.DISABLED)
        self.histogramme.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.spectre = tk.Button(self.info, text="Afficher Spectre", state=tk.DISABLED)
        self.spectre.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)

        self.box2 = tk.LabelFrame(self)
        self.box2.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)  

        self.scrolledFrame = ScrollerFrame(self.box2)
        self.scrolledFrame.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)

        self.bruit_gauss = TwoEntryPanel(self.scrolledFrame.interior, "Bruit Gaussien", "Appliquer", from_=1, to=250, resolution=1)
        self.bruit_uniforme = TwoEntryPanel(self.scrolledFrame.interior, "Bruit Uniforme", "Appliquer", from_=1, to=250, resolution=1)
        self.bruit_periodique = ThreeEntryPanel(self.scrolledFrame.interior, "Bruit Periodique", "Appliquer", from_=0, to=2, resolution=0.01)
        self.bruit_sp = EntryPanel(self.scrolledFrame.interior, "Bruit Sel et Poivre", "Appliquer", from_=0, to=1, resolution=0.01)

        self.brillance = EntryPanel(self.scrolledFrame.interior, "Brillance", "Changer la brillance", from_=-200, to=200, resolution=0.1)
        self.contraste = EntryPanel(self.scrolledFrame.interior, "Constraste", "Changer le contraste", from_=0, to=10, resolution=0.01)
        self.gamma = EntryPanel(self.scrolledFrame.interior, "Gamma", "Changer le Gamma", from_=0.01, to=2, resolution=0.01)
        self.gamma.entry.set(1)
        self.negatif = ButtonPanel(self.scrolledFrame.interior, "Negatif", "Appliquer l'effet Negatif")
        self.seuillage = EntryPanel(self.scrolledFrame.interior, "Seuillage", "Appliquer Seuillage", from_=0, to=250, resolution=1)
        self.logarithmique = EntryPanel(self.scrolledFrame.interior, "Logarithmique", "Appliquer", from_=0, to=10, resolution=0.1)
        self.logarithmique.entry.set(1)
        self.puissance =EntryPanel(self.scrolledFrame.interior, "Puissance", "Appliquer Puissance", from_=0, to=30, resolution=0.01)
        self.puissance.entry.set(1)

        self.lut_sigmoid = ButtonPanel(self.scrolledFrame.interior, "Sigmoid", "Appliquer la Lut")
        
        self.egaliser = ButtonPanel(self.scrolledFrame.interior, "Egalisation Histogramme", "Appliquer l'Egalisation")
        self.sobel = EntryPanel(self.scrolledFrame.interior, "Opérateur de Sobel", "Appliquer SOBEL", from_=1, to=30, resolution=0.01)
        self.moyenneur = EntryPanel(self.scrolledFrame.interior, "Filtre Moyenneur", "Appliquer Moyenneur", from_=1, to=15, resolution=1)
        self.laplacien = ButtonPanel(self.scrolledFrame.interior, "Filtre Laplacien", "Appliquer Laplacien")
        self.pb_ideal = EntryPanel(self.scrolledFrame.interior, "FFT Passe Bas Ideal", "Appliquer PB Ideal", from_=1, to=250, resolution=1)
        self.ph_ideal = EntryPanel(self.scrolledFrame.interior, "FFT Passe Haut Ideal", "Appliquer PH Ideal", from_=1, to=250, resolution=1)
        self.pb_gauss = EntryPanel(self.scrolledFrame.interior, "FFT Passe Bas Gauss", "Appliquer PB Gauss", from_=1, to=250, resolution=1)
        self.ph_gauss = EntryPanel(self.scrolledFrame.interior, "FFT Passe Haut Gauss", "Appliquer PH Gauss", from_=1, to=250, resolution=1)
        self.laplacien_fft = ButtonPanel(self.scrolledFrame.interior, "Laplacien FFT", "Appliquer PB Ideal")

        self.buttons = [self.brillance, self.contraste, self.gamma, self.lut_sigmoid, self.negatif, self.seuillage,
                        self.logarithmique, self.puissance, self.egaliser, self.sobel, self.moyenneur, self.laplacien, self.pb_ideal,
                        self.ph_ideal, self.pb_gauss, self.ph_gauss, self.laplacien_fft, self.bruit_gauss, self.bruit_uniforme, self.bruit_periodique,
                        self.bruit_sp]


