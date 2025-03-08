import csv

data = []
with open('../data/data.csv', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    # header = next(csv_reader)        # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到data中
        print(row)  # 选择某一列加入到data数组中