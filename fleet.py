from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = self.create_fleet()

    def create_fleet(self):
        weapon1 = Weapon()
        weapon1.type = 'Laser Beam'
        weapon1.attack_power = 5

        weapon2 = Weapon()
        weapon2.type = 'Sonar Pulse'
        weapon2.attack_power = 5

        weapon3 = Weapon()
        weapon3.type = 'Chum-Bucket Gauntlets'
        weapon3.attack_power = 10

        robot1 = Robot()
        robot1.name = 'Megatron'
        robot1.health = 30
        robot1.weapon = weapon1
        robot1.power_level = 10

        robot2 = Robot()
        robot2.name = 'R2-D2'
        robot2.health = 20
        robot2.weapon = weapon2
        robot2.power_level = 10

        robot3 = Robot()
        robot3.name = 'Karen'
        robot3.health = 20
        robot3.weapon = weapon3
        robot3.power_level = 10

        robots = [robot1, robot2, robot3]
        return robots
