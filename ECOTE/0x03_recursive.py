def recursive(i):
    if i == 100:
        return
    print(i, "재귀 함수")
    recursive(i+1)
    print(i, "종료")


recursive(1)