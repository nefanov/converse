
def fork(proc_entry):
        proc_entrt.call = 'fork'
        return proc_entry

def setsid()
        pass

def setpgid()
        pass

apply_rule = {
        'fork':fork,
        'setsid':setsid,
        'setpgid':setpgid
}

def check_cf(child, parent):
        def select_from(allias, child, parent):
                if allias[0] == 'child':
                        return child
                else:
                        return parent
# rules list composing
        setsid_cont = []
        setpgid_cont = []
        fork_cont = []
        setsid_cont.append({'eq':['child.g','child.s', 'child.g']})
        setpgid_cont.append({'eq':['child.g','child.p']})
        setpgid_cont.append({'neq':['child.s','child.p']})

        fork_cont.append({'eq':['child.g','parent.g']})
        fork_cont.append({'eq':['child.s','parent.s']})
        headers=['setsid','setpgid','fork']
        hierarch_list = [setsid_cont, setpgid_cont, fork_cont]


        for idx, rule in enumerate[hierarch_list]:
                corr = True
                for c in rule:
                        if c.key == 'eq':
                                if all( getattr(select_from(x.split('.')[0]),(x.split('.')[1])) == getattr(select_from(c.values[0].split('.')[0]),(c.values[0].split('.')[1]))  for x in c.values):
                                        corr = True
                                else:
                                        corr = False
                                        break
                        if
                if corr == True:
                        return apply_rule[headers[idx]](child)
