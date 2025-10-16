#!/usr/bin/env python3
import random
import json
import os
from glob import glob
from persistence import *

def main():
    print("\nWelcome to MicroQuizMaster")
    while True:
        print("\n1. Play a Quiz")
        print("2. Make a Quiz")
        print("3. Quit")
        choice = input("Enter choice number: ")

        if choice == "3":
            break
        elif choice == "2":
            os.system("python3 quizcreator.py")
        elif choice == "1":
            filename = input("Enter quiz filepath: ")
            try:
                questions, title = load_quiz(filename)
            except:
                print("Invalid filepath")    
                continue
            question_index = 0
            score = 0

            while question_index < len(questions):
                current_question = questions[question_index]
                correct_answer = current_question.correctAnswer
                wrong_answers = current_question.wrongAnswers
                answers = random.sample([correct_answer] + wrong_answers, len(wrong_answers) + 1)

                print(f"\nQuestion: {current_question.question}")
                for i, answer in enumerate(answers):
                    print(f"{i+1}. {answer}")
                user_answer = input("Select the correct answer: ")

                if user_answer.isdigit() and 1 <= int(user_answer) <= len(answers):
                    if answers[int(user_answer) - 1] == correct_answer:
                        score += 1
                    question_index += 1
                else:
                    print("Invalid choice.")

                if question_index >= len(questions):
                    print(f"Quiz completed! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    main()
