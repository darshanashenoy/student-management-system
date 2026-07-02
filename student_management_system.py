students = [
    ["Arun", 85],
    ["Sneha", 92],
    ["Rahul", 76],
    ["Anjali", 95],
    ["Kiran", 68]
]

def display(students):
    print("Name of student","Marks")
    for i in students:
        name,marks=i[0],i[1]
        print(name,marks)
def highest(students):
    c=0
    for i in students:
        if i[1]>c:
            c=i[1]
    for i in students:
        if i[1]==c:
            print("Highest scoring student:",i[0],"marks",i[1])
def average(students):
    c=0
    for i in students:
        c+=i[1]
    avg=c/len(students)
    print("Average marks=",avg)
def above80(students):
    print("Students scoring 80 are:")
    for i in students:
        if i [1]>80:
            print(i[0])
def search(students):
    search=False
    name=input("enter name to be searched:")
    for i in students:
        if i[0]== name:
            print("Student found successfully")
            search=True
    if search==False:
        print("Student not found")
def addstudent(students):
    name=input("enter name")
    marks=int(input("Enter marks"))
    students.append([name,marks])
    print("Added successfully")
def totalmarks(students):
    c=0
    for i in students:
        c+=i[1]
    print("The total marks is=",c)
def grades(students):
    for i in students:
        marks=i[1]
        if marks>=90 and marks<=100:
            print(i[0],"A")
        elif marks>=80 and marks<=89:
            print(i[0],"B")
        elif marks>=70 and marks<=79:
            print(i[0],"C")
        elif marks<70:
            print(i[0],"D")
def removestudent(students):
    name=input("enter name to remove ")
    for i in students:
        if i[0]==name:
            students.remove(i)
            print("removed successfully")
print("1. Display all students")
print("2. Highest mark")
print("3. Average mark")
print("4. Students scoring above 80")
print("5. Search student")
print("6. Add new student")
print("7. Remove a student")
print("8. Total marks")
print("9. Grades")
print("10. Exit")
while True:
    n=int(input("Enter number"))
    if n==1:
        display(students)
    elif n==2:
        highest(students)
    elif n==3:
        average(students)
    elif n==4:
        above80(students)
    elif n==5:
        search(students)
    elif n==6:
        addstudent(students)
    elif n==7:
        removestudent(students)
    elif n==8:
        totalmarks(students)
    elif n==9:
        grades(students)
    
    elif n==10:
        print("Thank you!")
        break
    else:
        print("Invalid option")