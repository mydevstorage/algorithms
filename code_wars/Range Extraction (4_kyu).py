def solution(args):
    result = ''
    tmp = []
    for i in args:
        if not tmp or i - tmp[-1] == 1:
            tmp.append(i)
        else:
            if len(tmp) == 2:
                result += f'{tmp[0]},{tmp[-1]},'
                tmp = []
                tmp.append(i)
            else:
                result += f'{tmp[0]}-{tmp[-1]},' if tmp[0] != tmp[-1] else f'{tmp[0]},'
                tmp = []
                tmp.append(i)
    if len(tmp) == 2:
        result += f'{tmp[0]},{tmp[-1]},'

    else:
        result += f'{tmp[0]}-{tmp[-1]},' if tmp[0] != tmp[-1] else f'{tmp[0]},'

    return result


# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14,
#          15, 17, 18, 19, 20])  # , '-6,-3-1,3-5,7-11,14,15,17-20'
solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20])  # , '-3--1,2,10,15,16,18-20'
