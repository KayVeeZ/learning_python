# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:32:04 2023

@author: KayVeeZ
"""


print("A wet lab program by ::KayVeeZ::")

#Calculate required solute from molarity

b = "Y"

while True:
    if (b=="Y"):
        mol_m = float(input("Please input molar mass of compoound in grams/mol : ")) 
        mol = float(input("Please input molarity (in mM) of compound : "))
        vol = float(input("Please input volume of solvent in milliliters : "))
        weight =  ((mol/1000)*vol*mol_m)
        print(weight,"mg")
        c = input("Do you wish to convert this measurement to grams? Y/N ")
        if (c=="Y" or c=="y"):
            weight = weight/1000
            print(weight, "grams")
        else:
            pass
        b = input("Do you want to continue? Y/N : ")
    else:
        a = 'Thank You!'
        print(a)
        break
d = input("Press Enter to exit....")
 
