# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 23:21:14 by slegaris          #+#    #+#              #
#    Updated: 2023/04/18 11:19:24 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 3:
    print("Error: Please provide exactly two integer arguments.")
    exit(0)
if len(sys.argv) == 2:
    print("Error: Please provide exactly two integer arguments.")
    exit(0)
elif len (sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("     python operations.py 10 3")
    exit(0)
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        sum_result = a + b
        difference_result = a - b
        product_result = a * b
        try:
            quotient_result = a / b
            remainder_result = a % b

            quotient_str = format(quotient_result, '.4g')
            if '.' in quotient_str:
                quotient_str = quotient_str.rstrip('0')
                if len(quotient_str.split('.')[1]) > 4:
                    quotient_str = format(quotient_result, '.4g') + '...'
            # quotient_str = quotient_str.rstrip('.')
        except ZeroDivisionError:
            quotient_result = "ERROR (division by zero)"
            remainder_result = "ERROR (modulo by zero)"

        print(f"Sum:            {sum_result:<}")
        print(f"Difference:     {difference_result:<}")
        print(f"Product:        {product_result:<}")
        print(f"Quotient:       {quotient_result:<}")
        print(f"Remainder:      {remainder_result:<}")

    except ValueError:
        print("Error: Both arguments must be integers.")
