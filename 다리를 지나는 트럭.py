def solution(bridge_length, weight, truck_weights):
    time=0
    num=[0]*bridge_length
    hap=0
    while num:
        time+=1
        hap-=num[0]
        num.pop(0)
        
        
        
        if truck_weights:
            if hap+truck_weights[0]<=weight:
                hap+=truck_weights[0]
                num.append(truck_weights.pop(0))
                
            else:
                num.append(0)
    return time
        
        
        
    
        
"""
truck_weights에서 앞에서차례로 다리를 건너는데 bridge_length는 다리에 올라갈 수 있는 트럭 개수, weight는 다리가 버틸 수 있는 무게이다

처음 구상은 truck_weights첫번쨰 요소와 b라는 리스트에 있는 요소를 더해 weights를 넘지 않는다면 추가하고 num이라는 변수에 count를 넣어
3을 넘어가면 pop시켜서 b변수에 넣는식으로 해보았다. 그러나 리스트에 2가지요소를 동시에 관리한다는건 쉽지 않았고 다른 방식을 고민해보았다.

다른사람의 풀이를 보면서 연구했는데, 먼저 bridge_length만큼 num에 0을 채운다.

그리고 time을 통해 시간을 계산하고 시간이 흐를떄마다 num을 pop시킨다.

truck_weights가 빌떄까지 num 즉 다리를 건너는 트럭의 합과 truck_weight첫 요소가 weight보다 작다면
t에 truck_weights 첫 요소를 넣고 num에다가 추가시킨다.
아니라면 다시 0을 append해서 num을 순환시킨다.
이 코드의 핵심은 num을 통해 0을 bridge_length만큼 넣어 자신의 차례가 되면 빠지게 하는것이다.


"""
