import psutil
import collections
import sys
import os

_base_path = os.getcwd()
parentdir_of_file = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(parentdir_of_file)

from grammar.types import *

# process_list
def process_list():
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        except psutil.NoSuchProcess:
            pass
        else:
            print(pinfo)
    return pinfo

# print tree recursively
def print_tree(node, tree, indent='  '):
    pgid=sid=1
    try:
        name = psutil.Process(node).name()
        pgid = os.getpgid(psutil.Process(node).pid)
        sid = os.getsid(psutil.Process(node).pid)
    except psutil.Error:
        name = "?"
    print(name, node, sid, pgid)
    if node not in tree:
        return
    children = tree[node][:-1]
    for child in children:
        sys.stdout.write(indent + "|- ")
        print_tree(child, tree, indent + "| ")
    child = tree[node][-1]
    sys.stdout.write(indent + "`_ ")
    print_tree(child, tree, indent + "  ")

# make pstree as data structure
# now this is a dict of lists: 'ppid': [pids]
def get_pstree():
    tree = collections.defaultdict(list)
    for p in psutil.process_iter():
        try:
            tree[p.ppid()].append(p.pid)
        except (psutil.NoSuchProcess, psutil.ZombieProcess):
            pass
    # on systems supporting PID 0, PID 0's parent is usually 0
    if 0 in tree and 0 in tree[0]:
        tree[0].remove(0)
    print_tree(min(tree), tree)
    return tree


if __name__ == '__main__':
    get_pstree()
