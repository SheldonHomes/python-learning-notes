"""
    升职加薪1：公司为了奖励大家，决定给每位员工涨工资，涨工资的条件如下：
    1. 工龄满5年，涨薪20%
    2. 工龄满3年，涨薪15%
    3. 工龄满1年，涨薪10%
    4. 工龄不满1年，涨薪5%

    员工表
    员工编号  姓名  工龄  工资
    1001    张三  6    10000
    1002    李四  2    8000
    1003    王五  4    12000
    1004    赵六  1    6000
    1005    孙七  0.5  9000

    升职加薪2：公司为了奖励大家，决定给每位员工涨工资，涨工资的条件如下：
    1. 级别为1，涨薪1000，级别+1
    2. 级别为2，涨薪800，级别+1
    3. 级别为3，涨薪600，级别+1
    4. 级别为4，涨薪400

    员工表
    员工编号  姓名  级别  工资
    1001    张三  1    5000
    1002    李四  2    6000
    1003    王五  3    8000
    1004    赵六  4    10000

"""

staff_statistics_1 = {
    '1001': {
        'name': '张三',
        'work_age': 6,
        'salary': 10000
    },
    '1002': {
        'name': '李四',
        'work_age': 2,
        'salary': 8000
    },
    '1003': {
        'name': '王五',
        'work_age': 4,
        'salary': 12000
    },
    '1004': {
        'name': '赵六',
        'work_age': 1,
        'salary': 6000
    },
    '1005': {
        'name': '孙七',
        'work_age': 0.5,
        'salary': 9000
    }
}

def raise_salary_1(staff_statistics):
    for id, staff_info in staff_statistics.items():
        if staff_info['work_age'] >= 5:
            staff_info['salary'] *= 1.2
        elif staff_info['work_age'] >= 3:
            staff_info['salary'] *= 1.15
        elif staff_info['work_age'] >= 1:
            staff_info['salary'] *= 1.1
        else:
            staff_info['salary'] *= 1.05
    return staff_statistics

staff_statistics_2 = {
    '1001': {
        'name': '张三',
        'level': 1,
        'salary': 5000
    },
    '1002': {
        'name': '李四',
        'level': 2,
        'salary': 6000
    },
    '1003': {
        'name': '王五',
        'level': 3,
        'salary': 8000
    },
    '1004': {
        'name': '赵六',
        'level': 4,
        'salary': 10000
    }
}

def raise_salary_2(staff_statistics):
    for id in staff_statistics:
        staff_info = staff_statistics[id]
        if staff_info['level'] == 1:
            staff_info['salary'] += 1000
            staff_info['level'] += 1
        elif staff_info['level'] == 2:
            staff_info['salary'] += 800
            staff_info['level'] += 1
        elif staff_info['level'] == 3:
            staff_info['salary'] += 600
            staff_info['level'] += 1
        else:
            staff_info['salary'] += 400
    return staff_statistics

def print_staff_info(staff_statistics):
    for id in staff_statistics:
        for key, value in staff_statistics[id].items():
            print(f'{key}: {format(float(value), '.2f') if key == "salary" else value}', end='\t')
        print()

if __name__ == '__main__':
    print_staff_info(raise_salary_1(staff_statistics_1))
    print()
    print_staff_info(raise_salary_2(staff_statistics_2))
