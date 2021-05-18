from tqdm import tqdm
from time import sleep

A = [1]*11
N = len(A)
bar = tqdm(total = N)
for a in A:
    bar.update(1)