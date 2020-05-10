import os
import sys
from PIL import Image

from utils import inp
from utils import lister_images
from utils import afficher_images

from controllers.mainController import MainController
from config import Config

MAIN = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(MAIN, "data")

def main():
    config = Config(DATA)
    controller = MainController(config)
    controller.run()
if __name__ == "__main__":
    main()