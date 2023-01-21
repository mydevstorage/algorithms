def only_oddDigPrimes(n):
    a, b, k = range(3, n + int(n * 0.6), 2), [], []
    for i in a:
        if [e for e in str(i) if int(e) % 2 == 0]:
            continue
        elif not len([q for q in range(2, int(i**0.5)+1) if i % q == 0]):
            b.append(i)
        else:
            continue
    for i in range(len(b)):
        if b[i] <= n:
            k.append(b[i])
        elif b[i] > n:
            p = b[i]
            break
    c = len(k)
    g = k[-1] if n != k[-1] else k[-2]
    print([c, g, p])


only_oddDigPrimes(100)
