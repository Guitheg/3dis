from PIL import Image
from tkinter import filedialog
import matplotlib.pyplot as plt

from utils import afficher_image, plot_fig, normalize
import tkinter as tk

from model.pt_to_pt import pt_to_pt, gamma, constraste, brillance, lut_sigmoid, opt
from model.pt_to_pt import negatif, seuillage, logarithmique, puissance
from model.histogramme import histogramme_valeur, histogramme_luminance, ddp, ddp_cumule
from model.histogramme import appliquer_egalisation_histogramme
from model import filtre
from model import bruit
from model.filtre import norm_fft


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

		self.view.histogramme.config(command=self.histogramme)
		self.view.spectre.config(command=self.spectre)

		self.view.negatif.button.config(command=self.negatif)
		self.view.seuillage.button.config(command=self.seuillage)
		self.view.logarithmique.button.config(command=self.logarithmique)
		self.view.puissance.button.config(command=self.puissance)
		self.view.egaliser.button.config(command=self.egaliser)

		self.view.sobel.button.config(command=self.sobel)
		self.view.moyenneur.button.config(command=self.moyenneur)
		self.view.laplacien.button.config(command=self.laplacien)
		self.view.pb_ideal.button.config(command=self.pb_ideal)
		self.view.ph_ideal.button.config(command=self.ph_ideal)
		self.view.pb_gauss.button.config(command=self.pb_gauss)
		self.view.ph_gauss.button.config(command=self.ph_gauss)
		self.view.laplacien_fft.button.config(command=self.laplacien_fft)

		self.view.bruit_gauss.button.config(command=self.bruit_gauss)
		self.view.bruit_uniforme.button.config(command=self.bruit_uniforme)
		self.view.bruit_periodique.button.config(command=self.bruit_periodique)
		self.view.bruit_sp.button.config(command=self.bruit_sp)

	def charger_image(self):
		path = filedialog.askopenfilename(parent=self.view,
                                initialdir=self.config.datadir,
                                title="Please select a file:",
                                filetypes=[('all files', '.*'), ('text files', '.txt')])
		img = Image.open(path)


		for bu in self.view.buttons:
			bu.enable()
		self.view.afficher_valeur.config(state=tk.NORMAL)
		self.view.histogramme.config(state=tk.NORMAL)
		self.view.spectre.config(state=tk.NORMAL)

		self.original = img.copy()
		self.old = img.copy()
		self.resultat = img.copy()

		afficher_image(self.original, self.config.figure, 1, 3, 1, title="Original", clear=True)
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
		self.set_resultat(appliquer_egalisation_histogramme(self.resultat))
		self.afficher_resultat("Egalisation")

	def sobel(self):
		a = self.view.sobel.entry.get()
		self.set_resultat(filtre.appliquer_op_sobel(self.resultat, a))
		self.afficher_resultat("Sobel")

	def moyenneur(self):
		a = self.view.moyenneur.entry.get()
		self.set_resultat(
			filtre.appliquer_filtre_moyenneur(self.resultat, a))
		self.afficher_resultat("Moyenneur")

	def laplacien(self):
		self.set_resultat(
			filtre.appliquer_laplacien(self.resultat))
		self.afficher_resultat("Laplacien")

	def pb_ideal(self):
		a = self.view.pb_ideal.entry.get()
		self.set_resultat(
			filtre.appliquer_PB_ideal(self.resultat, D=a, postrai=norm_fft))
		self.afficher_resultat("Passe Bas Ideal")

	def ph_ideal(self):
		a = self.view.ph_ideal.entry.get()
		self.set_resultat(
			filtre.appliquer_PH_ideal(self.resultat, D=a, postrai=norm_fft))
		self.afficher_resultat("Passe Haut Ideal")

	def pb_gauss(self):
		a = self.view.pb_gauss.entry.get()
		self.set_resultat(
			filtre.appliquer_PB_gaussien(self.resultat, D=a, postrai=norm_fft))
		self.afficher_resultat("Passe Bas Gaussien")

	def ph_gauss(self):
		a = self.view.ph_gauss.entry.get()
		self.set_resultat(
			filtre.appliquer_PH_gaussien(self.resultat, D=a, postrai=norm_fft))
		self.afficher_resultat("Passe Haut Gauss")

	def laplacien_fft(self):
		self.set_resultat(
			filtre.appliquer_laplacien_fft(self.resultat, postrai=norm_fft))
		self.afficher_resultat("Laplacien FFT")

	def bruit_gauss(self):
		a = self.view.bruit_gauss.entry1.get()
		b = self.view.bruit_gauss.entry2.get()
		self.set_resultat(
			bruit.bruit_gauss(self.resultat, u=a, s=b))
		self.afficher_resultat("Bruit Gauss")

	def bruit_uniforme(self):
		a = self.view.bruit_uniforme.entry1.get()
		b = self.view.bruit_uniforme.entry2.get()
		self.set_resultat(
		bruit.bruit_uniform(self.resultat, a=a, b=b))
		self.afficher_resultat("Bruit Gauss")

	def bruit_periodique(self):
		a = self.view.bruit_periodique.entry1.get()
		b = self.view.bruit_periodique.entry2.get()
		c = self.view.bruit_periodique.entry3.get()
		self.set_resultat(
			bruit.bruit_periodique(self.resultat, u0 = a, v0 = b, A = c))
		self.afficher_resultat("Bruit Gauss")

	def bruit_sp(self):
		a = self.view.bruit_sp.entry.get()
		self.set_resultat(
			bruit.bruit_s_p(self.resultat, prob=a))
		self.afficher_resultat("Bruit Gauss")

	def spectre(self):
		spectre = filtre._to_freq(self.resultat)
		afficher_image(normalize(np.log10(abs(spectre))), "Spectre", 1, 1, 1, "Spectre")
		plt.show()

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
		afficher_image(self.old, self.config.figure, 1, 3, 2, title="Résultat précédent")
		afficher_image(self.resultat, self.config.figure, 1, 3, 3, title="Résultat "+str(name))	
		plt.show()

	def reinitialiser(self):
		self.old = self.original.copy()
		self.resultat = self.original.copy()
		afficher_image(self.original, self.config.figure, 1, 3, 1, title="Original", clear=True)
		plt.show()

	def annuler(self):
		self.resultat = self.old.copy()
		afficher_image(self.resultat, self.config.figure, 1, 3, 3, title="Résultat précédent")
		plt.show()	

	def set_resultat(self, resultat):
		self.old = self.resultat.copy()
		self.resultat = resultat.copy()
		
		




