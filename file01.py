def main(data:str):
    f = open(data)
    data = f.read()
    res = data.split(',')
    f.close()
    return res
print(main('./data/data01.txt'))