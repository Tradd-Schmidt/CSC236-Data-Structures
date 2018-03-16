# Binary Search Tree


class BstNode:

    def __init__(self, data, scope):
        self.data = data
        self.left = None
        self.right = None
        self.scope = scope


def GetNewNode(data):
    newNode = BstNode(data)
    return newNode


def insert(head, data):

    if head == None:
        head = GetNewNode(data)

    elif data <= head.data:
        head.left = insert(head.left, data)

    else:
        head.right = insert(head.right, data)

    return head


def main():
    head = None
    head = insert(head, 6)
    head = insert(head, 4)
    head = insert(head, 7)
    head = insert(head, 10)

main()

