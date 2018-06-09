# see into splitting with: https://github.com/xolox/python-proc/blob/master/proc/tree.py
import psutil
import collections
import sys
import os
import glob

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
    fds=[]
    try:
        name = psutil.Process(node).name()
        pgid = os.getpgid(psutil.Process(node).pid)
        sid = os.getsid(psutil.Process(node).pid)
        fds = [] # list of results from file descriptors
       	fd_procfs = glob.glob('/proc/'+ str(psutil.Process(node).pid) + '/fd/*')
        for line in fd_procfs:
            try:
                with open('/proc/'+ str(psutil.Process(node).pid) + '/fdinfo/'+ line.split('/')[-1], 'rt+') as finfo:
                    liner = False
                    for l in finfo:
                        if l.split(':')[0] == 'flags':
                            val=l.replace(':',' ').replace('\t',' ').split(' ')[-1].replace('\n','')
                            fds.append({os.path.realpath(line):val})
                            liner = True
                    if liner ==False:
                        fds.append({os.path.realpath(line):'n/a'})

            except Exception as e:
                print(e)
                fds.append({os.path.realpath(line):'n/a'})
		
    except psutil.Error:
        name = "?"
    print(name, node, sid, pgid)
    for it in fds:
        print(it)
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
