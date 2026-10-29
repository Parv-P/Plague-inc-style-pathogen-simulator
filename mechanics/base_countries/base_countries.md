# Base countries

The project is now split up into 3 programs, here is what each program does:

'PSV3_Pathogen':

The code for the pathogen is now moved and set out as functions:

'__init__': initiates the pathogen class and all the variables related to the pathogen are set up

'Infect': the related code and formulas from Plague_Sim is moved to this function and it returns the variables healthy and infected so the main code gets the values for both variables

'Kill': the related code and formulas from Plague_Sim is also moved to this function and it returns the variables infected and dead so the main code gets the values for these variables as well

PSV3_Countries:

These 2 classes are used to control the functions for the new countries feature:

Countries: '__init__': initiates the countries class (or a specific country) and all variable related to the                 country is set up

           'PathogenProcess'




