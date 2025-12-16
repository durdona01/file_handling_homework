def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
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

    maxNum = nums[0]
    for num in nums:
        if num > maxNum:
            maxNum = num
    f.close()
    return maxNum

print(main('./data/data08.txt'))