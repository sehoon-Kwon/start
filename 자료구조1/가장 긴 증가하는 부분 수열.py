"""
열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

import sys
a=int(input())
num=list(map(int,sys.stdin.readline().split()))

dp=[]
state=False
for i in range(a-1):
    dpp=[num[i]]
    for j in range(i+1,a):
        if dpp[-1]<num[j]:
            dpp.append(num[j])
    print(dpp)
    if(len(dpp)>a//2):
        print(len(dpp))
        state=True
        break
    else:
        dp.append(len(dpp))
if state==False:
    print(max(dp))
이건 내가 푼 방법이다. dp로 푸는방법은 도저히 생각이 안나서 그냥 생각나는데로 설계 후 코드를 짜보았다.
단순히 큰값이 나오면 cnt하는것이라 테스트 케이스의 일부는 통과했지만 정확한 수열의 길이의 최댓값을 구하진 못했다 왜 ? i보다 j가 크지만 최대의 효율을 위해 뛰어 넘겨야 하는 경우가 있기 떄문
그래서 i와 j사이의 차가 가장 작은 숫자들 순으로 계산해서 구해보려했지만 설계를 제대로 못해서 포기했다.. 

"""
import sys
a=int(input())
num=list(map(int,sys.stdin.readline().split()))
dp=[0 for i in range(a)]
for i in range(a):
    for j in range(i):
        if num[i]>num[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))
"""
이건 정답코드를 보고 새로 짠 코드이다. i 이전의 숫자들과 비교해서 dp중에 가장 큰값을 i에 저장시키고
dp i 에는 +1 해준다. 이렇게하면 그 전의 숫자들을 이용해 배열에 그 숫자까지 도달하는 최대의 길이를 구할 수있다.
맨날 앞에있는 숫자를 뒤에 숫자와 비교하는 방식에서 해당숫자의 앞에 숫자들과 비교해서 동일시시키고 +시킨다는건 새로운 방식이였다.
잘 배워둬서 다음에 비슷한 문제가 나온다면 응용해봐야겠다.
"""
    