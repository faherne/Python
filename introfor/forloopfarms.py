#!/usr/bin/env python3

# Dictionary of farms
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across the list vendors
for farm in farms:
    print("The farm name is: " + str( farm["name"]))  # each time through the loop print value of x
    print("The farm animals are: " + str(farm["agriculture"]))
print("\nOur loop has ended.")  # when the loop ends print this

