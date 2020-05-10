import sys
import tkinter as tk
from gui.entry_panel import EntryPanel, ButtonPanel
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

        self.afficher_valeur = tk.Button(self.box1, text="Afficher Valeurs", state = tk.DISABLED)
        self.afficher_valeur.pack(side=tk.TOP)

        self.histogramme = ButtonPanel(self.box1, "Histogramme", "Calculer l'Histogramme")

        self.box2 = tk.LabelFrame(self)
        self.box2.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)

        

        self.scrolledFrame = ScrollerFrame(self.box2)
        self.scrolledFrame.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)

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


        self.buttons = [self.brillance, self.contraste, self.gamma, self.lut_sigmoid, self.histogramme, self.negatif, self.seuillage,
                        self.logarithmique, self.puissance, self.egaliser]


