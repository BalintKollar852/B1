import random
from turtle import Turtle
from n_mygameworld import *
from n_menu_menustage import *



class GameStage(MyStage):

    def back(self, pos, btn):
        self.menu.menu_Main()

    def jerrymove(self, pos, btn):
        animate(self.m, pos = pos)
        animate(self.m, pos = pos)


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

        self.m8: MyActor = MyActor("hitp.png", pos=(300, 300), anchor=(0, 0))
        self.add_actor(self.m8)
        self.menu: Menustage = menu
        self.set_on_mouse_down_listener(self.jerrymove)






