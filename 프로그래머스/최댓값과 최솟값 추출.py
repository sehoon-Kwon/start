def solution(s):
    srt=list(map(int,s.split()))

    return str(min(srt)) + " " + str(max(srt))

    #공백으로 되어있는 숫자를 입력받아 최댓값과 최솟값을 추출