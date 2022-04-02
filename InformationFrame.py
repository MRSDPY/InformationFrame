class InformationFrame:
    __tRows = 0
    __dataHolder = {}

    def __init__(self, id, path):
        self.id = id
        self.path = path
        self.readData()

    def readData(self):
        try:
            data = []
            with open(self.path, "r") as f:
                data = [line.strip(" \n") for line in f]

            for i in data:
                _data = i.split(" ")
                r = {
                    self.__tRows: dict(zip(_data[0::2], [int(x) for x in _data[1::2]]))
                }
                self.__tRows += 1
                self.__dataHolder.update(r)
            print(self.__dataHolder)
        except Exception as e:
            print(e)

    def displayFrameMetaData(self):
        print("***** INFORMATION META DATA *****")
        print("ID: ", self.id)
        print("Associated File: ", self.path)
        print("Frame Rows: ", self.__tRows)

    def displayCells(self, values: list):
        _indata = []
        for i in self.__dataHolder.keys():
            for j in range(len(values)):
                _d = self.__dataHolder[i].get(values[j])
                if _d is not None and _d != "":
                    _indata.append(_d)
        print(" ".join(str(x) for x in _indata))

    def displayRow(self, index: int):
        print(" ".join(str(v) for v in self.__dataHolder[index].values()))

    def sumCell(self, values: list):
        _indata = []
        for i in self.__dataHolder.keys():
            for j in range(len(values)):
                _d = self.__dataHolder[i].get(values[j])
                if _d is not None and _d != "":
                    _indata.append(_d)
        return sum(_indata)

    def avgCell(self, values: list):
        _indata = []
        for i in self.__dataHolder.keys():
            for j in range(len(values)):
                _d = self.__dataHolder[i].get(values[j])
                if _d is not None and _d != "":
                    _indata.append(_d)
        return sum(_indata) / len(_indata)

    def minCell(self, values: list):
        _indata = []
        for i in self.__dataHolder.keys():
            for j in range(len(values)):
                _d = self.__dataHolder[i].get(values[j])
                if _d is not None and _d != "":
                    _indata.append(_d)
        return min(_indata)

    def maxCell(self, values: list):
        _indata = []
        for i in self.__dataHolder.keys():
            for j in range(len(values)):
                _d = self.__dataHolder[i].get(values[j])
                if _d is not None and _d != "":
                    _indata.append(_d)
        return max(_indata)
