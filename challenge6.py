#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
for nefarm in farms[0]["agriculture"]:
    print("\nThe animals in NE Farm are " + nefarm) 

Answer = input("\nchoose a farm (NE Farm, W Farm, or SE Farm)").lower()


If Answer == "ne farm":
    for nefarm in farms[0]["agriculture"]:
    print("\nThe animals in NE Farm are " + nefarm)
elif
