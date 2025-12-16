def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    data = f.read()
    digits = '0123456789'
    ans = []
    for i in data:
        if i in digits:
            ans += [int(i)]
    f.close()
    return ans
print(main('./data/data03.txt'))