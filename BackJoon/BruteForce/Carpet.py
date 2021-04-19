brown = 24
yellow = 24

answer = []
box = brown + yellow

for x in range(1, box):
    y = box // x
    #print(x, y)
    if (x-2) * (y-2) == yellow:
        #print("#", x, y)
        answer = [x, y]

print(answer)