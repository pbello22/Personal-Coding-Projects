'''
Name: Paul Bello
Project: Cooking Time
Purpose: Use functions to calculate time left, preparation time, and total time spent making a lasagna
Date: 11/22/2022
'''

expected_minutes_in_oven = 40

#Calculates how much time is left for cooking in the oven
def remainingMinutes(TimeInOven):
    return expected_minutes_in_oven - TimeInOven


#print(remainingMinutes(15))


#Calculates the preparation time
def preparationMinutes(numLayers):
    return numLayers*2


#Calculates How much time has been spent making the lasagna so far
def totalTimeMakingMinutes(numLayers, TimeInOven):
    return TimeInOven + preparationMinutes(numLayers)

print('Total time spent making the lasagna: ' + str(totalTimeMakingMinutes(4, 15)) + ' minutes.')






