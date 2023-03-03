#---------------------------------------------------------------
#@program       program6_2.py        COP1000
#@author        Michael Napoli       2275778
#---------------------------------------------------------------
'''
This program reads the file created by program6_1
'''

def read_database(file_name):                                    # function to read the file
    line= '\n'                                                   # recognizing each line by the string "\n"
    line_count= 3                                                # the number of lines per entry is 3
    database= open(file_name, 'r')                               # open the file in read mode
    data_raw= database.read()                                    # the raw data is read
    data= data_raw.split(line)                                   # the data is split into separate lines
    print_rows(data,line_count)                                  # printig rows for each set of data

    database.close()                                             # close the database

def print_rows(data,line_count):                                                         # function to print the rows of data  
    data_length= (len(data)-1)                                                           # count number of times "\n" and -1 because of the extra new line at the end
    data_entry_count= data_length // line_count                                          # gets total number of complete entries
    print(f'{"Items":<13}|{"reg_price":^16}|{"price_reduction":^16}|{"sale_price":10}')  # formatted header with titles for columns
    print('--------------------------------------------------------------')              # divides the header from the body

    for a in range(0,data_length,line_count):
        item= data[a + 0]                                                                       # the item is the first data entry
        reg_price= float(data[a + 1])                                                           # regular price is the second data entry
        percent_reduce= float(data[a + 2])                                                      # percent reduction is the third data entry
        reduction= reg_price * (percent_reduce/100)                                             # reduction in price is the regular price times the reduction as a percent
        sale_price= reg_price - reduction                                                       # the sale price is the regular price minus the reduction amount
        print(f'{item:<12} | {reg_price:^14,.2f} | {reduction:^14,.2f} | {sale_price:10,.2f}')  # formatted output for items and pricing values
    
def main():
    file_name= 'betterbuysale'                                    # the file name
    read_database(file_name)                                      # this command reads the file

main()                                                            # calls main function    