def solution(citations):
    citations.sort()
    article_count = len(citations)

    for i in range(article_count):
        if citations[i] >= article_count-i:
            return article_count-i
    return 0

"""배열 n개중에서 h이상인게 h개 이상인 h의 최댓값을 구하는 문제이다.
처음에는 배열 중간을 자르고 그 이후에 값을 비교해서 return하는 방식으로 구상했는데
테스트케이스는 맞았지만 제출하니 반절은 시간이 너무 오래걸렸다.
그래서 찾아보니 큰수부터 비교해서 조건에 만족하면 바로 출력하는 형식으로 시간복잡도를 신경쓴 코드이다.
"""

"""
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

다른 사례의 코드이다. 도대체  무슨 원리인지 궁금해서 분석해보니 sort로 내림차순 정렬후 enumerate(리스트,1부터) 묶은 후에 min(인덱스,숫자)로 h를 구했다. 그 중에서 가장 큰 값을 구해 답을 도출하는 방식이다.
정말 생각하는거에 따라 코드가 clean code로 바뀌는게 신기하다. 열심히 공부해서 좀 더 가독성 좋고 효율적인 코드를 짜고싶다.
"""
