# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 16:07:38 by slegaris          #+#    #+#              #
#    Updated: 2023/04/17 18:13:07 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def parser(input1, input2):
    if input1.isdigit():
        print("You must provide a valid string as first parameter")
        exit(0)
    try:
        num_non_punctuation = int(sys.argv[2])
    except ValueError:
        print("You must provide a valid int as second parameter")
        exit(0)
    else:
        return 0

def filter_words(s, n):
    return [word.strip(string.punctuation) for word in s.split() if len(''.join(c for c in word if c not in string.punctuation)) > n]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("You must provide only 2 arguments in their correct format <string> <int>")
        exit(0)
    else:
        parser(sys.argv[1], sys.argv[2])

        input_string = sys.argv[1]
        num_non_punctuation = int(sys.argv[2])

        result = filter_words(input_string, num_non_punctuation)
        print(result)
