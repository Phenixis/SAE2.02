def dfs_path(g, start, end) -> list:
    result = []
    pred = dict()
    pred[start] = None
    stack = []
    remaining = list(g.nodes)
    stack.append(start)
    remaining.remove(start)
    found = False
    current = None
    while stack and not found:
        current = stack.pop()
        if current == end:
            found = True
        for n in g.neighbors(current):
            if n in remaining:
                stack.append(n)
                if n not in pred:
                    pred[n] = current
                remaining.remove(n)
    if found:
        while current:
            result = [current] + result
            current = pred[current]
        return result
    return []
