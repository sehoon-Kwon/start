import sys

temp="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #10진법이면 9까지 36진법이면 Z까지 표현
num1,num2=map(int,sys.stdin.readline().split())

answer=str()

while num1!=0:
    answer+=temp[num1%num2]
    num1//=num2

print(answer[::-1])

"""
진법변환은 16진수까지만 해보았는데 10진수를 36진법으로 출력하라길래 당황했다.
그래서 정답코드를 분석해보니 0부터Z까지 35까지 알맞는 숫자와 문자를 temp에 배치하고
10진법 수인 num1을 진법num2로 나눠 나온 나머지를 answer에 저장하고 revurse시켜서 출력해준다.
단순히 진법변환의 핵심으로 10진수로 예를들면 356를 10으로 나누면 몫은 35 나머지는 6이다 6을 정답에 추가하고 반복해주면 653이된다 우리는 맨끝자리에 대응될 값부터 구했기 떄문에 뒤집어주면 진법변환이 완료된다.
꾸준히 학습하는게 살길인것 같다.
"""