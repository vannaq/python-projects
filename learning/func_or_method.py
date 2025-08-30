#This is a mini project called "Function or Method" Quiz. 
import random

quiz_items = [
    ("upper()", "method"),
    ("len()", "function"),
    ("append()", "method"),
    ("sorted()", "function")
]


while True:
    score = 0                                                                               #Declaring variable score with a value of 0. Note that score needs to be defined outside of the for loop so it can increase or decrease with whichever condition met AND inside while loop so it resets every game.
    random.shuffle(quiz_items)                                                              #Shuffling quiz items before starting the for loop prevents repeated questions because the list is shuffled every time a new item is picked.
    
    for item, answer in quiz_items:
        user_input = input(f"Is {item} a function or method? ").strip().lower()             #The f is an f-string, or formatted string literal. It lets you insert variables or expressions directly inside strings using curly brackets {}. 
                                                                                            #.strip() is often used with .lower() when dealing with user input like in quizzes, forms, or chatbot responses. It "trims the edges" to remove extra whitespaces from the beginning and end of a string.
                                                                                            #.lower() converts all characters in a string to lowercase so "Function" is treated the same as "function"

        if user_input == answer:
            score = score + 1
            print(f"Correct! Your score is {score}.")
        else: 
            score = score - 1
            print(f"Nope! {item} is a {answer}. Your score is {score}.")

    print(f"Round complete! Your final score is {score}")
    
    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != "yes":
            print("Thanks for playing! Bye!")
            break
    
