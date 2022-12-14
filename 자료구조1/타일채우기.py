num=int(input())
dp=[0]*31
dp[2]=3
for i in range(4,num+1):
    if i%2==1:
        dp[i]=0
    else:
        dp[i]=dp[i-2]*3+sum(dp[:i-2])*2+2
print(dp[num])
    

"""
3xN크기의 벽을 2x1, 1x2크기 타일로 채우는 경우의수를 구하는 문제이다.
홀수의 경우 벽을 채울 수 없기 때문에 num이 홀수인 경우 0을 출력하게되고 
짝수인경우 dp[num-2]*3의 경우의수 + 0~num-4까지의 경우의수*2 + num에 대해 가로길이 num의 새로운 타일 만드는 경우 2가지를 합한것이 답이된다.
dp문제는 점화식 구성하는게 관건인것같다. 
"""