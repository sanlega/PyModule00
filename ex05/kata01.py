# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 23:14:28 by slegaris          #+#    #+#              #
#    Updated: 2023/04/17 15:08:15 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
# kata = None 

if kata:
    for language, creator in kata.items():
        print(f'{language} was created by {creator}')
else:
    exit(0)
