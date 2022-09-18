"""
priorities는 우선도 별로 인쇄물이 들어가있는데 숫자가 높을수록 우선도가 높다.
맨앞에 인쇄물부터 빼내는데 만약 뒤에 우선도가 더 높은 인쇄물이 존재할경우 빼서 맨 뒤에 넣는다.
location위치의 인쇄물이 나오는 순서를 출력하는 문제이다.
먼저 result에 priorities의 길이만큼 0을 넣고 location의 위치에 1을 넣었다.
priorities가 존재할떄까지 while문을 통해 만약 맨 앞에 priorities의 우선도가 가장 크다면
pop시키고 rank를 1 증가시킨다. 만약 result의 맨 앞이 1이라면 location위치라는 것이니 그대로 rank를 return해준다.
만약 아니라면 result도 동일하게 pop시켜버린다.
그리고 가장 큰 수가 아니라면 마찬가지 pop시킨 숫자를 다시 append시켜 맨 뒤로 넣는다.
result도 마찬가지로 빼서 뒤에 넣는다.
"""
def solution(priorities, location):
    rank=0
    num=0
    result=[0]*len(priorities)
    result[location]=1
    while priorities:
        if priorities[0]==max(priorities):
            priorities.pop(0)
            rank+=1
            if result[0]==1:
                return rank
            else:
                result.pop(0)
                
        else:
            priorities.append(priorities.pop(0))
            result.append(result.pop(0))

