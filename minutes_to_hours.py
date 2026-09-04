# This program converts minutes to hours and remaining minutes
def minutes_to_hours(minutes):
    """Calculate minutes to hours and remaining minutes."""
    hours = minutes // 60 
    remaining_minutes = minutes % 60 
    return hours, remaining_minutes

def get_minute_inputs():
    """Get a valid minute input from the user."""
    while True:
        try:
            minutes = int(input("Enter the number of minutes: "))
            
            if minutes < 0:
                print("Positive integer only!")
                continue
            return minutes

        except ValueError:
            print("Wrong input! Please enter a whole number!")

def run_calculator():
    """Run the minutes to hours converter."""
    minutes = get_minute_inputs()
    hours, remaining_minutes = minutes_to_hours(minutes)
   
    print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")

run_calculator()



