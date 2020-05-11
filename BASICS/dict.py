# prices = {'apple': 0.50, 'banana': 0.50}
# my_purchase = {
#         'apple': 1,
#         'banana': 1
# }
# grocery_bill = sum(prices[fruit] * my_purchase[fruit]
#                                       for fruit in my_purchase)
# print ('I owe the grocer $%.2f' % grocery_bill)

dogStrength = {'boxers': 5, 'labs': 3}
combined_Strength = {
    'boxers': 1,
    'labs': 1
}
total_strength = sum(dogStrength[dog] * combined_Strength[dog]
                     for dog in combined_Strength)
print('Total Strength from Dogs is %.2f' % total_strength)
