if __name__ == '__robot__':
    weapon1 = Weapon()

    weapon1.type = 'Laser Beam'
    weapon1.attack_power = 30

    weapon2 = Weapon()

    weapon2.type = 'Sonar Pulse'
    weapon2.attack_power = 25

    weapon3 = Weapon()

    weapon3.type = 'Chum-Bucket Gauntlets'
    weapon3.attack_power = 20


class Weapon:
    def __init__(self):
        self.type = ''
        self.attack_power = 0
