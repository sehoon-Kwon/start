def solution(participant, completion):
    hashDict={}
    Hsum=0
    
    for i in participant:
        hashDict[hash(i)]=i
        Hsum+=hash(i)
        
    for j in completion:
        Hsum-=hash(j)
        
    return hashDict[Hsum]

                


"""
participant배열에서 completion에 완주한 목록에 없는것을 도출하는 문제이다.
처음에는 단순히 차집합으로 list(set(participant)-set(completion))을통해 제출했지만 중복되는 케이스에서 틀렸다.
다음은 for문을 통해 하나하나 비교식으로 pop해서 마지막에 남는 친구를 return하는 방식이였는데 이건 시간초과로 오답이였다.
그래서 정답코드를보니 해시를 사용해 participant의 key를 모두 더한값에서 completion의 hash를 뺀 숫자의 키를 가진 하나를 출력하는거였다.
hash를 처음 접해봐서 그런지 시간이 다소 걸렸는데 hash(i)를 통해 key값을 넣고 Hsum 변수를 통해 합을 구한다. 그리고 compleyion을 for문을 통해 hash로 key값을 모두 빼면
남은 key값의 value를 도출하는것이다. 역시 다양한 유형을 경험하고 학습해야한다.
"""
