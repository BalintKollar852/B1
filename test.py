import sys, pygame
import random
pygame.init()

x=0.5
speed = [x, x]
size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ct.png")
ballrect = ball.get_rect()

Sair = True

while Sair:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: Sair=False
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        x=random.uniform(0, 1)
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        x=random.uniform(0, 1)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    pos = [0, 0]
    while Sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: Sair = False

        if ballrect.left < 0 or ballrect.right > width:
            x = random.uniform(0.1, 1)
            speed[0] = x if speed[0] < 0.0 else -x

        if ballrect.top < 0 or ballrect.bottom > height:
            x = random.uniform(0.1, 1)
            speed[1] = x if speed[1] < 0.0 else -x

        pos[0] += speed[0]
        pos[1] += speed[1]
        ballrect.topleft = (int(pos[0]), int(pos[1]))

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()

        def __init__(self, menu: 'Menustage'):
            super().__init__()

            self.m7: MyActor = MyActor("ctl10.png", pos=(350, 225), anchor=(0, 0))
            self.add_actor(self.m7)
            self.menu: Menustage = menu

            self.m6: MyActor = MyActor("ctl9.png", pos=(350, 225), anchor=(0, 0))
            self.add_actor(self.m6)
            self.menu: Menustage = menu

            self.m5: MyActor = MyActor("ctl8.png", pos=(350, 225), anchor=(0, 0))
            self.add_actor(self.m5)
            self.menu: Menustage = menu

            self.m3: MyActor = MyActor("clt6.png", pos=(350, 225), anchor=(0, 0))
            self.add_actor(self.m3)
            self.menu: Menustage = menu

            self.m4: MyActor = MyActor("ctl7.png", pos=(350, 225), anchor=(0, 0))
            self.add_actor(self.m4)
            self.menu: Menustage = menu

            self.m: MyActor = MyActor("cross.png", pos=(300, 300), anchor=(0, 0))
            self.add_actor(self.m)
            self.menu: Menustage = menu
            self.set_on_mouse_down_listener(self.jerrymove)

            self.m2: MyActor = MyActor("backr.png", pos=(0, 0), anchor=(0, 0))
            self.m2.set_on_mouse_down_listener(self.back)
            self.add_actor(self.m2)
            self.menu: Menustage = menu

            self.m8: MyActor = MyActor("hit.png", pos=(300, 300), anchor=(0, 0))
            self.add_actor(self.m8)
            self.menu: Menustage = menu

sys.exit()