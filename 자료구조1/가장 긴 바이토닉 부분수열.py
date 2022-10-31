import sys
num=int(input())
stack=list(map(int,sys.stdin.readline().split()))
restack=stack[::-1]
fresult=[1]*num
rresult=[1]*num
for i in range(num):
    for j in range(i):
        if stack[i]>stack[j]:
            fresult[i]=max(fresult[i],fresult[j]+1)
        if restack[i]>restack[j]:
            rresult[i]=max(rresult[i],rresult[j]+1)
    
result=[0]*num
for i in range(num):
    result[i]=fresult[i]+rresult[num-i-1]-1

print(max(result))

"""
앞선 문제와 비슷한 바이토닉 부분 수열을 구하는 문제이다. S를 기준으로 왼쪽은 작은수 오른쪽은 큰수로 이루어져있는 가장 긴 수열을 찾는 문제인데
restack에는 stack의 역순을 넣어 작아지는 긴 수열을 구할 수 있게 준비하고
for문을통해 stack의 왼쪽 즉 증가하는 부분수열을 구해서 fresult에 넣어주고 
restack에 역순으로 넣어진 숫자로 증가를 구해주면 역순으로 작아지는 부분수열을 구할 수있다.
마지막엔 result를 통해 0으로 예를들면 fresult[0]과 rresult[7]을 더하고 주어진 수열의 각 마지막숫자는 겹치기 때문에 -1해서 결과를 구해준다.
사실 구상만했지 제대로 코드는 작성하지 못해서 정답코드를 보고 분석해서 작성해보았다.
여러 유형을 접해봐야 여기서 역순으로 돌려서 구하는 이런 방식의 문제도 풀 수 있을 것 같다.
"""