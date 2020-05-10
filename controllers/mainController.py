
from controllers.homeController import HomeController
from gui.mainView import MainView


class MainController():

	def __init__(self, config):
		self.window = MainView(config)
		self.config = config

		self.home_controller = HomeController(self, self.window.home_view, config)
		
		

	def run(self):
		self.window.title(self.config.name)
		self.window.mainloop()