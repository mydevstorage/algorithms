import re

def find_matched_by_pattern(pattern):
    a, b, c = pattern[0], pattern[1], pattern[2]
    def predicat(text):
        if a == b == c: 
            temp = f'{a}\w*{b}\w*{c}'
        elif a != b == c: 
            temp = f'\\b[^{b}]{a}\w*{b}\w*{c}\w*\\b'
        elif a == b != c: 
            temp = f'\\b[^{c}]{a}[^{c}]{b}\w*{c}\w*\\b'
        elif a != b != c: 
            temp = f'\\b[^{b}{c}]*{a}[^{c}]*{b}\w*{c}\w*\\b'
        elif a != c == b: 
            temp = f'\\b[^{c}]{a}\w*{b}\w*{c}\w*\\b'
        print(temp)
        return bool(re.findall(temp, text))
    return predicat
    


predicate = find_matched_by_pattern('vvl')
print(predicate('revival')) # True
