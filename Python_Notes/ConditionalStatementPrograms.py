
'''
print('Welcome')

n1 = int(input('Enter first number :'))

n2 = int(input('Enter second number :'))

result = n1 + n2

#print(result)
#print("The Sum is :",result)

print('The sum of',n1,"and",n2,"is :", result)
'''


### simple  if  ###

# if condition return True
'''
print('start line')

if 10 > 5:
    print('hello 1')

print('end line')
'''

# if condition return False
'''
print('start line')

if 10 > 15:
    print('hello 1')

print('end line')
'''

## What is output?
'''
print('start line')

if 10 > 5  and 20 < 30:
    print('hello 1')

print('end line')
'''

### if - else

# if condition return True then if block executing
'''
print('start line')

if 10 > 5:
    print('hello 1')

else:
    print('hello 2')
    
print('end line')
'''

# if condition return False then else block executing
'''
print('start line')

if 10 > 15:
    print('hello 1')

else:
    print('hello 2')
    
print('end line')
'''

### if - elif - else
'''
print('start line')

if 10 > 15:
    print('condition 1')

elif 20 > 30:
    print('condition 2')

elif 200 > 30:
    print('condition 3')
    
else:
    print('else block')
    
print('end line')
'''


## How to validate a Student is Failed or Passed?
'''
marks = int(input('Enter Student marks :'))

if marks < 0 or marks > 100:
    print('Please enter valid marks between 0-100')

elif marks < 35:
    print('Sorry! Student failed.')

elif marks < 60:
    print('Congrats! Student passed with 2nd grade.')

else:
    print('Congrats! Student passed with 1st grade.')

print('end line')
'''

## How to find the biggest number among given Two numbers ?
'''
n1 = int(input('Enter first number :'))
    
n2 = int(input('Enter second number :'))

if n1 > n2:
    print(n1,"is a biggest number than",n2)
else:
    print(n2,"is a biggest number than",n1)
'''

## How to find the biggest number among given Three numbers ?
'''
n1 = int(input('Enter first number :'))
    
n2 = int(input('Enter second number :'))

n3 = int(input('Enter third number :'))

if n1 > n2 and n1 > n3:
    print(n1,"is a biggest number than",n2,"and",n3)

elif n2 > n3:
    print(n2,"is a biggest number than",n1,"and",n3)
  
else:
    print(n3,"is a biggest number than",n1,"and",n2)
'''
    
###
'''
print("The Maximum Number is :",max([10,50,20,70,30]))

print("The Minimum number is :",min([10,50,20,70,30]))

print("The Sum is :", sum([10,50,20,70,30]))
'''

##
'''
name = input('enter your name :')
print('Hello', name)
'''




























