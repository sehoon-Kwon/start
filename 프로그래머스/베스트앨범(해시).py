def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)): #enumerate와 zip로i에는 index를 g와 p에는 각각 generes와 plays로 만들었다. 
        if g not in dic1: # 만약 dic1에 generes가 존재하지않는다면 
            dic1[g] = [(i, p)] # dic1의 genres에 인덱스와 plays를 넣는다.
        else:
            dic1[g].append((i, p)) # 만약 존재한다면 g에 인덱스와 plays를 추가한다.

        if g not in dic2: #dic2에는 합을 넣는다. 만약 g가 dic2에 없다면
            dic2[g] = p # 그 값을 그대로 집어넣고
        else:
            dic2[g] += p #만약 이미 존재한다면 dic2의 g에 p 값을 추가한다.

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True): #dic2를 내림차순으로 정렬 (plays의 합이 큰값 먼저이므로)
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:#dic2에 내림차순한 k 기준으로 dic1을 내림차순으로 정렬해 최대 2개이므로 [:2]로 2개만 
            answer.append(i) # 인덱스를 출력해야하므로 i를 answer에 append시켜준다.

    return answer

    """
    generes와 plays가 주어지고 generes에 포함되는 plays의 합이 큰 generes가 먼저 그리고 그 중에 plays가 큰 값의 index부터 출력하는 문제이다.
    2가지의 딕셔너리를 동시에 관리해야했기 때문에 고민해본결과 아직 내 실력으론 부족한거 같아 다른 사람에 코드를 분석하기로 했다.
    각 코드마다 내가 찾아가면서 왜 이 코드를 썻는지 적어놓았다. enumerate와 zip으로 인덱스와 각 요소들을 묶어서 
    한 딕셔너리에는 값과 인덱스 한 딕셔너리에는 합을 넣어서 sorted(.items lambda)를 통해 정렬하면서 해시를 이용하는 코드를 보며 여러 기능의 코드를 볼 수 있었다.
    아직 한번에 풀기에는 부족한 실력이지만 이런 코드들을 보면서 내 실력으로 만들어야겠다고 생각했다.
    
            """