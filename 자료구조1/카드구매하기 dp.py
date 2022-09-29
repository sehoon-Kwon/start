import sys
num=int(input())
dp=[0 for _ in range(num+1)]
p=[0]+list(map(int,sys.stdin.readline().split()))

for i in range(1,num+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i],p[j]+dp[i-j])
print(dp[num])

"""
마찬가지로 dp를 이용하는 문제인데 문제 이해하는데 오래걸렸다.
만들어야하는 카드의 개수가 num으로 주어지고
밑에 Pn만큼의 숫자가 순서대로 주어진다. 인덱스 값을 합쳐서 num을 만들어야하며 그에 상응하는 값이 가장 큰것을 구하는 문제이다.
점화식은 dp[i]=p(j)+dp[i-j]이고 dp[1]은 1개 dp[2]는 d[1]+p[1] or d[0]+p[2]이다

dp는 문제이해도가 정말 중요한것 같다. 이해만 하면 풀기는 쉽다.
"""