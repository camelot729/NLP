import shelve

with shelve.open('index.db', 'c') as index:
    index.sync()
    # print(len(index))

