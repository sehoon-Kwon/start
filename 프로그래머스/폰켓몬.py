def solution(nums):
    answer=0
    
    Nlen=len(set(nums))
    result=int(len(nums)/2)
    
    if result<Nlen:
        answer=result
    else:
        answer=Nlen
    
    return answer


"""
nums에서 nums/2만큼 가져가도 좋은데 종류별로 1마리씩만 가져야하는데 가장 큰 숫자를 도출하는 문제이다.
어렵게 생각해서 for문을통해 count로 세고 max로 가장 큰값을 가져오려했는데 당연 효율성테스트에서 실패가 떳다.
그래서 단순히 set으로 중복을 제거한 숫자와 n/2만큼 나눈 숫자와 비교해서 큰값을 도출하면 되는 간단한 문제였다.
문제의 구조를 잘 파악하는게 중요할 것 같다.
""'
