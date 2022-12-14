a=int(input())
dp=[0 for _ in range(a+1)]
if a<3:
    print(a)
else:
    dp[1]=1
    dp[2]=2
    for i in range(3,a+1):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[a]%10007)

"""
앞선 1로 만들기와 같은 DP를 사용하는 문제이다.
2xn 크기의 직사각형을 1x2와 2x1타일로 채우는 방법의 수를 구하는 프로그램을 만들어야한다.
입력되는 n의 수를보면 순서대로 1 2 3 5 8 13 으로 i-1과 i-2를 더한 값이 dp3이 된다.
그렇게되면 DP를 사용해 1과 2는 고정으로 넣어놓고 3부터 i-1 i-2를 더한 값을 추가한다.
마지막에는 문제에서 말한대로 방법의 수를 10007로 나눈 나머지를 출력하기 위해 dp[i]%10007 
DP는 문제의 의도를 파악하고 설계하는것이 중점인 것 같다. 
"""
