import matplotlib.pyplot as plt
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
plt.style.use('ggplot')
plt.figure(figsize=(10, 8))


class VisualData:
    cpuData = {
        'labels': [],
        'sizes': []
    }

    domainData = {
        'labels': [],
        'sizes': []
    }

    frameData = {
        'labels': [],
        'sizes': []
    }

    projectData = {
        'labels': [],
        'sizes': []
    }

    def __init__(self):
        with open('../data/cpuData.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split()
                if len(parts) > 0:
                    self.cpuData['labels'].append(parts[0])
                    self.cpuData['sizes'].append(parts[1])
            f.close()
        with open('../data/domainData.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split()
                if len(parts) > 0:
                    self.domainData['labels'].append(parts[0])
                    self.domainData['sizes'].append(parts[1])
            f.close()
        with open('../data/frameData.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split()
                if len(parts) > 0:
                    self.frameData['labels'].append(parts[0])
                    self.frameData['sizes'].append(parts[1])
            f.close()
        with open('../data/projectData.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split()
                if len(parts) > 0:
                    self.projectData['labels'].append(parts[0])
                    self.projectData['sizes'].append(parts[1])
            f.close()

    def drawCpuChart(self):
        labels = self.cpuData['labels']
        sizes = self.cpuData['sizes']
        ax = plt.subplot(2, 2, 1)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title('编程语言比例(Top10)')

    def drawDomainChart(self):
        labels = self.domainData['labels']
        sizes = self.domainData['sizes']
        ax = plt.subplot(2, 2, 2)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title('技术领域比例(Top10)')

    def drawFrameChart(self):
        labels = self.frameData['labels']
        sizes = self.frameData['sizes']
        ax = plt.subplot(2, 2, 3)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title('技术框架比例(Top10)')

    def drawProjectChart(self):
        labels = self.projectData['labels']
        sizes = self.projectData['sizes']
        ax = plt.subplot(2, 2, 4)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title('应用项目比例(Top10)')


if __name__ == "__main__":
    obj = VisualData()
    obj.drawCpuChart()
    obj.drawDomainChart()
    obj.drawFrameChart()
    obj.drawProjectChart()
    plt.show()
