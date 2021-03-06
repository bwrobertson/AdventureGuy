import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.image(0).load(0, 0, 'PyxelArt/Cat.png')
        pyxel.image(1).load(0,0, 'PyxelArt/Man.png')
        pyxel.image(2).load(0,0, 'PyxelArt/Kitty.png')
        self.x = pyxel.width/2
        self.y = pyxel.height/2
        self.music= Music()
        self.cave = Cave()
        self.ocean = Ocean()
        self.glimmer = Glimmer()
        self.Fish = Fish()
        self.Bell = Bell()
        self.Cat = Cat()
        self.bell = False
        self.cat = False
        self.fish = False
        self.atCave = False
        self.isCat = False
        self.catFed = False
        self.testcat = testCat()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if(self.x+5>=pyxel.width-11):
                self.music.sfx_move()
            elif(5<=self.x+5<=25 and 10<=self.y<=20):
                self.music.sfx_move()
            else:
                self.x = (self.x + 5) % pyxel.width
        if pyxel.btnp(pyxel.KEY_LEFT):
            if(self.x-5<=0):
                self.music.sfx_move()
            elif(5<=self.x-5<=25 and 10<=self.y<=20):
                self.music.sfx_move()
            else:
                self.x = (self.x - 5) % pyxel.width
        if pyxel.btnp(pyxel.KEY_UP):
            if(self.y-5<=0):
                self.music.sfx_move()
            elif (5 <= self.x <= 25 and 10 <= self.y-5 <= 20):
                self.music.sfx_move()
            else:
                self.y = (self.y - 5) % pyxel.height
        if pyxel.btnp(pyxel.KEY_DOWN):
            if(self.y+5>=pyxel.height):
                self.music.sfx_move()
            elif (5 <= self.x <= 25 and 10 <= self.y+5 <= 20):
                self.music.sfx_move()
            else:
                self.y = (self.y + 5) % pyxel.height
        if pyxel.btnp(pyxel.KEY_SPACE):
            if(self.x>=pyxel.width-15):
                self.fish=True
                self.music.sfx_item()
            if(25<self.x<35 and (pyxel.height-25)<self.y<(pyxel.height-15)):
                self.bell=True
                self.music.sfx_item()
            if(14<self.x<16 and 20<self.y<30):
                self.atCave=True


    def draw(self):
        pyxel.cls(col=3)
        pyxel.rect(pyxel.width-11, pyxel.height, pyxel.width-13, 0, 10)
        if(self.isCat==False):
            pyxel.blt(self.x, self.y, 1, 0, 0, 7, 9, False)
            #pyxel.circ(self.x, self.y, 2, 6) #head
            #pyxel.rect(self.x - 1, self.y, self.x + 1, self.y + 5, 15)#face
            #pyxel.pix(self.x-1, self.y, 0)#rEye
            #pyxel.pix(self.x + 1, self.y, 0) #lEye
            #pyxel.rect(self.x - 2, self.y+3, self.x+2, self.y+3, 15)#arms
            #pyxel.rect(self.x - 1, self.y+2, self.x + 1, self.y + 5, 6)#body
            #pyxel.rect(self.x - 2, self.y+5, self.x + 2, self.y + 5, 4)#feet
        elif(self.isCat==True):
            pyxel.blt(self.x, self.y, 2, 0 , 0, 8, 5, False)
        self.cave.drawCave()
        self.ocean.drawOcean()
        if(self.bell==False):
            self.glimmer.drawGlimmer()
        if(self.bell==True):
            self.Bell.foundBell()
        if(self.fish==True):
            self.Fish.caughtFish()
        if (self.fish == False and self.atCave==True):
            self.Cat.hungryCat()
            if(self.Cat.count>=200):
                self.atCave=False
                self.Cat.count=0
        if (self.fish == True and self.atCave==True and self.catFed==False):
            self.Cat.feedCat()
            if(self.Cat.count>=200):
                self.atCave=False
                self.Cat.count=0
                self.catFed = True
        if(self.bell == True and self.atCave==True and self.catFed==True):
            self.Cat.jingleCat()
            self.isCat = True
            #if(self.Cat.count==200 and self.testcat.count<1000):
                #self.testcat.testKitty()



class Music:
    def __init__(self):

        # Sound effects
        pyxel.sound(0).set(
            note="c1", tone="s", volume="4", effect=("n" * 4 + "f"), speed=7)
        pyxel.sound(1).set(
            note="d3f3d4", tone="s", volume="4", effect=("n" * 4 + "f"), speed=10)

    def sfx_move(self):
        pyxel.play(ch=0, snd=0)

    def sfx_item(selfs):
        pyxel.play(ch=1, snd=1)

class Fish:
    def __init__(self):
        self.count = 0
    def caughtFish(self):
        if(self.count<200):
            pyxel.rect(40,40,120,65, 7)
            pyxel.rectb(40,40,120,65,0)
            pyxel.text(44,45, "You've obtained the", 0)
            pyxel.text(44,55 ,"catch of the day!", 0)
            self.count+=1

class testCat:
    def __init__(self):
        self.count = 0
        self.x = pyxel.width
        self.y = pyxel.height
        self.animate = 0

    def testKitty(self):
        if(self.count<1000):
            pyxel.rect(0, 0, pyxel.width, pyxel.height, 0)
            if(self.animate==0):
                pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16,False)
                self.x-=1
                self.y-=1
                if(self.x < 0 and self.y < 0):
                    self.animate=1
                    self.x=-20
                    self.y=pyxel.height/2
            elif(self.animate==1):
                pyxel.blt(self.x, self.y, 0, 0, 0, -16, 16, False)
                self.x+=1
                if(self.x > pyxel.width):
                    self.animate=2
                    self.x=0
                    self.y=0
            elif(self.animate==2):
                pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, False)
                self.x+=1
                self.y+=1
            self.count+=1

class Cat:
    def __init__(self):
        self.count = 0

    def hungryCat(self):
        if(self.count<200):
            pyxel.rect(40, 40, 120, 65, 7)
            pyxel.rectb(40, 40, 120, 65, 0)
            pyxel.text(44, 45, "You hear pained", 0)
            pyxel.text(44, 55, "yollowing inside!", 0)
            self.count+=1
    def feedCat(self):
        if(self.count<200):
            pyxel.rect(40, 40, 123, 65, 7)
            pyxel.rectb(40, 40, 123, 65, 0)
            pyxel.text(44, 45, "You toss fish in!", 0)
            pyxel.text(44, 55, "You hear purring!", 0)
            self.count += 1
    def jingleCat(self):
        if(self.count<200):
            pyxel.rect(40, 40, 122, 65, 7)
            pyxel.rectb(40, 40, 122, 65, 0)
            pyxel.text(44, 45, "You jingle the bell!", 0)
            pyxel.text(44, 55, "Something is coming!", 0)
            self.count += 1


class Cave:
    def drawCave(self):
        pyxel.rect(10,10,20,20, 5)#cave middle
        pyxel.rect(5, 15, 25, 20,5)#cave bottom
        pyxel.circ(9,14,3, 5) #cave right
        pyxel.circ(21,14,3,5) #cave left
        pyxel.rect(14,16,16,20,0) #opening middle
        pyxel.rect(12,18,18,20,0) #opening bottom

class Ocean:
    def __init__(self):
        self.count = 0

    def drawOcean(self):
        pyxel.rect(pyxel.width, pyxel.height, pyxel.width - 10, 0, 12)#Ocean
        if(self.count<30):
            pyxel.line(pyxel.width-10, pyxel.height, pyxel.width-10, 0, 7)
            pyxel.line(pyxel.width - 3, pyxel.height, pyxel.width - 3, 0, 7)
            self.count+=1
        elif(self.count<60):
            pyxel.line(pyxel.width - 6, pyxel.height, pyxel.width - 6, 0, 7)
            pyxel.line(pyxel.width, pyxel.height, pyxel.width, 0, 7)

            self.count+=1
        elif (self.count < 90):
            pyxel.line(pyxel.width-8, pyxel.height, pyxel.width-8, 0, 7)
            pyxel.line(pyxel.width - 2, pyxel.height, pyxel.width - 2, 0, 7)
            self.count += 1
        else:
            self.count=0

class Glimmer:
    def __init__(self):
        self.count = 0
    def drawGlimmer(self):
        if (self.count == 100):
            pyxel.pix(30, pyxel.height - 20, 7)
            self.count = 0
        else:
            pyxel.pix(30, pyxel.height - 20, 3)
            self.count += 1

class Bell:
    def __init__(self):
        self.count = 0
    def foundBell(self):
        if(self.count<200):
            pyxel.rect(40,40,120,65, 7)
            pyxel.rectb(40,40,120,65,0)
            pyxel.text(44,45, "You've obtained the", 0)
            pyxel.text(50,55 ,"Bell of Jingles!", 0)
            self.count+=1
App()
