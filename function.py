def validate_input(fruit_type,weight):
    if fruit_type not in ['orange', 'mango', 'watermelon'] or weight <= 0 :
        return "Invalid fruit type. Must be one of 'orange', 'mango', or 'watermelon' and Weight must be greater than 0"
    else:
        return calculate_fruit_price(fruit_type,weight)
    # elif fruit_type in ['orange', 'mango', 'watermelon']:
    #     return "pass"
    
    # if weight <= 0:
    #     return "Weight must be greater than 0"
    # elif weight >0 :
    #     return "pass"
    
def calculate_fruit_price(fruit_type,weight):
    if fruit_type == 'orange':
        price_per_kg = 75
    elif fruit_type == 'mango':
        price_per_kg = 80
    else:
        price_per_kg = 50
    # Calculate the total price
    total_price = price_per_kg * weight
    return total_price

def display_fruit_price(fruit_type,weight):
    result = validate_input(fruit_type,weight)
    if not result:
        return calculate_fruit_price(fruit_type,weight)
    else:
        return result