def hnt(n,x,y,z):
    if n ==1:
        print(x,'-->',z)
    else:
        hnt(n-1,x,z,y)       #将n-1个挪到y柱子
        print(x,'-->',z)     #将最后一个移动到z柱子
        hnt(n-1,y,x,z)       #将y上的移动到z柱子
while 1:
    n = int(input('输入汉诺塔的层数：'))
    hnt(n,'X','Y','Z')

