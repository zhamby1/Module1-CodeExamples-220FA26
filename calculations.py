#calculations in python consist of your typical math calcs

#adding
x = 7
y = 8
sum = x + y
print(sum)

#subtraction
a = 10
b = 3
difference = a - b
print(difference)

#multiplication
c = 10
d = 11
product = c * d
print(product)

#division
e = 10
d = 2
quotient = e / d
print(quotient)

#integer division - will drop anything after the decimal place
g = 31
h = 2
integer_quotient = g // h
print(integer_quotient)

#exponent
i = 2
j = 3
exponent = i ** j
print(exponent)

#modulo - remainder of a division calculation
k = 100
l = 7
remainder = k % l
print(remainder)

#how do we do calculations with inputs
#conversions - python inputs come in as strings by default..strings can only be combine or concatonated
number1 = "5"
number2 = "10"
total = number1 + number2
print(total)

#so we have to parse or convert a string input into a numerical value like a float or int
#python has built in functions to do this
#int() - converts values to an integer
#float() - converts values to a float

#in python we can chain functions together on one line to get an input and convert at the same time
number3 = int(input("Please give me a number to add "))
number4 = int(input("Please give me another number to add "))
myanswer = number3 + number4
print(myanswer)

#float conversion
money1 = float(input("Please enter the amount of money you wish to add "))
money2 = float(input("Please enter the second amount of money you wish to add "))

mytotal = money1 + money2
print(mytotal)