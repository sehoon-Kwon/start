a=int(input())
def factorial(N):
    if N==0:
        return 1
    else:
        return N * factorial(N-1)
print(factorial(a))
#재귀함수를 사용해 팩토리얼 구현
#재귀함수는 for문에 비해 느리지만 코드 길이와 변수가 적어 가독성이 높아진다.
#또한 피보나치 수열과 팩토리얼 등은 재귀함수를 이용하는것이 더 간단하다.
#가독성을 위해 속도를 극한까지 끌어올릴 필요가 없는이상 재귀함수를 사용하는것이 올바르다고 한다.
