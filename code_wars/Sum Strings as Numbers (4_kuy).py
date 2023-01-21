''' Первая версия не достаточно быстра
    Хорошие примеры zfill, zip, zip_longest. Сложная но хорошая практика'''

'''Использоватние zip_longest умеет дополнять недостающие элементы при разного размера списках'''




from itertools import zip_longest
def sum_strings(x, y):
    out, ret = '', 0

    for c_x, c_y in zip(x.zfill(len(y))[::-1], y.zfill(len(x))[::-1]):
        ret, d = divmod(int(c_x) + int(c_y) + ret, 10)
        out += str(d)

    out = f"{out}{'1' * ret}"[::-1] or '0'
    return out if len(out) < 2 else out.lstrip('0')

####################################################################


def sum_strings(x, y):
    res = ""
    carry = 0
    z = zip_longest(x[::-1], y[::-1], fillvalue="0")
    for e in [int(a)+int(b) for a, b, in z]:
        d, m = divmod(e+carry, 10)
        res += str(m)
        carry = d
    return ("1"*carry + res[::-1]).lstrip("0") or "0"


print(sum_strings("123", "456"))  # 579
