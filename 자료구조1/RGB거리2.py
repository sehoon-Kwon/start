import sys
inf=2147000000
num=int(input())
ans=inf
rgb=[]
for i in range(num):
  rgb.append(list(map(int,sys.stdin.readline().split())))
  
for i in range(3):
    dp=[[inf,inf,inf] for _ in range(num)]
    dp[0][i]=rgb[0][i]
    for j in range(1,num):
        dp[j][0]=rgb[j][0]+min(dp[j-1][1],dp[j-1][2])
        dp[j][1]=rgb[j][1]+min(dp[j-1][0],dp[j-1][2])
        dp[j][2]=rgb[j][2]+min(dp[j-1][0],dp[j-1][1])
    for j in range(3):
        if i!=j:
            ans=min(ans,dp[-1][j])
print(ans)

"""
집이 N개가 있는데 1번 집의 색은 2번 N번 집의 색과 같지 않아야 하고 N번 집의 색은 N-1번, 1번집의 색과 같지 않아야하고 i번 집의 색은 i-1, i+1집의 색과 같지않아야한다.
그 중에서 최솟값을 구하는 문제이다. 앞서 풀었던 RGB거리 문제랑 비슷하지만 이번 문제는 마지막 집과 첫번쨰 집의 색깔이 달라야한다.
그러므로 처음 집의 색을 미리 정해두고 dp를 구하면 된다. 그러므로 inf를 통해서 색을 지정한 후 RGB거리와 같은방식으로 min을 이용해 최소값을 구해나가면 된다.
RGB거리를 이용해서 문제를 풀어보려 했지만 시작값 고정을 어떻게 해야할지 정하지 못해서 계속 헤맷다 결국 정답코드를 참고하면서 정답을 작성했다.
졸작 준비와 과제가 겹쳐져서 혼자 공부하는시간이 많이 부족한 것 같다. 방학 시작하면 다시 열심히 공부해야겠다.

"""