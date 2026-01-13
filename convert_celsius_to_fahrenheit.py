# This program ask for user input and convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    celsius = float(input("Enter the celsius temperature: "))
    fahrenheit = celsius * 9 / 5 + 32 

    print(f"{celsius} degrees Fahrenheit is {fahrenheit:.1f} degrees Celsius") 

celsius_to_fahrenheit() # call to function