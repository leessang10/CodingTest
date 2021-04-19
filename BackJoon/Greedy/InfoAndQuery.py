def isMatch(opt1, opt2):
    # opt1은 검색 정보, opt2는 회원 정보
    # 0언어/1직군/2경력/3음식/4점수
    #print("검색 정보: ", opt1)
    #print("회원 정보: ", opt2)
    # 지원자 점수가 검색 조건보다 작으면 False
    if int(opt1[4]) > int(opt2[4]):
        return False
    for i in range(4):
        # 검색 조건이 '-'이면 어떤 값이든 상관 없으니까 다음 항목으로
        # 항목이 서로 다르면 False
        if opt1[i] != '-' and opt1[i] != opt2[i]:
            return False
    return True


def solution(info, query):
    result = []
    #조건 정보 하나씩
    for q in query:
        cnt = 0
        #1. 조건 정보 q를 항목별로 분리
        opt1 = q.split(" and ")
        food, score = opt1[3].split(" ")
        opt1.pop()
        opt1.append(food)
        opt1.append(score)
        #opt1은 검색하려는 조건 정보

        #지원자 지원 정보 하나씩
        for f in info:
            opt2 = f.split(" ")
            #opt2는 지원자 정보
            #언어/직군/경력/음식/점수
            if isMatch(opt1, opt2):
                print("#########합격자: ", opt2)
                #print("")
                cnt += 1
        #print("======================================")
        result.append(cnt)


    print(result)



#지원자 정보
info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
]
#조건 정보
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]

solution(info, query)