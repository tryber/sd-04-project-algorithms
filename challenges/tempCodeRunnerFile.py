def find_duplicate(nums):
    if nums is None:
        return False
    if type(nums) is str:
        return False
    
    for x in nums:
        if x == x:
            return x
        else:
            return False

print(find_duplicate('a'))