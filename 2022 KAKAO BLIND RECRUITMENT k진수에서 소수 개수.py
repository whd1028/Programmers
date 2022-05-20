# 문제 설명
# 양의 정수 n이 주어집니다. 
# 이 숫자를 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.

# 0P0처럼 소수 양쪽에 0이 있는 경우
# P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# P처럼 소수 양쪽에 아무것도 없는 경우
# 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
# 예를 들어, 101은 P가 될 수 없습니다.
# 예를 들어, 437674을 3진수로 바꾸면 211020101011입니다. 
# 여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 총 3개입니다. 
# (211, 2, 11을 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다는 점에 주의합니다.) 
# 211은 P0 형태에서 찾을 수 있으며, 2는 0P0에서, 11은 0P에서 찾을 수 있습니다.

# 정수 n과 k가 매개변수로 주어집니다. 
# n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return 하도록 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ n ≤ 1,000,000
# 3 ≤ k ≤ 10

# 입출력 예
# n	        k	    result
# 437674	3	    3
# 110011	10	    2

# 입출력 예 설명
# 입출력 예 #1
# 문제 예시와 같습니다.

# 입출력 예 #2
# 110011을 10진수로 바꾸면 110011입니다. 여기서 찾을 수 있는 조건에 맞는 소수는 11, 11 2개입니다. 
# 이와 같이, 중복되는 소수를 발견하더라도 모두 따로 세어야 합니다.

# 제한시간 안내
# 정확성 테스트 : 10초


def test():
    assert solution3(437674, 3) == 3  
    assert solution3(110011, 10) == 2  

def solution1(n, k):
    answer = 0
    num = ""
    while n:
        n, r = divmod(n,k)
        num = str(r) + num
    num_list = [i for i in map(int,num.replace('0',' ').split()) if i != 1 ]
    prime_num = find_prime_num(max(num_list))
    for i in num_list:
        if i in prime_num:
            answer += 1
    return answer
# 채점 결과
# 정확성: 86.9
# 합계: 86.9 / 100.0

def find_prime_num(m):
    num_list = set(range(2,m+1))
    prime_num = []
    while num_list:
        i = num_list.pop()
        num_list-=set(range(2*i,m+1,i))
        prime_num.append(i)
    return prime_num

def solution2(n, k):
    answer = 0
    num = ""
    while n:
        n, r = divmod(n,k)
        num = str(r) + num
    zero_check = True
    start = 0
    for i in range(len(num)):
        if num[i] == '0' and zero_check:
            if is_prime_number(int(num[start:i])):
                answer += 1
            zero_check = False
        elif num[i] != '0' and not(zero_check):
            start = i
            zero_check = True

    return answer
            
import math
def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution3(n,k):
    answer = 0
    num = ""
    while n:
        n, r = divmod(n,k)
        num = str(r) + num
    num_list = [i for i in map(int,num.replace('0',' ').split()) if i != 1 ]
    for i in num_list:
        if is_prime_number(i):
            answer += 1

    return answer

test()