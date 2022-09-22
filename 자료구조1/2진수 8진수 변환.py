a=int(input())
a=str(a)
b=int(a,2)
print(oct(b)[2:])

"""
2진수를 8진수로 변환하는 문제이다. 나는 2진수를 먼저 10진수로 변환 후 8진수로 변환해서 출력하도록 구성했는데
시간초과가 떳다. 그래서 분명 내장함수로 써서 괜찮을텐데 하고 찾아보니
print(oct(int(input(),2))[2:]) 정답코드였다.
변수에 지정하지 않고 바로 input()을 print에 넣어버리는거였다. 시간초과를 좀 더 신경써서 코드작성에 유의해야겠다.
"""
