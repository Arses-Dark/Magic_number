import random


class MagicNumberGame:
    def __init__(self):
        self.min_num = 0
        self.max_num = 10
        self.life = 3
        self.level = 1

    def generate_answer(self):
        return random.randint(self.min_num, self.max_num)

    def play_game(self, answer):
        while self.life > 0:
            print(f'\nLife in game: {self.life}')
            print(f'Level : {self.level}')

            guess = self.get_guess()

            if guess == answer:
                print('Congratulations! Your answer is correct.')
                self.life += 3
                self.level += 1

                self.max_num += 5
                answer = self.generate_answer()

            else:
                self.life -= 1
                print('Oops! Your answer is incorrect.')

                if guess < answer:
                    print('Your answer is too low.')
                else:
                    print('Your answer is too high.')

                response = input('Do you want to continue? (y/n): ').lower()

                if response == 'n':
                    print('Thanks for playing!')
                    exit()

        print(
            f'\nYou have failed to guess the magic number.\nThe answer was {answer}')

    def get_guess(self):
        while True:
            try:
                return int(input(f'Guess the magic number between {self.min_num} and {self.max_num}: '))
            except ValueError:
                print('Invalid input. Please enter a valid integer.')

    def run(self):
        print('Magic Number Game!!!')
        print('Are you ready to test your guessing skills?')

        while True:
            user_input = input(
                'Enter "start" to begin or "exit" to quit: ').lower()

            if user_input == 'start':
                answer = self.generate_answer()
                self.life = 3
                self.level = 1

                self.play_game(answer)

            elif user_input == 'exit':
                print('Goodbye!')
                break


if __name__ == '__main__':
    game = MagicNumberGame()
    game.run()
