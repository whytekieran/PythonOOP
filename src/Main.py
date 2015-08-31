from Classes import BaseClass, ChildClass, Student #Importing BaseClass, ChildClass and Student from the Classes module

#simple example showing the use of the function belonging to this class
print("Using BaseClass object to call function")
b = BaseClass()
b.hello()
print()

#the child class can also use this function as it is a child of BaseClass and inherites it
print("Using ChildClass object to call function which it inherites from BaseClass")
c = ChildClass()
c.hello()

#Declaring a Student object inherited from Person class, uses Person classes constructor for the first three arguments.   
print("Creating student object which inherites from Person")
s = Student("Kieran", 26, 100, 'A', "GMIT")
s.printDetails()                              #Student object can call function from Person class
print(s.grade)                                #Printing out the grade value  
print(s.school.schoolName)  #We can access the schoolname value by calling the Student object which calls the School object that was 
                            #declared inside the Student class, then from there we can reference its schoolName value.