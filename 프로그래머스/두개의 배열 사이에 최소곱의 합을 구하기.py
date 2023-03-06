def solution(A,B):
    answer=[];
    for i in range(len(A)):
        answer.append(min(A)*max(B))
        A.remove(min(A))
        B.remove(max(B))
    return sum(answer)