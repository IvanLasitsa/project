import time
import sys
from config import *
from entities import Dungeon, Player
from render import Render


class Game:
    def __init__(self):
        self.screen, self.clock = configureGame()
        self.player = Player(player['x'], player['y'], player['name'], player['maxHp'],
                             player['damage'], player['image_path'], player['animation_cooldown'])
        self.dungeon = Dungeon(self.player)
        self.dungeon.generate(26, room_names, room_images, enemies)
        self.is_running = True
        self.main_menu()

    def run(self):
        self.update()

    def update(self):
        while self.is_running:
            self.handle_events()
            self.render()
            self.clock.tick(FRAME_RATE)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key):
        if key in KEY_DIRECTIONS:
            direction_index = KEY_DIRECTIONS[key]
            if self.player.current_room.enemy:
                if not self.player.current_room.enemy.is_alive():
                    if len(self.player.current_room.connections) > direction_index:
                        self.player.move(self.player.current_room.connections[direction_index])
            else:
                if len(self.player.current_room.connections) > direction_index:
                    self.player.move(self.player.current_room.connections[direction_index])

    def render(self):
        listToRender = [[self.player.current_room], [self.player, self.player.current_room.enemy]]
        Render.render_stack(listToRender, self.screen)
        self.check_battle()
        self.check_victory()
        pygame.display.update()

    def check_battle(self):
        if self.player.current_room.enemy and (self.player.action == 0 or self.player.action == 3):
            self.dungeon.battle(self.player.current_room.enemy, self.screen)
            if not self.player.is_alive() and (self.player.action == 3 and self.player.frame_index == 5):
                self.game_over()

    def check_victory(self):
        if self.dungeon.check_exit_room(self.player.current_room):
            self.victory()

    def main_menu(self):
        menu = True
        play_button_rect = pygame.Rect(600, 400, 200, 100)
        pygame.draw.rect(self.screen, (255, 255, 255), play_button_rect) 
        self.screen.blit(pygame.image.load('images/main.png')
                                                  .convert(), (0, 0))
        pygame.display.flip()

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    self.game_exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        menu = False
                        self.run()

    def game_exit(self):
        self.show_message("Ви вийшли!")
        self.is_running = False

    def game_over(self):
        self.show_message("Ви Програли!")
        self.is_running = False

    def victory(self):
        self.show_message("Ви виграли!")
        self.is_running = False

    def show_message(self, message):
        self.screen.fill((0, 0, 0))
        Render.draw_text(self.screen, message, pygame.Color('white'), 600, 400)
        pygame.display.update()
        time.sleep(4)
