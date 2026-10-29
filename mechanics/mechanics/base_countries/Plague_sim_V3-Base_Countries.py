import time
import random
from PS_Countries import AllCountries

AllCountries = AllCountries()
days = 1
totalHealthy, totalInfected, totalDead = AllCountries.StoreTotal()

def Stats(dayCount):
    AllCountries.PrintTotal()
    print(f"Day: {dayCount}")
    print("---------------------------------")
    dayCount += 1
    return dayCount
    

isRunning = True
days = Stats(days)
time.sleep(1)
while isRunning == True:
    AllCountries.Update()
    totalHealthy, totalInfected, totalDead = AllCountries.StoreTotal()
    days = Stats(days)

    if totalHealthy <= 0 and totalInfected <= 0:
        print ("Everyone dead")
        print (f"Days taken: {days}")
        isRunning = False
    elif totalInfected <= 0 and totalDead != 0:
        print ("Pathogen killed everyone that was infected")
        print(f"Days taken: {days}")
        isRunning = False

    time.sleep(1)
        
    
