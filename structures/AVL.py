class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_height(head: TreeNode | None):
    if head is None:
        return -1

    l = get_height(head.left)
    r = get_height(head.right)

    z = max(l, r) + 1

    return z


def get_balance(head: TreeNode | None) -> int:
    if head is None:
        return 0

    l = get_height(head.left)
    r = get_height(head.right)

    z = l - r

    return z


def print_tree(head: TreeNode | None):
    if head is None:
        print("None", end=", ")

    else:
        print(f"{head.val}", end=", ")
        print_tree(head.left)
        print_tree(head.right)


# if there is imbalance on left child of right subtree = left-right
# if there is imbalance on left child of left subtree = right
# if there is imbalance on right child of left subtree = right-left
# if there is imbalance on right child of right subtree = left
def balance_tree(tree: TreeNode, balance: int):
    if balance > 0:
        x = get_balance(tree.left)
        if x > 0:
            tree = right_rotation(tree)
        elif x < 0:
            tree.left = left_rotation(tree.left)
            tree = right_rotation(tree)
    elif balance < 0:
        x = get_balance(tree.right)
        if x < 0:
            tree = left_rotation(tree)
        elif x > 0:
            tree.right = right_rotation(tree.right)
            tree = left_rotation(tree)

    return tree


def insert(head: TreeNode | None, val: int):
    if head is None:
        return TreeNode(val)

    if val < head.val:
        head.left = insert(head.left, val)
    else:
        head.right = insert(head.right, val)

    balance = get_balance(head)
    if (balance > 1 or balance < -1):
        head = balance_tree(head, balance)
    return head


def find_in_order_predecessor(head: TreeNode):
    if head is None:
        return None

    r = find_in_order_predecessor(head.right)
    if r is None:
        return head.val
    else:
        return r


def delete(head: TreeNode | None, val: int):
    if head is None:
        return None

    if head.val == val:
        if head.left is None and head.right is None:
            return None
        elif head.left is None and head.right is not None:
            return head.right
        elif head.left is not None and head.right is None:
            return head.left
        else:
            in_order_predecessor = find_in_order_predecessor(head.left)
            head.val = in_order_predecessor
            head.left = delete(head.left, in_order_predecessor)

    elif val < head.val:
        head.left = delete(head.left, val)
    else:
        head.right = delete(head.right, val)

    balance = get_balance(head)
    if balance > 1 or balance < -1:
        head = balance_tree(head, balance)
    return head


def right_rotation(head: TreeNode):
    aux: TreeNode = head.left
    head.left = None
    aux2: TreeNode | None = aux.right

    head.left = aux2
    aux.right = head
    return aux


def left_rotation(head: TreeNode):
    aux: TreeNode = head.right
    head.right = None
    aux2: TreeNode | None = aux.left

    head.right = aux2
    aux.left = head
    return aux


def main():
    tree = None
    print("Add items to AVL")
    while True:
        try:
            x = input()
            if x == "x":
                y = input()
                y = int(y)
                tree = delete(tree, y)
                print_tree(tree)
                print('\n')
            else:
                x = int(x)
                tree = insert(tree, x)
                print_tree(tree)
                print('\n')
        except:
            print("Bye!")
            break


if __name__ == "__main__":
    main()
