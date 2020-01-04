#please test the battle choose the weapons that have effects to see if they work (see on line 70) I was tired and I didnt feel like testing it now
#I also one the geo bee
import random
import math
import time
from colors import colors
from Resources import battle
from Resources import firstShop
print("\033[0;36;20m")
from replit import clear
# my dad is an ELA major so I asked him to help me write a story, and the one he came up with is much better. He gave me the jist of the start, but he will need a couple more days to finish the outline. I put what he's got so far in a file on the project
#cool, once hes done we can start making the rest
clear()
message =["______________________________________________________",'|                                                    |',"|                         []                         |","|                         []                         |","|                       ------                       |","|                        |^^|                        |","|                        |^^|                        |","|                        |^^|                        |","|                        |^^|                        |","|                        |^^|                        |","|                        \^^/                        |",'|                         \/                         |',"|____________________________________________________|"]
for cokelines in message :
  print(cokelines)
  time.sleep(1)
print("\033[1;34;20m")
print("                  Lord of the Shadows")
time.sleep(2)
print("           Made by Thecrowbar1234 and datacom88")
time.sleep(1)
input("                Press enter to continue")
clear()
print("\033[1;31;20m")
print('*Disclaimer: It is recommended that you get a pen and paper to keep track of your character stats, money, items, etc')
print("\033[0;36;20m")
print("Enter your name")
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
clear()
money = 30
Weapons = ["Greatsword","Staff","Scimitar","bow","beer mug","katana","Battle-axe","warhammer","Magic Staff","Hidden blade","Gunsword","Mossberg 500","Flint lock pistol","crossbow","Sword of Аркус","Spear of пророчество","Demon wind shuriken","kunai knife","The katana of horus","Axe of Jörmungandr","Trident of Посейдон","левиафан sword","левиафан bow","левиафан fang","левиафан katana","Prison wine","Дракон sword","Дракон bow","Дракон tooth","Дракон katana","Fire whiskey", "Mjölnir", " Radioactive Vodca" , "Ivory hook","Developers sword(only meant for Developers)","Sword of a million Truths"]
#34
Armor = ["Leather armor","Iron armor","Steel armor","Armor of Аркус","Samuri armor","Armor of Horus","левиафан armor","Дракон armor",'Titainium armor', 'Armor of the божественный', 'UnderArmor', 'Armor of the неустойчивый']
armorDEFstats = [1,2,2,2,3,3,3,4,4,3,3,1]
weaponATKstats = [4,3,3,2,2,3,4,4,4,4,4,4,3,3,4,5,5,5,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,5,69000,6]
armorPrices = [10,20,20,'earned through exploration',30,'earned through exploration','earned through exploration','earned through exploration',100,'earned through exploration',50,1]
weaponPrices = [35,30,30,25,25,30,35,35,35,35,35,35,30,30,"earned through exploration","earned through exploration",40,50,'earned through exploration',"earned through exploration",'earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration','earned through exploration',75,"non attainable","ete"]
WeaponEffects = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,3,2,2,2,2,2,1,1,1,1,1,3,3,0,4,4]
Classes = ["Choose your class","1 for the Drunkard. A lighthearted warrior, loves to sing, has 200% Blood alcohol level, also mutters that back then the alcohol they drank was %20000 pure alcohol, has random twiches, weapon of choice: beer mug. Stats: 6atk, 3def, 25hp, 6spd" , "2 for the Paladin. A brave and mighty warrior, does leg day. his abs have abs, although he is incredibly stupid. weapon of choice: Longsword, and shield. Stats: 5atk, 5def, 27hp, 3spd" , "3 for Elf. A boastful high-class hero, bathes in caviar and thinks he's better than you, and is also kind of a D#&%. weapon of choice: longbow. Stats: 8atk, 2def, 24hp, 6spd" , "4 for mage. Super old and super mean also hates people. weapon of choice: Magic staff, and book of spells. Stats: 10atk, 0def, 25hp, 6spd" , "5 for Dwarf. his beard is longer than his hammer, even his wife has a beard. weapon of choice: warhammer. Stats: 2atk, 8def, 28hp, 2spd" , " 6 for Monk. never talks ever. he doesn't eat. he doesn't sleep. he doesn't even use the bathroom. weapon of choice: bare hands. Stats: 7atk, 3def, 24hp, 7spd" , "7 for pirate. A swash buckling, wife stealing, scoundrel of a man, randomly prays to jack sparrow. weapon of choice: scimitar, flint-lock pistol. Stats: 7atk, 3def, 25hp, 6spd" , " 8 for Viking. under all his beard and his hair his skin is blue, he might be one of the blue man group, always mutters that if you start trying to baptize him he'll swing his axe down on you. weapon of choice: hand axe, short sword. Stats: 7atk, 3def, 25hp, 5spd" , "9 for Samurai. If you utter the word ninja he will kill you. the only way to get him to stop bugging you is to sho gun. weapon of choice: katana. Stats 7atk, 4def, 25hp, 4spd" , "10 for Assassin, not much is known about him. weapon of choice: Hidden blade. Stats: 9atk, 1def, 23hp, 10spd"]
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
  characterClass = 'Drunkard'
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
  characterATK = 7
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
  characterDEF = 1
  characterHP = 23
  characterSPD = 10
  characterClass = 'Assassin'
  weaponID = 9
  characterCritChance = 10
clear()
if Character_Name == '--|dev{kevin}]/' or Character_Name == '--|dev{matthew}]/' or Character_Name == 'test2289' :
  weaponID = 34
  originalHealth = characterHP
  characterDEF = 6900
  characterSPD = 6900
  characterHP = 690000000
  character_Class = 'Dev'
#delete after the game is released
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
armorID = 0
effect = WeaponEffects[weaponID]
print("Your armor is ",Armor[armorID])
print("It has ",armorDEFstats[armorID]," defense")
originalDEF = characterDEF
characterDEF = characterDEF + armorDEFstats[armorID]
characterATK = characterATK + weaponATK
input("Press enter to continue")
clear()
print('You push open the door to the Inn of the Sows Ear and step out of the searing afternoon sun. The inn is cool and dark. You are greeted with a friendly wave from the innkeeper, and hard stares from the other patrons. ')
#character descriptions 
#if class = 'Archer' then print('') else print('A rugged and tanned elf is sitting by the fireplace. ')
print('You walk up to the bar and order a mug of Souten wine. You strike up a conversation with the barkeep, and manage to get him talking about Lord Cadwell. "Aye, the Lord''s the richest man in these parts. He works his serfs hard, but knows how to throw a fine summer festival. Why I remember, seven summers ago, he served whole legs of lamb smothered in herbs of provence. Why, that was a fine spread, almost as good as twelve summers ago, when... You are saved from the gustatory rememberances of the barkeep by the entrance of a sharp looking gentleman in fine clothes. He returns the hard looks of the other patrons with a searching look of his own. You try to ignore his glance. He approaches and says, "I''ve decided you should be the leader of this rabble." Then he addresses the entire bar. "My name is Cyrus, high steward to his grace Lord Cadwell. All you adventurers, follow me to the Private suite behind the bar, lord cadwell has a proposition for you." You follow the others into the private suite. ' )
input("Press enter to continue")
clear()
mi = 0
potions1 = 10
clear()
print("But first, would you like to buy something?")
input("Press enter to continue")
dog = 1
oh = 0
shopresults = firstShop.firstShop(money,potions1,Weapons,weaponATKstats,weaponPrices,Armor,armorDEFstats,armorPrices,weaponID,armorID)
weaponID = shopresults[0]
money = shopresults[1]
armorID = shopresults[2]
characterDEF = originalDEF
potions1 = shopresults[3]
characterDEF = characterDEF + armorDEFstats[armorID]
characterATK = originalATK
characterATK = characterATK + weaponATKstats[weaponID]
enemieHP = random.randint(36,45)
enemieATK = random.randint(8,11)
enemieSPD = random.randint(3,10)
battleresult = battle.battle(characterATK,characterDEF,characterHP,characterSPD,characterCritChance,enemieATK,enemieHP,enemieSPD,potions1,money,originalHealth,effect)
potions1 = battleresult[1]
characterHP = battleresult[0]
print("You have ",potions1," potions")
print("You have ",characterHP," HP")
money = battleresult[2]
print("You have $", money)
input("Press enter to continue")
