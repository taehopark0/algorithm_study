# 크레인 인형 뽑기

import numpy as np

def solution(board, moves):
    answer = 0
    new_list = list()
    board1 = np.transpose(board)
    for k, move in enumerate(moves):
        for i in range(len(board1)):
            if board1[move - 1][i] != 0:
                new_list.append(board1[move - 1][i])
                board1[move - 1][i] = 0
                if len(new_list) > 1:
                    if new_list[-1] == new_list[-2]:
                        answer += 2
                        new_list.pop(-1)
                        new_list.pop(-1)
                break
#루프가 도는 중간에도 break가 있으면 아래 코드로 가지 못함
#enumerate를 통해 index와 값을 한번에 정할 수 있다.

    return answer