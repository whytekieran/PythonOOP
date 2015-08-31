from abc import ABCMeta, abstractmethod #importing these clases from abc (abstract base class) module used for creating abstract classes

#SIMPLE INHERITANCE
#Using (object) inside parenthesis allows you to call the the __init__ function (constructor) of BaseClass and allows access to BaseClass 
#variables from an inheriting class. This is very useful for any inheriting class. This particular code would run without (object) with 
#the statement: class BaseClass:    .....This is because we are not accessing the base classes __init__ function or its variables, only the
#one function defined in it. Shown in main.py we call the hello() function from both a BaseClass object and a ChildClass object
#and both work successfully. It is usually good practice to declare a base class like the following code has been written.

#Base Class
class BaseClass(object):
    def hello(self):
        print("Hello this method is inherited from BaseClass")
     
#Child class        
class ChildClass(BaseClass): #This statement lets ChildClass inherite from BaseClass
    pass                     #the 'pass' statement allows this class with no indented code block to run  

############################################################################################################################################
#MORE COMPLEX INHERITANCE
#More complex inheritance using the "super" function (like in java) to call the constructor of the base class from inherited class.
#Means if base class takes any arguments, those same arguments must be passed into the constructor of the inheriting class which uses,
#'super' to call the base classes constuctor. 
class Person(object): #'object' keyword is nessesary for inheritance
    name = ""
    age = 0
    health = 0
    
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health
        
    def printDetails(self):
        print("NAME:{0}   AGE:{1}   HEALTH:{2}".format(self.name, self.age, self.health))
        
#School class        
class School:
    schoolName = ""
    
    def __init__(self, schoolName):
        self.schoolName = schoolName

#Person class        
class Student(Person):
    grade = 0
    #constuctor
    def __init__(self, name, age, health, grade, schoolName): #passing in values for constructor
        super(Student, self).__init__(name, age, health)#use super keyword on student class then use .__init__() to pass in superclass values
        self.grade = grade         #other values assigned grade is passed to class instance variable
        self.school = School(schoolName)#Creating instance of School class (self.school) and passing in the schoolname to its constuctor

###########################################################################################################################################

#MULTIPLE INHERITANCE - is possible in python the example below shows how its done.
#class SubClassName(Student, School, Person):

###########################################################################################################################################
    
#SIMPLE ABSTRACT CLASS EXAMPLE

class ParentClass(metaclass=ABCMeta): #metaclass=ABCMeta used to make an abstract class
    @abstractmethod                   #use the @abstractmethod decorator to define an abstract method  
    def printString(self):
        pass
    
class SubClass(ParentClass):
    def printString(self):
        print("This is a string")
        
s = SubClass()
s.printString()






    
    
    
    
    
        