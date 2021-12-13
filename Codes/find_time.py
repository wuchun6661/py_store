import time as t

#now_time = t.localtime()

now_time = t.strftime("%Y年%m月%d日%H:%M:%S",t.localtime())

result_time = "最后修改日期：" + now_time + "\n"

with open("Now_time.txt",'w') as f:
    f.write(result_time)
print(result_time)
