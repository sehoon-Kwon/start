from collections import deque
def solution(prices):
    answer=[]
    prices=deque(prices)
    while prices:
        sec=0
        p=prices.popleft()
        
        for price in prices:
            sec+=1
            if price<p:
                break
        answer.append(sec)
    return answer
"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
사실 처음에는 문제 이해를 못했다. 그래서 다른사람들 보니까 다들 이해를 못했다더라 그래서 분석해본결과는
prices는 [1,2,3,2,3]
return은 [4,3,1,1,0]
으로 1초시점의 1원의 주가는 더 떨어진적 없이 끝까지 가격이 떨어지지 않았으니 4를 return
2초시점의 2원의 주가는 더 떨어진적 없이 끝까지 가격이 떨어지지 않았으니 3을 리턴
3초시점의 3원의 주가는 1초뒤에 가격이 떨어지므로 1을 리턴
4초시점의 2원의 주가는 1초간 가격이 떨어지지 않았으므로 1을 리턴
5초시점의 3원은 마지막이므로 0을 리턴해준다.

코드분석은 먼저 deque로 prices를 선언해주고
p로 가장 앞에 숫자를 pop해준다.
prices리스트에서 초를 1 더해주고 만약 price보다 p가 크다면 break 해버린다 왜? 가격이 떨어진것이기 떄문
그리고 걸린 시간을 answer에 넣어준다.

사실 문제 구상보다는 문제 이해가 더 오래걸린 타입이다.
문제를 보고 무슨 알고리즘을 써야하는지 바로 알아야한다는데 더 세밀히 공부 해야겠다.
"""
