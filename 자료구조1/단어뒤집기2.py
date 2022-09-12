import sys
b=list(sys.stdin.readline().rstrip())
tag=False
first=''
result=''
for i in b:
    if tag==False:
        if i=='<':#<이면 tag를 true로 바꾸고 정상출력하게 만듬
            tag=True
            first+=i
        elif i==' ':#만약 공백이면 공백 추가하고 그전까지 저장된 first를 result에 추가함 그리고 first초기화
            first+=i
            result+=first
            first=''
        else:
            first=i+first #첨부터 왼쪽부터 넣어서 역순으로 배치함
    elif tag==True:#만약 <안에있다면 정상출력
        first+=i
        if i=='>':#만약 >이면 tag를 false로 돌리고 <>사이에있는거 그대로 합침 그리고 first 초기화
            tag=False
            result+=first
            first=''
    
print(result+first) #만약 <>없이 기본연결되면 first에 저장만되어있는 배열이 있기 떄문에 result+first로 출

#파이썬의 스택에 대해서 조금 더 고민할 수 있는 문제였다.리스트가아닌  단순 문자열로도 풀이가 가능했다.
