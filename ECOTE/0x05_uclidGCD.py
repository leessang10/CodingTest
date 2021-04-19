def gcd_recursive(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_recursive(b, a % b)


result = gcd_recursive(192, 162)
print(result)