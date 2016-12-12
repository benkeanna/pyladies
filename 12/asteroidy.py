import pyglet
import math
import random

ROTATION_SPEED = 200
ACCELERATION = 300

def load_image(path):
    image = pyglet.image.load(path)
    image.anchor_x = image.width // 2
    image.anchor_y = image.width // 2
    return image

spaceship_img = load_image('SpaceShooterRedux/PNG/playerShip3_green.png')
asteroid_imgs = [
    load_image('SpaceShooterRedux/PNG/Meteors/meteorGrey_big1.png'),
    load_image('SpaceShooterRedux/PNG/Meteors/meteorGrey_big2.png'),
    load_image('SpaceShooterRedux/PNG/Meteors/meteorGrey_big3.png'),
    load_image('SpaceShooterRedux/PNG/Meteors/meteorGrey_big4.png'),
    ]

window = pyglet.window.Window()

pressed_keys = set()

batch = pyglet.graphics.Batch()

class SpaceObject:
    def __init__(self, window):
        self.x = window.width / 2
        self.y = window.height / 2
        self.rotation = 0
        self.x_speed = 0
        self.y_speed = 0
        self.window = window
    def draw(self):
            self.sprite.x = self.x
            self.sprite.y = self.y
            self.sprite.rotation = 90 - self.rotation
    def tick(self, dt):
        distance_x = self.x_speed * dt
        distance_y = self.y_speed * dt
        self.x = self.x + distance_x
        self.y = self.y + distance_y

        while self.x > self.window.width:
            self.x = self.x - self.window.width
        while self.x < 0:
            self.x = self.x + self.window.width
        while self.y > self.window.height:
            self.y = self.y - self.window.height
        while self.y < 0:
            self.y = self.y + self.window.height

class Spaceship(SpaceObject):
    def __init__(self, window):
        super().__init__(window)
        self.sprite = pyglet.sprite.Sprite(spaceship_img, batch=batch)

    def tick(self, dt):
        if pyglet.window.key.LEFT in pressed_keys:
            self.rotation = self.rotation + ROTATION_SPEED * dt
        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation = self.rotation - ROTATION_SPEED * dt
        if pyglet.window.key.UP in pressed_keys:
            rot = math.radians(self.rotation)
            self.x_speed = self.x_speed + dt * ACCELERATION * math.cos(rot)
            self.y_speed = self.y_speed + dt * ACCELERATION * math.sin(rot)
        if pyglet.window.key.DOWN in pressed_keys: # nepovinne zpomalovani
            rot = math.radians(self.rotation)
            self.x_speed = self.x_speed - dt * ACCELERATION * math.cos(rot)
            self.y_speed = self.y_speed - dt * ACCELERATION * math.sin(rot)
        super().tick(dt)

class Asteroid(SpaceObject):
    def __init__(self, window):
        super().__init__(window)
        img = random.choice(asteroid_imgs)
        self.sprite = pyglet.sprite.Sprite(img, batch=batch)

        self.x = 0
        self.y = random.uniform(0, self.window.height)


objects = []
objects.append(Spaceship(window))
objects.append(Asteroid(window))

def draw():
    window.clear()
    for obj in objects:
        obj.draw()

    for x in -window.width, 0, window.width:
        for y in -window.height, 0, window.height:
            pyglet.gl.glPushMatrix()
            pyglet.gl.glTranslatef(x, y, 0)
            batch.draw()
            pyglet.gl.glPopMatrix()

def key_pressed(key, mod):
    pressed_keys.add(key)

def key_released(key, mod):
    pressed_keys.discard(key)


window.push_handlers(
    on_draw=draw,
    on_key_press=key_pressed,
    on_key_release=key_released,
    )

def tick(dt):
    for obj in objects:
        obj.tick(dt)

pyglet.clock.schedule_interval(tick, 1/30)



pyglet.app.run()
