import os, sys
_base_path = os.getcwd()
parentdir_of_file = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(parentdir_of_file)

def find_node(node, pid=1, s=None):
    if not s:  # pid_lookup
        if node.proc.p == pid:
            return node
        else:
            for item in node.children:
                res=find(item, pid)
                if res:
                    return item

#basic process description
class ProcessEntry(object):
    def __init__(self, p, g, s):
        self.p = p
        self.g = g
        self.s = s

### It seems good to set any tree as betatree        

#node: process + some constraints + children == tree
#so node is a tree itself
class Node(object):
    def __init__(self, p, g, s, pp=None, children=[]):
        self.proc = ProcessEntry(p,g,s)
        self.children = children
        self.parent = pp


    def __getitem__(self, key):
        return find(self,key)
        pass

    def __setitem__(self, key, value):
        pass

    def __repr__(self):
        return "Node({p}, {g}, {s}, {pp})".format(p=self.proc.p, g=self.proc.g, s=self.proc.s, pp=self.parent)

#initial or ordinary trees


# auxiliary trees for recursion
class BNode:
    def __init__(self, node):
        self.topnode = node
        self.footnode = node

def test():
    print(find_node(Node(1,1,1),pid=2))


#test:
#test
test()
