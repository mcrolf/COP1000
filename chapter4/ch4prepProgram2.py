#ch4 prep program   COP 1000
#by Michael Napoli  2275778

def main():
    #printing the header for the output.
    print(f'|{"Number":<8}|{"SQUARE":^10}|{"CUBE":>16}|')
    
    for x in range(5,51,5): #for a number in the range between 5 and 50, increasing by 5.
        square= x**2        #x^2
        cube= x**3          #x^3
        print(f'{x:<7}\t{square:^8,}\t{cube:>12,}') #printing the base number on the left, square in the middle, and cube on right.

main()