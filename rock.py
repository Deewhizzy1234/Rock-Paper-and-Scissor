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
choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors."))
import random
our_list = [rock, paper, scissors]
computer_choice = random.choice(our_list)
if choice == 0 and computer_choice == scissors:
    print(rock)
    print("You chose rock, \nComputer chose:")
    print(computer_choice)
    print("computer chose scissors You won.")
elif choice == 0 and computer_choice == paper:
    print(rock)
    print("You chose rock, \nComputer chose:")
    print(computer_choice)
    print("Computer chose paper. You lost.")
elif choice == 1 and computer_choice == rock:
    print(paper)
    print("You chose paper, \nComputer chose:")
    print(computer_choice)
    print("Computer chose rock. You won.")
elif choice == 1 and computer_choice == scissors:
    print(paper)
    print("You chose paper, \nComputer chose:")
    print(computer_choice)
    print("Computer chose scissors. You lost.")
elif choice == 2 and computer_choice == rock:
    print(scissors)
    print("You chose scissors, \nComputer chose:")
    print(computer_choice)
    print("Computer chose rock. You lost")
elif choice == 2 and computer_choice == paper:
    print(scissors)
    print("You chose scissors, \nComputer chose:")
    print(computer_choice)
    print("Computer chose paper. You won")
else:
    print("You chose the same with the computer it's a tie")



#if choice == 1:
    #print(paper)
    #print("You chose paper, \nComputer chose:")
    #print(computer_choice)







