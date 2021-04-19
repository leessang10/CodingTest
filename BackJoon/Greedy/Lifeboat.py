people = [70, 50, 80, 50]
limit = 100
people.sort()
boat = 0
#정렬된 people의 가장 작은 값과 가장 큰 값을 비교하기 위해 i, j 초기화
i, j = 0, len(people) - 1
while i <= j:
    boat += 1
    if people[i] + people[j] <= limit:
        i += 1
    j -= 1

print(boat)