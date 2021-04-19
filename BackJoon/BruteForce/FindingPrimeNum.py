from itertools import permutations


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

numbers = "0130"
candidate = []
for i in numbers:
    if isPrime(int(i)):
        candidate.append(int(i))

for i in range(2, len(numbers)+1):
    for perNum in permutations(numbers, i):
        num = 0
        for p in perNum:
            num += int(p)
            num *= 10
        num //= 10
        if isPrime(num):
            candidate.append(num)

print(set(candidate))