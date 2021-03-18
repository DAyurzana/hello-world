#section_2
#Duke Ayurzana
#2/25/2021
#CSS 225
import random
from main_character import player
def start():
    inventory = []
    print("As the warrior growing up he becomes more stronger than ever before.")
    print("There will be magical spirit awaken, people named her as an Ancient Maiden.")
    print("Ancient Maiden knows secret locations of special magical weapons that can efeat any monsters and creatures. Duke will be need those items and the Ancient")
    print("Maiden will help him to discover those weapons.")
    player.inventory.append("Sword and Iron Shield")
    player.inventory.append("Axe and Stone Shield")
    print(player.inventory)
    ancient_guide = (input("Click H to see Ancient advice"))
    if ancient_guide == "H":
        print("The boss monster is going to be hard tough")
        print("Ancestors recommending the Axe and Stone Shield for to beat foreign creature.")
    choose_weapon = input("Which weapon would you like to use? type A for Sword and Iron Shield or B for Axe and Stone Shield.")
    if choose_weapon == "A":
        print("You have equipped Sword and Iron Shield")
        player.inventory.append("Sword and Iron Shield")
        print("You Lose!")
        exit()
    elif choose_weapon == "B":
        print("You have equipped Axe and Stone Shield")
        player.inventory.append("Axe and Stone Shield")