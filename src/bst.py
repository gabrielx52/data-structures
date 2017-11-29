"""Binary search tree."""


class Node(object):
    """BST Node object class."""

    def __init__(self, val, parent=None):
        """Constructor method for BST Node."""
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent


class BST(object):
    """Binary search tree object class."""

    def __init__(self, iterable=None):
        """Constructor method for BST."""
        self._root = None
        self._size = 0
        self._depth = 0
        self._balance = 0
        if iterable:
            if isinstance(iterable, (list, set)):
                for item in iterable:
                    self.insert(item)
            else:
                raise TypeError('Iterable must be a list or set.')

    def insert(self, val):
        """Insert value into BST."""
        if isinstance(val, (int, float)):
            if self._root is None:
                self._root = Node(val)
                self._size += 1
                return
            deep = 0
            current = self._root
            if val > self._root.val:
                self._balance -= 1
            else:
                self._balance += 1
            while True:
                if val > current.val:
                    deep += 1
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val, current)
                        self._size += 1
                        self.depth_checker(deep)
                        return
                if val < current.val:
                    deep += 1
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val, current)
                        self._size += 1
                        self.depth_checker(deep)
                        return
                if val == current.val:
                    return
        else:
            raise TypeError('Node value must be float or int.')

    def depth_checker(self, depth):
        """Compare and update current depth with node depth."""
        if depth > self._depth:
            self._depth = depth

    def search(self, val):
        """Return node containing val."""
        current = self._root
        try:
            if val == current.val:
                return current
            while True:
                if val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        return None
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        return None
                if val == current.val:
                    return current
        except AttributeError:
            return

        # def _search_helper(self, direction=):
        #     """."""
        #     pass

    def size(self):
        """Return size of BST."""
        return self._size

    def depth(self):
        """Return depth of BST."""
        return self._depth

    def contains(self, val):
        """Return True/False if val is in BST."""
        return bool(self.search(val))

    def balance(self):
        """Return True/False if BST is balanced."""
        return self._balance

    def in_order(self):
        """Return in-order traversal generator."""
        stack = []
        current = self._root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                yield current.val
                current = current.right

    def pre_order(self):
        """Return pre-order traversal generator."""
        stack = [self._root]
        current = None
        while current or stack:
            if not current:
                current = stack.pop()
            else:
                yield current.val
                stack.extend([current.right, current.left])
                current = stack.pop()

    def post_order(self):
        """Return post-order traversal generator."""
        stack = []
        current = self._root
        while current or stack:
            if current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if stack and current.right == stack[-1]:
                    stack.pop()
                    stack.append(current)
                    current = current.right
                else:
                    yield current.val
                    current = None

    def breadth_first(self):
        """Return breadth-first traversal generator."""
        stack = []
        current = self._root
        while current or stack:
            if current:
                yield current.val
                stack.extend([current.left, current.right])
                current = stack.pop(0)
            else:
                current = stack.pop(0)

    def delete(self, val):
        """Delete node containing val from the BST."""
        current, parent = self._root, None
        while current and current.val != val:
            parent = current
            if val > current.val:
                current = current.right
            else:
                current = current.left
        if current is None:
            return
        tmp = None
        if current.left and current.right:
            tmp = self._remove(current)
            tmp.left = current.left
            tmp.right = current.right
        elif current.left is None:
            tmp = current.right
        else:
            tmp = current.left

        if current == self._root:
            self._root = tmp
        elif parent.left == current:
            parent.left = tmp
        else:
            parent.right = tmp

        return

    def _remove(self, node):
        """Remove child node."""
        current, parent = node.right, node
        while current.left:
            parent = current
            current = current.left
        if current == parent.right:
            parent.right = current.right
        else:
            parent.left = current.right
        return current

    def delete_2(self, val):
        """Delete method for BST."""
        target = self.search(val)
        if target:
            if target.right and target.left:
                self._parent_remover_twins(target)
            elif target.right:
                self._parent_remover(target, target.right)
            elif target.left:
                self._parent_remover(target, target.left)
            else:
                self._parent_remover(target)
                target.parent = None
        else:
            return

    def _parent_remover(self, target, child=None):
        """Remove node with one or no children."""
        if target.val < target.parent.val:
            target.parent.left = child
            if child:
                child.parent = target.parent.left
        else:
            target.parent.right = child
            if child:
                child.parent = target.parent.left

    def _parent_remover_twins(self, target):
        """Remove node with two children."""
        pass


if __name__ == '__main__':  # pragma: no cover
    import timeit as ti
    tree_1 = BST([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    tree_2 = BST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    tree_3 = BST([5, 6, 4, 7, 3, 8, 2, 9, 1, 10])

    time_1 = ti.timeit("tree_1.search(5)", setup="from __main__ import tree_1")
    time_2 = ti.timeit("tree_2.search(5)", setup="from __main__ import tree_2")
    time_3 = ti.timeit("tree_3.search(8)", setup="from __main__ import tree_3")

    print('Negatively skewed tree search time: ', time_1)
    print('Positively skewed tree search time: ', time_2)
    print('Balanced tree search time: ', time_3)
