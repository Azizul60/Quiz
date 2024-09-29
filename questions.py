import json
import time
import random

def main():

    filename= 'questions.json'

    questions = load_file(filename)
    print("Welcome to the Quiz!\n")

    while True:
        start_quiz(questions)
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again != 'yes':
            break

def load_file(filename):
    with open(filename ,'r') as file :
        return json.load(file)

def start_quiz(questions):

    score=0
    random.shuffle(questions)

    for question in questions:
        print(f"\n {question["question"]}")
    
        for option in question["options"]:
            print(option)
        
        # Get user's answer with a time limit of 100 seconds
        start_time = time.time()
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if time.time()-start_time > 100:
            print(" Time's up")
        elif answer==question['answer']:
            print("Correct Answer")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}")
    
    print(f"\nQuiz finished! Your score: {score}/{len(questions)}")


if __name__=="__main__":
    main()
