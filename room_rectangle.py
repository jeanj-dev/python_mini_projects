# This program compute the area and perimeter of a rectangle
def area_and_perimeter():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area: {area} Perimeter: {perimeter}")

area_and_perimeter() # Call to function