# def sumIntervals(intervals):
#     a = set()
#     for i in intervals:
#         b = range(i[0], i[1])
#         for q in b:
#             a.add(q)
#     print(len(a))


def sumIntervals(intervals):
    intervals.sort()
    mn = intervals[0][0]
    mx = intervals[0][1]
    x, y = 0, 0
    for i in intervals:
        if i[0] > mx:
            x += i[0] - mx
        if i[1] < mn:
            y += mn - i[1]
        if i[0] <= mn:
            mn = i[0]
        if i[1] >= mx:
            mx = i[1]
    print(mn, mx, x, y)
    print(mx - mn - x - y)


# sumIntervals([
#     [1, 5],
#     [10, 20],
#     [1, 6],
#     [16, 19],
#     [5, 11]
# ])  # 19
# sumIntervals([
#     [0, 20],
#     [-100000000, 10],
#     [30, 40]
# ])  # 100000030
sumIntervals([(1, 4), (3, 5)])  # 7
sumIntervals([(1, 5), (7, 10), (1, 5)])  # 7
