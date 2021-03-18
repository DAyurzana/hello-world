#section_3
#Duke Ayurzana
#2/25/2021
#CSS 225
import random
from main_character import player
def start():
    print("Duke battling with the higher levels of enemies, and he has been training a lot and earned good amount of epxeriences")
    print("Heartless monsters hunting around survivors camp.")
    print("Lots of people terrified and hoping that monsters would leave soon.")
    print("Duke will stand against the strongest monsters.")
    print("Boss monster arrives")
    print("Duke will fight with the mightiest monster")
    print("The Boss monsters has 20hp")
    boss_monster = 15
    player.hp = 25
    while player.hp > 0 and boss_monster > 0:
        damage = random.randint(3, 5)
        print(damage)
        boss_monster -= damage
        print("When the Boss monster attack player will lose", damage)
        if boss_monster <= 0:
            print("You won!")
            return
        damage = random.randint(3, 5)
        player.hp -= damage
        print("Whoever's hp reached to 0 will lose the game", player.hp)

        if player.hp <= 0:
            print("Lose")
            exit()
