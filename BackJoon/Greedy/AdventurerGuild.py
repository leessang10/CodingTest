n = int(input())
li = list(map(int, input().split(" ")))

li.sort()
result = 0
cnt = 0
# li = {a b c d e f g}
for i in li:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)