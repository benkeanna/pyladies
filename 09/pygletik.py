import pyglet
import math
rychlost = 20

window = pyglet.window.Window() # trida Window

def nacti_obrazek(jmeno):
    obrazek = pyglet.image.load(jmeno)
    # obrazek.anchor_x = obrazek.width // 2
    # obrazek.anchor_y = obrazek.width // 2
    return obrazek

obrazek = nacti_obrazek('had.png')
obrazek2 = nacti_obrazek('had2.png')
had = pyglet.sprite.Sprite(obrazek)

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 1/4)

def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 1/4)

def zpracuj_text(text):
    print(had.x)

def tik(t):
    had.x = had.x + rychlost *t
    had.y = abs(math.sin(had.x / 5) * 50)

def vykreslit():
    window.clear()
    had.draw()

def klik(x,y,tlacitko,mod):
    had.x = x
    had.y = y

window.push_handlers(
            on_text = zpracuj_text,
            on_draw = vykreslit,
            on_mouse_press = klik,
            )
pyglet.clock.schedule_interval(tik, 1/30)
pyglet.clock.schedule_once(zmen, 1)
pyglet.app.run() # smicka udalosti, musi byt na konci
print('Hotovo')
