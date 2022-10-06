import sys
num=int(sys.stdin.readline())

dp=[1]*10

for i in range(num-1):
    for j in range(1,10):
        dp[j]+=dp[j-1]

print(sum(dp)%10007)

"""
오르막수는 수의 자리가 오름차순을 이루는 수를 말한다 예를들어 2234 3678등의 수를 말한다.
수의 길이 num이 주어질때 오르막 수의 개수를 구하는 문제이다. 처음 접했을땐 예전에 풀었던 쉬운계단수 문제가 생각났다.
당시 그 문제는 [i]는 자리수 [j]는 앞에올 수 있는 일의자리수를 기준으로 문제를 푸는거였는데 그렇게 풀면 2자리 문제 밖에 못풀어서 구상하진 못했다.
그래서 점화식만 보고 문제를 풀려고했는데 점화식을 보니 끝나는 숫자를 기준으로 점화식을 풀어놨다.
점화식만보면
    0   1   2   3   4   5   6   7   8   9
1   1   1   1   1   1   1   1   1   1   1

2   1   2   3   4   5   6   7   8   9   10

3   1   3   5   9   14  20  27  35  44  54

이다. 보면 dp[j]=dp[j]+dp[j+1]로 점화식이 구성되는걸 볼 수 있다
이를 통해 dp를 구상해서 sum으로 합을 구해준다.

"""