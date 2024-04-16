# 프로그래머스 Level 2
# 오픈 채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888
from collections import defaultdict


def state_to_message(state, name):
    if state == "Enter":
        return f"{name}님이 들어왔습니다."
    elif state == "Leave":
        return f"{name}님이 나갔습니다."


def solution(record):
    a = []
    uid_dict = defaultdict(str)

    for info in record:
        i = info.split(' ')
        if i[0] != "Leave":
            uid_dict[i[1]] = i[-1]

    for info in record:
        i = info.split(' ')
        state = i[0]
        if state != 'Change':
            message = state_to_message(i[0], uid_dict[i[1]])
            a.append(message)
    return a


if __name__ == "__main__":
    records = [["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]]
    result = [["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]]

    for re, res in zip(records, result):
        out = solution(re)
        if out == res:
            print('O')
        else:
            print('X')
