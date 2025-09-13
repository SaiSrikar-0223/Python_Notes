
#SyntaxError
'''
def message():
'''

'''
def message():
    pass
'''

## Create a function with required statements and execute it
'''
print('start line')

#Create a function
def message():
    # body of function
    print('Welcome to function')
    print('Hello 1')
    print('Hello 2')

# Calling function
message()

print('last line')

message()
'''


## TypeError: message() missing 1 required positional argument: 'name'
'''
print('start line')

def  message(name):
    print('Hello', name)

message()

print('last line')
'''

## What is output?
''''
print('start line')

def  message(name):
    print('Hello', name)

message('Virat')

print('last line')
'''

## TypeError: message() takes 1 positional argument but 2 were given
'''
print('start line')

def  message(name):
    print('Hello', name)

message('Virat', 'Rohit')

print('last line')
'''

## What is output?
'''
print('start line')

def  message(name):
    print('Hello', name)

x = 'Virat'

message(x)

print('last line')
'''

## add variables and print result
'''
def addition(x,y):
    print('X value is :',x)
    print('Y value is :',y)
    print('Sum is :', x + y)

addition(20,10)
'''

## What is output?
'''
def addition(x,y):
    print('X value is :',x)
    print('Y value is :',y)
    print('Sum is :', x + y)
    return None

print(addition(20,10))
'''


## What is output?
'''
def addition(x,y):
    print('X value is :',x)
    print('Y value is :',y)
    #print('Sum is :', x + y)
    return x + y

print("The Sum is :",addition(20,10))
'''

## Can we assign a function result to a variable
'''
def addition(x,y):
    return x + y

result = addition(10,20)

print(result)
'''

## Can we use a function result in an expression
'''
def addition(x,y):
    return x + y

result = addition(10,20) * 2 + 10

print(result)
'''


## Can we call a functionName before creating it?

# NameError: name 'addition' is not defined
'''
result = addition(10,20)

def addition(x,y):
    return x + y

print(result)

'''

## Can we call a function inside another function?
'''
def f1():
    print('I am from f1() function')

def f2():
    print('I am from f2() function - first line')
    f1()
    print('I am from f2() function - last line')

f2()
'''


## Can we call a functionName inside same functionName (It leads to Infinite function)

# RecursionError: maximum recursion depth exceeded
'''
def f1():
    print('I am from f1() function')
    f1()

f1()
'''


### Working with return keyword 
'''
def message():
    print('line 1')
    print('line 2')
    print('line 3')
    print('line 4')
    print('line 5')
    print('line 6')
    return None

print(message())
'''

## In every function "return"  keyword  statement is a last statement
'''
def message():
    print('line 1')
    print('line 2')
    print('line 3')
    return None
    print('line 4')
    print('line 5')
    print('line 6')

print(message())
'''

####  Types of  Functions ####

# 1. Predefined  Functions
''' print(), id(), type(), input() , int(), float(), list(), tuple(),
         sum() ,min(), max() , len(), eval(), sorted(), reversed(),....'''

# 2. Userdefined Functions
''' message(), addition, add(), sub(), mul(), deposite() , withdraw(),..'''


####  Types of Arguments ####

# 1. Non-Default | Required | Positional arguments

# 2. Default  arguments

# 3. Keyword  arguments

# 4. Arbitory | Variable length arguments


# 1. Non-Default | Required | Positional arguments
'''
def add(a,b):
    return a + b

print(add(20,10))
'''

# 2. Default  arguments
'''
def add(a=10,b=20):
    print('Value of a is :',a) # 10
    print('Value of b is :',b) # 20
    return a + b

print(add())
'''

# What is output?
'''
def add(a=10,b=20):
    print('Value of a is :',a) # 30
    print('Value of b is :',b) # 20
    return a + b

print(add(30))
'''
# What is output?
'''
def add(a=10,b=20):
    print('Value of a is :',a) # 30
    print('Value of b is :',b) # 40
    return a + b

print(add(30,40))
'''

### Working with both  "non-default" and "default" arguments
'''
def add(a,b=20):
    print('Value of a is :',a) # 30
    print('Value of b is :',b) # 20
    return a + b

print(add(30))
'''

'''
def add(a,b=20):
    print('Value of a is :',a) # 30
    print('Value of b is :',b) # 40
    return a + b

print(add(30,40))
'''

# SyntaxtError
'''
def add(b=20,a):
    print('Value of a is :',a) # 30
    print('Value of b is :',b) # 20
    return a + b

print(add(30))
'''

## Note: In a function definition
'''
left side --->> Non-default arguments  required
right side ---->> default-arguments required
'''

# 3. Keyword  arguments
'''
def Employee(id, ename, salary, dept):
    print('Employee Id is :', id)
    print('Employee Name is :', ename)
    print('Employee Salary is :', salary)
    print('Employee Dept is :', dept)

Employee(1, 'Virat', 20000, 'HR')
'''

# What is output?
'''
def Employee(id, ename, salary, dept):
    print('Employee Id is :', id)
    print('Employee Name is :', ename)
    print('Employee Salary is :', salary)
    print('Employee Dept is :', dept)

Employee('Virat', 1, 'HR',20000)
'''

# What is output?
'''
def Employee(id, ename, salary, dept):
    print('Employee Id is :', id)
    print('Employee Name is :', ename)
    print('Employee Salary is :', salary)
    print('Employee Dept is :', dept)

Employee(ename='Virat', id=1, dept='HR',salary=20000)
'''


# What is output?
'''
def display(a,b,c):
    print('value of a is :', a)
    print('value of b is :', b)
    print('value of c is :', c)
    
display(10,20,30)
'''

# SyntaxError
'''
def display(a,b,a):
    print('value of a is :', a)
    print('value of b is :', b)
    print('value of c is :', c)
    
display(10,20,30)
'''

# What is output?
'''
def display(a,b,c,d):
    print('value of a is :', a)
    print('value of b is :', b)
    print('value of c is :', c)
    print('value of d is :', d)
    
display(10,20,d=40, c=30)
'''

# SyntaxError
'''
def display(a,b,c,d):
    print('value of a is :', a)
    print('value of b is :', b)
    print('value of c is :', c)
    print('value of d is :', d)
    
display(10,d=40, c=30, 20)
'''

## Note: At the time of calling function
'''
left side ----> positional arguments required
right side --->  keyword arguments required
'''

# 4. Arbitory | Variable length arguments (*args , **kwargs)
'''
def display(a,*b):
    print('value of a is :', a) # 10
    print('value of b is :', b) # (20, 30, 40, 50)
    
display(10,20,30,40,50)
'''

# What is output?
'''
def display(*a,b):
    print('value of a is :', a) # 10
    print('value of b is :', b) # (20, 30, 40, 50)
    
display(10,20,30,40,50)
'''

# What is output?
'''
def display(*a,**b):
    print('value of a is :', a) # (10, 20, 30, 40, 50)
    print('value of b is :', b) # {'eno': 101, 'ename': 'Ramu'}
    
display(10,20,30,40,50, eno=101,ename="Ramu")
'''

# SyntaxError
'''
def display(**b,*a):
    print('value of a is :', a) # (10, 20, 30, 40, 50)
    print('value of b is :', b) # {'eno': 101, 'ename': 'Ramu'}
    
display(10,20,30,40,50, eno=101,ename="Ramu")
'''

## Note: at the time of defininti function
'''
left side ---->> *argus  required
right side --->> **kwargs required
'''

##Note: at the time of defininti function
'''
left side ---->> non-default arguments

2nd position --->> default arguments  or  *args

3rd position --->>  *args   or  default arguments

right side ---->>  **kwargs  arguments
'''
##Note: at the time of Calling function
'''
left side --->>  positional arguments | non-keyword arguments

right side --->> keyword arguments
'''



word_dic={}

def wordcout(str):
    word_list=str.split()
    #print(word_list)
        
    for word in word_list:
        if word not in word_dic:
            word_dic[word]=1
        else:
            word_dic[word]=word_dic[word]+1

s = """hi ram hi how are you hello krishna what areyou doing
we will meet to night hi hello ")s'hi ram hi how are you hello
krishna what areyou doing we will meet to night hi hello
"""

wordcout(s)

print(word_dic)







## What is output?
'''
def display(a, b=20, *c, **d):
    print('value of a is :', a) # 10
    print('value of b is :', b) # 25
    print('value of c is :', c) # (30, 40, 50)
    print('value of d is :', d) # {'eno': 101, 'ename': 'Ramu'}
    
display(10,25,30,40,50, eno=101,ename="Ramu")
'''

## What is output?
'''
def display(a, *c, b=20, **d):
    print('value of a is :', a) # 10
    print('value of b is :', b) # 20
    print('value of c is :', c) # (25, 30, 40, 50)
    print('value of d is :', d) # {'eno': 101, 'ename': 'Ramu'}
    
display(10,25,30,40,50, eno=101,ename="Ramu")
'''

# SyntaxError
'''
def display(a, *c, b=20, **d):
    print('value of a is :', a) # 10
    print('value of b is :', b) # 20
    print('value of c is :', c) # (25, 30, 40, 50)
    print('value of d is :', d) # {'eno': 101, 'ename': 'Ramu'}
    
display(10,25,30,40,50, eno=101,ename="Ramu",60)
'''






















     



















