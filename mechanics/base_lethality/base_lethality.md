# Base infectivity
The base lethality is added to the initial version, with the win condition changed from "everyone infected" to "everyone dead":

variables: added all the needed variables for lethality (and other ones for symptoms)

Stats function: stats now shows death in the stats function

deathRate and newDead: added new variables for lethality: lethality * 0.004 * organBoost * (1 + (infected/population)) and int(infected * deathRate)

This version gets the finished lethality of a pathogen, but it is most likely going to beat the infectivity and mean the win condition is not met
