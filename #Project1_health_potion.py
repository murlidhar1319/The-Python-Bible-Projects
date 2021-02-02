#Project_1:Crafting a Health Potion
#Module, random 


import random

health = 50

#1=easy, 2=medium, 3=hard
difficulty_level = 3

potion_health = random.randint(25, 50) // difficulty_level
# print(potion_health)

health = health + potion_health
print(health)


