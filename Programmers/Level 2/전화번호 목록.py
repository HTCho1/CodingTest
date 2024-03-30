# 프로그래머스 Level 2
# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
from collections import defaultdict


def solution(phone_book):
    hash_dict = defaultdict(str)
    for p in phone_book:
        hash_dict[p] = p

    for ha in hash_dict:
        temp = ""
        for h in ha:
            temp += h
            if temp in hash_dict and temp != ha:
                return False
    return True


if __name__ == "__main__":
    phone_books = [["119", "97674223", "1195524421"],
                   ["123", "456", "789"],
                   ["12", "123", "1235", "567", "88"]]
    results = [False, True, False]

    for pb, res in zip(phone_books, results):
        out = solution(pb)
        if out == res:
            print('O')
        else:
            print('X')
