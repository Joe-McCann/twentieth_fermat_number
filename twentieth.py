import math
import tqdm

n = 20
p = math.floor((2**n - math.log(n+2, 2))/(n+2))
residue = 2 ** (2**n - p * (n+2))
n2 = 2 ** (n + 2)
binary = "1011101000101110"[::-1]

#for a in tqdm.tqdm(range(3, 10**9)):
a = 10**21
total = 1
next_square = a
mod_value = a * n2 + 1

for i in range(1, len(binary)):
    next_square = pow(next_square, 2, mod_value)
    if binary[i] == "1":
        total = (total * next_square) % mod_value

if total == (mod_value - residue):
    print(a)
    print("FOUND IT OMFGGGG")
    input()
print(total)
