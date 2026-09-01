# This program asks for user input and converts Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32

def get_celsius():
    """Get a valid Celsius temperature from the user."""
    while True:
        try:
            celsius_value = float(input("Enter the Celsius temperature: "))
            return celsius_value
        except ValueError:
            print("Wrong input! Numbers only!")
    
def run_converter():
    """Run the Celsius to Fahrenheit converter."""
    celsius = get_celsius()
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is {fahrenheit:.1f} degrees Fahrenheit")


run_converter()
