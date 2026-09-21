# 通过分隔符连接列表/元组
print(','.join(['a', 'b', 'c'])) # a,b,c
# 格式化字符串
str1 = "my name is {0} {name}"
newStr = str1.format('Hank',name = 'Miller')
print(newStr)
# 按照给定字符分裂字符串
splitStr = str1.split()
print(splitStr)
# 获取子串
start = 1
print(str1[start:8])
# 补 '0' 向右对齐字符串
day = '2'
print(day.zfill(2)) # 02
print(day.zfill(3)) # 002
print(day.zfill(2).zfill(2)) # 02