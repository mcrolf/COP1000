#------------------------------------------------------------------------------
#@program      filemaker.py        COP1000
#@author       Michael Napoli      2275778
#------------------------------------------------------------------------------

is_open= False                                                            # initialize is_open as false

def write_entry(database,data_entry):                                     # define write_entry function
    database.write(str(data_entry))                                       # writing to the database pasing in data_entry as a string

def main():
    file_name= 'friends.txt'                                              # naming the file friends.txt
    database= open(file_name,'w')                                         # open the file in write mode
    is_open= True                                                         # saying the file is now open
    prompt1= 'Enter the first name of a friend (or Enter to Quit): '      # prompt1 asks the user to enter the name or press enter to cancel
    prompt2= 'Enter the age (integer) of this friend: '                   # prompt2 asks the age of the friend as an integer

    while is_open:                                                        # while the file is open
        prompt1_ans= input(prompt1)                                       # ask for the answer to prompt1
        if prompt1_ans == "":                                             # if prompt1 recieves enter key as input
            database.close()                                              # close the database
            is_open= False                                                # saying the database is not open
            print('The file has been created')                            # print that the file has been created
        else:                                                             # if a responce to prompt1 is entered
            prompt2_ans= int(input(prompt2))                              # ask for the answer to prompt2
            data_entry= prompt1_ans + "\n" + str(prompt2_ans) + "\n"      # format data entry
            write_entry(database,data_entry)                              # writes the data to the file
main()