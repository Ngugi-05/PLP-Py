import random


class flashcard:
    def __init__(self):

        self.fruits = {'apple': 'red',
                       'orange': 'orange',
                       'watermelon': 'green',
                       'banana': 'yellow'}

    def quiz(self):
        while (True):

            fruit, color = random.choice(list(self.fruits.items()))

            print("What is the color of {}".format(fruit))
            user_answer = input()

            if (user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")

            option = int(input("enter 0 , if you want to play again : "))
            if (option):
                break


class Advancedflashcard(flashcard):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.total = 0

    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))

            print("What is the color of {}".format(fruit))
            user_answer = input()
            self.total += 1
            if (user_answer.lower() == color):
                print("Correct answer")
                self.score += 1
            else:
                print(f"Wrong answer. The correct color is {color}")
            option = input(
                "enter 0 if you want to quit or press Enter to continue : ")
            if (option):
                break
        print(f"Your final score is {self.score} out of {self.total}")


print("welcome to fruit quiz ")
fc = Advancedflashcard()
fc.quiz()
