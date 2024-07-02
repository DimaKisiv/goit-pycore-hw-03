import random

#generates list fo random number within range and specified amount
def get_numbers_ticket(min, max, quantity):
    if (not validate(min, max, quantity)):
        print("Input data is not valid")
        return []
    return generate_list(min, max, quantity)

#process of generating here
def generate_list(min, max, quantity):
    list_of_numbers = []
    while(len(list_of_numbers) < quantity):
        random_number = random.randint(min, max)
        if random_number not in list_of_numbers:
            list_of_numbers.append(random_number)
    list_of_numbers.sort()
    return list_of_numbers

#vlidation of input values for generation 
def validate(min, max, quantity):
    if(min < 0 
    or min >= 1000 
    or max > 1000
    or max <= min 
    or quantity < 0
    or (max-min+1) < quantity): #when not enough range of numbers for unique list
        return False
    else: 
        return True
    

print(get_numbers_ticket(997, 999, 3))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(999, 999, 3))
