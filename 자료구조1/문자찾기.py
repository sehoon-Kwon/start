import sys
a=list(sys.stdin.readline().rstrip())
count=[-1]*26
for i in a:
    count[ord(i)-ord('a')]=a.index(i)
print(*count)

#이전에 풀었던 문자개수를 조금 더 배운 후에 다시 풀어봤다. 점점 생각의 폭이 늘어나는거 같아 뿌듯하다.
