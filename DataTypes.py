print(1+7)
print("Hello World")
a=8
if(a>6):
    print("a is greater")
else:
    print("a is smaller")


##Variables in Python
age=32
name="Swati" 
height= 5.2

print(age, name, height)

#Python allows to change variable during run time
var= 10
print(var, type(var))

var="Hello"
print(var, type(var))

var= 6.2
print(var, type(var))

#Getting input from the user

age=input("What is the age")
print(age, type(age)) 

##Type is returned as int but we know it's age and it should be int so we can type cast it

age=int(input("What is the age?"))
print(age, type(age))

##Simple calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number:"))

addition = num1 + num2
subtraction = num1- num2
product = num1*num2
quotient= num1/num2

print("Addition: ",addition)
print("Subtraction: ", subtraction)
print("Product: ", product)
print("Quotient: ", quotient)


