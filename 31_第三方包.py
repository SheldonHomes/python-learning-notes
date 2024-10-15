"""
在Python程序的生态中，有各种各样的第三方包，这些包由社区中的个人和团队开发，提供了各种各样的功能，极大地丰富了Python生态。

一些常用的第三方包如下：
    矩阵计算常用包：Numpy
    数据分析常用包：Pandas
    大数据计算常用包：Pyspark、apache-flink
    图形可视化常用包：Matplotlib、Pyecharts
    机器学习常用包：Tensorflow、Pytorch、Scikit-learn
    网络爬虫常用包：Scrapy、Requests
    数据库连接常用包：PyMySQL、SQLAlchemy
    网络编程常用包：Flask、Django
由于第三方包是由社区中的个人和团队开发，因此它们通常需要通过pip命令进行安装。

安装第三方包的步骤：
    1. 打开命令行工具
        注：在vscode中，可以使用快捷键Ctrl+`打开终端
        如果项目是在虚拟环境中，需要先激活虚拟环境，再打开终端
    2. 输入pip install 包名
        例如：pip install numpy
        注：如果需要安装指定版本的包，可以在包名后面加上==版本号，例如：pip install numpy==1.21.2
        如果项目是在虚拟环境中运行，需要指定虚拟环境的pip，例如：.venv\Scripts\pip install numpy
    3. 等待安装完成
    4. 在Python程序中导入第三方包
        例如：import numpy as np
"""

import numpy as np

# 使用第三方包
arr = np.array([1, 2, 3, 4, 5])
print(arr)