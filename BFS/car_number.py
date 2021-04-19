def car_number(s, n):
    if len(s) == 0:
        return n

    if s[0] == 'd':
        car_number(s[1:], n + 10)
    if s[0] == 'c':
        car_number(s[1:], n + 26)


s = input()
result = car_number(s, 0)
print(result)