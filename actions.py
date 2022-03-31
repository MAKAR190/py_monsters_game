# Game actions here
from termcolor import cprint
def attack(hero, monsters):
    option = input('''
    What attack do you want to use: 
    1 - default attack
    2 - super
    ''')
    if option == '1':
        for monster in monsters:
             monster.hp = monster.hp - hero.damage
             hero.hp =  hero.hp  - monster.damage
             if monster.hp <= 0:
                monsters.remove(monster)
                if len(monsters) > 0:
                  cprint(f"You beated one monster ({monster.name})! {len(monsters)} monsters left!", "blue")
                  break
                elif len(monsters) <=0:
                  cprint("Congratulations! You beated all monsters!", "blue")
                  break
             elif len(monsters) > 0 and monster.hp > 0 and hero.hp > 0: 
                  print("Keep going!")
                  break
    elif option == '2':
         if hero.superLimit > 0:
          for monster in monsters:
               monster.hp = monster.hp - hero.damage * 5
               hero.hp = hero.hp - monster.damage
               hero.superLimit = hero.superLimit - 1
               if monster.hp <= 0:
                  monsters.remove(monster)
                  if len(monsters) > 0:
                   cprint(f"You beated one monster ({monster.name})!  {len(monsters)} monsters left!", "blue")
                   break
                  elif len(monsters) <=0:
                   cprint("Congratulations! You beated all monsters!", "blue")
                   break
               elif len(monsters) > 0 and monster.hp > 0 and hero.hp > 0: 
                  print("Keep going!")
                  break
         else:
           cprint("Your super has ended!", "red")     
    else:
     cprint("Nie wiem...", "red")