# данный файл содержит методы проверки вершин на соответствие системным вызовам
# проверки осуществляются иерархично, от более строгого условия системного вызова к менее
# пример: setsid требует и группы, и сессии. setpgid - только группы. 
# Вывод: сначала проверить setsid, потом - setpgid.
# каждому системному вызову соответствует правило
# бесконтекстные правила записываются в виде множества проверок атрибутов на ==, !=.
# бесконтекстные правила записываются в виде множества операций поиска по ветви и дереву, а также проверок атрибутов на ==, !=
# *разложение на такие проверки мотивирует дополнительно рассмотреть построение решения в грамматиках с контекстами (Охотин, Бараш)
# здесь используется простая проверка, без грамматик с контекстами.
# имена контекстных частей вызовов <name>_context(...)
from proc import *

def fork(proc_entry):
        proc_entry.call = 'fork'
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


def check_cf(child, parent, node_arr):
        
        def compose_rules_cf():
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
                return headers, hierarch_list

        def select_from(allias, child, parent):
                if allias[0] == 'child':
                        return child
                else:
                        return parent

        headers, hierarch_list = compose_rules_cf()
        for idx, rule in enumerate[hierarch_list]:
                corr = True
                for c in rule:
                        if all( getattr(select_from(x.split('.')[0]),(x.split('.')[1])) == getattr(select_from(c.values[0].split('.')[0]),(c.values[0].split('.')[1]))  for x in c.values):
                                if c.key == 'eq':
                                        corr = True
                                elif c.key =='neq':
                                        corr = False
                                        break
                        else:
                                if c.key == 'neq':
                                        corr = True
                                elif c.key =='eq':
                                        corr = False
                                        break
                if corr == True:
                        return apply_rule[headers[idx]](child, parent, node_arr)
               
def fork(child, parent=None):
        child.call = 'fork'
        return node_arr

def setsid(child, parent, node_arr):
        node_arr.insert(0, proc(child.p, parent.g, parent.s, child.pp)) # forked node by design
        node_arr[-1].call='setsid'
        return node_arr

def setpgid(child, parent, node_arr):
        node_arr.insert(0, proc(child.p, parent.g, child.s, child.pp)) # forked node by design
        node_arr[-1].call='setpgid'
        return node_arr
