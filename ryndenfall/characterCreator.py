#!/usr/bin/env python3
#
# Thomas tran
# CPSC 362
# 2021-11-28
# tdttran2000@csu.fullerton.edu
#

"""
This file contains the character creator which starts off the game. 
"""

import string 
import csv

class PlayerCharacter:
    #Initialization for Player's Character with their attributes.
    def __init__(self, name, gender, nation, order, level, attack, mana, hp, defense, agility):
            self.name = name
            self.gender = gender
            self.nation = nation
            self.order = order
            self.lvl = level
            self.attack = attack
            self.mana = mana
            self.hp = hp
            self.defense = defense
            self.agility = agility

    def displayInfo(self):
        print("----{} the {}'s Info----".format(self.name, self.order))
        print("Gender: {}".format(self.gender))
        print("Nation: {}".format(self.nation))
        print("Level: {}".format(self.lvl))
        print("Atk Stat: {}".format(self.attack))
        print("Mana Stat: {}".format(self.mana))
        print("Def Stat: {}".format(self.defense))
        print("Agl Stat: {}".format(self.agility))
        print("Health Stat: {}".format(self.hp))
        return

def characterCreator():

    print("Please tell me our hero's name!: "); pName = input()
    #pName = input()

    print("Now tell me, is {} a young man or woman?(Please input Male or Female): ".format(pName))
    pGender = input()
    if pGender.casefold() == "male" or pGender.casefold() == "female":
        pass
    else: 
        while pGender.casefold() != "male" or pGender.casefold() != "female":
            print("I'm sorry, could you please repeat that?(Please input male or female): ")
            pGender = input()


    print("Now tell me, what nation does {} hail from?\n"\
        "1. The Militaristic Ayrsandria Empire, whose people strive to innovate, believing only in the power of science.\n"\
        "2. The Theocratic Kingdom of Lieandral, whose people have an affinity for nature and the world around them.\n"\
        "3. The Sharp Kincerpent Shogunate, whose people are cunning, resourceful, and adaptable due to the harsh conditions\
        of their environment.\n"\
        "4. The Shattered Kingdom of Morterra, whose people only know war and violence.".format(pName))
    print("(Input a number 1-4): ")
    intNation = int(input())
    while (intNation > 4) or (intNation < 1): 
        print("I'm sorry, could you please repeat that?(Please input a number 1-4): ")
        intNation = input()
    if intNation == 1:
        pNation = str("Ayrsandria")
        pOrder = str("Mekhanik")
    elif intNation == 2:
        pNation = str("Lieandral")
        pOrder = str("Mhajikor")
    elif intNation == 3:
        pNation = str("Kincerpent")
        pOrder = str("Umbral")
    elif intNation == 4:
        pNation = str("Morterra")
        pOrder = str("Paladyn")


    totalStatPoints = int(20)
    pAtk = int(1)
    pMna = int(1)
    pDef = int(1)
    pAgl = int(1)
    pHp = int(5)

    if (pOrder == "Paladyn"):
        pAtk += 5
    elif (pOrder == "Mhajikor"):
        pMna += 5
    elif (pOrder == "Mekhanik"):
        pDef += 5
    elif (pOrder == "Umbral"):
        pAgl += 5

    print("Good good, here are {} the {}'s stats...\n"\
    "[Total Points Available] = {} \n".format(pName, pOrder, totalStatPoints))
    print("Base Attack = {}".format(pAtk))
    print("Base Mana = {}".format(pMna))
    print("Base Defense = {}".format(pDef))
    print("Base Agility = {}".format(pAgl))
    print("Base Health = {}".format(pHp))
    
    print("\nHow many points would you like to add to Attack?: ")
    usedPoints = int(input())
    pAtk += usedPoints
    totalStatPoints -= usedPoints

    print("\n[Total Points Available] = {}".format(totalStatPoints))
    print("How many points would you like to add to Mana?: ")
    usedPoints = int(input())
    pMna += usedPoints
    totalStatPoints -= usedPoints

    print("\n[Total Points Available] = {}".format(totalStatPoints))
    print("How many points would you like to add to Defense?: ")
    usedPoints = int(input())
    pDef += usedPoints
    totalStatPoints -= usedPoints
    
    print("\n[Total Points Available] = {}".format(totalStatPoints))
    print("How many points would you like to add to Agility?: ")
    usedPoints = int(input())
    pAgl += usedPoints
    totalStatPoints -= usedPoints

    print("\n[Total Points Available] = {}".format(totalStatPoints))
    print("How many points would you like to add to Health?: ")
    usedPoints = int(input())
    pHp += usedPoints
    totalStatPoints -= usedPoints
    
    pCharacter = PlayerCharacter(pName, pGender, pNation, pOrder, 1, pAtk, pMna, pHp, pDef, pAgl)
    return pCharacter

def main():
    
    print("[] Welcome to Ryndenfall's Character Creator! []\n")
    print("[============================================]\n")

    player = characterCreator()

    player.displayInfo()
    
    with open('character_log.csv', 'w', newline='') as csvfile:
        characterFields = ['name', 'gender', 'nation', 'order', 'lvl', 'attack', 'mana', 'hp', 'defense', 'agility']
        writer = csv.DictWriter(csvfile, fieldnames=characterFields)
        
        writer.writeheader()
        writer.writerow({'name': player.name, 'gender':player.gender, 'nation':player.nation, 'order': player.order, 'lvl':player.lvl, 'attack': player.attack, 'mana': player.mana, 'hp': player.hp, 'defense': player.defense, 'agility': player.agility})

if __name__ == '__main__':
    main()
    