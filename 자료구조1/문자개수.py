import sys
string=list(sys.stdin.readline().rstrip())
count=[0]*26 #알파벳 개수만큼
for i in string:
    count[ord(i)-ord('a')]+=1 #ord를 0으로 만들어서 index를 맞춘
print(*count)
