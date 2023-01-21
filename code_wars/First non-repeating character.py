def first_non_repeating_letter(string):
    a = string.lower()
    for i in a:
        if a.count(i) == 1:
            b = a.index(i)
            c = string[b:b+1]
            return c if c else ''
    return ''
