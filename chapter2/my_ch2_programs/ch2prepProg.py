#prep program
#by Michael Napoli

def main():
    
    #prompt user for test scores
    print('Input the test scores: ')

    #inputting test scores
    test_one = float(input('Test 1: '))
    test_two = float(input('Test 2: '))
    test_three = float(input('Test 3: '))
    
    #maths
    test_all = test_one + test_two + test_three
    test_avg = test_all / 3

    #output
    print(f'the average of these scores is {test_avg:.2f}%.')

main()