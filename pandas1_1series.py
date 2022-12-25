import pandas as pd
import numpy as np

print("创建" + "*" * 20)

print('-' * 8 + '从列表创建' + '-' * 8)
# 带索引的一列数据
s1 = pd.Series([1,2,3,4,5])
print(s1)


print('-' * 8 + '从 ndarray 创建' + '-' * 8)
# 索引为 a b c d e
s2 = pd.Series(np.arange(5), index=['a','b','c','d','e'])
print(s2)

print('-' * 8 + '从字典创建' + '-' * 8)
# 创建一个字典,用key来构成表的索引
temp_dict = {"name": "zhangsan", "age": 27, "tel": 10086}
# 字典数据直接传入data
s3 = pd.Series(temp_dict)
print(s3)

print('-' * 8 + '从标量值构造' + '-' * 8)
s4 = pd.Series(1., index=list("abcde"))
print(s4)




