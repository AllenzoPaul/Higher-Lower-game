from art import logo, vs
from game_data import data
import random

def format_data(account):
    """take the account data and returns printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == a
    else:
        return guess == b 


#display the logo 
print(logo)
score = 0

#generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A : {format_data(account_a)}.")
print(vs)
print(f"Against B : {format_data(account_b)}.")

#ask user for a guess
guess = input("Who has more followers? A or B").lower()

#get the followers of each account 
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]
is_correct = check_answer(guess, a_follower_count, b_follower_count)

#give user their feedback
  
if is_correct:
    score += 1
    print(f"You're right! Your current score: {score}")   
else:
    print(f"You're wrong! Your total score is: {score}")