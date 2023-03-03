# voting2.py

'''
    Write a program that prompts the user
    to enter his/her age and citizenship
    status. Then reply that the user can
    legally vote or not.
'''

def main():

    age = int(input('Enter your age '))
    citizen = input('Are you a citizen y/n? ')

    if age >= 18 and citizen == 'y':
        print('You can legally vote.')
    else:
        print('You cannot vote')
        


main()

