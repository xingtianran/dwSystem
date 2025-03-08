import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import tkinter as tk

# 示例数据
labels = ['A', 'B', 'C', 'D']
sizes = [20, 30, 35, 15]

# 绘制饼状图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True,
        textprops={'fontsize': 12}, colors=['red', 'green', 'blue', 'yellow'])

# 添加标题
plt.title('好看的饼状图示例', fontsize=16)

plt.axis('equal')  # 保持图形为圆形

root = tk.Tk()
root.wm_state('zoomed')  # 设置全屏

plt.show()
root.destroy()