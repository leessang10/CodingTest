str1 = input()
str2 = []
value = 0
for s in str1:
    if 'A' <= s <= 'Z':
        str2.append(s)

    if '0' <= s <= '9':
        value += int(s)


str2.sort()
if value != 0:
    str2.append(str(value))

print(''.join(str2))