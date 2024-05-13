from glob import glob
import random
import pygame

from config import debugMode
from render import Render
from .statushBar import StatusBar


def import_animation(path):
	temp_list = []
	for file_path in sorted(glob(f'{path}/*.png')):
		img = pygame.image.load(file_path)
		img = pygame.transform.scale(img,
		                             (img.get_width() * 6, img.get_height() * 6))
		temp_list.append(img)
	return temp_list


class Enemy:
	def __init__(self, x, y, name, maxHp, damage, image_path, animation_cooldown=150, rarity=None):
		self.x = x
		self.y = y
		self.name = name
		self.maxHp = maxHp
		self.health = maxHp
		self.damage = damage
		self.animation_cooldown = animation_cooldown
		self.rarity = rarity
		self.animation_list = [import_animation(f'{image_path}/idle'),
		                       import_animation(f'{image_path}/attack'),
		                       import_animation(f'{image_path}/run'),
		                       import_animation(f'{image_path}/dead')]
		self.frame_index = 0
		self.action = 0  # 0:idle, 1:attack, 2:run, 3:dead
		self.update_time = pygame.time.get_ticks()

		self.healthBar = StatusBar(self.x - 50, 738, self.maxHp, self.name, self.maxHp)

		self.image = self.animation_list[self.action][self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.__alive = True

	def update(self):
		self.image = self.animation_list[self.action][self.frame_index]
		if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
			if self.action == 2:
				self.x += 60
				self.rect.center = (self.x, self.y)

		if self.frame_index >= len(self.animation_list[self.action]):
			if self.action == 2:
				self.run()
			elif self.action == 3:
				self.frame_index = len(self.animation_list[self.action]) - 1
			else:
				self.idle()

	def draw(self, screen):
		screen.blit(self.image, self.rect)
		self.healthBar.draw(self.health, screen)

	def is_alive(self):
		return self.__alive

	def take_damage(self, damage):
		if self.health >= damage:
			self.health -= damage
		else:
			self.health = 0

	def idle(self):
		self.action = 0
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def attack(self, enemy):
		self.action = 1
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		damage = random.randint(1, self.damage)
		print(f"{self.name} атакує {enemy.name} та завдає {damage} урона.") if debugMode else ...
		enemy.take_damage(damage)

	def run(self):
		self.action = 2
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def death(self):
		self.action = 3
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		self.__alive = False
