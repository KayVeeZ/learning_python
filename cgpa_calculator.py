num_sem =int(input('Please enter number of semesters: '))

for i in range(num_sem):
    b = int(input(f'Enter number of subjects in sem {i+1}: '))
    for j in range(b):
        list_cred=[]

        sub = input(f'Enter name of subject {j+1} in sem {i+1} :')
        c = float(input(f'Enter number of credits (ECU/ACU) for {sub.upper()}: '))
        list_cred.append(c)
        e= float(input(f'Enter grade points (GP) for subject {sub.upper()}: '))
        list_marks = []
        list_marks.append(e*c)

total_marks=0.0
total_creds=0.0
print(list_marks)
print(list_cred)
for x in range(0,len(list_marks)):
    total_marks = total_marks + list_marks[x]
for y in range(0,len(list_cred)):
    total_creds = total_creds + list_cred[y]



print(f'total marks :{total_marks}')
print(f'total credits: {total_creds}')
cgpa=total_marks/total_creds
print(f'Your CGPA is : {cgpa}')