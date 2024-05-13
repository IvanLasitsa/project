import pygame
from render import Render
from config import displayWidth, displayHeight, debugMode


class Room:
    def __init__(self, name, image, enemy=None):
        self.name = name
        self.image = image
        self.connections = [] 
        self.enemy = enemy
        self.isExit = False

    def connect(self, other_room):
        self.connections.append(other_room)

    def spawnEnemy(self, enemy):
        self.enemy = enemy

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        rect = pygame.Rect(0, displayHeight - 100, displayWidth, 100)
        pygame.draw.rect(screen, (0, 0, 0), rect)

        if self.connections:
            Render.draw_room_info(screen, self.name, self.connections, rect)
        if self.connections:
            Render.draw_text(screen, self.name, pygame.Color('white'), 0, 0)
            for i, room in enumerate(self.connections):
                color = pygame.Color('gold' if debugMode else 'white') if room.isExit else pygame.Color('white')
                Render.draw_text(screen, f"{i + 1}. {room.name}", color, rect.x + 40,
                                 rect.y + 10 + i * 30)
