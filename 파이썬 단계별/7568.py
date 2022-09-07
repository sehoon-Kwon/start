a=int(input())
h=[]
t=[]
count=[]
for i in range(a):
    b,c=input().split()
    h.append(b)
    t.append(c)


for j in range(a):
    cnt=1
    for z in range(a):
        
        if int(h[z])>int(h[j]) and int(t[z])>int(t[j]) and j!=z:
            cnt+=1  
    count.append(cnt)
for z in count:
    print(z,end=' ')
            
