#ch3 prep program COP1000
#by Michael Napoli 2275778

from traceback import print_exception


def main():
    
    #defining base variables
    coffeePrice= float()
    coffeeAmount= int()
    salesTax= float()
    shippingCost= float()
    grandTotal= float()

    
    #prompt the user to input the amount of cofee they would like
    print('Time to proceed wit your order! ')

    #entering quatity of coffee
    coffeeAmount= int(input('How many pounds would you like? '))
    #defining difference in pricing by amount
    if coffeeAmount <= 9:
            coffeePrice= 12
    if 10 <= coffeeAmount < 20:
            coffeePrice= 10 
    if 20 <= coffeeAmount < 40:
            coffeePrice= 8.75
    if 40 <= coffeePrice:
            coffeePrice= 7.5
    
    #defining calculated costs
    subtotal= coffeeAmount * coffeePrice
    salesTax= subtotal * 0.07
    shippingCost= coffeeAmount
    if subtotal > 150:
        shippingCost = 0
    grandTotal= subtotal + salesTax + shippingCost

    #output
    print(f'Cost of coffee: ${subtotal:.2f}')
    print(f'7% Sales Tax: ${salesTax:.2f}')
    print(f'The shipping cost is: ${shippingCost:.2f}')
    print(f'Total payable amount: ${grandTotal:.2f}')

main()