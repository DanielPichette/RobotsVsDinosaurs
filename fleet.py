from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robot_fleet = []
        self.create_fleet()

    def create_fleet(self):
        weapon1 = Weapon()
        weapon1.type = 'Laser Beam'
        weapon1.attack_power = 30

        weapon2 = Weapon()
        weapon2.type = 'Sonar Pulse'
        weapon2.attack_power = 25

        weapon3 = Weapon()
        weapon3.type = 'Chum-Bucket Gauntlets'
        weapon3.attack_power = 20

        robot1 = Robot()
        robot1.name = 'Megatron'
        robot1.health = 300
        robot1.weapon = weapon1
        robot1.power_level = 8

        robot2 = Robot()
        robot1.name = 'siri unbound'
        robot1.health = 200
        robot1.weapon = weapon2
        robot1.power_level = 15

        robot3 = Robot()
        robot3.name = 'Karen'
        robot3.health = 200
        robot3.weapon = weapon3
        robot3.power_level = 10

        self.robot_fleet.append(robot1)
        self.robot_fleet.append(robot2)
        self.robot_fleet.append(robot3)

    def print_fleet(self):
        print self.robot_fleet
