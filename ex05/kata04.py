# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/14 00:03:59 by slegaris          #+#    #+#              #
#    Updated: 2023/04/17 15:13:15 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (0, 4, 132.42222, 10000, 12345.67)
# kata = ()

if kata:
    module_number = f'module_{kata[0]:02d}'
    ex_number = f'ex_{kata[1]:02d}'

    formatted_numbers = '{:.2f}, {:.2e}, {:.2e}'.format(kata[2], kata[3], kata[4])

    output = f'{module_number}, {ex_number} : {formatted_numbers}'

    print(output)
else:
    exit(0)
