#these are comments, do not run in code
#variables store data
#Python is a weakly language - means you do not have to declare data types before assigning value

#Python does have data types like any other language - they are just not explicit
#data types define what type of data can be store in a variable (numerical, text, etc..)
#python following basic data types

#integer or int - whole numbers
#float - decimal number
#string or str - strings/text non numerical
#bool - True or False

x = 8 #int
y = 3.85 #float
name = "John" #string
is_student = True #bool

#variables hold data and are like nouns
#however we will be using functions.  We will start with pre-built functions that are part of python
#functions perform actions or calculations
#they are denoted by the () (you will know something is a function by () )
#the text you put inbetween the () are called arguments, it is used to pass data to the function

#one prebuilt function we will use is the print function
#it displays data on screen, based on what you use as an argument
print(x)
print(y)
print(name)
print(is_student)

#you can also just print raw text, and we can append a variable as text using ,
print("Hello", name)

#another function we will use is the input() function
#input allows a user to give the program some information to process from the user
#the data is store in a variable, and by default comes in as a string
#syntax is variable_name = input(prompt_text)
username = input("What is your username ")
print("Your username is", username)

#variables, like any other programming language, can change throughout the program
#you can use the current value of a variable in its *own* calculation

#if I have x = 8, I can say x = x + 2 which would equal 10.  It take current value of x as part of calculation
x = 8
x = x + 2
print(x)