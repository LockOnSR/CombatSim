import random
min = 1
max = 20
import time

class Character:
    def __init__(self, name, level, health, armor, attack):
        self.name = name
        self.level = level
        self.health = health
        self.armor = armor
        self.attack = attack

class Monster:
    def __init__(self, monsterName, monsterLevel, monsterHealth, monsterArmor, monsterAttack):
        self.monsterName = monsterName
        self.monsterLevel = monsterLevel
        self.monsterHealth = monsterHealth
        self.monsterArmor = monsterArmor
        self.monsterAttack = monsterAttack

def attack(self, attack, monsterArmor, monsterHealth, health):
    self.attack = attack
    attack = random.randint(min, max)
    while monsterHealth > 0 or health > 0:
        if (monsterArmor > attack):
            print("The challenger barely missed!")
        elif (monsterArmor < attack):
            print("The challenger has struck the monster!")
            monsterHealth = -1
        else:
            print("The challenger barely missed the monster! So close yet so far!")
        if health == 0 or monsterHealth == 0:
            print("The round has ended!")

#Monster List#
Monster1 = Monster("Rat", 0, 1, 1, random.randint(min,max))
Monster2 = Monster("Zombie", 1, 3, 2, random.randint(min,max))
Monster3 = Monster("Ghoul", 2, 5, 5, random.randint(min,max))
Monster4 = Monster("PitMaster", 3, 10, 8, random.randint(min,max))
Monster5 = Monster("Lich", 5, 20, 10, random.randint(min,max))

print("Welcome to the Arena Challenge!")
time.sleep(1)
print()
print("The only way out is to survive the onslaught of Monsters!")
time.sleep(1)
print()
print("The rules are simple. If you roll the dice and the number is larger than the armor of the monster you hit! If the number is lower than you miss.")
time.sleep(1)
print()
print()
print("The first combatant to reach zero health loses")
time.sleep(2)

a = 0
y = 0
z = 0
x = 0
n = 0


print()
name = input("What is your Characters name? ")
time.sleep(2)

roundCount = 1+n
level = 1+a
health = 5+y
armor = 9+z
experience = 0+x
attack = attack

stats = [level, health, armor, experience, attack]

if experience == 3:
    print("Congrats you are now level 2")
    a = 1
    y = 3
    z = 1
if experience == 8:
    print("Congrats you are now level 3!")
    a = 2
    y = 6
    z = 2
if experience == 16:
    print("Congrats you are now MAX Level!")
    print("Time to take on the lich!")
    a = 3
    y = 9
    z = 3

print()
print()
print("Your Character", name,"starts at level", level,"with", health,"health and an armor of", armor)
time.sleep(1)
print()
print("During your challenege you can level up and get more health and armor")
print()
path = input("You now have three different choices: [B]egin a new challenege, [F]ight the Lich, and [Q]uit: ")
print()

while path == "Q":
    print("Come back", name,"when you feel you can take on the challenge!")
    time.sleep(2)
    quit


while path == "B" or path == "b":
    print("Good luck on your challenege")
    time.sleep(1)
    print("Round", roundCount ,":", name,"you best be ready!") 
    print("Your current stats are: ")
    time.sleep(1)
    print("Level:", level, "Health:", health, "Armor:", armor)
    time.sleep(1)

    if roundCount == 1:
        print("The monster you'll find this round is...", Monster1.monsterName,"The monster is level:", Monster1.monsterLevel, "With a health of:", Monster1.monsterHealth, "And an armor score of:", Monster1.monsterArmor)
    if roundCount == 2:
        print("The monster you'll find this round is...", Monster2.monsterName,"The monster is level:", Monster2.monsterLevel, "With a health of:", Monster2.monsterHealth, "And an armor score of:", Monster2.monsterArmor)
    if roundCount == 3:
        print("The monster you'll find this round is...", Monster3.monsterName,"The monster is level:", Monster3.monsterLevel, "With a health of:", Monster3.monsterHealth, "And an armor score of:", Monster3.monsterArmor)
    if roundCount == 4:
        print("The monster you'll find this round is...", Monster4.monsterName,"The monster is level:", Monster4.monsterLevel, "With a health of:", Monster4.monsterHealth, "And an armor score of:", Monster4.monsterArmor)
    if roundCount == 5 or path == "F" or path == "f":
        print("The monster you'll find this round is...", Monster5.monsterName,"The monster is level:", Monster5.monsterLevel, "With a health of:", Monster5.monsterHealth, "And an armor score of:", Monster5.monsterArmor)
        Print()
        time.sleep(1)
        print("This is the Final Boss... Good Luck Challenger!")

    time.sleep(1)
    print("Time to fight! Let's see who goes first!")
    time.sleep(1)
    speed = random.randint(min, max)
    print()
    monsterSpeed = random.randint(min, max)
    
    
    if (monsterSpeed < speed):
        Character.attack(attack)
    



    if roundCount == 5:
        print("Congrats! You have won all 5 Rounds and are the Arena Grand Champion!")
        print()
        time.sleep(1)
        print("Come back and challenge the arena again sometime!")
        print()
        time.sleep(1)
        restart = input(print("Want to (p)lay again now? or time bask in your (g)lory for a while?"))
        time.sleep(1)

        if restart == "p" or restart == "P":
            n = 0
            a = 0
            y = 0
            x = 0
            z = 0
        if restart == "g" or restart == "G":
            time.sleep(1)
            print("Go bask in your glory champuion!")
            time.sleep(1)
            print("Come back when you're ready to defend your title!")
            time.sleep(1)
            quit
