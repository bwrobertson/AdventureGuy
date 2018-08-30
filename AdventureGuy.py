import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = pyxel.width/2
        self.y = pyxel.height/2
        self.music= Music()
        self.border = Border()
        self.cave = Cave()
        self.pond = Pond()
        self.glimmer = 0
        self.cat = False
        self.fish = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if(self.x+5==pyxel.width):
                self.music.sfx_move()
            else:
                self.x = (self.x + 5) % pyxel.width
        if pyxel.btnp(pyxel.KEY_LEFT):
            if(self.x-5==0):
                self.music.sfx_move()
            else:
                self.x = (self.x - 5) % pyxel.width
        if pyxel.btnp(pyxel.KEY_UP):
            if(self.y-5==0):
                self.music.sfx_move()
            else:
                self.y = (self.y - 5) % pyxel.height
        if pyxel.btnp(pyxel.KEY_DOWN):
            if(self.y+5==pyxel.height):
                self.music.sfx_move()
            else:
                self.y = (self.y + 5) % pyxel.height

    def draw(self):
        self.border.drawBorder()
        pyxel.circ(self.x, self.y, 2, 6) #head
        pyxel.rect(self.x - 1, self.y, self.x + 1, self.y + 5, 15)#face
        pyxel.pix(self.x-1, self.y, 0)#rEye
        pyxel.pix(self.x + 1, self.y, 0) #lEye
        pyxel.rect(self.x - 2, self.y+3, self.x+2, self.y+3, 15)#arms
        pyxel.rect(self.x - 1, self.y+2, self.x + 1, self.y + 5, 6)#body
        pyxel.rect(self.x - 2, self.y+5, self.x + 2, self.y + 5, 4)#feet
        self.cave.drawCave()
        self.pond.drawPond()
        if(self.glimmer==100):
            pyxel.pix(30,pyxel.height-20, 7)
            self.glimmer=0
        else:
            pyxel.pix(30,pyxel.height-20, 3)
            self.glimmer+=1

class Music:
    def __init__(self):

        # Sound effects
        pyxel.sound(0).set(
            note="c1", tone="s", volume="4", effect=("n" * 4 + "f"), speed=7)

    def sfx_move(self):
        pyxel.play(ch=0, snd=0)

class Border:
    def drawBorder(self):
        pyxel.cls(col=3)
        pyxel.rect(0, 0, 2, pyxel.height, 1)
        pyxel.rect(0, 0, pyxel.width, 2, 1)
        pyxel.rect(pyxel.width,pyxel.height, pyxel.width-2, 0, 1)
        pyxel.rect(pyxel.width, pyxel.height, 0, pyxel.height-2, 1)

class Cave:
    def drawCave(self):
        pyxel.rect(10,10,20,20, 5)#cave middle
        pyxel.rect(5, 15, 25, 20,5)#cave bottom
        pyxel.circ(9,14,3, 5) #cave right
        pyxel.circ(21,14,3,5) #cave left
        pyxel.rect(14,16,16,20,0) #opening middle
        pyxel.rect(12,18,18,20,0) #opening bottom

class Pond:
    def drawPond(self):
        pyxel.circ(pyxel.width-20, pyxel.height-20, 10, 12) #main pond
        pyxel.circb(pyxel.width-20, pyxel.height-20, 9, 7)
        pyxel.circb(pyxel.width - 20, pyxel.height - 20, 6, 7)
        pyxel.circb(pyxel.width - 20, pyxel.height - 20, 3, 7)

App()
