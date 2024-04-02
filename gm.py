def gmean(a, b):
    if (a > b):
        mean = (a * b) / (a + b)
        print(mean)
        print(a, "is greater than", b)
    elif (b > a):
        mean = (a * b) / (a + b)
        print("Geometric mean is:", mean)
        print(b, "is greater than", a)
    else:
        print("Both numbers are equal.")


i = "Y"
while (i == "Y"):
    i = input("Do you want to calculate Geometric mean? (Y for Yes, N for No) : ")
    if (i == "N"):
        break
    elif (i == "Y"):
        c = int(input("Please provide 1st number: "))
        d = int(input("Please provide 2nd number: "))
        gmean(c, d)
    else:
        print("Invalid Input, Try again!")
print("See you Later!")

