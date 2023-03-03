#-------------------------------------------------------------------------
#@program      program6_1.py        COP1000
#@author       Michael Napoli       2275778
#-------------------------------------------------------------------------
'''
This program prompts the user to enter an item that is on sale,
prompts the user to enter the retail price, then prompts the user to
enter the discount as a percent.
'''

is_open= False                                                                 # the file starts as not open

def write_entry(database,data_entry):
    database.write(str(data_entry))                                            # write to the database passing data_entry

def main():
    file_name= 'betterbuysale'                                                 # naming the file
    database= open(file_name, 'w')                                             # opens the file in write mode
    is_open= True                                                              # the file is now open
    prompt1= 'Enter item name (or press enter to quit): '                      # prompt for entry 1
    prompt2= "Enter item's regular price: "                                    # prompt for entry 2
    prompt3= "Enter price reduction as a percent: "                            # prompt for entry 3
    while is_open:
        prompt1_ans= input(prompt1)                                            # prompt1 answer is the user input
        if prompt1_ans == "":                                                  # if the user hits the enter or retuen key
            database.close()                                                   # close the database
            is_open= False                                                     # the file is not open
            print(f'the file {file_name} has been created')                    # prompts the user that the file has been created
        else:
            prompt2_ans= float(input(prompt2))                                                  # the answer for prompt2 is entered as a float value
            prompt3_ans= int(input(prompt3))                                                    # the answer for prompt3 is entered as an integer
            data_entry= prompt1_ans + '\n' + str(prompt2_ans) + '\n' + str(prompt3_ans) + '\n'  # the data entered is the item, retail price, and sale percent on separate lines
            write_entry(database,data_entry)                                                    # write the entry to the database

main()                                                                         # runs the main function