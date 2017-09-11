import sys

adj1 = [[0,0,1,0,1,0,0],[0,0,1,0,0,1,0],[1,1,0,0,0,0,0],[0,0,0,0,1,1,1],[1,0,0,1,0,0,0],[0,1,0,1,0,0,0],[0,0,0,1,0,0,0]]
adj2 = [[0,0,1,0,1,0,0],[0,0,1,0,0,0,0],[1,1,0,0,0,1,0],[0,0,0,0,1,0,0],[1,0,0,1,0,0,1],[0,0,1,0,0,0,0],[0,0,0,0,1,0,0]]

def DFS(adj, node, used):
    if used[node] == 1:
        return
        
    print node
    used[node] = 1

    nodesize = len(adj)
    for child in range(nodesize):
        if adj[node][child] == 0:
            continue
        if used[child] == 1:
            continue
        DFS(adj, child, used)
    return

def go_DFS(adj):
    root = 0
    used = [0 for i in range(len(adj))]
    DFS(adj, root, used)

def DFS_nore(adj):
    stack = []
    dim = len(adj)
    used = [0 for i in range(dim)]
    
    root = 0
    used[root] = 1
    print root
    stack.append(root)
    need_back = True

    while len(stack) != 0:
        if need_back:
            tail = stack.pop(len(stack))
        need_back = True
        for child in adj[tail]:
            if adj[tail][child] == 0:
                continue
            if used[child] == 1:
                continue

            need_back = False
            print child
            stack.append(child)
            used[child] = 1

        if need_back:
            stack.pop(len(stack))
     

if "__main__" == __name__:
    go_DFS(adj1)
    print ""
    go_DFS(adj2)
    print ""
