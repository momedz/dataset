from pymongo import MongoClient

client = MongoClient('10.80.37.160', 27017)
database = client['queue']
collection = database['task']

data = [{
    'assign': 'hscmstream',
    'parameter': {
        'radius': round(r * 0.05, 2),
        'np': np
    },
    'dataset': {
        'name': 'AHCM_20k_2d',
        'normalize': False
    },
    'status': 'todo'
} for np in range(2, 21) for r in range(1,11)]



# print(data.__len__())

# data = [{
#     'assign': 'hscmstream',
#     'parameter': {
#         'radius': 0.25,
#         'np': 2
#     },
#     'dataset': {
#         'name': 'HCM_5k',
#         'normalize': False
#     },
#     'status': 'todo'
# }]

collection.insert_many(data)