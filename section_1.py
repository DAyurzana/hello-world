#section_1
#Duke Ayurzana
#2/20/2021
#CSS 225
import random
from main_character import player
def start():
    print("The world has been invaded by alien creatures.")
    print("Survivors from the attack gathered and finding way to get away from monsters.")
    print("Duke becomes the warrior from small group of survivors and will fight against monsters.")
    print("However, a warrior needs experiences to get powerful from destroying of small creatures.")
    print("Duke will need to see random survivors to get information about monster types.")
    print("Duke will choose a monster to fight, it will gain his power for greater alien creatures.")
    print("A. Level 1 monster or B. Level 5 monster")
    picking_a_fight = (input("Which monster would you challenge? Type A or B"))
    if picking_a_fight == "A":
        print("Level 1 monster arrives")
        print("Duke will fight with the monster")
        print("The level 1 monsters have 3hp")
        level_1_monster = 3
        while player.hp > 0 and level_1_monster > 0:
            damage = random.randint(1,3)
            print(damage)
            level_1_monster -= damage
            damage = random.randint(1,2)
            player.hp -= damage
            print("When lvl1 monster attack player will lose", damage)
            print("Whoever's hp reached to 0 will lose the game")

            if player.hp <= 0:
                print("Lose")
                exit()
            elif level_1_monster <=0:
                print("You won!")
                return
        #Win
    if picking_a_fight == "B":
        print("Level 5 monster arrives")
        print("Duke will fight with the monster")
        print("The level 5 monsters have 3hp")
        level_5_monster = 6
        while player.hp > 0 and level_5_monster > 0:
            damage = random.randint(2,4)
            print(damage)
            level_5_monster -= damage
            damage = random.randint(2,3)
            player.hp -= damage
            print("When lvl5 monster attack player will lose", damage)
            print("Whoever's hp reached to 0 will lose the game")
            if player.hp <= 0:
                print("Lose")
                exit()
            elif level_5_monster <=0:
                print("You Won!")
                return
