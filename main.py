"""
    简单端口扫描程序
    主程序
"""
def menu():
   print('''
    ----菜单
    
    --------1. TCP_CONN扫描
    --------2. TCP_SYN扫描
    --------3. TCP_FIN扫描
    --------4. UDP扫描
    --------5. 显示菜单
    --------6. 退出
    ''')

def main():
    targetIP=input("请输入目标IP：")
    a=int(input("请输入扫描起始端口："))
    b=int(input("请输入扫描终止端口："))
    portslist=(list(range(a,b)))
    menu()
    while True:
        try:
            options=int(input("请输入扫描方式："))
        except:
            continue
        if options==1:
           from TCP_CONN import conn_scanner
           conn_scanner(targetIP,portslist) 
        elif options==2:
           from TCP_SYN import syn_scanner
           syn_scanner(targetIP,portslist)
        elif options==3:
           from TCP_FIN import fin_scanner
           fin_scanner(targetIP,portslist)
        elif options==4:
           from UDP import udp_scanner
           udp_scanner(targetIP,portslist)
        elif options==5:
            menu()
        elif options==6:
            break
        else:
            continue
     
main()

