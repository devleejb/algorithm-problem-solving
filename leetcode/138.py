from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodeMap = {}
        nodeList = []
        copiedNodeList = []

        idx = 0
        while head:
            nodeMap[id(head)] = idx
            nodeList.append(head)
            copiedNodeList.append(Node(head.val))
            idx += 1
            head = head.next

        for i, node in enumerate(copiedNodeList):
            if i + 1 < len(copiedNodeList):
                node.next = copiedNodeList[i + 1]

            if nodeList[i].random:
                randomIdx = nodeMap[id(nodeList[i].random)]
                node.random = copiedNodeList[randomIdx]

        if copiedNodeList:
            return copiedNodeList[0]
        else:
            return None
