def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer

    """
    def solution(s):
    result=[]
    app=[]
    num=0
    for i in range(len(s)):
        if len(app)==0:
            if s[i].isalpha():
                app.append(s[i].upper())
            elif s[i]==" ":
                num+=1
            else:
                app.append(s[i])
        elif len(app)==num and s[i]!=" ":
            for i in range(num):
                app.append(" ")
            num=0
            app.append(s[i].upper())
        else:
            if s[i]==" ":
                app.append(" ")
                result.extend(app)
                app.clear()
            else:
                app.append(s[i].lower())                   
    result.extend(app)    
    return ''.join(result)

    마지막까지 푼 풀이이다. 중복 공백 case 한가지가 풀리지 않아 몇시간동안 전전긍긍해서 정답 코드를 봤더니 capitalize 내장함수를 사용하면 매우 간단히 풀 수 있는 문제였다.
    내장함수에 대해서도 공부가 필요하다고 느꼈다.
    """