class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
with open('user.out', 'w') as f:
    for nums in map(loads, sys.stdin):
        i = 0
        max = len(nums)
        while i < max:
            if nums[i] == 0:
                #nums = nums[0:i] + nums[i+1:] + [0]
                nums.append(nums.pop(i))
                max-=1
            else:
                i+=1
        print(
            dumps(nums).replace(' ', ''), 
            file=f
        )

exit()        
