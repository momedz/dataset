import json
import os
import numpy

configpath = "./datasets/"

def path():
    if configpath is None:
        return os.getcwdu()
    else:
        return configpath

def local():
    # ---
    def statistics(file):
        d = list()
        c = list()
        for line in open(file, "r"):
            d.append(line.split())
            c.append(line.split()[-1])
        return {
            "dimention": d[0].__len__() - 1,
            "count": c.__len__(),
            "cluster": set(c).__len__(),
        }
    # ---
    file_dr = os.listdir(path()+"/real/")
    file_ds = os.listdir(path()+"/synthetic/")
    local = dict({
        "real": [],
        "synthetic": [],
    })
    for f in file_dr:
        file = {
            "name": f.split(".")[0],
            "stat": statistics(path()+"/real/"+f)
        }
        local["real"].append(file)

    for f in file_ds:
        file = {
            "name": f.split(".")[0],
            "stat": statistics(path() + "/synthetic/" + f),
        }
        local["synthetic"].append(file)
    return local

def jsonFile(file, normalize):
    # ---
    def pathFile(file):
        file_dr = os.listdir(path() + "/real/")
        file_ds = os.listdir(path() + "/synthetic/")
        pathfile = dict()
        for line in file_dr:
            pathfile.update({ line.split(".")[0]: path() + "/real/" + line })
        for line in file_ds:
            pathfile.update({ line.split(".")[0]: path() + "/synthetic/" + line })
        return pathfile[file]
    def normalize_data(datalist):
        min = numpy.array(datalist).min(axis=0)
        max = numpy.array(datalist).max(axis=0)
        datapoint = (datalist - min) / (max - min)
        listdatapoint = dict()
        for point in datapoint:
            listdatapoint.update({listdatapoint.__len__(): list(point)})
        return listdatapoint
    # ---
    with open(pathFile(file)) as rf:
        listdatapoint = dict()
        listdataclass = dict()
        listpoint = list()
        for line in rf:
            lengthdata = line.split().__len__()
            datapoint = list(map(lambda x: float(x), line.split()[0:lengthdata-1]))
            dataclass = list(map(lambda x: str(x), line.split()[lengthdata-1:]))
            listdatapoint.update({listdatapoint.__len__(): datapoint})
            listdataclass.update({listdataclass.__len__(): dataclass})
            listpoint.append(datapoint)
        data = dict({
            "data": {
                "point": listdatapoint,
                "class": listdataclass,
            },
            "count": listdataclass.__len__(),
            "dimension": listdatapoint[0].__len__(),
        })
        if normalize:
            data["data"]["point"] = normalize_data(listpoint)
    return json.dumps(data)

def getFile(file, type='json', normalize=False):
    if type == 'json':
        return jsonFile(file, normalize)
    else:
        return None

def information():
    with open(path() + '/information.json') as rf:
        return json.dumps(json.load(rf))

def update_information():
    log = {
        "local": local(),
        "online": "TODO",
    }
    with open(path() + '/information.json', 'w') as wf:
        wf.write(json.dumps(log, sort_keys=True, indent=4, separators=(',', ': ')))

if __name__ != '__main__':
    update_information()