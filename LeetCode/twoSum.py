class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, arg1 in enumerate(nums):
            arg2 = target - arg1
            if arg2 in hashmap:
                print(hashmap)
                return [hashmap[arg2], index]
            hashmap[arg1] = index
        return None

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,4]
    target = 6
    result = s.twoSum(nums,target)
    print(result)
