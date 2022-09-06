n = int(input())
#n= 원반의 개수 a= 출발점기둥 b=보조기둥 c=도착기둥
def hanoi(n, a, b, c):
    if n == 1: #원반 하나를 옮기려면 그냥 옮기면 된다.
        print(a, c)
    else:
        hanoi(n - 1, a, c, b) 
        print(a, c)
        hanoi(n - 1, b, a, c)
sum=2**n-1
print(sum)
hanoi(n, 1, 2, 3)
