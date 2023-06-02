import collections

import dataset
from dataset import *
db = dataset.connect('sqlite:///../db.sqlite')
# db.create_table('CH')
# global db
table: Table = db['notech']
r = table.find_one(ch=1111)
# for x in r:
#     print(x['text'])
print(r['text'])


# if not table.exists:
# table.insert(dict(chid=1234))
# else:
#     table.update(dict(chid=12344566767), ['CH'])

# table.delete()
# r = db['CH'].all()
# db1: Database = dataset
# r: Table = db['CH']
#
# # for x in r:
# #     x: collections.OrderedDict
# #     print(x)
# #     print(f'id: {x}')
# #     # print(type(x))
#
# for x in r.all():
#     print(x['chid'])
