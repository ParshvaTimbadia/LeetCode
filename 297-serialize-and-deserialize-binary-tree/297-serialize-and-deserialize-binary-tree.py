# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def helper(node):
            
            if node is None:
                result.append("None")
                return
            
            result.append(str(node.val))
            helper(node.left)
            helper(node.right)
        
        helper(root)
        result = ",".join(result)
        
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        new_data = data.split(",")
        
        index = 0
        def helper():
            nonlocal index
            
            if new_data[index] == 'None':
                return None
            
            node = TreeNode(new_data[index])
            index += 1 
            node.left = helper()
            index += 1
            node.right = helper()
            
            return node
        
        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))