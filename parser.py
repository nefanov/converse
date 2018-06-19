from proc import *
from reader import *
import sys, os
#from sortedcontainers import SortedList
"""
How to use sorted list:
>>> from sortedcontainers import SortedList
>>> l = SortedList()
>>> l.update([0, 4, 1, 3, 2])
>>> l.index(3)
3
>>> l.add(5)
>>> l[-1]

"""

def normalize_str(line):
	for idx in range(len(line)-1):
		if ((line[idx]).isdigit() and line[idx+1]=='[') or ((line[idx]).isdigit() and line[idx+1]==']') or (line[idx]=='[' and line[idx+1]==']') or ((line[idx+1]).isdigit() and line[idx]=='[') or ((line[idx+1]).isdigit() and line[idx]==']'):
			line=line[:idx+1]+' '+line[idx+1:]
	return line

class parser:
	def __init__(self, ord_list=list(), arglist=list()):
		self.idx = ord_list
		self.arglist = arglist


	def first_stage(self, raw_line, stack=stack(), start='0', dbg=False):
		raw_line = normalize_str(raw_line)
		line = raw_line.split(' ')
		current = start
		pos = 0
		stack.push(['<s>']) # root metadata
		stack.print_stack()
		while pos in range(len(line)):
			if (line[pos]).isdigit():
				cand = []
				for i in line[pos:pos+len(self.arglist)]:
					if not (i).isdigit():
						break
					else:
						cand.append(int(i))

				if len(cand)==len(self.arglist):
					stack.push(proc(cand[0],cand[1],cand[2],cand[3])) # automate it
					if dbg == True:
						print(stack[stack.sp-1])
					pos += len(self.arglist)
					metadata = stack.frame_get_metadata()
					metadata.append([{stack.bp-1:None},{stack.sp-1:cand[0]}])
					stack.frame_update_metadata(metadata)
					current = cand[0] # ? redundancy
				else:
					print("Parsing.error")
					if dbg==True:
						stack.print_stack()
						print('Candidate',cand)

						print("Position ", pos,line[pos],"in data ", line)
					sys.exit(1)
			if line[pos] =='[':
				stack.frame()
				stack.push([])
				pos +=1
			
			if line[pos]==']':
# parse, then unwind
# implicit left-to-right rules match: setsid, setpgid(self), fork
				for rule in cf_rules:
					pass
				stack.unwind()
				pos +=1



		if dbg==True:
			print("==============================\n\n1st stage is finished. Stack is:")
			stack.print_stack()


def test():
	p  = parser(arglist=['p','g','s','pp'])

	p.first_stage("1 1 1 0[5 4 3 1 [ ] 3 3 3 1 [ 4 4 3 3 [ ] 9 3 3 3 [ ] ] ]", dbg=True)

test()
