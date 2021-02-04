di_fang = ['shanghai', 'beijing', 'yunnan', 'haerbing', 'qingdao']
print('原始排列')
print(di_fang)

print('\n按字母顺序')  # 按字母顺序排列，但不影响原有序列
print(sorted(di_fang))  # 调用sorted()函数，不影响原序列

print('\n原始顺序')
print(di_fang)

print('\n按字母倒序')
print(sorted(di_fang, reverse=True))

print('\n原始顺序')
print(di_fang)

print('\n倒着打印')
di_fang.reverse()  # 方法reverse()永久修改
print(di_fang)
print('\n倒着打印重复一次')
di_fang.reverse()  # 重复方法reverse()恢复原来序列
print(di_fang)

print('\n按字母顺序')  # 顺序永久改变
di_fang.sort()  # 方法sort()修改

print(di_fang)
print('\n按字母倒序')
di_fang.sort(reverse=True)
print(di_fang)
