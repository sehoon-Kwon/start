num=int(input())
dp=[0]*12
dp[0]=1
dp[1]=1
dp[2]=2
for i in range(3,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
for i in range(num):
    a=int(input())
    print(dp[a])
"""
정수 a를 입력받아 1,2,3의 합으로 나타내는 방법의 개수를 출력하는 문제이다.
규칙을 알면 쉬운데 dp[3]= dp[0]+dp[1]+dp[2] 처럼 i=(i-1)+(i-2)+(i-3) 인 규칙을 이용해
dp를 사용해서 구해보았다.
"""