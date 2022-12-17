import random
import sys
import time

wins = 0
loses = 0
ties = 0
times_played = 1


def stats():
    print("\nwins: %s" % wins)
    print("loses: %s" % loses)
    print("ties: %s\n" % ties)
    time.sleep(1)


def draw():
    # print the rock
    print(" 🗿 ")

    # print the paper
    print(" 📜 ")

    # print the scissor
    print(" ✂️ \n")


def game_over():
     if times_played == 6:
         print("\nGAME OVER!!\n")
         if wins > loses:
             print("You won!!\n")
             stats()
             time.sleep(3)
             sys.exit()
         elif wins < loses:
             print("You Lost!\n")
             stats()
             time.sleep(3)
             sys.exit()
         else:
             print("That was a Draw!!\n")
             stats()
             time.sleep(3)
             sys.exit()


while True:
    game_over()
    time.sleep(1)
    if times_played == 1:
        print("\nLets play ROCK, PAPER, SCISSORS\n")
        draw()
        time.sleep(2)
        print("The one with the highest score wins!!\n")
        print("5 rounds in total!\n")
    else:
        print("\nRound %s" % times_played)
        print("Good Luck!")
        time.sleep(1)
    time.sleep(1)
    time.sleep(0.7)
    stats()
    time.sleep(2)
    computer_num = random.randint(1, 3)
    if computer_num == 1:
        computer_choise = "r"
    elif computer_num == 2:
        computer_choise = "p"
    else:
        computer_choise = "s"
    choise = input("Enter your move: (r)ock , (p)aper , (s)cissors, (e)xit\n-> ")
    while True:
        if choise in ["r", "p", "s"]:
            for i in range(1, 4):
                print(i)
                time.sleep(1)
        if computer_choise == choise:
            ties += 1
            print("Thats a tie! Both chose %s" % computer_choise)
            time.sleep(4)
            times_played += 1
            break
        elif computer_choise == "r" and choise == "p":
            print("Congratulations you won!! you chose paper and he chose rock")
            wins += 1
            time.sleep(4)
            times_played += 1
            break
        elif computer_choise == "r" and choise == "s":
            print("You lost!!, you chose scissors and he chose rock")
            loses += 1
            time.sleep(4)
            times_played += 1
            break
        elif computer_choise == "p" and choise == "r":
            print("You lost!!, you chose rock and he chose paper")
            loses += 1
            time.sleep(4)
            times_played += 1
            break
        elif computer_choise == "p" and choise == "s":
            print("Congratulations you won!! you chose scissors and he chose paper")
            wins += 1
            time.sleep(4)
            times_played += 1
            break
        elif computer_choise == "s" and choise == "p":
            print("You lost!! You chose paper and he chose scissors")
            loses += 1
            time.sleep(4)
            times_played += 1
            break
        elif computer_choise == "s" and choise == "r":
            print("You won!! You chose rock and he chose scissors")
            wins += 1
            time.sleep(4)
            times_played += 1
            break
        elif choise == "e":
            print("Ok, see you next time!")
            time.sleep(2)
            sys.exit()
        else:
            print("Wrong input! Try again")
            time.sleep(2)
            break

