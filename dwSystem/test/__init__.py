import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

data1 = {
    'labels': ['web', '物联网', '前端', '云原生', '操作系统', '大数据', '深度学习', '自然语言处理', '数据库管理', '计算机视觉'],
    'sizes': [122, 67, 40, 33, 28, 27, 10, 3, 3, 3]
}

data2 = {
    'labels': ['A', 'B', 'C', 'D'],
    'sizes': [40, 30, 20, 10]
}

# 计算位置
positions = [0, 1.5]

def draw_pie_chart(data, pos):
    labels = data['labels']
    sizes = data['sizes']
    ax = plt.subplot(1, 2, pos)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    ax.set_title(f'技术领域比例 {pos}')

draw_pie_chart(data1, 1)
draw_pie_chart(data2, 2)

plt.show()
