def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈
        # print("=", stack)
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # print("==", stack)

            # 값을 한개 빼서 k는 1 감소
            k -= 1
            # 내부의 값을 제거
            stack.pop()
        # 새로운 값을 삽입
        stack.append(num)

    # 남은 부분은 삭제
    if k != 0:
        stack = stack[:-k]
    answer = ''.join(stack)

    return answer