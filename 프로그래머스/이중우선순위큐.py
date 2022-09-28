import heapq
def solution(operations):
    answer = []
    heap=[]
    rheap=[]
    for i in operations:
        a,b=i.split()
        b=int(b)
        if a=='I':
            heapq.heappush(heap,b)
        elif a=='D':
            if heap:
                if b==-1:
                    heapq.heappop(heap)
                else:
                    mvalue=max(heap)
                    heap.remove(mvalue)
    if not heap:
        return [0,0]
                    
    return max(heap),heap[0]


"""
이중우선순위큐 문제로 oprations에는 순서대로 명령이 들어가있다.
I 숫자는 큐에 주어진 숫자를 삽입
D 1 은 최댓값을 삭제
D -1은 최솟값을 삭제한다.
그래서 나는 먼저 heap을 만들고
operations에서 i를 공백을 두고 뽑아와서 a,b에 넣었다. b는 문자와 숫자의 정렬이 다르므로 int형으로 만들어준다.
만약 a가 I면 b를 heap에 넣어주고 a가 D이고 heap이 차있다면 b가 -1일때 heap은 가장 작은숫자를 pop시키고
b가 1이라면 mvalue에 heap의 가장 큰값을 넣고 remove시켜준다.
마지막에는 heap이 비어있을때는 0,0을 출력하라고 했기 떄문에 return [0,0] 시켜주고
비어있지 않다면 최댓값과 최솟값으 return 시켜준다.

heap연습문제들을 풀고 이 문제를 풀어서 그런지 간단히 풀 수 있었다. 발목을 잡은건
최댓값이였는데 단순히 max를 사용해 heap의 최댓값을 뽑고 remove시키는 간단한 구현으로 성공시켰다.
점점 발전하고 자신감 있게 설계하는 모습을 보니 뿌듯하다.
"""