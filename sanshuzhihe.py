'''
动物牛牛是一个勇敢的冒险家，它正在探索一个神秘的岛屿。岛上有许多宝藏，但是宝藏被隐藏在一系列数字中。牛牛找到了一个整数数组 nums，它相信这个数组中存在一些特殊的三元组，满足以下条件：

三元组的和等于 0。
三元组中的元素不能重复。
牛牛想按照字典序返回所有满足条件的三元组。
请你帮助牛牛解决这个问题，设计一个函数 findTriplets，接收一个整数数组 nums 作为参数，并返回一个二维整数数组，表示满足条件的三元组，按照字典序返回所有的三元组。
'''

def findTriplets(nums):
    # write code here
    results = []
    nums.sort()
    for i in range(len(nums)-2):
        # 去重
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                results.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # 去重
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
    return results

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    result = findTriplets(nums)
    print(result)