from itertools import combinations

dwarfs = [20, 7, 23, 19, 10, 15, 25, 8, 13]
dwarfs.sort()
# for i in range(9):
#     dwarfs.append(int(input()))
# print(dwarfs)
for c in combinations(dwarfs, 7):
    if sum(c) == 100:
        for i in c:
            print(i)
        break
