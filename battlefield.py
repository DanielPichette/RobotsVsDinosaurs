from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.dino_herd = Herd().dinosaurs
        self.robot_fleet = Fleet().robots
        # create fleet and herd


# member methods

    def display_welcome(self):
        print('Welcome to the battle of the century. dinosaurs Vs Robots!')
        welcome_prompt = raw_input('would you like to play the dinosaurs or the robots?')

    def battle_as_robots(self):
        robot_defeated = []
        dinosaurs_defeated = []
        self.display_welcome()
        while len(dinosaurs_defeated) or len(robot_defeated) < 3:






    def robot_list(self):
    print(self.robot_fleet)


    def dinosaur_list(self):
    print(self.dino_herd)


    def robots_turn(self):
        print self.robot_fleet
        attack_prompt = raw_input('which robot would you like to attack with? robot1 robot2 or robot3 ?')
        print self.dino_herd
        target_prompt = raw_input('which dinosaur would you like to attack? dinosaur1 dinosaur2 or dinosaur3 ?')
        self.robot_fleet.attack_dinosaur(attack_prompt,target_prompt)
        if target_prompt.health < 0:



