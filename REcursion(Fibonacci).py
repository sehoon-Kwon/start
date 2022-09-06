a=int(input())
def fivo(N):
    if N<=1:
        return N
    return fivo(N-1)+fivo(N-2)
        
print(fivo(a))
