import sys

adj1 = [[0,0,1,0,1,0,0],[0,0,1,0,0,1,0],[1,1,0,0,0,0,0],[0,0,0,0,1,1,1],[1,0,0,1,0,0,0],[0,1,0,1,0,0,0],[0,0,0,1,0,0,0]]
adj2 = [[0,0,1,0,1,0,0],[0,0,1,0,0,0,0],[1,1,0,0,0,1,0],[0,0,0,0,1,0,0],[1,0,0,1,0,0,1],[0,0,1,0,0,0,0],[0,0,0,0,1,0,0]]

def go_BFS(adj):
    nodesize = len(adj)
    used = [0 for i in range(nodesize)]
    queue = []

    root = 0
    queue.append(root)
    print root
    used[root] = 1

    while len(queue) != 0:
        head = queue.pop(0)
        for child in range(nodesize):
            if adj[head][child] == 0:
                continue
            if used[child] == 1:
                continue
                
            queue.append(child)
            print child
            used[child] = 1
 
def BFS_re(adj, node, used, queue):
    nodesize = len(adj)

    if used[node] == 1:
        return

    print node
    used[node] = 1

    for child in range(nodesize):
        if adj[node][child] == 0:
            continue
        if used[child] == 1:
            continue

        queue.append(child)
            
if "__main__" == __name__:
    go_BFS(adj1)
    print ""
    go_BFS(adj2)
    print ""
