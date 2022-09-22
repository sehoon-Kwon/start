def solution(clothes):
    answer=1
    cloth={}
    
    for i in clothes:
        if i[1] in cloth.keys(): # .keys()를 통해 cloth key값안에 clothes의 key가 없다면 cloth에 key를 추가하고 아니라면 key 기준으로 value에 넣는다.
            cloth[i[1]].append(i[0])
        else:
            cloth[i[1]]=[i[0]]
    
    for j in cloth.values():
        answer*=len(j)+1
    return answer-1
    
"""
clothes에는 2차원배열로 서로 다른 옷의 조합의 수를 구하는 문제이다
그래서 해시를 통해 key값 별로 해시테이블을 구성해주고
그렇게 구성된 cloth의 values를 기준으로 길이값 + 1을 answer에 곱해준다. 왜? 옷을 0개 혹인 1개 입기 떄문
그리고 아무것도 안입는 경우는 없다했으니 곱한 answer값에 -1 해서 return해준다. 
해시에 대해서 공부할 수 있는 기회였다.
"""
"""
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes]) # 2차원 배열이니 clothes[1]을 기준으로 Counter 시켜준다.
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 #reduce함수와 lambda를 통해 cnt의 values()값을 *해주는데 초기값은 1로 주어서 만약 2와 1이 value에 있었다면 1*(2+1) + 3*(1+1)를 통해 조합별 *를 구한다. 그리고 아무것도 안입는 경우가 없다했으므로 -1을해준다.
    return answer
    #이건 다른사람 풀이인데 파이썬을 잘 활용한거 같아서 가져왔다. reduce함수와 lambda함수의 기능을 좀 더 공부할 수 있었고 다음 문제에서 활용할 수 있었음 좋겠다.
"""