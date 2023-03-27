from function import display_fruit_price

fruit_type = input("what type of fruit that you want to buy?")
weight = input("how many kg to buy?")

result = display_fruit_price(fruit_type, weight)
print(result)







# def test_calculate_fruit_price():
#     # Test oranges
#     assert calculate_fruit_price('orange', 1) == 75
#     assert calculate_fruit_price('orange', 1.5) == 112.5
#     assert calculate_fruit_price('orange', 0.5) == 37.5
    
#     # Test mangoes
#     assert calculate_fruit_price('mango', 1) == 80
#     assert calculate_fruit_price('mango', 2.5) == 200
#     assert calculate_fruit_price('mango', 0.25) == 20
    
#     # Test watermelons
#     assert calculate_fruit_price('watermelon', 1) == 50
#     assert calculate_fruit_price('watermelon', 2) == 100
#     assert calculate_fruit_price('watermelon', 0.75) == 37.5
    
#     # Test invalid input
#     try:
#         calculate_fruit_price('banana', 1)
#         assert False, "Expected ValueError for invalid fruit type"
#     except ValueError:
#         pass
    
#     try:
#         calculate_fruit_price('orange', -1)
#         assert False, "Expected ValueError for negative weight"
#     except ValueError:
#         pass
    
#     try:
#         calculate_fruit_price('watermelon', 0)
#         assert False, "Expected ValueError for zero weight"
#     except ValueError:
#         pass
    
#     print("All test cases pass")



# def test_result_a_score_100():
#     score = 100
#     expected_result = "A"
#     actual_result = calculate_grade(score)
#     assert expected_result == actual_result