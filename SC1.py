#Name:
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

enemy_creatures = {
    "enemy_1" : {
         "name" : "centaur",
       "weapon" : "crossbow",
       "damage" : 55,
       "health" : 500,
},
    "enemy_2" : {
         "name" : "minotaur",
       "weapon" : "great axe",
       "damage" : 200,
       "health" : 2000,
    "armor protection" : "30% damage negation",
    },
    "enemy_3" : {
         "name" : "star kissed knight",
       "weapon" : "dwarf-star greatsword",
       "damage" : 10000,
       "health" : 85000,
    "armor protection" : "70% damage negation",
        "mount" : "pegasus",
    },
    "enemy_4" : {
         "name" : "elf warrior",
       "weapon" : "magical musket",
       "damage" : 3500,
       "health" : 10000,
        "armor protection" : "10% damage negation",
},
    "enemy_5" : {
         "name" : "medusa's spawn",
       "weapon" : "eyes",
       "damage" : "Infinity",
       "health" : 60000,
    }
}
print(enemy_creatures)
enemy_creatures["enemy_1"].update({"damage": input()})
print(enemy_creatures["enemy_1"])
