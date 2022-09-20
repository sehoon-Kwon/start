a,b=map(int,input().split())

def cnt_number(n,k):
    cnt=0
    while n:
        n//=k
        cnt+=n
    return cnt

answer=min(cnt_number(a,5)-cnt_number(b,5)-cnt_number(a-b,5),cnt_number(a,2)-cnt_number(b,2)-cnt_number(a-b,2))

print(answer)


"""
nCr을 구해서 끝자리 0의 개수를 출력하는 문제이다. 단순 재귀함수로 팩토리얼을 구하면 시간초과로 실패한다.
아무리 짜봐도 시간초과가 풀리지않아 답을 찾아보았다.
끝자리가 0이라는것은 10의배수라는 것이며 10은 2와 5로 구성되어있다. 2와 5가 짝이 맞아야하므로 2와 5의 개수중 더 작은게 10의 개수라고한다.
n//=k를 통해 5나 2가 n번 곱해진 수를 모두 count해주고 그중 가장 작은수를 print해준다.
여러 문제를 접해봐야겠다. 
"""
