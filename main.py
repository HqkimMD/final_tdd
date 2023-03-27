from function import display_fruit_price

print("what type of fruit that you want to buy?")
fruit_type = input()
print("how many kg to buy?")
weight = int(input())

result = display_fruit_price(fruit_type, weight)
print(result)
