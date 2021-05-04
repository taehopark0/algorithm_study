#https://programmers.co.kr/learn/courses/30/lessons/42862#qna

# n	lost	reserve	 return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]     	4
# 3	[3]	    [1]	        2

def solution(n,lost,reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    arr = list(range(n+1))
    arr.pop(0)
    rest = [x for x in arr if (x not in lost) and (x not in reserve)]
    sparse = [x for x in reserve if x not in lost]
    rest = list(set(rest+sparse))
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            rest.append(lost[i])
        elif lost[i]-1 in reserve:
            rest.append(lost[i])
            reserve.remove(lost[i]-1)
        elif lost[i]-1 not in reserve and lost[i]+1 in reserve:
            rest.append(lost[i])
            reserve.remove(lost[i]+1)
    rest = list(set(rest))
    return len(rest)
print(solution(n,lost,reserve))
