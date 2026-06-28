# This program asks for user input and converts Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    """Convert a celsius temperature to fahrenheit."""
    return celsius * 9 / 5 + 32


def celsius_value():
    """Get user input, call the conversion function, and display the value."""
    while True:
        try:
            celsius = float(input("Enter the celsius temperature: "))
            break
        except ValueError:
            print("Wrong input! Numbers only!")

    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is {fahrenheit:.1f} degrees Fahrenheit")


celsius_value()
