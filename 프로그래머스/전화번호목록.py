def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

"""
phone_book에서 전화번호부에 적힌 전화번호 중 한 번호가 다른 번호의 접두어인 경우를 확인하는 문제이다.
그래서 phone_book을 정렬시켜 번호의 숫자가 적은 숫자부터 비교를 해서 접두어가 나오면 False를 리턴시켰다.
"""
