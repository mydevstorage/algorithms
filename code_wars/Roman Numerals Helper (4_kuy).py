base = {
    1: 'I', 20: 'XX', 200: 'CC', 0: '',
    2: 'II', 30: 'XXX', 300: 'CCC',
    3: 'III', 40: 'XL', 400: 'CD',
    4: 'IV', 50: 'L', 500: 'D',
    5: 'V', 60: 'LX', 600: 'DC',
    6: 'VI', 70: 'LXX', 700: 'DCC',
    7: 'VII', 80: 'LXXX', 800: 'DCCC',
    8: 'VIII', 90: 'XC', 900: 'CM',
    9: 'IX', 100: 'C', 1000: 'M',
    10: 'X', 2000: 'MM', 3000: 'MMM',
}
br = {value: key for key, value in base.items()}
a = dict(sorted(br.items(), key=lambda x: x[1], reverse=True))


class RomanNumerals:

    def to_roman(val):
        ed = val % 10
        dec = val % 100 // 10 * 10
        sot = val % 1000 // 100 * 100
        ts = val % 10000 // 1000 * 1000
        res = base[ts] + base[sot] + base[dec] + base[ed]
        print(res)

    def from_roman(roman_num):
        sum = 0
        i = len(roman_num)
        while len(roman_num):
            if a.get(roman_num[:i]):
                sum += a[roman_num[:i]]
                roman_num = roman_num[i:]
                i = len(roman_num)
                continue
            i -= 1
        return sum


# RomanNumerals.to_roman(1000)  # , 'M', '1000 should == "M"'
# RomanNumerals.to_roman(4)  # , 'IV', '4 should == "IV"'
# RomanNumerals.to_roman(1)  # , 'I', '1 should == "I"'
# RomanNumerals.to_roman(1990)  # , 'MCMXC', '1990 should == "MCMXC"'
# RomanNumerals.to_roman(2008)  # , 'MMVIII', '2008 should == "MMVIII"'
RomanNumerals.from_roman('XXI')  # , 21, 'XXI should == 21'
RomanNumerals.from_roman('I')  # , 1, 'I should == 1'
RomanNumerals.from_roman('IV')  # , 4, 'IV should == 4'
RomanNumerals.from_roman('MMVIII')  # , 2008, 'MMVIII should == 2008'
RomanNumerals.from_roman('MDCLXVI')  # , 1666, 'MDCLXVI should == 1666'
