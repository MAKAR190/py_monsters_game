# Main file with game input options

from hero import generate_hero
from monsters_generate import get_monsters_list, additional_monsters
from actions import attack
from termcolor import cprint, colored
cprint("Generate your hero: ", "green")
hero = generate_hero()
cprint("Generate monsters: ", "green")
monster = get_monsters_list()
additional_monsters(monster)
while hero.hp > 0 and len(monster.children) > 0:
    attack(hero, monster.children)
if hero.hp > 0 and len(monster.children) <=0:
    cprint("You won!", "green")
if hero.hp <= 0:
    cprint("You lost!", "red")