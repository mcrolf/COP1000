#-------------------------------------------------------------------------
#@program        filereader.py         COP1000
#@author         Michael Napoli        2275778
#-------------------------------------------------------------------------

def read_database(file_name):
    newline= "\n"                                                           # variable used to identify separate data values
    newline_count= 2                                                        # each entry contains 2 lines
    database= open(file_name,"r")                                           # opens the database
    data_raw= database.read()                                               # prep database
    data= data_raw.split(newline)                                           # split the data into a list
    print_rows(data,newline_count)                                          # prints a row of formatted data for each entry, also average age

    database.close()                                                        # closes database after print

def print_rows(data,newline_count):                                         # define print_rows function
    avg_age= 0                                                              # set up accumulator for average age
    data_length= (len(data)-1)                                              # count number of times the newline character. -1 because there is an extra at the end
    data_entry_count= data_length // newline_count                          # gets total number of complete entries
    
    for a in range(0,data_length,newline_count):                            # for each entry
        name= data[a + 0]                                                   # the name is the first entry
        age= data[a + 1]                                                    # the age is the second entry
        print(f'My friend {name} is {age}')                                 # print the name and age of the friend from the entry
        avg_age += int(age)                                                 # adding age to average age accumulator
    
    avg_age= avg_age / data_entry_count                                     # get average age
    print(f'The average age of friends is {age:,.1f}')                      # printing formatted average age

def main():                                                                 # main function
    file_name= 'friends.txt'                                                # file name for database file
    read_database(file_name)                                                # opens the database at the file name

main()