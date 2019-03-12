import json
import os
import numpy as np
from typing import Dict, List

config_path: str = "./dataset/data"


class DataStatistics(object):
    def __init__(self, dimension, cluster, count):
        self.dimension = dimension
        self.cluster = cluster
        self.count = count


def local() -> Dict[str, List[Dict[str, str]]]:
    # ---
    def statistics(file: str) -> Dict[str, int]:
        d: List[str] = list(map(lambda line: str(line.split()), open(file, "r")))
        c: List[str] = list(map(lambda line: line.split()[-1], open(file, "r")))
        return DataStatistics(len(d.pop()), len(set(c)), len(c)).__dict__

    # ---
    return dict({
        "real": list(map(lambda path: {
            "name": path.split(".")[0],
            "statistics": statistics(config_path + "/real/" + path)
        }, os.listdir(config_path + "/real/"))),
        "synthetic": list(map(lambda path: {
            "name": path.split(".")[0],
            "statistics": statistics(config_path + "/synthetic/" + path)
        }, os.listdir(config_path + "/synthetic/"))),
    })


def json_file(file, normalize) -> str:
    # ---
    def path_file(file: str) -> str:
        paths: List[str] = os.listdir(config_path + "/real/") + os.listdir(config_path + "/synthetic/")
        path: str = list(filter(lambda path: file in path, paths)).pop()
        if ".synthetic." in path:
            return config_path + '/synthetic/' + path
        else:
            return config_path + '/real/' + path

    def normalize_data(datalist):
        min = np.array(datalist).min(axis=0)
        max = np.array(datalist).max(axis=0)
        datapoint = (datalist - min) / (max - min)
        listdatapoint = dict()
        for point in datapoint:
            listdatapoint.update({listdatapoint.__len__(): list(point)})
        return listdatapoint

    # ---
    datas = list(map(lambda x: x.strip().split(), open(path_file(file))))
    # print(list(map(lambda x: x[-1], datas)))
    # print(list(map(lambda x: x[0:-1], datas)))
    data = dict({
        "data": {
            "point": list(map(lambda x: list(map(lambda y: float(y), x[0:-1])), datas)),
            "class": list(map(lambda x: x[-1], datas))
        },
        "count": datas.__len__(),
        "dimension": datas.pop().__len__()
    })
    if normalize:
        data["data"]["point"] = normalize_data(data["data"]["point"])

    return json.dumps(data)


def information() -> str:
    with open(config_path + '/information.json') as rf:
        return json.dumps(json.load(rf))


def update_information() -> None:
    with open(config_path + '/information.json', 'w') as wf:
        wf.write(json.dumps(local(), sort_keys=True, indent=2, separators=(',', ': ')))


if __name__ != '__main__':
    update_information()
