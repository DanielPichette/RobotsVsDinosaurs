class Dinosaur:
    def __init__(self):
        self.type = ''
        self.health = 0
        self.energy = 0
        self.attack_power = 0

    def attack_robot(self, robot_victim):
        robot_victim.health -= self.attack_power
        if robot_victim.health < 0:
            fleet1.robot_army.remove(robot_victim)
        if robot_army =[]:
            print('Dinosaurs Win!')