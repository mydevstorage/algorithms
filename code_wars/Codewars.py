row1 = ' AAA  BBBB   CCC  DDDD  EEEEE FFFFF  GGG  H   H IIIII JJJJJ K   K L     M   M N   N  OOO  PPPP   QQQ  RRRR   SSS  TTTTT U   U V   V W   W X   X Y   Y ZZZZZ      '
row2 = 'A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     MM MM NN  N O   O P   P Q   Q R   R S   S   T   U   U V   V W   W X   X Y   Y     Z      '
row3 = 'A   A B   B C     D   D E     F     G     H   H   I       J K K   L     M M M N   N O   O P   P Q   Q R   R S       T   U   U V   V W   W  X X   Y Y     Z       '
row4 = 'AAAAA BBBB  C     D   D EEEEE FFFFF G GGG HHHHH   I       J KK    L     M   M N N N O   O PPPP  Q   Q RRRR   SSS    T   U   U V   V W W W   X     Y     Z        '
row5 = 'A   A B   B C     D   D E     F     G   G H   H   I       J K K   L     M   M N   N O   O P     Q Q Q R R       S   T   U   U V   V W W W  X X    Y    Z         '
row6 = 'A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     M   M N  NN O   O P     Q  QQ R  R  S   S   T   U   U  V V  W W W X   X   Y   Z          '
row7 = 'A   A BBBB   CCC  DDDD  EEEEE F      GGG  H   H IIIII JJJJ  K   K LLLLL M   M N   N  OOO  P      QQQQ R   R  SSS    T    UUU    V    W W  X   X   Y   ZZZZZ      '
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
r1, r2, r3, r4, r5, r6, r7 = [], [], [], [], [], [], []
ROW = {row1: r1, row2: r2, row3: r3, row4: r4, row5: r5, row6: r6, row7: r7}
new = []
for z, k in ROW.items():
    a = 0
    for i in range(0, len(row1)):
        if i % 6 == 0:
            k.append(z[i:i + 5])
    z = dict(zip(alpha, k))
    new.append(z)
r1, r2, r3, r4, r5, r6, r7 = new[0], new[1], new[2], new[3], new[4], new[5], new[6]
result = [r1, r2, r3, r4, r5, r6, r7]


def block_print(string):

    last = ''
    if string.strip() == '':
        return last
    tmp = string.strip().lower()
    for a in result:
        for i in range(len(tmp)):
            if i == len(tmp) - 1:
                last += a[tmp[i]]
            else:
                last += a[tmp[i]] + ' '
        if a == result[-1]:
            last += ''
        else:
            last += '!!'
    return last


print(block_print('heLLo WorLD'))

