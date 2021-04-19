num = {'c': 26, 'd': 10}
carNum = list(input())
result = num[carNum[0]]

for i in range(1, len(carNum)):
    multiNum = num[carNum[i]]
    if carNum[i] == carNum[i-1]:
        multiNum -= 1
    result *= multiNum

print(result)
