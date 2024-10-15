def login(password):
    # 登录函数
    if password == "15ruike":
        return None
    else:
        print("你不是丁真，你是谁")
        exit(0)

def menu():
    # 主菜单函数
    print("----------主菜单----------")
    print("丁真，您好，欢迎来到理塘ATM")
    print("查询余额\t[输入 1]")
    print("存款\t\t[输入 2]")
    print("取款\t\t[输入 3]")
    print("退出\t\t[输入 4]")
    print("丁真，您好，欢迎来到理塘ATM")
    num_input = input("请输入您的选择：")
    return num_input

def balance_info():
    # 账户余额
    balance = 50000000
    return balance

def check_balance():
    # 查询账户余额
    check_num = balance_info()
    print("---------查询余额---------")
    print(f"丁真，您好，您的余额还有：{check_num}")
    input()

def add_balance(add_num):
    # 存款
    current_num = balance_info()
    print("---------存款---------")
    print(f"丁真，您好，您存款{add_num}成功")
    print(f"丁真，您好，您的余额还有：{current_num + int (add_num)}")
    input()

def take_balance(take_num):
    # 取款
    current_num = balance_info()
    print("---------存款---------")
    print(f"丁真，您好，您取款{take_num}成功")
    print(f"丁真，您好，您的余额还有：{current_num - int (take_num)}")
    input()

def main():
    # 来自理塘的ATM机！实现丁真电子烟梦想的ATM机！
    
    # 登录
    login_num = input("丁真，您好，请输入您的账户密码：")
    login(login_num)
    num = None
    if num == 1:
        exit(0)
    # 循环实现功能
    while num == None:
        action_num = menu()
        if action_num == '1':
            check_balance()
        elif action_num == '2':
            add_balance(input("请输入要存款的数目："))
        elif action_num == '3':
            take_balance(input("请输入要取款的数目："))
        elif action_num == '4':
            num = 1 

if __name__ == '__main__':
    main()