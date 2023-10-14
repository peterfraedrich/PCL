#!/usr/bin/env python3

class PCLObject:
    file_path: str

    def __init__(self, file_path: str):
        self.file_path: file_path
        return

    def __repr__(self) -> str:
        pass

    def Dump(self) -> str:
        return self.__repr__()

    def DumpFile(self, path: str):
        with open(path, 'w+') as f:
            f.write(self.__repr__())
        return


def Parse(path: str) -> PCLObject:
    pcl_o = PCLObject(path)
    return pcl_o


class PCLType:
    py_type: type
    Key: str
    Value: object

    def __init__(self, key: str, type: str, value: object):
        self.Key = key
        self.Value = value
        return


class PCLString(PCLType):
    py_type = str


class PCLNumber(PCLType):

    def __init__(self, key: str, type: str, value: object):
        self.Key = key
        self.Value = value
        self.py_type = self._getType(type)

    def _getType(self, type: str):
        try:
            int(type)
            return int
        except TypeError:
            pass
        try:
            float(type)
            return float
        except TypeError:
            pass
        raise TypeError


class PCLBoolean(PCLType):
    py_type = bool
    pass


class PCLList(PCLType):
    py_type = list
    pass


class PCLDict(PCLType):
    py_type = dict
    pass
