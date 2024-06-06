class Dog:
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



