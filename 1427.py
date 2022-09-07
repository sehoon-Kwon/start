a=list(map(int,str(input())))#자릿수마다 리스트에 저
sort_a=sorted(a,reverse=True)
for i in sort_a:
    print(i,end='')
