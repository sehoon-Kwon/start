import sys
num=int(input())
if num==1:
    print(int(input()))
else:
    dp=[]
    for i in range(num):
        dp.append(list(map(int,sys.stdin.readline().split())))
    dp[1][0]+=dp[0][0]
    dp[1][1]+=dp[0][0]
    if num==2:
        print(max(dp[num-1]))
    else:
        for i in range(2,num):
            for j in range(i+1):
                if j==0:
                    dp[i][j]+=dp[i-1][0]
                elif j==i:
                    dp[i][j]+=dp[i-1][j-1]
                else:
                    dp[i][j]+=max(dp[i-1][j-1],dp[i-1][j])
        print(max(dp[num-1]))
    
"""
삼격형의 크기 num이 주어지고 둘쨰줄 부터 n+1번째 줄까지 정수 삼각형이 주어진다.
첫쨰줄부터 대각선 왼쪽 오른쪽으로만 갈 수 있는데 마지막 줄까지 최대의 합을 구하는 문제이다.
dp 문제를 많이 접하다 보니 이정도는 쉽게 구상할 수 있었다.
먼저 dp에는 리스트별로 숫자를 넣어주고
dp[1]의 두개의 원소는 dp[0]을 더할 수 밖에 없기 떄문에 기준으로 넣어줬다.
1과 2의 경우 1은 바로 출력 2는 [0]과[1]을 더한 값중 최대의 값을 출력해서 오류가 없도록 만들어준다.
그 후 이중 for문을 통해서 가장 왼쪽과 가장 오른쪽은 바로 위의 숫자만 더할 수 있기 때문에 
j가 0인값과 j가 i와 동일한 값은 바로 위의 값을 더하도록 지정해주고
나머지 값들은 i-1줄의 j-1과 j 둘중 큰 값을 더해주면 완성이다.
점점 dp문제가 익숙해 지다보니 이정도는 빠르게 구상하고 문제를 이해하고 풀 수 있는것 같다.
더 공부하고 노력해서 다른문제도 바로바로 구상하고 풀 수 있도록 해야겠다.
"""