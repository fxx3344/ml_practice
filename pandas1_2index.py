import pandas as pd
import numpy as np

s2 = pd.Series(np.arange(5), list("abcde"))

print(s2)

print("切片和索引" + "*" * 20)

print('-' * 8 + '支持数字索引操作' + '-' * 8)
print(s2[0])

print('-' * 8 + '支持切片操作' + '-' * 8)
print(s2[:3])

# print('-' * 8 + '花式索引' + '-' * 8)
# print(s2[1,0,2])

# print('-' * 8 + '布尔索引' + '-' * 8)
# print(s2[s2>2])
