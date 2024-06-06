class Person(object):
    
    def __init__ (self,name,idNumber):
        self.name=name
        self.idNumber=idNumber
        
    def display(self):
        print(self.name)
        print(self.idNumber)
    
    def details(self):
        print("My name is {}".format(self.name))
        print("My id number is {} ".format(self.idNumber))
        
#child class
class Employee(Person):
    def __init__ (self,name,idNumber,salary,post,age,companyName):
        super().__init__(name, idNumber)
        self.salary=salary
        self.post=post
        self.age=age
        self.companyName=companyName
        
        # Person.__init__(self,name,idNumber)
    
    def detail(self):
        print("My salary in NRs is {}".format(self.salary))
        print("My post in the {} company is {}".format(self.companyName,self.post))
        print("My age is {}".format(self.age))

# p=Employee("Subash",79010478,200000,'Python Developer',19,"ABC")  

# p.details() 
# p.detail()  


class Employee2(Person):
    def __init__(self,name,idNumber,Address,ContactNo):
        super().__init__(name,idNumber) # Ambiguous(due to excess of same parent from two child class) so to reduce it we use super keyword 
        self.address=Address
        self.contact=ContactNo
        
    def detailsEmp2(self):
        print("My name is : {} ".format(self.name))
        print("My id number is : {} ".format(self.idNumber))
        print("My address is : {} ".format(self.address))
        print("My contact number is {} ".format(self.contact))

# p2=Employee2("Subash",79010478,"Bode",9749459199)  
# p2.detailsEmp2() 
 

name=str(input("Enter your name : "))
id=int(input("Enter your id number: "))
salary=float(input("Enter your salary in NRs. : "))
position=str(input("Enter your position in a company: "))
age=int(input("Enter your age : "))
address=str(input("Enter your address: "))
contact=int(input("Enter your contact number: "))
company=str(input("Enter your company name : "))

p1=Employee(name, id, salary, position, age, company)
p2 = Employee2(name, id, address, contact)

p1.details()
p2.detailsEmp2()



   
        