# Generate monster class here
from termcolor import cprint, colored
class Monster:
    def __init__(self, name, hp, damage, children):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.children = children
def generate_monster():
  error = True
  while error:
   try: 
    name = input("Name: ")
    if len(name) <=0:
     cprint("You need to give normal name for your monster...", "red") 
     error = True
    else:
     hp = int(input("Health: "))
     damage = int(input("Damage: "))
     monster = Monster(name, hp, damage, [])
     error = False
     return monster
   except ValueError:
    error = True
    cprint("You entered not number in health/damage input...", "red")
def get_monsters_list():
  error = True
  while error:
   try: 
    monsters = []
    monster = generate_monster() 
    quantity = int(input(colored("How many: ", "blue")))
    i = 0
    while i < quantity:
        monsters.append(monster)
        i+=1
    monster.children.extend(monsters)
    print(monster.children)
    error = False
    return monster
   except ValueError:
    error = True
    cprint("You entered not number in quantity input...", "red")

def additional_monsters(monster):
    add_monsters = ""
    while add_monsters.lower() != 'n':
     add_monsters = input(colored("Do you want to add another type of monster?(Y/N)", "blue"))
     if add_monsters.lower() == "n":
        break
     elif add_monsters.lower() == 'y':
      new_monsters = get_monsters_list()
      monster.children.extend(new_monsters.children)
     else:
        cprint("Don't understand you...", 'red') 
    return monster
    





