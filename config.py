import pygame

debugMode = False

displayWidth = 1400
displayHeight = 800
FRAME_RATE = 24

room_images = []

room_names = [f"Room {chr(room_letter)}" for room_letter in range(ord('A'), ord('Z')+1)]

player = {
    "x": 240,
    "y": 515,
    "name": 'player',
    "maxHp": 120,
    "damage": 10,
    "image_path": 'images/enemies/knight',
    "animation_cooldown": 150
}
enemies = [
    {
        "x": 1160,
        "y": 505,
        "name": "Злий Маг",
        "health": 100,
        "damage": 3,
        "rarity": 0.4,
        "image_path": './images/enemies/wizard',
        "type": 'wizard'
    },
    {
        "x": 1160,
        "y": 467,
        "name": "Скелет",
        "health": 30,
        "damage": 2,
        "rarity": 0.6,
        "image_path": 'images/enemies/skeleton',
        "type": 'skeleton'
    },
    {
        "x": 1160,
        "y": 470,
        "name": "Скелет варіор",
        "health": 50,
        "damage": 4,
        "rarity": 0.3,
        "image_path": 'images/enemies/skeleton_warrior',
        "type": 'skeleton'
    },
    {
        "x": 1040,
        "y": 440,
        "name": "Вовк",
        "health": 65,
        "damage": 3,
        "rarity": 0.5,
        "image_path": 'images/enemies/wolf',
        "type": 'wolf'
    }
]

KEY_DIRECTIONS = {
    pygame.K_1: 0,
    pygame.K_2: 1,
    pygame.K_3: 2,
}


def configureGame():
    pygame.init()
    screen = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption('Dungeon')
    clock = pygame.time.Clock()

    for i in range(1, 27):
        room_images.append(pygame.transform.scale(pygame.image.load(f'images/rooms/{i}.jpg')
                                                  .convert(), (displayWidth, displayHeight)))

    return screen, clock
