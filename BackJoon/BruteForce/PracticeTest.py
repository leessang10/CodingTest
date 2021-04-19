
answers = [1, 3, 2, 4, 2]


#문제 조건
student1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
student2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

score = [0, 0, 0]

for i in range(len(answers)):
    #학생1이 맞은 갯수
    if answers[i] == student1[i % len(student1)]:
        score[0] = score[0] + 1
    if answers[i] == student2[i % len(student2)]:
        score[1] = score[1] + 1
    if answers[i] == student3[i % len(student3)]:
        score[2] = score[2] + 1
answer = []
mx = max(score)
for i in range(len(score)):
    if mx == score[i]:
        answer.append(i+1)
print(answer)