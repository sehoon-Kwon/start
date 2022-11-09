dp=[]
for i in range(9):
    dp.append(int(input()))

sdp=sum(dp)
first=0
second=0
for i in range(8):
    for j in range(i+1,9):
        if sdp-(dp[i]+dp[j])==100:
            first=dp[i]
            second=dp[j]
dp.remove(first)
dp.remove(second)
dp.sort()
for i in dp:
    print(i)
    
"""
처음 접하는 브루트포스 문제로 9개의 숫자중 7개가 100이되는 경우의 7개의 수를 오름차순 정렬로 출력하는 문제이다.
그래서 먼저 배열의 합을 구하고 만약 배열-(i+j)가 100이라면 first와 second에 지정시켜준다.
여기서 정답이 여러가지인 경우 아무거나 출력한다. 라고 조건이 명시되어있기 때문에 마지막으로 나온 first,second를 배열에서 지워주고
정렬해서 출력해줬다. 브루트포스 들어가는 문제라 아직까진 쉬운 것 같다. 
"""