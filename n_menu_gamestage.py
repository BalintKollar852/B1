import random
from turtle import Turtle
from n_mygameworld import *
from n_menu_menustage import *
import sys, pygame
from random import Random

class GameStage(MyStage):

    def back(self, pos, btn):
        self.menu.menu_Main()

    def crossmove(self, timer=0):
        r: Random = Random()
        animate(self.cross, duration=1, pos=(r.randint(200, 600), r.randint(100, 500)))

    def click(self, pos, button):
        pass

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

        self.cross: MyActor = MyActor("cross.png", pos=(350, 300), anchor=(0, 0))
        self.add_actor(self.cross)
        self.menu: Menustage = menu
        self.set_on_mouse_down_listener(self.click)

        self.m2: MyActor = MyActor("backr.png", pos=(0, 0), anchor=(0, 0))
        self.m2.set_on_mouse_down_listener(self.back)
        self.add_actor(self.m2)
        self.menu: Menustage = menu

        self.t : MyTickTimer = MyTickTimer(func=self.crossmove, interval=1)
        self.add_timer(self.t)
        self.crossmove()