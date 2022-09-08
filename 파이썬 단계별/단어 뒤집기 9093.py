import sys
a=int(sys.stdin.readline())

for i in range(a):
    b=list(sys.stdin.readline().split())
    for j in b:
        print(j[::-1], end=' ') #b의 리스트를 반대로 출력함. 보통 어레이는 array[start:end:step]이고 start는 시작인덱스 end는 끝낼인덱스 step는 건너뛸개수와 방향인데 음수일 경우 역순으로 출력이다.
    
    print() #띄어쓰기 떄문에 넣어둠
