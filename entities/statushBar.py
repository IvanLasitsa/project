import pygame
from render import Render


class StatusBar:
	def __init__(self, x, y, hp, name, max_hp):
		self.x = x
		self.y = y
		self.hp = hp
		self.name = name
		self.max_hp = max_hp

	def draw(self, hp, screen):
		self.hp = hp
		ratio = self.hp / self.max_hp
		Render.draw_text(screen, self.name, 'white', self.x+35, self.y-25)
		pygame.draw.rect(screen, "red", (self.x, self.y, 150, 25))
		pygame.draw.rect(screen, "green", (self.x, self.y, 150 * ratio, 25))
		Render.draw_text(screen, f'{self.hp}/{self.max_hp}', "white", self.x + 35, self.y)
