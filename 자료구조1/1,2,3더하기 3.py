num=int(input())
dp=[0]*1000001
dp[0]=1
dp[1]=1
dp[2]=2
for i in range(3,1000001):
    dp[i]=dp[i-1]%1000000009+dp[i-2]%1000000009+dp[i-3]%1000000009

for i in range(num):
    a=int(input())
    print(dp[a]%1000000009)

"""
앞서 풀었던 1,2,3더하기 5를 풀었기때문에 3은 모방해서 풀었다.
풀었던것처럼 점화식은 dp[i]=dp[i-1]+dp[i-2]+dp[i-3]을 통해서 풀었고
숫자가 워낙 커서 dp[i]에 넣을때 바로 %1000000009를 통해서 시간을 줄여서 통과했다.

"""