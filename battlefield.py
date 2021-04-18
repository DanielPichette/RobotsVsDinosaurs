from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.dino_herd = Herd().dinosaurs
        self.robot_fleet = Fleet().robots
        self.robot_defeated = []
        self.dinosaurs_defeated = []
        # create fleet and herd

    # member methods


    def display_welcome(self):
        print('Welcome to Dinosaurs Vs Robots!')
        welcome_prompt = raw_input('would you like to play the dinosaurs or the robots?')
        print (welcome_prompt + 'lets get started!')

    def robot_list(self):
        print(self.robot_fleet)

    def dinosaur_list(self):
        print(self.dino_herd)

    def robots_turn(self):
        print self.robot_fleet
        attack_prompt = raw_input('who would you like to  attack with? robot1 robot2 or robot3 ?')
        print self.dino_herd
        if attack_prompt == 1:
            attacker = robot1
            return attacker
        elif attack_prompt == 2:
            attacker = robot2
            return attacker
        elif attack_prompt == 1:
            attacker = robot3
            return attacker
        target_prompt = raw_input('who would you like to attack? 1 2 or 3 ?')
        if target_prompt == 1:
            target = dinosaur1
            return target
        elif target_prompt == 2:
            target = dinosaur2
            return target
        elif target_prompt == 3:
            target = dinosaur3
            return target

        if target.health < 0:
           self.dinosaurs_defeated.append(target)

    def dinosaurs_turn(self):
        print self.dino_herd
        attack_prompt = raw_input('who would you like to  attack with? robot1 robot2 or robot3 ?')
        print self.dino_herd
        if attack_prompt == 1:
            attacker = dinosaur1
            return attacker
        elif attack_prompt == 2:
            attacker = dinosaur2
            return attacker
        elif attack_prompt == 1:
            attacker = dinosaur3
        return attacker
        target_prompt = raw_input('who would you like to attack? 1 2 or 3 ?')
        if target_prompt == 1:
            target = robot1
            return target
        elif target_prompt == 2:
            target = robot2
            return target
        elif target_prompt == 3:
            target = robot3
            return target

        if target.health < 0:
            self.robot_defeated.append(target)

    def battle(self):
        print ('its time to battle!')

    def display_winner(self):
        if len(self.robot_defeated) == 3:
            print('Dinodaurs Win!!')
        elif len(self.robot_defeated) == 3:
            print (Robots Win!!)

    def run_game(self):
        self.display_welcome()
        while len(self.dinosaurs_defeated) or len(self.robot_defeated) < 3:
            self.battle()
            self.robots_turn()
            self.dinosaurs_turn()
        self.display_winner()