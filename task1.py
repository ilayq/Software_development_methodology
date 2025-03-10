import math
import random


def lcm(a, b):
    """Функция для нахождения наименьшего общего кратного двух чисел."""
    return abs(a * b) // math.gcd(a, b)


def lcm_of_three(a, b, c):
    """Функция для нахождения НОК трех чисел."""
    return lcm(lcm(a, b), c)


def play_nok_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    for _ in range(3):
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = lcm_of_three(*numbers)

        print(f"Question: {numbers[0]} {numbers[1]} {numbers[2]}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_nok_game()
