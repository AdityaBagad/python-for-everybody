# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.
largest = None
smallest = None
total = 0
count = 0

while True:
    try:
        numbers = input('Enter a number: ')
        if numbers == 'done': 
            print('Maximum: ',largest)
            print('Minimum: ',smallest)
            print('Total: ',total)
            print('Count: ',count)
            break
        num = float(numbers)
        if smallest is None or smallest >= num:
            smallest = num
        elif largest is None or largest <= num:
            largest = num   
        total += num
        count += 1
    except:
        print('Bad Input')        