from PIL import Image
from tkinter import filedialog
import matplotlib.pyplot as plt

from utils import afficher_image, plot_fig
import tkinter as tk

from model.pt_to_pt import pt_to_pt, gamma, constraste, brillance, lut_sigmoid, opt
from model.pt_to_pt import negatif, seuillage, logarithmique, puissance
from model.histogramme import histogramme_valeur, histogramme_luminance, ddp, ddp_cumule, egaliser_histogramme

import numpy as np
class HomeController():
	def __init__ (self, master, home_view, config):
		self.master = master
		self.config = config
		self.view = home_view

		self.view.btn_charger_image.config(command=self.charger_image)
		self.view.reinitialiser.config(command=self.reinitialiser)
		self.view.afficher_valeur.config(command=self.afficher_valeurs)
		self.view.annuler.config(command=self.annuler)

		self.view.brillance.button.config(command=self.brillance)
		self.view.contraste.button.config(command=self.contraste)
		self.view.gamma.button.config(command=self.gamma)
		self.view.lut_sigmoid.button.config(command=self.lut_sigmoid)
		self.view.histogramme.button.config(command=self.histogramme)

		self.view.negatif.button.config(command=self.negatif)
		self.view.seuillage.button.config(command=self.seuillage)
		self.view.logarithmique.button.config(command=self.logarithmique)
		self.view.puissance.button.config(command=self.puissance)
		self.view.egaliser.button.config(command=self.egaliser)


	def charger_image(self):
		path = filedialog.askopenfilename(parent=self.view,
                                initialdir=self.config.datadir,
                                title="Please select a file:",
                                filetypes=[('all files', '.*'), ('text files', '.txt')])
		img = Image.open(path)


		for bu in self.view.buttons:
			bu.enable()
		self.view.afficher_valeur.config(state=tk.NORMAL)

		self.original = img.copy()
		self.old = img.copy()
		self.resultat = img.copy()

		afficher_image(self.original, self.config.figure, 2, 2, 1, title="Original", clear=True)
		plt.show()

	def afficher_valeurs(self):
		print(np.array(self.resultat))

	def brillance(self):
		g = self.view.brillance.entry.get()
		self.set_resultat(pt_to_pt(self.resultat, brillance, g))
		self.afficher_resultat("Brillance")

	def contraste(self):
		g = self.view.contraste.entry.get()
		self.set_resultat(pt_to_pt(self.resultat, constraste, g))
		self.afficher_resultat("Contraste")

	def gamma(self):
		g = self.view.gamma.entry.get()
		self.set_resultat(pt_to_pt(self.resultat, gamma, g))
		self.afficher_resultat("Gamma")

	def lut_sigmoid(self):
		self.set_resultat(pt_to_pt(self.resultat, lut_sigmoid))
		self.afficher_resultat("LUT Sigmoid")

	def negatif(self):
		self.set_resultat(pt_to_pt(self.resultat, negatif))
		self.afficher_resultat("Negatif")

	def logarithmique(self):
		g = self.view.logarithmique.entry.get()
		self.set_resultat(pt_to_pt(self.resultat, logarithmique, g))
		self.afficher_resultat("Logarithmique")

	def seuillage(self):
		g = self.view.seuillage.entry.get()
		self.set_resultat(pt_to_pt(self.resultat, seuillage, g))
		self.afficher_resultat("Seuillage")

	def puissance(self):
		g = self.view.puissance.entry.get()
		self.set_resultat(pt_to_pt(self.resultat, puissance, g))
		self.afficher_resultat("Puissance")

	def egaliser(self):
		self.set_resultat(egaliser_histogramme(self.resultat))
		self.afficher_resultat("Egalisation")


	def histogramme(self):
		histo = histogramme_valeur(self.resultat)
		histo_lum = histogramme_luminance(self.resultat)
		ddp_ = ddp(self.resultat)
		res_ddp = ddp_cumule(self.resultat)
		# print(pt_to_pt(self.resultat, histogram_equalization, res_ddp, 0, 255, 0, 255))
		plot_fig(histo, self.config.figure_param, 2, 2, 1, title="Histogramme de Valeur", clear=True)
		plot_fig(histo_lum, self.config.figure_param, 2, 2, 2, title="Histogramme de Luminance")
		plot_fig(ddp_, self.config.figure_param, 2, 2, 3, title="PDF")
		plot_fig(res_ddp, self.config.figure_param, 2, 2, 4, title="CDF")
		plt.show()

	def afficher_resultat(self, name):
		afficher_image(self.old, self.config.figure, 2, 2, 3, title="Résultat précédent")
		afficher_image(self.resultat, self.config.figure, 2, 2, 4, title="Résultat "+str(name))	
		plt.show()

	def reinitialiser(self):
		self.old = self.original.copy()
		self.resultat = self.original.copy()
		afficher_image(self.original, self.config.figure, 2, 2, 1, title="Original", clear=True)
		plt.show()

	def annuler(self):
		self.resultat = self.old.copy()
		afficher_image(self.resultat, self.config.figure, 2, 2, 4, title="Résultat précédent")
		plt.show()	

	def set_resultat(self, resultat):
		self.old = self.resultat.copy()
		self.resultat = resultat.copy()
		
		




