import time
import random

population = 8000000000
infectivity = 1
infected = 0
days = 1

def Stats(population, infected, days):
    print(f"healthy:  {population}")
    print(f"infected: {infected}")
    print(f"day:      {days}")
    print("---------------------------------")
    days += 1
    return days
    

isRunning = True
days = Stats(population, infected, days)
time.sleep(1)
while isRunning == True:
    newInfected = int(population * min(infectivity * 0.018, 0.35) * (random.random() * 0.3))
    population -= newInfected
    infected += newInfected
    days = Stats(population, infected, days)

    if population <= 0:
        print ("Everyone infected")
        print (f"Days taken: {days}")
        is_running = False

    time.sleep(1)
        
    
