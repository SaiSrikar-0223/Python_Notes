
### Syntax Errors  ####

# SyntaxError
'''
print('hello 1')

 print('hello 2')
'''

# SyntaxError
'''
a = 10
print a
'''

# SyntaxError
'''
if 10 > 5:
    print('hello 1')
    print('hello 2')

print('hello hi')

else:
    print('hello 3')
    print('hello 4')
'''

# SyntaxError
'''
for  in range(10):
    print(i)

'''

# SyntaxError
'''
def add(x=10,y):
    print(x)
    print(y)
    print(x + y)

add(20)
'''

# SyntaxError
'''
def add(x,y=20):
    print(x)
    print(y)
    print(x + y)

add(y=25,30)
'''


### Working with Runtime  Errors  ####

#IndexError: list index out of range
'''
print('start line')

lst = [10,20,30]

print(lst[4])

print('end line')
'''


# Using without exception handling  returns FileNotFoundError:
'''
print('start line')

fileobject = open('demo.txt', 'r') 

print('end line')
'''

# Using exception handling returns user friendly message
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r')
except:
    print('Given file name not available')

print('end line')
'''

## if raised exception class is  handling  proprly by excepty block then returns exception message
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError
    
except FileNotFoundError:
    print('Given file name not available')

print('end line')
'''

## if raised exception class is not handling by excepty block then returns exception
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError
    
except NameError:
    print('Given file name not available')

print('end line')
'''

## Working with "else" block ###
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError
    
except NameError:
    print('Given file name not available')

else:
    data = fileobject.read()
    print(data)
    
print('end line')
'''

# try block with multiple named exception blocks
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError

except NameError:
    print('Error : NameError returns')

except ValueError:
    print('Error: ValueError returns')
    
except FileNotFoundError:
    print('Given file name not available')

else:
    data = fileobject.read()
    print(data)
    
print('end line')
'''

#  try block with multiple named exception blocks and defalt except block
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError

except NameError:
    print('Error : NameError returns')

except ValueError:
    print('Error: ValueError returns')
    
except KeyError:
    print('Given file name not available')

except:
    print('Some thing wrong')
else:
    data = fileobject.read()
    print(data)
    
print('end line')
'''


## SyntaxError
'''
print('start line')

try:
    fileobject = open('demo.txt', 'r') # FileNotFoundError

except NameError:
    print('Error : NameError returns')

except ValueError:
    print('Error: ValueError returns')

except:
    print('Some thing wrong')
    
except KeyError:
    print('Given file name not available')


else:
    data = fileobject.read()
    print(data)
    
print('end line')

'''
















    
