from math import log

def to_base(num, toBase=2, fromBase=10):
    '''
    to_base() is a function that converts any number (num) in any base
    fromBase (set to 10 by default)) to any base (toBase) that by default is
    equal to 2 (binary).
    '''
    num = int(str(num), fromBase)
    out = ''
    max = int(log(num, toBase)) 
    for i in reversed(range(max+1)):
        digit = num//(toBase**i)
        out += str(digit if digit < 10 else chr(digit + 87))
        num %= toBase**i
    return out




