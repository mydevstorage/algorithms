from time import *

# def hamming(n):

    # len_l = 1
    # num = 2

    # def ishamnum(num):
    #     while num % 5 == 0:
    #         num /= 5
    #     while num % 3 == 0:
    #         num /= 3
    #     while num % 2 == 0:
    #         num /= 2
    #     return num == 1

    # while len_l < n:
    #     if ishamnum(num):
    #         len_l += 1
    #     num += 1
    # return num - 1


# def hamming(n):

#     def ishamnum(num):
#         while num % 5 == 0:
#             num /= 5
#         while num % 3 == 0:
#             num /= 3
#         while num % 2 == 0:
#             num /= 2
#         return num == 1

#     h = [1]
#     i, j, k = 1, 1, 1
#     while len(h) < n:
#         x2 = 2 * i
#         x3 = 3 * j
#         x5 = 5 * k

#         result = min(x2, x3, x5)
#         if result not in h:
#             h.append(result)
#         if x2 == result:
#             i += 1
#             continue
#         if x3 == result:
#             j += 1
#             continue
#         if x5 == result:
#             k += 1
#     return h[-1]

def hamming(k):
    a = {1:1,}
    lenth = 2
    s = set(range(2, 6))
    for _ in range(k-1):
        n = min(s)
        s.remove(n)
        if n not in a:
            a[lenth] = n
            lenth += 1
        for i in range(2, 6):
            s.add(n * i)
    return a[k]


start = time()
print(hamming(50000))
print(time() - start)