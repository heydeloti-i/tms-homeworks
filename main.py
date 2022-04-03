from exceptions import ValidationError
from validator import Data
from validator import Validator

__author__ = "Anishchenko"

import random

def advice_passport(age):
    """Рекомендации по действиям с паспортом"""
    if 16 <= age <= 17:
        return ' Не забудь получить первый паспорт по достижению 16 лет.'

    elif 25 <= age <= 26:
        return ' Не забудь заменить паспорт по достижению 25 лет.'

    elif 45 <= age <= 46:
        return ' Не забудь заменить паспорт по достижению 45 лет.'


def guess_number_game():
    generated_number = random.randint(1,5)
    guess_number = 0
    while True:
        users_guess = int(input("Input a random number from 1 to 5: "))
        if generated_number != users_guess:
            guess_number += 1
            continue
        break

    print(f"You've guessed the number. It was your {guess_number} try")



def main():
    try_number = 0
    while True:
        name, age = Data()
        validate = Validator
        print(f"It's your {try_number + 1} try.")
        while name is None:
            name = input('Введите ваше имя: ')
        try_number += 1
        try:
            name.validate()
        except Exception as exception:
            print (f'Ой, я словил ошибку: {exception}')
            try_number += 1
            name = None


        while age is None:
            age = input('Введите ваш возраст: ')
            try:
                age.validate()
            except Exception as exception:
                print(f'Ой, я словил ошибку: {exception}')
                continue
    break

#    advice = advice_passport(age)
 #   if advice is None:
  #      advice = ""

   # print(f'Привет, {name.title()}! Тебе {age} лет. {advice} Это {try_number} попытка.')
    guess_number_game()

main()

