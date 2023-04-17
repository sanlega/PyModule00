# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 22:02:43 by slegaris          #+#    #+#              #
#    Updated: 2023/04/17 22:34:20 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import *
import sys

ran_num = randint(1, 99)

print("This is an interactive guessing game!\n"
        "You have to enter a number between 1 and 99 to find out the secret number.\n"
        "Type 'exit' to end the game.\n"
        "Good luck!")
count = 0
win = False
while not win:
    guess_str = input("What's your guess between 1 and 99?\n>> ")
    if guess_str.isdigit():
        guess = int(guess_str)
        count += 1
        if guess != ran_num and guess < ran_num:
            print("Too low!")
        elif guess != ran_num and guess > ran_num:
            print("Too high!")
        else:
            win = True
            if count == 1:
                if guess == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                print("Congratulations! You got it on your first try!")
            elif guess == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
    elif guess_str.lower() == "exit":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("That's not a number.")

if win and count > 1:
    print(f"Congratulations, you've got it!\nYou won in {count} attempts!")
    sys.exit(0)
