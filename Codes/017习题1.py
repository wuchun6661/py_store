def power(x,y):
    result = x ** y
    return result

def gcd(x,y):
    while y:
        t = x % y
        x = y
        y = t
    return x
def Dec2Bin(dec):
    temp = []
    result = ''
    while dec:
        yushu = dec % 2
        dec = dec // 2
        temp.append(yushu)
    while temp:
        result += str(temp.pop())
    return result
