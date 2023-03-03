#program2_2
#by Michael Napoli COP1000

def main():

    #prompt the user tro enter the numerator and denominator
    print('Enter the numerator and denominator of the fraction you would like to solve.')

    #entering the numerator and denominator
    numerator = int(input('Enter the numerator: '))
    denominator = int(input('Enter the denominator: '))

    #doing the maths
    wholeNumber = numerator // denominator
    remainder = numerator % denominator

    #output
    print(f'The mixed number is {wholeNumber} and {remainder}/{denominator}.')

main()