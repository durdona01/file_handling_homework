def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    d = f.read()
    res = [0,0]
    for i in d:
        if i.isdigit():
            res[0] += 1
        else:
            res[1]+= 1

    f.close()
    return res
    
print(main('./data/data05.txt'))