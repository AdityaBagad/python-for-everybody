# Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature.

Celsius = float(input('Enter Celsius temperature: '))
Fahrenheit = ((Celsius * 9) / 5) + 32
print('Fahrenheit:',Fahrenheit)