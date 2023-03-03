#--------------------------------------------------------------
#@program     program9_1.py      COP1000
#@author      Michael Npaoli     2275778
#--------------------------------------------------------------
'''
Write a program that stores current grades in a dictionary,
with course codes as keys and percent grades as values. 
Start with an empty dictionary and then use a while loop to 
enable input of course codes and percent grades from the keyboard. 
Enter data for at least five courses. After entering the data, 
use a for loop and the keys to show the current status of all courses. 
This same loop should include code that enables determination 
of the worst course and the average of all courses. 
Both of these findings should be printed when the loop ends. 
The worst course should be dropped and reported. 
This being done, the program should use another loop and the 
items method to display the revised courses and grades and 
report the revised term average.
'''
def grades():
    term_grades= {}                                                   # starting with empty dict.
    course_count= len(term_grades)                                    # the number of courses is the number of elements in the dict.
    course= input("Enter course code or press enter to quit: ")       # prompt user to enter course code or press enter to quit
    termtotal= 0                                                      # accumulator for all grade points. start at zero
    
    while course != "":                                               # while course is not enter to quit 
        grade= int(input("enter the grade for the course as %: "))    # prompt user to enter grade
        term_grades[course]= grade                                    # grade is the value for the key entered as course
        course_count= len(term_grades)                                # take a count of the number of elements in the dict.
        termtotal += grade                                            # add the grade to the accumulator
        course= input("Enter course code or press enter to quit: ")   # prompt user to enter another course

    for course,grade in term_grades.items():
        print(f"Grade in {course} is {grade}%")                       # formatted output for courses and grades in term_grades

    termavg= termtotal/course_count                                   # calculating the average of all grade values in the dict
    print(f"curent term average is {termavg:.2f}%")                   # formatted print for average grade values

    
    mingrade= min(term_grades.values())                               # detecting the minimum grade value and assigning it to mingrade
    for course in term_grades.keys():                                 # for the key 'course' in the dict.
        if term_grades[course] == mingrade:                           # if the value for a course is equal to the minimum grade
            mincourse = course                                        # assign the lowest value course
    
    print(f"Worst course is {mincourse}: {mingrade}% ")               # formatted print for lowest scoring course and associated grade
        
    print(f"dropped {mincourse}")                                     # tells the user the lowest value course is dropped
    term_grades.pop(mincourse)                                        # remove the lowest val course from the dict.
        
    course_recount= len(term_grades)                                  # count number of elements remaining in course
    new_termtotal= sum(list(term_grades.values()))                    # the new total of all grade values is the sum of those values
    print(f"Here are my revised grades...")                           # lets user know revised grades will output
    
    for course,grade in term_grades.items():
        print(f"Grade in {course} is {grade}%")                       # formatted output for courses and grades after removal of lowest course
    
    revisedavg= new_termtotal/course_recount                          # get new average grade from new total and new course count
    print(f"The revised average is {revisedavg:.2f}%")                # formatted output for new average grade

grades()