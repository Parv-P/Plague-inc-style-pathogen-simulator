import time
import random

population = 8000000000
healthy = 8000000000
infectivity = 1
infected = 0
lethality = 0.1
organBoost = 1
dead = 0
days = 1

def Stats(h, i, d, dayCount):
    print(f"healthy:  {h}")
    print(f"infected: {i}")
    print(f"dead:     {d}")
    print(f"day:      {dayCount}")
    print("---------------------------------")
    dayCount += 1
    return dayCount
    

isRunning = True
days = Stats(healthy, infected, dead, days)
time.sleep(1)
while isRunning == True:
    newInfected = int(healthy * min(infectivity * 0.018, 0.35) * (random.random() * 0.3))
    deathRate = lethality * 0.004 * organBoost * (1 + (infected/population))
    newDead = int(infected * deathRate)
    healthy -= newInfected
    infected += newInfected
    infected -= newDead
    dead += newDead
    days = Stats(healthy, infected, dead, days)

    if healthy <= 0 and infected <= 0:
        print ("Everyone dead, simulator finished")
        print (f"Days taken: {days}")
        isRunning = False

    time.sleep(1)
        
    
