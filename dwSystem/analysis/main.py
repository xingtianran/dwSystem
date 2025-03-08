import csv
import jieba


class AnalysisData:
    data = ''
    computeDict = []
    domainDict = []
    frameDict = []
    projectDict = []

    def __init__(self):
        dataList = []
        with open('../data/data.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                dataList.append(row[1])

        self.data = ' '.join(dataList)

        self.data = self.data.lower()

    def readCpuWord(self):
        with open('../dictionary/computerWord.txt', 'r', encoding='utf-8') as f:
            self.computeDict = f.read().splitlines()
            f.close()
        return self.computeDict

    def readDomainWord(self):
        with open('../dictionary/domainWord.txt', 'r', encoding='utf-8') as f:
            self.domainDict = f.read().splitlines()
            f.close()
        return self.domainDict

    def readFrameWord(self):
        with open('../dictionary/frameWord.txt', 'r', encoding='utf-8') as f:
            self.frameDict = f.read().splitlines()
            f.close()
        return self.frameDict

    def readProjectWord(self):
        with open('../dictionary/projectWord.txt', 'r', encoding='utf-8') as f:
            self.projectDict = f.read().splitlines()
            f.close()
        return self.projectDict

    # 计算机语言
    def analysisCpuData(self):

        jieba.load_userdict(self.readCpuWord())
        words = jieba.cut(self.data)
        computer_words = [word for word in words if word in self.computeDict]
        counts = {}
        for word in computer_words:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)
        wList = []
        for i in range(10):
            wList.append(items[i])
        with open('../data/cpuData.txt', 'w', encoding='utf-8') as f:
            for item in wList:
                f.write(' '.join(map(str, item)) + '\n')
            f.close()

    # 统计计算机领域
    def analysisDomainData(self):

        jieba.load_userdict(self.readDomainWord())
        words = jieba.cut(self.data)
        domain_words = [word for word in words if word in self.domainDict]
        counts = {}
        for word in domain_words:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)
        wList = []
        for i in range(10):
            wList.append(items[i])
        with open('../data/domainData.txt', 'w', encoding='utf-8') as f:
            for item in wList:
                f.write(' '.join(map(str, item)) + '\n')
            f.close()

# 统计语言框架
    def analysisFrameData(self):

        jieba.load_userdict(self.readFrameWord())
        words = jieba.cut(self.data)
        frame_words = [word for word in words if word in self.frameDict]
        counts = {}
        for word in frame_words:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)
        wList = []
        for i in range(10):
            wList.append(items[i])
        with open('../data/frameData.txt', 'w', encoding='utf-8') as f:
            for item in wList:
                f.write(' '.join(map(str, item)) + '\n')
            f.close()

# 统计项目
    def analysisProjectData(self):

        jieba.load_userdict(self.readProjectWord())
        words = jieba.cut(self.data)
        project_words = [word for word in words if word in self.projectDict]
        counts = {}
        for word in project_words:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)
        wList = []
        for i in range(10):
            wList.append(items[i])
        with open('../data/projectData.txt', 'w', encoding='utf-8') as f:
            for item in wList:
                f.write(' '.join(map(str, item)) + '\n')
            f.close()


if __name__ == "__main__":
    obj = AnalysisData()
    obj.analysisCpuData()
    obj.analysisDomainData()
    obj.analysisFrameData()
    obj.analysisProjectData()
