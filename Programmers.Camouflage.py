clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    dic = dict()
    result=1
    for i in range(len(clothes)):
        key=clothes[i][1]
        value = clothes[i][0]
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] =[value]
    for key in dic.keys():
        result = result*(len(dic[key])+1)
    return result-1
print(solution(clothes))