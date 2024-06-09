'''class Dog:
    attribute1="mammal"
    
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
     
    def speak(self):
        return("My pet {} sounds as {}".format(self.name,self.sound))
        
Rodger=Dog("Rodger","bhaw bhaw")
Tommy=Dog("Tommy","Meow Moew")

print("Rodger is a {}".format(Rodger.__class__.attribute1))
print("Tommy is a {}".format(Tommy.__class__.attribute1))

print("My pet dog name is :{} ".format(Rodger.name))
print("My pet cat  name is : {}".format(Tommy.name))

print(Rodger.speak())
print(Tommy.speak())
'''

'''
class Dog:
    animal='dog'
    
    def __init__(self,breed,color):
        self.breed=breed
        self.color=color

Rodger=Dog("Pug","brown")
Buzo =Dog("BullDog","Black")

print("Rodger details:")
print("Rodger is a",Rodger.animal)
print("Breed :",Rodger.breed)
print("Color :" ,Rodger.color)

print("Buzo details:")
print("Buzo is a ",Buzo.animal)
print("Breed:",Buzo.breed)
print("Color:",Buzo.color)

print("\nAccessing class variables using class name")
print(Dog.animal)

'''

class Student :
    def secondSem(self,books,labFile,Attendance,Holiday):
        self.books=books
        self.labfile=labFile
        self.attendance=Attendance
        self.holiday=Holiday
        
class Teacher:
    def subjects(self,AI,TOC,CN):
        self.ai=AI
        self.toc=TOC
        self.cn=CN

students=[]
count=0
 
num_students=int(input("Enter the number of students :"))  
for _ in range (num_students): 
    count+=1
    no=int(input("Enter the number of books :"))
    BName=input("Enter book names: ").split(" ")
    lab=input("Enter the lab subject name :")
    attend=int(input("Enter the no of present days :"))
    holiday=input("Enter holiday day :")
    
    student=Student()
    student.secondSem(BName,lab,attend,holiday)
    students.append(student)
    
    print(f"Total no of books for {count } : {no}")
    print('Book names are :',','.join(student.books))
    print('Lab subject is :',student.labfile)
    print('Total no of present day :',student.attendance)
    print("Holiday day is :",student.holiday)
