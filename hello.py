# This program says hello and ask for my name

print('Hello word!')
print('what is your name?')  # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('what is your age?')  # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

# Type programs into the file editor (not in the interactive shell window with the >>> prompt)
# The execution starts at the top and moves down.
# Comments begin with a # character and are ignored by Python; they are notes & reminders for the programmer.
# Functions are like mini-programs in your program.
# The print() function displays the value passed to it.
# The input() function lets users type in a value.
# The len() function takes a string value and returns an integer value of the string's length.
# The int(), str(), and float() functions can be used to convert values' data type.
