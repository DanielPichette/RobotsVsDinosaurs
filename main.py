from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from weapon import Weapon
from battlefield import Battlefield

if __name__ == '__main__':
    dinosaur1 = Dinosaur()

    dinosaur1.type = 'raptor'
    dinosaur1.health = 200
    dinosaur1.energy = 10
    dinosaur1.attack_power = 30

    dinosaur2 = Dinosaur()

    dinosaur2.type = 'pterosaur'
    dinosaur2.health = 200
    dinosaur2.energy = 15
    dinosaur2.attack_power = 20

    dinosaur3 = Dinosaur()

    dinosaur3.type = 'triceratops'
    dinosaur3.health = 300
    dinosaur3.energy = 8
    dinosaur3.attack_power = 35

    robot1 = Robot()

    robot1.name = 'Megatron'
    robot1.health = 300
    robot1.weapon = 'laser Beam'
    robot1.power_level = 8

    robot2 = Robot()

    robot1.name = 'siri unbound'
    robot1.health = 200
    robot1.weapon = 'Sonar Pulse'
    robot1.power_level = 15

    robot3 = Robot()

    robot1.name = 'Karen'
    robot1.health = 200
    robot1.weapon = 'Chum-Bucket Gauntlets'
    robot1.power_level = 10