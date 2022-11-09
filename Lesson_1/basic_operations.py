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