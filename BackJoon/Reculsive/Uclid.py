def uclidGCD(a, b):
    if a % b == 0:
        return b
    else:
        return uclidGCD(b, a % b)


a, b = map(int, input().split(" "))
uclidGCD(a, b)