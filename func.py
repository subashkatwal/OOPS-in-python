def main():
    class Employee:
        def __init__ (self,name,age):
            self.name=name
            self.age=age
        def __str__ (self):
            return f'Employee(Name:{self.name},Age:{self.age})'

    emp_name=int(input("Enter the number of employee : "))
    employee=[]
        
    for _ in range (emp_name):
        name=(input("Enter the name of employee ."))
        age=int(input("Enter the age of the employee."))
        employee.append(Employee(name,age))
        
    for emp in employee:
        print(emp)
        

if __name__ =="__main__":
    main()