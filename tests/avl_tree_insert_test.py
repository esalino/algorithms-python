import unittest

from trees.avl_tree_insert import insert


class TestAvlTreeInsert(unittest.TestCase):
    def test_avl_tree_insert(self):
        root = None
        arr = [14, 25, 21, 10, 23, 7, 26, 12, 30, 16, 19]
        for i in arr:
            root = insert(root, i);

        test_string = self.create_test_string(root)
        self.assertEqual(test_string, "21:3,14:2,10:1,7:0,12:0,16:1,19:0,25:2,23:0,26:1,30:0")

    def create_test_string(self, node):
        if node is None:
            return None
        left = self.create_test_string(node.left)
        right = self.create_test_string(node.right)
        test_string = str(node.val) + ":" + str(node.ht)
        if left is not None:
            test_string = test_string + "," + left
        if right is not None:
            test_string = test_string + "," + right
        return test_string


if __name__ == '__main__':
    unittest.main()
