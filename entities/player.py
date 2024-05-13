from .enemy import Enemy


class Player(Enemy):
    def __init__(self, x, y, name, maxHp, damage, image_path, animation_cooldown):
        super().__init__(x, y, name, maxHp, damage, image_path, animation_cooldown)
        self.current_room = None  
        self.next_room = None
        self.action = 0

    def update(self):
        super().update()
        if self.x >= 1400 and self.next_room:
            self.x = -50
            self.rect.center = (self.x, self.y)
            self.current_room = self.next_room
            self.run()
        if self.x >= 230 and self.next_room == self.current_room:
            self.next_room = None
            self.x = 240
            self.rect.center = (self.x, self.y)
            self.idle()

    def move(self, new_room):
        self.action = 2
        self.next_room = new_room
