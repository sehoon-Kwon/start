import sys
num=int(input())
dp=[False for _ in range(num+1)] #min으로 구해야하기 때문에 0이아닌 False로 선언해준다.
p=[0]+list(map(int,sys.stdin.readline().split()))

for i in range(1,num+1):
    for j in range(1,i+1):
        if dp[i]==False: #만약 dp[i]가 False라면
            dp[i]=dp[i-j]+p[j] #i에 기본값을 넣어놓고
        else:
            dp[i]=min(dp[i],p[j]+dp[i-j]) # 최소값을 비교해서 값에 담아준다.
print(dp[num])

"""
카드구매하기1과 마찬가지로 이번엔 max값이 아닌 min값을 구하는 것이다 max 문제에서는
dp를 0으로 채웠지만 min을 구하기위해 False를 넣어놓고 기본값을 그다음에 집어넣은 후 min으로 최솟값을 뽑아내준다.
"""