# voting.py

'''
    Write a program that prompts the user
    to enter his/her age and citizenship
    status. Then reply that the user can
    legally vote or not.

    Pseudocode
    prompt for age
    prompt for citizen status
    if user is 18 or older
        if user is a citizen
            print user can vote
        else
            print user cannot vote
'''

def main():

    age = int(input('Enter your age '))

    if age < 18:
        print('You are not old enough to vote')
    else:
        citizen = input('Are you a citizen y/n? ')
        if citizen == 'y':
            print('You can legally vote.')
        else:
            print('You are old enough but you have to be a citizen')
        





main()

