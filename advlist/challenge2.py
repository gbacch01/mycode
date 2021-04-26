#!/usr/bin/env python3
icecream= ["flavors", "salty"]
print(icecream)
num= [99]
icecream.append(num)
print(icecream)
#user inputs name
name = input("What is your name? ")
#print that puts all of that together
print(f"{icecream[-1]} {icecream[0]} and {name} chooses to be {icecream[1]}")
#print(icecream[-1] + "Flavors, and ", name + "chooses to be salty"
