# flashcard app, that has medical terminolgy, on screen flashcard with term, suffix, prefix, (eventually) body part. Also, one button, for help "clue" (goes to 4 multiple choice), and Input field for answer. 
# Point systems input 2, pick mc 1, and card flip none.
# timer for fast mode, number of questions, 25 minutes max. 

import random
import json

user_score = 0
questions_answered = 0
questions_answered_correctly = 0

with open("medical_dictionaries.json", "r") as f:
    medical_word_parts_merged_by_letter = json.load(f)

def retrieve_random_key_values(data):
    random_category = random.choice(list(data.keys())) #fetches random dictionary letter
    inner_dict = data[random_category] #pulls dictionary for that letter
    random_key = random.choice(list(inner_dict.keys())) #choose random key of that dictionary
    random_value = inner_dict[random_key] #pulls values from that key
    return random_key, random_value

def format_answer_list(answer_list):
    if len(answer_list) == 1:
        return answer_list[0]
    elif len(answer_list) == 2:
        return answer_list[0] + " or " + answer_list[1]
    else:
        return ", ".join(answer_list[:-1]) + ", or " + answer_list[-1]

def evaluate_user_input(user_input, correct_answers, is_retry=False):
    if user_input in correct_answers:
        score = 1 if is_retry else 2
        message = "Spare! 1 point." if is_retry else "Correct, 2 points; good job!"
        return score, message
    else:
        return 0, f"{format_answer_list(correct_answers).title()} was the correct answer. 0 points."

def handle_question(prompt, correct_answers):
    user_input = input(prompt + "\nAnswer: ")
    if user_input.lower() == "skip":
        return 0, "Skipping, no points gained or lost", False
    score, message = evaluate_user_input(user_input, correct_answers)
    if score > 0:
        return score, message, True
    retry_input = input(f"{user_input.title()} is incorrect, please try again: ")
    score, message = evaluate_user_input(retry_input, correct_answers, is_retry=True)
    return score, message, score > 0

playing_game = True

while playing_game:
    term, answer = retrieve_random_key_values(medical_word_parts_merged_by_letter)
    prompt = f"What does {term} mean? (Type 'skip' to get a new question.)"
    score, message, correct = handle_question(prompt, answer)
    print(message)
    user_score += score
    questions_answered += 1
    if score > 0:
      questions_answered_correctly += 1
    play_again = input("Would you like to go again? (Y/N): ").lower()
    if play_again in ("n", "no"):
        playing_game = False
        print("Goodbye!")