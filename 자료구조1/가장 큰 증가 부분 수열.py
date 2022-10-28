import sys
num=int(input())
stack=list(map(int,sys.stdin.readline().split()))
result=[0]*num
result[0]=stack[0]
for i in range(1,num):
    for j in range(i):
        if stack[j]<stack[i]:
            result[i]=max(result[i],result[j]+stack[i])
        else:
            result[i]=max(result[i],stack[i])
    
print(max(result))

"""
시험기간이 끝나 오랜만에 문제를 풀어보았다. 수열 stack이 주어지는데 부분수열중 합잉 가장 큰것을 구하는 문제이다.
처음 구상은 for문을 거꾸로돌아 먼저 나오는 낮은숫자와의 합을 구해서 마지막에 max를 하는거였는데 부분수열이기 때문에
테스트케이스가 통과안되는 몇개가 있었다. 그래서 앞에서부터 순서대로 수열 i와 j를 비교해 수열 i가 더 크다면
result[i]와 result[j]와 stack[i]를 비교해 큰값을 집어넣는 방식으로 풀었다.
"""