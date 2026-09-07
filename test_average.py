# This program calculates the average test score
def average_test_score(first_score, second_score, third_score):
    """Calculate the average of the three test scores."""

    average_score = (first_score + second_score + third_score) / 3
    return average_score

def get_test_score(prompt):
    """Get a valid score from the user."""

    while True:
        try:
            score = float(input(prompt))
            if score < 0 or score > 100:
                print("Enter a score from 0 to 100!")
                continue

            return score

        except ValueError:
            print("Wrong input! Numbers only!")

def test_score_inputs():
    """Get valid test score inputs from the user."""

    first_score = get_test_score("Enter the first test score: ")
    second_score = get_test_score("Enter the second test score: ")
    third_score = get_test_score("Enter the third test score: ")

    return first_score, second_score, third_score

def run_test_score():
    """Run the test average calculator."""
    first_test, second_test, third_test = test_score_inputs()
    average_score = average_test_score(first_test, second_test, third_test)

    print(f"Average test score: {average_score:.1f}") 

run_test_score()

