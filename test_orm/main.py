import dataset

db = dataset.connect('sqlite:///test.sqlite')
# db.create_table('CH')
table = db['CH']

table.insert(dict(chid=1018726552936128553))
# table.update(dict(chid=12344566767), ['CH'])

