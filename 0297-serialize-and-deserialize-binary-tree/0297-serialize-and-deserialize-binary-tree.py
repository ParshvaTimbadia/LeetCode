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
        # Create an pre order traversal for serailization:
        result = []
        def helper(node):
            
            if node is None:
                result.append("None")
                return 
            
            result.append(str(node.val))
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return ",".join(result)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.split(",")
        index = 0
        
        def helper():
            nonlocal index
            
            if data[index] == "None":
                index += 1
                return None
            
            if index == len(data):
                return None
            
            node = TreeNode(data[index])
            index += 1
            node.left = helper()
            node.right = helper()
            
            return node
        
        return helper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))