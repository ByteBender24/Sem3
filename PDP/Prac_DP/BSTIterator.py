# --------------------------------------------------------------------ITERATOR PATTERN-----------------------------------------
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._inorder_stack(root)

    def _inorder_stack(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def has_next(self):
        return len(self.stack) > 0

    def __next__(self):
        if self.has_next():
            current_node = self.stack.pop()
            self._inorder_stack(current_node.right)
            return current_node.key
        else:
            raise StopIteration

    def __iter__(self):
        return self

# Example Usage


def build_sample_tree():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    return root


def main():
    root = build_sample_tree()
    iterator = BSTIterator(root)

    print("In-order traversal using Iterator:")
    for i in iterator:
        print(i)


if __name__ == "__main__":
    main()
