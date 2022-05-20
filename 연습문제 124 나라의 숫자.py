# 문제 설명
# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
# 예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

# 10진법	124 나라	10진법	    124 나라
# 1	        1	        
# 2	        2	        
# 3	        4	        
# 4	        11	        
# 5	        12
# 6	        14
# 7	        21
# 8	        22
# 9	        24
# 10	    41
# 11        42
# 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

# 제한사항
# n은 500,000,000이하의 자연수 입니다.
# 입출력 예
# n	    result
# 1	    1
# 2	    2
# 3	    4
# 4	    11

def test():
    assert solution2(1) == 1	        
    assert solution2(2) == 2	        
    assert solution2(3) == 4	        
    assert solution2(4) == 11	        
    assert solution2(5) == 12
    assert solution2(6) == 14
    assert solution2(7) == 21
    assert solution2(8) == 22
    assert solution2(9) == 24
    assert solution2(10) == 41	        


def solution(n: int) -> int:
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return int(answer)

from collections import deque as dq
def solution2(n :int) -> int:
    num_list   = ['1', '2', '4']
    bfs = dq([(i,v) for i,v in enumerate(num_list)])
    m = bfs[-1][0]
    while True:
        pop_i, pop_num = bfs.popleft()
        if pop_i+1 == n:
            return int(pop_num)

        for num in num_list:
            new_num = pop_num + num
            m += 1
            if m+1 == n:
                return int(new_num)
            bfs.append((m,new_num))


test()
# for i in range(40):
#     print(f"{i = }")
#     print(f"{i} - > ", end='')
#     while i > 0:
#         q, r = divmod(i,3)
#         print(f"{(q)} - > ", end='')
#         i = q
#     print('\n')


# 124나라	십진법      i
# 1       1 = 3*0 + 1   0 = 3*0 + 0 
# 2       2 = 3*0 + 2   1 = 3*0 + 1
# 4       3 = 3*1 + 0   2 = 3*0 + 2

# 11      4 = 3*1 + 1   3 = 3*1 + 0
# 12      5 = 3*1 + 2   4 = 3*1 + 1
# 14      6 = 3*2 + 0   5 = 3*1 + 2

# 21      7 = 3*2 + 1   6 = 3*2 + 0
# 22      8 = 3*2 + 2   7 = 3*2 + 1
# 24      9 = 3*3 + 0   8 = 3*2 + 2

# 41      10 = 3*3 + 1  9 = 3*3 + 0
# 42      11 = 3*3 + 2  10 = 3*3 + 1
# 44      12 = 3*4 + 0  11 = 3*3 + 2

# 111     13 = 3*4 + 1  12 = 3*4 + 0
# 112     14 = 3*4 + 2  13 = 3*4 + 1
# 114     15 = 3*5 + 0  14 = 3*4 + 2

# 121     16 = 3*5 + 1
# 122     17 = 3*5 + 2
# 124     18 = 3*6 + 0

# 141     19 = 3*6 + 1
# 142     20 = 3*6 + 2
# 144     21 = 3*7 + 0

# 211     22 = 3*7 + 1
# 212     23 = 3*7 + 2
# 214     24 = 3*8 + 0

# 221     25 = 3*8 + 1
# 222     26 = 3*8 + 2
# 224     27 = 3*9 + 0

# 241     28 = 3*9 + 1
# 242     29 = 3*9 + 2
# 244     30 = 3*10 + 0

# 411     31 = 3*10 + 1
# 412     32 = 3*10 + 2
# 414     33 = 3*11 + 0

# 421     34 = 3*11 + 1
# 422     35 = 3*11 + 2
# 424     36 = 3*12 + 0

# 441     37 = 3*12 + 1
# 442     38 = 3*12 + 2
# 444     39 = 3*13 + 0

# 1111    40 = 3*13 + 1







# 124나라   i    십진법
# 1         0    1 = 3*0 + 1
# 2         1    2 = 3*0 + 2
# 4         2    3 = 3*1 + 0

# 11        3    4 = 3*1 + 1
# 12        4    5 = 3*1 + 2
# 14        5    6 = 3*2 + 0
# 21        6    7 = 3*2 + 1
# 22        7    8 = 3*2 + 2
# 24        8    9 = 3*3 + 0
# 41        9    10 = 3*3 + 1
# 42        10   11 = 3*3 + 2
# 44        11   12 = 3*4 + 0
# 111       12   13 = 3*4 + 1
# 112       13   14 = 3*4 + 2
# 114       14    15 = 3*5 + 0
# 121           16 = 3*5 + 1
# 122           17 = 3*5 + 2
# 124           18 = 3*6 + 0
# 141           19 = 3*6 + 1
# 142           20 = 3*6 + 2
# 144           21 = 3*7 + 0
# 211           22 = 3*7 + 1
# 212           23 = 3*7 + 2
# 214           24 = 3*8 + 0
# 221           25 = 3*8 + 1
# 222           26 = 3*8 + 2
# 224           27 = 3*9 + 0
# 241           28 = 3*9 + 1
# 242           29 = 3*9 + 2
# 244           30 = 3*10 + 0
# 411           31 = 3*10 + 1
# 412           32 = 3*10 + 2
# 414           33 = 3*11 + 0
# 421           34 = 3*11 + 1
# 422           35 = 3*11 + 2
# 424           36 = 3*12 + 0
# 441           37 = 3*12 + 1
# 442           38 = 3*12 + 2
# 444           39 = 3*13 + 0
# 1111          40 = 3*13 + 1




