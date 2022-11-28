'''
# define variables
a_int = 2
b_int = 3

a_string = "Edward"
b_string = "Amoah"

# simple basic operations functinos
def addition(a,b):
    return a + b

def substraction(a,b):
    return a - b

## int operations 

c = addition(a_int, b_int)

print(c)

d = substraction(a_int, b_int)

print(d)

## string operations 

e = addition(a_string, b_string)

print(e) 

f = substraction(a_string, b_string) # this operation will fail because you can't substract a string from another string

print(f)
'''

############# LESSON 2

name_1 = "Edward"
name_2 = 'Edwardd'
name_3 = "Amoah"

age_1 = 45
age_2 = 25
age_3 = 15
age_4 = 25


height_1 = 2.5
height_2 = 5.3
height_3 = 45.0 

def equals(a,b):
    return a == b

def not_equals(a,b):
    return a != b

def greater_than(a,b):
    return a > b

#print(equals(name_1, name_2))

answer = greater_than(name_2, name_1) 
print(answer)

#print(not_equals(name_1, name_2))
