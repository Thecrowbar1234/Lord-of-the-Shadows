import random
import time
from Resources import NOICE as os
def battle(a,b,c,d,h,e,f,g,potions,money1,ohealth,fx):
  stun = 1
  roun = 3
  Chance1 = 2
  os.clear()
  characterTurn = 2
  os.state("Looks like you got yourself in a battle")
  input("Press enter to continue")
  enemieCharge = 0
  charge = 0
  eOHealth = f
  #-----------------------------------------------------------
  if d >= g :
    while f > 0 or c > 0 :
      os.clear()
      if c <= 0 :
        os.state("Your dead, ha ha!")
        return()
      Chance1 = 1
      os.state("You have " + str(c) + " HP")
      os.state("Your opponent has " + str(f) + " HP")
      os.state("Your charge is " + str(charge))
      message = ["Choose:","","1. Attack","2. Heal up","3. Charge up special attack"]
      for cokelines in message :
        os.state(cokelines)
        time.sleep(.2)
      print()
      characterTurn = int(input())
      os.clear()
      if characterTurn == 1 :
        Chance1 = random.randint(1,h)
        if charge == 2 :
          a = a + a + a
          if Chance1 == 1 :
            a = a + 10
          os.state('You use your special charge attack, it does ' + str(a) + ' Dmg')
          f = f - a
          if Chance1 == 1 :
            a = a - 10
          a = a / 3
          charge = 0
        elif Chance1 == 2 :
          os.state("You miss your attack")
          if charge == 2 :
            charge = 0
        else :
          if Chance1 == 1 :
            a = a + 10
          os.state('you attack, it does ' + str(a) + ' Dmg')
          f = f - a
          if Chance1 == 1 :
            a = a - 10
      elif characterTurn == 2 :
        #put in later
        if potions == 0 :
          os.state("You don't have any potions.")
        else :
          m = c + 5
          if m > ohealth :
            s = ohealth - c
            os.state("You healed " + str(s) + " HP")
            c = ohealth
          else:
            c = c + 5
            os.state('you drink a health potion, it heals 5HP')
          potions = potions - 1
          print("You have " + str(potions) + " potions of healing")
          Chance1 = 2
      elif characterTurn == 3 :
        charge = charge + 1
        Chance1 = 2
        os.state("You charge up an attack")
        if charge >= 2 :
          charge = 2 
      input("Press enter to continue")
      os.clear()
      enemieTurn = random.randint(1,3)
      #enemie turn -----------------------------------------------------------
      q = c
      roun = roun + 1
      if characterTurn == 1 and not Chance1 == 2 :
        roun = 1
      if fx == 4 :
        stun = 1
        if roun < 3 :
          f = f - 4
          os.state("The enemie burned from black fire, it did 5 damage")
      elif fx == 3 :
        stun = 1
        if not Chance1 == 2 and characterTurn == 1 :
          stun = random.randint(1,3)
      elif fx == 2 :
          if roun < 3 :
            os.state("The enemie took withering damage, it did 1 damage")
            f = f - 1
      elif fx == 1 :
        if roun < 3 :
          os.state("The enemie took burn damage, it did 1 damage")
          f = f - 1
      else :
        os.clear()
      if f <= 0 :
        os.state("You didn't lose")
        addition = random.randint(3,10)
        os.state("You earned $" + str(addition))
        money1 = money1 + addition
        input("Press enter to continue")
        return(c,potions,money1)
      if stun == 2 :
        os.state("The enemie was struck by lightning")
        os.state("The enemie was stunned")
        os.state("They took 1 damage")
        f = f - 1
      elif c < 16 or enemieCharge == 2 :
        chance = random.randint(1,15)
        if enemieCharge == 2 :
          e = e + e + e
          if chance == 1 :
            e = e + 10
          os.state("The enemie uses their special charge attack, it does " + str(e) + " Dmg")
          c = c - e
          if chance == 1 :
            e = e - 10
          e = e / 3
          enemieCharge = 0
        elif chance == 2 :
          os.state("The enemie misses their attack")
          if enemieCharge == 2 :
            enemieCharge = 0
        else :
          if chance == 1 :
            e = e + 10
          os.state('They attack, it does ' + str(e) + ' Dmg')
          c = c - e
          if chance == 1 :
            e = e - 10
        if not chance == 2 :
          c = c + b
          if q <= c :
            os.clear()
            c = q
            os.state("You blocked the attack")
          else :
            os.state("You blocked " + str(b) + " points of damage")
      elif f < 16 :
        w = f + 5
        if w > eOHealth :
          f = eOHealth
        else :
          f = f + 5
        os.state("They healed up")
      elif f > 20 :
        enemieCharge = enemieCharge + 1
        os.state("The enemie charges an attack")
        if enemieCharge >= 2 :
          enemieCharge = 2
      input("Press enter to continue")
  #- -----------------------------------------------------------
  elif d < g :
    while f > 0 or c > 0 :
      if f <= 0 :
        os.state("You didn't lose")
        addition = random.randint(3,10)
        os.state("You earned $" + str(addition))
        money1 = money1 + addition
        input("Press enter to continue")
        return(c,potions,money1)
      enemieTurn = random.randint(1,3)
      q = c
      roun = roun + 1
      if characterTurn == 1 and not Chance1 == 2 :
        roun = 1
      if fx == 4 :
        stun = 1
        if roun < 5 :
          f = f - 5
          os.state("The enemie burned from black fire, it did 5 damage")
      elif fx == 3 :
        stun = 1
        if Chance1 == 1 or characterTurn == 1 :
          stun = random.randint(1,3)
      elif fx == 2 :
          if roun < 3 :
            os.state("The enemie took withering damage, it did 1 damage")
            f = f - 1
      elif fx == 1 :
        if roun < 3 :
          f = f - 1
        else :
          os.state("The enemie stopped burning")
      else :
        os.clear()
      if f <= 0 :
        os.state("You didn't lose")
        addition = random.randint(3,10)
        os.state("You earned $" + str(addition))
        money1 = money1 + addition
        input("Press enter to continue")
        return(c,potions,money1)
      if stun == 2 :
        os.state("The enemie was struck by lightning")
        os.state("The enemie was stunned")
        os.state("They took 1 damage")
        f = f - 1
      elif c > 16 or enemieCharge == 2 :
        chance = random.randint(1,15)
        if enemieCharge == 2 :
          e = e + e + e
          if chance == 1 :
            e = e + 10
          os.state("The enemie uses their special charge attack, it does " + str(e) + " Dmg")
          c = c - e
          if chance == 1 :
            e = e - 10
          e = e / 3
          enemieCharge = 0
        elif chance == 2 :
          os.state("The enemie misses their attack")
          if enemieCharge == 2 :
            enemieCharge = 0
        else :
          if chance == 1 :
            e = e + 10
          os.state('They attack, it does ' + str(e) + ' Dmg')
          c = c - e
          if chance == 1 :
            e = e - 10
        if not chance == 2 :
          c = c + b
          if q <= c :
            os.clear()
            c = q
            os.state("You blocked the attack")
          else :
            os.state("You blocked " + str(b) + " points of damage")
      elif f < 16 :
        w = f + 5
        if w > eOHealth :
          f = eOHealth
        else :
          f = f + 5
        os.state("They healed up")
      elif f > 20 :
        enemieCharge = enemieCharge + 1
        os.state("The enemie charges an attack")
        if enemieCharge >= 2 :
          enemieCharge = 2
      input("Press enter to continue")
      os.clear()
      if c <= 0 :
        os.state("Your dead, ha ha!")
        return()
      Chance1 = 1
      os.state("You have " + str(c) + " HP")
      os.state("Your opponent has " + str(f) + " HP")
      os.state("Your charge is " + str(charge))
      message = ["Choose:","","1. Attack","2. Heal up","3. Charge up special attack"]
      for cokelines in message :
        os.state(cokelines)
        time.sleep(.2)
      print()
      characterTurn = int(input())
      os.clear()
      if characterTurn == 1 :
        Chance1 = random.randint(1,h)
        if charge == 2 :
          a = a + a + a
          if Chance1 == 1 :
            a = a + 10
          os.state('You use your special charge attack, it does ' + str(a) + ' Dmg')
          f = f - a
          if Chance1 == 1 :
            a = a - 10
          a = a / 3
          charge = 0
        elif Chance1 == 2 :
          os.state("You miss your attack")
          if charge == 2 :
            charge = 0
        else :
          if Chance1 == 1 :
            a = a + 10
          os.state('you attack, it does ' + str(a) + ' Dmg')
          f = f - a
          if Chance1 == 1 :
            a = a - 10
      elif characterTurn == 2 :
        #put in later
        if potions == 0 :
          os.state("You don't have any potions.")
        else :
          m = c + 5
          if m > ohealth :
            s = ohealth - c
            os.state("You healed " + str(s) + "HP")
            c = ohealth
          else:
            c = c + 5
            os.state('you drink a health potion, it heals 5HP')
          potions = potions - 1
          os.state("You have " + str(potions) + " potions of healing")
        Chance1 = 2
      elif characterTurn == 3 :
        charge = charge + 1
        os.state("You charge up an attack")
        if charge >= 2 :
          charge = 2 
        Chance1 = 2
      input("Press enter to continue")
      os.clear()
