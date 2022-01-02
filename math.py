#Add Implementation
#Addition
def add(x,y):
	return x+y

#Subtract Implementation
#Subtraction
def subtract(x,y):
	return x-y      #on master branch

#Multiplication
#Multiply Implementation
def multiply(x,y):
	return x*y        #on Bug456 branch

#Division
#Divide Implementation
def divide(x,y):
	if y==0:         #on master branch
	    return DIVIDE_BY_0_ERROR
	else:
	    return x/y

def square(x):
	return x*x
