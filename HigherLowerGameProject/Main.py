import random
from art import logo
from art import vs
from game_data import data
from replit import clear


def get_items():
    item = random.choice(data)
    return item

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"
  

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def play_game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_items()
    account_b = get_items()
    

    while game_should_continue:
        account_a = account_b
        account_b = get_items()

        print(f"Compare A : {format_data(account_a)}.")
        print(vs)
        print(f"Compare B : {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_account = account_a['follower_count']
        b_follower_account = account_b['follower_count']

        is_correct = check_answer(guess,a_follower_account,b_follower_account)

        clear()
        print(logo)

        if is_correct:
           score +=1
           print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
    
play_game()






