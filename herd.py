from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaur_herd = []

    # member methods
    def create_herd(self):
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
        dinosaur3.attack_power = 30

        self.dinosaur_herd.append(dinosaur1)
        self.dinosaur_herd.append(dinosaur2)
        self.dinosaur_herd.append(dinosaur3)

    def print_herd(self):
        print self.dinosaur_herd
