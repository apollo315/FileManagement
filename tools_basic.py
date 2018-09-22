from functools import reduce

################################################################################################
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    # 功能：单个字符数字转数字；
    # 输入：字符；
    # 输出：数字；
    return DIGITS[s]


def str2int(s):
    # 功能：字符串数字转数字；
    # 输入：字符串；
    # 输出：数字；
    # 来源：廖雪峰的Python教程->函数式编程->高阶函数->map/reduce
    # 创建日期：2018-09-21

    # 算法步骤：
    # 1、map(char2num, s)，将字符串每一位转为数字，存储在Iterator惰性序列中；
    # 2、reduce(lambda x, y: x * 10 + y, 惰性序列)，将惰性序列生成数字，如123 = (1*10 + 2) * 10 + 3
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


################################################################################################

