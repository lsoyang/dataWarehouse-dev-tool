import os
import xlrd

book = xlrd.open_workbook("source.xlsx")
table = book.sheet_by_index(0)
max_row = table.nrows
max_col = table.ncols
# 库名
database = table.cell(0, 0)
# 表名
table_name = table.cell(0, 1)

# 找到需要判断空值的字段名
list1 = []
for i in range(1, max_row):
    if table.cell(i, 1).value != '':
        list1.append(table.cell(i, 0).value)

print(list1)

# 找到需要枚举分布的字段名
list2 = []
for i in range(1, max_row):
    if table.cell(i, 2).value != '':
        list2.append(table.cell(i, 0).value)

print(list2)

# 找到需要判断空值的字段名
list3 = []
for i in range(1, max_row):
    if table.cell(i, 3).value != '':
        list3.append(table.cell(i, 0).value)

print(list3)

# 开始生成SQL：
