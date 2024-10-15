"""
账单处理：
    1. 读取账单文件
    2. 将文件写出到bill.txt.bak作为备份
    3. 将待支付的订单删除，只保留已支付的订单

"""

f1 = open("D:\\Python Projects\\PYLearning\\test\\test_bill.txt", "r", encoding="utf-8")
f2 = open("D:\\Python Projects\\PYLearning\\test\\test_bill.txt.bak", "w", encoding="utf-8")

for line in f1.readlines():
    if "待支付" not in line:
        f2.write(line)

f1.close()
f2.close()