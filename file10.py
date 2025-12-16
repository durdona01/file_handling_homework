def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data)
    d = f.readlines()
    ans = d[2]

    for i in range(len(d)):
        if len(d[i]) > len(ans):
            ans = d[i]
    f.close()
    return ans[:-1]
print(main('./data/data10.txt'))