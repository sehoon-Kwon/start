import sys,math
a=int(input())
for i in range(a):
    sum=0
    num=list(map(int,sys.stdin.readline().split()))
    for j in range(1,num[0]):
        for z in range(j+1,num[0]+1):
            sum+=math.gcd(num[j],num[z])
    print(sum)
"""
a는 테스트케이스의 개수고 num의[0]은 테스트케이스 수의 개수가 나타난다. 각 테스트케이스의 모든 쌍의 GCD의 합을 구하는 문제이다.
나는 먼저 sum변수를 만들어주고 num에 리스트를 담아주었다. 그리고 for문을 통해 num[0]을 제외한 테스트케이스 수 개수보다 하나 모자라게 i를 돌려주고
j를통해 i+1부터 j끝까지 비교하도록 for문을 작성했다. 그리고 sum변수에 math.gcd를 통해 GCD를 각자 더해서 sum을 도출하게 만들었다.
"""
