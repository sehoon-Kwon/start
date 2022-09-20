a=int(input())

def fivo(n):
    if n==0:
        return 1
    else:
        return n*fivo(n-1)

num=str(fivo(a))
count=0

for i in num[::-1]:
    if i=='0':
        count+=1
    else:
        print(count)
        break



"""숫자가 주어지면 n!의 뒤에서부터 처음 0이 아닌 숫자가 나올떄까지 0의 개수를 구하는 문제이다
먼저 재귀함수를 통해 팩토리얼을 구해주고 str로 변환후 뒤에서부터 0이면 count+=1해주고 아니면 count값을 print하고
break하게 구성했다.
"""
