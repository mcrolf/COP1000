# range_test.py

'''
    Prompt for an odd integer between 200
    and 300 that is also a multiple 17.
'''

def main():

    num = int(input('Enter an odd integer between 200 and 300 that is also a multiple 17 '))

    if num % 2 == 1 and num > 200 and num < 300 and num % 17 == 0:
        print(f'{num} is good')
    else:
        print(f'{num} is incorrect')


main()
