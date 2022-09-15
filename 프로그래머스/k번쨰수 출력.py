def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        sort_num=sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(sort_num[commands[i][2]-1])
    return answer


"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

위에껀 내가 쓴거고 밑에껀 다른사람이 쓴건데 1줄로 작성한거보고 대단하다고 느꼈다.
아직 파이썬의 lambda식을 배우진 않아서 무슨 원리인지 알아보았는데
lambda x의 x는 매개변수이고 sorted부터 표현식인데 commands에서 요소를 뽑아 sorted를 하고 바로 list로 리턴하는 방식이다.
얼른 더 배워서 가독성 좋은 코드를 짜고싶어졌다.
"""
