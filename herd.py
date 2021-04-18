from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = self.create_herd()

    # member methods
    def create_herd(self):
        dinosaur1 = Dinosaur()
        dinosaur1.type = 'raptor'
        dinosaur1.health = 20
        dinosaur1.energy = 10
        dinosaur1.attack_power = 5

        dinosaur2 = Dinosaur()
        dinosaur2.type = 'pterosaur'
        dinosaur2.health = 20
        dinosaur2.energy = 10
        dinosaur2.attack_power = 5

        dinosaur3 = Dinosaur()
        dinosaur3.type = 'triceratops'
        dinosaur3.health = 30
        dinosaur3.energy = 5
        dinosaur3.attack_power = 10

        dinos = [dinosaur1, dinosaur2, dinosaur3]
        return dinos
