#Base infectivity

this is the initial version of plague_sim, it has the infectivity loop for the final version of the simulator and a basic win condition:

variables: has all the variables needed for this version

Stats function: gives the stats, then adds a day onto the days variable

newInfected: this is the main variable, it determines the amount of people that get infected using this formula: healthy * min(infectivity * 0.018, 0.35) * (random.random() * 0.3)

This version gets the infectivity of a pathogen, but it is not realistic and the time will drag out for excessive periods of time
