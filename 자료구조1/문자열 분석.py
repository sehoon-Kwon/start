import sys
while 1:
    
    string=list(sys.stdin.readline().rstrip('\n'))
    count=[0]*4
    if not string:
        break
    for i in string:
        if i.isupper():
            count[1]+=1
        elif i.islower():
            count[0]+=1
        elif i.isdigit():
            count[2]+=1
        elif i.isspace():
            count[3]+=1
    print(*count)
    

        
"""import sys
while 1:
    try:
        string=list(sys.stdin.readline().rstrip())
        count=[0]*4
        for i in string:
            if i.isupper():
                count[1]+=1
            elif i.islower():
                count[0]+=1
            elif i.isdigit():
                count[2]+=1
            elif i.isspace():
                count[3]+=1
        print(*count)
    except EOFError:
        break

처음 풀이한 상태, 왜 계속 뒤쪽 공란을 계산 안하는지 검색해보니 rstrip()문제였다. rstrip('\n')으로 해주면 빈칸과 스패이스바를 구분하기때문에 뒤쪽 스패이스바도 계산한다.
그리고 제출했더니 출력초과... 왜? 알고봤더니 input은 EOFError를 발생시키고 sys.stdin.readline()은 빈 문자열을 반환한다.
그래서 input을 썻으면 EOF sys.stdin.readline()을썻으면 not을 써서 오류를 잡아줘야한다.
"""
