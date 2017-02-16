# coding=utf-8
__author__ = 'g7842'
try:
    import cPickle as pickle
except ImportError:
    import pickle

# pick dumps dump
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
with open('_files/dump.txt', 'wb') as f:
    pickle.dump(d, f)

#pick loads load
with open('_files/dump.txt', 'rb') as f:
    print(pickle.load(f))
#print(pickle.loads("{'age': 20, 'score': 88, 'name': 'Bob'}"))

#json
from testclass import Student
import json

xiaoming = Student('王小明', 5, '小明')


def to_json(std):
    return {'name': std.get_name(), 'age': std.get_age()}

print(json.dumps(xiaoming, default=to_json))
print(json.dumps(xiaoming, default=lambda obj: obj.__dict__))
