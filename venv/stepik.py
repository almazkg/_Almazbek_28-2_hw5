class Team:
    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def info(self):
         return f'Name:{self.__name} position: {self.__position}'


class Player(Team):
    def __int__(self, name, number, stats):
        super().__init__(name, number, stats)
        self.__stats = stats

    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, new_stats):
        self.__stats = new_stats








import random


class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, boss):
        boss.health -= self.damage


class HeroBomber(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def die(self, boss):
        boss.health -= 100


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def attack(self, boss):
        if random.random() < 0.3:  # 30% chance to stun the boss
            print(f"{self.name} stunned the boss!")
        else:
            super().attack(boss)


class Boss:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, hero):
        hero.health -= self.damage


hero1 = HeroBomber("Hero Bomber", 100, 20)
hero2 = Thor("Thor", 120, 18)
boss = Boss("Boss", 500, 50)

while True:
    print(f"{hero1.name} attacks {boss.name}")
    hero1.attack(boss)
    if boss.health <= 0:
        print(f"{hero1.name} defeats {boss.name}!")
        break

    print(f"{hero2.name} attacks {boss.name}")
    hero2.attack(boss)
    if boss.health <= 0:
        print(f"{hero2.name} defeats {boss.name}!")
        break

    print(f"{boss.name} attacks {hero1.name}")
    boss.attack(hero1)
    if hero1.health <= 0:
        print(f"{boss.name} defeats {hero1.name}!")
        hero1.die(boss)  # if Hero Bomber dies, the boss takes additional damage
        break

    print(f"{boss.name} attacks {hero2.name}")
    boss.attack(hero2)
    if hero2.health <= 0:
        print(f"{boss.name} defeats {hero2.name}!")
        break













position = 2
name = ('David')
print(name)
number = (23)
print(number)
#position = ('midfielder')
#print(position)
print(Team.info())








