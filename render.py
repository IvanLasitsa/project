from config import *


class Render:
	@staticmethod
	def init_font():
		pygame.font.init()
		return pygame.font.Font(None, 36)

	@staticmethod
	def render_stack(renderList, screen):
		for item in renderList[0]:
			item.draw(screen)

		for item in renderList[1]:
			if item:
				item.update()
				item.draw(screen)

	@staticmethod
	def draw_room_info(screen, current_room_name, connected_rooms, rect):
		Render.draw_text(screen, current_room_name, pygame.Color('white'), 0, 0)
		for i, room in enumerate(connected_rooms):
			color = pygame.Color('gold' if debugMode else 'white') if room.isExit else pygame.Color('white')
			Render.draw_text(screen, f"{i + 1}. {room.name}", color, rect.x + 40, rect.y + 10 + i * 30)

	@staticmethod
	def draw_text(surface, text, color, x, y):
		font = Render.init_font()
		text_surface = font.render(text, True, color)
		surface.blit(text_surface, (x, y))
