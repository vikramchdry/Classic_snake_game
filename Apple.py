import random
import pygame
from config import Config
import numpy as np 



class Apple:
	def __init__(self,display):
		self.x_pos = 0
		self.y_pos = 0
		self.display = display
		self.appleDisplay()



	def appleDisplay(self):


		height = Config['game']['height']
		width = Config['game']['width']
		bumper = 30
		max_x = (width  - 30 - Config['snake']['width'])
		max_y = (height  - 30 - Config['snake']['height'])
		self.x_pos = random.randint(30,max_x)
		self.y_pos = random.randint(30,max_y)


		


	def draw(self):
		return pygame.draw.rect(
            self.display, 
            Config['colors']['red'],
            [
                self.x_pos,
                self.y_pos,
                Config['apple']['height'],
                Config['apple']['width']
                ])




