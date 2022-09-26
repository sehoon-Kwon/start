import sys
a,b=map(int,sys.stdin.readline().split())
num=int(input())
numlist=list(map(int,sys.stdin.readline().split()))
ten=[]
n=0
power=0
for i in numlist[::-1]: #a진법을 10진수로 바꾸기위해 1의자리부터 순서대로 a^0을 해준다(첫째 자리부터 계산을 위해 [::-1]을 통해 뒤집어서 계산한다)
    n+=(i*(a**power)) #n=n+(첫째자리*(a진법**0~자릿수만큼)
    power+=1
while n:
    ten.append(str(n%b)) # 이 수를 b진법으로 바꾸기위해 n을 b로 계속 나누며 나눈 나머지만 ten에 넣어준다.
    n//=b
print(' '.join(ten[::-1])) #첫째자리고 맨 뒤에 있어야 하므로 뒤집음
"""
a진법의 수를 b진법으로 출력하는 문제이다.
먼저 자리수의 개수만큼 받아온 numlist를 첫째자리부터 계산하기위해 뒤집어서 첫째자리 * a진법을 자릿수만큼 거듭제곱해서 n을 구해준다
그렇게 받아온 n을 b진법으로 나눈 나머지를 ten에 넣어주고 n은 b와 나눈 몫으로 계산한다
그렇게 받아온 ten을 첫째자리가 맨 뒤에 있어야 하므로 다시 [::-1]로 돌려서 출력해준다
"""
