import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("main.pyxres")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 5) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)
        pyxel.blt(20, 20, 0, 24, 48, 16, 16, 0)

App()
