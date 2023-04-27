# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 23:19:59 by slegaris          #+#    #+#              #
#    Updated: 2023/04/19 02:12:31 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (19,42,21)
# kata = ()

if len(kata) == 0:
    exit(0)
numbers_string = ''
for i, number in enumerate(kata):
    if i > 0:
        numbers_string += ', '
    numbers_string += str(number)

print(f'The {len(kata)} numbers are {numbers_string}')
