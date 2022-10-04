"""
어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 예를 들어 11=32+12+12(3개 항)이다. 이런 표현방법은 여러 가지가 될 수 있는데, 11의 경우 11=22+22+12+12+12(5개 항)도 가능하다. 이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.
num=int(input())
cnt=0
sqnum=num//2
while num!=0:
    if num==1:
        cnt+=1
        break
    if sqnum*sqnum>num:
        sqnum-=1
    else:
        if num<4:
            cnt=cnt+3
            break
        else:
            num=num-(sqnum*sqnum)
            cnt+=1

print(cnt)
이건 내가 푼 코드이다. sqnum을 num의 2로 나누고 그 수부터 차례대로 제곱근이 num을 안넘어가는 숫자부터 제곱근한것을 -하고 
num이 4보다 작아지면 그 아래 숫자들은 1밖에 가능하지 않기때문에 그냥 3을 +시키고 break시켰다 테스트케이스는 통과했지만
정답으론 인정되지 못했다.최소 개수를 출력하는것을 만족하지 못했기 때문이다.
"""
num=int(input())
dp=[i for i in range(num+1)]
for i in range(1,num+1):
    for j in range(1,i):
        if (j*j)>i:
            break
        if dp[i]>dp[i-j*j]+1:
            dp[i]=dp[i-j*j]+1
print(dp[num])

"""
위는 정답코드를 인용해서 작성한 코드이다. dp에는 0부터 num+1까지 차례대로 넣는다. 왜? 1^2으로만 이루어진 숫자가 최대의 숫자이기 때문이다.
그렇게 dp[i]를 [i-j*j]+1보다 크면 dp[i]에 집어넣는다. 왜? 예를들어 dp[4]는 현재 값이 4이지만 i-j*j는 j가 2일때 dp[0]+1값은 1이기때문에 dp[4]는 1이된다. dp[5]는 dp값은 5이지만 dp[5-2*2]+1을하면 2가되기 때문에 dp[5]에는 2를 넣어주는것이다.
아직까지 구조적인 설계능력이 부족한 것 같다. 좀 더 많은 dp문제를 접해봐야겠다.
"""