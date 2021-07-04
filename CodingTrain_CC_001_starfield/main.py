from random import randint

from Drawing.interface import Interface
from utils import translate

width = 1000
height = 1000
decrement = 0


def mouse_move(x, y, hovered):
    global decrement
    if hovered:
        decrement = translate(x, 0, width, 0, 20)


class Program(Interface):
    def __init__(self):
        Interface.__init__(self, "Starfield", width, height, "black", "white")
        self.amount = 800
        self.stars = [Star() for _ in range(self.amount)]
        self.show_frames = True
        self.translate(width / 2, height / 2)
        self.on_mouse_move = lambda x, y: mouse_move(x, y, self.mouse_hovered)
        self.on_click = lambda x, y: print(x, y)

    def draw(self):
        for star in self.stars:
            star.update()
            star.draw(self)


class Star:
    def __init__(self):
        self.x = randint(-int(width / 2), int(width / 2))
        self.y = randint(-int(height / 2), int(height / 2))
        self.z = randint(0, width)
        self.last_x = self.x
        self.last_y = self.y

    def update(self):
        self.z -= decrement
        if self.z > 0:
            return

        self.z = width
        self.x = randint(-int(width / 2), int(width / 2))
        self.y = randint(-int(height / 2), int(height / 2))
        self.last_x = self.x
        self.last_y = self.y

    def draw(self, interface):
        dx = translate(self.x / self.z, 0, 1, 0, width)
        dy = translate(self.y / self.z, 0, 1, 0, height)
        rad = translate(self.z, 0, width, 16, 0)
        interface.ellipse(dx, dy, rad, rad)

        interface.line(self.last_x, self.last_y, dx, dy)
        self.last_x = dx
        self.last_y = dy


Program().run()
