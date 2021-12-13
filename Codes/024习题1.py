def Dec_Bin(dec):
    result = ''

    if dec:
        result = Dec_Bin(dec//2)
        return result + str(dec%2)
    else:
        return result
while 1:
    n = int(input('输入十进制：'))
    print('对应二进制为：',Dec_Bin(n))
