def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data)
    d = f.read()
    
    nums = []
    for i in d:
        if i.isdigit():
            nums += [int(i)]

    minNum = nums[0]
    for num in nums:
        if num < minNum:
            minNum = num
    f.close()
    return minNum

print(main('./data/data09.txt'))