from pymongo import MongoClient

client = MongoClient('10.80.37.160', 27017)
database = client['queue']
collection = database['task']

collection.insert_one({
    'assign': 'hscmstream',
    'parameter': {
        'radius': 0.30,
        'np': 2
    },
    'dataset': {
        'name': 'moon',
        'normalize': False
    },
    'status': 'todo'
})