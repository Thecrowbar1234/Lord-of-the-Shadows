#we use os.clear() now instead of clear() because os.clear() is better
import random
import math
import time
from Resources import NOICE as os
from colors import colors
from Resources import battle
from Resources import Shop
print("\033[0;36;20m")
os.clear()
message =["______________________________________________________",'|                                                    |',"|                         []                         |","|                         []                         |","|                       ------                       |","|                        |^^|                        |","|                        |^^|                        |","|                        |^^|                        |","|                        |^^|                        |","|                        |^^|                        |","|                        \^^/                        |",'|                         \/                         |',"|____________________________________________________|"]
for cokelines in message :
  print(cokelines)
  time.sleep(.7)
print("\033[1;34;20m")
os.state("                   Dungeon of Shadows")
time.sleep(2)
os.state("   Made by Thecrowbar1234, datacom88, and itsmelucas")
time.sleep(1)
input("                Press enter to continue")
os.clear()
print("\033[1;31;20m")
os.state('*Disclaimer: It is recommended that you get a pen and paper to keep track of your character stats, money, items, etc')
print("\033[0;36;20m")
os.state("Enter your name")
Character_Name = input()
if Character_Name == 'abcdefghijklmnopqrstuvwxyz' :
  Character_Name = "alphabet"
elif Character_Name == 'JacobTeslaDude' :
  Character_Name = 'Phillip'
  print('your name has been changed to Phillip')
elif Character_Name == 'Jacob Peters' :
  Character_Name = 'Phillip'
  print('your name has been changed to Phillip')
elif Character_Name == 'Jacob' :
  Character_Name = 'Phillip'
  print('your name has been changed to Phillip')
elif Character_Name == 'Kevin Xu' :
  Character_Name = 'Kevin the god of this world, the greatest person that ever existed'
elif Character_Name == 'Matthew Walley' :
  Character_Name = 'Matthew the Arbiter of justice in this world'
elif Character_Name == 'Edward Elric' :
  Character_Name = 'Fullmetal Alchemist'
elif Character_Name == 'Evil' :
  Character_Name = 'Pierce Hawthorne'
elif Character_Name == 'Keanu Reeves' :
  Character_Name = 'No your breathtaking!'
elif Character_Name == 'pop music' :
  Character_Name = 'the root of all pain and suffering in this world'
elif Character_Name == 'Eric Parsons':
  Character_Name = 'E-reader'
elif Character_Name == 'Carson Dunn' :
  Character_Name = 'reeeeeeeeeeeeee'
elif Character_Name == 'Yariel Lara' :
  Character_Name = 'Croikey'
elif Character_Name == 'George Mutrie' :
  Character_Name = 'Gorge'
elif Character_Name == 'Lucas Stucky' :
  Character_Name = 'The Creator of the great Monty'
os.clear()
money = 30
Weapons = ["Greatsword","Staff","Scimitar","bow","beer mug","katana","Battle-axe","warhammer","Magic Staff","Hidden blade","Gunsword","Mossberg 500","Flint lock pistol","crossbow","Sword of Arcus","Spear of hope","Demon wind shuriken","kunai knife","The katana of horus","Axe of Jörmungandr","Trident of Poseidon","Kampe's Scimitar","Leviathan sword","Leviathan bow","Leviathan fang","Sword of Yin","Prison wine","Scimitar of Draconis","Dragon sword","Dragon bow","Dragon tooth","Sword of Yang","Fire whiskey", "Mjölnir", " Radioactive Vodca" , "Ivory hook","Developers sword(only meant for Developers)","Excalibur","Sword of σκορπισμένη φωτιά","Bow of σκορπισμένη φωτιά","Knife of σκορπισμένη φωτιά","Sword of Yin and Yang","Black molohov" ,"un boligrafo morado","chaotic AK-47","The One Ring","AK-47"]
#35
Armor = ["Leather armor","Iron armor","Steel armor","Armor of Arcus","Samuri armor","Armor of Horus","Leviathan armor","Dragon armor",'Titainium armor', 'Armor of the Divine', 'UnderArmor', 'Armor of the Unstable',"Armor of Achilles"]
armorDEFstats = [1,2,2,2,3,3,3,4,4,3,3,1,4]
weaponATKstats = [4,3,3,2,2,3,4,4,4,4,4,4,3,3,5,5,5,5,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,5,69000,7,8,8,8,8,8,10,8,10,5]
armorPrices = [10,20,20,'earned through exploration',30,'earned through exploration','earned through exploration','earned through exploration',100,'earned through exploration',50,1,"ete"]
weaponPrices = [35,30,30,25,25,30,35,35,35,35,35,35,30,30,"earned through exploration","earned through exploration",40,50,'earned through exploration',"earned through exploration",'earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration',"ete","ete",'earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration',75,"non attainable","ete","ete","ete","ete","ete","earned in the special limited edition christmas lootbox!","ete",40]
WeaponEffects = [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,3,0,0,2,3,3,2,2,2,2,2,2,1,1,1,1,1,1,3,3,0,4,3,4,4,4,4,4,0,4,0]
Classes = ["Choose your class","1 for Drunkard. A lighthearted warrior, loves to sing, has 200% Blood alcohol level, also mutters that back then the alcohol they drank was %20000 pure alcohol, has random twiches, weapon of choice: beer mug. Stats: 6atk, 3def, 25hp, 6spd" , "2 for Paladin. A brave and mighty warrior, does leg day. his abs have abs, although he is incredibly stupid. weapon of choice: Greatsword, and shield. Stats: 5atk, 5def, 27hp, 3spd" , "3 for Elf. A boastful high-class hero, bathes in caviar and thinks he's better than you, and is also kind of a D#&%. weapon of choice: bow. Stats: 8atk, 2def, 24hp, 6spd" , "4 for mage. Super old and super mean also hates people. weapon of choice: Magic staff, and book of spells. Stats: 10atk, 0def, 25hp, 6spd" , "5 for Dwarf. his beard is longer than his hammer, even his wife has a beard. weapon of choice: warhammer. Stats: 2atk, 8def, 28hp, 2spd" , "6 for Monk. never talks ever. he doesn't eat. he doesn't sleep. he doesn't even use the bathroom. weapon of choice: staff Stats: 7atk, 3def, 24hp, 7spd" , "7 for pirate. A swash buckling, wife stealing, scoundrel of a man, randomly prays to jack sparrow. weapon of choice: scimitar, flint-lock pistol. Stats: 7atk, 3def, 25hp, 6spd" , "8 for Viking. under all his beard and his hair his skin is blue, he might be one of the blue man group, always mutters that if you start trying to baptize him he'll swing his axe down on you. weapon of choice: war axe Stats: 7atk, 3def, 25hp, 5spd" , "9 for Samurai. If you utter the word ninja he will kill you. the only way to get him to stop bugging you is to sho gun. weapon of choice: katana. Stats 7atk, 4def, 25hp, 4spd" , "10 for Assassin, not much is known about him. He walks in the dead of night unsean. Is Ialian. You don't know why. His last name is Auditore, you think you have heard of him. weapon of choice: Hidden blade. Stats: 9atk, 1def, 23hp, 10spd" , "11 for Demolitionist, is concerningly destructive, constantly blows things up, your 76% sure you saw him try to kiss fire. weapon of choice: Shotgun, grenade. Stats: 7atk, 2def, 27hp, 5spd"]
for cokelines in Classes :
  os.state(cokelines)
  print()
  time.sleep(0.2)
print()
classAtkStats = [6,5,8,10,4,7,7,7,7,9,8]
classDefStats = [3,5,2,0,3,3,3,3,4,1,2]
classHpStats = [25,27,24,24,28,24,25,25,25,23,27]
classSpdStats = [6,3,6,6,2,7,6,5,4,1,2]
ClassName = ['Drunkard','Paladin','Elf','Mage','Dwarf','Monk','Pirate','Viking','Samurai','Assassin','Demolitionist']
ClassWep = [4,0,3,8,7,1,2,6,5,9,11]
classCritStats = [5,3,15,4,6,20,2,4,6,10,5]
characterClassNum = int(input()) - 1
characterClass = ''
characterATK = classAtkStats[characterClassNum]
characterDEF = classDefStats[characterClassNum]
characterHP = classHpStats[characterClassNum]
characterSPD = classSpdStats[characterClassNum]
characterClass = ClassName[characterClassNum]
weaponID = ClassWep[characterClassNum]
characterCritChance = classCritStats[characterClassNum]
os.clear()
if Character_Name == '--|dev{kevin}]/' or Character_Name == '--|dev{matthew}]/' or Character_Name == '--|dev{lucas}]/' or Character_Name == 'test2289' :
  weaponID = 36
  originalHealth = characterHP
  characterDEF = 6900
  characterSPD = 6900
  characterHP = 690000000
  character_Class = 'Dev'
#delete after the game is released
characterStats = [characterATK," attack,",characterDEF," defense,",characterHP," health points,",characterSPD," speed"]
weapon = (Weapons[weaponID])
weaponATK = (weaponATKstats[weaponID])
os.state("Your name is" + " " + Character_Name + ".")
if characterClassNum == 10 or characterClassNum == 3 :
  os.state("Your class is an" + " " + characterClass)
else :
  os.state("Your class is a" + " " + characterClass)
os.state("you have" + " " + str(characterStats[0]) + " " + characterStats[1] + " " + str(characterStats[2]) + " " + characterStats[3] + " " + str(characterStats[4]) + " " + characterStats[5] + " " + str(characterStats[6]) + " " + characterStats[7] + ".")
os.state("Your weapon is a "+ weapon + ", it does" + " " + str(weaponATK) + " damage.")
originalATK = characterATK
#is a constant
armorID = 0
effect = WeaponEffects[weaponID]
os.state("Your armor is " + Armor[armorID] + ".")
os.state("It has " + str(armorDEFstats[armorID]) + " defense.")
originalDEF = characterDEF
characterDEF = characterDEF + armorDEFstats[armorID]
characterATK = characterATK + weaponATK
input("Press enter to continue")
os.clear()
os.state('You push open the door to the Inn of the Sows Ear and step out of the searing afternoon sun. The inn is cool and dark. You are greeted with a friendly wave from the innkeeper, and hard stares from the other patrons. ')
#character descriptions 
#if class = 'Archer' then print('') else print('A rugged and tanned elf is sitting by the fireplace. ')
os.state("You walk up to the bar and order a mug of Souten wine. You strike up a conversation with the barkeeper, and manage to get him talking about Lord Cadwell. \" Aye, the Lord's the richest man in these parts. He works his serfs hard, but knows how to throw a fine summer festival. Why I remember, seven summers ago, he served whole legs of lamb smothered in herbs of provence. Why, that was a fine spread, almost as good as twelve summers ago, when...\" You are saved from the gustatory rememberances of the barkeep by the entrance of a sharp looking gentleman in fine clothes. He returns the hard looks of the other patrons with a searching look of his own. You try to ignore his glance. He approaches and says, \" Are you " + Character_Name + "? The great " + characterClass + " decided you should be the leader of this rabble.\" Then he addresses the entire bar. \"My name is Cyrus, high steward to his highness Lord Cadwell. All you adventurers, follow me to the Private suite behind the bar, lord cadwell has a proposition for you.\" You follow the others into the private suite. Inside you see a dark-haired middle-aged man, wealding a hailberd, and a shadow-like figure in the corner, and finally the man himself lord Cadwell, an old tough, blond man. A long, thin scar runs down the side of his face like a river, and abruptly stops at the beginng of his chin. A broad smile spreads across his face as he begins to describe his proposition. I require your services, I recently purchased a ruin, it hasn\'t properly been dated, but its probably somewhat recent, lord cadwell says reassuringly. And as you already know, i\'ve selected you, " + Character_Name + " to lead the team i\'ve assembled, the women in the corner is, suddenly the dark haired man chimes in, \" cut the crap old man!, what\'s this job paying?\" Cyrus exclaims, obviosly trying to hold back anger \" sir  you may not adress lord cadw-,\" \n \" that\'s enough cyrus, well i guess i\'ll start with that muscular gentleman over there, gesturing to the dark hared man, that\'s chrom, the hailberd is his weapon of choice.\" , and that shadowed figure in the corner is kerrigan, her weapon of choice is throwing daggers, and a crossbow, gesturing to the polished oak-wood crossbow in her hands,  and finally, my good steward, Cyrus. \" \" sir, i'm just a servent, i'm not fit for exploration \" \" Cyrus, you won't be exploring, just tagging along, to make sure they follow through with the contract,\"wah\" - cyrus pauses,\"ok, i'll go\".  \"good then it's settled you'll leave imnettiatly\"")
input("Press enter to continue")
os.clear()
potions1 = 10
os.clear()
os.state("But first, would you like to buy something?")
input("Press enter to continue")
dog = 1
oh = 0
shopresults = Shop.firstShop(money,potions1,Weapons,weaponATKstats,weaponPrices,Armor,armorDEFstats,armorPrices,weaponID,armorID)
weaponID = shopresults[0]
money = shopresults[1]
armorID = shopresults[2]
characterDEF = originalDEF
potions1 = shopresults[3]
characterDEF = characterDEF + armorDEFstats[armorID]
characterATK = originalATK
characterATK = characterATK + weaponATKstats[weaponID]
os.clear()
os.state("Lord Cadwell leads you to what looks like a renovated shack. He leads you down to the basement, and shows you the entrance to the basement.\n\"This is where you will explore\" he points to a door. Your senses tell you not to go in, but you heard the pay so you do not object. After you go through the doorway, you hear an explosion. You run toward the way you came from. and you see a crumble. You pick out an item from the rubble, and you find a burnt read stick.")
os.state("\"Dynamite,\" you whisper to yourself. You realize that this was all a way for Lord cadwell to get rid of nusciances. You were a rogue who inspired the fears of many villagers. Chrom is a person who hated cadwell, but you are not sure about cyrus and kerrigan.")
way = int(input("You reach a fork in the path. Which way do you go?\n\n1. Left\n2. Right\n"))
os.clear()
if way == 1 :
  os.state("You walk for about 30 minutes, and you reach a door. You push through and find yourself in a massive cavern. The creatures look at you hostily, and the ground is covered with the remains who werent as fortunate.")
  os.state("Suddenly, a wolf runs up to you and attacks you.")
  input("Press enter to continue")
  os.clear()
  enemieHP = random.randint(36,45)
  enemieATK = random.randint(8,11)
  enemieSPD = random.randint(3,10)
  originalHealth = characterHP
  battleresult = battle.battle(characterATK,characterDEF,characterHP,characterSPD,characterCritChance,enemieATK,enemieHP,enemieSPD,potions1,money,originalHealth,effect)
  potions1 = battleresult[1]
  characterHP = battleresult[0]
  os.state("You have " + str(potions1) + " potions.")
  os.state("You have " + str(characterHP) + " HP.")
  money = battleresult[2]
  os.state("You have $" + str(money) + '.')
  input("Press enter to continue")
  os.clear()
  os.state("The animals back off, knowing they cannot win with a frontal assault.")
  os.state("You find a potion in the wolfs hide.")
  potions1 = potions1 + 1
  os.state("You have "+ str(potions1) + " potions.")
  input("Press enter to continue")
  os.clear()
  while way == 1 :
    os.state("You and the group arrive at a comfortable looking rock. You set up camp there. After being reinvigorated by sleep, you decide you must explore. There are 3 routes you can take, which pne do you take?")
    way2 = int(input("1. Left\n2.right\n3.middle\n"))
    os.clear()
    if way2 == 1 :
      os.state("You arrive at what looks to be a fort, though it is abandoned. You walk in and find the remains of what looks like soldiers. You find a potion of healing in a chest. You find a path. Which way do you go?")
      way3 = int(input("1.Left\n2.Right\n"))
      if way3 == 1 :
        os.clear()
        os.state("You find a tower and climb up it. You walk up to find an AK-47.")
        os.state("It has " + str(weaponATKstats[46]) + " Damage.")
        os.state("Your Weapon is a " + Weapons[weaponID] + ".")
        os.state("Your weapon has " + str(weaponATKstats[weaponID]) + " Damage.")
        choice = int(input("1 for yes 0 for no\n"))
        if choice == 1 :
          os.clear()
          os.state("Your Weapon is an AK-47.")
          os.state("It has " + str(weaponATKstats[46]) + " Damage.")
          characterATK = originalATK
          weaponID = 46
          characterATK += weaponATKstats[weaponID]
          input("Press enter to continue")
          os.clear()
      elif way3 == 2 :
        os.state("You turn around the corner to see the zombified remains of a soldier. Suddenly the soldier turns toward you and attacks you.")
        input("Press enter to continue")
        enemieHP = random.randint(36,45)
        enemieATK = random.randint(8,11)
        enemieSPD = random.randint(3,10)
        originalHealth = characterHP
        battleresult = battle.battle(characterATK,characterDEF,characterHP,characterSPD,characterCritChance,enemieATK,enemieHP,enemieSPD,potions1,money,originalHealth,effect)
        potions1 = battleresult[1]
        characterHP = battleresult[0]
        os.state("You have " + str(potions1) + " potions.")
        os.state("You have " + str(characterHP) + " HP.")
        money = battleresult[2]
        os.state("You have $" + str(money) + '.')
        input("Press enter to continue")
    elif way2 == 2 :
      os.state("You find a cave. Strangely, it has a lock on it so you cannot enter.")
      input("Press enter to continue")
    elif way2 == 3 :
      os.state("You find a stairwell into the underground.")
      os.state("You find a few wolves gaurding what looks like a chest. You try to get the chest, but the wolves stop you and growle.")
