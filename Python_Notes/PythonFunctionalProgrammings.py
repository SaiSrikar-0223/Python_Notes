
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


















