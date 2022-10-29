import sys
a=int(input())
num=list(map(int,sys.stdin.readline().split()))
dp=[0 for i in range(a)]
for i in range(a):
    for j in range(i):
        if num[i]<num[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))

"""
이전에 풀었던 가장 긴 증가하는 부분수열과 동일한 문제이지만 이번엔 감소하는 부분수열의 가장 긴 개수를 구하는 문제이다.
마찬가지로 num[j]가 i보다 크고 dp[j]가 크다면 dp[i]를 dp[j]로 하고 dp[i]를 +1해준다.
비슷한 유형의 문제를 보면 여러 유형의 문제를 많이 풀어봐야 당황하지 않을 것 같다.
"""