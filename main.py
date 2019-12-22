#Kevin- when are you going to be on?
import os
import random
import math
import time
from replit import clear
print("Enter your name")
Character_Name = input()
if Character_Name == 'abcdefghijklmnopqrstuvwxyz' :
  Character_Name = "alphabet"
elif Character_Name == 'Jacob Peters' :
  Character_Name = 'Phillip'
elif Character_Name == 'Kevin Xu' :
  Character_Name = 'Kevin the god of this world, the greatest person that ever existed'
elif Character_Name == 'Matthew Walley' :
  Character_Name = 'Matthew the Arbiter of justice in this world'
elif Character_Name == 'Edward Elric' :
  Character_Name = 'Fullmetal Alchemist'
elif Character_Name == 'Evil' :
  Character_Name = 'Pierce Hawthorne'
Classes = ["Choose your class","1 for the Drunkered. A lighthearted warrior, loves to sing, has 200% Blood alcohol level, also mutters that back then the alcohol they drank was %20000 pure alcohol, has random twiches, weapon of choice: beer mug. Stats: 6atk, 3def, 25hp, 6spd" , "2 for the Paladin. A brave and mighty warrior, does leg day. his abs have abs, although he is incredibly stupid. weapon of choice: Longsword, and shield. Stats: 5atk, 5def, 27hp, 3spd" , "3 for Elf. A boastful high-class hero, bathes in caviar and thinks he's better than you, and is also kind of a D#&%. weapon of choice: longbow. Stats: 8atk, 2def, 24hp, 6spd" , "4 for mage. Super old and super mean also hates people. weapon of choice: wand, and book of spells. Stats: 10atk, 0def, 25hp, 6spd" , "5 for Dwarf. his beard is longer than his hammer, even his wife has a beard. weapon of choice: warhammer. Stats: 2atk, 8def, 28hp, 2spd" , " 6 for Monk. never talks ever. he doesn't eat. he doesn't sleep. he doesn't even use the bathroom. weapon of choice: bare hands. Stats: 7atk, 3def, 24hp, 7spd" , "7 for pirate. A swash buckling, wife stealing, scoundrel of a man, randomly prays to jack sparrow. weapon of choice: scimitar, flint-lock pistol. Stats: 6atk, 3def, 25hp, 6spd" , " 8 for Viking. before he kills something he always yells for odin, always mutters that if you start trying to baptize him he'll swing his axe down on you. weapon of choice: hand axe, short sword. Stats: 7atk, 3def, 25hp, 5spd" , "9 for Samurai. If you utter the word ninja he will kill you. the only way to get him to stop bugging you is to sho gun. weapon of choice: katana. Stats 7atk, 4def, 25hp, 4spd" , "10 for Assassin, not much is known about him. weapon of choice: Hidden blade. Stats: 9atk, 0def, 23hp, 10spd"]
#line 10-61 is how the computer decides what class you are, it takes a number, then assigns you stats
clear()
money = 30
Weapons = ["Greatsword","Staff","Scimitar","bow","beer mug","katana","waraxe","warhammer","Magic Staff","Hidden blade"]
weaponATKstats = [4,3,3,2,2,3,4,4,3,3]
for cokelines in Classes :
  print(cokelines)
  print()
  time.sleep(0.4)
print()
characterClassNum = int(input())
characterClass = ''
if characterClassNum == 1 :
  characterATK = 6
  characterDEF = 3
  characterHP = 25
  characterSPD = 6
  characterClass = 'Drunkered'
  weaponID = 4
  characterCritChance = 5
elif characterClassNum == 2 :
  characterATK = 5
  characterDEF = 5
  characterHP = 27
  characterSPD = 3
  characterClass = 'Paladin'
  characterCritChance = 3
  weaponID = 0
elif characterClassNum == 3 :
  characterATK = 8
  characterDEF = 2
  characterHP = 24
  characterSPD = 6
  characterClass = 'Elf'
  characterCritChance = 15
  weaponID = 3
elif characterClassNum == 4 :
  characterATK =  10
  characterDEF = 0
  characterHP = 24
  characterSPD = 6
  characterClass = 'Mage'
  characterCritChance = 4
  weaponID = 8
elif characterClassNum == 5 :
  characterATK = 4
  characterDEF = 3
  characterHP = 28
  characterSPD = 2
  characterClass = 'Dwarf'
  weaponID = 7
  characterCritChance = 6
elif characterClassNum == 6 :
  characterATK = 7
  characterDEF = 3
  characterHP = 24
  characterSPD = 7
  characterClass = 'Monk'
  weaponID = 1
  characterCritChance = 20
elif characterClassNum == 7 :
  characterATK = 6
  characterDEF = 3
  characterHP = 25
  characterSPD = 6
  characterClass = 'Pirate'
  weaponID = 2
  characterCritChance = 6
elif characterClassNum == 8 :
  characterATK = 7
  characterDEF = 3
  characterHP = 25
  characterSPD = 5
  characterClass = 'Viking'
  weaponID = 6
  characterCritChance = 4
elif characterClassNum == 9 :
  characterATK = 7
  characterDEF = 4
  characterHP = 25
  characterSPD = 4
  weaponID = 5
  characterClass = 'Samurai'
  characterCritChance = 6
elif characterClassNum == 10 :
  characterATK = 9
  characterDEF = 0
  characterHP = 23
  characterSPD = 10
  characterClass = 'Assassin'
  weaponID = 9
  #Kevin - changed it to assasin because viking and barabrian had too similar stats and in history they similar
  characterCritChance = 10
clear()
characterStats = [characterATK," attack,",characterDEF," defense,",characterHP," health points,",characterSPD," speed"]
weapon = (Weapons[weaponID])
weaponATK = (weaponATKstats[weaponID])
print("Your name is ",Character_Name)
if characterClassNum == 10 or characterClassNum == 3 :
  print('your class is an ' , characterClass)
else :
  print("Your class is a ",characterClass)
print("You have",characterStats)
print("Your weapon is a ",weapon,", it does ",weaponATK," damage.")
originalATK = characterATK
#is a constant
characterATK = characterATK + weaponATK
randomClassNum = random.randint(1,10)
partyMember2class = ''
partyMember3class = ''
partyMember4class = ''
partyMember2Name = ''
partyMember3Name = ''
partyMember4Name = ''
def setPartyMemberClass(x,y,z) :
  if x == 1 :
    z = 'Drunkered'
    y = 'Barney'
  elif x == 2 :
    z = 'Paladin'
    y = 'Lancelot'
  elif x == 3 :
    z = 'Elf'
    y = 'Legolas'
  elif x == 4 :
    z = 'mage'
    y = 'Gandalf'
  elif x == 5 :
    z = 'dwarf'
    y = 'Gimly'
  elif x == 6 :
    z = 'monk'
    y = 'Aang'
  elif x == 7 :
    z = 'pirate'
    y = 'Blackbeard'
  elif x == 8 :
    z = 'viking'
    y = 'Hiccup, the hiccup in his life'
  elif x == 9 :
    z = 'Samuri'
    y = 'Hanzo'
  else:
    z = 'Assassin'
    y = 'Ezio'
  return(z,y)
partyMember2class = setPartyMemberClass(randomClassNum,partyMember2Name,partyMember2class)
randomClassNum = random.randint(1,10)
partyMember3class  = setPartyMemberClass(randomClassNum,partyMember3Name,partyMember3class)
randomClassNum = random.randint(1,10)
partyMember4class = setPartyMemberClass(randomClassNum,partyMember4Name,partyMember4class)
message = ["Your partymembers are","a/n",partyMember2class,"a/n",partyMember3class,"a/n",partyMember4class]
for cokelines in message :
  print(cokelines)
  time.sleep(0.4)
input("Press enter to continue")
clear()
partyMembers = 4
print('The land of Asирияkлда is one that has been taken over by an evil overlord who is only known by the lord of the shadows, and you and your party set out to bring an end to his regime.')
input("Press enter to continue")
clear()
mi = 0
enemieATK = random.randint(7,11)
enemieHP = random.randint(35,45)
enemieSPD = random.randint(2,9)
potions1 = 10
temporary = 1
# have stats add up to 35
# all enimie stats should add up to 25 atk well 30 becaus ethere are 2 enimes ok yeah that b
#the enemie group is only as fast a their fastest person
#they should be grouped into one person
potions = 0
#def battle(characterStats are first four parmeters,enemie stats are the other three)
# a =characteratk, b = characterDef, c = characterhp, d = character spd, e = enemie atk, h = crit chance f = enemie hp, g = enemie spd 2 chages = 1 sp attack which is 3a 
def battle(a,b,c,d,h,e,f,g,potions,money1):
  clear()
  enemieCharge = 0
  charge = 0
  #-----------------------------------------------------------
  if d >= g :
    while f > 0 or c > 0 :
      clear()
      if c <= 0 :
        print("You suck")
        return()
      print("You have ",c," HP")
      print("Your opponent has ",f," HP")
      print("Your charge is ",charge)
      message = ["Choose:","","1. Attack","2. Heal up","3. Charge up special attack"]
      for cokelines in message :
        print(cokelines)
        time.sleep(.4)
      print()
      characterTurn = int(input())
      clear()
      if characterTurn == 1 :
        Chance1 = random.randint(1,h)
        if charge == 2 :
          a = a + a + a
          if Chance1 == 1 :
            a = a + 10
          print('You use your special charge attack, it does ' , a , 'Dmg')
          f = f - a
          if Chance1 == 1 :
            a = a - 10
          a = a / 3
          charge = 0
        elif Chance1 == 2 :
          print("You miss your attack")
          if charge == 2 :
            charge = 0
        else :
          if Chance1 == 1 :
            a = a + 10
          print('you attack, it does ' , a , 'Dmg')
          f = f - a
          if Chance1 == 1 :
            a = a - 10
      elif characterTurn == 2 :
        if potions == 0 :
          print("You don't have any potions.")
        else :
          c = c + 5
          print('you drink a health potion, it heals 5HP')
          potions = potions - 1
          print("You have ",potions," potions of healing")
      elif characterTurn == 3 :
        charge = charge + 1
        print("You charge up an attack")
        if charge >= 2 :
          charge = 2 
      input("Press enter to continue")
      clear()
      enemieTurn = random.randint(1,3)
      #enemie turn -----------------------------------------------------------
      if f <= 0 :
        print("You didn't lose")
        addition = random.randint(3,10)
        print("You earned $",addition)
        money1 = money1 + addition
        input("Press enter to continue")
        return(c,potions,money1)
      if enemieTurn == 1 :
        chance = random.randint(1,15)
        if enemieCharge == 2 :
          e = e + e + e
          if chance == 1 :
            e = e + 10
          print("The enemie uses their special charge attack, it does " , e, "Dmg")
          c = c - e
          if chance == 1 :
            e = e - 10
            e = e / 3
          enemieCharge = 0
        elif chance == 2 :
          print("The enemie misses their attack")
          if enemieCharge == 2 :
            enemieCharge = 0
        else :
          if chance == 1 :
            e = e + 10
          print('They attack, it does ' , e , 'Dmg')
          c = c - e
          if chance == 1 :
            e = e - 10
        if not chance == 2 :
          c = c + b
          print("You blocked ",b,"points of damage")
      elif enemieTurn == 2 :
        f = f + 5
        print("They healed up")
      elif enemieTurn == 3 :
        enemieCharge = enemieCharge + 1
        print("The enemie charges an attack")
        if enemieCharge >= 2 :
          enemieCharge = 2
      input("Press enter to continue")
  #- -----------------------------------------------------------
  elif d < g :
    while f > 0 or c > 0 :
      if f <= 0 :
        print("You didn't lose")
        addition = random.randint(3,10)
        print("You earned $",addition)
        money1 = money1 + addition
        input("Press enter to continue")
        return(c,potions,money1)
      enemieTurn = random.randint(1,3)
      if enemieTurn == 1 :
        chance = random.randint(1,15)
        if enemieCharge == 2 :
          e = e + e + e
          if chance == 1 :
            e = e + 10
          print("The enemie uses their special charge attack, it does " , e, "Dmg")
          c = c - e
          if chance == 1 :
            e = e - 10
            e = e / 3
          enemieCharge = 0
        elif chance == 2 :
          print("The enemie misses their attack")
          if enemieCharge == 2 :
            enemieCharge = 0
        else :
          if chance == 1 :
            e = e + 10
          print('They attack, it does ' , e , 'Dmg')
          c = c - e
          if chance == 1 :
            e = e - 10
        if not chance == 2 :
          c = c + b
          print("You blocked ",b,"points of damage")
      elif enemieTurn == 2 :
        f = f + 5
        print("They healed up")
      elif enemieTurn == 3 :
        enemieCharge = enemieCharge + 1
        print("The enemie charges an attack")
        if enemieCharge >= 2 :
          enemieCharge = 2
      input("Press enter to continue")
      clear()
      #enemie turn -----------------------------------------------------------
      if c <= 0 :
        print("You suck")
        return()
      print("You have ",c," HP")
      print("Your opponent has ",f," HP")
      print("Your charge is ",charge)
      message = ["Choose:","","1. Attack","2. Heal up","3. Charge up special attack"]
      for cokelines in message :
        print(cokelines)
        time.sleep(.4)
      print()
      characterTurn = int(input())
      clear()
      if characterTurn == 1 :
        Chance1 = random.randint(1,h)
        if charge == 2 :
          a = a + a + a
          if Chance1 == 1 :
            a = a + 10
          print('You use your special charge attack, it does ' , a , 'Dmg')
          f = f - a
          if Chance1 == 1 :
            a = a - 10
          a = a / 3
          charge = 0
        elif Chance1 == 2 :
          print("You miss your attack")
          if charge == 2 :
            charge = 0
        else :
          if Chance1 == 1 :
            a = a + 10
          print('you attack, it does ' , a , 'Dmg')
          f = f - a
          if Chance1 == 1 :
            a = a - 10
      elif characterTurn == 2 :
        if potions == 0 :
          print("You don't have any potions.")
        else :
          c = c + 5
          print('you drink a health potion, it heals 5HP')
          potions = potions - 1
          print("You have ",potions," potions of healing")
      elif characterTurn == 3 :
        charge = charge + 1
        print("You charge up an attack")
        if charge >= 2 :
          charge = 2 
      input("Press enter to continue")
      clear()
      enemieTurn = random.randint(1,3)
battleresult = battle(characterATK,characterDEF,characterHP,characterSPD,characterCritChance,enemieATK,enemieHP,enemieSPD,potions1,money)
potions1 = battleresult[1]
characterHP = battleresult[0]
print("you have ",potions1," potions")
print("You have ",characterHP, "HP")
money = battleresult[2]
print("You have $",money)
#we can start the story
#battle system is complete
