#problem-solving one
#by Michael Napoli

def main():
    #prompt the user for height input
    print('Input your height: ')
    #asks the user to input amount of feet and inches as separate inputs
    h_ft = int(input('Feet: '))
    h_inch = int(input('Inches: '))
    #unit conversions
    h_inch += h_ft * 12
    h_cm = round(h_inch * 2.54, 1)

    print('Your height is : %d cm.' % h_cm)

main()