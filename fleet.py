from robot import Robot
from weapon import weapon1, weapon2, weapon3

if __name__ == '__fleet__':
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

    robot1.name = 'Karen'
    robot1.health = 200
    robot1.weapon = weapon3
    robot1.power_level = 10


class Fleet:
    def __init__(self):
        self.robot_army = []

    def create_herd(self):
        self.robot_army.append(robot1)
        self.robot_army.append(robot2)
        self.robot_army.append(robot3)

    def print_herd(self):
        print self.dinosaurs