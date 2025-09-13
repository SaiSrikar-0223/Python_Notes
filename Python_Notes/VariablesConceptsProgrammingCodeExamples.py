
# print('hello 1')
# print('hello 2')
# print('hello 3')
# print('hello 4')
# print('hello 5')

#### Types of Variables ####
'''
1. Global Variable

2. Local Variable

3. Parameterized Variable

4. Class Variable

5. Instance Variable

'''


### Working with  global + local + parametrized variable scopes ###
'''
a = 10 # global scope
class Employee:
    def display(self, c=30): # Paramerized variable scope ---->> local scope only
        b = 20 # local scope
        print("Inside Class : Value of a is :", a)
        print("Inside Class : Value of b is :", b)
        print("Inside Class : Value of c is :", c)


emp = Employee()
emp.display()


print('Outside Class : value of a :', a )
#print('Outside Class : value of b :', b ) # NameError: name 'b' is not defined
# print('Outside Class : value of c :', c ) # NameError: name 'c' is not defined
'''


## Converting local variable scope into  global variable scope using "global" keyword
'''
a = 10 # global scope
class Employee:
    def display(self, c=30): # Paramerized variable scope ---->> local scope only
        global b
        b = 20 # local scope  ---->> conerting like global scope
        print("Inside Class : Value of a is :", a)
        print("Inside Class : Value of b is :", b)
        print("Inside Class : Value of c is :", c)


emp = Employee()
emp.display()


print('Outside Class : value of a :', a )
print('Outside Class : value of b :', b ) # NameError: name 'b' is not defined
# print('Outside Class : value of c :', c ) # NameError: name 'c' is not defined
'''

### Working with  class variables ####
'''
class Employee:
    # class variables
    eno = 101
    ename = 'Sachin'

    def display(self):

        print("Employee number is :", eno)
        print("Employee number is :", ename)

emp1 = Employee()
emp1.display()
'''

## Class variables using className , we can access inside class and outside class
'''
class Employee:
    # class variables
    eno = 101
    ename = 'Sachin'

    def display(self):
        print("Inside Class : Employee number is :", Employee.eno)
        print("Inside Class : Employee number is :", Employee.ename)

emp1 = Employee()
emp1.display()
print()
print("Outside Class : Employee number is :", Employee.eno)
print("Outside Class : Employee number is :", Employee.ename)
'''


## Class variables using className reference , we can access inside class and outside class
'''
class Employee:
    # class variables
    eno = 101
    ename = 'Sachin'

    def display(self):
        print("Inside Class : Employee number is :", emp1.eno)
        print("Inside Class : Employee number is :", emp1.ename)

emp1 = Employee()
emp1.display()
print()
print("Outside Class : Employee number is :", emp1.eno)
print("Outside Class : Employee number is :", emp1.ename)
'''


## Class variables using self parameter , we can access inside class but not outside class

class Employee:
    # class variables
    eno = 101
    ename = 'Sachin'

    def display(self):
        print("Inside Class : Employee number is :", self.eno)
        print("Inside Class : Employee number is :", self.ename)

emp1 = Employee()
emp1.display()
print()
# print("Outside Class : Employee number is :", self.eno) # NameError: name 'self' is not defined
# print("Outside Class : Employee number is :", self.ename)






















