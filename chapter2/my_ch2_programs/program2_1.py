#program2_1
#by Michael Napoli COP1000


def main():
    #defining variables
    miles= float()
    kilometers= float()
    
    #the input prompt
    miles=float(input('Enter number of miles to convert to kilometers: '))
    
    #conversion
    kilometers= miles* 1.60934
    
    #the output
    print(f'there are {kilometers:.3f} km in {miles} mi.')
 
main() #perform the main function