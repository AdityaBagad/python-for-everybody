# Rewrite your pay computation to give the employee 1.5 times 
# the hourly rate for hours worked above 40 hours.

hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    extra_time = int(hours - 40) * 1.5 * rate
    gross_pay = (40 * rate) + extra_time
else :
    gross_pay = hours * rate

print(gross_pay)
