def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    data = f.read()
    res = []
    for i in data:
        if not i.isdigit() and i != '\n':
            res += [i]
    f.close()
    return res
print(main('./data/data04.txt'))