def solution(numbers):
    num=sorted(numbers,key=lambda x:int(x%10),reverse=True)
        
    
    return ''.join(map(str,num))


"""
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


    가장 위 코드는 처음 작성한 코드이다. 첫째자리를 기준으로 정렬해서 출력하는거였는데 테스트케이스중 반만 맞췄다.
    중복에대한 부분도 있고 오류가 많았는데 다른사람의 풀이를 보고 도대체 무슨 원리로 저게 돌아가는지 알아보았는데
    numbers의 원소가 1000이하이기 때문에 number을 문자열로 리스트에 넣고 자릿수를 3자리로 맞춰주는거였다.
    그렇게되면  3과 31 310은 333 313 310이된다. 이렇게되면 문자열비교연산을 통해 첫 인덱스를 비교하고 같으면 다음 인덱스를 비교하기때문에 121과 12의 경우 12가 먼저 와야하는데 *3을 해주면 121121과 1212로 12가 먼저 정렬되게 하여 문제를 풀이한것이다.
    또한 마지막에 int로 변환하고 str로 변환해서 000을 처리해준다.
    문자열 정렬도 이해할 수 있었고 생각의 범위를 넓혀야 이런 코드도 짤 수 있구나를 느꼈다.


import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

    위 방법과는 또 다른 새로운 방법을 알았다. comparator를 통해 인자를 비교하는것이다.
    6, 10, 2라면 6과 10을 더해서 610 106이므로 revuerse=True로 6이 먼저 출력되고 같은 방법으로 6을 기준으로 2와 비교해서 62>26이므로 6이 먼저 출력된다.
    이렇게 정렬하면 6,2,10으로 정렬된다. 새로운 방법을 하나하나 배우니 뿌듯했다.

    """
