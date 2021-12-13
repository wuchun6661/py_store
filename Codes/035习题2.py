import easygui as g

msg = '请输入一下个人信息'
title = '个人信息'
field_names = [' *姓名',' 年龄',' *身高',' 体重']
field_values = []
field_values = g.multenterbox(msg,title,field_names)

while 1:
    if field_values == None:
        break
    errmsg = ''
    for i in range(len(field_names)):
        option = field_names[i].strip()
        if field_values[i].strip()=='' and option[0]=='*':
            errmsg += ('【%s】为必填项\n\n' % field_names[i])
    if errmsg == '':
        break
    field_values = g.multenterbox(errmsg,title,field_names,field_values)
    
print('用户的资料如下：%s' % str(field_values))
        
