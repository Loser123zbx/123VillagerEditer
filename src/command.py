import json

def getDict(file):
    a = open(file, 'r' ,encoding = 'utf-8')
    data = a.readlines()
    a.close()
    keys =  []
    for i in data:
        keys.append(i.split(' ')[1])
    values = []
    for i in data:
        values.append(i.split(' ')[0])
    dic = dict(zip(keys, values))
    return dic

if __name__ == "__main__":
    pass
