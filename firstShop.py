import time
from replit import clear

#a is money, b is potions, c is the weapon list, d is the weapon ATK stats, e is weapon price, f is armor names, g is armor def stats, h is armor price
#j is weaponID

def firstShop(a,b,c,d,e,f,g,h,j,k) :
  dog = 1
  while dog == 1 : 
    clear()
    print("You have $",a)
    message = ['An old shopkeeper croaks what would you like to buy today traveler? He pulls out an enormous bug with blades, horns, and even a human body, sticking out the side.' , 'he is selling a ' , '1.Flint lock pistol ; does 3 damage                       $30','2.Mossberg 500 ; does 4 damage                            $35' , '3.Gunsword ; does 4 damage                                $35','4.Crossbow ; does 4 damage                                $30',"5.Ivory hook ; does 5 damage                              $75","6.Iron armor ; has 2 defense                              $20","7.Steel ; armor has 2 defense                             $20 ","8.Potions of healing heal ; 5 health                       $5","9.Leave the store"]
    for cokelines in message :
      print(cokelines)
      time.sleep(.4)
    print()
    doo = int(input())
    if doo == 1 :
      if e[12] > a :
        clear()
        print('you do not have enough money to buy that!')
        input("Press enter to continue")
      else:
        clear()
        print("Are you sure you want to buy that?")
        print("It costs $",e[12])
        print("It does ", d[12]," damage")
        print("Your weapon is a ",c[j])
        print("It does ",d[j]," damage")
        print("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          clear()
          a = a - 30
          print("You bought the flint lock pistol")
          j = 12
          print("Your weapon is a ",c[j])
          print("It does ",d[12]," damage")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          clear()
          print("Okay")
          input("Press enter to continue")
    elif doo == 2 :
      if e[11] > a :
        clear()
        print("You do not have enough money to buy that!")
        input("Press enter to continue")
      else :
        clear()
        print("Are you sure you want to buy that?")
        print("It costs $",e[11])
        print("It does ",d[11]," damage")
        print("Your weapon is ",c[j])
        print("It does ",d[j]," damage")
        print("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          clear()
          a = a - 35
          print("You bought the mossberg 500")
          j = 11
          print("Your weapon is a ",c[j])
          print("It does ",d[j]," damage")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          clear()
          print("Okay")
          input("Press enter to continue")
    elif doo == 3 :
      if e[10] > a :
        clear()
        print(" You do not have enough that!")
        input("Press enter to continue")
      else :
        clear()
        print("Are you sure you want to buy that?")
        print("It costs $",e[10])
        print("It does ",d[10]," damage")
        print("Your weapon is a ",c[j])
        print("Your weapon does ",d[j]," damage")
        print("You have $",a)
        print("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          clear()
          a = a - 35
          print("You bought the Gunsword")
          j = 10
          print("Your weapon is a ",c[j])
          print("It does ",d[j]," damage")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          print("Okay")
          input("Press enter to continue")
    elif doo == 4 :
      if e[13] > a :
        clear()
        print(" You do not have enough that!")
        input("Press enter to continue")
      else :
        clear()
        print("Are you sure you want to buy that?")
        print("It costs $",e[13])
        print("It does ",d[13]," damage")
        print("Your weapon is a ",c[j])
        print("Your weapon does ",d[j]," damage")
        print("You have $",a)
        print("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          clear()
          a = a - 30
          print("You bought the Crossbow")
          j = 13
          print("Your weapon is a ",c[j])
          print("It does ",d[j]," damage")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          print("Okay")
          input("Press enter to continue")
    elif doo == 5 :
      if e[33] > a :
        clear()
        print("You do not have enough money to buy that!")
        input("Press enter to continue")
      else :
        clear()
        print("Are you sure you want to buy that?")
        print("It costs $",e[33])
        print("It does ",d[33]," damage")
        print("Your weapon is ",c[j])
        print("It does ",d[j]," damage")
        print("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          clear()
          a = a - 75
          print("You bought the Ivory hook")
          j = 33
          print("Your weapon is a ",c[j])
          print("It does ",d[j]," damage")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          clear()
          print("Okay")
          input("Press enter to continue")
    elif doo == 6 :
      if h[1] > a :
        clear()
        print("You do not have enough money to buy that!")
        input("Press enter to continue")
      else :
        clear()
        print("Are you sure you want to buy that?")
        print("It costs $",h[1])
        print("It has ",g[1]," defense")
        print("Your armor is ",f[k])
        print("It has ",g[k]," defense")
        print("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          clear()
          a = a - 20
          print("You bought the Iron armor")
          k = 1
          print("Your armor is ",f[k])
          print("It has ",g[k]," defense")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          clear()
          print("Okay")
          input("Press enter to continue")
    elif doo == 7 :
      if h[2] > a :
        clear()
        print("You do not have enough money to buy that!")
        input("Press enter to continue")
      else :
        clear()
        print("Are you sure you want to buy that?")
        print("It costs $",h[2])
        print("It has ",g[2]," defense")
        print("Your armor is ",f[k])
        print("It has ",g[k]," defense")
        print("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          clear()
          a = a - 20
          print("You bought the Steel armor")
          k = 2
          print("Your armor is ",f[k])
          print("It has ",g[k]," defense")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          clear()
          print("Okay")
          input("Press enter to continue")
    elif doo == 8 :
      clear()
      print("How many would you like?")
      potions2 = int(input())
      q = potions2 * 5
      if q > a :
        clear()
        print("You cannot afford that")
        input("Press enter to continue")
      else :
        clear()
        b = b + potions2
        a = a - q
        print("You have ",b,"potions")
        input("Press enter to continue")
    elif doo == 9 :
      print("Thank you")
      input("Press enter to continue")
      return(j,a,k,b)
