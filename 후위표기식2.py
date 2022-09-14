import sys
num=int(sys.stdin.readline())
a=list(sys.stdin.readline().rstrip())
result=[]
num_list=[0]*num
for i in range(num):
    num_list[i]=int(input())
for i in a:
    if i.isalpha():
        result.append(num_list[ord(i)-ord('A')])
    else:
        b=result.pop()
        a=result.pop()
        if i=='+':
            result.append(a+b)
        elif i=='*':
            result.append(a*b)
        elif i=='/':
            result.append(a/b)
        elif i=='-':
            result.append(a-b)
print('%.2f' %result[0])
    

"""처음엔 i를 순서대로 넣고 기호가 나오면 마지막 숫자와 다음 숫자를 pop해서 두개를 기호에 맞게 연산해주는거였는데 숫자를 바로 input해서 append해주면
중복된 문자가 나오면 대처를 못하는게 오류였다. 그러므로 list에 ord[i]-ord['A']를 해서 알파벳 형태가 아닌 피연산자값의 형태로 저장해주면 해결된다.

