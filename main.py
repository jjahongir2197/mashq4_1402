import random

class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, enemy):
        damage = random.randint(1, self.power)
        enemy.hp -= damage
        print(f"{self.name} {enemy.name}ga {damage} zarba berdi")

class Game:
    def start(self):
        p = Character(input("Qahramon: "), 100, 20)
        e = Character("Dragon", 120, 15)

        while p.hp > 0 and e.hp > 0:
            p.attack(e)
            if e.hp <= 0:
                print("Siz yutdingiz!")
                break
            e.attack(p)
            if p.hp <= 0:
                print("Yutqazdingiz!")

Game().start()
