# Rewrite your pay computation with time-and-a-half for over time and 
# create a function called computepay which takes two parameters
# (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        extra_time = int(hours - 40) * 1.5 * 10
        gross_pay = (hours * rate) + extra_time
    else :
        gross_pay = hours * rate

    return (gross_pay)    

hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

gross_pay = computepay(hours, rate)
print(gross_pay)