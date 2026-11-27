import json 
import random
from pathlib import Path

QUESTIONS_FILE = Path(__file__).parent /"Questions.json"

def load_question(path):
    """Read the questions from a JSON file and return them as a list of dicts."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)
    
    #THe question
def ask_question(number, q):
    """Show one question with shuffled choices, return True if correct."""
    correct_text = q["choices"][q["answer"]]   # remember the right answer by its text
    choices = q["choices"][:]                  # make a copy of the list
    random.shuffle(choices)                    # shuffle the copy
    correct_index = choices.index(correct_text)  # where did it end up?

    print(f"\nQuestion {number}: {q['question']}")
    for i, choice in enumerate(choices, start=1):
        print(f"  {i}. {choice}")

    while True:
        raw = input("Your answer (number): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(choices):
            break
        print(f"Please enter a number from 1 to {len(choices)}.")

    if int(raw) - 1 == correct_index:
        print("Correct!")
        return True

    print(f"Wrong. The answer was: {choices[correct_index]}")
    return False
    
    

def run_quiz():
    questions = load_question(QUESTIONS_FILE)
    random.shuffle(questions)
    
    score = 0
    for number, q in enumerate(questions, start=1):
        if ask_question(number, q):
            score += 1
    
    print(f"\nYou scored {score}/{len(questions)} ({score / len(questions):.0%})")

if __name__== "__main__":
    run_quiz()