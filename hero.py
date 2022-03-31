# Generate your hero
from termcolor import cprint
class Hero:
    def __init__(self, name, hp, damage, superLimit):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.superLimit = superLimit
    
def generate_hero():
 error = True
 while error:
   try: 
    name = input("Name: ")
    if len(name) <=0:
        cprint("You need to give normal name for your hero...", "red") 
        error = True
    else:    
     hp = int(input("Health: "))
     damage = int(input("Damage: "))
     superLimit = 3
     hero = Hero(name, hp, damage, superLimit)
     error = False
     return hero
   except ValueError:
       error = True
       cprint("You entered not number in health/damage input...", "red")
        
