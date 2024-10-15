"""
序列切片：
序列名[起始下标:终止下标:步长]
    起始下标表示从何处开始，包含
    终止下标表示到何处结束，不包含
    步长N表示间隔N-1个取一个

"""

"""
The supply of game for London is going steadily up (itran). Headkeeper Hudson, We believe, has been now told to reeive all orders for fly paper and for preservation of your hen pheasant's life.
"""

def slider(list: list) -> list:
    new_list = list[0::3]
    return new_list

def split(string: str) -> list:
    list = string.split(" ")
    for index in range(len(list)):
        list[index] = list[index].strip(",")
        list[index] = list[index].strip(".")
    return list

def regenerator(list: list):
    print("福尔摩斯解密后的密文是：")
    for index in list:
        print(f"{index} ", end='')

def main():
    text = input("请输入福尔摩斯的密文：")
    text_list = split(text)
    new_list = slider(text_list)
    regenerator(new_list)

if __name__ == '__main__':
    main()
