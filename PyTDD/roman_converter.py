def roman_converter(num):
    if not isinstance(num, int):
        return None
    
    if num >= 4000 or num <= 0:
        return None
    ''''  
    ROMAN_VALUES = [
        (1000, 'M'),
        (500, 'D'),
        (100, 'C'),
        (50, 'L'),
        (10, 'X'),
        (5, 'V'),
        (1, 'I')
    ]
    
    out = ''
    for (value, symbol) in ROMAN_VALUES:
        while num >= value:
            out += symbol
            num -= value

    return out
