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
        d: List[str] = [str(line.split()) for line in open(file, "r")]
        c: List[str] = [line.split()[-1] for line in open(file, "r")]
        return DataStatistics(len(d.pop()), len(set(c)), len(c)).__dict__

    # ---
    return dict({
        "real": [{
            "name": path.split(".")[0],
            "statistics": statistics(config_path + "/real/" + path)
        } for path in os.listdir(config_path + "/real/")],
        "synthetic": [{
            "name": path.split(".")[0],
            "statistics": statistics(config_path + "/synthetic/" + path)
        } for path in os.listdir(config_path + "/synthetic/")]
    })


def json_file(file, normalize) -> str:
    # ---
    def path_file(file: str) -> str:
        paths: List[str] = os.listdir(config_path + "/real/") + os.listdir(config_path + "/synthetic/")
        path: str = [path for path in paths if file in path].pop()

        if ".synthetic." in path:
            return config_path + '/synthetic/' + path
        else:
            return config_path + '/real/' + path

    def normalize_data(datalist: List[List[float]]) -> List[List[float]]:
        min = np.array(datalist).min(axis=0)
        max = np.array(datalist).max(axis=0)
        datapoint = (np.array(datalist) - min) / (max - min)
        return [list(p) for p in datapoint]

    # ---
    datas = [x.strip().split() for x in open(path_file(file), "r")]
    data = dict({
        "data": {
            "point": [[float(y) for y in x[0:-1]] for x in datas],
            "class": [p[-1] for p in datas],
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
