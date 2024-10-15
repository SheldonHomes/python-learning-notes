"""
数据输入：input语句（函数）
  与print语句相对的语句，用于用户输入数据
  使用方法：
  ① 使用input(提示信息)语句获取键盘输入
  ② 使用一个变量接收（存储）输入的数据

  注：通过input函数输入的数据全部属于字符串数据，其他数据需要用数据转换后使用

"""


do = True
while do or game == "原神":
  # 利用input语句获取输入，用game变量接收
  game = input("你喜欢玩什么游戏？")
  if game == "原神":
    print("不是哥们你真喜欢玩原神啊？")
    break
  else:
    print("世界上怎么会有人不喜欢玩原神？再给你一次机会")


recharge = input("你要给原神充多少钱？")
# recharge中存储的数据为字符串，需要数据转换后使用
if int(recharge) < 648:
  print("充这么少？你玩牛魔的原神")
else:
  print("诶你真充啊？真是mhy纯种汗血大龟龟")
