# author: Tony Moulden
# date: 07/02/2021
#
# description: variables excersize

# --------------- Section 1 --------------- #

# 1.1 | Variable Creation | Strings
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that holds your name.
#   2) Create a variable that holds your birthday.
#   3) Create a variable that holds the name of an animal you like.
#
# Print
#   4) Print each variable, describing it when you print it.
#
# Example Code
example_name = 'elia'
print('EXAMPLE: my name is', example_name)

# WRITE CODE BELOW
name = 'Tony'
print('my name is', name)
birthday = 'October 30th'
print('my bithday is', birthday)
animal = 'Vulture'
print('one of my favorite animals is a', animal)


# 1.2 | Variable Creation | Integers / Floats
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# All variables created in this section should hold either an integer or float.
#
# Variables
#   1) Create a variable that holds your favorite number.
#   2) Create a variable that holds the day of the month of your birthday.
#   3) Create a variable that holds a negative number.
#   4) Create a variable that holds a floating (decimal) point number.
#
# Print
#   5) Print each variable, describing the value you print.

# WRITE CODE BELOW
favnum = '22'
print('my favorite number is', favnum)
bday = '10/30'
print('the day of my birthday is', bday)
neg = '-22'
print('the negative number Iv\'e chosen is', neg)
float = '0.22'
print('my floating number is', float)


# 1.3 | Overwriting Variables
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Overwrite the variable holding your name, and save a different name to it.
#   2) Overwrite the variable holding birthday with the day you think would be best to have a birthday on.
#   3) Overwrite the variable holding your favorite number and set it to a number you think is unlucky.
#
# Print
#   4) Print the variables you've overwritten, describing the values you print.
#
# Example Code
example_name = 'lucia'
print('EXAMPLE: my new name is', example_name)

# WRITE CODE BELOW
name = 'Moulden'
print('my new name is', name)
birthday = 'Friday'
print('the best day to have my birthday on is', birthday)
favnum = '99'
print('If i had to chose it would have to be', favnum)


# 1.4 | Operations
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that is the sum of two numbers.
#   2) Create a variable that is the product of three numbers.
#   3) Create a variable by dividing the previously created sum, with the previously created product.
#
#   4) Create a variable that is the concatenation of your name and an animal you like (use the variables!)
#   5) Create a variable that is an acronym (like 'lol') multiplied by your birth day.
#
#   6) Create a variable that is difference of itself minus the number you think is unlucky.
#   7) Overwrite the lucky variable with the itself squared.
#
# Print
#   7) Print all the new variables you've created along with what the represent
#
# Example Code
example_sum = 11 + 21
print('EXAMPLE: the sum of 11 and 21 is', example_sum)

# WRITE CODE BELOW
sum = 21 + 1
print('the sum of 21 and 1 is', sum)
product = 11 * 2 * 1
print('the product of 11, 2, and 1 is', product)
divide = sum / product
print('this is what I got', divide)
mashup = 'ton' + 'cheetah'
print('this is what I got', mashup)
weird = 'omg' * 30
print('this is it', weird)
mathstuff = 122 - 99
print('this is the number', mathstuff)
favnum = 22 ^ 22
print('This is it squared', favnum)
