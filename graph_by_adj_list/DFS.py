import sys

adl1 = {0:[2,4],1:[2,5],2:[0,1],3:[4,5,6],4:[0,3],5:[1,3],6:[3]}
adl2 = {0:[2,4],1:[2],2:[0,1,5],3:[4],4:[0,3,6],5:[2],6:[4]}
adl3 = {0:[2,4],1:[2,7,9,10],2:[0,1,5],3:[4,16],4:[0,3,6],5:[2,11,15],6:[4,17,18],7:[],9:[],10:[],11:[],17:[],15:[19,20],16:[20],18:[23],20:[21],23:[24],19:[],21:[],24:[]}
tree1 = {0:[2,4],1:[7,9],2:[1,5],3:[16,-1],4:[3,6],5:[11,15],6:[17,18],15:[19,20],16:[22,-1],18:[23,-1],20:[21,-1],23:[-1,24]}

def DFS(adl, node, used):
    if used[node] == 1:
        return

    print node
    used[node] = 1

    for child in adl[node]:
        if used[child] == 1:
            continue
        DFS(adl, child, used)

def go_DFS(adl):
    root = 0
    used = [0 for i in range(1000)]
    DFS(adl, root, used)

if "__main__" == __name__:
    go_DFS(adl1)
    print ""
    go_DFS(adl2)
    print ""
    go_DFS(adl3)
    print ""
