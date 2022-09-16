import sys
string=list(sys.stdin.readline().rstrip())
result=[]
for i in range(len(string)):
    result.append(string[i:]) # 첫번째 문자열 제거
result.sort()
for i in range(len(string)):
    print(''.join(result[i]))

