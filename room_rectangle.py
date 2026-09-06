# This program computes the area and perimeter of a rectangle
def area_and_perimeter(length, width):
    """Calculate the area and perimeter of a rectangle."""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                print("Positive number only!")
                continue

            return number

        except ValueError:
            print("Wrong input! Numbers only!")

def get_rectangle_inputs():
    """Get valid rectangle inputs."""
    length = get_number("Enter the length: ")
    width = get_number("Enter the width: ")
    return length, width

def run_rectangle():
    """Run the area and perimeter of the rectangle."""
    length, width = get_rectangle_inputs()
    area, perimeter = area_and_perimeter(length, width)
    print(f"Area: {area} Perimeter: {perimeter}")

run_rectangle()