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


def build_sample_tree():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    return root


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    return root


def build_bst(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=' ')
        inorder_traversal(node.right)


# Example usage:
elements = [5, 3, 7, 2, 4, 6, 8]
bst_root = build_bst(elements)

# Perform an inorder traversal to check if the BST is constructed correctly
print("Inorder Traversal:")
inorder_traversal(bst_root)


def main():
    root = build_sample_tree()
    iterator = BSTIterator(root)

    print("In-order traversal using Iterator:")
    for i in iterator:
        print(i)

    iterator2 = BSTIterator(bst_root)
    for i in iterator2:
        print(i)

if __name__ == "__main__":
    main()


#--------------------------------------------------------------------------------------------------------------------------------
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class TraversalStrategy:
    def traverse(self, root, result):
        pass


class InOrderStrategy(TraversalStrategy):
    def traverse(self, root, result):
        if root:
            self.traverse(root.left, result)
            result.append(root.key)
            self.traverse(root.right, result)


class PreOrderStrategy(TraversalStrategy):
    def traverse(self, root, result):
        if root:
            result.append(root.key)
            self.traverse(root.left, result)
            self.traverse(root.right, result)


class PostOrderStrategy(TraversalStrategy):
    def traverse(self, root, result):
        if root:
            self.traverse(root.left, result)
            self.traverse(root.right, result)
            result.append(root.key)


class BSTIterator:
    def __init__(self, root, traversal_strategy=InOrderStrategy()):
        self.nodes = []
        self.index = 0
        self.traverse(root, traversal_strategy)

    def traverse(self, root, traversal_strategy):
        traversal_strategy.traverse(root, self.nodes)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.nodes):
            current_node = self.nodes[self.index]
            self.index += 1
            return current_node
        else:
            raise StopIteration

# Example usage:
elements = [5, 3, 7, 2, 4, 6, 8]
bst_root = None

# Build BST
for element in elements:
    bst_root = insert(bst_root, element)

# Create iterators for preorder and postorder traversals using strategy pattern
preorder_iterator = BSTIterator(
    bst_root, traversal_strategy=PreOrderStrategy())
postorder_iterator = BSTIterator(
    bst_root, traversal_strategy=PostOrderStrategy())

# Print results using for loop
print("Preorder Traversal:")
for key in preorder_iterator:
    print(key, end=' ')

print("\n\nPostorder Traversal:")
for key in postorder_iterator:
    print(key, end=' ')
