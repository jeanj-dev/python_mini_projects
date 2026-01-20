# This program asks for user input and converts Fahrenheit to Celsius
def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))
    celsius = (fahrenheit - 32) * 5 / 9

    print(f"{fahrenheit} degrees Fahrenheit is {celsius:.1f} degrees Celsius.") 

fahrenheit_to_celsius() 
