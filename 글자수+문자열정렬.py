import sys
a=int(sys.stdin.readline())
word=[]
for i in range(a):
    b=sys.stdin.readline().strip() #readline은 \n이 기본이기때문에 strip을 써서 붙여준다.
    word.append(b)

set_word=set(word)#중복을 없애라 했기 떄문에 set으로 먼저 중복을 제거해준다.

sort_word=[]
for i in set_word:
    sort_word.append((len(i),i)) #글자수가 1차로 정렬되어야하기때문에 len(i)로 글자 수를 넣어준다.
sort_word.sort(key=lambda x: (x[0],x[1]))#lambda를 통해 0번째로 정렬 후 1번째 기준으로 다시 정렬 하는것


b=[i[1]for i in sort_word] #2차원에서 한열을 취합후 다시 print 해준다.
for i in b:
    print(i)
