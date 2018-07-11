names = []
assignments = []
grades = []
count = 0 

for index in range(3):
    names.append(input("Digite os nomes: " ))
    assignments.append(input("Nota atual: "))
    grades.append(input("Nota potencial: "))
    

for i in range(3):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n"
    print(message.format(names[count].title(), assignments[count], grades[count], int(grades[count]) + int(assignments[count])*2))
    count+=1



