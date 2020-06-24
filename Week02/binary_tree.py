"""
Binary Tree Data Structure
"""
class BinaryTreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

def create_binary_tree(iterable = ()):
    """ Given in iterable, create a binary tree in level order
        Example: create_tree([0,1,2,3,4,5,6,7,8,9])

                ____0__
               /       \
            __1__       2
           /     \     / \
          3       4   5   6
         / \     /
        7   8   9
    """
    def insert(node, i):
        if i < len(iterable) and iterable[i] is not None:
            node = BinaryTreeNode(iterable[i])
            node.left = insert(node.left, 2 * i + 1)
            node.right = insert(node.right, 2 * i + 2)
        return node
    return insert(None, 0)

def print_binary_tree(root, index=False):
    """ Pretty-print the binary tree.
        Inspired by https://pypi.org/project/binarytree/
    """
    def build_tree_string(root, current, index=False, delimiter='-'):
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(current, delimiter, root.val)
        else:
            node_repr = str(root.val)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = \
            build_tree_string(root.left, 2 * current + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            build_tree_string(root.right, 2 * current + 2, index, delimiter)

        # Draw the branch connecting the current root node to the left sub-box
        # Pad the line with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root node
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root node to the right sub-box
        # Pad the line with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root repr positions
        return new_box, len(new_box[0]), new_root_start, new_root_end

    lines = build_tree_string(root, 0, index)[0]
    print('\n' + '\n'.join((line.rstrip() for line in lines)))
