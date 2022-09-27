import heapq
def solution(jobs):
    heap=[]
    now,answer,i=0
    start=-1
    while i<len(jobs): 
        for j in jobs:
            if start<j[0]<=now: #전의 패킷 시작시간보다 크고 현재 시간보다 작거나 같으면 heap에 소요시간과 시작시간 순으로 넣는다 왜? 소요시간이 짧은 순서대로 넣어야하기 떄문에 소요시간을 먼저 넣는다.
                heapq.heappush(heap,[j[1],j[0]])
        if heap: #만약 heap에 값이 있다면
            cur=heapq.heappop(heap) # 소요시간이 짧은것을 cur에 pop시킨다.
            start=now # 현재시점을 now와 바꾼다. 왜? 현재시점을 최신화 시켜줘야 jobs에서 이미 지난 패킷을 거를 수 있음
            now+=cur[0] #현재 시간은 heap에서 빼온 가장 짧은 소요시간을 더해준다.
            answer+=(now-cur[1]) # 결괏값에는 현재시간에서 시작시간을 빼서 더해준다. 왜? 대기시간을 빼줘야하기 때문
            i+=1 # 하나의 패킷이 처리되었기 때문에 i를 1 더해준다.
        else:
            now+=1 # 만약 처리할 값이 없다면 now를 1늘려서 다음 패킷을 받는다.
    return int(answer/len(jobs)) # 평균값을 구해야하기 때문에 연산해준다.
"""
위는 start까지 사용하여 정답코드이다. 데이터 패킷을 전송하는 평균의 최소값을 산출하는 문제이다.
jobs는 2차원으로 되어있으며 각 배열의 [0]에는 시작시간 [1]에는 소요시간이 들어가있다.
처음에는 heap을 역으로 넣어서 소요시간이 짧은 순서대로 계산을 하려고 했는데 현재 시간을 소유하면서 
그에따른 응답시간을 계산하려고 하니 방법이 잘 떠오르지 않았다. 그래서 정답코드를 일부 보면서 내 식대로 설계를 해보려고 했지만
0,3 1,9 2,6의 기댓값은 9 였지만 6이 나왔다. 아래는 정답코드를 보면서 내 식대로 푼 식인데 거의 다 비슷하지만 start 없이 풀었다
저 당시에는 start의 필요성을 제대로 파악도 못한채 heap에 넣으면 자동으로 정렬되기 떄문에 작은 순서대로 pop할것이다 라고 생각했지만
jobs을 pop하는 것이 아닌 heap에 push하고 pop을 해서 jobs에는 영향을 끼치지 않으므로 start가 없으면 계속 0,3이 연산될것이다. 이런 단순한 문제도 파악하지 못한채
정답 코드를 인용하면서도 문제를 못 푼 나에게 화가났다. 못푸는건 아직 실력이 없기 떄문에 배우면 되지만 어이없는 실수는 방지해야한다. 
좀 더 꼼꼼하게 코드를 살펴보고 내것으로 만들어야겠다.   
import heapq
def solution(jobs):
    heap=[]
    now=0
    answer=0
    i=0
    while i<len(jobs):
        for j in jobs:
            if j[0]<=now:
                heapq.heappush(heap,[j[1],j[0]])
        if heap:
            cur=heapq.heappop(heap)
            now+=cur[0]
            answer+=(now-cur[1])
            i+=1
        else:
            now+=1
    return int(answer/len(jobs))
"""