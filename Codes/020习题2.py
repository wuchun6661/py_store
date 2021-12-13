str1 = '''ABSaDKSbRIHcRHGcdDIF'''
str2 = ''
countA = 0
countB = 0
countC = 0
length = len(str1)

for i in range(3,length-3):
    if str1[i] == '\n':
        continue
    if str1[i].islower():
        if (str1[i-3].isupper() and str1[i-2].isupper() and str1[i-1].isupper()
            and str1[i+1].isupper() and str1[i+2].isupper() and str1[i+3].isupper()):
            str2 += str1[i]

print(str2)        
        
