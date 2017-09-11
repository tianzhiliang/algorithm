import sys

adl1 = {0:[2,4],1:[2,5],2:[0,1],3:[4,5,6],4:[0,3],5:[1,3],6:[3]}
adl2 = {0:[2,4],1:[2],2:[0,1,5],3:[4],4:[0,3,6],5:[2],6:[4]}
adl3 = {0:[2,4],1:[2,7,9,10],2:[0,1,5],3:[4,16],4:[0,3,6],5:[2,11,15],6:[4,17,18],7:[],9:[],10:[],11:[],17:[],15:[19,20],16:[20],18:[23],20:[21],23:[24],19:[],21:[],24:[]}
tree1 = {0:[2,4],1:[7,9],2:[1,5],3:[16,-1],4:[3,6],5:[11,15],6:[17,18],15:[19,20],16:[22,-1],18:[23,-1],20:[21,-1],23:[-1,24]}

def go_pre_order_traverse(tree):
    pre_order_traverse(tree, 0)
    
def pre_order_traverse(tree, node): # tree
    if not node in tree or len(tree[node]) == 0:
        print node
        return

    print node
    if tree[node][0] != -1:
        pre_order_traverse(tree, tree[node][0])
    if tree[node][1] != -1:
        pre_order_traverse(tree, tree[node][1])

    return

if "__main__" == __name__:
    go_pre_order_traverse(tree1)
