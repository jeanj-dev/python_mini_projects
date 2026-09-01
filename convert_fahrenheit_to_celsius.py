# This program asks for user input and converts Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def get_fahrenheit():
    """Get a valid Fahrenheit temperature from the user."""
    while True:
        try:
            fahrenheit_value = float(input("Enter the Fahrenheit temperature: "))
            return fahrenheit_value
        except ValueError:
            print("Wrong input! Numbers only!")

def run_converter():
    """Run the Fahrenheit to Celsius converter."""
    fahrenheit = get_fahrenheit()
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is {celsius:.1f} degrees Celsius.") 
    

run_converter() 
