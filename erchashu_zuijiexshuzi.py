'''
动物牛牛是一只聪明的牛，它现在面临一个二叉树的问题。给定一个二叉树的根节点 root、一个目标值 target 和一个整数 m，请你返回二叉树中与目标值最接近的 m 个节点值。
请你编写一个函数 findClosestElements，接收一个二叉树的根节点 root、一个整数 target 和一个整数 m 作为参数，返回一个整数数组，表示与目标值最接近的 m 个节点值。
返回数组以非递减的形式给出。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @param target double浮点型 
# @param m int整型 
# @return int整型一维数组
#
class Solution:
    def findClosestElements(self , root: TreeNode, target: float, m: int) -> List[int]:
        # write code here
        # 中序遍历
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        vals = inorder_traversal(root)
        sorted_vals = sorted(vals)

        # 二分查找，找出最接近target的目标值
        def find_closest_index(arr, target):
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        closest_index = find_closest_index(sorted_vals, target)

        # 以最接近值为中点，找出左右两侧最接近的m个值
        left, right = closest_index - 1, closest_index
        results = []

        while len(results) < m:
            if left < 0:
                results.append(sorted_vals[right])
                right += 1
            elif right >= len(sorted_vals):
                results.append(sorted_vals[left])
                left -= 1
            else:
                if abs(sorted_vals[left] - target) <= abs(sorted_vals[right] - target):
                    results.append(sorted_vals[left])
                    left -= 1
                else:
                    results.append(sorted_vals[right])
                    right += 1

        return sorted(results)
