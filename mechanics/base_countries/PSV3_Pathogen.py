import random

class Pathogen:
    def __init__(self, population, infectivity, lethality, organBoost):
        self.infectivity = infectivity
        self.lethality = lethality
        self.organBoost = organBoost
        self.population = population
        
    def Infect(self, healthy, infected):
        newInfected = int(healthy * min(self.infectivity * 0.018, 0.35) * (random.random() * 0.3))
        healthy -= newInfected
        infected += newInfected
        return healthy, infected

    def Kill(self, infected, dead):
        deathRate = self.lethality * 0.004 * self.organBoost * (self.lethality + (infected/self.population))
        newDead = int(infected * deathRate)
        infected -= newDead
        dead += newDead
        return infected, dead
