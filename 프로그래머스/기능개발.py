"""
각 기능은 진도가 100%일떄 서비스에 반영할 수 있다. 앞에 있는 progresses가 100%가 되어야만 다음 progresses가 배포될 수 있다.
만약 뒤에 있는 progresses가 먼저 100%가 완료될시 앞에있는 progresses가 100%가 될떄 같이 배포된다.
일별로 배포될떄 몇개의 progresses가 밸포되는지 출력하는 문제이다.
먼저 progresses + day*speeds가 100이 넘지 않는다면 day를 점점 늘려서 100이 되게 맞춘다.
만약 100이 되면 pop시키고 cnt를 1 증가시킨다. day는 그대로이기 떄문에 다음 progresses가 100이 넘는다면
바로 pop시키고 cnt를 1 증가시킨다. 만약 다음 progresses가 100을 못넘긴다면 cnt를 result에 append시킨다.



"""
def solution(progresses, speeds):
    result=[]
    day=0
    cnt=0
    while len(progresses):
        if (progresses[0]+day*speeds[0])>=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        else:
            if cnt>0:
                result.append(cnt)
                cnt=0
            day+=1
    result.append(cnt)
    return result
