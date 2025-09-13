
'''
class Employee:
    pass
'''


'''
class Employee:
    eno = 101
    ename = 'Rohit'

    def message(self):
        pass 
    
'''


# create Employee class
'''
class Employee:
    # create attributes
    eno = 101
    ename = 'Rohit'

    # create method
    def message(self):
        pass 


# Create the object to Employee class
emp = Employee()
'''

# create Employee class
'''
class Employee:
    # create attributes
    eno = 101
    ename = 'Rohit'

    # create method
    def message(self):
        print('Hello message() method') 


# Create the object to Employee class
emp = Employee()
emp.message() 

print("Employee number is :",emp.eno)
print("Employee name is :",emp.ename)
'''


## Can we create more than one object for a single class?
'''
class Employee:
    def message(self):
        print('I am from message() method')

    def display(self):
        print('I am from display() method')


emp1 = Employee()
emp1.message()
emp1.display()
print()


emp2 = Employee()
emp2.message()
emp2.display()
'''


### Working with constructor  concept ###

# Non-Parameterized Constructor
'''
class Employee:
    def __init__(self):
        print('I am a constructor method')

    def message(self):
        print('I am a message method')

emp1 = Employee()
emp1.message() 

emp2 = Employee()
'''


# Parameterized Constructor
'''
class Employee:
    def __init__(self, eno, ename):
        print('I am a constructor method')
        print('Employee number is :', eno)
        print('Employee name is :', ename)

    def message(self, name):
        print('I am a message method')
        print('Hello', name)

emp1 = Employee(101, 'Virat')
print()

emp1.message('Sachin') 
'''

## Can we create  more than one constructor in a single class
'''
class Employee:
    def __init__(self):
        print('I am a first constructor')

    def __init__(self):
        print('I am a second constructor')

emp1 = Employee()
'''

## How to find the number of objects created for a single class
'''
class Employee:
    count = 0
    
    def __init__(self):
        Employee.count = Employee.count + 1
        
emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

print("Total number of objects :",Employee.count)

'''


'''
class Employee:
    count = 0
    
    def __init__(self):
        Employee.count = Employee.count + 1
        
    def message(self):
        print('hello')
        
emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

print("Total number of objects :",Employee.count)

print(emp1.count)
print(Employee.count)
'''






