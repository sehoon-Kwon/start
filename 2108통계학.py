import sys
from collections import Counter
num=int(input())
num_list=[]
num_list2=[0]*4001

for i in range(num):
    num_list.append(int(sys.stdin.readline()))
snum_list=sorted(num_list)
cnt=Counter(snum_list).most_common(2) ## 2개의 가장 흔한 값 도출 이렇게되면 cnt에[('값',횟수),('값',횟수)]

print(round(sum(num_list)/num))
print(snum_list[num//2])
if len(snum_list)>1: #만약 snum_list가 하나 이상이라면
    if cnt[0][1]==cnt[1][1]: #그런데 만약 2개의 값의 횟수가 같다면?
        print(cnt[1][0]) # 2번째 값 출력
    else:
        print(cnt[0][0]) # 아니라면 1번째 값 출력
else:
    print(cnt[0][0]) #1개밖에없으면 그냥출력
if len(snum_list)>1:
    if snum_list[num-1]<=0 and snum_list[0]<=0:
        print(abs(snum_list[0])-abs(snum_list[num-1]))
    elif snum_list[num-1]<=0 or snum_list[0]<=0:
        print(abs(snum_list[num-1])+abs(snum_list[0]))
    else:
        print(abs(snum_list[num-1])-abs(snum_list[0]))
else:
    print(0)
