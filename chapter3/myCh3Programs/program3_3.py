#program3_3   COP1000
#by Michael Napoli   2275778

def main():

    #prompt the user to enter a two digit number
    first_number= int(input('Enter a two-digit integer: '))

    #determining if the first input is a two digit number, if yes, enter a second input
    if (first_number < 100 and first_number > 9):
        second_number= int(input('Enter another DIFFERENT two-digit integer: '))
        #determining if the second input is a two digit number
        if (second_number < 100 and second_number > 9):
            #if the first input is larger than the second, subtract the second value from the first and output the difference
            if (first_number > second_number):
                diffVal= first_number - second_number
                print(f'{first_number} is larger than {second_number} by {diffVal}.')
            #if the first input is not larger than the second, subtract the first value from the second and output the difference
            else:
                diffVal= second_number - first_number
                print(f'{second_number} is larger than {first_number} by {diffVal}.')
        #if the second input is not two digits, fail
        else:
            print("That's not a two-digit number! Try again")
    #if the first input entered is not two digits, fail
    else:
        print("That's not a two-digit number! Try again")

main()