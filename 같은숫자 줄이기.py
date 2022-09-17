def solution(arr):
    stack=[]
    result=[arr[0]]
    for i in arr:
        if stack:
            num=stack.pop()
            if num!=i:
                result.append(i)

        stack.append(i)

            
        

    return result
"""
배열중에 붙어있는 숫자를 하나로 줄이는 문제인데 처음 숫자는 stack에 집어넣고 stack이 차있다면 stack에 마지막 숫자를 빼서 i와 비교하고 i와 다르다면 result에 i를 넣는 방식이다.                





def no_continuous(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result

이건 다른사람 풀이인데 result가 비어있다면 result에 c를 추가하고 아니라면 result의 마지막 숫자와 비교해서 다르다면 추가하는 방식이다
이게 더 가독성 있고 간단해서 가져와봤다. 역시 꾸준히 노력해야겠다.
"""
