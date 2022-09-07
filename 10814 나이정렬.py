import sys
a=int(sys.stdin.readline())

first=[]
for i in range(a):
    first.append(list(sys.stdin.readline().split()))

first.sort(key=lambda x:int(x[0]))

for i in range(a):
    print(first[i][0],first[i][1])


#문제는 오는순서로 정렬하는건데 어렵게 생각하다보니 인덱스를 따로 빼서 정렬하는 방법을 찾고있었다.
    # 4시간정도 고민하고 고치다가 도저히 궁금해서 찾아보니 그냥 정렬하면 된단다.
    # 단순하게 생각하는것도 필요한가보다.
