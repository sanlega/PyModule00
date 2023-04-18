# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 23:20:17 by slegaris          #+#    #+#              #
#    Updated: 2023/04/18 01:56:09 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) < 2:
    print("You must provide at least one argument.")
    exit(0)

i = len(sys.argv)

while i > 1:
    input_str = sys.argv[i - 1][::-1]
    swapcase = input_str.swapcase()
    print(swapcase)
    i -= 1
