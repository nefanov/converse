# requires networkx 1.11

import networkx as nx

def hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, 
                  pos = None, parent = None):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node of current branch
       width: horizontal space allocated for this branch - avoids overlap with other branches
       vert_gap: gap between levels of hierarchy
       vert_loc: vertical location of root
       xcenter: horizontal location of root
       pos: a dict saying where all nodes go if they have been assigned
       parent: parent of this branch.'''
    if pos == None:
        pos = {root:(xcenter,vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = G.neighbors(root)
#    if parent != None:   #this should be removed for directed graphs.
#        neighbors.remove(parent)  #if directed, then parent not in neighbors.
    if len(neighbors)!=0:
        dx = width/len(neighbors) 
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G,neighbor, width = dx, vert_gap = vert_gap, 
                                vert_loc = vert_loc-vert_gap, xcenter=nextx, pos=pos, 
                                parent = root)
    return pos


import matplotlib.pyplot as plt
G=nx.DiGraph()
#G.add_edges_from([(1,2), (1,3), (1,4), (2,5), (2,6), (2,7), (3,8), (3,9), (4,10),
#                  (5,11), (5,12), (6,13)])

# А лучше сдедать мапу labels - номер: '1 1 1'
edges = [1,2,3,4]
labels = {1:'1 1 1', 2:'2 1 1', 3:'3 1 1', 4:'4 4 4'}

G.add_edges_from([(1,2),(1,3), (3,4)])
pos = hierarchy_pos(G,1)
nx.draw_networkx_edge_labels(G,pos, 
    {
        (1,2):"fork()", (1,3):"fork()"
    },
    label_pos=0.5, font_size=18, font_color='k',
)
nx.draw(G, pos=pos, labels=labels, node_size=2500, node_color='yellow',font_size=18 ,with_labels=True)

plt.savefig('hierarchy.png')

print(pos)
