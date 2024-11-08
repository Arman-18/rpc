import random

def get_player_choice():
    return input("Choose Rock, Paper, or Scissors: ").lower()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def main():
    print("Welcome to the Rock, Paper, Scissors Game!")
    explain_rules()
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
