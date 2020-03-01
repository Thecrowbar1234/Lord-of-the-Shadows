import time
from Resources import NOICE as os
#a is money, b is potions, c is the weapon list, d is the weapon ATK stats, e is weapon price, f is armor names, g is armor def stats, h is armor price
#j is weaponID
def firstShop(a,b,c,d,e,f,g,h,j,k) :
  dog = 1
  while dog == 1 : 
    os.clear()
    print("You have $",a)
    message = ['An old shopkeeper croaks what would you like to buy today traveler? He pulls out an enormous bug with blades, horns, and even a human body, sticking out the side.' , 'he is selling a ' , '1.Flint lock pistol ; does 3 damage                       $30','2.Mossberg 500 ; does 4 damage                            $35' , '3.Gunsword ; does 4 damage                                $35','4.Crossbow ; does 4 damage                                $30',"5.Ivory hook ; does 5 damage                              $75","6.Iron armor ; has 2 defense                              $20","7.Steel armor ; has 2 defense                             $20 ","8.Potions of healing heal ; 5 health                       $5","9.Leave the store"]
    for cokelines in message :
      os.state(cokelines)
      time.sleep(.2)
    print()
    doo = int(input())
    if doo == 1 :
      if e[12] > a :
        os.clear()
        os.state('you do not have enough money to buy that!')
        input("Press enter to continue")
      else:
        os.clear()
        os.state("Are you sure you want to buy that?")
        os.state("It costs $" + str(e[12]) + ".")
        os.state("It does " + str(d[12]) + " damage.")
        os.state("Your weapon is a "+ c[j] + '.')
        os.state("It does " + str(d[j]) + " damage.")
        os.state("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          os.clear()
          a = a - 30
          os.state("You bought the flint lock pistol.")
          j = 12
          os.state("Your weapon is a " + c[j])
          os.state("It does " + str(d[12]) + " damage.")
          os.state("You have $" + str(a) + ".")
          input("Press enter to continue")
        elif buy == 0 :
          os.clear()
          os.state("Okay")
          input("Press enter to continue")
    elif doo == 2 :
      if e[11] > a :
        os.clear()
        os.state("You do not have enough money to buy that!")
        input("Press enter to continue")
      else :
        os.clear()
        os.state("Are you sure you want to buy that?")
        os.state("It costs $" + str(e[11]) + ".")
        os.state("It does " + str(d[11]) + " damage.")
        os.state("Your weapon is a " + c[j] + ".")
        os.state("It does " + str(d[j]) + " damage.")
        os.state("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          os.clear()
          a = a - 35
          os.state("You bought the mossberg 500.")
          j = 11
          os.state("Your weapon is a " + c[j] + ".")
          os.state("It does " + str(d[j]) + " damage.")
          os.state("You have $" + str(a) + ".")
          input("Press enter to continue")
        elif buy == 0 :
          os.clear()
          os.state("Okay")
          input("Press enter to continue")
    elif doo == 3 :
      if e[10] > a :
        os.clear()
        os.state(" You do not have enough that!")
        input("Press enter to continue")
      else :
        os.clear()
        os.state("Are you sure you want to buy that?")
        os.state("It costs $" + str(e[10]))
        os.state("It does " + str(d[10]) + " damage")
        print("Your weapon is a ",c[j])
        print("Your weapon does ",d[j]," damage")
        print("You have $",a)
        os.state("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          os.clear()
          a = a - 35
          os.state("You bought the Gunsword")
          j = 10
          print("Your weapon is a ",c[j])
          print("It does ",d[j]," damage")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          os.state("Okay")
          input("Press enter to continue")
    elif doo == 4 :
      if e[13] > a :
        os.clear()
        os.state(" You do not have enough that!")
        input("Press enter to continue")
      else :
        os.clear()
        os.state("Are you sure you want to buy that?")
        print("It costs $",e[13])
        print("It does ",d[13]," damage")
        print("Your weapon is a ",c[j])
        print("Your weapon does ",d[j]," damage")
        print("You have $",a)
        os.state("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          os.clear()
          a = a - 30
          os.state("You bought the Crossbow")
          j = 13
          print("Your weapon is a ",c[j])
          print("It does ",d[j]," damage")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          os.state("Okay")
          input("Press enter to continue")
    elif doo == 5 :
      if e[33] > a :
        os.clear()
        os.state("You do not have enough money to buy that!")
        input("Press enter to continue")
      else :
        os.clear()
        os.state("Are you sure you want to buy that?")
        print("It costs $",e[33])
        print("It does ",d[33]," damage")
        print("Your weapon is ",c[j])
        print("It does ",d[j]," damage")
        os.state("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          os.clear()
          a = a - 75
          os.state("You bought the Ivory hook")
          j = 33
          print("Your weapon is a ",c[j])
          print("It does ",d[j]," damage")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          os.clear()
          os.state("Okay")
          input("Press enter to continue")
    elif doo == 6 :
      if h[1] > a :
        os.clear()
        os.state("You do not have enough money to buy that!")
        input("Press enter to continue")
      else :
        os.clear()
        os.state("Are you sure you want to buy that?")
        print("It costs $",h[1])
        print("It has ",g[1]," defense")
        print("Your armor is ",f[k])
        print("It has ",g[k]," defense")
        os.state("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          os.clear()
          a = a - 20
          os.state("You bought the Iron armor")
          k = 1
          print("Your armor is ",f[k])
          print("It has ",g[k]," defense")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          os.clear()
          os.state("Okay")
          input("Press enter to continue")
    elif doo == 7 :
      if h[2] > a :
        os.clear()
        os.state("You do not have enough money to buy that!")
        input("Press enter to continue")
      else :
        os.clear()
        os.state("Are you sure you want to buy that?")
        print("It costs $",h[2])
        print("It has ",g[2]," defense")
        print("Your armor is ",f[k])
        print("It has ",g[k]," defense")
        os.state("1 for yes 0 for no")
        buy = int(input())
        if buy == 1 :
          os.clear()
          a = a - 20
          os.state("You bought the Steel armor")
          k = 2
          print("Your armor is ",f[k])
          print("It has ",g[k]," defense")
          print("You have $",a)
          input("Press enter to continue")
        elif buy == 0 :
          os.clear()
          os.state("Okay")
          input("Press enter to continue")
    elif doo == 8 :
      os.clear()
      os.state("How many would you like?")
      potions2 = int(input())
      q = potions2 * 5
      if q > a :
        os.clear()
        os.state("You cannot afford that")
        input("Press enter to continue")
      else :
        os.clear()
        b = b + potions2
        a = a - q
        print("You have ",b,"potions")
        input("Press enter to continue")
    elif doo == 9 :
      os.state("Thank you")
      input("Press enter to continue")
      return(j,a,k,b)
