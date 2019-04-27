import random

class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"The {self.name} deals {self.power} damage to the {enemy.name}.")
        if enemy.health > 0:
            print(f"The {enemy.name} now has {enemy.health} health.")
        elif enemy.health <= 0:
            print(f"The {enemy.name} is dead.")
            self.proceed()
    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")
    def nothing(self, enemy):
        self.health -= enemy.power
        print(f"The {self.name} cowers in fear and lets the {enemy.name} deal {enemy.power} damage.")
        if self.health == 0:
            print("You died!")
            exit()
    def proceed(self):
        print("What do you want to do now?")
        print("1. Venture off the land")
        print("2. Go home")
        choice1 = int(input("> "))
        if choice1 == 1:
            print("A goblin has appeared!")
            you.main()
        if choice1 == 2:
            print("You managed to return home safely. Now it\'s time to rest....")
            exit()

class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power) ## super(works here too)

class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)



you = Hero('hero', random.randint(15, 20), random.randint(10, 15))
goblin = Goblin('goblin', random.randint(10, 15), random.randint(5, 15))

# hero.health()
# hero.attack(goblin)
# goblin.attack(hero)


print("You, the hero, wakes up from a deep slumber and suddenly a goblin heads towards your direction!")

def main():

    while goblin.alive() and you.alive():
        print(f"The {you.name} has {you.health} health and {you.power} power.")
        print(f"The {goblin.name} has {goblin.health} health and {goblin.power} power.\n")
        print("What do you want to do?")
        print("1. Fight goblin")
        print("2. Do nothing")
        print("3. Flee")
        choice = int(input("> "))
        if choice == 1:
            you.attack(goblin)
        if choice == 2:
            you.nothing(goblin)
            if you.health <= 0:
                print("You died!")
        if choice == 3:
            print("You flee.")
            you.proceed()

main()

