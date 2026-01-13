
# This program converts minutes to hours and remaining minutes
def min_to_hr():
    minutes = int(input("Enter the number of minutes: "))
    hours = minutes // 60 # // integer divsion to whole numbers
    remaining_minutes = minutes % 60 # % get remainder
    
    print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")

min_to_hr()
