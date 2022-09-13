import sys
string=''
stack=[]
rhkfgh=False
word=list(sys.stdin.readline().rstrip())
for i in word:
    if i.isalpha(): #isalpha는 문자열이면 true를 도출한다. i가 만약 문자열이라면 바로 string에 넣어준다.
        string+=i
    elif i=='*' or i=='/': # 만약 i가 *나 /이면 stack이 차있고 stack의 마지막이 *나/이면 pop해주고 자신이 stack에 들어간다.
        while stack and (stack[-1]=='*' or stack[-1]=='/'):
            string+=stack.pop()
        stack.append(i)
    elif i=='+' or i=='-': #만약 i가 +나 -면 stack에 여는괄호 앞까지 모두 pop시키고 자신이 들어간다.
        while stack and stack[-1]!='(':
            string+=stack.pop()
        stack.append(i)
    elif i==')': #만약 i가 닫는괄호면 여는괄호까지 모두 pop하고 여는괄호를 pop시킨다.
        while stack and stack[-1]!='(':
            string+=stack.pop()
        stack.pop()
    elif i=='(': # 만약 여는괄호면 stack에 들어감.
        stack.append(i)
while stack:
    string+=stack.pop()
print(string)

#처음 봤을땐 어제 했던 < > 사이엔 reverse없고 나머진 reverse해서 출력하는 문제가 생각나서 True와 False로 나눌려고 했지만 중복 괄호가 생기면
#어김없이 오류가 생겼다. 그래서 다른사람들것을 참고해서 (도 스택에 넣고 닫는괄호가 생기면 여는괄호까지 pop시키고 만약 *이나/기 연산이 나오면 기존에 있던걸 pop해주고 자신이 들어간다. 우선순위가 동일하기 떄문에 먼저 들어간게 나올 수 있도록 하는것이다.
# +와 - 는 우선순위가 가장 낮기때문에 기존 등호를 (까지 모두 pop시키고 자신이 들어간다.
