import os
from tkinter import ttk
import tkinter as tk 

from gui.homeView import HomeView

class MainView(tk.Tk):

	def __init__(self, config):
		tk.Tk.__init__(self, None)
		self.config = config
		self.windowSizeX = self.config.X
		self.windowSizeY = self.config.Y
		p = self.config.p

		self.note = ttk.Notebook(self, 
								height=int(self.windowSizeY-p*self.windowSizeY), 
								width=int(self.windowSizeX-p*self.windowSizeX))
		self.note.pack()

		self.home_view = HomeView(self.note, config)
		self.note.add(self.home_view, text=self.config.home)
