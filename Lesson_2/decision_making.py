# Decision Making for Farmer Resilience

baseline = [1,3,4,2,4,1,3,2,4,2] # list of numbers [1,4]
endline = [2,3,4,4,4,2,3,2,4,2] # list of endline scores

# 

farmer_1_baseline = 1
farmer_2_baseline = '3.0'

farmer_1_endline = 2
farmer_2_endline = '4.0'

def greater_than(a,b):
    return a > b

farmer_1_score_increase = greater_than(farmer_2_endline, farmer_2_baseline)
#print(f"Farmer 2's score increase: {farmer_1_score_increase}")

# decision making
'''
if statement:
    CODE for true
else:
    code for false

if statement:
    code for true 


if statement_1:
    code for true 1
elif statement_2:
    code for ture 2
else:
    code for false
'''

print()
print()

if greater_than(farmer_2_endline, farmer_2_baseline):
    print("Farmer's score increase")

else:
    print("Farmer's score did not increase")

    

# equals     
if farmer_1_endline == farmer_1_baseline:
    print("Farmer's 1 score is the same")
else:
    print("Farmer's 1 score is not the same")

## Homework ##
###### if elif else statements #######
    
#### use the python comparison operators as statements ####
    
#### different string, float, int ######
