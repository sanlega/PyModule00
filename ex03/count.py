# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 23:20:57 by slegaris          #+#    #+#              #
#    Updated: 2023/04/13 23:20:59 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

def text_analyzer(s=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if s is None:
        s = input("What is the string to analyze?\n>> ")

    if not isinstance(s, str):
        print("Error: argument is not a string.")
        return

    upper_count = sum(c.isupper() for c in s)
    lower_count = sum(c.islower() for c in s)
    punctuation_count = sum(c in string.punctuation for c in s)
    space_count = sum(c.isspace() for c in s)

    print(f"The text contains {len(s)} character(s):")
    print(f"- {upper_count} upper letter(s)")
    print(f"- {lower_count} lower letter(s)")
    print(f"- {punctuation_count} punctuation mark(s)")
    print(f"- {space_count} space(s)")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error: more than one argument is provided.")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
