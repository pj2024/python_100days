rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
game = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You entered invalid number!")
else:
    print(game[user_choice])
    computer_choice = random.randint(0, 2)

    print("computer Choice:\n")
    print(game[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice < user_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's draw!")

    # play_game = int(input("Do you want to play again Type 1"))
    #
    # if play_game == 1:
    #     flag = true
    # else:
    #     flag = false
