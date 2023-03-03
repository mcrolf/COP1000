#program2_3
#by Michael Napoli COP1000

from re import sub


def main():
    #defining variables
    itemPrice= float()
    itemQuantity= int()
    
    #prompt the user to enter the price and quantity of items
    print('Time to check out: ')

    #entering the price and quantity
    itemPrice = float(input("Enter the item's price: "))
    itemQuantity = int(input('Enter the number of items: '))

    #doing the math to add up the items and calculate sales tax
    subTotal = itemPrice* itemQuantity
    salesTax = subTotal* (.07)
    grandTotal = subTotal + salesTax

    #print the output
    print(f'The subtotal is ${subTotal: ,.2f}.')
    print(f'The sales tax is ${salesTax: ,.2f}.')
    print(f'You pay: ${grandTotal: ,.2f}.')

main()