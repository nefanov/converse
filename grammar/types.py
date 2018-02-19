import os, sys
_base_path = os.getcwd()
parentdir_of_file = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(parentdir_of_file)

from sys_util.pstree import process_list

#basic process description
class Node:
    def __init__(self, p, g, s):
        self.p = p
        self.g = g
        self.s = s

#initial or ordinary trees
class Tree:
    def __init__(self, node=Node(1,1,1), children=[]):
        self.node=node
        self.children=children

# auxiliary trees for recursion
class Btree:
    def __init__(self, node):
        self.topnode = node
        self.footnode = node