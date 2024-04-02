import random
from playsound import playsound
title="Kaun Banega Crorepati"

print(title)

playsound('C:\codes\kbc_project\intro.mp3')
subt="(Gag Edition)"

print(subt)

rs1 = 'How many fingers does shit have?'
rs2 = 'What does an animal do?'
rs3 = 'If a car could fly what would benum do?'
rs4 = 'Is a neuron a nerve cell?'
rs5 = 'Science is greater than anything.'
rs6 = 'Hanso, hahaha....'
r1 = 'A. 25\nB. 230\nC. Million\nD. None'
r2 = 'A. Bhag\nB. Bhagdaud\nC. Be an animal\nD. Daud'
r3 = 'A. Ask it questions\nB. Drive it\nC. Break it\nD. Shit on it'
r4 = 'A. Yes\nB. No\nC. Both\nD. I Do not Know'
r5 = 'A. Chutia Hai kya?\nB. Bhang Khai Hai?\nC. I do not know\nD. That is your opinion'
r6 = 'A. Nai\nB.Hag dia hanste hanste\nC. Bhag\nD. Maybe'
a1 = 'D'
a2 = 'C'
a3 = 'A'
a4 = 'C'
a5 = 'D'
a6 = 'B'

quest = [rs1, rs2, rs3, rs4, rs5, rs6]
alst = [r1, r2, r3, r4, r5, r6]
answer = [a1, a2, a3, a4, a5, a6]
i = 0
x = 1
j = ["₹0", "₹5,000", "₹10,000", "₹20,000", "₹40,000", "₹80,000", "₹1,60,000"]
for i in range(5):
    for x in j:
        b = int
    if i == 0:
        x = i+1
        playsound('C:\codes\kbc_project\question.mp3')
        print("For ₹5,000 Here is the first question:")
        q1 = random.choice(quest)
        print(q1)
        if q1 == rs1:
            print(r1)
        elif q1 == rs2:
            print(r2)
        elif q1 == rs3:
            print(r3)
        elif q1 == rs4:
            print(r4)
        elif q1 == rs4:
            print(r3)
        elif q1 == rs5:
            print(r5)
        elif q1 == rs6:
            print(r6)
        z = input("Please input choice: ")
        y = z
        if q1 == rs1:
            if y == a1:
                b = 1
            else:
                b = 0

        if q1 == rs2:
            if y == a2:
                b = 1
            else:
                b = 0

        if q1 == rs3:
            if y == a3:
                b = 1
            else:
                b = 0

        if q1 == rs4:
            if y == a4:
                b = 1
            else:
                b = 0

        if q1 == rs5:
            if y == a5:
                b = 1
            else:
                b = 0

        if q1 == rs6:
            if y == a6:
                b = 1
            else:
                b = 0
        quest.remove(q1)
        if b == 1:
            print("Correct Answer! You have won ₹5,000")
        else:
            print("Wrong Answer! Your winning amount is", j[x - 1])
            break

    i = i + 1
    x = x + 1
    if i == 1:

        playsound('C:\codes\kbc_project\question.mp3')
        print("For", j[x], "Here is the next question:")
        q1 = random.choice(quest)
        print(q1)
        if q1 == rs1:
            print(r1)
        elif q1 == rs2:
            print(r2)
        elif q1 == rs3:
            print(r3)
        elif q1 == rs4:
            print(r4)
        elif q1 == rs4:
            print(r3)
        elif q1 == rs5:
            print(r5)
        elif q1 == rs6:
            print(r6)
        z = input("Please input choice: ")
        y = z
        if q1 == rs1:
            if y == a1:
                b = 1
            else:
                b = 0

        if q1 == rs2:
            if y == a2:
                b = 1
            else:
                b = 0

        if q1 == rs3:
            if y == a3:
                b = 1
            else:
                b = 0

        if q1 == rs4:
            if y == a4:
                b = 1
            else:
                b = 0

        if q1 == rs5:
            if y == a5:
                b = 1
            else:
                b = 0

        if q1 == rs6:
            if y == a6:
                b = 1
            else:
                b = 0
        quest.remove(q1)
        if b == 1:
            print("Correct Answer! You have won", j[x])
        else:
            print("Wrong Answer! Your winning amount is", j[x - 1])
            break

    if i == 2:

        playsound('C:\codes\kbc_project\question.mp3')
        print("For", j[x], "Here is the next question:")
        q1 = random.choice(quest)
        print(q1)
        if q1 == rs1:
            print(r1)
        elif q1 == rs2:
            print(r2)
        elif q1 == rs3:
            print(r3)
        elif q1 == rs4:
            print(r4)
        elif q1 == rs4:
            print(r3)
        elif q1 == rs5:
            print(r5)
        elif q1 == rs6:
            print(r6)
        z = input("Please input choice: ")
        y = z
        if q1 == rs1:
            if y == a1:
                b = 1
            else:
                b = 0

        if q1 == rs2:
            if y == a2:
                b = 1
            else:
                b = 0

        if q1 == rs3:
            if y == a3:
                b = 1
            else:
                b = 0

        if q1 == rs4:
            if y == a4:
                b = 1
            else:
                b = 0

        if q1 == rs5:
            if y == a5:
                b = 1
            else:
                b = 0

        if q1 == rs6:
            if y == a6:
                b = 1
            else:
                b = 0
        quest.remove(q1)
        if b == 1:
            print("Correct Answer! You have won", j[x])
        else:
            print("Wrong Answer! Your winning amount is", j[x - 1])
            break

    if i == 3:

        playsound('C:\codes\kbc_project\question.mp3')
        print("For", j[x], "Here is the next question:")
        q1 = random.choice(quest)
        print(q1)
        if q1 == rs1:
            print(r1)
        elif q1 == rs2:
            print(r2)
        elif q1 == rs3:
            print(r3)
        elif q1 == rs4:
            print(r4)
        elif q1 == rs4:
            print(r3)
        elif q1 == rs5:
            print(r5)
        elif q1 == rs6:
            print(r6)
        z = input("Please input choice: ")
        y = z
        if q1 == rs1:
            if y == a1:
                b = 1
            else:
                b = 0

        if q1 == rs2:
            if y == a2:
                b = 1
            else:
                b = 0

        if q1 == rs3:
            if y == a3:
                b = 1
            else:
                b = 0

        if q1 == rs4:
            if y == a4:
                b = 1
            else:
                b = 0

        if q1 == rs5:
            if y == a5:
                b = 1
            else:
                b = 0

        if q1 == rs6:
            if y == a6:
                b = 1
            else:
                b = 0
        quest.remove(q1)
        if b == 1:
            print("Correct Answer! You have won", j[x])
        else:
            print("Wrong Answer! Your winning amount is", j[x - 1])
            break

    if i == 4:

        playsound('C:\codes\kbc_project\question.mp3')
        print("For", j[x], "Here is the next question:")
        q1 = random.choice(quest)
        print(q1)
        if q1 == rs1:
            print(r1)
        elif q1 == rs2:
            print(r2)
        elif q1 == rs3:
            print(r3)
        elif q1 == rs4:
            print(r4)
        elif q1 == rs4:
            print(r3)
        elif q1 == rs5:
            print(r5)
        elif q1 == rs6:
            print(r6)
        z = input("Please input choice: ")
        y = z
        if q1 == rs1:
            if y == a1:
                b = 1
            else:
                b = 0

        if q1 == rs2:
            if y == a2:
                b = 1
            else:
                b = 0

        if q1 == rs3:
            if y == a3:
                b = 1
            else:
                b = 0

        if q1 == rs4:
            if y == a4:
                b = 1
            else:
                b = 0

        if q1 == rs5:
            if y == a5:
                b = 1
            else:
                b = 0

        if q1 == rs6:
            if y == a6:
                b = 1
            else:
                b = 0
        quest.remove(q1)
        if b == 1:
            print("Correct Answer! You have won", j[x])
        else:
            print("Wrong Answer! Your winning amount is", j[x - 1])
            break

    if i == 5:

        playsound('C:\codes\kbc_project\question.mp3')
        print("For", j[x], "Here is the next question:")
        q1 = random.choice(quest)
        print(q1)
        if q1 == rs1:
            print(r1)
        elif q1 == rs2:
            print(r2)
        elif q1 == rs3:
            print(r3)
        elif q1 == rs4:
            print(r4)
        elif q1 == rs4:
            print(r3)
        elif q1 == rs5:
            print(r5)
        elif q1 == rs6:
            print(r6)
        z = input("Please input choice: ")
        y = z
        if q1 == rs1:
            if y == a1:
                b = 1
            else:
                b = 0

        if q1 == rs2:
            if y == a2:
                b = 1
            else:
                b = 0

        if q1 == rs3:
            if y == a3:
                b = 1
            else:
                b = 0

        if q1 == rs4:
            if y == a4:
                b = 1
            else:
                b = 0

        if q1 == rs5:
            if y == a5:
                b = 1
            else:
                b = 0

        if q1 == rs6:
            if y == a6:
                b = 1
            else:
                b = 0
        quest.remove(q1)
        if b == 1:
            print("Correct Answer! You have won", j[x])
        else:
            print("Wrong Answer! Your winning amount is", j[x - 1])
            break

