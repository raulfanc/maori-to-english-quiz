from translate import Translator
import random
from english_words import get_english_words_set


def create_translator(to_lang):
    """Creates a translator to the specified language"""
    return Translator(to_lang=to_lang)


def generate_maori_words(english_words, translator):
    """Translates English words to Maori and returns a dictionary of Maori:English word pairs"""
    maori_words = {}
    total_words = len(english_words)
    translated_words = []  # Store the translated words
    for i, word in enumerate(english_words, start=1):
        print(f"Initialising Maori Dictionary,Translating word {i} of {total_words}...")
        try:
            maori_translation = translator.translate(word)
            maori_words[maori_translation] = word
            translated_words.append(maori_translation)
        except Exception as e:
            print(f"Error translating word '{word}': {e}")
    return maori_words, translated_words  # Return the dictionary and the list


def answer_match_quiz(quiz_words, maori_words):
    """Conducts an answer match quiz and returns the score"""
    score = 0
    for question_number, maori_word in enumerate(quiz_words):
        user_answer = input(f"Q{question_number + 1}. Please translate '{maori_word}' into English: ").lower()
        correct_answer = maori_words[maori_word]

        if user_answer == correct_answer:
            print("Correct! Good job!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is '{correct_answer}'")
        print('*****************************************\n')
    return score


def multiple_choices_quiz(quiz_words, maori_words, english_words_set):
    """Multiple Choices Quiz Mode: Asks the user to select the correct translation from multiple choices"""
    score = 0
    for i, maori_word in enumerate(quiz_words, start=1):
        correct_answer = maori_words[maori_word]
        incorrect_answers = random.sample(english_words_set - {correct_answer}, 3)
        choices = [correct_answer] + incorrect_answers
        random.shuffle(choices)  # Randomize the order of choices

        print(f"Q{i}. What is the English translation for '{maori_word}'?")
        for j, choice in enumerate(choices, start=1):
            print(f"{chr(64 + j)}. {choice}")

        user_answer = input("Your answer is: ")
        if choices[ord(user_answer.upper()) - 65] == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is '{correct_answer}'.\n")

    return score



def main():
    """Main function that creates the translator, generates Maori words, and conducts the quiz"""
    translator_to_maori = create_translator("mi")
    english_words_set = get_english_words_set(['web2'], lower=True)
    random_english_words = random.sample(list(english_words_set), 10)
    maori_words, translated_words = generate_maori_words(random_english_words, translator_to_maori)

    quiz_words = random.sample(translated_words, 10)  # Randomly select Maori words for the quiz

    print("Please select a quiz mode:\n1. Answer Match Quiz\n2. Multiple Choices Quiz")
    quiz_mode = int(input("Your choice is: "))

    if quiz_mode == 1:
        score = answer_match_quiz(quiz_words, maori_words)
    elif quiz_mode == 2:
        score = multiple_choices_quiz(quiz_words, maori_words, english_words_set)

    else:
        print("Invalid selection. Please run the program again and select either 1 or 2.")
        return

    print(f'Good Job! Your final score is {score}')


if __name__ == "__main__":
    main()



