#program3_1 COP1000
#by Michael Napoli 2275778

def main():
    
    #defined constants for calculations
    overtime_multiplyer= 1.5
    regular_hours= 40
    regular_pay= float()

    
    #defining variables for user input (hourly rate and hours worked)
    hourlyRate= float(input('What is the hourly rate? '))
    hoursWorked= float(input('How many hours were worked? '))

    #payout calculations for regular pay
    if hoursWorked <= regular_hours:
        normalHours= hoursWorked
        overtimeHours= 0
    #calculations for overtime pay
    else:
        normalHours= regular_hours
        overtimeHours= hoursWorked - regular_hours
    overtimePay= overtimeHours * hourlyRate * overtime_multiplyer
    regular_pay= regular_hours * hourlyRate
    
    #calculation for total pay
    grossPay= overtimePay + regular_pay   
    
    #the output text with the results from the calculations
    print(f'Regular Pay= ${regular_pay:,.2f}')
    print(f'Overtime Pay= ${overtimePay:,.2f}')
    print(f'Gross Pay= ${grossPay:,.2f}')

main()