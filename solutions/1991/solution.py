from dataclasses import dataclass, field
from typing import Optional, Dict, List


@dataclass
class Node:
    value: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None


@dataclass
class BinaryTree:
    root: Node
    preorder_list: List[str] = field(default_factory=list)
    inorder_list: List[str] = field(default_factory=list)
    postorder_list: List[str] = field(default_factory=list)

    def traverse_preorder(self, node: Node):
        self.preorder_list.append(node.value)
        if node.left:
            self.traverse_preorder(node.left)
        if node.right:
            self.traverse_preorder(node.right)

    def traverse_inorder(self, node: Node):
        if node.left:
            self.traverse_inorder(node.left)
        self.inorder_list.append(node.value)
        if node.right:
            self.traverse_inorder(node.right)

    def traverse_postorder(self, node: Node):
        if node.left:
            self.traverse_postorder(node.left)
        if node.right:
            self.traverse_postorder(node.right)
        self.postorder_list.append(node.value)

    def traverse_all(self):
        self.traverse_preorder(self.root)
        self.traverse_inorder(self.root)
        self.traverse_postorder(self.root)


nodes: Dict[str, Node] = {}

n = int(input())
for _ in range(n):
    parent, left_child, right_child = input().split()

    if parent in nodes:
        node = nodes[parent]
    else:
        node = Node(value=parent)
        nodes[parent] = node

    if left_child != ".":
        left_child_node = Node(value=left_child, left=None, right=None)
        node.left = left_child_node
        nodes[left_child] = left_child_node

    if right_child != ".":
        right_child_node = Node(value=right_child, left=None, right=None)
        node.right = right_child_node
        nodes[right_child] = right_child_node

bt = BinaryTree(root=nodes["A"])
bt.traverse_all()
print("".join(bt.preorder_list))
print("".join(bt.inorder_list))
print("".join(bt.postorder_list))
