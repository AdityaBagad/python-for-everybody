# Rewrite your pay program using try and except so that your program handles non-numeric input 
# gracefully by printing a message and exiting the program. 
# The following shows two executions of the program:
try:
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Enter Numeric data')
    quit()
    
if hours > 40:
    extra_time = int(hours - 40) * 1.5 * 10
    gross_pay = (hours * rate) + extra_time
else :
    gross_pay = hours * rate

print(gross_pay)