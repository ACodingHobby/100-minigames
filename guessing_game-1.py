class Number:
    
    def __init__(self, num):
        self.num = num
        self.lives = 3

    def guess_number(self):
        while self.lives != 0:
            try:
                guess = int(input("Enter your guess: "))
                
                if guess == self.num:
                    print("Good job, you won!")
                    break
              
                if guess != self.num:
                    self.lives -= 1
                    if self.lives != 0:
                        print(f"Oops, that's wrong. You have {self.lives} lives left.")
                    elif self.lives == 0:
                        print("You lost")
                        break

            except ValueError:
                print("Enter a valid number.")

print("\nWelcome to the guessing game.\nYou have 3 lives to try to guess the secret number.\n")
guess_game = Number(5)
guess_game.guess_number()
