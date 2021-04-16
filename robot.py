from weapon import Weapon


class Robot:
    def __init__(self):
        self.name = ''
        self.health = 0
        self.power_level = 0
        self.weapon = Weapon()

    def attack_dinosaur(self, dinosaur_victim):
        dinosaur_victim.health -= self.weapon.attack_power

