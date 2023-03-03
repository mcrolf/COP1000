#-------------------------------------------------------
#@program    program7_1.py       COP1000
#@author     Michael Napoli      2275778
#-------------------------------------------------------
'''
This program requires the main function and a custom value-returning function.
In the main function, code these steps in this sequence:
    use a list comprehension to generate 50 random integers all from -40 to 40, inclusive. These represent Celsius temperatures.
    use an f_string to report the lowest and highest Celsius temperature in the list.
    determine if 0C is in the list. If it is report the index where it first occurs. 
    If it isn't in the list, report that, too.
    use a random module method to create a sublist of 10 unique Celsius temperatures.
    sort this sublist in ascending order.
    pass the Celsius sublist as the sole argument to the custom value-returning function.
In the custom function:
    use either a loop or a list comprehension to create a list of 10 Fahrenheit temperatures equivalent to the Celsius temperatures. 
    A bonus of 3 points will be awarded if a list comprehension is employed.
    return the Fahrenheit list to main.
Back in main:

    use a for loop and the range function to print a table showing the equivalent Celsius and Fahrenheit temperatures in columns with widths that you choose.
    include column headings and display the averages as shown below
'''
import random

def main():
    temps_c= []                                                                   # temps_c is an empty list
    for n in range(50):                                                           # for a total of 50 numbers
        temps_c.append(random.randint(-40,40))                                    # make each value a random integer from -40 to 40
    print(f"lowest temp is {min(temps_c)}C and Highest temp is {max(temps_c)}C")  # formatted output for lowest and highest temps in the list
    
    if 0 in temps_c:                                                              # if zero is in the sublist
        print(f"Found 0C at index {temps_c.index(0)+1}")                          # formatted output for zero and its index in the list
    else:
        print(f"0C was not in this list")                                         # formatted output if zero not in list
    
    sublist_temps= random.sample(temps_c,k=10)                                    # the sublist is a random sample of 10 items from the list
    sublist_temps.sort()                                                          # sort sublist from least to greatest
    
    print(f"{'CELSIUS'} {'FARENHEIT'}")                                           # header for conversion output
    temp_av= 0                                                                    # accumulator for temp avg
    ctof= [float(temp * (9/5) + 32) for temp in sublist_temps]
    for temp in sublist_temps:     
        temp_av += temp                                                           # add to average temp accumulator
        print(f"{temp:<10d} {ctof:.1f}")                                          # formatted output for temps in c and f
    
    temp_av /= len(sublist_temps)                                                 # the average temp is the accumulated values divided by the number of items in the list
    
    print()                                                                       # blank space
    print(f"{temp_av:<10.1f} {ctof:.1f}     <--- averages")                       # formatted print for the averages

# def c_to_f(sublist_temps):                                                        # pass in the sublist as the argument for the function c to f
#     return float(sublist_temps * (9/5) + 32)                                      # return the values of the sublist converted to fahrenheit

main()