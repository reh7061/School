from random import randint

# Basic turn-based game for school project. Jan 2024.

# Colors for aesthetic since it is a terminal based code.
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
reset = '\033[0m'

# Classes are not utilized in to it's full capacity & overlappings occurs
# such as Monster having methods in Player class due to skill issues.
class Lives:

  def __init__(self, n, h, d, g):
    self.name = n
    self.health = h
    self.damage = d
    self.gold = g
    self.inBattle = False

  def isDead(self):
    return self.health <= 0

  def reduceHealth(self, damage):
    self.health -= damage

  def viewStats(self):
    print("\nLevel: " + str(self.level) + green + " Health: " +
          str(self.health) + red + " Damage: " + str(self.damage) + yellow +
          " Gold: " + str(self.gold) + reset)


class Player(Lives):
  level = 1

  def __init__(self, name):
    super().__init__(name, 100, 10, 50)

  def heal(self):
    hp = int(input("\nHow much to heal? 1 HP = 3 Gold "))
    if self.gold >= hp * 3:
      self.gold -= hp * 3
      tmp = self.health
      self.health += hp
      print("\nYou now have " + yellow + str(self.gold) + " gold left.")
      print(green + "Health: " + red + str(tmp) + reset + " --> " + green +
            str(self.health) + reset + '\n')
      return True
    else:
      print(red + "\nYou don't have enough gold\n" + reset)
      return False

  def upgrade(self):
    dmg = int(input("\nHow many stats? +1 DMG = 10 Gold "))
    if self.gold >= dmg * 10:
      self.gold -= dmg * 10
      tmp = self.damage
      self.damage += dmg
      print('\n' + red + "Damage: " + green + str(tmp) + reset + " --> " +
            red + str(self.damage) + reset)
      print("You now have " + yellow + str(self.gold) + " gold left.\n" +
            reset)
    else:
      print("You dont have enough gold.")

  def attackMonster(self, monster, lessHP=False):
    if lessHP:
      self.inBattle = True
      print("You attacked the " + red + monster.name + reset)
      print("You did " + red + str(self.damage) + " DMG" + reset)
      monster.reduceHealth(self.damage)
      print("The " + red + monster.name + reset + " has " + green +
            str(monster.health) + " HP left" + reset)
      print("---------")
    else:
      self.inBattle = True
      print("You attacked the " + red + monster.name + reset)
      print("You did " + red + str(self.damage) + " DMG" + reset)
      monster.reduceHealth(self.damage)
      print("The " + red + monster.name + reset + " has " + green +
            str(monster.health) + " HP left" + reset)
      print("---------")

  def monsterAttack(self, monster, lesserHP=False):
    # Monster turn
    if lesserHP:
      self.inBattle = True
      print("The " + red + monster.name + reset + " attacks you and delt " +
            red + str(monster.damage) + " DMG" + reset)
      self.reduceHealth(self.health)
      print("You now have " + green + str(self.health) + " HP left\n" + reset)
    else:
      self.inBattle = True
      print("The " + red + monster.name + reset + " attacks you and delt " +
            red + str(monster.damage) + " DMG" + reset)
      self.reduceHealth(monster.damage)
      print("You now have " + green + str(self.health) + " HP left\n" + reset)

  def levelUp(self):
    self.level += 1
    self.damage += 1
    print("You leveled up to level " + str(plr.level))

  def getLevel(self):
    return self.level

  def hasWon(self):
    return (self.level >= 10 or self.gold >= 300)


def getMonsters():
  monsters = []
  monsters.append(Lives("Goblin", 20, 5, 10))
  monsters.append(Lives("Orc", 30, 8, 20))
  monsters.append(Lives("Dragon", 50, 15, 50))
  return monsters


plr = Player("Not Used")
mon = getMonsters()

print("Welcome, this is a turn-based game.\n")
print("Your goal is to reach LVL 10 or 300 Gold to win the game.\n")
print("Your current stats are: \nLevel: " + str(plr.level) + " Health: " +
      str(plr.health) + " Damage: " + str(plr.damage) + " Gold: " +
      str(plr.gold))

while True:
  done = False
  firstTime = True
  msg = False
  copyMonster = mon[randint(0, 2)]
  currentMonster = Lives(copyMonster.name, copyMonster.health,
                         copyMonster.damage, copyMonster.gold)

  if plr.isDead():
    print(red + "\nYou died. Game Over." + reset)
    print("You reached level " + str(plr.level) + " and had " + str(plr.gold) +
          " gold.")
    break

  if plr.hasWon():
    print(green + "\nYou won the game! Congrats.\n" + reset)
    break

  # Nested Loop
  while currentMonster.health > 0 and plr.health > 0:
    print("-------------------------------------------")
    if firstTime:
      print("You encountered an " + currentMonster.name + green +
            " (Not In Battle)\n" + reset)
      firstTime = False
    if not plr.inBattle:
      print("What do you want to do?")
    if plr.inBattle:
      print("What do you want to do? " + red + "(In Battle)" + reset)
    choice = input("1. Attack 2. Run 3. Heal 4. Upgrade 5. View Stats ")
    if choice == "1":
      print()
      # If dmg exceeds monster health, reduce by hp, else hp goes negative
      if plr.damage > currentMonster.health or currentMonster.damage > plr.health:
        plr.attackMonster(currentMonster, True)
        if not currentMonster.isDead():
          plr.monsterAttack(currentMonster, True)
      else:
        plr.attackMonster(currentMonster)
        if not currentMonster.isDead():
          plr.monsterAttack(currentMonster)
    elif choice == "2":
      # 50% chance to run away.
      if randint(1, 2) % 2 == 0:
        print(green + "\nYou ran away\n" + reset)
        plr.inBattle = False
        break
      else:
        print(red + "\nYou failed to flee\n" + reset)
        plr.monsterAttack(currentMonster)

    elif choice == "3":
      if plr.inBattle:
        if plr.heal():
          plr.monsterAttack(currentMonster)
      else:
        plr.heal()

    elif choice == "4":
      if not plr.inBattle:
        plr.upgrade()
      else:
        print(red + "\nCannot upgrade during battle" + reset)

    elif choice == "5":
      plr.viewStats()

    if currentMonster.isDead():
      plr.inBattle = False
      print("You won!")
      plr.gold += currentMonster.gold
      print("You got " + str(currentMonster.gold) + " gold")
      plr.levelUp()
