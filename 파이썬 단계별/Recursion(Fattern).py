a=int(input())
def star(n):
    if n==3:
        return['***','* *','***']
    arr=star(n//3)
    stars=[]

    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(n//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(star(a)))
#재귀함수를 이용한 패턴찍기
