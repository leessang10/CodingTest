
N = int(input())
move = input().split()

#(Y, X)
y = 1
x = 1



for m in move:
    if m == 'R':
        if x < N:
            x += 1
    elif m == 'L':
        if x > 1:
            x -= 1
    elif m == 'U':
        if y > 1:
            y -= 1
    elif m == 'D':
        if y < N:
            y += 1

print(y, x)


