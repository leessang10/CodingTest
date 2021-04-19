participant = ["marina", "josipa", "nikola", "vinko", "filipa"]

completion = ["josipa", "filipa", "marina", "nikola"]


for com in completion:
    for par in participant:
        if com == par:
            participant.remove(com)
    answer = participant[0]

