def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    d = f.readlines()
    res = []
    for i in d:
        res += [len(i)-1]
    f.close()
    return res
print(main('./data/data06.txt'))