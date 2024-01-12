from math import *

import risar
from risar import stoj

class Turtle:
    def __init__(self):
        self.x = risar.maxX/2
        self.y = risar.maxY/2
        self.angle = 0
        self.pen_active = True
        self.pause = 0
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 2, risar.zelena, 3)
        self.pen_pos = risar.krog(0, 0, 2, risar.rumena, 3)
        self.width = 1
        self.color = risar.bela
        self.stamps = set()
        self.update()

    def update(self):
        self.body.setPos(self.x, self.y)
        self.pen_pos.setPos(self.x, self.y)
        phi = radians(90 - self.angle)
        self.head.setPos(self.x + 5 * cos(phi), self.y - 5 * sin(phi))
        risar.obnovi()
        if self.pause:
            self.wait(self.pause)

    def forward(self, a):
        phi = radians(90 - self.angle)
        nx = self.x + a * cos(phi)
        ny = self.y - a * sin(phi)
        if self.pen_active:
            risar.crta(self.x, self.y, nx, ny, self.color, self.width)
        self.x = nx
        self.y = ny
        self.update()

    def turn(self, phi):
        self.angle += phi
        self.update()

    def backward(self, a):
        self.forward(-a)

    def left(self):
        self.turn(-90)

    def right(self):
        self.turn(90)

    def fly(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.update()

    def pen_up(self):
        self.pen_active = False
        self.pen_pos.hide()

    def pen_down(self):
        self.pen_active = True
        if not self.head.isVisible():
            self.pen_pos.show()

    def wait(self, s):
        risar.cakaj(s)

    def hide(self):
        self.body.hide()
        self.head.hide()
        self.pen_pos.hide()

    def show(self):
        self.body.show()
        self.head.show()
        if self.pen_active:
            self.pen_pos.show()

    def set_pause(self, s):
        self.pause = s

    def no_pause(self):
        self.set_pause(0)

    def turnAround(self):
        self.angle += 180

    def setWidth(self, width):
        self.width = width

    def setColor(self, color):
        self.color = color

    def stamp(self):
        body = risar.krog(0, 0, 5, risar.zelena, 3)
        head = risar.krog(0, 0, 2, risar.zelena, 3)
        body.setPos(self.x, self.y)
        phi = radians(90 - self.angle)
        head.setPos(self.x + 5 * cos(phi), self.y - 5 * sin(phi))
        self.stamps.add((body, head))

    def clearStamps(self):
        for stamp in self.stamps:
            for oblika in stamp:
                risar.odstrani(oblika)


zelva = Turtle()
zelva.fly(risar.maxX/2, risar.maxY/2 + 100, 270)
zelva.set_pause(0.25)
# zelva.wait(0.5)
# zelva.pen_up()
# zelva.wait(0.5)
# zelva.hide()
# zelva.wait(0.5)
# zelva.show()
# zelva.wait(0.5)
# zelva.hide()
# zelva.wait(0.5)
# zelva.pen_down()
# zelva.wait(0.5)
# zelva.show()
# zelva.wait(0.5)
for barva in [risar.modra, risar.rdeca, risar.zelena, risar.rumena]:
    zelva.stamp()
    zelva.setColor(barva)
    zelva.forward(100)
    zelva.right()
    zelva.forward(100)

zelva.clearStamps()
risar.stoj()

