from pymongo import MongoClient

client = MongoClient('10.80.37.160', 27017)
database = client['queue']
collection = database['task']

data = [{
    'assign': 'denstream',
    'parameter': {
        'init': 1000,
        'lambda': 0.01,
        'epsilon': round(r * 0.05, 2),
        'mu': np,
        'beta': 0.2,
    },
    'dataset': {
        'name': 'HCM_5k',
        'normalize': False
    },
    'status': 'todo'
} for np in range(2, 21) for r in range(1,11)]



# print(data.__len__())

# data = [{
#     'assign': 'denstream',
#     'parameter': {
#         'init': 1000,
#         'lambda': 0.01,
#         'epsilon': 0.5,
#         'mu': 10,
#         'beta': 0.2,
#     },
#     'dataset': {
#         'name': 'HCM_5k',
#         'normalize': False
#     },
#     'status': 'todo'
# }]

collection.insert_many(data)