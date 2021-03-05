class Node:
    def __init__(self):
        self.parent = 0
        self.children = []

    def __str__(self):
        return "parent: {}, children: {}".format(self.parent, self.children)


def main():
    n = int(input())
    pp = list(map(int, input().split(" ")))
    nodes = [Node() for _ in range(n)]
    for i, p in enumerate(pp):
        nodes[i+1].parent = p
    for i in range(n):
        for j in range(i + 1, n):
            if i + 1 == nodes[j].parent:
                nodes[i].children.append(i + 1)
    for node in nodes:
        print(node)


if __name__ == '__main__':
    main()
