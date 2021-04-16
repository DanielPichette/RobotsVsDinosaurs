from herd import Herd
from fleet import Fleet

herd1 = Herd()
fleet1 = Fleet()


class Battlefield:
    def __init__(self):
        self.herd = herd1
        self.fleet = fleet1

    # member methods
    def run_game(self): # what does run game exactly mean?


    def display_welcome(self):
        print ('Welcome to showdown of the century: Dinosaurs VS Robots!')

    def show_dino_opponent_options(self): # says is 'staitic'
        print (herd1)

    def show_robot_opponent_options(self):
        print (fleet1)
