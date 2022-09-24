a=int(input())
result=''
if a==0:
    print(0)
while a!=0:
    if a%-2:
        a=a//-2+1
        result='1'+result
    else:
        a=a//-2
        result='0'+result
print(result)

"""
10진법으로 표현된 a를 -2진법수로 출력하는 문제이다.
a가 0이될때까지 a를 -2로 나눠서 0이 아니라면 a를 -2로 나눈 몫에 +1을 해주고 result 앞에 1을 넣는다
0이라면 a를 -2로 나는 몫을 사용하고 result앞에는 0을 넣는다.
"""