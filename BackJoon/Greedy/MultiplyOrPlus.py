n = input()

result = int(n[0])

for i in range(1, len(n)):
    i = int(i)
    if i <= 1 or result <=1:
        result += i
    else:
        result *= i

print(result)