import random







title = "Kaun Banega Crorepati"

print(title.center(100))


subt = "(Bakchod Edition)"

print(subt.center(100))
fz = input("Press Enter to continue...")
print('Get Ready!')

#Questions
rs1 = 'How many fingers does shit have?'
rs2 = 'What does an animal do?'
rs3 = 'If a car could fly what would benum do?'
rs4 = 'Nora Fatehi aur Disha Patani?'
rs5 = 'Science is greater than anything.'
rs6 = 'Hanso, hahaha....'
rs7 = 'Kutte kya bolte hai?'
rs8 = 'DJ wale babu konsa gaana baja rahe hai?'
rs9 = 'Agar x=10, train 100 kmph ki speed se chal ri hai aur nucleus biology aur physics dono me hai, to benum aj kis color ka kachha pehnke aya hai?'
rs10 = 'Munna kyu badnaam hua?'
rs11 = 'Don ko pakadna mushkil hi nai namumkin hai, aisa kyu?'
rs12 = 'If you could have any power what would you ask for?'
rs13 = 'Joey is to Ross as Salman is to?'
rs14 = 'Complete the song:"Baby ko bass pasand hai......"'

#Answer_List
r1 = 'A. 25\nB. 230\nC. Million\nD. None'
r2 = 'A. Bhag\nB. Bhagdaud\nC. Be an animal\nD. Daud'
r3 = 'A. Ask it questions\nB. Drive it\nC. Break it\nD. Shit on it'
r4 = 'A. Nora\nB. Disha\nC. Threesome\nD. Padhle g*ndu'
r5 = 'A. Bhosadpappu ho ka be?\nB. Mai to Einstein hu\nC. Je ky hota hai?\nD. Science to gutke ki tarah chaba jata hu mai'
r6 = 'A. Nai\nB. Hag dia hanste hanste\nC. Bhag\nD. Maybe'
r7 = 'A. Bhau\nB. Au\nC. Woof\nD. Dichkyau\nE. Abe chodampatti ke, kutte kabse bolne lag gaye?'
r8 = 'A. Selfie Maine Leli Aj\nB. Andheri Rato ka Raja\nC. Ye kaisa question hai chiraand se\nD. Jajantaram Mamantaram\n'
r9 = 'A. Ye bhi dekhna hota hai?\nB. Mai to uska haseen badan ke roobaru ho jau bas\nC. Bhag\nD. Young ke modulus se pata chalega'
r10 = 'A. Usne munni ko n*nni dikhani thi\nB. Kyuki Munna Doctor nai ban paya\nC. Kyuki Munna Salman Khan hai\nD. Kyuki munni bhi badnaam hai'
r11 = 'A. Kyuki wo darpok hai\nB. Abe mai Don hu, nai bata sakta\nC. Wo baalo me tel lagata hai, isliye uski guddi hath nai lagti\nD. Mujhe nai batana, man ni hai'
r12 = 'A. I am too lazy to answer.\nB. Sleep\nC. Samay ki dhaar rok dunga jaise moot rukta hai \nD. Daaru pio lehn ke bodo'
r13 = 'A. Rakhi Sawant\nB. Mo angreji na awe\nC. Suar\nD. Kutte ka Moot'
r14 = 'A. Dhin Tina Dhin Tin Tina\nB. Tan tana nana nana\nC. Dhika chin dhoom dhoom\nD. Dhoom Chika Dhoom'

#Answer_Key
a1 = 'D'
a2 = 'C'
a3 = 'A'
a4 = 'D'
a5 = 'A'
a6 = 'B'
a7 = 'E'
a8 = 'C'
a9 = 'D'
a10 = 'B'
a11 = 'C'
a12 = 'C'
a13 = 'C'
a14 = 'A'

#Winning_Amount
j1 = "₹0"
j2 = "₹5,000"
j3 = "₹10,000"
j4 = "₹20,000"
j5 = "₹40,000"
j6 = "₹80,000"
j7 = "₹1,60,000"
j8 = "₹3,20,000"
j9 = "₹6,40,000"
j10 = "₹12,50,000"
j11 = "₹25,00,000"
j12 = "₹50,00,000"
j13 = "₹1,00,00,000"
j14 = "₹3,00,00,000"
j15 = "₹7,00,00,000"

#lists
quest = [rs1, rs2, rs3, rs4, rs5, rs6, rs7, rs8, rs9, rs10, rs11, rs12, rs13, rs14]
alst = [r1, r2, r3, r4, r5, r6,r7,r8,r9, r10, r11, r12, r13, r14]
ans = [a1, a2, a3, a4, a5, a6,a7,a8, a9, a10, a11, a12, a13, a14]
j = [j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15]

#initialised_values
x = 0
ind = int
b = 1
n='Y'


for x in range(14):
    if n == 'Y' and b == 1:
        q1 = random.choice(quest)
        ind = quest.index(q1)
        print("For", j[x + 1], "Here is question", x + 1, ":")
        print(q1)
        print(alst[ind])
        print(ans[ind])#for checking the answer if the correct answer is being provided
        y = input("Please Input Your Choice: ")
        if y == ans[ind]:
            
            b = 1
            print("Correct Answer! You have won", j[x+1], "\n")
            quest.remove(quest[ind])
            ans.remove(ans[ind])
            alst.remove(alst[ind])

            if not x == 14:
                n = input("Do you want to continue?(Y/N): ")
                if n =='Y':
                    pass
                else:
                    print(f"Your take home amount is {j[x - 1]}")
                    out = input("Press Enter to exit...")
                    break
            else:
                print("You have won KBC Bakchod Edition!")
                fn = input("Press Enter to exit...")
                break
        else:
            b = 0
            print (f"Wrong answer!Your take home amount is {j[x]}")
            out = input("Press Enter to exit...")
            print("these are the quesitons in order")
            print(quest)
            print("This is the answer list")
            print(alst)
            print("These are the correct answers")
            print(ans)
            break
        x = x + 1