def solution(s):
    stack=[]
    for i in s:
        if stack:
            if i=='(':
                stack.append(i)
            else:
                stack.pop()
        else:
            if i==')':
                return False
            else:
                stack.append(i)
    if len(stack)==0:
        return True
    else:
        return False
"""괄호가 모두 짝이 있으면 True 없으면 False를 return하는 문제이다.
먼저 stack이 차있으고 i가 (면 stack에 넣고 아니면 )이기떄문에 stack을 pop시킨다.
stack이 비어있고 i가 )라면 무조건 짝이 맞지 않기때문에 False를 retun해주고
아니라면 stack에 추가해준다.
만약 마지막에 stack이 비어있다면 모두 짝이 있기때문에 True를 리턴
아니라면 짝이 없으므로 False를 return해준다.



        
def is_pair(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

이건 다른사람 풀이인데 단순히 )의 개수가 (보다 더 많아지면 바로 break해버리는 풀이인데 이렇게 풀 수 도있으니 신기했다. 
