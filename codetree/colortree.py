from collections import deque

root = []
nodes = {}

ROOT_PID = -1
resList = []


def create_node(mID, pID, color, maxDepth):
    return {
        "mID": mID,
        "pID": pID,
        "color": color,
        "maxDepth": maxDepth,
        "children": [],
    }


def check_depth_validity(mID, depth):
    if nodes[mID]["maxDepth"] <= depth:
        return False

    if nodes[mID]["pID"] == ROOT_PID:
        return True
    else:
        return check_depth_validity(nodes[mID]["pID"], depth + 1)


def add_node(mID, pID, color, maxDepth):
    global root

    node = create_node(mID, pID, color, maxDepth)

    if pID != ROOT_PID and (pID not in nodes):
        return
    elif pID != ROOT_PID and not check_depth_validity(pID, 1):
        return

    nodes[mID] = node

    if pID != ROOT_PID:
        nodes[pID]["children"].append(mID)
    else:
        root.append(node)


def change_color(mID, color):
    q = deque([mID])

    while q:
        targetMID = q.popleft()
        nodes[targetMID]["color"] = color

        for childNode in nodes[targetMID]["children"]:
            q.append(childNode)


def view_color(mID):
    resList.append(nodes[mID]["color"])


def dfs(mID):
    totalScore = 0
    scoreSet = set([nodes[mID]["color"]])
    for child in nodes[mID]["children"]:
        score, childScoreSet = dfs(child)
        totalScore += score
        scoreSet = scoreSet.union(childScoreSet)

    return (totalScore + len(scoreSet) ** 2, scoreSet)


def view_score():
    scoreSum = 0
    for r in root:
        score, _ = dfs(r["mID"])
        scoreSum += score
    resList.append(scoreSum)


Q = int(input())

for _ in range(Q):
    ops = list(map(int, input().split()))

    if ops[0] == 100:
        add_node(ops[1], ops[2], ops[3], ops[4])
    elif ops[0] == 200:
        change_color(ops[1], ops[2])
    elif ops[0] == 300:
        view_color(ops[1])
    elif ops[0] == 400:
        view_score()

for res in resList:
    print(res)
