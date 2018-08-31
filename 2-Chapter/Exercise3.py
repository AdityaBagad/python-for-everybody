# Write a program to prompt the user for hours and rate perhour to compute gross pay.

hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
gross_pay = hours * rate
print('Pay:',gross_pay)