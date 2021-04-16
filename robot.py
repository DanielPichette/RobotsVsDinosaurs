from battlefield import herd1
from weapon import Weapon


class Robot:
    def __init__(self):
        self.name = ''
        self.health = 0
        self.power_level = 0
        self.weapon = Weapon()   # is this the proper way to incorporate weapon?


    def attack_dinosaur(self, dinosaur_victim):
        dinosaur_victim.health -= self.weapon.attack_power
        if dinosaur_victim.health < 0:
            herd1.dinosaur_army.remove(dinosaur_victim)
        if dinosaur_army = []:
            print('Robots Win!')
