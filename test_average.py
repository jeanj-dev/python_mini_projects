# This program calculates the average test score
def average_test_score():
    first_score = float(input("Enter the first test score: "))
    second_score = float(input("Enter the second test score: "))
    third_score = float(input("Enter the third test score: "))

    average_score = (first_score + second_score + third_score) / 3
    print(f"Average test score: {average_score:.1f}") 

average_test_score() 
