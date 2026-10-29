# Base countries

The project is now split up into 3 programs, here is what each program does:

PSV3_Pathogen:

The code for the pathogen is now moved and set out as functions:

__init__: initiates the pathogen class and all the variables related to the pathogen are set up

Infect: the related code and formulas from Plague_Sim is moved to this function and it returns the variables healthy and infected so the main code gets the values for both variables

KilL: the related code and formulas from Plague_Sim is also moved to this function and it returns the variables infected and dead so the main code gets the values for these variables as well

PSV3_Countries:

These 2 classes are used to control the functions for the new countries feature:

Countries: __init__: initiates the countries class (or a specific country) and all variable related to the country is set up

Countries: PathogenProcess: holds the main pathogen processes so the main program works normally

Countries: PathogenSpreadHere: has the function that lets the countries act as its own countries rather than 1 whole country or a country that doesent get affected entirely

AllCountries: __init__: initiates countries UK and USA and has the class set up for both countries and both put in a list to determine if there are any people infected there

AllCountries: Spread: holds the function that holds the feature of the pathogen spreading from country to country

AllCountries: Update: updates the amt healthy, infected and dead for every country

AllCountries: PrintTotal and StoreTotal: both functions collect the amt healthy, infected and dead from every country then PrintTotal prints the totals for all three conditions and StoreTotal returns the values to be stored inside the main program

Plague_Sim_V3: 

The code has changed a lot to make use of the three classes:

Variables: totalHealthy, totalInfected and totalDead are in one line so the values are returned properly

Stats: uses the PrintTotal funtion and adds the days passed onto it, with updating the day as well

The main loop: the code is now just the Update function and StoreTotal functions with the win conditon (and a new one for the only time where the pathogen loses): the same win condition (pathogen wipes out humanity) and a new win condition (pathogen burns itself out by killing all people that is infected)

