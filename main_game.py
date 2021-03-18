#main game.py
#Duke Ayurzana
#2/20/2021
#CSS 225


#This is the main controller of the whole game.
#Introduce the game.
#Set any inital values to the main character's properties.

from main_character import player
import section_1
import section_2
import section_3


print("old name: ", player.name)
#player.name = input("Enter your name: ")
#print("new name: ", player.name)

section_1.start()
section_2.start()
section_3.start()