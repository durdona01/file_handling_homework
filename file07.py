def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data)
    d = f.read()
    res = []
    for i in d:
        if i.isdigit():
            res += [int(i)]
    sum_n = 0
    for num in res:
        sum_n += num
    f.close()
    return sum_n
print(main('./data/data07.txt'))