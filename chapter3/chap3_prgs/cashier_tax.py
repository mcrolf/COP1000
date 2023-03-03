# cashier_tax.py

def main():

    SALES_TAX_RATE = 0.07

    # inputs
    item = input('Enter item description ')
    price = float(input('Enter unit price of the item '))
    quantity = int(input('Enter the quantity '))
    taxable = input('Is it taxable y/n? ')

    # processing
    subtotal = price * quantity
    if taxable == 'y':
        tax = subtotal * SALES_TAX_RATE
    else:
        tax = 0

    total = subtotal + tax
    
    # print a bill
    print(f'Subtotal ${subtotal:,.2f}')
    print(f'Sales tax ${tax:,.2f}')
    print(f'Total ${total:,.2f}')


main()
        
        

    
    
    
