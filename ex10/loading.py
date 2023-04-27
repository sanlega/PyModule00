# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 22:56:27 by slegaris          #+#    #+#              #
#    Updated: 2023/04/18 11:58:52 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tqdm import tqdm
import time

def ft_progress(listy):
    return tqdm(listy, 
                iterable="=>",
                ncols=80, 
                # mininterval=0.1, 
                # maxinterval=0.5, 
                bar_format='{l_bar}{bar}{r_bar}',
                ascii=' >=',
                smoothing=0.8,
                colour='green',
                unit_scale=True,)

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
