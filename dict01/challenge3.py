#!/usr/bin/env python4
char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America)")
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")
heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }  
print(char_name + " " + char_stat + heroes[char_name][char_stat])
#print(heroes[char_name]+ heroes[char_stat] + heroes[char_name][char_stat])

