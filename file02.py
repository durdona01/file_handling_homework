def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data)
    data = f.read()
    f.close()
    return len(data)
print(main('./data/data02.txt'))