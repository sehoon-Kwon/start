n, m = map(int, input().split())
ori = []
mini = []

for _ in range(n):
    ori.append(input())#기존 문양 받아오기

for a in range(n - 7): #8*8최대그기조절 경우의수로 
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):             
                if (j + b)%2 == 0: # 흰색으로 시작한경우와 검은색으로 시작한경우 두가지를 구함 인덱스의 합으로 홀짝을 구분
                    if ori[b][j] != 'W': idx1 += 1  
                    if ori[b][j] != 'B': idx2 += 1
                else :
                    if ori[b][j] != 'B': idx1 += 1
                    if ori[b][j] != 'W': idx2 += 1
        mini.append(idx1)                         
        mini.append(idx2)                         

print(min(mini))       
