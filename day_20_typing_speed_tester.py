
import random
import time


sentences = [
    "Python is a popular programming language.",
    "Practice makes programming easier and faster.",
    "Learning new skills takes time and patience.",
    "Consistency is the key to success.",
    "Technology makes our daily life easier."
]


def calculate_accuracy(original, typed):
    correct = 0

    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1

    if len(original) == 0:
        return 0

    accuracy = (correct / len(original)) * 100
    return accuracy


def calculate_wpm(correct_characters, elapsed_time):
    minutes = elapsed_time / 60

    if minutes <= 0:
        return 0

    wpm = (correct_characters / 5) / minutes
    return wpm


def start_test():
    sentence = random.choice(sentences)

    print("\n===== TYPING SPEED TEST =====")
    print("\nType the following sentence:\n")
    print(sentence)

    input("\nPress Enter when you are ready to start...")

    print("\nStart typing!")
    start_time = time.time()

    typed_text = input("\nYour text: ")

    end_time = time.time()

    elapsed_time = end_time - start_time

    accuracy = calculate_accuracy(sentence, typed_text)

    correct_characters = sum(
        1 for a, b in zip(sentence, typed_text) if a == b
    )

    wpm = calculate_wpm(correct_characters, elapsed_time)

    errors = max(len(sentence), len(typed_text)) - correct_characters

    print("\n===== YOUR RESULTS =====")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Typing speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Incorrect characters: {errors}")

    if accuracy >= 95:
        print("Excellent accuracy!")
    elif accuracy >= 80:
        print("Good job! Keep practicing.")
    else:
        print("Keep practicing to improve your accuracy.")


def main():
    while True:
        print("\n===== TYPING SPEED TESTER =====")
        print("1. Start Test")
        print("2. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            start_test()

        elif choice == "2":
            print("Thanks for playing. Keep practicing!")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
