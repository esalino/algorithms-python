# https://www.hackerrank.com/challenges/self-balancing-tree/problem

# the hackerrank test problems are based on height of a null node being -1 and
# a leaf being height 0 instead of the usual heights for null and leaf being 0 and 1


class Node:
    def __init__(self):
        self.val = None
        self.ht = None
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        n = Node()
        n.ht = 0
        n.val = val
        return n

    insert_and_balance_subtrees(root, val)
    # Still need to balance root
    root = balance_subtree(root)
    root.ht = get_height(root) + 1
    return root


def insert_and_balance_subtrees(node, val):
    if node is None:
        return node

    child = node.left if val < node.val else node.right
    new_child = insert_and_balance_subtrees(child, val)

    if new_child is None:
        new_node = Node()
        new_node.val = val
        new_node.ht = 0
        # If height is 0 it is now 1 otherwise same as it already was.
        if node.ht == 0:
            node.ht = 1

        if val < node.val:
            node.left = new_node
        else:
            node.right = new_node

        return node

    if val < node.val:
        node.left = balance_subtree(node.left)
    else:
        node.right = balance_subtree(node.right)

    node.ht = get_height(node) + 1;
    return node


def balance_subtree(node):
    balance = get_balance(node)
    if -2 < balance < 2:
        return node

    if balance == 2:
        child_balance = get_balance(node.left)
        if child_balance < 0:
            # left-right case which if we have will always comes before left-left case
            temp = node.left.right
            node.left.right = node.left.right.left
            temp.left = node.left
            node.left = temp

            node.left.left.ht = get_height(node.left.left)
            node.left.ht = get_height(node.left)
            node.ht = get_height(node)

        # left- left case
        temp = node.left
        node.left = node.left.right
        temp.right = node

        temp.left.ht = get_height(temp.left) + 1
        temp.right.ht = get_height(temp.right) + 1
        temp.ht = get_height(temp) + 1
        return temp

    else:
        child_balance = get_balance(node.right)
        if child_balance > 0:
            # right-left case which if we have will always comes before right-right case
            temp = node.right.left
            node.right.left = node.right.left.right
            temp.right = node.right
            node.right = temp

            node.right.right.ht = get_height(node.right.right)
            node.right.ht = get_height(node.right)
            node.ht = get_height(node)

        # right-right case
        temp = node.right
        node.right = node.right.left
        temp.left = node

        temp.right.ht = get_height(temp.right) + 1
        temp.left.ht = get_height(temp.left) + 1
        temp.ht = get_height(temp) + 1
        return temp


def get_balance(node):
    left_height = -1 if node.left is None else node.left.ht
    left_right = -1 if node.right is None else node.right.ht
    return left_height - left_right


def get_height(node):
    left_height = -1 if node.left is None else node.left.ht
    left_right = -1 if node.right is None else node.right.ht
    return max(left_height, left_right)
