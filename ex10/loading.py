# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 22:56:27 by slegaris          #+#    #+#              #
#    Updated: 2023/04/17 23:38:06 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tqdm import tqdm
import time
import sys

def ft_progress(lst):
    total = len(lst)
    start_time = time.time()

    initial_sample = 10
    for i in range(initial_sample):
        time.sleep(0.01)
    initial_eta = start_time * (total / initial_sample)

    with tqdm(total=total, unit="elem", ncols=80, mininterval=0.1, maxinterval=0.5, bar_format="ETA: {eta}s {l_bar}{bar}| {n_fmt}/{total_fmt} | elapsed time {elapsed_s:3.2f}s", dynamic_ncols=True, ascii=" >=") as pbar:
        pbar.set_postfix(eta=f"{initial_eta:.0f}", refresh=False)
        pbar.refresh()
        time.sleep(0.1)

        for item in lst:
            yield item
            elapsed = time.time() - start_time
            if pbar.n != 0:
                pbar.set_postfix(eta=f"{elapsed * (total - pbar.n) / pbar.n:.0f}", refresh=False)
            pbar.update(1)
            time.sleep(0.01)

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
