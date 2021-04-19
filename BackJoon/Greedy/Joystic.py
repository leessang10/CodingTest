name = list("JEROEN")

# A를 기준으로 하 버튼을 사용하는 경우: N O P Q R S T U V W X Y Z
# A는 버튼을 안 눌러도 되고, N은 상,하 버튼 둘다 된다
# A를 기준으로 상 버튼을 사용하는 경우: B C D E F G H I J K L M N
count = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]

answer = 0
i = 0

while True:
    #상하 이동 횟수를 더함
    answer += count[i]
    #움직일 필요 없으니까 0으로 초기화
    count[i] = 0
    #아무것도 움직이지 않아도 된다면 종료
    if sum(count) == 0:
        break

    left, right = 1, 1
    #기준점 왼쪽 이동 시 0이 발견되는 위치를 구함
    while count[i - left] == 0:
        left += 1
    #시작점 기준 오른쪽 이동 시 0이 발견되는 위치를 구함
    while count[i + right] == 0:
        right += 1
    answer += left if left < right else right
    i += -left if left < right else right

print(answer)