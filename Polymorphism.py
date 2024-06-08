#Polymorphism means having many forms 
""" Ploy means many and morphism means form """


"""Some inbuilt polymorphism functions : """
# print(len("Python"))

#Using lists
# print(len(['2','4','6']))

#Using tuple 
# print(len({'2','3','4'}))

#Using dict 
# thisDict={
#     "Name":"Subash",
#     "Age":'19',
#     "Gender":"Male"  
# }
# print(len(thisDict))

"""User defined polymorphism functions """

# def add (x,y,z=0):
#     return(x+y+z)

# print(add(2,3))
# print(add(3,4,5))

"""Polymorphism with class methods : """
'''  
class Nepal():
    def capital(self):
        print("Kathmandu is the capital city of Nepal")
    
    def languages(self):
        print("Nepali is the widely speaking language of Nepal ")
    
    def type(self):
        print("Nepal is a developing country")
    
class USA():
    
    def capital(self):
        print("Washington DC is the capital city of Nepal")
    
    def languages(self):
        print("English is the widely speaking language of Nepal ")
    
    def type(self):
        print("USA is a developed country")

objNepal=Nepal()
objUSA=USA()

for country in (objNepal,objUSA):
    country.capital()
    country.languages()
    country.type()

'''  

