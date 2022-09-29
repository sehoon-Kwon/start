import heapq
def solution(sizes):
    heap=[]
    mleft=[]
    mright=[]
    for i in sizes:
        if i[0]>i[1]:
            heapq.heappush(heap,(i[1],i[0]))
        else:
            heapq.heappush(heap,(i[0],i[1]))
    for i in heap:
        heapq.heappush(mleft,i[0])
        heapq.heappush(mright,i[1])
    return max(mleft)*max(mright)
    """
    2차원 배열로 되어있는 sizes에서 모든 사이즈를 충족하는 명함의 최소 값을 구하는 문제이다.
    내가 설계한것은 heap을 사용해서 각 요소의 2개의 수를 비교해서 작은수는 왼쪽 큰수는 오른쪽으로 push했다.
    그 후 mleft와 mrgiht에 각 요소를 넣고 max로 큰값을 가져와 *연산을 해서 정답을 가져왔다.
    최대 9.86ms로 사실 시간을 생각안하고 푼거라 기대는 안했다.


    def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

    이건 다른사람 코드인데 최대 3ms로 내꺼보다 3배나 빠르다.
    여기서는 heap에 넣었다 뺴는게 아니라 for문으로 sizes에서 각각 요소를 가져와 a보다 b가 크면 순서를 바꿔서 a에 큰수 b에 작은수를 구성했다.
    그 후 row에 a중에 큰값을 col에 b중에 큰값을 가져와서 바로 연산했다. 이걸 보고 내 코드를 보니 매우 복잡해보인다. 좀 더 가독성 좋은 코드를 짜기위해 노력해야겠다.
    """