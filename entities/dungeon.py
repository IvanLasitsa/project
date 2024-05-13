import random
from config import debugMode

import pygame
from render import Render
from .room import Room
from .enemy import Enemy


class Dungeon:
    def __init__(self, player):
        self.player = player
        self.rooms = []  
        self.__exitRoom = None

    def check_exit_room(self, room):
        return self.__exitRoom == room

    def add_room(self, room):
        self.rooms.append(room)

    def generate(self, num_rooms, room_names, room_images, enemies):
        unique_names = random.sample(room_names, num_rooms)
        unique_images = random.sample(room_images, num_rooms)
        player_index = random.randint(0, num_rooms)

        for i in range(num_rooms):
            name = unique_names[i]
            image = unique_images[i]
            room = Room(name, image)
            if player_index == i:
                self.spawn_player(room)
            else:
                self.spawnEnemyInRoom(room, enemies)
            self.add_room(room)

        self.connect_rooms()

    def connect_rooms(self):
        for room in self.rooms:
            num_connections = random.randint(2, 3)
            connected_rooms = set()
            while len(room.connections) < num_connections:
                other_room = random.choice(self.rooms)
                if other_room != room and other_room not in connected_rooms:
                    room.connect(other_room)
                    connected_rooms.add(other_room)

        self.generate_exit_room()
        print(f'Вихід - {self.__exitRoom.name}') if debugMode else ...

    def generate_exit_room(self):
        self.__exitRoom = random.choice(self.rooms)
        self.__exitRoom.isExit = True
        if self.player.current_room == self.__exitRoom:
            self.generate_exit_room()
            

    def spawn_player(self, room):
        self.player.current_room = room
        print(f'Гравець в кімнаті - {room.name}') if debugMode else ...

    @staticmethod
    def spawnEnemyInRoom(room, enemies):
        enemy = random.choice(enemies)
        if random.random() < enemy['rarity']:
            enemies = Enemy(enemy['x'], enemy['y'], enemy['name'], enemy['health'],
                            enemy['damage'], enemy['image_path'], 150, enemy['rarity'])
            print(f"{room.name} || enemy: {enemies.name}") if debugMode else ...

            room.spawnEnemy(enemies)

    def battle(self, enemy, screen):
        while self.player.health > 0 and enemy.health > 0:
            listToRender = [[self.player.current_room], [self.player, self.player.current_room.enemy]]
            Render.render_stack(listToRender, screen)
            pygame.display.update()

            if self.player.action == 0:
                self.player.attack(enemy)
            if enemy.action == 0:
                enemy.attack(self.player)

            if enemy.health <= 0:
                enemy.death()
                print(f"{enemy.name} помер!") if debugMode else ...
                print(f"Життя ворога {enemy.health}") if debugMode else ...
                break
            if self.player.health <= 0:
                self.player.death()
                print(f"{self.player.name} помер!") if debugMode else ...
                print(f"Життя гравця {self.player.health}") if debugMode else ...
                break
