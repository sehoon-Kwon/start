import sys
num=int(input())


for i in range(num):
    cnt=int(input())

    num1=list(map(int,sys.stdin.readline().split()))
    num2=list(map(int,sys.stdin.readline().split()))
    

    for j in range(1,cnt):
        if j==1:
            num1[1]+=num2[0]
            num2[1]+=num1[0]
        else:
            num1[j]+=max(num2[j-1],num2[j-2])
            num2[j]+=max(num1[j-1],num1[j-2])
    
    print(max(num1[cnt-1],num2[cnt-1]))


"""
num개수만큼의 2xcnt개수의 스티커가 존재하고 한장을 때면 변을 공유하는 스티커는 모두 찢어진다고 한다. 스티커마다 점수가 존재하고 최대의 스티커를 떼어내려고 한다. 최댓값을 구하는 문제이다.
처음 구상은 num1과 num2로 각 줄의 숫자를 구하고 대각선의 숫자를 더해서 최댓값을 구하는 식으로 구상했는데
간과한게 있었는데 num1의 [0]값을 선택하면 num1[1]과 num1[0]이 없어진다. 바로 대각선말고 대각선+1을 선택할 수 있는데
바로 대각선과 대각선+1의 합 중 최댓값을 구하면 되는 문제이다. 최대의 경우의 수를 파악해야지 dp문제를 쉽게 풀 수 있을것 같다.
문제를 유심히 관찰하는 힘을 길러야겠다.
"""