#in python we can use the , in the print function to display variable values
#this can be cumbersome if we want to display multiple values in different parts of the sentence
#we may also want to format our variables to look a certain way
#the f-string help us format variables with in a string using string interpolation
#string interpolation has a bunch of cool features, a couple we will use below

name = "Zach"
age = 40
money = 45.258418
years_since_year_zero = 2026

print(f"Hello, my name is {name} and I am {age} years old")

#you can also do inline expressions if you want (calculations)
print(f"Next year, I will be {age + 1} years old")

#you can format by rounding or dropping decimals
print(f"Your change is {money:.2f}")

#you can use comma separators
print(f"It has been {years_since_year_zero:,} since AD 0")


#inline debug formatting
print(f"{name=}")