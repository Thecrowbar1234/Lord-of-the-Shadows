import random
import time
from replit import clear
def battle(a,b,c,d,h,e,f,g,potions,money1,ohealth,fx):
  roun = 3
  clear()
  print("Looks like you got yourself in a battle")
  enemieCharge = 0
  charge = 0
  eOHealth = e
  #-----------------------------------------------------------
  if d >= g :
    while f > 0 or c > 0 :
      clear()
      if c <= 0 :
        print("Your dead, ha ha!")
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
        #put in later
        if potions == 0 :
          print("You don't have any potions.")
        else :
          m = c + 5
          if m > ohealth :
            s = ohealth - c
            print("You healed ",s,"HP")
            c = ohealth
          else:
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
      q = c
      roun = roun + 1
      if characterTurn == 1 and not Chance1 == 1 :
        roun = 1
      if fx == 4 :
        stun = random.randint(1,3)
        if Chance1 == 1 or characterTurn == 2 or characterTurn == 3 :
          stun = 1
        if not roun == 3 :
          f = f - 2
          print("The enemie took burn and poison damage, it did 2 damage")
        else :
          print("The enemie stopped burning and the poison weared off")
      elif fx == 3 :
        stun = random.randint(1,3)
        if Chance1 == 1 or characterTurn == 2 or characterTurn == 3 :
          stun = 1
      elif fx == 2 :
          if not roun == 3 :
            print("The enemie took poison damage, it did 1 damage")
            f = f - 1
          else :
            print("The poison weared off")
      elif fx == 1 :
        if not roun == 3 :
          print("The enemie took burn damage, it did 1 damage")
          f = f - 1
        else :
          print("The enemie stopped burning")
      else :
        clear()
      if f <= 0 :
        print("You didn't lose")
        addition = random.randint(3,10)
        print("You earned $",addition)
        money1 = money1 + addition
        input("Press enter to continue")
        return(c,potions,money1)
      if stun == 2 :
        print("The enemie was stunned")
      elif enemieTurn == 1 :
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
          if q <= c :
            clear()
            c = q
            print("You blocked the attack")
          else :
            print("You blocked ",b,"points of damage")
      elif enemieTurn == 2 :
        w = f + 5
        if w > eOHealth :
          f = eOHealth
        else :
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
      q = c
      roun = roun + 1
      if characterTurn == 1 and not Chance1 == 1 :
        roun = 1
      if fx == 4 :
        stun = random.randint(1,3)
        if Chance1 == 1 or characterTurn == 2 or characterTurn == 3 :
          stun = 1
        if not roun == 3 :
          f = f - 2
          print("The enemie took burn and poison damage, it did 2 damage")
        else :
          print("The enemie stopped burning and the poison weared off")
      elif fx == 3 :
        stun = random.randint(1,3)
        if Chance1 == 1 or characterTurn == 2 or characterTurn == 3 :
          stun = 1
      elif fx == 2 :
          if not roun == 3 :
            print("The enemie took poison damage, it did 1 damage")
            f = f - 1
          else :
            print("The poison weared off")
      elif fx == 1 :
        if not roun == 3 :
          print("The enemie took burn damage, it did 1 damage")
          f = f - 1
        else :
          print("The enemie stopped burning")
      else :
        clear()
      if f <= 0 :
        print("You didn't lose")
        addition = random.randint(3,10)
        print("You earned $",addition)
        money1 = money1 + addition
        input("Press enter to continue")
        return(c,potions,money1)
      if stun == 2 :
        print("The enemie was stunned")
      elif enemieTurn == 1 :
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
          if q <= c :
            clear()
            c = q
            print("You blocked the attack")
          else :
            print("You blocked ",b,"points of damage")
      elif enemieTurn == 2 :
        w = f + 5
        if w > eOHealth :
          f = eOHealth
        else :
          f = f + 5
        print("They healed up")
      elif enemieTurn == 3 :
        enemieCharge = enemieCharge + 1
        print("The enemie charges an attack")
        if enemieCharge >= 2 :
          enemieCharge = 2
      input("Press enter to continue")
      clear()
      if c <= 0 :
        print("Your dead, ha ha!")
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
        #put in later
        if potions == 0 :
          print("You don't have any potions.")
        else :
          m = c + 5
          if m > ohealth :
            s = ohealth - c
            print("You healed ",s,"HP")
            c = ohealth
          else:
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
#please test for me
