print("A wet lab program by ::KayVeeZ::")

#Calculate required volume of known solution to make desired volume of changed molarity

b = "Y"

while True:
    if (b=="Y" or b=='y'):
        m2 = float(input("Enter desired molarity (in mM) : "))
        v2 = float(input("Enter desired volume (in mL) : "))
        m1 = float(input("Enter known molarity (in mM) : "))
        v1 = (m2 * v2)/m1

        print(f"You need {v1} ml of current solution to make {v2} ml of desired solution.")
        b = input("Do you want to continue? Y/N : ")
    else:
        a = 'Thank You!'
        print(a)
        break
d = input("Press Enter to exit....")