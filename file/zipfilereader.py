import sys
import zipfile
from parse import compile
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''Maintain a list of pid{[dictionary{timestamp, count}, ...]'''


class Record:
    def __init__(self):
        self.dictOfLists = {}

    def update(self, pid, timestamp, count):
        if pid in self.dictOfLists:
            self.dictOfLists[pid].append({timestamp: count})
        else:
            self.dictOfLists[pid] = [{timestamp: count}]

    def showPids(self):
        for key in self.dictOfLists:
            print(key)
            arrayOfDictionaries = self.dictOfLists[key]
            for entry in arrayOfDictionaries:
                # print("{}".format(entry))
                for item in entry:
                    print("{} {}".format(item, entry[item]))

    def getPids(self):
        return self.dictOfLists.keys()

    def getRecords(self):
        return self.dictOfLists

    def getRecordLength(self):
        return len(self.dictOfLists)

    def getKey(self, index):
        keys = self.dictOfLists.keys()
        count = 0;
        for key in keys:
            if count == index:
                return key
            count += 1

        print("index {} is out of bounds".format(index))

    def getXvalues(self,key):
        # key = self.getKey(index)
        list = []
        arrayOfDictionaries = self.dictOfLists[key]
        for entry in arrayOfDictionaries:
            for item in entry:
                list.append(item)
        return list

    def getYValues(self,key):
        # key = self.getKey(index)
        list = []
        arrayOfDictionaries = self.dictOfLists[key]
        for entry in arrayOfDictionaries:
            for item in entry:
                list.append(int(entry[item]))
        return list

    def runPlot(self):
        for pid in self.dictOfLists:
            self.plot(pid)


    def plot(self, pid):
        # Data
        # df = pd.DataFrame({'x_values': range(1, 11), 'y1_values': np.random.randn(10),
        #                    'y2_values': np.random.randn(10) + range(1, 11),
        #                    'y3_values': np.random.randn(10) + range(11, 21)})
        xLabel = "{}_time".format(pid)
        xValues = self.getXvalues(pid)
        yLabel = "{}_filecount".format(pid)
        yValues = self.getYValues(pid)

        print("xLabel: {}".format(xLabel))
        print("xValues: {}".format(xValues))
        print("yLabel: {}".format(yLabel))
        print("yValues: {}".format(yValues))

        xlength = len(xValues)
        ylength = len(yValues)
        print("len: {} {}".format(xlength, ylength))
        print("np.random.randn: {}".format(np.random.randn(xlength - 1)))
        df = pd.DataFrame({
                           xLabel: range(0, ylength), yLabel: yValues,
                           })

        # multiple line plots
        plt.plot(xLabel, yLabel, data=df, marker='', color='olive', linewidth=2)
        # show legend
        plt.legend()

        # show graph
        plt.show()


def getTimestamp(line):
    fields = line.split()
    return fields[0]


def doFileCount(line, record):
    p = compile("{} filecount for pid {} is {}")
    result = p.parse(line)
    timestamp = result[0].lstrip().rstrip()
    pid = result[1].rstrip()
    count = result[2].rstrip()
    ## Register PID with count
    record.update(pid, timestamp, count)


def readPerfLog(zip):
    record = Record()
    perflog = z.getinfo("openfiles_perf/perf.log")
    print("{} filesize: {}".format(perflog.filename, perflog.file_size))
    print("{} compress_size: {}".format(perflog.filename, perflog.compress_size))

    with zip.open(perflog) as f:
        for b_line in f:
            line = b_line.decode('utf-8')
            print("Type: {}".format(type(line)))
            print(line.rstrip().lstrip())
            index = line.find('filecount for pid', 0)
            print("index: {}".format(index))
            if index > -1:
                doFileCount(line, record)
    record.showPids()
    record.runPlot()


prog = sys.argv[0]
filename = sys.argv[1]
print("filename = {}".format(filename))

z = zipfile.ZipFile(filename)
z.printdir()

readPerfLog(z)
z.close()
