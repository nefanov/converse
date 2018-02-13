class ProcessEntry(object):
    def __init__(self, p, g, s):
        self.p = p
        self.g = g
        self.s = s


class Node(object):
    def __init__(self, p, g, s, pp=None, children=[]):
        self.proc = ProcessEntry(p,g,s)
        self.children = children
        self.parent = pp
