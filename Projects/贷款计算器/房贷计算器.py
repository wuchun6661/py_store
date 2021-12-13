import easygui as e
import sys
#引入easyui和sys两个基本库
#easygui用于显示交互对话框
#sys用于调用当前操作操作系统相关指令（例如本代码中用到了sys.exit()结束进程的功能）

def Calculate_loan_dengjin(num,month,rate_year):  #等额本金的计算函数
    rate = rate_year/12
    bj_left = num
    result = "期数\t月供\t偿还本金\t\t偿还利息\t\t剩余本金\n"
    sum_loan = 0
    
    for i in range(1,month+1):                             #i为当前期数
        yg = num/month + (num - (num/month)*(i-1))*rate    #yg为月供
        bj_return = num/month                              #bj_return为本期应还本金
        loan = (num - (num/month)*(i-1))*rate              #loan为当期利息
        bj_left = bj_left - bj_return                      #bj_left为剩余本金
        sum_loan += loan
        
        result += "第%d期\t%d\t%d\t\t%d\t\t%d\n"%(i,yg,bj_return,loan,bj_left)
    result += "\n贷款总额：%d\n\n利息总和：%d\n\n还款总额：%d"%(num,sum_loan,num+sum_loan) 

    flag = e.buttonbox(result,choices=('重新计算','另存为','结束'))
    return [flag,result]

def Calculate_loan_dengxi(num,month,rate_year):  #等额本息的计算函数
    rate = rate_year/12
    bj_left = num
    yg = (  num*rate*pow((1+rate),month) )  /  ( pow((1+rate),month)-1 )
    bj_return = 0

    result = "期数\t月供\t偿还本金\t\t偿还利息\t\t剩余本金\n"
    sum_loan = 0
    
    for i in range (1,month+1):
        loan = bj_left*rate
        bj_return = yg - loan
        bj_left = bj_left - bj_return
        sum_loan += loan
        
        result += "第%d期\t%d\t%d\t\t%d\t\t%d\n"%(i,yg,bj_return,loan,bj_left)
    result += "\n贷款总额：%d\n\n利息总和：%d\n\n还款总额：%d"%(num,sum_loan,num+sum_loan)     

    flag = e.buttonbox(result,choices=('重新计算','另存为','结束'))
    return [flag,result]


def loan_main():     #主函数
        
    start_flag = e.buttonbox('欢迎使用房贷计算器\n\n版本号：1.6.3\n\n作者：杨令飞', choices=('结束', '开始'))
    if start_flag == '结束' or start_flag == None:
        sys.exit(0)
    
    while 1:
        msg = '请输入贷款信息和选择贷款方式\n\n' + '贷款期限每期为一个月\n\n' + '贷款时间为x年+y月\n\n' + '等额本金输入1，等额本息输入2'
        title = '房贷计算器' 
        field_names = ['贷款金额（万）','贷款期间（年）','贷款期限（月）','贷款年利率(%)','贷款方式']
        field_values = []
        field_values = e.multenterbox(msg,title,field_names)
        
        if field_values == None:
            sys.exit(0)
            
       

        year = int(0)
        month = int(0)
        num = int(field_values[0]) * 10000
        if field_values[1] != '':
            year = int(field_values[1])
        if field_values[2] != '':
            month = int(field_values[2])
    
        month = year*12+month
        rate_year = float(field_values[3]) * 0.01
            
        if field_values[4] == '1':
            flag_main = Calculate_loan_dengjin(num,month,rate_year)
            
        if field_values[4] == '2':
            flag_main = Calculate_loan_dengxi(num,month,rate_year)

        if flag_main[0] == '结束':
            break

        if flag_main[0] == '另存为':
            file_name = e.filesavebox(msg=None, title=None, default='房贷还款信息.txt', filetypes=["*.txt"])
            with open(file_name,'w') as f:
                f.write(flag_main[1])
            flag_last = e.buttonbox('文件保存成功！\n\n保存路径为:%s'%file_name,choices=('继续计算','结束'))
            if flag_last == '结束':
                sys.exit(0)


                
loan_main()         #调用主函数

