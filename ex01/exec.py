# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 23:20:17 by slegaris          #+#    #+#              #
#    Updated: 2023/04/13 23:20:22 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = len(sys.argv)

while i > 1:
    input_str = sys.argv[i - 1][::-1]
    swapcase = input_str.swapcase()
    print(swapcase, end=' ')
    i -= 1
