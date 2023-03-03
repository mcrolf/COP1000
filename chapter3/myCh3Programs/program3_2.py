#program3_2   COP1000
#by Michael Napoli   2275778

def main():

    #user input and defining the number the user enters
    your_number= int(input('Enter an odd multiple of 19 that is more than 60 and less than 200: '))

    #defining bounds and factor value
    upper_bound= 200
    lower_bound= 60
    factor= your_number / 19
    
    #output    
    #if the user input is an integer between the upper and lower bounds, and the factor is an odd number, return the factor in the output.
    if your_number in range (lower_bound,upper_bound) and factor % 2 == 1:
        print(f'Good Job! Your factor is {factor}')
    #if the number is not within range or the factor is not an odd number, return incorrect input.
    else:
        print('Incorrect Input')

main()