import random
import time

rpc = ["rock", "paper", "scissor"]
random_computer_guess = random.choice(rpc)

def guess():
        while True:
                script = ["rock...", "paper...", "scissor...", "shoot!"]
                for i in script:
                        time.sleep(1)
                        print(i, end=" ")
                print("\n")
                time.sleep(1)

                shoot = input("rock, paper, scissor: ")


        

                if shoot == random_computer_guess:
                        print("Tied, try again.")
                elif shoot.lower() == "rock" and random_computer_guess == "paper":
                        print("You lose!")
                        print(f"The computer chose {random_computer_guess}, which beats {shoot}!")
                        break
                elif shoot.lower() == "rock" and random_computer_guess == "scissor":
                        print("You win!")
                        print(f"You chose {shoot}, which beats the computer's {random_computer_guess}!")
                        break
                elif shoot.lower() == "paper" and random_computer_guess == "rock":
                        print("You win!")
                        print(f"You chose {shoot}, which beats the computer's {random_computer_guess}!")
                        break
                elif shoot.lower() == "paper" and random_computer_guess == "scissor":
                        print("You lose!")
                        print(f"The computer chose {random_computer_guess}, which beats {shoot}!")
                        break
                elif shoot.lower() == "scissor" and random_computer_guess == "rock":
                        print("You win!")
                        print(f"You chose {shoot}, which beats the computer's {random_computer_guess}!")
                        break
                elif shoot.lower() == "scissor" and random_computer_guess == "paper":
                        print("You lose!")
                        print(f"The computer chose {random_computer_guess}, which beats {shoot}!")
                        break


print("Welcome to rock paper scissors!")
guess()
