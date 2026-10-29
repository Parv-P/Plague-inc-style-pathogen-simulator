from PS_Pathogen import Pathogen
import random

class Countries:
    def __init__(self, population):
        self.population = population
        self.healthy = population
        self.infected = 0
        self.dead = 0
        self.Pathogen = Pathogen(self.population, infectivity = 1.0, lethality = 0.1, organBoost = 1.0)

    def PathogenProcess(self):
        self.healthy, self.infected = self.Pathogen.Infect(self.healthy, self.infected)
        self.infected, self.dead = self.Pathogen.Kill(self.infected, self.dead)

    def PathogenSpreadHere(self, patientZeroCount):
        self.infected = min(patientZeroCount, self.healthy)
        self.healthy -= self.infected

class AllCountries:

    def __init__(self):
        self.countries = {
           "UK": Countries(69483900),
           "USA": Countries(349594000)
        }
        self.healthyCountries = list(self.countries.keys())
        self.infectedCountries = []
         
    def Spread (self):
        isInfected = random.random()
        if isInfected < 0.05:
            if len(self.healthyCountries) > 0:
                random_country_name = random.choice(self.healthyCountries)
                self.healthyCountries.remove(random_country_name)
                self.infectedCountries.append(random_country_name)
                target_country = self.countries[random_country_name]
                target_country.PathogenSpreadHere(patientZeroCount=1)
                print(f"The pathogen has just started spreading in {random_country_name}!")

    def Update(self):
        for countryName, countryObj in self.countries.items():
            countryObj.PathogenProcess()
            
    def PrintTotal(self):
        totalHealthy = 0
        totalInfected = 0
        totalDead = 0
        for countryName, countryObj in self.countries.items():
            totalHealthy += countryObj.healthy
            totalInfected += countryObj.infected
            totalDead += countryObj.dead
        print(f"--- WORLD STATUS ---")
        print(f"Healthy: {totalHealthy}")
        print(f"Infected: {totalInfected}")
        print(f"Dead: {totalDead}")

    def StoreTotal(self):
        totalHealthy = 0
        totalInfected = 0
        totalDead = 0
        for countryName, countryObj in self.countries.items():
            totalHealthy += countryObj.healthy
            totalInfected += countryObj.infected
            totalDead += countryObj.dead
        return totalHealthy, totalInfected, totalDead
        

