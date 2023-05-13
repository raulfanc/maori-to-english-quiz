import random

Maori = [
    'tahi', 'rua', 'toru', 'wha', 'rima',
    'ono', 'whitu', 'waru', 'iwa', 'tekau',
    'kia ora', 'haere ra', 'morena', 'ka kite ano', 'haere mai',
    'ka pai', 'kei te pai', 'kino', 'whanau', 'iwi',
    'tai', 'hui', 'karakia', 'waiata', 'pakipaki',
    'kai', 'katao', 'waka', 'marae', 'ma',
    'pango', 'whero', 'paraone', 'karaka', 'kowhai',
    'kakariki', 'kahurangi', 'poroporo', 'rahina', 'ratu',
    'raapa', 'rapare', 'ramere', 'rahoroi', 'ratapu',
    'aotearoa', 'motu', 'hotaka', 'wahine', 'tane'
]

EnglishTranslation = [
    'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', 'nine', 'ten',
    'hello', 'good bye', 'good morning', 'see you later', 'welcome',
    'good', 'well done', 'bad', 'family', 'tribe',
    'friend', 'meeting', 'prayer', 'song', 'clap',
    'food', 'water', 'canoe', 'meeting house', 'white',
    'black', 'red', 'brown', 'orange', 'yellow',
    'green', 'blue', 'purple', 'monday', 'tuesday',
    'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
    'zealand', 'island', 'program', 'woman', 'man'
]



def generate_quiz_words(num_questions, maori_list):
    """Generates a list of random Maori words for the quiz"""
    quiz_words = random.sample(maori_list, num_questions)
    return quiz_words


def answer_match_quiz(quiz_words, maori_list, english_list):
    """Conducts an answer match quiz and returns the score"""
    score = 0
    for question_number, maori_word in enumerate(quiz_words):
        """handle the Quiz to take Enter as a valid answer"""
        while True:
            user_answer = input(f"Q{question_number + 1}. Please translate '{maori_word}' into English: ").lower()
            if user_answer == "":
                print("Invalid input. Please enter your answer.")
            else:
                break

        correct_answer = english_list[maori_list.index(maori_word)]

        if user_answer == correct_answer:
            print("Correct! Good job!")
            print('^^^^^^^^^^^^^^^^^^^^^^^^^\n')
            score += 1
        else:
            print(f"Incorrect! The correct answer is '{correct_answer}'")
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
    return score



def multiple_choices_quiz(quiz_words, maori_list, english_list):
    """Conducts a multiple choices quiz and returns the score"""
    score = 0
    for question_number, maori_word in enumerate(quiz_words):
        choices = random.sample(english_list, 3)
        correct_answer = english_list[maori_list.index(maori_word)]
        choices.append(correct_answer)
        random.shuffle(choices)

        print(f"Q{question_number + 1}. What is the English translation for '{maori_word}'?")
        for choice_number, choice in enumerate(choices):
            print(f"{chr(65 + choice_number)}. {choice}")

        valid_choices = ['a', 'b', 'c', 'd']

        while True:
            user_choice = input("Your choice is: ").lower()

            if user_choice in valid_choices:
                selected_choice = choices[ord(user_choice) - ord('a')]
                if selected_choice == correct_answer:
                    print("Correct! Good job!")
                    score += 1
                else:
                    print(f"Incorrect! The correct answer is '{correct_answer}'")
                break
            else:
                print("Invalid choice. Please select a valid option (A, B, C, or D).")
                continue

        print('*****************************************\n' '*****************************************\n')

    return score


def main():
    """Main function that generates quiz words and conducts the quiz based on user selection"""
    num_questions = 10  # Number of quiz questions

    print("Please select a quiz mode:")
    print("1. Answer Match Quiz")
    print("2. Multiple Choices Quiz")
    quiz_mode = int(input("Your choice is: "))

    # Generate quiz words
    quiz_words = generate_quiz_words(num_questions, Maori)

    if quiz_mode == 1:
        score = answer_match_quiz(quiz_words, Maori, EnglishTranslation)
    elif quiz_mode == 2:
        score = multiple_choices_quiz(quiz_words, Maori, EnglishTranslation)
    else:
        print("Invalid selection. Please run the program again and select either 1 or 2.")
        return

    print(f"Good Job! Your final score is {score}/{num_questions}")


if __name__ == "__main__":
    main()
