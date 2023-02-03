import random

class thegame:

    def __init__(self):
        self.LOWER = 1
        self.HIGHER = 100000

    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    def start(self):
        random_number = self.get_random_number()

        print(
            f"guess the number from {self.LOWER} to {self.HIGHER}")

        chances = 0
        while True:
            user_number = int(input("enter your guess: "))
            if user_number == random_number:
                print(
                    f"you guessed correctly in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif user_number < random_number:
                print("your guess is less than the number")
            else:
                print("your guess is higher than the number")
            chances += 1

numberGuessingGame = thegame()
numberGuessingGame.start()
