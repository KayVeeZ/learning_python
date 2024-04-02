from os import mkdir as md
number= input('How many  are there in the course?')
for i in range(int(number)):
    md(f'Week {i+1}')
input("Press Enter to exit...")