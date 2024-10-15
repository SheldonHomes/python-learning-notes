"""
要求:
定义如下变量:
    name 变量
    stock_price 股价
    stock_code 股票代码
    stock_price_daily_growth_factor 股票每日增长系数
    growth_days 增长天数
计算经过growth_days天的增长后,股价达到了多少钱
使用字符串格式化输出,浮点数要求精确到小数点后2位
示例:
    公司:益盛药业 股票代码:003032 当前股价:19.99
    每日增长系数:1.2 7天增长后股价为:71.63
第一行用f快速格式化输出,第二行用正常格式化输出

"""

# 定义股票的名字、股价、代码
name = "益盛药业"
stock_price = 19.99
stock_code = "003032"

# 定义股票增长系数与天数
stock_price_daily_growth_factor = 1.2
growth_days = 7

# 输出示例
print(f"公司:{name} 股票代码:{stock_code} 当前股价:{str(stock_price)}")
print("每日增长系数:%.1f %d天增长后股价为:%.2f" % (stock_price_daily_growth_factor, growth_days, (stock_price_daily_growth_factor**growth_days)*stock_price))
