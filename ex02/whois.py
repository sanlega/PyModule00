# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 23:20:30 by slegaris          #+#    #+#              #
#    Updated: 2023/04/13 23:20:32 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

num = None

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
    except (ValueError, IndexError):
        print("AssertionError: argument is not an integer")

    if len(sys.argv) == 2:
        if num is not None and len(sys.argv) == 2:
            if num == 0:
                print("I'm Zero.")
            elif (num % 2) == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
    elif len(sys.argv) > 2:
        print ("AssertionError: more than one argument are provided")
else:
    print("AssertionError: Please provide an argument")
