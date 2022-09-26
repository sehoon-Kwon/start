import heapq
def solution(scoville, K):
    heap=[]
    for i in scoville:
        heapq.heappush(heap,i)
    
    count=0
    while heap[0]<K:
        try:
            heapq.heappush(heap,heapq.heappop(heap)+(heapq.heappop(heap)*2))
        except IndexError:
            return -1
        count+=1
    return count
        
            
        
        
"""
만약 scoville의 원소중에 가장 작은 숫자가 K보다 작다면 원소 중 가장 작은수 + 두번째로 작은수*2의 값을 추가하고 두 값은 뺀다 그렇게 해서 
모든 원소가 K보다 크다면 연산을 한 횟수를 return해야하는 문제이다.
처음에는 min을통해 가장 작은값을 뽑아서 계산하는 방식으로 했지만 테스트케이스는 통과해도 시간초과를 당했다.
다음에는 sorted를 통해 append마다 sorted했더니 그것도 당연히 시간초과를 당했다.
그래서 문제의 유형답게 heap을 검색해서 기능을 보니 자동으로 pop과 append를 시행할때마다 정렬을 해준다는거보고 신세계를 보았다.
바로 heap을 통해 scoville을 heap에 넣어주었고
heap은 자동 정렬되기때문에 0원소가 K보다 클때까지 연산을 실시했고 heappush를 통해 원소를 넣고 heappop은 기존 pop과달리 가장 작은수를 pop시켜주었다.
그렇게 연산을 할때마다 count를 +1해주고 만약 더 연산할 값이 없다면 -1을 return해주고 만약 [0]값이 K보다 커졌다면
count를 return하게 했다. 맨날 sorted만 하다가 heap을 만나니 문제를 더 효율성있게 풀 수 있었다. 얼른 더 많은 기능들을 사용하여 효율적인 코드를 짜고싶다.
"""