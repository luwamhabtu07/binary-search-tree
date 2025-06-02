class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    def delete(self, value):
        def _min_value_node(node):
            while node.left:
                node = node.left
            return node

        def _delete(node, value):
            if not node:
                return None
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                # Case 1: No child
                if not node.left and not node.right:
                    return None
                # Case 2: One child
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # Case 3: Two children
                temp = _min_value_node(node.right)
                node.value = temp.value
                node.right = _delete(node.right, temp.value)
            return node

        self.root = _delete(self.root, value)

    def inorder_traversal(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result
