import json
import os
from random import choice

# Set the working directory to the location of your project
project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)

class FCP:
    def __init__(self, **kwargs):

        self.age = self.generate("Âge")
        self.corpulence = self.generate("Corpulence")
        self.peau = self.generate("Couleur de peau")
        self.cheveux = self.generate("Couleur des cheveux")
        self.yeux = self.generate("Couleur des yeux")
        self.genre = self.generate("Genre")
        self.nez = self.generate("Nez")
        self.posture = self.generate("Posture")
        self.taille = self.generate("Taille")
        self.visage = self.generate("Visage")

        pass

    def generate(self, trait):
        file_name = 'fcp_'+trait+'.json'
        with open(os.path.join('data', file_name), 'r') as json_file:
            table = json.load(json_file)

        alea = choice(list(table.values()))

        return alea

