import random as rn

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

options = [rock, paper, scissors]
your_score = 0
computer_score = 0


for i in range(1,4):
      user_choose = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors. \n"))
      print(options[user_choose])

      computer_choose = rn.randint(0,2)
      print("Computer choose: ")
      print(options[computer_choose])
      if user_choose >= 2 and user_choose<0:
         print("You typed an invalid number, you lose.")
      elif user_choose == 0 and computer_choose == 2:
         print("You win!")
         your_score += 1
      elif user_choose == 2 and computer_choose == 0:
         print("You lose.")
         computer_score += 1
      elif user_choose > computer_choose:
         print("You win!")
         your_score += 1
      elif computer_choose > user_choose:
         print("You lose.")
         computer_score += 1
      elif computer_choose == user_choose:
         print("İt's a draw.")
         continue

if your_score>computer_score:
    print(f"Your score: {your_score} ,Computer score: {computer_score}.You win!")
elif computer_score> your_score:
    print(f"Your score: {your_score} ,Computer score: {computer_score}.You Lose!")
else:
    print(f"Your score: {your_score} ,Computer score: {computer_score}.There is no winner!")



