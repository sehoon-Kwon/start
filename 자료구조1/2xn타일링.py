dp=[0]*1001
dp[0]=1
dp[1]=1
a=int(input())
for i in range(2,a+1):
    dp[i]=dp[i-1]+dp[i-2]*2

print(dp[a]%10007)

"""
앞서 풀었던 1xn타일링과 동일한 문제이다. 2xn직사각형을 1x2,2x1,2x2타일로 채우는 방법의 수를 구하는 문제이다.
i=i-1+(i-2)*2의 규칙이다. 0과 1을 미리 정해주고 dp를통해 구해주면 간단히 구할 수 있다.

"""