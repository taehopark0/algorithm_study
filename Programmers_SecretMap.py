
#지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
#전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다.
# 각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다.
# 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
#"지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
#암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.
# https://programmers.co.kr/learn/courses/30/lessons/17681

n = 5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    new_list = list()

    for i in range(n):
        arr1[i] = bin(arr1[i]).replace("b","")
        arr2[i] = bin(arr2[i]).replace("b","")
        new_list.append(int(arr1[i])+int(arr2[i]))

    for j in range(len(new_list)):
        new_list[j] = str(new_list[j])
        new_list[j] = new_list[j].zfill(n).replace("1","#").replace("2","#").replace('0',' ')

    return new_list

print(solution(n,arr1,arr2))
