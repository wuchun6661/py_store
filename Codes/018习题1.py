def sum2(*num,base = 3):
    "功能：求和 * 基数"
    result = 0
    for a in num:
        result += a
    return result * base

def findStr(desStr,subStr):
    "查双字符在字符串中出现次数"
    count = 0
    length = len(desStr)
    if subStr not in desStr:
        print('未找到',subStr,'字符串!')
    else:
        for each in range(length-1):
            if desStr[each]==subStr[0] and desStr[each+1]==subStr[1]:
                count +=1
        print(subStr,'在字符串中出现了',count,'次')
            
