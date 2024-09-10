# calculate discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        
        #calculates if the discount_percent is above 20%
        discounted_price = price * (discount_percent / 100)
        price_after_discount = price - discounted_price

        #returns the final price  after applying the discount
        return price_after_discount
    
    #returns the original price if the discount_percent is less than 20%
    else:
        return price
    

    #added a user input for both original price and discount percentage

original_price_input = float(input('Enter the original price: '))
discount_percent = float(input('Enter the discount percentage: '))

#get the final price 

final_price = calculate_discount(original_price_input, discount_percent)
print(f'The final price after the discount is: {final_price}')
    
