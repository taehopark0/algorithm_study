# kakao 시험
# s는 words와 숫자의 혼합
# 숫자	영단어
# 0: zero 1:one 2:two 3:three 4:four 5: five 6:six 7:seven 8:eight 9:nine
#  s	                result
# "one4seveneight"	    1478
# "23four5six7"	        234567
# "2three45sixseven"	234567
# "123"	                123
# * three"는 3, "six"는 6, "seven"은 7에 대응되기 때문에 정답은 입출력 예 #2와 같은 234567이 됩니다.
# * 입출력 예 #2와 #3과 같이 같은 정답을 가리키는 문자열이 여러 가지가 나올 수 있습니다.

import re
s= "one4seveneight"
result = 1478
list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def solution(s):

    for k,lst in enumerate(list):
        s = re.sub(lst,str(k),s)
    return s
print(solution(s))