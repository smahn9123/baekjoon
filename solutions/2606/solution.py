import sys


class Node:

    def __init__(self, i: int):
        self.i: int = i
        self.nodes: list[Node] = []
        self.infested: bool = False


n = int(next(sys.stdin))
nodes = [Node(i) for i in range(n + 1)]

for connect in sys.stdin.readlines()[1:]:
    a, b = map(int, connect.split())
    node_a, node_b = nodes[a], nodes[b]
    if node_b not in node_a.nodes:
        node_a.nodes.append(node_b)
    if node_a not in node_b.nodes:
        node_b.nodes.append(node_a)


def infest_dfs(node: Node):
    node.infested = True
    for neighbor_node in node.nodes:
        if not neighbor_node.infested:
            infest_dfs(neighbor_node)


infest_dfs(nodes[1])
print(sum(1 for node in nodes[2:] if node.infested is True))
