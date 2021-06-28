from itertools import permutations

v=["홍길동","성춘향","이몽룡","변사또"]
r=3

for result in permutations(v, r):
    print(result)