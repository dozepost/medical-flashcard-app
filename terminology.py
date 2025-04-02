# flashcard app, that has medical terminolgy, on screen flashcard with term, suffix, prefix, (eventually) body part. Also, one button, for help "clue" (goes to 4 multiple choice), and Input field for answer. 
# Point systems input 2, pick mc 1, and card flip none.
# timer for fast mode, number of questions, 25 minutes max. 

import random
import json

with open("medical_dictionaries.json", "r") as f:
    medical_word_parts_merged_by_letter = json.load(f)

def retrieve_random_word_parts(data):
    random_letter = random.choice(list(medical_word_parts_merged_by_letter.keys())) #fetches random dictionary letter
    random_wordpart_dict = medical_word_parts_merged_by_letter[random_letter] #pulls dictionary for that letter
    random_wordpart_key = random.choice(list(random_wordpart_dict.keys())) #choose random key of that dictionary
    random_wordpart_value = random_wordpart_dict[random_wordpart_key] #pulls values from that key
    return random_wordpart_key, random_wordpart_value

user_score = 0
questions_answered = 0
questions_answered_correctly = 0

def answer_length(answer_list):
    if len(answer_list) == 1:
        return answer_list[0]
    elif len(answer_list) == 2:
        return answer_list[0] + " or " + answer_list[1]
    else:
        return ", ".join(answer_list[:-1]) + ", or " + answer_list[-1]
    
playing_game = True

while playing_game:  
    random_wordpart_key, random_wordpart_value = retrieve_random_word_parts(medical_word_parts_merged_by_letter)
    print(f"What does {random_wordpart_key} mean? (Type 'Skip' to get a new question.)")
    user_input = input("Answer: ")

    if user_input.lower() == "skip":
            print("Skipping, no points gained or lost")
    else:
        if user_input in random_wordpart_value:
            print("Correct! 2 points!")
            user_score += 2
            questions_answered_correctly += 1
        else: 
            retry_input = input(f"{user_input.title()} is incorrect, please try again: ") 
            
            if retry_input in random_wordpart_value:
                print("Spare! 1 point")
                user_score += 1
                questions_answered_correctly += 1
            else: 
                    print(f"{answer_length(random_wordpart_value).title()} was the correct answer. 0 points.")
        
        questions_answered += 1
        print(f"You current score is {user_score}. You've answered {questions_answered_correctly}/{questions_answered} correctly.")
    again = input("Would you like another term? (y/n): ").lower()
    if again != "y":
        playing_game = False
        print(f"See you next time!")