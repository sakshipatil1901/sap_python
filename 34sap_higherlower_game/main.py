import random
import data
import os

score = 0


def display_accountinfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, followers_1, followers_2):
    if followers_1 < followers_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False


account_B = random.choice(data.data)

continue_flag = True
while continue_flag:
    account_A = account_B
    account_B = random.choice(data.data)
    while account_A == account_B:
        account_B = random.choice(data.data)

    print(f"Compare 1: {display_accountinfo(account_A)}")
    print(f"Compare 2: {display_accountinfo(account_B)}")
    guess = int(input("Who has more followers? Type 1 or 2: "))
    followers_count_1 = account_A["follower_count"]
    followers_count_2 = account_B["follower_count"]
    is_correct = check_answer(guess, followers_count_1, followers_count_2)
    os.system('cls')
    if is_correct:
        score += 1
        print(f"You are right. Your score is: {score}")
    else:
        print(f"You are wrong. your final score is: {score} ")
        continue_flag = False
