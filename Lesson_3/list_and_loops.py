### list ### 

# We have 5 farmers, each farmer has a baseline and endline resilience value 

farms_baseline = [1, 2, 3, 2, 1] # farmers baseline 
farms_endline = [1, 4, 3, 3 ,5] # famers endline

# accessing list values
print()
'''
index = 0
print(f"Farmers {index+1} baseline resilience is {farms_baseline[index]}") # the fisrt element/value is referenced as zero

index = 1
print(f"Farmers {index+1} baseline resilience is {farms_baseline[index]}")

index = 2
print(f"Farmers {index+1} baseline resilience is {farms_baseline[index]}")

index = 3
print(f"Farmers {index+1} baseline resilience is {farms_baseline[index]}")

index = 4
print(f"Farmers {index+1} baseline resilience is {farms_baseline[index]}")
'''

##### for loops #####

# if statement:
#   action 
# else:
#   else-action

# for statement-condition:
#   actions

#print(f"Farmers {farms_baseline.index(farmer)+1} baseline resilience is {farmer}")

'''
for farmer_baseline in farms_baseline:
    print(farmer_baseline)
'''

#### while loop ####

index = 0  
while index < 5:
    print(farms_baseline[index])
    index = index + 1 


#### homework ####

### 1. print the endline with for and while loop ###
### 2. write a for loop to check if the endline is greater the baseline for each farmer ####