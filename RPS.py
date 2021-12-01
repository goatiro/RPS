import time
import random
print("Made by Goatiro.")
print("Version 2.0")
loose = ("You loose.")
win = ("You win!")
lives = 5
score = 0
drew = 0
computer_lives = 7
password_list = []

while True:
    print("To begin fill in the below information.")
    username = input("Username : ")
    password = input("Password : ")
    searchfile = open("accounts.txt", "r")
    for line in searchfile:
        password_list.append(line.strip())

        if username and password in password_list:
            print("Access Granted")
            time.sleep(0.5)
            print("Loading.")
            time.sleep(0.5)
            print("Loading..")
            time.sleep(0.5)
            print("Loading...")
            time.sleep(0.5)
            start_menu = """
            ----------RPS----------
            -------Live Rules------
            """
            print(start_menu)
            while True:
                rps = input("Rock, paper, scissors?      ")
                computer = ("scissors", "rock", "paper")
                computer = random.choice(computer)
                # rock if statments
                if rps == "rock" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == "rock" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score += 1
                # paper if statments
                if rps == "paper" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == "paper" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score += 1
                # scissors if statments
                if rps == "scissors" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == "scissors" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score += 1
                # duplicates
                if rps == computer:
                    print("The computer choose", computer)
                    print("")
                    print("You drew.")
                    print("")
                    print("")
                    drew += 1
                # system
                if rps == "lives":
                    print(lives)
                if rps == "score":
                    print(score)
                if rps == "drew":
                    print(drew)
                # lives
                if lives == 0 or rps == "test":
                    print("Thanks for playing.")
                    print("You have run out of lives")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit.")
                    exit()
                if computer_lives == 0:
                    print("Thanks for playing.")
                    print("The computer lost all it's lives. You win.")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit.")
                    exit()
                # exit
                if rps == "exit":
                    break
    else:
        print("Your username of password is incorrect.")
        print("---------------------------------------")
